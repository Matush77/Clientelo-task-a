"""Draw the stratified random sample for manual review and build a blind review form.

Strata (docs/PLAN.md, chapter 9): ~30 INCLUDED (all of them if <= 35), 5 real rejects, 5 control-set rejects.
The reviewer sees claimed values and source URLs only - not the agents' quotes, not the pipeline's verdict/tier.
The key (review_id -> candidate, verdict) is written to a separate file the reviewer should not open.
"""

from __future__ import annotations

import csv
import html
import json
import random
from collections import defaultdict
from pathlib import Path

from investordb.batches import CALIBRATION_IDS
from investordb.candidates import OUT as CANDIDATES_CSV
from investordb.evidence import CLAIMS_CSV

ROOT = Path(__file__).resolve().parents[2]
REVIEW_DIR = ROOT / "data" / "review"
DECISIONS_CSV = CLAIMS_CSV.with_name("decisions.csv")
SEED = 20261012
N_INCLUDED, CENSUS_UP_TO, N_REAL_REJECTS, N_CONTROLS = 30, 35, 5, 5

PRIMARY = [
    ("real_investor", "Je to skutočný investor (investuje vlastné/spravované peniaze do firiem)?"),
    ("active_36m", "Má doloženú investíciu do firmy v posledných 36 mesiacoch (od 2023-10-08)?"),
    ("type_vc", "Je to VC investor (VC, korporátny VC alebo štátny VC investujúci priamo)?"),
    ("hq_cz_sk", "Sídli investičný tím v Česku alebo na Slovensku?"),
]
SECONDARY = [
    ("sources_support", "Podporujú uvedené zdroje uvedené investície (firma + dátum)?"),
    ("sectors_ok", "Sú uvedené sektory správne?"),
    ("ticket_ok", "Je uvedená výška tiketu správna?"),
    ("capital_ok", "Je uvedený celkový kapitál správny?"),
]


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def draw(decisions: list[dict], controls: set[str]) -> list[tuple[str, dict]]:
    rng = random.Random(SEED)
    pool = [d for d in decisions if d["candidate_id"] not in CALIBRATION_IDS]
    included = [d for d in pool if d["status"] == "INCLUDED"]
    real_rejects = [d for d in pool if d["status"] in ("REJECTED", "OOS") and d["candidate_id"] not in controls]
    control_rejects = [d for d in pool if d["status"] in ("REJECTED", "OOS") and d["candidate_id"] in controls]
    picked = [("included", d) for d in (included if len(included) <= CENSUS_UP_TO else rng.sample(included, N_INCLUDED))]
    picked += [("real_reject", d) for d in rng.sample(real_rejects, min(N_REAL_REJECTS, len(real_rejects)))]
    picked += [("control_reject", d) for d in rng.sample(control_rejects, min(N_CONTROLS, len(control_rejects)))]
    rng.shuffle(picked)
    return picked


def claimed_view(cid: str, claims: list[dict], decision: dict) -> dict:
    """What the pipeline claims about the record - verified values and source URLs, no quotes, no verdict."""
    ok = [c for c in claims if c["candidate_id"] == cid and c["auto_check"] == "ok"]
    investments = []
    for c in ok:
        if c["field"] == "investments":
            v = json.loads(c["value"]) or {}
            investments.append({"company": v.get("company"), "date": c["event_date"] or v.get("date"), "url": c["source_url"]})
    sources = sorted({c["source_url"] for c in ok})
    return {
        "name": decision["name"], "website": decision["website"], "legal_name": decision["legal_name"],
        "company_id": decision["company_id"], "registry_url": decision["registry_url"],
        "hq_country": decision["hq_country"], "types": decision["investor_types"], "sectors": decision["sectors"],
        "stages": decision["stages"],
        "ticket": " – ".join(x for x in (decision["ticket_min"], decision["ticket_max"]) if x),
        "total_capital_eur": decision["total_capital_eur"], "capital_method": decision["capital_method"],
        "funds": decision["funds"], "investments": sorted(investments, key=lambda i: i["date"] or "", reverse=True),
        "sources": sources,
    }


