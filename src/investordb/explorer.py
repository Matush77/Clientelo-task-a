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
/* Layout: a ledger of investors on the left, the evidence sheet of the selected one on the right; one column on phones */
:root {
  --paper: #f3f5f8; --sheet: #ffffff; --ink: #16202c; --ink-2: #4b5766; --rule: #d8dee6;
  --accent: #1f4fb8; --accent-soft: #e4ebfb; --ok: #1d7549; --ok-soft: #e0f1e7; --warn: #8f5400; --warn-soft: #fbeed6;
  --bad: #a3322b; --bad-soft: #f8e3e1; --quote: #f7f8fa;
  --display: "Public Sans", "Segoe UI", system-ui, sans-serif; --body: "Public Sans", "Segoe UI", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --paper: #0e1319; --sheet: #151c24; --ink: #e4e9ef; --ink-2: #9fabb9; --rule: #2a3542;
  --accent: #91afff; --accent-soft: #1c2944; --ok: #74d3a2; --ok-soft: #15301f; --warn: #f0b661; --warn-soft: #382a12;
  --bad: #f2948a; --bad-soft: #3a1c19; --quote: #111820; color-scheme: dark } }
:root[data-theme="dark"] {
  --paper: #0e1319; --sheet: #151c24; --ink: #e4e9ef; --ink-2: #9fabb9; --rule: #2a3542;
  --accent: #91afff; --accent-soft: #1c2944; --ok: #74d3a2; --ok-soft: #15301f; --warn: #f0b661; --warn-soft: #382a12;
  --bad: #f2948a; --bad-soft: #3a1c19; --quote: #111820; color-scheme: dark }
* { box-sizing: border-box }
body { margin: 0; background: var(--paper); color: var(--ink); font: 15px/1.5 var(--body); }
a { color: var(--accent); text-underline-offset: 2px }
a:focus-visible, button:focus-visible, input:focus-visible, select:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.wrap { max-width: 1240px; margin: 0 auto; padding-inline: 16px; padding-block: 20px 40px }
header.top { display: flex; flex-wrap: wrap; gap: 8px 24px; align-items: baseline; justify-content: space-between; padding-bottom: 14px; border-bottom: 1px solid var(--rule) }
h1 { font: 800 clamp(22px, 3vw, 30px)/1.15 var(--display); letter-spacing: -0.01em; margin: 0; text-wrap: balance }
.lede { color: var(--ink-2); margin: 4px 0 0; max-width: 70ch }
.stats { display: flex; flex-wrap: wrap; gap: 6px 18px; font: 500 13px/1.4 var(--mono); color: var(--ink-2) }
.stats b { color: var(--ink); font-weight: 500 }
.tools { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; padding-block: 14px }
.tools input[type=search] { flex: 1 1 220px; min-width: 0; padding: 8px 10px; border: 1px solid var(--rule); border-radius: 6px; background: var(--sheet); color: var(--ink); font: inherit }
.tools select { padding: 7px 8px; border: 1px solid var(--rule); border-radius: 6px; background: var(--sheet); color: var(--ink); font: inherit }
.seg { display: inline-flex; border: 1px solid var(--rule); border-radius: 6px; overflow: hidden }
.seg button { border: 0; background: var(--sheet); color: var(--ink-2); padding: 7px 11px; font: 500 13px var(--body); cursor: pointer }
.seg button + button { border-left: 1px solid var(--rule) }
.seg button[aria-pressed=true] { background: var(--accent-soft); color: var(--accent) }
.grid { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 18px; align-items: start }
@media (max-width: 860px) { .grid { grid-template-columns: minmax(0, 1fr) } }
.ledger { background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; overflow: hidden }
.row { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 2px 10px; padding: 10px 14px; border-bottom: 1px solid var(--rule); cursor: pointer; background: none; border-left: 0; border-right: 0; border-top: 0; width: 100%; text-align: left; color: inherit; font: inherit }
.row:last-child { border-bottom: 0 }
.row:hover { background: var(--quote) }
.row[aria-current=true] { background: var(--accent-soft) }
.row .nm { font-weight: 600; min-width: 0; overflow-wrap: anywhere }
.row .sub { grid-column: 1 / -1; display: flex; flex-wrap: wrap; gap: 4px 14px; font: 12.5px/1.4 var(--mono); color: var(--ink-2) }
.stamp { font: 500 12px/1 var(--mono); border: 1.5px solid currentColor; outline: 1px solid currentColor; outline-offset: 1.5px; border-radius: 2px; padding: 3px 5px; color: var(--accent); align-self: center }
.stamp.B { color: var(--ink-2) }
.stamp.R { color: var(--warn) }
.chg { color: var(--warn) }
.sheet { background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; padding: 18px 20px 22px; position: sticky; top: calc(env(safe-area-inset-top, 0px) + 12px); max-height: calc(100vh - 24px); overflow: auto }
@media (max-width: 860px) { .sheet { position: static; max-height: none } }
.sheet h2 { font: 800 22px/1.2 var(--display); margin: 0; text-wrap: balance }
.legal { color: var(--ink-2); font-size: 13.5px; margin-top: 2px }
.legal code, .mono { font: 13px var(--mono) }
.facts { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px 18px; margin: 16px 0 6px; padding: 12px 0; border-block: 1px solid var(--rule) }
.fact .k { font: 600 11px/1.3 var(--body); text-transform: uppercase; letter-spacing: .06em; color: var(--ink-2) }
.fact .v { font-weight: 500; overflow-wrap: anywhere }
.fact .v.num { font: 500 15px var(--mono); font-variant-numeric: tabular-nums }
h3 { font: 600 12px/1.3 var(--body); text-transform: uppercase; letter-spacing: .07em; color: var(--ink-2); margin: 20px 0 8px }
.chips { display: flex; flex-wrap: wrap; gap: 5px }
.chip { font: 500 12px/1.2 var(--mono); padding: 3px 7px; border-radius: 999px; background: var(--quote); border: 1px solid var(--rule); color: var(--ink-2) }
.chip.ok { background: var(--ok-soft); color: var(--ok); border-color: transparent }
.chip.warn { background: var(--warn-soft); color: var(--warn); border-color: transparent }
.chip.acc { background: var(--accent-soft); color: var(--accent); border-color: transparent }
.ev { border-top: 1px solid var(--rule); padding: 10px 0 }
.ev:first-of-type { border-top: 0 }
.ev .head { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline }
.ev .date { font: 500 13px var(--mono); min-width: 7.5ch; font-variant-numeric: tabular-nums }
.ev .co { font-weight: 600 }
.src { margin-top: 6px; display: grid; gap: 6px }
blockquote { margin: 0; padding: 7px 10px; background: var(--quote); border-left: 2px solid var(--rule); font-size: 13.5px; color: var(--ink); overflow-wrap: anywhere }
blockquote.counted { border-left-color: var(--accent) }
.meta { font: 12px/1.4 var(--mono); color: var(--ink-2); display: flex; flex-wrap: wrap; gap: 2px 10px }
.notes li { margin: 3px 0 }
.cmp { width: 100%; border-collapse: collapse; font-size: 13.5px }
.cmp th, .cmp td { text-align: left; padding: 5px 8px; border-bottom: 1px solid var(--rule); vertical-align: top }
.cmp th { font: 600 11px var(--body); text-transform: uppercase; letter-spacing: .06em; color: var(--ink-2) }
.cmp td.num { font-family: var(--mono); font-variant-numeric: tabular-nums }
.tblwrap { overflow-x: auto }
.empty { color: var(--ink-2); font-style: italic }
footer { margin-top: 22px; color: var(--ink-2); font-size: 13px; max-width: 80ch }
@media (prefers-reduced-motion: no-preference) { .row { transition: background .12s } }
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
const day = d => d ? d : "bez dátumu";
let state = {q: "", country: "", sector: "", sort: "name", sel: null};
try { const s = JSON.parse(localStorage.getItem("investor-explorer") || "{}"); Object.assign(state, {sort: s.sort || "name"}); } catch (e) {}

const invs = DATA.investors;
const sectors = [...new Set(invs.flatMap(i => i.sectors))].sort((a, b) => (SECTOR[a]||a).localeCompare(SECTOR[b]||b, "sk"));
document.getElementById("sector").innerHTML += sectors.map(s => `<option value="${esc(s)}">${esc(SECTOR[s]||s)}</option>`).join("");
document.getElementById("sort").value = state.sort;
const m = DATA.meta;
document.getElementById("stats").innerHTML = [
  `<span><b>${invs.filter(i => i.status === "INCLUDED").length}</b> zaradených</span>`,
  `<span>stav k <b>${esc(m.as_of)}</b></span>`,
  m.precision ? `<span>presnosť <b>${esc(m.precision)}</b></span>` : "",
  `<span>${m.refined ? "<b>spresnené</b> (Sonnet 5.5)" : "zmrazená verzia"}</span>`].join("");
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
  document.getElementById("list").innerHTML = list.length ? list.map(i => `
    <button type="button" class="row" data-id="${esc(i.id)}" aria-current="${i.id === state.sel}">
      <span class="nm">${esc(i.name)}</span>
      <span class="stamp ${i.status === "INCLUDED" ? esc(i.tier) : "R"}" title="${i.status === "INCLUDED" ? "úroveň dôkazov " + esc(i.tier) : "na kontrolu"}">${i.status === "INCLUDED" ? esc(i.tier) : "?"}</span>
      <span class="sub"><span>${esc(i.hq)}</span><span>${eur(i.capital)}</span><span>posledný obchod ${esc(i.last_date || "–")}</span>${changed(i) && DATA.meta.refined ? '<span class="chg">spresnené</span>' : ""}</span>
    </button>`).join("") : `<p class="empty" style="padding:14px">Žiadny investor nevyhovuje filtru.</p>`;
  renderSheet();
}
function quoteBlock(s) {
  return `<div><blockquote class="${s.counted ? "counted" : ""}">${esc(s.quote)}</blockquote>
    <div class="meta"><span>${link(s.url, s.domain)}</span>${s.published ? `<span>publikované ${esc(s.published)}</span>` : ""}<span>${esc(s.tier)}</span>${s.context ? `<span>${s.context === "deal" ? "správa o obchode" : "zmienka"}</span>` : ""}${s.refined ? "<span>spresnenie</span>" : ""}</div></div>`;
}
function renderSheet() {
  const i = invs.find(x => x.id === state.sel);
  const el = document.getElementById("sheet");
  if (!i) { el.innerHTML = `<p class="empty">Vyberte investora v zozname.</p>`; return; }
  const ticket = i.ticket_eur[0] || i.ticket_eur[1] ? `${eur(i.ticket_eur[0])} – ${eur(i.ticket_eur[1])}` : "neuvedené";
  const b = i.before;
  const capChanged = (b.capital ?? null) !== (i.capital ?? null);
  const rows = [
    ["Celkový kapitál", eur(b.capital) + (b.capital_method ? ` <span class="meta">${esc(b.capital_method)}</span>` : ""), eur(i.capital) + (i.capital_method ? ` <span class="meta">${esc(i.capital_method)}</span>` : ""), capChanged],
    ["Posledný obchod", `${esc(b.last_date || "–")} ${esc(b.last_company)}`, `${esc(i.last_date || "–")} ${esc(i.last_company)}`, b.last_date !== i.last_date],
    ["Obchody za 36 mes.", b.n_36m, i.n_36m, b.n_36m !== i.n_36m],
    ["Úroveň", b.tier || "–", i.status === "INCLUDED" ? (i.tier || "–") : "na kontrolu", b.tier !== i.tier || i.status !== "INCLUDED"]];
  el.innerHTML = `
    <h2>${esc(i.name)}</h2>
    <div class="legal">${esc(i.legal_name)} · IČO <code>${esc(i.company_id)}</code> · ${link(i.registry_url, "záznam v registri")}${i.website ? " · " + link(i.website, i.website.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, "")) : ""}</div>
    ${i.status !== "INCLUDED" ? `<p class="chip warn" style="display:inline-block;margin-top:10px">Na kontrolu: ${esc(i.explanation)}</p>` : ""}
    <div class="facts">
      <div class="fact"><div class="k">Sídlo</div><div class="v">${esc(i.hq)}</div></div>
      <div class="fact"><div class="k">Typ</div><div class="v">${esc(i.types.map(t => TYPE[t] || t).join(", ") || "–")}</div></div>
      <div class="fact"><div class="k">Celkový kapitál</div><div class="v num">${eur(i.capital)}</div></div>
      <div class="fact"><div class="k">Tiket</div><div class="v num">${ticket}</div></div>
      <div class="fact"><div class="k">Obchody</div><div class="v num">${i.n_inv} · ${i.n_36m} za 36 mes.</div></div>
    </div>
    <div class="chips">${i.sectors.map(s => `<span class="chip acc">${esc(SECTOR[s] || s)}</span>`).join("")}${i.stages.map(s => `<span class="chip">${esc(STAGE[s] || s)}</span>`).join("")}</div>
    ${DATA.meta.refined ? `<h3>Pred a po spresnení</h3><div class="tblwrap"><table class="cmp"><thead><tr><th></th><th>zmrazené (v3)</th><th>spresnené</th></tr></thead><tbody>
      ${rows.map(r => `<tr><th scope="row">${r[0]}</th><td class="num">${r[1]}</td><td class="num${r[3] ? " chg" : ""}">${r[2]}</td></tr>`).join("")}</tbody></table></div>
      ${i.notes.length ? `<ul class="notes">${i.notes.map(n => `<li>${esc(n)}</li>`).join("")}</ul>` : `<p class="empty">Spresnenie nič nezmenilo.</p>`}` : ""}
    <h3>Kapitál a fondy</h3>
    ${i.funds.length ? i.funds.map(f => `<div class="ev"><div class="head"><span class="co">${esc(f.name || "AUM")}</span><span class="mono">${esc(f.size || "")}</span>
      ${f.status ? `<span class="chip ${FUND[f.status]?.[1] || ""}">${esc(FUND[f.status]?.[0] || f.status)}</span>` : ""}${f.counted ? `<span class="chip ok">započítané</span>` : ""}</div>
      <div class="src">${quoteBlock({...f, tier: "", context: "", counted: f.counted})}</div></div>`).join("") : `<p class="empty">Zdroje veľkosť fondov neuvádzajú.</p>`}
    ${i.targets ? `<p class="meta">Len plánované, nezapočítané: ${esc(i.targets)}</p>` : ""}
    <h3>Investície (${i.deals.length})</h3>
    ${i.deals.map(d => `<div class="ev"><div class="head"><span class="date">${esc(day(d.date))}</span><span class="co">${esc(d.company)}</span>
      ${d.round && d.round !== "unknown" ? `<span class="chip">${esc(STAGE[d.round] || d.round)}</span>` : ""}${d.amount ? `<span class="chip">${esc(d.amount)}</span>` : ""}</div>
      <details><summary class="meta">${d.sources.length} ${d.sources.length === 1 ? "zdroj" : "zdroje"} · ${esc(d.sources.map(s => s.domain).filter((v, k, a) => a.indexOf(v) === k).join(", "))}</summary>
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
