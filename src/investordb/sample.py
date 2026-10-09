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
    ("active_36m", "Má doloženú investíciu do firmy uskutočnenú v posledných 36 mesiacoch (od 2023-10-09)?"),
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
        # only investments the pipeline actually counts: no exits, investor named; a date only if it is a deal date
        if c["field"] == "investments" and c.get("deal_context") != "exit" and c.get("attributed") != "0":
            v = json.loads(c["value"]) or {}
            date = c["event_date"][:{"year": 4, "month": 7}.get(c.get("event_date_precision"), 10)] \
                if c.get("deal_context") == "deal" and c["event_date"] else ""
            investments.append({"company": v.get("company"), "date": date, "url": c["source_url"]})
    sources = sorted({c["source_url"] for c in ok})
    return {
        "name": decision["name"], "website": decision["website"], "legal_name": decision["legal_name"],
        "company_id": decision["company_id"], "registry_url": decision["registry_url"],
        "hq_country": decision["hq_country"], "types": decision["investor_types"], "sectors": decision["sectors"],
        "stages": decision["stages"],
        "ticket": " – ".join(x for x in (decision["ticket_min"], decision["ticket_max"]) if x),
        "total_capital_eur": decision["total_capital_eur"], "capital_method": decision["capital_method"],
        "capital_note": decision.get("capital_note", ""), "funds_target": decision.get("funds_target", ""),
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


def refresh() -> list[str]:
    """Re-render the SAME sample (same review IDs, same records) from the current pipeline output.
    Used after a re-freeze, so a reviewer's answers - stored per review ID - stay valid. Returns review IDs whose
    displayed record changed."""
    key = _read(REVIEW_DIR / "review_key.csv")
    decisions = {d["candidate_id"]: d for d in _read(DECISIONS_CSV)}
    claims = _read(CLAIMS_CSV)
    old = {r["review_id"]: r for r in json.loads((REVIEW_DIR / "review_records.json").read_text(encoding="utf-8"))}
    records, changed = [], []
    for k in key:
        d = decisions[k["candidate_id"]]
        rec = {"review_id": k["review_id"], **claimed_view(k["candidate_id"], claims, d)}
        if rec != old.get(k["review_id"]):
            changed.append(k["review_id"])
        records.append(rec)
        k.update(status=d["status"], reason=d["reason"], tier=d["tier"])
    with (REVIEW_DIR / "review_key.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(key[0].keys()))
        w.writeheader()
        w.writerows(key)
    (REVIEW_DIR / "review_records.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    (REVIEW_DIR / "review.html").write_text(render_form(records), encoding="utf-8")
    spot_ids = [r["review_id"] for r in _read(REVIEW_DIR / "spotcheck_ids.csv")]
    if spot_ids:
        by_id = {r["review_id"]: r for r in records}
        (REVIEW_DIR / "spotcheck.html").write_text(
            render_form([by_id[i] for i in spot_ids], key="investordb-spotcheck-v2", filename="spotcheck_results.csv"),
            encoding="utf-8")
    return changed


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


def _overall(answers: dict) -> str:
    vals = [(answers.get(k) or {}).get("answer", "cannot_tell") for k, _ in PRIMARY]
    return "exclude" if "no" in vals else "include" if all(v == "yes" for v in vals) else "cannot_tell"


def _ai_answers(folder: Path, pattern: str) -> dict[str, dict]:
    out = {}
    for path in sorted(folder.glob(pattern)):
        for r in json.loads(path.read_text(encoding="utf-8")):
            out[r["review_id"]] = r
    return out


SPOTCHECK_SEED = 20261009


def build_spotcheck(target: int = 10, min_random: int = 3) -> Path:
    """Human audit of the AI review (D34): every record where Sonnet and the Haiku verifier disagree (or Sonnet cannot
    tell) + random agreeing records as an unbiased control. The form does not show why a record was picked."""
    sonnet = _ai_answers(REVIEW_DIR / "sonnet", "s_b*.json")
    haiku = _ai_answers(ROOT / "data" / "raw" / "agents" / "verifier", "v_b*.json")
    records = {r["review_id"]: r for r in json.loads((REVIEW_DIR / "review_records.json").read_text(encoding="utf-8"))}
    disputed = sorted(rid for rid in records if rid in sonnet and (
        _overall(sonnet[rid]) == "cannot_tell" or _overall(sonnet[rid]) != _overall(haiku.get(rid, {}))))
    agreeing = sorted(rid for rid in records if rid not in disputed)
    n_random = max(min_random, target - len(disputed))
    control = random.Random(SPOTCHECK_SEED).sample(agreeing, min(n_random, len(agreeing)))
    picked = disputed + control
    random.Random(SPOTCHECK_SEED).shuffle(picked)
    with (REVIEW_DIR / "spotcheck_ids.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["review_id", "why_selected", "sonnet_overall", "haiku_overall"])
        for rid in picked:
            w.writerow([rid, "disagreement" if rid in disputed else "random_control",
                        _overall(sonnet.get(rid, {})), _overall(haiku.get(rid, {}))])
    path = REVIEW_DIR / "spotcheck.html"
    path.write_text(render_form([records[rid] for rid in picked], key="investordb-spotcheck-v2",
                                filename="spotcheck_results.csv"), encoding="utf-8")
    return path


def render_form(records: list[dict], key: str = "investordb-review-v2", filename: str = "review_results.csv") -> str:
    questions = json.dumps({"primary": PRIMARY, "secondary": SECONDARY}, ensure_ascii=False)
    data = json.dumps(records, ensure_ascii=False)
    return (TEMPLATE.replace("__DATA__", data).replace("__QUESTIONS__", questions).replace("__N__", str(len(records)))
            .replace("investordb-review-v2", key).replace("review_results.csv", filename))


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
const DATA=__DATA__, Q=__QUESTIONS__, KEY='investordb-review-v2';
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
 <dt>Celkový kapitál</dt><dd>${r.total_capital_eur?Number(r.total_capital_eur).toLocaleString('sk')+' € ('+esc(r.capital_method)+')':'–'}${r.capital_note?'<br><small>'+esc(r.capital_note)+'</small>':''}</dd>
 <dt>Plánované fondy</dt><dd>${esc(r.funds_target)||'–'}</dd>
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
