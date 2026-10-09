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
        d = deals.setdefault(key, {"company": company, "date": "", "sources": []})
        if counted.get(key) is c:
            d["date"] = c["event_date"][:10]
            d["round"], d["amount"] = v.get("round") or "", v.get("amount") or ""
        d["sources"].append({"url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"],
                             "published": c.get("published_date") or "", "tier": c["source_tier"],
                             "context": c.get("deal_context") or "", "refined": "verdict" in v,
                             "counted": counted.get(key) is c})
    cap = total_capital(ok, on)
    funds = [{"name": _value(c).get("name"), "size": _value(c).get("size"), "status": _value(c).get("status") or "",
              "url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"],
              "counted": any(c is k for k in cap["counted"])}
             for c in ok if c["field"] == "funds" or (c["field"] == "total_capital" and cap["method"] == "aum_stated")]
    profile = {}
    for field in ("sectors", "stages", "ticket", "investor_type", "hq_country", "identity"):
        c = next((c for c in ok if c["field"] == field), None)
        if c:
            profile[field] = {"url": c["source_url"], "domain": domain(c["source_url"]), "quote": c["quote"]}
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
        "funds": funds, "profile": profile,
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,800;1,400&display=swap">
<style>
/* Layout: a ledger of investors on the left, the evidence sheet of the selected one on the right; one column on phones.
   Contrast: body text >= 12:1, secondary text >= 7:1, tertiary >= 4.8:1 on both the page and the cards, in both themes. */