def build(out_dir: Path = REVIEW_DIR) -> Path:
    decisions = _read(DECISIONS_CSV)
    claims = _read(CLAIMS_CSV)
    controls = {c["candidate_id"] for c in _read(CANDIDATES_CSV) if c["control_category"]}
    picked = draw(decisions, controls)
    out_dir.mkdir(parents=True, exist_ok=True)

    records, key = [], []
    for n, (stratum, d) in enumerate(picked, 1):
        rid = f"R{n:02d}"
        records.append({"review_id": rid, **claimed_view(d["candidate_id"], claims, d)})
        key.append({"review_id": rid, "candidate_id": d["candidate_id"], "stratum": stratum, "status": d["status"],
                    "reason": d["reason"], "tier": d["tier"]})

    with (out_dir / "review_key.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(key[0].keys()))
        w.writeheader()
        w.writerows(key)
    (out_dir / "review_records.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    html_path = out_dir / "review.html"
    html_path.write_text(render_form(records), encoding="utf-8")
    return html_path


VERIFIER_BATCH_DIR = ROOT / "data" / "raw" / "agents" / "verifier" / "batches"


def make_verifier_batches(size: int = 5) -> list[Path]:
    """The verifier gets exactly the records (and the same information) the human reviewer gets."""
    records = json.loads((REVIEW_DIR / "review_records.json").read_text(encoding="utf-8"))
    VERIFIER_BATCH_DIR.mkdir(parents=True, exist_ok=True)
    paths = []
    for n, start in enumerate(range(0, len(records), size), 1):
        path = VERIFIER_BATCH_DIR / f"v_b{n:02d}.json"
        path.write_text(json.dumps(records[start:start + size], ensure_ascii=False, indent=1), encoding="utf-8")
        paths.append(path)
    return paths


def render_form(records: list[dict]) -> str:
    questions = json.dumps({"primary": PRIMARY, "secondary": SECONDARY}, ensure_ascii=False)
    data = json.dumps(records, ensure_ascii=False)
    return TEMPLATE.replace("__DATA__", data).replace("__QUESTIONS__", questions).replace("__N__", str(len(records)))


TEMPLATE = """<!doctype html>
<html lang="sk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ručná kontrola vzorky</title>
<style>
:root{--bg:#fafaf9;--card:#fff;--text:#1c1917;--muted:#57534e;--line:#e7e5e4;--accent:#1d4ed8;--ok:#15803d}
@media (prefers-color-scheme:dark){:root{--bg:#1c1917;--card:#292524;--text:#f5f5f4;--muted:#a8a29e;--line:#44403c;--accent:#93c5fd;--ok:#4ade80}}
body{margin:0;background:var(--bg);color:var(--text);font:15px/1.5 system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:16px}
h1{font-size:22px;margin:8px 0}.muted{color:var(--muted)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin:16px 0}
.card h2{font-size:18px;margin:0 0 8px}.card.done{border-color:var(--ok)}
dl{display:grid;grid-template-columns:150px 1fr;gap:4px 12px;margin:8px 0}dt{color:var(--muted)}dd{margin:0;overflow-wrap:anywhere}
a{color:var(--accent)} ul{margin:4px 0;padding-left:20px}
fieldset{border:0;border-top:1px solid var(--line);margin:10px 0 0;padding:8px 0 0}
.q{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px;padding:4px 0}.q span{flex:1 1 320px}
.q label{margin-right:10px;white-space:nowrap}
input[type=number]{width:70px}textarea{width:100%;min-height:40px;background:var(--bg);color:var(--text);border:1px solid var(--line)}
.bar{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
button{background:var(--accent);color:var(--bg);border:0;border-radius:6px;padding:8px 14px;font-weight:600;cursor:pointer}
</style></head><body><main>
<h1>Ručná kontrola vzorky – VC investori CZ + SK</h1>
<p class="muted">__N__ záznamov v náhodnom poradí. Pri každom otvorte zdroje (a podľa potreby si dohľadajte ďalšie) a odpovedzte
na otázky. Hodnoty sú tvrdenia pipeline – nie sú zaručene správne. Odpovede sa ukladajú v tomto prehliadači;
na konci kliknite <b>Exportovať CSV</b> a súbor uložte ako <code>data/review/review_results.csv</code>.</p>
<div class="bar"><button id="export">Exportovať CSV</button><span id="progress" class="muted"></span></div>
<div id="records"></div>
</main><script>
const DATA=__DATA__, Q=__QUESTIONS__, KEY='investordb-review-v1';
let answers={}; try{answers=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const link=u=>u?`<a href="${esc(u)}" target="_blank" rel="noopener">${esc(u)}</a>`:'–';
function radios(rid,name,opts){const cur=(answers[rid]||{})[name];
 return opts.map(o=>`<label><input type="radio" name="${rid}_${name}" value="${o}" ${cur===o?'checked':''}> ${o}</label>`).join('')}
function card(r){const inv=r.investments.length?'<ul>'+r.investments.map(i=>`<li>${esc(i.company)} – ${esc(i.date||'bez dátumu')} – ${link(i.url)}</li>`).join('')+'</ul>':'<i>žiadne doložené</i>';
 const src=r.sources.length?'<ul>'+r.sources.map(s=>`<li>${link(s)}</li>`).join('')+'</ul>':'–';
 const p=Q.primary.map(([k,t])=>`<div class="q"><span>${t}</span><span>${radios(r.review_id,k,['áno','nie','neviem'])}</span></div>`).join('');
 const s=Q.secondary.map(([k,t])=>`<div class="q"><span>${t}</span><span>${radios(r.review_id,k,['áno','nie','neviem','neuvedené'])}</span></div>`).join('');
 const a=answers[r.review_id]||{};
 return `<section class="card" id="${r.review_id}"><h2>${r.review_id} · ${esc(r.name)}</h2><dl>
 <dt>Web</dt><dd>${link(r.website)}</dd><dt>Právnická osoba</dt><dd>${esc(r.legal_name)||'–'} ${r.company_id?'(IČO '+esc(r.company_id)+')':''} ${r.registry_url?link(r.registry_url):''}</dd>
 <dt>Sídlo</dt><dd>${esc(r.hq_country)||'–'}</dd><dt>Typ</dt><dd>${esc(r.types)||'–'}</dd><dt>Sektory</dt><dd>${esc(r.sectors)||'–'}</dd>
 <dt>Štádiá</dt><dd>${esc(r.stages)||'–'}</dd><dt>Tiket</dt><dd>${esc(r.ticket)||'–'}</dd>
 <dt>Celkový kapitál</dt><dd>${r.total_capital_eur?Number(r.total_capital_eur).toLocaleString('sk')+' € ('+esc(r.capital_method)+')':'–'}</dd>
 <dt>Fondy</dt><dd>${esc(r.funds)||'–'}</dd><dt>Investície</dt><dd>${inv}</dd><dt>Všetky zdroje</dt><dd>${src}</dd></dl>
 <fieldset><b>Hlavné otázky</b>${p}</fieldset><fieldset><b>Polia</b>${s}</fieldset>
 <fieldset><label>Minúty na záznam <input type="number" min="0" name="${r.review_id}_minutes_spent" value="${esc(a.minutes_spent)}"></label>
 <textarea name="${r.review_id}_note" placeholder="Poznámka (voliteľné)">${esc(a.note)}</textarea></fieldset></section>`}
const keys=[...Q.primary,...Q.secondary].map(q=>q[0]);
function progress(){let done=0;DATA.forEach(r=>{const a=answers[r.review_id]||{};const ok=Q.primary.every(([k])=>a[k]);if(ok)done++;
 document.getElementById(r.review_id).classList.toggle('done',ok)});document.getElementById('progress').textContent=`Hotovo ${done} / ${DATA.length}`}
document.getElementById('records').innerHTML=DATA.map(card).join('');
document.addEventListener('input',e=>{const [rid,...rest]=e.target.name.split('_');const k=rest.join('_');
 answers[rid]=answers[rid]||{};answers[rid][k]=e.target.value;try{localStorage.setItem(KEY,JSON.stringify(answers))}catch(err){};progress()});
document.getElementById('export').onclick=()=>{const cols=['review_id',...keys,'minutes_spent','note'];
 const rows=[cols.join(',')].concat(DATA.map(r=>cols.map(c=>{const v=c==='review_id'?r.review_id:((answers[r.review_id]||{})[c]??'');return '"'+String(v).replace(/"/g,'""')+'"'}).join(',')));
 const blob=new Blob(['\\ufeff'+rows.join('\\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='review_results.csv';a.click()};
progress();
</script></body></html>"""


if __name__ == "__main__":
    print(build())
