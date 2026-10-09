"""Interactive explorer of the included investors: every value with the source and verbatim quote behind it.

    python -m investordb.cli explorer        -> docs/explorer.html (self-contained, opens offline)

The page shows the refined database (D38) when it exists, otherwise the frozen one, and for every record what
refinement changed. All text from web pages is HTML-escaped in the browser (it is data, never markup).
"""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

from investordb.evidence import domain
from investordb.money import parse_money, to_eur
from investordb.pipeline import total_capital
from investordb.refine import INVESTORS_REFINED, PROCESSED, _value, counted_deals, rebuild_all
from investordb.registries import core_name

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "explorer.html"


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _num(v: str) -> float | None:
    return float(v) if v not in ("", None) else None


def _eur(text: str | None, currency: str | None, on: str) -> tuple[float | None, bool]:
    """An amount as written ('nearly €55 million', 'přes 780 milionů Kč') in EUR, so amounts line up in one column.
    Returns (eur, approximate); ranges and amounts without a currency stay unconverted."""
    m = parse_money(text, currency)
    if not m or m.is_range:
        return None, False
    return round(to_eur(m, on)), m.approx or m.currency != "EUR"


def investor_view(row: dict, before: dict, merged: list[dict], on: str) -> dict:
    ok = [c for c in merged if c["auto_check"] == "ok"]
    counted = counted_deals(ok)
    deals: dict[str, dict] = {}
    for c in ok:
        if c["field"] != "investments" or c.get("attributed") == "0" or c.get("deal_context") == "exit":
            continue
        v = _value(c)
        company = str(v.get("company") or "").strip()
        if not company:
            continue
        key = core_name(company)
        d = deals.setdefault(key, {"company": company, "date": "", "round": "", "amount": "", "eur": None,
                                   "approx": False, "sources": []})
        if counted.get(key) is c:
            d["date"] = c["event_date"][:10]
            d["round"], d["amount"] = v.get("round") or "", v.get("amount") or ""
            d["eur"], d["approx"] = _eur(d["amount"], None, on)
        d["sources"].append({"url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"],
                             "published": c.get("published_date") or "", "tier": c["source_tier"],
                             "context": c.get("deal_context") or "", "refined": "verdict" in v,
                             "counted": counted.get(key) is c})
    cap = total_capital(ok, on)
    funds = []
    for c in ok:
        if c["field"] == "funds" or (c["field"] == "total_capital" and cap["method"] == "aum_stated"):
            v = _value(c)
            size = v.get("size") or v.get("amount") or ""
            eur, approx = _eur(size, v.get("currency"), on)
            funds.append({"name": v.get("name") or "AUM (spravovaný kapitál)", "size": size, "eur": eur,
                          "approx": approx, "status": v.get("status") or ("aum" if c["field"] == "total_capital" else ""),
                          "url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"],
                          "published": c.get("published_date") or "", "counted": any(c is k for k in cap["counted"])})
    profile = {}
    for field in ("sectors", "stages", "ticket", "investor_type", "hq_country", "identity"):
        c = next((c for c in ok if c["field"] == field), None)
        if c:
            profile[field] = {"url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"],
                              "published": c.get("published_date") or ""}
    return {
        "id": row["candidate_id"], "name": row["name"], "legal_name": row["legal_name"], "company_id": row["company_id"],
        "registry_url": row["registry_url"], "hq": row["hq_country"], "website": row["website"],
        "types": [t for t in row["investor_types"].split(",") if t],
        "sectors": [s for s in row["sectors"].split(",") if s], "stages": [s for s in row["stages"].split(",") if s],
        "ticket": [row["ticket_min"], row["ticket_max"]], "ticket_eur": [_num(row["ticket_min_eur"]), _num(row["ticket_max_eur"])],
        "capital": _num(row["total_capital_eur"]), "capital_method": row["capital_method"],
        "capital_note": row["capital_note"], "targets": row["funds_target"],
        "status": row["status"], "tier": row["tier"], "explanation": row["explanation"],
        "n_inv": int(row["n_investments"] or 0), "n_36m": int(row["n_investments_36m"] or 0),
        "last_date": row["last_investment_date"], "last_company": row["last_investment"],
        "before": {"capital": _num(before["total_capital_eur"]), "capital_method": before["capital_method"],
                   "last_date": before["last_investment_date"], "last_company": before["last_investment"],
                   "n_36m": int(before["n_investments_36m"] or 0), "tier": before["tier"], "status": before["status"]},
        "notes": [n for n in (row.get("refine_notes") or "").split("; ") if n],
        "deals": sorted(deals.values(), key=lambda d: d["date"] or "0", reverse=True),
        "funds": sorted(funds, key=lambda f: (not f["counted"], -(f["eur"] or 0))), "profile": profile,
    }


def build(as_of: date, meta: dict) -> dict:
    result = rebuild_all(as_of)
    on = as_of.isoformat()
    rows = result["rows"]
    investors = [investor_view(rows[cid], result["before"][cid], result["merged"][cid], on) for cid in sorted(rows)]
    return {"meta": {**meta, "as_of": on, "refined": INVESTORS_REFINED.exists() and bool(result["claims"])},
            "investors": sorted(investors, key=lambda r: r["name"].lower())}