:root {
  --paper: #e9edf2; --sheet: #ffffff; --raised: #f6f8fb; --ink: #0f1822; --ink-2: #364352; --ink-3: #566273;
  --rule: #c9d2dd; --rule-strong: #9fadbd;
  --accent: #1a44a3; --accent-soft: #dfe7f9; --on-accent: #ffffff;
  --ok: #145c38; --ok-soft: #d7ecdf; --warn: #7d4300; --warn-soft: #f8e6c6;
  --quote: #f1f4f8; --quote-rule: #a9b6c6;
  --display: "Public Sans", "Segoe UI", system-ui, sans-serif; --body: "Public Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #0a0f15; --sheet: #141b24; --raised: #1a2330; --ink: #f1f4f8; --ink-2: #c6d0dc; --ink-3: #9eabba;
  --rule: #2e3a49; --rule-strong: #4a5a6d;
  --accent: #a6bfff; --accent-soft: #1f2d4a; --on-accent: #0a0f15;
  --ok: #86e0b1; --ok-soft: #14301f; --warn: #f5c477; --warn-soft: #3a2a10;
  --quote: #0f151d; --quote-rule: #4a5a6d; color-scheme: dark } }
:root[data-theme="dark"] {
  --paper: #0a0f15; --sheet: #141b24; --raised: #1a2330; --ink: #f1f4f8; --ink-2: #c6d0dc; --ink-3: #9eabba;
  --rule: #2e3a49; --rule-strong: #4a5a6d;
  --accent: #a6bfff; --accent-soft: #1f2d4a; --on-accent: #0a0f15;
  --ok: #86e0b1; --ok-soft: #14301f; --warn: #f5c477; --warn-soft: #3a2a10;
  --quote: #0f151d; --quote-rule: #4a5a6d; color-scheme: dark }
* { box-sizing: border-box }
body { margin: 0; background: var(--paper); color: var(--ink); font: 16px/1.55 var(--body); -webkit-font-smoothing: antialiased }
a { color: var(--accent); text-underline-offset: 3px; text-decoration-thickness: 1px }
a:hover { text-decoration-thickness: 2px }
a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible, summary:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; border-radius: 4px }
.wrap { max-width: 1280px; margin: 0 auto; padding-inline: 16px; padding-block: 24px 48px }
header.top { display: flex; flex-wrap: wrap; gap: 12px 32px; align-items: flex-end; justify-content: space-between; padding-bottom: 18px; border-bottom: 2px solid var(--rule) }
h1 { font: 800 clamp(24px, 3.2vw, 34px)/1.15 var(--display); letter-spacing: -0.015em; margin: 0; text-wrap: balance }
.lede { color: var(--ink-2); margin: 8px 0 0; max-width: 68ch; font-size: 16.5px }
.stats { display: flex; flex-wrap: wrap; gap: 8px }
.stat { background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; padding: 6px 12px; font-size: 14px; color: var(--ink-2); line-height: 1.3 }
.stat b { display: block; color: var(--ink); font: 600 17px/1.25 var(--body); font-variant-numeric: tabular-nums }
.tools { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; padding-block: 16px }
.tools input[type=search] { flex: 1 1 260px; min-width: 0; height: 44px; padding: 0 14px; border: 1.5px solid var(--rule-strong); border-radius: 8px; background: var(--sheet); color: var(--ink); font: 16px var(--body) }
.tools input[type=search]::placeholder { color: var(--ink-3) }
.tools select { height: 44px; padding: 0 10px; border: 1.5px solid var(--rule-strong); border-radius: 8px; background: var(--sheet); color: var(--ink); font: 15px var(--body) }
.seg { display: inline-flex; border: 1.5px solid var(--rule-strong); border-radius: 8px; overflow: hidden; height: 44px }
.seg button { border: 0; background: var(--sheet); color: var(--ink-2); padding: 0 16px; font: 600 15px var(--body); cursor: pointer }
.seg button + button { border-left: 1.5px solid var(--rule-strong) }
.seg button[aria-pressed=true] { background: var(--accent); color: var(--on-accent) }
.count { color: var(--ink-2); font-size: 14px; margin: 0 0 8px }
.grid { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 20px; align-items: start }
@media (max-width: 900px) { .grid { grid-template-columns: minmax(0, 1fr) } }
.ledger { background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; overflow: hidden }
.row { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 4px 12px; padding: 12px 16px 12px 13px; border: 0; border-bottom: 1px solid var(--rule); border-left: 3px solid transparent; cursor: pointer; background: none; width: 100%; text-align: left; color: inherit; font: inherit }
.row:last-child { border-bottom: 0 }
.row:hover { background: var(--raised) }
.row[aria-current=true] { background: var(--accent-soft); border-left-color: var(--accent) }
.row .nm { font: 600 17px/1.3 var(--body); min-width: 0; overflow-wrap: anywhere }
.row .sub { grid-column: 1 / -1; display: flex; flex-wrap: wrap; align-items: center; gap: 4px 16px; font-size: 14.5px; color: var(--ink-2); font-variant-numeric: tabular-nums }
.row .sub b { color: var(--ink); font-weight: 600 }
.tier { font: 600 13px/1 var(--body); border-radius: 6px; padding: 5px 8px; align-self: center; white-space: nowrap; border: 1.5px solid var(--accent); color: var(--accent) }
.tier.B { border-color: var(--ink-3); color: var(--ink-2) }
.tier.R { border-color: var(--warn); color: var(--warn) }
.pill { display: inline-block; font: 600 12.5px/1 var(--body); padding: 4px 8px; border-radius: 999px; background: var(--warn-soft); color: var(--warn) }
.sheet { background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; padding: 22px 26px 28px; position: sticky; top: calc(env(safe-area-inset-top, 0px) + 12px); max-height: calc(100vh - 24px); overflow: auto }
@media (max-width: 900px) { .sheet { position: static; max-height: none; padding: 18px 18px 24px } }
.sheet h2 { font: 800 27px/1.2 var(--display); margin: 0; text-wrap: balance; letter-spacing: -0.01em }
.legal { color: var(--ink-2); font-size: 15px; margin-top: 6px; display: flex; flex-wrap: wrap; gap: 2px 14px }
.legal code, .mono { font: 500 14.5px var(--mono); font-variant-numeric: tabular-nums }
.facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px 22px; margin: 18px 0 12px; padding: 16px 18px; background: var(--raised); border: 1px solid var(--rule); border-radius: 10px }
.fact .k { font: 600 13px/1.3 var(--body); color: var(--ink-2); margin-bottom: 3px }
.fact .v { font: 600 17px/1.35 var(--body); overflow-wrap: anywhere; font-variant-numeric: tabular-nums }
h3 { font: 700 15px/1.3 var(--body); text-transform: uppercase; letter-spacing: .06em; color: var(--ink); margin: 30px 0 10px; padding-bottom: 8px; border-bottom: 2px solid var(--rule) }
h3 .n { color: var(--ink-3); font-weight: 600 }
.chips { display: flex; flex-wrap: wrap; gap: 6px }
.chip { font: 600 13px/1.2 var(--body); padding: 5px 10px; border-radius: 999px; background: var(--raised); border: 1px solid var(--rule-strong); color: var(--ink-2) }
.chip.ok { background: var(--ok-soft); color: var(--ok); border-color: transparent }
.chip.warn { background: var(--warn-soft); color: var(--warn); border-color: transparent }
.chip.acc { background: var(--accent-soft); color: var(--accent); border-color: transparent }
.ev { border-top: 1px solid var(--rule); padding: 14px 0 }
.ev:first-of-type { border-top: 0; padding-top: 4px }
.ev .head { display: flex; flex-wrap: wrap; gap: 6px 12px; align-items: center }
.ev .date { font: 500 15px var(--mono); min-width: 10.5ch; font-variant-numeric: tabular-nums; color: var(--ink) }
.ev .date.none { color: var(--ink-3); font-family: var(--body); font-style: italic; font-size: 14.5px }
.ev .co { font: 600 16.5px/1.35 var(--body) }
.src { margin-top: 10px; display: grid; gap: 10px }
blockquote { margin: 0; padding: 10px 14px; background: var(--quote); border-left: 4px solid var(--quote-rule); border-radius: 0 6px 6px 0; font-size: 15.5px; line-height: 1.55; color: var(--ink); overflow-wrap: anywhere }
blockquote.counted { border-left-color: var(--accent) }
.meta { font-size: 14px; line-height: 1.45; color: var(--ink-2); display: flex; flex-wrap: wrap; gap: 2px 14px; margin-top: 5px }
.meta a { font-weight: 600 }
details > summary { cursor: pointer; margin-top: 6px; color: var(--accent); font-size: 14.5px; font-weight: 600; list-style: none; display: inline-flex; gap: 6px; align-items: center }
details > summary::-webkit-details-marker { display: none }
details > summary::before { content: "▸"; font-size: 13px; transition: transform .15s }
details[open] > summary::before { transform: rotate(90deg) }
details > summary span { color: var(--ink-2); font-weight: 400 }
.notes { margin: 12px 0 0; padding-left: 20px; color: var(--ink) }
.notes li { margin: 5px 0 }
.cmp { width: 100%; border-collapse: collapse; font-size: 15px }
.cmp th, .cmp td { text-align: left; padding: 9px 10px; border-bottom: 1px solid var(--rule); vertical-align: top }
.cmp thead th { font: 700 13px var(--body); color: var(--ink-2); border-bottom: 2px solid var(--rule-strong) }
.cmp tbody th { font: 600 14.5px var(--body); color: var(--ink); white-space: nowrap }
.cmp td { font-variant-numeric: tabular-nums }
.cmp td small { display: block; color: var(--ink-3); font-size: 13px; margin-top: 2px }
.cmp td.chg { background: var(--warn-soft); color: var(--ink); font-weight: 600 }
.cmp td.chg small { color: var(--ink-2) }
.tblwrap { overflow-x: auto; border: 1px solid var(--rule); border-radius: 8px }
.tblwrap .cmp tr:last-child th, .tblwrap .cmp tr:last-child td { border-bottom: 0 }
.legend { font-size: 13.5px; color: var(--ink-2); margin: 8px 0 0 }
.legend i { display: inline-block; width: 12px; height: 12px; border-radius: 3px; background: var(--warn-soft); border: 1px solid var(--warn); vertical-align: -1px; margin-right: 4px }
.empty { color: var(--ink-2); font-style: italic }
.targets { margin-top: 10px; padding: 10px 14px; border-radius: 8px; background: var(--warn-soft); color: var(--ink); font-size: 15px }
footer { margin-top: 28px; color: var(--ink-2); font-size: 14.5px; max-width: 82ch; line-height: 1.6 }
@media (prefers-reduced-motion: no-preference) { .row { transition: background .12s } }
@media (prefers-reduced-motion: reduce) { details > summary::before { transition: none } }
</style>
<!--BODY-->
<div class="wrap">
<header class="top">
  <div><h1>VC investori so sídlom v Česku a na Slovensku</h1>
  <p class="lede">Pilot databázy investorov: každá hodnota má zdroj, dátum a doslovnú citáciu, ktorú program overil na stránke zdroja.</p></div>
  <div class="stats" id="stats"></div>
