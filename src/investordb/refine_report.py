"""docs/REFINEMENT.md - what the refinement stage (D38) changed, and whether it made the data more accurate."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path

from investordb.metrics import wilson
from investordb.refine import CLAIMS_GAPFILL, GAP_FIELDS, GAPFILL_DIR, JUDGE_DIR, filled, judge_metrics, summary

GAP_LABEL = {"sectors": "Sektory", "stages": "Štádiá", "ticket": "Tiket", "total_capital": "Celkový kapitál"}


def gapfill_section(rows: dict) -> list[str]:
    """D41: what the gap-filling agent found for the fields the assignment names, and what is not public."""
    batches = [r for p in sorted((GAPFILL_DIR / "batches").glob("gf_b*.json"))
               for r in json.loads(p.read_text(encoding="utf-8"))]
    if not batches or not CLAIMS_GAPFILL.exists():
        return []
    with CLAIMS_GAPFILL.open(encoding="utf-8") as f:
        claims = list(csv.DictReader(f))
    missing = {b["candidate_id"]: b["missing"] for b in batches}
    out = ["## 6. Doplnenie chýbajúcich polí (D41)\n",
           "Zadanie žiada pri každom investorovi sektor, typickú investíciu a jej veľkosť a celkový kapitál. Po spresnení "
           "niektoré z týchto polí chýbali. Agent Sonnet 5.5 ([pokyn](../prompts/gapfill_agent.md)) hľadal **len "
           "chýbajúce polia**; sektory smel odvodiť z portfólia (každý odvodený sektor dokladá citácia o firme z "
           "portfólia a v dátach je označený `inferred`), tiket a kapitál len ak ich zdroj uvádza. Pole, ktoré nenašiel, "
           "je v stĺpci `not_public` – nie prázdne a nie odhadnuté.\n",
           "| Pole | Vyplnené pred | Doplnené | Verejne neuvedené | Vyplnené po |\n|---|---|---|---|---|"]
    for field in GAP_FIELDS:
        need = [cid for cid, m in missing.items() if field in m]
        done = [cid for cid in need if filled(rows[cid], field)]
        not_public = [cid for cid in need if field in (rows[cid].get("not_public") or "").split("; ")]
        before = len(rows) - len(need)
        out.append(f"| {GAP_LABEL[field]} | {before}/{len(rows)} | +{len(done)} | {len(not_public)} | "
                   f"**{before + len(done)}/{len(rows)}** |")
    checks = Counter(c["auto_check"] for c in claims)
    out.append(f"\nStrojová kontrola doplnených tvrdení: " + ", ".join(f"`{k}` {v}" for k, v in checks.most_common())
               + ".\n")
    out.append("| Investor | Chýbalo | Výsledok |\n|---|---|---|")
    for cid, need in missing.items():
        r = rows[cid]
        res = []
        for field in need:
            if filled(r, field):
                if field in ("sectors", "stages"):
                    val = r[field].replace(",", ", ") + (" (odvodené z portfólia)" if r.get(f"{field}_basis") == "inferred" else "")
                elif field == "ticket":
                    lo, hi = (f"{float(x) / 1e6:.2f}" if x else "?" for x in (r["ticket_min_eur"], r["ticket_max_eur"]))
                    val = f"{lo} – {hi} mil. €" if r["ticket_min_eur"] else f"do {hi} mil. €"
                else:
                    val = f"{float(r['total_capital_eur']) / 1e6:.1f} mil. €"
                res.append(f"{GAP_LABEL[field].lower()}: {val}")
            else:
                res.append(f"{GAP_LABEL[field].lower()}: verejne neuvedené")
        out.append(f"| {r['name']} | {', '.join(GAP_LABEL[f].lower() for f in need)} | {'; '.join(res)} |")
    out.append("")
    return out

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "REFINEMENT.md"

FIELD_SK = {"funds": "fondy", "investments": "investície"}
VERDICT_SK = {"confirmed": "dátum potvrdený", "corrected": "dátum opravený", "not_found": "dátum sa nenašiel",
              "not_this_investor": "investor sa na kole nepodieľal", "new": "nový novší obchod"}
STATUS_SK = {"final_close": "uzavretý fond", "first_close": "prvé uzavretie", "target": "len cieľ / plán"}


def pct(p: float) -> str:
    return f"{100 * p:.1f} %"


def ci(k: int, n: int) -> str:
    if not n:
        return "–"
    p, lo, hi = wilson(k, n)
    return f"**{k}/{n} = {pct(p)}** (95 % CI {pct(lo)} – {pct(hi)})"


def _eur(v: str) -> str:
    return f"{float(v) / 1e6:,.1f} mil. €".replace(",", " ") if v else "–"


def build(result: dict, as_of: date) -> str:
    s = summary(result)
    before, rows = result["before"], result["rows"]
    lines: list[str] = []
    add = lines.append
    add("# Spresnenie slabých polí silnejším modelom (D38)\n")
    add(f"*Generované skriptom `python -m investordb.cli refine report` (`as_of` = {as_of}). Zmrazená databáza "
        "(tag `pilot-frozen-v3`) zostáva nezmenená a meraná v [PRECISION_REPORT.md](PRECISION_REPORT.md); spresnená "
        "verzia je v `data/processed/investors_refined.csv`.*\n")

    add("## 1. Prečo\n")
    add("Slepá kontrola vzorky (Sonnet 5.5) a ručná kontrola autora ukázali, že **kto** je v databáze, je správne "
        "(23/23), ale dve polia sú slabé: **celkový kapitál** (správny len v 6 z 12 hodnotených záznamov – cieľové "
        "veľkosti fondov a prvé uzavretia počítané ako uzavreté fondy, staršie fondy chýbali) a **dátumy obchodov** "
        "(zdroje sedeli v 19 z 23 záznamov – ako dátum obchodu sa niekedy použil dátum článku, ktorý staršiu investíciu "
        "len spomína). Haiku na takéto čítanie článkov nestačil.\n")

    add("## 2. Ako\n")
    add("- **Agent:** Claude Sonnet 5.5, [pokyn](../prompts/refine_agent.md), 6 agentov po 4 investoroch – všetkých "
        f"{len(before)} zaradených. Dostal, čo databáza tvrdí (fondy, datované obchody), a mal to overiť.\n"
        "- **Úloha A – fondy:** každý fond so stavom zbierky (`final_close` / `first_close` / `target`), sumou a "
        "doslovnou citáciou. Kapitál = súčet uzavretých fondov + prvých uzavretí; cieľ sa nepočíta. Program navyše "
        "odmietne sumu, pred ktorou citácia hovorí „target / cieľová / až“ (`target_near`), aj keď agent tvrdí opak.\n"
        "- **Úloha B – dátumy:** pre každý započítaný obchod dátum, keď bola investícia prvýkrát oznámená, s verdiktom "
        "potvrdený / opravený / nenájdený / iný investor.\n"
        "- **Rovnaké strojové kontroly** ako všetky ostatné tvrdenia: citácia na stránke, hodnota v citácii, kontext "
        "obchodu, priradenie investorovi.\n"
        "- **Pravidlá zlúčenia:** overený spresnený dátum nahradí pôvodný; dátum, ktorý agent nepotvrdil, sa prestane "
        "počítať (firma ostane v portfóliu ako zmienka); ak by záznam po spresnení prestal spĺňať pravidlá, nevyradí "
        "sa, ale ide na ručnú kontrolu (`REVIEW_REFINED`).\n")

    add("## 3. Strojové kontroly spresnených tvrdení\n")
    add("| Pole | Výsledok kontroly | Počet |\n|---|---|---|")
    for (field, status), n in sorted(s["auto_check"].items()):
        add(f"| {FIELD_SK.get(field, field)} | `{status}` | {n} |")
    add("")
    add("Stav fondov podľa agenta: " + ", ".join(f"{STATUS_SK.get(k, k)} {v}×" for k, v in s["fund_status"].most_common())
        + ".  ")
    add("Verdikty k dátumom obchodov: " + ", ".join(f"{VERDICT_SK.get(k, k)} {v}×" for k, v in s["verdicts"].most_common())
        + ".\n")

    add("## 4. Čo sa v databáze zmenilo\n")
    cap_b = sum(1 for r in before.values() if r["total_capital_eur"])
    cap_a = sum(1 for r in rows.values() if r["total_capital_eur"])
    cap_changed = [cid for cid in rows if before[cid]["total_capital_eur"] != rows[cid]["total_capital_eur"]]
    last_changed = [cid for cid in rows if before[cid]["last_investment_date"] != rows[cid]["last_investment_date"]]
    status_changed = [cid for cid in rows if rows[cid]["status"] != "INCLUDED"]
    tier_changed = [cid for cid in rows if rows[cid]["status"] == "INCLUDED" and rows[cid]["tier"] != before[cid]["tier"]]
    add(f"- Kapitál vyplnený: {cap_b}/{len(before)} → **{cap_a}/{len(rows)}**; zmenená hodnota pri **{len(cap_changed)}** "
        "investoroch.")
    add(f"- Posledný obchod sa zmenil pri **{len(last_changed)}** investoroch; úroveň dôkazov (A/B) pri "
        f"**{len(tier_changed)}**.")
    add(f"- Na ručnú kontrolu po spresnení (`REVIEW_REFINED`): **{len(status_changed)}**"
        + (": " + ", ".join(rows[c]["name"] for c in status_changed) if status_changed else "") + ".")
    if result["problems"]:
        add("- Integritné kontroly: " + "; ".join(result["problems"]))
    else:
        add("- Integritné kontroly (každý zaradený má overený datovaný obchod v okne, kapitál má overené tvrdenie): bez chýb.")
    add("")
    add("| Investor | Kapitál pred | Kapitál po | Posledný obchod pred | po | Obchody 36 m pred → po | Zmeny |")
    add("|---|---|---|---|---|---|---|")
    for cid in sorted(rows, key=lambda c: rows[c]["name"].lower()):
        b, a = before[cid], rows[cid]
        notes = a.get("refine_notes", "")
        status = "" if a["status"] == "INCLUDED" else " **→ na kontrolu**"
        add(f"| {a['name']}{status} | {_eur(b['total_capital_eur'])} | {_eur(a['total_capital_eur'])} | "
            f"{b['last_investment_date'] or '–'} | {a['last_investment_date'] or '–'} | "
            f"{b['n_investments_36m']} → {a['n_investments_36m']} | {notes.replace('|', '/') or '–'} |")
    add("")

    add("## 5. Je spresnená verzia presnejšia? (slepá kontrola faktov)\n")
    if not (JUDGE_DIR / "key.csv").exists() or not any(JUDGE_DIR.glob("j_b*.json")):
        add("*Kontrola faktov ešte nebežala.*\n")
        return "\n".join(lines)
    j = judge_metrics()
    add("Hodnoty z oboch verzií (zmrazenej aj spresnenej) dostal **nový** agent Sonnet 5.5 "
        "([pokyn](../prompts/refine_judge_agent.md)) zmiešané, zoradené náhodne a **bez informácie, z ktorej verzie "
        "pochádzajú**. Každú hodnotu overil v zdrojoch. Rovnaká hodnota v oboch verziách sa hodnotila raz. "
        f"Ohodnotených položiek: {j['answered']} z {j['items']}.\n")
    add("| Pole | Zmrazená verzia (v3) | Spresnená verzia |\n|---|---|---|")
    for typ, label in (("capital", "Celkový kapitál správny"), ("deal", "Obchod: investor + dátum (±2 mesiace) správne"),
                       ("identity", "Identita v registri správna")):
        b, a = j[(typ, "before")], j[(typ, "after")]
        add(f"| {label} | {ci(b['yes'], b['n'])} | {ci(a['yes'], a['n'])} |")
    add("")
    add("Prísne počítanie: „neviem“ = nepotvrdené. Rozpis odpovedí:\n")
    add("| Pole | Verzia | Odpovede |\n|---|---|---|")
    for typ in ("capital", "deal", "identity"):
        for version, label in (("before", "zmrazená"), ("after", "spresnená")):
            ans = j[(typ, version)]["answers"]
            add(f"| {typ} | {label} | " + ", ".join(f"{k} {v}" for k, v in sorted(ans.items())) + " |")
    add("")
    wrong = [(k, a) for k, a in j["answers"].items() if a["answer"] != "yes" and j["key"][k]["after"] == "1"]
    if wrong:
        add("### Hodnoty spresnenej verzie, ktoré kontrola nepotvrdila\n")
        add("| Položka | Typ | Odpoveď | Zdôvodnenie |\n|---|---|---|---|")
        for k, a in sorted(wrong):
            add(f"| {k} | {j['key'][k]['type']} | {a['answer']} | {str(a.get('why', '')).replace('|', '/')[:300]} |")
        add("")

    add("### Výklad (napísaný ručne k behu z 9. 10. 2026)\n")
    add("- **Dátumy obchodov:** všetkých 14 chýb zmrazenej verzie je rovnakého typu – dátum prehľadového článku, ktorý "
        "staršiu investíciu len spomína (portfólio v článku o novom fonde). Spresnenie ich opravilo. Zostali 2 chyby: "
        "blogový príspevok investora z apríla 2026 opakuje oznámenie kola z marca 2025 (ArtMaster).\n"
        "- **Kapitál:** zmrazená verzia chybovala hlavne tým, že započítala **cieľ** fondu (Presto, Purple, Tensor, "
        "ZAKA) alebo vynechala starší fond (Rockaway, Tilia, Reflex). Spresnená verzia ciele nepočíta; zvyšné chyby "
        "sú **podhodnotenia** – chýba fond, navýšenie kapitálu alebo AUM, ktoré investor uvádza na webe (Neulogy "
        "65 mil. €). Ďalší krok: v pokyne žiadať aj AUM uvádzané investorom a navýšenia kapitálu. Znovu to spustiť a "
        "merať tou istou kontrolou by však bolo ladenie na testovacích dátach, preto to ostáva ako odporúčanie.\n"
        "- **Identita v registri:** 24/24 vrátane 8 záznamov, ktorých identita sa zmenila vo v3 a ktorých opakovaná "
        "kontrola predtým zlyhala na limite relácie (D36).\n")
    lines.extend(gapfill_section(rows))
    add("## 7. Obmedzenia\n")
    add("- Spresňoval aj kontroloval model tej istej rodiny (Sonnet 5.5). Kontrolór bol iný agent bez prístupu k "
        "výstupu spresnenia a nevedel, ktorá hodnota je nová, chyby oboch však môžu byť korelované. Rozhodujúce je "
        "preto, že každé nové tvrdenie prešlo rovnakými strojovými kontrolami ako zvyšok databázy.\n"
        "- Kontrola faktov meria hodnoty, ktoré v databáze **sú**. Chýbajúci kapitál (neuvedené) sa do presnosti "
        "nepočíta – vyplnenosť je uvedená zvlášť v kap. 4.\n"
        "- Spresnenie je po zmrazení: primárna metrika presnosti záznamov (PRECISION_REPORT) sa ním nemení.\n")
    return "\n".join(lines)


def write(result: dict, as_of: date) -> Path:
    OUT.write_text(build(result, as_of), encoding="utf-8")
    return OUT