def render(data: dict, standalone: bool = True) -> str:
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.replace("__DATA__", payload)
    if standalone:
        page = ('<!doctype html>\n<html lang="sk">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + page.replace("<!--BODY-->", "</head>\n<body>") + "\n</body>\n</html>\n")
    else:
        page = page.replace("<!--BODY-->", "")
    return page


def write(as_of: date, meta: dict, out: Path = OUT, artifact_out: Path | None = None) -> dict:
    data = build(as_of, meta)
    out.write_text(render(data), encoding="utf-8")
    if artifact_out:
        artifact_out.write_text(render(data, standalone=False), encoding="utf-8")
    return data


TEMPLATE = r"""<title>Databáza VC investorov CZ/SK</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Public+Sans:wght@400;500;600;700;800&display=swap">
<style>
/* Layout: a sortable ledger table of investors (left) and the evidence sheet of the selected investor (right);
   every list of numbers is a table with fixed, aligned columns; one column on phones.
   Type scale 13 / 14.5 / 16 / 18 / 24 / 32. Contrast: text >= 12:1, secondary >= 7:1, tertiary >= 4.8:1. */
:root {
  --paper: #e6eaf0; --sheet: #ffffff; --raised: #f4f6f9; --row-hover: #eef2f8; --ink: #0f1822; --ink-2: #364352; --ink-3: #566273;
  --rule: #d3dae3; --rule-strong: #a3b0bf;
  --accent: #1a44a3; --accent-soft: #e1e8f8; --on-accent: #ffffff;
  --ok: #145c38; --ok-soft: #d7ecdf; --warn: #7d4300; --warn-soft: #f8e6c6;
  --quote: #f1f4f8; --quote-rule: #a9b6c6; --shadow: 0 1px 2px rgba(15, 24, 34, .06), 0 4px 16px rgba(15, 24, 34, .06);
  --display: "Public Sans", "Segoe UI", system-ui, sans-serif; --body: "Public Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #0a0f15; --sheet: #131a23; --raised: #19222e; --row-hover: #1c2634; --ink: #f1f4f8; --ink-2: #c6d0dc; --ink-3: #9eabba;
  --rule: #2a3544; --rule-strong: #4a5a6d;
  --accent: #a6bfff; --accent-soft: #1f2d4a; --on-accent: #0a0f15;
  --ok: #86e0b1; --ok-soft: #14301f; --warn: #f5c477; --warn-soft: #3a2a10;
  --quote: #0f151d; --quote-rule: #4a5a6d; --shadow: none; color-scheme: dark } }
:root[data-theme="dark"] {
  --paper: #0a0f15; --sheet: #131a23; --raised: #19222e; --row-hover: #1c2634; --ink: #f1f4f8; --ink-2: #c6d0dc; --ink-3: #9eabba;
  --rule: #2a3544; --rule-strong: #4a5a6d;
  --accent: #a6bfff; --accent-soft: #1f2d4a; --on-accent: #0a0f15;
  --ok: #86e0b1; --ok-soft: #14301f; --warn: #f5c477; --warn-soft: #3a2a10;
  --quote: #0f151d; --quote-rule: #4a5a6d; --shadow: none; color-scheme: dark }
* { box-sizing: border-box }
body { margin: 0; background: var(--paper); color: var(--ink); font: 16px/1.5 var(--body); -webkit-font-smoothing: antialiased }
a { color: var(--accent); text-underline-offset: 3px; text-decoration-thickness: 1px }
a:hover { text-decoration-thickness: 2px }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; border-radius: 4px }
button, select, input { font: inherit; color: inherit }
.num { font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap }
.mono { font-family: var(--mono); font-variant-numeric: tabular-nums }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap }
.wrap { max-width: 1320px; margin: 0 auto; padding-inline: 16px; padding-block: 24px 48px }

/* page header */
.top { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 16px 40px; align-items: end; padding-bottom: 20px }
.eyebrow { font: 600 13px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--accent); margin: 0 0 10px }
h1 { font: 800 clamp(26px, 3.2vw, 32px)/1.15 var(--display); letter-spacing: -0.015em; margin: 0; text-wrap: balance }
.lede { color: var(--ink-2); margin: 10px 0 0; max-width: 64ch }
.stats { display: grid; grid-template-columns: repeat(3, minmax(120px, auto)); background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; box-shadow: var(--shadow) }
.stat { padding: 12px 18px; display: grid; gap: 2px }
.stat + .stat { border-left: 1px solid var(--rule) }
.stat b { font: 700 22px/1.2 var(--body); font-variant-numeric: tabular-nums }
.stat span { font-size: 13px; color: var(--ink-2) }
@media (max-width: 760px) { .top { grid-template-columns: minmax(0, 1fr) } .stats { grid-template-columns: repeat(3, minmax(0, 1fr)) } .stat { padding: 10px 12px } .stat b { font-size: 18px } }

/* toolbar: one row of equally tall controls */
.tools { display: grid; grid-template-columns: minmax(0, 1fr) auto auto auto; gap: 10px; align-items: stretch; padding: 14px; margin-bottom: 18px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; box-shadow: var(--shadow) }
.tools input[type=search], .tools select { height: 44px; padding: 0 14px; border: 1.5px solid var(--rule-strong); border-radius: 8px; background: var(--sheet); min-width: 0 }
.tools input[type=search]::placeholder { color: var(--ink-3) }
.seg { display: inline-flex; border: 1.5px solid var(--rule-strong); border-radius: 8px; overflow: hidden }
.seg button { border: 0; background: var(--sheet); color: var(--ink-2); padding: 0 16px; font-weight: 600; cursor: pointer; min-width: 52px }
.seg button + button { border-left: 1.5px solid var(--rule-strong) }
.seg button[aria-pressed=true] { background: var(--accent); color: var(--on-accent) }
.check { display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border: 1.5px solid var(--rule-strong); border-radius: 8px; cursor: pointer; white-space: nowrap; font-weight: 600; color: var(--ink-2) }
.check input { width: 18px; height: 18px; accent-color: var(--accent); margin: 0 }
.check:has(input:checked) { border-color: var(--accent); background: var(--accent-soft); color: var(--accent) }
@media (max-width: 900px) { .tools { grid-template-columns: minmax(0, 1fr) auto } .tools input[type=search] { grid-column: 1 / -1 } }
@media (max-width: 480px) { .tools { grid-template-columns: minmax(0, 1fr) } .seg { display: grid; grid-template-columns: repeat(3, 1fr) } }

/* two panes */
.grid { display: grid; grid-template-columns: minmax(0, 11fr) minmax(0, 13fr); gap: 20px; align-items: start }
@media (max-width: 1000px) { .grid { grid-template-columns: minmax(0, 1fr) } }
.panel { background: var(--sheet); border: 1px solid var(--rule); border-radius: 12px; box-shadow: var(--shadow); overflow: hidden }

/* investor ledger: header and rows share one column template, so every value sits under its heading */
.ledger { --cols: minmax(0, 1fr) 104px 108px 48px 64px }
.lhead, .row { display: grid; grid-template-columns: var(--cols); column-gap: 12px; align-items: center; padding: 0 16px }
.lhead { position: sticky; top: 0; z-index: 2; background: var(--raised); border-bottom: 2px solid var(--rule-strong); min-height: 44px }
.lhead button { border: 0; background: none; padding: 10px 0; font: 700 13px/1.2 var(--body); color: var(--ink-2); cursor: pointer; display: flex; gap: 4px; align-items: center; justify-content: flex-start; text-align: left }
.lhead button.r { justify-content: flex-end; text-align: right }
.lhead button.c { justify-content: center }
.lhead button:hover { color: var(--ink) }
.lhead button[aria-pressed=true] { color: var(--accent) }
.lhead .arr { font-size: 11px; width: 10px }
.rows { max-height: calc(100vh - 230px); overflow: auto }
@media (max-width: 1000px) { .rows { max-height: none } }
.row { width: 100%; min-height: 64px; border: 0; border-bottom: 1px solid var(--rule); background: none; text-align: left; cursor: pointer; padding-block: 10px; position: relative }
.row:last-child { border-bottom: 0 }
.row:hover { background: var(--row-hover) }
.row[aria-current=true] { background: var(--accent-soft) }
.row[aria-current=true]::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--accent) }
.row .nm { min-width: 0 }
.row .nm b { display: block; font: 600 16px/1.3 var(--body); overflow-wrap: anywhere }
.row .nm small { display: flex; flex-wrap: wrap; gap: 2px 10px; font-size: 13.5px; color: var(--ink-2); margin-top: 2px }
.row .nm small .m-date { display: none }
.row .nm small .ty { max-width: 100%; white-space: nowrap; overflow: hidden; text-overflow: ellipsis }
.chg-mark { color: var(--warn); font-weight: 600 }
.chg-mark::before { content: "●"; font-size: 9px; margin-right: 4px; vertical-align: 2px }
.row .v { font-size: 15px; color: var(--ink) }
.row .v.dim { color: var(--ink-3) }
.tier { justify-self: center; display: inline-grid; place-items: center; width: 34px; height: 28px; border-radius: 6px; font: 700 14px/1 var(--body); border: 1.5px solid var(--accent); color: var(--accent) }
.tier.B { border-color: var(--ink-3); color: var(--ink-2) }
.tier.R { border-color: var(--warn); color: var(--warn); width: auto; padding: 0 6px; font-size: 12px }
.empty { color: var(--ink-2); font-style: italic; padding: 18px 16px; margin: 0 }
@media (max-width: 640px) {
  .ledger { --cols: minmax(0, 1fr) 92px 44px }
  .ledger .c-date, .ledger .c-n36 { display: none }
  .row .nm small .m-date { display: inline }
}

/* evidence sheet */
.sheet { position: sticky; top: 12px; max-height: calc(100vh - 24px); overflow: auto }
@media (max-width: 1000px) { .sheet { position: static; max-height: none } }
/* the evidence sheet has its own deep-navy scheme, so it reads as a separate surface from the light list;
   every color inside it comes from these tokens (contrast of text on it: 5.7:1 or more in both themes) */
.sheet {
  --sheet: #14202e; --head: #1a2a3d; --raised: #1b2a3b; --row-hover: #213247; --ink: #f2f5f9; --ink-2: #c5cfdb; --ink-3: #9eabbb;
  --rule: #2b3b4f; --rule-strong: #4a5e76; --accent: #a9c1ff; --accent-soft: #243758; --on-accent: #0b1220; --edge: #3d6ae0;
  --ok: #8ae3b4; --ok-soft: #153629; --warn: #f6c87d; --warn-soft: #3d2d12; --quote: #0f1924; --quote-rule: #50657e;
  background: var(--sheet); color: var(--ink); color-scheme: dark; border: 1px solid #0b1520; border-top: 4px solid var(--edge) }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .sheet {
  --sheet: #1a2b45; --head: #203457; --raised: #22365a; --row-hover: #26406a; --ink: #f4f7fb; --ink-2: #cdd7e4; --ink-3: #a7b4c6;
  --rule: #2f4568; --rule-strong: #4f6a92; --accent: #b3caff; --accent-soft: #2c4572; --edge: #7d9cff;
  --ok: #90e6b9; --ok-soft: #173a2d; --warn: #f8cd86; --warn-soft: #433217; --quote: #132036; --quote-rule: #5a7398; border-color: #2f4568 } }
:root[data-theme="dark"] .sheet {
  --sheet: #1a2b45; --head: #203457; --raised: #22365a; --row-hover: #26406a; --ink: #f4f7fb; --ink-2: #cdd7e4; --ink-3: #a7b4c6;
  --rule: #2f4568; --rule-strong: #4f6a92; --accent: #b3caff; --accent-soft: #2c4572; --edge: #7d9cff;
  --ok: #90e6b9; --ok-soft: #173a2d; --warn: #f8cd86; --warn-soft: #433217; --quote: #132036; --quote-rule: #5a7398; border-color: #2f4568 }
.sh-head { position: sticky; top: 0; z-index: 3; background: var(--head); padding: 20px 24px 14px; border-bottom: 1px solid var(--rule) }
.sh-head h2 { font: 800 26px/1.2 var(--display); margin: 0; letter-spacing: -0.01em; text-wrap: balance }
.legal { display: flex; flex-wrap: wrap; gap: 4px 16px; margin-top: 6px; font-size: 14.5px; color: var(--ink-2) }
.legal code { font: 500 14.5px var(--mono); color: var(--ink) }
.banner { margin-top: 12px; padding: 10px 14px; border-radius: 8px; background: var(--warn-soft); color: var(--ink); font-size: 15px }
.sh-body { padding: 18px 24px 28px }
.kpis { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border: 1px solid var(--rule); border-radius: 10px; overflow: hidden }
.kpi { padding: 12px 14px; display: grid; gap: 2px; align-content: start; background: var(--raised) }
.kpi + .kpi { border-left: 1px solid var(--rule) }
.kpi .k { font-size: 13px; font-weight: 600; color: var(--ink-2) }
.kpi .v { font: 700 20px/1.25 var(--body); font-variant-numeric: tabular-nums; white-space: nowrap; overflow: hidden; text-overflow: ellipsis }
.kpi .s { font-size: 13px; color: var(--ink-2); overflow-wrap: anywhere }
@media (max-width: 640px) { .kpis { grid-template-columns: repeat(2, minmax(0, 1fr)) } .kpi:nth-child(3) { border-left: 0 } .kpi:nth-child(n+3) { border-top: 1px solid var(--rule) } }
.kv { display: grid; grid-template-columns: 128px minmax(0, 1fr); margin: 16px 0 0; border-top: 1px solid var(--rule) }
.kv dt, .kv dd { margin: 0; padding: 10px 0; border-bottom: 1px solid var(--rule) }
.kv dt { font-size: 14px; font-weight: 600; color: var(--ink-2); padding-right: 12px }
.kv dd { font-size: 15.5px }
.chips { display: flex; flex-wrap: wrap; gap: 6px }
.chip { display: inline-block; font: 600 13px/1.2 var(--body); padding: 4px 10px; border-radius: 999px; background: var(--raised); border: 1px solid var(--rule-strong); color: var(--ink-2); white-space: nowrap }
.chip.ok { background: var(--ok-soft); color: var(--ok); border-color: transparent }
.chip.warn { background: var(--warn-soft); color: var(--warn); border-color: transparent }
.chip.acc { background: var(--accent-soft); color: var(--accent); border-color: transparent }
section.blk { margin-top: 30px }
.blk-h { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; padding-bottom: 8px; margin-bottom: 0; border-bottom: 2px solid var(--ink) }
.blk-h h3 { font: 700 18px/1.3 var(--body); margin: 0 }
.blk-h .n { font-size: 14px; color: var(--ink-2); font-weight: 500 }
.blk-note { font-size: 14.5px; color: var(--ink-2); margin: 10px 0 0 }

/* data tables built from <details> rows: the summary is the row, the open part holds the quotes */
.dt { --cols: 1fr }
.dt-head, .dt-row > summary { display: grid; grid-template-columns: var(--cols); column-gap: 14px; align-items: center; padding: 0 10px }
.dt-head { min-height: 38px; background: var(--raised); border-bottom: 1px solid var(--rule-strong); font: 700 13px/1.2 var(--body); color: var(--ink-2) }
.dt-sub { padding: 14px 10px 6px; font: 700 13px/1.2 var(--body); color: var(--ink-2); border-bottom: 1px solid var(--rule) }
.dt-row { border-bottom: 1px solid var(--rule) }
.dt-row > summary { min-height: 48px; padding-block: 9px; cursor: pointer; list-style: none }
.dt-row > summary::-webkit-details-marker { display: none }
.dt-row > summary:hover { background: var(--row-hover) }
.dt-row[open] > summary { background: var(--accent-soft) }
.dt-row .strong { font-weight: 600; overflow-wrap: anywhere }
.dt-row .muted, .dt-head .muted { color: var(--ink-3) }
.dt-row .orig { display: block; font-size: 13px; color: var(--ink-2); font-weight: 400 }
.tog { justify-self: end; font-size: 13.5px; font-weight: 600; color: var(--accent); white-space: nowrap }
.tog::after { content: " ▾"; display: inline-block; transition: transform .15s }
.dt-row[open] .tog::after { transform: rotate(180deg) }
.dt-open { padding: 12px 10px 16px; display: grid; gap: 12px; background: var(--sheet) }
blockquote { margin: 0; padding: 10px 14px; background: var(--quote); border-left: 4px solid var(--quote-rule); border-radius: 0 6px 6px 0; font-size: 15.5px; line-height: 1.55; overflow-wrap: anywhere }
blockquote.counted { border-left-color: var(--accent) }
.meta { display: flex; flex-wrap: wrap; gap: 2px 14px; margin-top: 6px; font-size: 13.5px; color: var(--ink-2) }
.meta a { font-weight: 600 }
.funds { --cols: minmax(0, 1fr) 116px 150px 72px }
.deals { --cols: 100px minmax(0, 1fr) 96px 112px 76px }
.prof { --cols: 120px minmax(0, 1fr) 72px }
@media (max-width: 640px) {
  .funds { --cols: minmax(0, 1fr) 96px 64px } .funds .c-st { display: none }
  .deals { --cols: 92px minmax(0, 1fr) 64px } .deals .c-rd, .deals .c-amt { display: none }
}
.st-dot { display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 600 }
.st-dot::before { content: ""; width: 10px; height: 10px; border-radius: 50%; background: currentColor; flex: none }
.st-final_close, .st-aum { color: var(--ok) } .st-first_close { color: var(--accent) } .st-target { color: var(--warn) } .st- { color: var(--ink-3) }
.yes { color: var(--ok); font-weight: 700 }
.targets { margin-top: 12px; padding: 10px 14px; border-radius: 8px; background: var(--warn-soft); font-size: 15px }

/* before / after */
.cmp-wrap { margin-top: 12px; border: 1px solid var(--rule); border-radius: 10px; overflow-x: auto }
.cmp { width: 100%; border-collapse: collapse; font-size: 15px }
.cmp th, .cmp td { padding: 10px 12px; border-bottom: 1px solid var(--rule); text-align: left; vertical-align: top }
.cmp tr:last-child th, .cmp tr:last-child td { border-bottom: 0 }
.cmp thead th { background: var(--raised); font: 700 13px var(--body); color: var(--ink-2); border-bottom: 1px solid var(--rule-strong) }
.cmp tbody th { font-weight: 600; white-space: nowrap; width: 30% }
.cmp td { font-variant-numeric: tabular-nums; width: 35% }
.cmp td small { display: block; font-size: 13px; color: var(--ink-2); margin-top: 2px }
.cmp td.chg { background: var(--warn-soft); font-weight: 700 }
.cmp td.chg::after { content: "zmenené"; display: block; font: 600 12px var(--body); color: var(--warn); margin-top: 4px }
@media (max-width: 640px) { .cmp th, .cmp td { padding: 8px } .cmp tbody th { white-space: normal; width: 34% } .cmp td { width: 33% } .sh-head, .sh-body { padding-inline: 16px } }
.notes { margin: 12px 0 0; padding: 0; list-style: none; display: grid; gap: 6px }
.notes li { padding: 8px 12px; border-radius: 8px; background: var(--raised); font-size: 15px }
footer { margin-top: 28px; color: var(--ink-2); font-size: 14.5px; max-width: 82ch; line-height: 1.6 }
@media (prefers-reduced-motion: no-preference) { .row, .dt-row > summary { transition: background .12s } }
@media (prefers-reduced-motion: reduce) { .tog::after { transition: none } }
</style>
<!--BODY-->
<div class="wrap">
<header class="top">
  <div>
    <p class="eyebrow">Zadanie A · pilot</p>
    <h1>VC investori so sídlom v Česku a na Slovensku</h1>
    <p class="lede">Každá hodnota má zdroj, dátum a doslovnú citáciu, ktorú program overil na stránke zdroja. Vyberte investora v tabuľke a rozbaľte riadok, aby ste videli citácie.</p>
  </div>
  <div class="stats" id="stats"></div>
</header>
<div class="tools" role="search">
  <label class="sr" for="q">Hľadať</label>
  <input type="search" id="q" placeholder="Hľadať investora, sektor alebo portfóliovú firmu">
  <div class="seg" id="country" role="group" aria-label="Krajina sídla">
    <button type="button" data-v="" aria-pressed="true">Všetky</button><button type="button" data-v="CZ" aria-pressed="false">CZ</button><button type="button" data-v="SK" aria-pressed="false">SK</button>
  </div>
  <label class="sr" for="sector">Sektor</label>
  <select id="sector"><option value="">Všetky sektory</option></select>
  <label class="check"><input type="checkbox" id="onlychg"> Len zmenené spresnením</label>
</div>
<div class="grid">
  <section class="panel ledger" aria-label="Investori">
    <div class="lhead" id="lhead"></div>
    <div class="rows" id="list"></div>
  </section>
  <article class="panel sheet" id="sheet" aria-live="polite"></article>
</div>
<footer id="foot"></footer>
</div>
<script>
const DATA = __DATA__;
const SECTOR = {ai_data:"AI a dáta",enterprise_saas:"B2B SaaS",fintech_insurtech:"fintech",health_digital:"digitálne zdravie",life_sciences_medtech:"life sciences",deeptech_hardware:"deeptech",cleantech_energy:"cleantech",mobility_logistics:"mobilita",consumer_ecommerce:"spotrebiteľ",edtech:"edtech",proptech_construction:"proptech",agri_food:"agri/food",cybersecurity:"kyberbezpečnosť",media_gaming:"médiá/hry",industry_manufacturing:"priemysel",iot_telecom:"IoT",hr_worktech:"HR tech",travel_hospitality:"cestovanie",govtech_legaltech:"govtech",defense_space:"obrana/vesmír",sector_agnostic:"bez sektorového zamerania"};
const STAGE = {pre_seed:"pre-seed",seed:"seed",series_a:"séria A",series_b_plus:"séria B+",growth:"growth",buyout:"buyout"};
const TYPE = {vc:"VC",cvc:"korporátny VC",public_vc:"verejný VC",pe:"PE",real_estate:"nehnuteľnosti",angel_network:"sieť angel investorov",family_office:"family office"};
const STATUS = {final_close:"uzavretý fond", first_close:"prvé uzavretie", target:"len cieľ", aum:"uvedené AUM", "":"stav neuvedený"};
const TIER_SRC = {T1:"register / regulátor", T2:"web investora", T3:"tlač"};
const PROFILE = {sectors:"Sektory", stages:"Štádiá", ticket:"Tiket", investor_type:"Typ", hq_country:"Sídlo", identity:"Identita"};
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = u => /^https?:\/\//i.test(u || "") ? u : "";
const link = (u, label) => safeUrl(u) ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(label || u)}</a>` : esc(label || "");
const eur = (v, approx) => v == null ? "–" : (approx ? "≈ " : "") + (v >= 1e6 ? (v/1e6).toLocaleString("sk", {minimumFractionDigits: 1, maximumFractionDigits: 1}) + " mil. €" : Math.round(v/1e3).toLocaleString("sk") + " tis. €");
const method = m => !m ? "" : m === "aum_stated" ? "uvedené AUM" : (k => k ? `súčet ${k[1]} ${k[1] === "1" ? "fondu" : "fondov"}` : m)(m.match(/sum_of_(\d+)_closed_funds/));
const arrow = t => esc(t).replace(/ -&gt; /g, " → ");
const plural = (n, one, few, many) => n === 1 ? one : n >= 2 && n <= 4 ? few : many;
const COLS = [
  {key: "name", label: "Investor", cls: "", cmp: (a, b) => a.name.localeCompare(b.name, "sk")},
  {key: "capital", label: "Kapitál", cls: "r", cmp: (a, b) => (b.capital ?? -1) - (a.capital ?? -1)},
  {key: "last", label: "Posl. obchod", cls: "c-date", cmp: (a, b) => (b.last_date || "").localeCompare(a.last_date || "")},
  {key: "n36", label: "36 m", cls: "r c-n36", title: "Investície za posledných 36 mesiacov", cmp: (a, b) => b.n_36m - a.n_36m},
  {key: "tier", label: "Úroveň", cls: "c", title: "Úroveň dôkazov A / B", cmp: (a, b) => (a.tier || "Z").localeCompare(b.tier || "Z")},
];
let state = {q: "", country: "", sector: "", onlyChg: false, sort: "name", sel: null};
try { const s = JSON.parse(localStorage.getItem("investor-explorer") || "{}"); if (COLS.some(c => c.key === s.sort)) state.sort = s.sort; } catch (e) {}

const invs = DATA.investors;
const m = DATA.meta;
const sectors = [...new Set(invs.flatMap(i => i.sectors))].sort((a, b) => (SECTOR[a]||a).localeCompare(SECTOR[b]||b, "sk"));
document.getElementById("sector").innerHTML += sectors.map(s => `<option value="${esc(s)}">${esc(SECTOR[s]||s)}</option>`).join("");
document.getElementById("stats").innerHTML =
  `<div class="stat"><b>${invs.filter(i => i.status === "INCLUDED").length}</b><span>zaradených investorov</span></div>` +
  (m.precision ? `<div class="stat"><b>${esc(m.precision)}</b><span>správne zaradených</span></div>` : "") +
  `<div class="stat"><b>${esc(m.as_of.split("-").reverse().join(". ").replace(/^0/, ""))}</b><span>${m.refined ? "stav po spresnení" : "zmrazená verzia"}</span></div>`;
document.getElementById("foot").innerHTML = esc(m.footer || "");

const changed = i => i.notes.length > 0 || i.status !== "INCLUDED";
function matches(i) {
  const q = state.q.trim().toLowerCase();
  if (state.country && i.hq !== state.country) return false;
  if (state.sector && !i.sectors.includes(state.sector)) return false;
  if (state.onlyChg && !changed(i)) return false;
  if (!q) return true;
  return [i.name, i.legal_name, i.company_id, ...i.sectors.map(s => SECTOR[s] || s), ...i.deals.map(d => d.company)].join(" ").toLowerCase().includes(q);
}
function renderHead() {
  document.getElementById("lhead").innerHTML = COLS.map(c => `<button type="button" class="${c.cls}" data-sort="${c.key}" aria-pressed="${state.sort === c.key}"${c.title ? ` title="${esc(c.title)}"` : ""}>${c.label}<span class="arr" aria-hidden="true">${state.sort === c.key ? (c.key === "name" ? "▲" : "▼") : ""}</span></button>`).join("");
}
function renderList() {
  const list = invs.filter(matches).sort(COLS.find(c => c.key === state.sort).cmp);
  if (!list.some(i => i.id === state.sel)) state.sel = list[0]?.id || null;
  renderHead();
  document.getElementById("list").innerHTML = list.length ? list.map(i => `
    <button type="button" class="row" data-id="${esc(i.id)}" aria-current="${i.id === state.sel}">
      <span class="nm"><b>${esc(i.name)}</b><small><span class="ty" title="${esc(i.types.map(t => TYPE[t] || t).join(", "))}">${esc(i.hq)} · ${esc(i.types.map(t => TYPE[t] || t).join(", "))}</span><span class="m-date">obchod ${esc(i.last_date || "–")}</span>${changed(i) && m.refined ? '<span class="chg-mark">spresnené</span>' : ""}</small></span>
      <span class="v num${i.capital == null ? " dim" : ""}">${eur(i.capital)}</span>
      <span class="v mono c-date">${esc(i.last_date || "–")}</span>
      <span class="v num c-n36">${i.n_36m}</span>
      <span class="tier ${i.status === "INCLUDED" ? esc(i.tier) : "R"}" title="${i.status === "INCLUDED" ? "Úroveň dôkazov " + esc(i.tier) : "Na ručnú kontrolu"}">${i.status === "INCLUDED" ? esc(i.tier) : "kontrola"}</span>
    </button>`).join("") : `<p class="empty">Žiadny investor nevyhovuje filtru.</p>`;
  renderSheet();
}
function quotes(list) {
  return list.map(s => `<div><blockquote class="${s.counted ? "counted" : ""}">${esc(s.quote)}</blockquote>
    <div class="meta"><span>${link(s.url, s.domain)}</span>${s.published ? `<span>publikované ${esc(s.published)}</span>` : ""}${s.tier ? `<span>${esc(TIER_SRC[s.tier] || s.tier)}</span>` : ""}${s.context ? `<span>${s.context === "deal" ? "správa o obchode" : "len zmienka – dátum sa nepočíta"}</span>` : ""}${s.refined ? "<span>zo spresnenia</span>" : ""}</div></div>`).join("");
}
function fundRows(i) {
  if (!i.funds.length) return `<p class="empty">Zdroje veľkosť fondov neuvádzajú.</p>`;
  return `<div class="dt funds"><div class="dt-head"><span>Fond</span><span class="num">Suma v EUR</span><span class="c-st">Stav · v kapitáli</span><span></span></div>
    ${i.funds.map(f => `<details class="dt-row"><summary>
      <span class="strong">${esc(f.name)}<span class="orig">pôvodne: ${esc(f.size || "neuvedené")}</span></span>
      <span class="num">${eur(f.eur, f.approx)}</span>
      <span class="c-st"><span class="st-dot st-${esc(f.status)}">${esc(STATUS[f.status] ?? f.status)}</span><span class="orig">${f.counted ? '<span class="yes">✓ započítané</span>' : "nezapočítané"}</span></span>
      <span class="tog">citácia</span></summary>
      <div class="dt-open">${quotes([{...f, tier: "", context: ""}])}</div></details>`).join("")}</div>`;
}
function dealRows(list) {
  return list.map(d => `<details class="dt-row"><summary>
      <span class="mono${d.date ? "" : " muted"}">${esc(d.date || "bez dátumu")}</span>
      <span class="strong">${esc(d.company)}</span>
      <span class="c-rd">${d.round && d.round !== "unknown" ? esc(STAGE[d.round] || d.round) : '<span class="muted">–</span>'}</span>
      <span class="num c-amt">${d.eur != null ? eur(d.eur, d.approx) : (d.amount ? `<span class="muted">${esc(d.amount)}</span>` : '<span class="muted">–</span>')}</span>
      <span class="tog">${d.sources.length} ${plural(d.sources.length, "zdroj", "zdroje", "zdrojov")}</span></summary>
      <div class="dt-open">${quotes(d.sources)}</div></details>`).join("");
}
function renderSheet() {
  const i = invs.find(x => x.id === state.sel);
  const el = document.getElementById("sheet");
  if (!i) { el.innerHTML = `<p class="empty">Vyberte investora v tabuľke.</p>`; return; }
  const b = i.before;
  const ticket = i.ticket_eur[0] || i.ticket_eur[1] ? `${eur(i.ticket_eur[0])} – ${eur(i.ticket_eur[1])}` : '<span class="muted">neuvedené</span>';
  const dated = i.deals.filter(d => d.date), undated = i.deals.filter(d => !d.date);
  const cmpRows = [
    ["Celkový kapitál", `${eur(b.capital)}<small>${esc(method(b.capital_method) || "neuvedené")}</small>`, `${eur(i.capital)}<small>${esc(method(i.capital_method) || "neuvedené")}</small>`, (b.capital ?? null) !== (i.capital ?? null)],
    ["Posledný obchod", `${esc(b.last_date || "–")}<small>${esc(b.last_company)}</small>`, `${esc(i.last_date || "–")}<small>${esc(i.last_company)}</small>`, b.last_date !== i.last_date],
    ["Investície za 36 mes.", b.n_36m, i.n_36m, b.n_36m !== i.n_36m],
    ["Úroveň dôkazov", b.tier || "–", i.status === "INCLUDED" ? (i.tier || "–") : "na kontrolu", b.tier !== i.tier || i.status !== "INCLUDED"]];
  el.innerHTML = `
    <header class="sh-head">
      <h2>${esc(i.name)}</h2>
      <div class="legal"><span>${esc(i.legal_name)}</span><span>IČO <code>${esc(i.company_id)}</code></span><span>${link(i.registry_url, "záznam v registri")}</span>${i.website ? `<span>${link(i.website, i.website.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""))}</span>` : ""}</div>
      ${i.status !== "INCLUDED" ? `<div class="banner"><b>Na ručnú kontrolu.</b> ${esc(i.explanation)}</div>` : ""}
    </header>
    <div class="sh-body">
      <div class="kpis">
        <div class="kpi"><span class="k">Celkový kapitál</span><span class="v">${eur(i.capital)}</span><span class="s">${esc(method(i.capital_method) || "zdroje ho neuvádzajú")}</span></div>
        <div class="kpi"><span class="k">Posledný obchod</span><span class="v">${esc(i.last_date || "–")}</span><span class="s">${esc(i.last_company || "")}</span></div>
        <div class="kpi"><span class="k">Investície</span><span class="v">${i.n_inv}</span><span class="s">${i.n_36m} za posledných 36 mes.</span></div>
        <div class="kpi"><span class="k">Úroveň dôkazov</span><span class="v">${i.status === "INCLUDED" ? esc(i.tier) : "kontrola"}</span><span class="s">${i.tier === "A" ? "2+ datované obchody, 2+ zdroje" : i.tier === "B" ? "1+ datovaný obchod za 36 mes." : ""}</span></div>
      </div>
      <dl class="kv">
        <dt>Sídlo</dt><dd>${esc(i.hq)}</dd>
        <dt>Typ</dt><dd>${esc(i.types.map(t => TYPE[t] || t).join(", ") || "–")}</dd>
        <dt>Sektory</dt><dd>${i.sectors.length ? `<span class="chips">${i.sectors.map(s => `<span class="chip acc">${esc(SECTOR[s] || s)}</span>`).join("")}</span>` : "–"}</dd>
        <dt>Štádiá</dt><dd>${i.stages.length ? `<span class="chips">${i.stages.map(s => `<span class="chip">${esc(STAGE[s] || s)}</span>`).join("")}</span>` : "–"}</dd>
        <dt>Tiket</dt><dd>${ticket}</dd>
      </dl>
      ${m.refined ? `<section class="blk"><div class="blk-h"><h3>Pred a po spresnení</h3><span class="n">${i.notes.length ? i.notes.length + " " + plural(i.notes.length, "zmena", "zmeny", "zmien") : "bez zmeny"}</span></div>
        <div class="cmp-wrap"><table class="cmp"><thead><tr><th scope="col">Údaj</th><th scope="col">Zmrazené (v3)</th><th scope="col">Po spresnení</th></tr></thead><tbody>
        ${cmpRows.map(r => `<tr><th scope="row">${r[0]}</th><td>${r[1]}</td><td${r[3] ? ' class="chg"' : ""}>${r[2]}</td></tr>`).join("")}</tbody></table></div>
        ${i.notes.length ? `<ul class="notes">${i.notes.map(n => `<li>${arrow(n)}</li>`).join("")}</ul>` : ""}</section>` : ""}
      <section class="blk"><div class="blk-h"><h3>Kapitál a fondy</h3><span class="n">${i.funds.length} ${plural(i.funds.length, "tvrdenie", "tvrdenia", "tvrdení")}</span></div>
        ${i.capital_note ? `<p class="blk-note">${esc(i.capital_note)}</p>` : ""}
        ${fundRows(i)}
        ${i.targets ? `<p class="targets"><b>Len plánované, do kapitálu sa nepočítajú:</b> ${esc(i.targets)}</p>` : ""}</section>
      <section class="blk"><div class="blk-h"><h3>Investície</h3><span class="n">${dated.length} datovaných · ${undated.length} bez dátumu</span></div>
        <div class="dt deals"><div class="dt-head"><span>Dátum</span><span>Firma</span><span class="c-rd">Kolo</span><span class="num c-amt">Suma kola</span><span></span></div>
        ${dealRows(dated)}
        ${undated.length ? `<div class="dt-sub">V portfóliu, bez dátumu obchodu</div>${dealRows(undated)}` : ""}</div></section>
      <section class="blk"><div class="blk-h"><h3>Zdroje ostatných údajov</h3><span class="n">${Object.keys(i.profile).length}</span></div>
        <div class="dt prof"><div class="dt-head"><span>Údaj</span><span>Zdroj</span><span></span></div>
        ${Object.entries(i.profile).map(([k, s]) => `<details class="dt-row"><summary><span class="strong">${esc(PROFILE[k] || k)}</span><span>${esc(s.domain)}</span><span class="tog">citácia</span></summary>
          <div class="dt-open">${quotes([{...s, tier: "", context: ""}])}</div></details>`).join("")}</div></section>
    </div>`;
  el.scrollTop = 0;
}
document.getElementById("lhead").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; state.sort = b.dataset.sort;
  try { localStorage.setItem("investor-explorer", JSON.stringify({sort: state.sort})); } catch (err) {} renderList(); });
document.getElementById("list").addEventListener("click", e => { const r = e.target.closest(".row"); if (!r) return; state.sel = r.dataset.id; renderList();
  if (matchMedia("(max-width: 1000px)").matches) document.getElementById("sheet").scrollIntoView({behavior: "smooth", block: "start"}); });
document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; renderList(); });
document.getElementById("sector").addEventListener("change", e => { state.sector = e.target.value; renderList(); });
document.getElementById("onlychg").addEventListener("change", e => { state.onlyChg = e.target.checked; renderList(); });
document.getElementById("country").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; state.country = b.dataset.v;
  document.querySelectorAll("#country button").forEach(x => x.setAttribute("aria-pressed", x === b)); renderList(); });
renderList();
</script>"""