</header>
<div class="tools" role="search">
  <input type="search" id="q" placeholder="Hľadať investora, sektor alebo portfóliovú firmu" aria-label="Hľadať">
  <div class="seg" id="country" role="group" aria-label="Krajina">
    <button type="button" data-v="" aria-pressed="true">Všetky</button><button type="button" data-v="CZ" aria-pressed="false">CZ</button><button type="button" data-v="SK" aria-pressed="false">SK</button>
  </div>
  <select id="sector" aria-label="Sektor"><option value="">Všetky sektory</option></select>
  <select id="sort" aria-label="Zoradiť">
    <option value="name">Podľa názvu</option><option value="last">Posledný obchod</option><option value="capital">Kapitál</option><option value="n36">Obchody za 36 mes.</option>
  </select>
</div>
<p class="count" id="count" aria-live="polite"></p>
<div class="grid">
  <nav class="ledger" id="list" aria-label="Investori"></nav>
  <article class="sheet" id="sheet" aria-live="polite"></article>
</div>
<footer id="foot"></footer>
</div>
<script>
const DATA = __DATA__;
const SECTOR = {ai_data:"AI a dáta",enterprise_saas:"B2B SaaS",fintech_insurtech:"fintech",health_digital:"digitálne zdravie",life_sciences_medtech:"life sciences",deeptech_hardware:"deeptech",cleantech_energy:"cleantech",mobility_logistics:"mobilita",consumer_ecommerce:"spotrebiteľ",edtech:"edtech",proptech_construction:"proptech",agri_food:"agri/food",cybersecurity:"kyberbezpečnosť",media_gaming:"médiá/hry",industry_manufacturing:"priemysel",iot_telecom:"IoT",hr_worktech:"HR tech",travel_hospitality:"cestovanie",govtech_legaltech:"govtech",defense_space:"obrana/vesmír",sector_agnostic:"bez sektora"};
const STAGE = {pre_seed:"pre-seed",seed:"seed",series_a:"séria A",series_b_plus:"séria B+",growth:"growth",buyout:"buyout"};
const TYPE = {vc:"VC",cvc:"korporátny VC",public_vc:"verejný VC",pe:"PE"};
const FUND = {final_close:["uzavretý","ok"],first_close:["prvé uzavretie","acc"],target:["len cieľ","warn"]};
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = u => /^https?:\/\//i.test(u || "") ? u : "";
const link = (u, label) => safeUrl(u) ? `<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(label || u)}</a>` : esc(label || "");
const eur = v => v == null ? "–" : v >= 1e6 ? (v/1e6).toLocaleString("sk", {maximumFractionDigits: 1}) + " mil. €" : Math.round(v/1e3).toLocaleString("sk") + " tis. €";
const TIER_SRC = {T1: "register / regulátor", T2: "web investora", T3: "tlač"};
const method = m => !m ? "" : m === "aum_stated" ? "uvedené AUM" :
  (k => k ? `súčet ${k[1]} ${k[1] === "1" ? "fondu" : "fondov"}` : m)(m.match(/sum_of_(\d+)_closed_funds/));
