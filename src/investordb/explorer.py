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
            funds.append({"name": v.get("name") or "", "size": size, "eur": eur,
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
.top-r { display: grid; gap: 10px; justify-items: end }
.lang { height: 36px }
.lang button { min-width: 48px; font-size: 14px; letter-spacing: .04em }
@media (max-width: 760px) { .top-r { justify-items: stretch } .lang { justify-self: end } }
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
@media (max-width: 480px) { .tools { grid-template-columns: minmax(0, 1fr) } .tools .seg { display: grid; grid-template-columns: repeat(3, 1fr) } }

/* two panes */
.grid { display: grid; grid-template-columns: minmax(0, 11fr) minmax(0, 13fr); gap: 20px; align-items: start }
@media (max-width: 1000px) { .grid { grid-template-columns: minmax(0, 1fr) } }
.panel { background: var(--sheet); border: 1px solid var(--rule); border-radius: 12px; box-shadow: var(--shadow); overflow: hidden }

/* investor ledger: header and rows share one column template, so every value sits under its heading */
.ledger { --cols: minmax(0, 1fr) 100px 108px 84px 66px }
.lhead, .row { display: grid; grid-template-columns: var(--cols); column-gap: 12px; align-items: center; padding: 0 16px }
.lhead { position: sticky; top: 0; z-index: 2; background: var(--raised); border-bottom: 2px solid var(--rule-strong); min-height: 44px }
.lhead button { white-space: nowrap; border: 0; background: none; padding: 10px 0; font: 700 13px/1.2 var(--body); color: var(--ink-2); cursor: pointer; display: flex; gap: 4px; align-items: center; justify-content: flex-start; text-align: left }
.lhead button.r { justify-content: flex-end; text-align: right }
.lhead button.c { justify-content: center }
.lhead button:hover { color: var(--ink) }
.lhead button[aria-pressed=true] { color: var(--accent) }
.lhead .arr { font-size: 11px; width: 12px; text-align: center; color: var(--ink-3) }
.lhead button[aria-pressed=true] .arr { color: var(--accent) }
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
.sh-body { padding: 18px 24px 28px; container-type: inline-size }
.kpis { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border: 1px solid var(--rule); border-radius: 10px; overflow: hidden }
.kpi { padding: 12px 14px; display: grid; gap: 2px; align-content: start; background: var(--raised) }
.kpi + .kpi { border-left: 1px solid var(--rule) }
.kpi .k { font-size: 13px; font-weight: 600; color: var(--ink-2) }
.kpi .v { font: 700 20px/1.25 var(--body); font-variant-numeric: tabular-nums; white-space: nowrap; overflow: hidden; text-overflow: ellipsis }
.kpi .s { font-size: 13px; color: var(--ink-2); overflow-wrap: anywhere }
@media (max-width: 640px) { .kpis { grid-template-columns: repeat(2, minmax(0, 1fr)) } .kpi:nth-child(3) { border-left: 0 } .kpi:nth-child(n+3) { border-top: 1px solid var(--rule) } }
@container (max-width: 760px) { .kpis { grid-template-columns: repeat(2, minmax(0, 1fr)) } .kpi:nth-child(3) { border-left: 0 } .kpi:nth-child(n+3) { border-top: 1px solid var(--rule) } }
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
.chg-l { display: block; font: 600 12px var(--body); color: var(--warn); margin-top: 4px }
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
    <p class="eyebrow" id="t-eyebrow"></p>
    <h1 id="t-h1"></h1>
    <p class="lede" id="t-lede"></p>
  </div>
  <div class="top-r">
    <div class="seg lang" id="lang" role="group" aria-label="Jazyk / Language">
      <button type="button" data-l="sk" lang="sk" aria-pressed="true">SK</button><button type="button" data-l="en" lang="en" aria-pressed="false">EN</button>
    </div>
    <div class="stats" id="stats"></div>
  </div>
</header>
<div class="tools" role="search">
  <label class="sr" for="q" id="t-qlabel"></label>
  <input type="search" id="q">
  <div class="seg" id="country" role="group">
    <button type="button" data-v="" aria-pressed="true" id="t-all"></button><button type="button" data-v="CZ" aria-pressed="false">CZ</button><button type="button" data-v="SK" aria-pressed="false">SK</button>
  </div>
  <label class="sr" for="sector" id="t-seclabel"></label>
  <select id="sector"></select>
  <label class="check"><input type="checkbox" id="onlychg"> <span id="t-onlychg"></span></label>
</div>
<div class="grid">
  <section class="panel ledger" id="ledger">
    <div class="lhead" id="lhead"></div>
    <div class="rows" id="list"></div>
  </section>
  <article class="panel sheet" id="sheet" aria-live="polite"></article>
</div>
<footer id="foot"></footer>
</div>
<script>
const DATA = __DATA__;
const I18N = {
  sk: {
    title: "Databáza VC investorov CZ/SK", eyebrow: "Zadanie A · pilot", h1: "VC investori so sídlom v Česku a na Slovensku",
    lede: "Každá hodnota má zdroj, dátum a doslovnú citáciu, ktorú program overil na stránke zdroja. Vyberte investora v tabuľke a rozbaľte riadok, aby ste videli citácie.",
    search: "Hľadať", searchPh: "Hľadať investora, sektor alebo portfóliovú firmu", country: "Krajina sídla", all: "Všetky",
    sector: "Sektor", allSectors: "Všetky sektory", onlyChg: "Len zmenené spresnením", investors: "Investori",
    statIncl: "zaradených investorov", statPrec: "správne zaradených", statRefined: "stav po spresnení", statFrozen: "zmrazená verzia",
    colName: "Investor", colCap: "Kapitál", colLast: "Posl. obchod", col36: "Nedávne", col36t: "Nedávne investície: počet za posledných 36 mesiacov (od 9. 10. 2023)",
    colTier: "Úroveň", colTiert: "Úroveň dôkazov A / B", asc: "vzostupne", desc: "zostupne", flip: "kliknutím obrátite poradie", sortBy: "zoradiť podľa tohto stĺpca", refinedMark: "spresnené", dealShort: "obchod", review: "kontrola",
    tierT: "Úroveň dôkazov", reviewT: "Na ručnú kontrolu", none: "Žiadny investor nevyhovuje filtru.", pick: "Vyberte investora v tabuľke.",
    registry: "záznam v registri", toReview: "Na ručnú kontrolu.",
    kCap: "Celkový kapitál", kCapNone: "zdroje ho neuvádzajú", kLast: "Posledný obchod", kInv: "Investície", kInvSub: n => `${n} za posledných 36 mes.`,
    kTier: "Úroveň dôkazov", tierA: "2+ datované obchody, 2+ zdroje", tierB: "1+ datovaný obchod za 36 mes.",
    hq: "Sídlo", type: "Typ", sectors: "Sektory", stages: "Štádiá", ticket: "Tiket", notGiven: "neuvedené",
    cmpH: "Pred a po spresnení", cmpCol: "Údaj", cmpFrozen: "Zmrazené (v3)", cmpAfter: "Po spresnení", changedLbl: "zmenené",
    cmpCap: "Celkový kapitál", cmpLast: "Posledný obchod", cmp36: "Nedávne investície (36 mes.)", cmpTier: "Úroveň dôkazov",
    changes: n => n ? `${n} ${plural(n, "zmena", "zmeny", "zmien")}` : "bez zmeny",
    fundsH: "Kapitál a fondy", claims: n => `${n} ${plural(n, "tvrdenie", "tvrdenia", "tvrdení")}`, noFunds: "Zdroje veľkosť fondov neuvádzajú.",
    fFund: "Fond", fEur: "Suma v EUR", fStatus: "Stav · v kapitáli", orig: "pôvodne", counted: "✓ započítané", notCounted: "nezapočítané",
    quote: "citácia", targets: "Len plánované, do kapitálu sa nepočítajú:", aumName: "AUM (spravovaný kapitál)",
    dealsH: "Investície", dealsN: (a, b) => `${a} datovaných · ${b} bez dátumu`, dDate: "Dátum", dCo: "Firma", dRound: "Kolo", dAmt: "Suma kola",
    undatedSub: "V portfóliu, bez dátumu obchodu", noDate: "bez dátumu", sources: n => `${n} ${plural(n, "zdroj", "zdroje", "zdrojov")}`,
    profH: "Zdroje ostatných údajov", pField: "Údaj", pSrc: "Zdroj", published: "publikované", dealMsg: "správa o obchode",
    mention: "len zmienka – dátum sa nepočíta", fromRefine: "zo spresnenia",
    footer: "Zdroj: data/processed/investors_refined.csv a claims*.csv v repozitári Clientelo-task-a. Citácie sú doslovné úryvky z verejných stránok v pôvodnom jazyku, ktoré program overil na stránke zdroja; sumy v EUR prepočítal program kurzom ECB (≈ = približne alebo prepočet z inej meny).",
    STATUS: {final_close: "uzavretý fond", first_close: "prvé uzavretie", target: "len cieľ", aum: "uvedené AUM", "": "stav neuvedený"},
    TIER_SRC: {T1: "register / regulátor", T2: "web investora", T3: "tlač"},
    PROFILE: {sectors: "Sektory", stages: "Štádiá", ticket: "Tiket", investor_type: "Typ", hq_country: "Sídlo", identity: "Identita"},
    TYPE: {vc: "VC", cvc: "korporátny VC", public_vc: "verejný VC", pe: "PE", real_estate: "nehnuteľnosti", angel_network: "sieť angel investorov", family_office: "family office"},
    STAGE: {pre_seed: "pre-seed", seed: "seed", series_a: "séria A", series_b_plus: "séria B+", growth: "growth", buyout: "buyout"},
    SECTOR: {ai_data: "AI a dáta", enterprise_saas: "B2B SaaS", fintech_insurtech: "fintech", health_digital: "digitálne zdravie", life_sciences_medtech: "life sciences", deeptech_hardware: "deeptech", cleantech_energy: "cleantech", mobility_logistics: "mobilita", consumer_ecommerce: "spotrebiteľ", edtech: "edtech", proptech_construction: "proptech", agri_food: "agri/food", cybersecurity: "kyberbezpečnosť", media_gaming: "médiá/hry", industry_manufacturing: "priemysel", iot_telecom: "IoT", hr_worktech: "HR tech", travel_hospitality: "cestovanie", govtech_legaltech: "govtech", defense_space: "obrana/vesmír", sector_agnostic: "bez sektorového zamerania"},
  },
  en: {
    title: "CZ/SK VC Investor Database", eyebrow: "Assignment A · pilot", h1: "VC investors headquartered in Czechia and Slovakia",
    lede: "Every value has a source, a date and a verbatim quote that a program checked on the source page. Pick an investor in the table and expand a row to see the quotes.",
    search: "Search", searchPh: "Search investor, sector or portfolio company", country: "Country of HQ", all: "All",
    sector: "Sector", allSectors: "All sectors", onlyChg: "Only changed by refinement", investors: "Investors",
    statIncl: "investors included", statPrec: "correctly included", statRefined: "refined data as of", statFrozen: "frozen version",
    colName: "Investor", colCap: "Capital", colLast: "Last deal", col36: "Recent", col36t: "Recent investments: number in the last 36 months (since 9 Oct 2023)",
    colTier: "Tier", colTiert: "Evidence tier A / B", asc: "ascending", desc: "descending", flip: "click to reverse", sortBy: "sort by this column", refinedMark: "refined", dealShort: "deal", review: "review",
    tierT: "Evidence tier", reviewT: "Needs manual review", none: "No investor matches the filter.", pick: "Pick an investor in the table.",
    registry: "registry record", toReview: "Needs manual review.",
    kCap: "Total capital", kCapNone: "not stated in sources", kLast: "Last deal", kInv: "Investments", kInvSub: n => `${n} in the last 36 months`,
    kTier: "Evidence tier", tierA: "2+ dated deals, 2+ sources", tierB: "1+ dated deal in 36 months",
    hq: "HQ", type: "Type", sectors: "Sectors", stages: "Stages", ticket: "Ticket", notGiven: "not stated",
    cmpH: "Before and after refinement", cmpCol: "Field", cmpFrozen: "Frozen (v3)", cmpAfter: "Refined", changedLbl: "changed",
    cmpCap: "Total capital", cmpLast: "Last deal", cmp36: "Recent investments (36 mo)", cmpTier: "Evidence tier",
    changes: n => n ? `${n} ${n === 1 ? "change" : "changes"}` : "no change",
    fundsH: "Capital and funds", claims: n => `${n} ${n === 1 ? "claim" : "claims"}`, noFunds: "Sources do not state fund sizes.",
    fFund: "Fund", fEur: "Amount in EUR", fStatus: "Status · in capital", orig: "as written", counted: "✓ counted", notCounted: "not counted",
    quote: "quote", targets: "Planned only, not counted as capital:", aumName: "AUM (assets under management)",
    dealsH: "Investments", dealsN: (a, b) => `${a} dated · ${b} undated`, dDate: "Date", dCo: "Company", dRound: "Round", dAmt: "Round size",
    undatedSub: "In the portfolio, no deal date", noDate: "no date", sources: n => `${n} ${n === 1 ? "source" : "sources"}`,
    profH: "Sources of other fields", pField: "Field", pSrc: "Source", published: "published", dealMsg: "deal announcement",
    mention: "mention only – date not counted", fromRefine: "from refinement",
    footer: "Source: data/processed/investors_refined.csv and claims*.csv in the Clientelo-task-a repository. Quotes are verbatim excerpts from public pages in their original language, checked by a program on the source page; EUR amounts converted by the program at ECB rates (≈ = approximate or converted from another currency).",
    STATUS: {final_close: "closed fund", first_close: "first close", target: "target only", aum: "stated AUM", "": "status not stated"},
    TIER_SRC: {T1: "registry / regulator", T2: "investor's website", T3: "press"},
    PROFILE: {sectors: "Sectors", stages: "Stages", ticket: "Ticket", investor_type: "Type", hq_country: "HQ", identity: "Identity"},
    TYPE: {vc: "VC", cvc: "corporate VC", public_vc: "public VC", pe: "PE", real_estate: "real estate", angel_network: "angel network", family_office: "family office"},
    STAGE: {pre_seed: "pre-seed", seed: "seed", series_a: "Series A", series_b_plus: "Series B+", growth: "growth", buyout: "buyout"},
    SECTOR: {ai_data: "AI & data", enterprise_saas: "B2B SaaS", fintech_insurtech: "fintech", health_digital: "digital health", life_sciences_medtech: "life sciences", deeptech_hardware: "deeptech", cleantech_energy: "cleantech", mobility_logistics: "mobility", consumer_ecommerce: "consumer", edtech: "edtech", proptech_construction: "proptech", agri_food: "agri/food", cybersecurity: "cybersecurity", media_gaming: "media/gaming", industry_manufacturing: "industry", iot_telecom: "IoT", hr_worktech: "HR tech", travel_hospitality: "travel", govtech_legaltech: "govtech", defense_space: "defense/space", sector_agnostic: "sector-agnostic"},
  },
};
// texts produced by the pipeline in Slovak (refinement notes, capital notes, planned funds) - translated by pattern
const EN_PATTERNS = [
  [/^(.*): dátum (\S+) -> (\S+)$/, (_, c, a, b) => `${c}: date ${a} → ${b}`],
  [/^nový obchod (.*) \((.*)\)$/, (_, c, d) => `new deal ${c} (${d})`],
  [/^fond (.*) znovu neoverený$/, (_, f) => `fund ${f} not re-verified`],
  [/^(.*): investor sa na kole nepodieľal$/, (_, c) => `${c}: investor did not take part in the round`],
  [/^(.*): dátum obchodu sa nepotvrdil$/, (_, c) => `${c}: deal date not confirmed`],
  [/^(.*): opravený dátum sa nepodarilo overiť$/, (_, c) => `${c}: corrected date could not be verified`],
  [/^(.*): novšie kolo \((.*)\) sa nepodarilo overiť, pôvodný dátum ostáva$/, (_, c, d) => `${c}: later round (${d}) could not be verified, original date kept`],
  [/^(.*): zatiaľ len prvé uzavretie (.*)$/, (_, f, a) => `${f}: first close only so far, ${a}`],
  [/^(.*) → EUR kurzom ECB (\S+) \((.*)\)$/, (_, a, r, d) => `${a} → EUR at ECB rate ${r} (${d})`],
  [/^(.*) \(cieľ \/ plán\)$/, (_, f) => `${f} (target / plan)`],
  [/^nespracované$/, () => "not processed"],
];
const plural = (n, one, few, many) => n === 1 ? one : n >= 2 && n <= 4 ? few : many;
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = u => /^https?:\/\//i.test(u || "") ? u : "";
const link = (u, label) => safeUrl(u) ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(label || u)}</a>` : esc(label || "");

let lang = "sk";
const hashLang = (location.hash || "").replace("#", "");
try { const s = JSON.parse(localStorage.getItem("investor-explorer") || "{}"); if (s.lang) lang = s.lang; } catch (e) {}
if (hashLang === "sk" || hashLang === "en") lang = hashLang;
let T = I18N[lang];
const tr = text => lang === "sk" || !text ? text : (p => p ? text.replace(p[0], p[1]) : text)(EN_PATTERNS.find(p => p[0].test(text)));
const trList = text => (text || "").split("; ").filter(Boolean).map(tr).join("; ");
const eur = (v, approx) => {
  if (v == null) return "–";
  const pre = approx ? "≈ " : "";
  if (lang === "en") return pre + (v >= 1e6 ? "€" + (v/1e6).toLocaleString("en", {minimumFractionDigits: 1, maximumFractionDigits: 1}) + "M" : "€" + Math.round(v/1e3).toLocaleString("en") + "k");
  return pre + (v >= 1e6 ? (v/1e6).toLocaleString("sk", {minimumFractionDigits: 1, maximumFractionDigits: 1}) + " mil. €" : Math.round(v/1e3).toLocaleString("sk") + " tis. €");
};
const method = mth => {
  if (!mth) return "";
  if (mth === "aum_stated") return lang === "en" ? "stated AUM" : "uvedené AUM";
  const k = mth.match(/sum_of_(\d+)_closed_funds/);
  if (!k) return mth;
  return lang === "en" ? `sum of ${k[1]} ${k[1] === "1" ? "fund" : "funds"}` : `súčet ${k[1]} ${k[1] === "1" ? "fondu" : "fondov"}`;
};
const arrow = t => esc(tr(t)).replace(/ -&gt; /g, " → ");
// each column: how to read its value, how two values compare (ascending), and the direction a first click uses
const COLS = [
  {key: "name", label: "colName", cls: "", first: 1, get: i => i.name, cmp: (a, b) => a.localeCompare(b, lang)},
  {key: "capital", label: "colCap", cls: "r", first: -1, get: i => i.capital, cmp: (a, b) => a - b},
  {key: "last", label: "colLast", cls: "c-date", first: -1, get: i => i.last_date || null, cmp: (a, b) => a.localeCompare(b)},
  {key: "n36", label: "col36", cls: "r c-n36", title: "col36t", first: -1, get: i => i.n_36m, cmp: (a, b) => a - b},
  {key: "tier", label: "colTier", cls: "c", title: "colTiert", first: 1, get: i => i.status === "INCLUDED" ? i.tier || null : null, cmp: (a, b) => a.localeCompare(b)},
];
let state = {q: "", country: "", sector: "", onlyChg: false, sort: "name", dir: 1, sel: null};
try { const s = JSON.parse(localStorage.getItem("investor-explorer") || "{}");
  if (COLS.some(c => c.key === s.sort)) { state.sort = s.sort; state.dir = s.dir === -1 ? -1 : 1; } } catch (e) {}
const save = () => { try { localStorage.setItem("investor-explorer", JSON.stringify({sort: state.sort, dir: state.dir, lang})); } catch (e) {} };
// sort by the active column in the chosen direction; missing values always last, ties by name
function byColumn(a, b) {
  const c = COLS.find(x => x.key === state.sort), va = c.get(a), vb = c.get(b);
  const missing = (va == null) - (vb == null);
  return missing || (va == null ? 0 : state.dir * c.cmp(va, vb)) || a.name.localeCompare(b.name, lang);
}

const invs = DATA.investors;
const m = DATA.meta;
const typeText = i => i.types.map(t => T.TYPE[t] || t).join(", ");
const changed = i => i.notes.length > 0 || i.status !== "INCLUDED";

function applyLang() {
  T = I18N[lang];
  document.documentElement.lang = lang;
  document.title = T.title;
  const set = (id, text) => { const el = document.getElementById(id); if (el) el.textContent = text; };
  set("t-eyebrow", T.eyebrow); set("t-h1", T.h1); set("t-lede", T.lede); set("t-qlabel", T.search);
  set("t-all", T.all); set("t-seclabel", T.sector); set("t-onlychg", T.onlyChg); set("foot", T.footer);
  document.getElementById("q").placeholder = T.searchPh;
  document.getElementById("country").setAttribute("aria-label", T.country);
  document.getElementById("ledger").setAttribute("aria-label", T.investors);
  document.querySelectorAll("#lang button").forEach(b => b.setAttribute("aria-pressed", b.dataset.l === lang));
  const sectors = [...new Set(invs.flatMap(i => i.sectors))].sort((a, b) => (T.SECTOR[a] || a).localeCompare(T.SECTOR[b] || b, lang));
  const sel = document.getElementById("sector");
  sel.innerHTML = `<option value="">${esc(T.allSectors)}</option>` + sectors.map(s => `<option value="${esc(s)}">${esc(T.SECTOR[s] || s)}</option>`).join("");
  sel.value = state.sector;
  const asOf = new Date(m.as_of + "T12:00:00");
  document.getElementById("stats").innerHTML =
    `<div class="stat"><b>${invs.filter(i => i.status === "INCLUDED").length}</b><span>${esc(T.statIncl)}</span></div>` +
    (m.precision ? `<div class="stat"><b>${esc(m.precision)}</b><span>${esc(T.statPrec)}</span></div>` : "") +
    `<div class="stat"><b>${esc(asOf.toLocaleDateString(lang === "en" ? "en-GB" : "sk", {day: "numeric", month: lang === "en" ? "short" : "numeric", year: "numeric"}))}</b><span>${esc(m.refined ? T.statRefined : T.statFrozen)}</span></div>`;
  renderList();
}
function matches(i) {
  const q = state.q.trim().toLowerCase();
  if (state.country && i.hq !== state.country) return false;
  if (state.sector && !i.sectors.includes(state.sector)) return false;
  if (state.onlyChg && !changed(i)) return false;
  if (!q) return true;
  return [i.name, i.legal_name, i.company_id, ...i.sectors.flatMap(s => [I18N.sk.SECTOR[s] || s, I18N.en.SECTOR[s] || s]), ...i.deals.map(d => d.company)].join(" ").toLowerCase().includes(q);
}
function renderHead() {
  const dirName = state.dir === 1 ? T.asc : T.desc;
  document.getElementById("lhead").innerHTML = COLS.map(c => {
    const on = state.sort === c.key;
    return `<button type="button" class="${c.cls}" data-sort="${c.key}" aria-pressed="${on}" title="${esc((c.title ? T[c.title] + " · " : "") + (on ? dirName + " · " + T.flip : T.sortBy))}">${esc(T[c.label])}<span class="arr" aria-hidden="true">${on ? (state.dir === 1 ? "▲" : "▼") : "↕"}</span></button>`;
  }).join("");
}
function renderList() {
  const list = invs.filter(matches).sort(byColumn);
  if (!list.some(i => i.id === state.sel)) state.sel = list[0]?.id || null;
  renderHead();
  document.getElementById("list").innerHTML = list.length ? list.map(i => `
    <button type="button" class="row" data-id="${esc(i.id)}" aria-current="${i.id === state.sel}">
      <span class="nm"><b>${esc(i.name)}</b><small><span class="ty" title="${esc(typeText(i))}">${esc(i.hq)} · ${esc(typeText(i))}</span><span class="m-date">${esc(T.dealShort)} ${esc(i.last_date || "–")}</span>${changed(i) && m.refined ? `<span class="chg-mark">${esc(T.refinedMark)}</span>` : ""}</small></span>
      <span class="v num${i.capital == null ? " dim" : ""}">${eur(i.capital)}</span>
      <span class="v mono c-date">${esc(i.last_date || "–")}</span>
      <span class="v num c-n36">${i.n_36m}</span>
      <span class="tier ${i.status === "INCLUDED" ? esc(i.tier) : "R"}" title="${esc(i.status === "INCLUDED" ? T.tierT + " " + i.tier : T.reviewT)}">${i.status === "INCLUDED" ? esc(i.tier) : esc(T.review)}</span>
    </button>`).join("") : `<p class="empty">${esc(T.none)}</p>`;
  renderSheet();
}
function quotes(list) {
  return list.map(s => `<div><blockquote class="${s.counted ? "counted" : ""}">${esc(s.quote)}</blockquote>
    <div class="meta"><span>${link(s.url, s.domain)}</span>${s.published ? `<span>${esc(T.published)} ${esc(s.published)}</span>` : ""}${s.tier ? `<span>${esc(T.TIER_SRC[s.tier] || s.tier)}</span>` : ""}${s.context ? `<span>${esc(s.context === "deal" ? T.dealMsg : T.mention)}</span>` : ""}${s.refined ? `<span>${esc(T.fromRefine)}</span>` : ""}</div></div>`).join("");
}
function fundRows(i) {
  if (!i.funds.length) return `<p class="empty">${esc(T.noFunds)}</p>`;
  return `<div class="dt funds"><div class="dt-head"><span>${esc(T.fFund)}</span><span class="num">${esc(T.fEur)}</span><span class="c-st">${esc(T.fStatus)}</span><span></span></div>
    ${i.funds.map(f => `<details class="dt-row"><summary>
      <span class="strong">${esc(f.name || T.aumName)}<span class="orig">${esc(T.orig)}: ${esc(f.size || T.notGiven)}</span></span>
      <span class="num">${eur(f.eur, f.approx)}</span>
      <span class="c-st"><span class="st-dot st-${esc(f.status)}">${esc(T.STATUS[f.status] ?? f.status)}</span><span class="orig">${f.counted ? `<span class="yes">${esc(T.counted)}</span>` : esc(T.notCounted)}</span></span>
      <span class="tog">${esc(T.quote)}</span></summary>
      <div class="dt-open">${quotes([{...f, tier: "", context: ""}])}</div></details>`).join("")}</div>`;
}
function dealRows(list) {
  return list.map(d => `<details class="dt-row"><summary>
      <span class="mono${d.date ? "" : " muted"}">${esc(d.date || T.noDate)}</span>
      <span class="strong">${esc(d.company)}</span>
      <span class="c-rd">${d.round && d.round !== "unknown" ? esc(T.STAGE[d.round] || d.round) : '<span class="muted">–</span>'}</span>
      <span class="num c-amt">${d.eur != null ? eur(d.eur, d.approx) : (d.amount ? `<span class="muted">${esc(d.amount)}</span>` : '<span class="muted">–</span>')}</span>
      <span class="tog">${esc(T.sources(d.sources.length))}</span></summary>
      <div class="dt-open">${quotes(d.sources)}</div></details>`).join("");
}
function renderSheet() {
  const i = invs.find(x => x.id === state.sel);
  const el = document.getElementById("sheet");
  if (!i) { el.innerHTML = `<p class="empty">${esc(T.pick)}</p>`; return; }
  const b = i.before;
  const ticket = i.ticket_eur[0] || i.ticket_eur[1] ? `${eur(i.ticket_eur[0])} – ${eur(i.ticket_eur[1])}` : `<span class="muted">${esc(T.notGiven)}</span>`;
  const dated = i.deals.filter(d => d.date), undated = i.deals.filter(d => !d.date);
  const cmpRows = [
    [T.cmpCap, `${eur(b.capital)}<small>${esc(method(b.capital_method) || T.notGiven)}</small>`, `${eur(i.capital)}<small>${esc(method(i.capital_method) || T.notGiven)}</small>`, (b.capital ?? null) !== (i.capital ?? null)],
    [T.cmpLast, `${esc(b.last_date || "–")}<small>${esc(b.last_company)}</small>`, `${esc(i.last_date || "–")}<small>${esc(i.last_company)}</small>`, b.last_date !== i.last_date],
    [T.cmp36, b.n_36m, i.n_36m, b.n_36m !== i.n_36m],
    [T.cmpTier, b.tier || "–", i.status === "INCLUDED" ? (i.tier || "–") : T.review, b.tier !== i.tier || i.status !== "INCLUDED"]];
  el.innerHTML = `
    <header class="sh-head">
      <h2>${esc(i.name)}</h2>
      <div class="legal"><span>${esc(i.legal_name)}</span><span>IČO <code>${esc(i.company_id)}</code></span><span>${link(i.registry_url, T.registry)}</span>${i.website ? `<span>${link(i.website, i.website.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""))}</span>` : ""}</div>
      ${i.status !== "INCLUDED" ? `<div class="banner"><b>${esc(T.toReview)}</b> ${esc(i.explanation)}</div>` : ""}
    </header>
    <div class="sh-body">
      <div class="kpis">
        <div class="kpi"><span class="k">${esc(T.kCap)}</span><span class="v">${eur(i.capital)}</span><span class="s">${esc(method(i.capital_method) || T.kCapNone)}</span></div>
        <div class="kpi"><span class="k">${esc(T.kLast)}</span><span class="v">${esc(i.last_date || "–")}</span><span class="s">${esc(i.last_company || "")}</span></div>
        <div class="kpi"><span class="k">${esc(T.kInv)}</span><span class="v">${i.n_inv}</span><span class="s">${esc(T.kInvSub(i.n_36m))}</span></div>
        <div class="kpi"><span class="k">${esc(T.kTier)}</span><span class="v">${i.status === "INCLUDED" ? esc(i.tier) : esc(T.review)}</span><span class="s">${esc(i.tier === "A" ? T.tierA : i.tier === "B" ? T.tierB : "")}</span></div>
      </div>
      <dl class="kv">
        <dt>${esc(T.hq)}</dt><dd>${esc(i.hq)}</dd>
        <dt>${esc(T.type)}</dt><dd>${esc(typeText(i) || "–")}</dd>
        <dt>${esc(T.sectors)}</dt><dd>${i.sectors.length ? `<span class="chips">${i.sectors.map(s => `<span class="chip acc">${esc(T.SECTOR[s] || s)}</span>`).join("")}</span>` : "–"}</dd>
        <dt>${esc(T.stages)}</dt><dd>${i.stages.length ? `<span class="chips">${i.stages.map(s => `<span class="chip">${esc(T.STAGE[s] || s)}</span>`).join("")}</span>` : "–"}</dd>
        <dt>${esc(T.ticket)}</dt><dd>${ticket}</dd>
      </dl>
      ${m.refined ? `<section class="blk"><div class="blk-h"><h3>${esc(T.cmpH)}</h3><span class="n">${esc(T.changes(i.notes.length))}</span></div>
        <div class="cmp-wrap"><table class="cmp"><thead><tr><th scope="col">${esc(T.cmpCol)}</th><th scope="col">${esc(T.cmpFrozen)}</th><th scope="col">${esc(T.cmpAfter)}</th></tr></thead><tbody>
        ${cmpRows.map(r => `<tr><th scope="row">${esc(r[0])}</th><td>${r[1]}</td><td${r[3] ? ' class="chg"' : ""}>${r[2]}${r[3] ? `<span class="chg-l">${esc(T.changedLbl)}</span>` : ""}</td></tr>`).join("")}</tbody></table></div>
        ${i.notes.length ? `<ul class="notes">${i.notes.map(n => `<li>${arrow(n)}</li>`).join("")}</ul>` : ""}</section>` : ""}
      <section class="blk"><div class="blk-h"><h3>${esc(T.fundsH)}</h3><span class="n">${esc(T.claims(i.funds.length))}</span></div>
        ${i.capital_note ? `<p class="blk-note">${esc(trList(i.capital_note))}</p>` : ""}
        ${fundRows(i)}
        ${i.targets ? `<p class="targets"><b>${esc(T.targets)}</b> ${esc(trList(i.targets))}</p>` : ""}</section>
      <section class="blk"><div class="blk-h"><h3>${esc(T.dealsH)}</h3><span class="n">${esc(T.dealsN(dated.length, undated.length))}</span></div>
        <div class="dt deals"><div class="dt-head"><span>${esc(T.dDate)}</span><span>${esc(T.dCo)}</span><span class="c-rd">${esc(T.dRound)}</span><span class="num c-amt">${esc(T.dAmt)}</span><span></span></div>
        ${dealRows(dated)}
        ${undated.length ? `<div class="dt-sub">${esc(T.undatedSub)}</div>${dealRows(undated)}` : ""}</div></section>
      <section class="blk"><div class="blk-h"><h3>${esc(T.profH)}</h3><span class="n">${Object.keys(i.profile).length}</span></div>
        <div class="dt prof"><div class="dt-head"><span>${esc(T.pField)}</span><span>${esc(T.pSrc)}</span><span></span></div>
        ${Object.entries(i.profile).map(([k, s]) => `<details class="dt-row"><summary><span class="strong">${esc(T.PROFILE[k] || k)}</span><span>${esc(s.domain)}</span><span class="tog">${esc(T.quote)}</span></summary>
          <div class="dt-open">${quotes([{...s, tier: "", context: ""}])}</div></details>`).join("")}</div></section>
    </div>`;
  el.scrollTop = 0;
}
document.getElementById("lang").addEventListener("click", e => { const b = e.target.closest("button"); if (!b || b.dataset.l === lang) return;
  lang = b.dataset.l; save(); applyLang(); });
document.getElementById("lhead").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return;
  // the active column flips its direction; a new column starts in its most useful direction
  if (state.sort === b.dataset.sort) state.dir = -state.dir;
  else { state.sort = b.dataset.sort; state.dir = COLS.find(c => c.key === state.sort).first; }
  save(); renderList(); });
document.getElementById("list").addEventListener("click", e => { const r = e.target.closest(".row"); if (!r) return; state.sel = r.dataset.id; renderList();
  if (matchMedia("(max-width: 1000px)").matches) document.getElementById("sheet").scrollIntoView({behavior: "smooth", block: "start"}); });
document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; renderList(); });
document.getElementById("sector").addEventListener("change", e => { state.sector = e.target.value; renderList(); });
document.getElementById("onlychg").addEventListener("change", e => { state.onlyChg = e.target.checked; renderList(); });
document.getElementById("country").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; state.country = b.dataset.v;
  document.querySelectorAll("#country button").forEach(x => x.setAttribute("aria-pressed", x === b)); renderList(); });
applyLang();
</script>"""