const arrow = t => esc(t).replace(/ -&gt; /g, " → ");
let state = {q: "", country: "", sector: "", sort: "name", sel: null};
try { const s = JSON.parse(localStorage.getItem("investor-explorer") || "{}"); Object.assign(state, {sort: s.sort || "name"}); } catch (e) {}

const invs = DATA.investors;
const sectors = [...new Set(invs.flatMap(i => i.sectors))].sort((a, b) => (SECTOR[a]||a).localeCompare(SECTOR[b]||b, "sk"));
document.getElementById("sector").innerHTML += sectors.map(s => `<option value="${esc(s)}">${esc(SECTOR[s]||s)}</option>`).join("");
document.getElementById("sort").value = state.sort;
const m = DATA.meta;
document.getElementById("stats").innerHTML = [
  `<span class="stat"><b>${invs.filter(i => i.status === "INCLUDED").length}</b>zaradených investorov</span>`,
  m.precision ? `<span class="stat"><b>${esc(m.precision)}</b>presnosť zaradenia</span>` : "",
  `<span class="stat"><b>${esc(m.as_of)}</b>${m.refined ? "stav po spresnení" : "zmrazená verzia"}</span>`].join("");
document.getElementById("foot").innerHTML = esc(m.footer || "");

function matches(i) {
  const q = state.q.trim().toLowerCase();
  if (state.country && i.hq !== state.country) return false;
  if (state.sector && !i.sectors.includes(state.sector)) return false;
  if (!q) return true;
  const hay = [i.name, i.legal_name, i.company_id, ...i.sectors.map(s => SECTOR[s] || s), ...i.deals.map(d => d.company)].join(" ").toLowerCase();
  return hay.includes(q);
}
function sorted(list) {
  const by = {name: (a, b) => a.name.localeCompare(b.name, "sk"), last: (a, b) => (b.last_date||"").localeCompare(a.last_date||""),
    capital: (a, b) => (b.capital ?? -1) - (a.capital ?? -1), n36: (a, b) => b.n_36m - a.n_36m};
  return [...list].sort(by[state.sort]);
}
function changed(i) { return i.notes.length > 0 || i.status !== "INCLUDED"; }
function renderList() {
  const list = sorted(invs.filter(matches));
  if (state.sel && !list.some(i => i.id === state.sel)) state.sel = list[0]?.id || null;
  if (!state.sel && list.length) state.sel = list[0].id;
  document.getElementById("count").textContent = `Zobrazených ${list.length} z ${invs.length} investorov`;
  document.getElementById("list").innerHTML = list.length ? list.map(i => `
    <button type="button" class="row" data-id="${esc(i.id)}" aria-current="${i.id === state.sel}">
      <span class="nm">${esc(i.name)}</span>
      <span class="tier ${i.status === "INCLUDED" ? esc(i.tier) : "R"}" title="${i.status === "INCLUDED" ? "Úroveň dôkazov " + esc(i.tier) + (i.tier === "A" ? ": aspoň 2 datované obchody z 2 nezávislých zdrojov" : ": aspoň 1 datovaný obchod za 36 mesiacov") : "Na ručnú kontrolu"}">${i.status === "INCLUDED" ? "úroveň " + esc(i.tier) : "na kontrolu"}</span>
      <span class="sub"><span><b>${esc(i.hq)}</b></span><span>kapitál <b>${eur(i.capital)}</b></span><span>posledný obchod <b>${esc(i.last_date || "–")}</b></span>${changed(i) && DATA.meta.refined ? '<span class="pill">spresnené</span>' : ""}</span>
    </button>`).join("") : `<p class="empty" style="padding:16px">Žiadny investor nevyhovuje filtru.</p>`;
  renderSheet();
}
function quoteBlock(s) {
  return `<div><blockquote class="${s.counted ? "counted" : ""}">${esc(s.quote)}</blockquote>
    <div class="meta"><span>${link(s.url, s.domain)}</span>${s.published ? `<span>publikované ${esc(s.published)}</span>` : ""}${s.tier ? `<span>${esc(TIER_SRC[s.tier] || s.tier)}</span>` : ""}${s.context ? `<span>${s.context === "deal" ? "správa o obchode" : "len zmienka, dátum sa nepočíta"}</span>` : ""}${s.refined ? "<span>zo spresnenia</span>" : ""}</div></div>`;
}
function renderSheet() {
  const i = invs.find(x => x.id === state.sel);
  const el = document.getElementById("sheet");
  if (!i) { el.innerHTML = `<p class="empty">Vyberte investora v zozname.</p>`; return; }
  const ticket = i.ticket_eur[0] || i.ticket_eur[1] ? `${eur(i.ticket_eur[0])} – ${eur(i.ticket_eur[1])}` : "neuvedené";
  const b = i.before;
  const capChanged = (b.capital ?? null) !== (i.capital ?? null);
  const rows = [
    ["Celkový kapitál", eur(b.capital) + (b.capital_method ? `<small>${esc(method(b.capital_method))}</small>` : ""), eur(i.capital) + (i.capital_method ? `<small>${esc(method(i.capital_method))}</small>` : ""), capChanged],
    ["Posledný obchod", `${esc(b.last_date || "–")}<small>${esc(b.last_company)}</small>`, `${esc(i.last_date || "–")}<small>${esc(i.last_company)}</small>`, b.last_date !== i.last_date],
    ["Obchody za 36 mes.", b.n_36m, i.n_36m, b.n_36m !== i.n_36m],
    ["Úroveň", b.tier || "–", i.status === "INCLUDED" ? (i.tier || "–") : "na kontrolu", b.tier !== i.tier || i.status !== "INCLUDED"]];
  el.innerHTML = `
    <h2>${esc(i.name)}</h2>
    <div class="legal"><span>${esc(i.legal_name)}</span><span>IČO <code>${esc(i.company_id)}</code></span><span>${link(i.registry_url, "záznam v registri")}</span>${i.website ? `<span>${link(i.website, i.website.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""))}</span>` : ""}</div>
    ${i.status !== "INCLUDED" ? `<p class="chip warn" style="display:inline-block;margin-top:10px">Na kontrolu: ${esc(i.explanation)}</p>` : ""}
    <div class="facts">
      <div class="fact"><div class="k">Sídlo</div><div class="v">${esc(i.hq)}</div></div>
      <div class="fact"><div class="k">Typ</div><div class="v">${esc(i.types.map(t => TYPE[t] || t).join(", ") || "–")}</div></div>
      <div class="fact"><div class="k">Celkový kapitál</div><div class="v">${eur(i.capital)}</div></div>
      <div class="fact"><div class="k">Tiket</div><div class="v">${ticket}</div></div>
      <div class="fact"><div class="k">Investície</div><div class="v">${i.n_inv} (${i.n_36m} za 36 mes.)</div></div>
    </div>
    <div class="chips">${i.sectors.map(s => `<span class="chip acc">${esc(SECTOR[s] || s)}</span>`).join("")}${i.stages.map(s => `<span class="chip">${esc(STAGE[s] || s)}</span>`).join("")}</div>
    ${DATA.meta.refined ? `<h3>Pred a po spresnení</h3><div class="tblwrap"><table class="cmp"><thead><tr><th scope="col"></th><th scope="col">Zmrazené (v3)</th><th scope="col">Po spresnení</th></tr></thead><tbody>
      ${rows.map(r => `<tr><th scope="row">${r[0]}</th><td>${r[1]}</td><td${r[3] ? ' class="chg"' : ""}>${r[2]}</td></tr>`).join("")}</tbody></table></div>
      <p class="legend"><i></i>zmenená hodnota</p>
      ${i.notes.length ? `<ul class="notes">${i.notes.map(n => `<li>${arrow(n)}</li>`).join("")}</ul>` : `<p class="empty">Spresnenie nič nezmenilo.</p>`}` : ""}
    <h3>Kapitál a fondy</h3>
    ${i.capital_note ? `<p class="meta">${esc(i.capital_note)}</p>` : ""}
    ${i.funds.length ? i.funds.map(f => `<div class="ev"><div class="head"><span class="co">${esc(f.name || "AUM")}</span><span class="mono">${esc(f.size || "")}</span>
      ${f.status ? `<span class="chip ${FUND[f.status]?.[1] || ""}">${esc(FUND[f.status]?.[0] || f.status)}</span>` : ""}${f.counted ? `<span class="chip ok">započítané</span>` : ""}</div>
      <div class="src">${quoteBlock({...f, tier: "", context: "", counted: f.counted})}</div></div>`).join("") : `<p class="empty">Zdroje veľkosť fondov neuvádzajú.</p>`}
    ${i.targets ? `<p class="targets"><b>Len plánované, do kapitálu sa nepočítajú:</b> ${esc(i.targets)}</p>` : ""}
    <h3>Investície <span class="n">(${i.deals.length})</span></h3>
    ${i.deals.map(d => `<div class="ev"><div class="head"><span class="date${d.date ? "" : " none"}">${esc(d.date || "bez dátumu")}</span><span class="co">${esc(d.company)}</span>
      ${d.round && d.round !== "unknown" ? `<span class="chip">${esc(STAGE[d.round] || d.round)}</span>` : ""}${d.amount ? `<span class="chip">${esc(d.amount)}</span>` : ""}</div>
      <details><summary>Zobraziť citácie (${d.sources.length}) <span>· ${esc(d.sources.map(s => s.domain).filter((v, k, a) => a.indexOf(v) === k).join(", "))}</span></summary>
      <div class="src">${d.sources.map(quoteBlock).join("")}</div></details></div>`).join("")}
    <h3>Ostatné polia</h3>
    ${Object.entries(i.profile).map(([k, s]) => `<div class="ev"><div class="head"><span class="co">${esc({sectors:"Sektory",stages:"Štádiá",ticket:"Tiket",investor_type:"Typ",hq_country:"Sídlo",identity:"Identita"}[k] || k)}</span></div><div class="src">${quoteBlock({...s, tier: "", context: ""})}</div></div>`).join("")}
  `;
}
document.getElementById("list").addEventListener("click", e => { const r = e.target.closest(".row"); if (!r) return; state.sel = r.dataset.id; renderList();
  if (matchMedia("(max-width: 860px)").matches) document.getElementById("sheet").scrollIntoView({behavior: "smooth", block: "start"}); });
document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; renderList(); });
document.getElementById("sector").addEventListener("change", e => { state.sector = e.target.value; renderList(); });
document.getElementById("sort").addEventListener("change", e => { state.sort = e.target.value; try { localStorage.setItem("investor-explorer", JSON.stringify({sort: state.sort})); } catch (err) {} renderList(); });
document.getElementById("country").addEventListener("click", e => { const b = e.target.closest("button"); if (!b) return; state.country = b.dataset.v;
  document.querySelectorAll("#country button").forEach(x => x.setAttribute("aria-pressed", x === b)); renderList(); });
renderList();
</script>"""
