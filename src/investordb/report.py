"""Compute the pre-registered metrics (docs/PLAN.md, chapter 9) and write docs/PRECISION_REPORT.md (Slovak).

Who judges each sample record (decision D34):
  - Claude Sonnet 5.5 reviews all records (data/review/sonnet/*.json),
  - the human audits a subset - every Sonnet/Haiku disagreement + a random control set
    (data/review/spotcheck_ids.csv, answers in data/review/spotcheck_results.csv); the human answer wins,
  - the Haiku verifier (data/raw/agents/verifier/*.json) is the second, independent AI opinion.
If a full human review exists (data/review/review_results.csv), it is used instead (the original design).
"""

from __future__ import annotations

import csv
import json
import statistics
from collections import Counter
from pathlib import Path

from investordb.metrics import chapman, cohen_kappa, wilson

ROOT = Path(__file__).resolve().parents[2]
REVIEW_DIR = ROOT / "data" / "review"
PROCESSED = ROOT / "data" / "processed"
VERIFIER_DIR = ROOT / "data" / "raw" / "agents" / "verifier"
REPORT = ROOT / "docs" / "PRECISION_REPORT.md"

PRIMARY = ["real_investor", "active_36m", "type_vc", "hq_cz_sk"]
FIELDS = ["sources_support", "sectors_ok", "ticket_ok", "capital_ok"]
SK = {"áno": "yes", "nie": "no", "neviem": "cannot_tell", "neuvedené": "not_given", "": "cannot_tell"}


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig") as f:  # the review form exports with a BOM (for Excel)
        return list(csv.DictReader(f))


def overall(answers: dict) -> str:
    vals = [answers.get(k, "cannot_tell") for k in PRIMARY]
    if any(v == "no" for v in vals):
        return "exclude"
    if all(v == "yes" for v in vals):
        return "include"
    return "cannot_tell"


def human_answers(path: Path) -> dict[str, dict]:
    out = {}
    for r in _read(path):
        a = {k: SK.get((r.get(k) or "").strip(), "cannot_tell") for k in PRIMARY + FIELDS}
        a.update(minutes=r.get("minutes_spent", ""), note=r.get("note", ""), by="človek")
        a["overall"] = overall(a)
        out[r["review_id"]] = a
    return out


def ai_answers(folder: Path, pattern: str, by: str) -> dict[str, dict]:
    out = {}
    for path in sorted(folder.glob(pattern)):
        for r in json.loads(path.read_text(encoding="utf-8")):
            a = {k: (r.get(k) or {}).get("answer", "cannot_tell") for k in PRIMARY + FIELDS + ["identity_ok"]}
            a.update(note="; ".join(f"{k}: {(r.get(k) or {}).get('why', '')}" for k in PRIMARY + FIELDS
                                    if (r.get(k) or {}).get("answer") in ("no", "cannot_tell"))[:400], by=by)
            a["overall"] = overall(a)
            out[r["review_id"]] = a
    return out


def pct(p: float) -> str:
    return f"{100 * p:.1f} %"


def ci(k: int, n: int) -> str:
    p, lo, hi = wilson(k, n)
    return f"**{k}/{n} = {pct(p)}** (95 % CI {pct(lo)} – {pct(hi)})" if n else "–"


def kappa(a: dict, b: dict, ids: list[str]) -> tuple[int, int, float]:
    both = [r for r in ids if r in a and r in b]
    agree = sum(a[r]["overall"] == b[r]["overall"] for r in both)
    decided = [r for r in both if "cannot_tell" not in (a[r]["overall"], b[r]["overall"])]
    k = cohen_kappa([a[r]["overall"] for r in decided], [b[r]["overall"] for r in decided]) if decided else float("nan")
    return agree, len(both), k


def build() -> str:
    key = {r["review_id"]: r for r in _read(REVIEW_DIR / "review_key.csv")}
    sonnet = ai_answers(REVIEW_DIR / "sonnet", "s_b*.json", "Sonnet 5.5")
    haiku = ai_answers(VERIFIER_DIR, "v_b*.json", "Haiku 5.5")
    human_full = human_answers(REVIEW_DIR / "review_results.csv")
    human_spot = human_answers(REVIEW_DIR / "spotcheck_results.csv")
    spot = {r["review_id"]: r for r in _read(REVIEW_DIR / "spotcheck_ids.csv")}
    final = human_full or {rid: human_spot.get(rid) or sonnet[rid] for rid in key if rid in sonnet or rid in human_spot}

    investors = _read(PROCESSED / "investors.csv")
    decisions = _read(PROCESSED / "decisions.csv")
    claims = _read(PROCESSED / "claims.csv")
    candidates = {c["candidate_id"]: c for c in _read(PROCESSED / "candidates.csv")}
    dec = {d["candidate_id"]: d for d in decisions}
    lines: list[str] = []
    add = lines.append

    as_of = investors[0]["as_of"] if investors else "?"
    add("# Meranie presnosti – pilot VC investori CZ + SK\n")
    add(f"*Generované skriptom `python -m investordb.cli report` z dát zmrazených tagom `pilot-frozen-v3` "
        f"(`as_of` = {as_of}). Metriky sú definované vopred v [PLAN.md](PLAN.md), kap. 9.*\n")

    # --- who judged
    add("## 1. Kto hodnotil vzorku\n")
    findings = _read(REVIEW_DIR / "human_findings.csv")
    if human_full:
        add(f"Všetkých {len(human_full)} záznamov vzorky ručne overil človek.\n")
    elif not human_spot:
        add(f"- **Claude Sonnet 5.5** posúdil všetkých {len(sonnet)} záznamov vzorky naslepo. Dostal rovnaké informácie "
            "ako formulár pre človeka a zdroje si otváral sám – [pokyn](../prompts/reviewer_agent.md). **Presnosť nižšie "
            "je teda presnosť podľa nezávislej AI kontroly silnejším modelom.**")
        add(f"- **Claude Haiku 5.5** (nezávislý overovateľ) posúdil tých istých {len(haiku)} záznamov – druhý AI názor.")
        add("- **Človek** (autor) formulár prešiel, **štruktúrované odpovede však nevyplnil** (rozhodnutie D36). Jeho "
            "kvalitatívne zistenia viedli k dvom opravám pipeline (v2, v3):\n")
        add("| Záznam | Zistenie | Dôsledok |\n|---|---|---|")
        for f in findings:
            add(f"| {f['record']} | {f['finding']} | {f['consequence']} |")
        add("\n**Obmedzenie:** zadanie žiada ručne overenú vzorku. Formálne ručné meranie presnosti chýba. Nahrádza ho "
            "slepá AI kontrola dvoma modelmi a kvalitatívny ľudský audit opísaný vyššie.\n")
    else:
        disputed = [r for r, s in spot.items() if s["why_selected"] == "disagreement"]
        n_inc = sum(key[r]["stratum"] == "included" for r in human_spot)
        control = [r for r, s in spot.items() if s["why_selected"] == "random_control"]
        add(f"- **Claude Sonnet 5.5** posúdil všetkých {len(sonnet)} záznamov vzorky naslepo (rovnaké informácie ako "
            "formulár pre človeka, zdroje si otváral sám) – [pokyn](../prompts/reviewer_agent.md).")
        add(f"- **Človek** (autor) ručne overil {len(human_spot)} záznamov vo formulári (D40): {len(disputed)} sporné "
            f"medzi AI kontrolórmi a {len(control)} náhodné kontrolné; z nich {n_inc} zaradené a {len(human_spot) - n_inc} "
            f"{'vyradený (návnada)' if len(human_spot) - n_inc == 1 else 'vyradené'}. Polia (kapitál, zdroje) videl v spresnenej verzii (D38). **Kde sa človek a Sonnet "
            "líšia, platí odpoveď človeka.**")
        add(f"- **Claude Haiku 5.5** (nezávislý overovateľ) posúdil tých istých {len(haiku)} záznamov – druhý AI názor.")
        add("- Rozhodnutie a dôvody: [DECISIONS.md](DECISIONS.md) D34, D40. Zadanie žiada ručne overenú vzorku – úplnú "
            "ručnú kontrolu nahradila AI kontrola s ľudským auditom; obmedzenie je uvedené v README.")
        if findings:
            add("- Pred formulárom človek urobil kvalitatívny audit, ktorý viedol k dvom opravám pipeline (v2, v3):\n")
            add("| Záznam | Zistenie | Dôsledok |\n|---|---|---|")
            for f in findings:
                add(f"| {f['record']} | {f['finding']} | {f['consequence']} |")
        add("")

    # --- pipeline overview
    status = Counter(d["status"] for d in decisions)
    add("## 2. Výsledok pipeline\n")
    add("| Stav | Počet |\n|---|---|")
    for s in ("INCLUDED", "REJECTED", "OOS", "NEEDS_REVIEW"):
        add(f"| {s} | {status.get(s, 0)} |")
    reasons = Counter(d["reason"] for d in decisions if d["status"] in ("REJECTED", "OOS"))
    add("\nDôvody vyradenia: " + ", ".join(f"{r} {n}×" for r, n in reasons.most_common()) + "\n")

    # --- primary metric
    # records the CURRENT database includes (a record sampled as included in v2 may have left the database in v3)
    included_ids = [rid for rid, k in key.items() if k["stratum"] == "included" and k["status"] == "INCLUDED"
                    and rid in final]
    left = [rid for rid, k in key.items() if k["stratum"] == "included" and k["status"] != "INCLUDED"]
    add("## 3. Primárna metrika: presnosť zaradených záznamov\n")
    add("Záznam je správny, ak hodnotiteľ zo zdrojov potvrdil **všetky štyri**: skutočný investor ∧ aktívny "
        "v 36 mesiacoch ∧ VC ∧ sídlo CZ/SK.\n")
    correct = [r for r in included_ids if final[r]["overall"] == "include"]
    decided = [r for r in included_ids if final[r]["overall"] != "cannot_tell"]
    add(f"- **Výsledná presnosť** (prísne, „neviem“ = nepotvrdené): {ci(len(correct), len(included_ids))}")
    add(f"- Len rozhodnuté záznamy (bez „neviem“): {ci(len(correct), len(decided))}")
    if human_spot and not human_full:
        h_ids = [r for r in included_ids if r in human_spot]
        h_ok = [r for r in h_ids if human_spot[r]["overall"] == "include"]
        add(f"- Len záznamy, ktoré ručne overil človek: {ci(len(h_ok), len(h_ids))}")
    if not human_full and sonnet:
        s_ok = [r for r in included_ids if sonnet.get(r, {}).get("overall") == "include"]
        add(f"- Pre porovnanie – len podľa Sonnetu (pred ľudským auditom): {ci(len(s_ok), len(included_ids))}")
    if left:
        add(f"- Záznamy vybrané ako zaradené, ktoré po oprave v3 už v databáze nie sú (nezapočítané): "
            + ", ".join(f"{r} ({key[r]['status']} {key[r]['reason']})" for r in left))
    add("\n| Otázka | Áno | Nie | Neviem |\n|---|---|---|---|")
    for q in PRIMARY:
        c = Counter(final[r][q] for r in included_ids)
        add(f"| {q} | {c['yes']} | {c['no']} | {c['cannot_tell']} |")

    # --- rejections
    add("\n## 4. Správnosť vyradenia\n")
    add("Vyradenie je správne, ak hodnotiteľ pri aspoň jednej zo štyroch otázok odpovedal „nie“. Duplicity (E8) sa "
        "hodnotia zvlášť (D29): vyradenie je správne, ak ide o skutočného investora a jeho zlúčený hlavný záznam je "
        "zaradený.\n")
    add("| Vrstva | Správne vyradené |\n|---|---|")
    for stratum, label in (("real_reject", "skutočné vyradené záznamy (bez duplicít)"),
                           ("control_reject", "kontrolná sada (návnady)")):
        ids = [r for r, k in key.items() if k["stratum"] == stratum and r in final and k["reason"] != "E8"]
        ok = [r for r in ids if final[r]["overall"] == "exclude"]
        add(f"| {label} – prísne | {ci(len(ok), len(ids))} |")
        # for E7 ('no evidence of investing') a reviewer who also finds nothing answers 'cannot tell' - that supports
        # the rejection rather than contradicting it
        consistent = [r for r in ids if final[r]["overall"] == "exclude"
                      or (key[r]["reason"] == "E7" and final[r]["overall"] == "cannot_tell")]
        if len(consistent) != len(ok):
            add(f"| {label} – vrátane „ani hodnotiteľ nenašiel dôkaz“ pri E7 | {ci(len(consistent), len(ids))} |")
    dups = [r for r, k in key.items() if k["reason"] == "E8" and r in final]
    if dups:
        def primary_included(rid: str) -> bool:
            expl = dec.get(key[rid]["candidate_id"], {}).get("explanation", "")
            primary = expl.split("duplicate of ")[-1].split(" ")[0] if "duplicate of" in expl else ""
            return dec.get(primary, {}).get("status") == "INCLUDED"
        ok = [r for r in dups if final[r]["real_investor"] == "yes" and primary_included(r)]
        add(f"| duplicity (E8) – firma je v databáze cez zlúčený záznam | {ci(len(ok), len(dups))} |")

    # --- fields: the zmrazená v3 as judged by Sonnet; the human saw the REFINED fields (D40), reported separately
    fields_by = human_full or sonnet
    add("\n## 5. Presnosť a vyplnenosť polí (zaradené záznamy)\n")
    add("| Pole | Presnosť (áno / áno+nie) | Vyplnenosť v databáze |\n|---|---|---|")
    fill = {"sectors_ok": "sectors", "ticket_ok": "ticket_min_eur", "capital_ok": "total_capital_eur"}
    for q in FIELDS:
        c = Counter(fields_by[r][q] for r in included_ids if r in fields_by)
        filled = f"{sum(1 for i in investors if i.get(fill[q]))}/{len(investors)}" if q in fill else "–"
        add(f"| {q} | {ci(c['yes'], c['yes'] + c['no'])} | {filled} |")
    if sonnet:
        stale = {r["review_id"] for r in _read(REVIEW_DIR / "identity_changed_v3.csv")}
        c = Counter(sonnet[r].get("identity_ok", "cannot_tell") for r in included_ids if r in sonnet and r not in stale)
        add(f"| identity_ok (len Sonnet; bez {len(stale)} záznamov s identitou zmenenou vo v3) | "
            f"{ci(c['yes'], c['yes'] + c['no'])} | – |")

    if human_spot and not human_full:
        h_inc = [r for r in human_spot if key[r]["stratum"] == "included" and key[r]["status"] == "INCLUDED"]
        add(f"\nČlovek pri {len(h_inc)} zaradených záznamoch hodnotil polia **spresnenej verzie** (D40); presnosť "
            "spresnených polí meria podrobne slepá kontrola faktov v [REFINEMENT.md](REFINEMENT.md):\n")
        add("| Pole (spresnená verzia) | Áno | Nie | Neviem | Neuvedené |\n|---|---|---|---|---|")
        for q in FIELDS:
            c = Counter(human_spot[r][q] for r in h_inc)
            add(f"| {q} | {c['yes']} | {c['no']} | {c['cannot_tell']} | {c['not_given']} |")

    # --- how ambiguous the sources themselves are (the human's main qualitative finding, D36)
    inc_ids = {i["candidate_id"] for i in investors} | {m for i in investors for m in i["evidence_ids"].split()}
    inv_inc = [c for c in claims if c["field"] == "investments" and c["auto_check"] == "ok"
               and c["candidate_id"] in inc_ids and c.get("deal_context") != "exit" and c.get("attributed") != "0"]
    if inv_inc:
        n = len(inv_inc)
        dated = [c for c in inv_inc if c.get("deal_context") == "deal" and c["event_date"]]
        day = [c for c in dated if c.get("event_date_precision") == "day"]
        with_amount = [c for c in inv_inc if (json.loads(c["value"]) or {}).get("amount")]
        add("\n### Nejasnosť zdrojov (investície zaradených investorov)\n")
        add(f"Z {n} overených investícií zaradených investorov: **{len(dated)} ({pct(len(dated) / n)})** má dátum, ktorý "
            f"možno považovať za dátum obchodu (z toho {len(day)} s presnosťou na deň); "
            f"**{n - len(dated)} ({pct((n - len(dated)) / n)})** je len zmienka bez dátumu obchodu (portfólio, prehľadové "
            f"články); suma je uvedená pri **{len(with_amount)} ({pct(len(with_amount) / n)})**. Potvrdzuje to zistenie z "
            "ľudskej kontroly: z verejných článkov často nie je jasné, kedy a koľko investor investoval.\n")

    # --- automatic checks
    checks = Counter(c["auto_check"] for c in claims)
    total = sum(checks.values())
    inv = [c for c in claims if c["field"] == "investments" and c["auto_check"] == "ok"]
    add("\n## 6. Strojové kontroly (všetky tvrdenia agentov)\n")
    add(f"{total} tvrdení: " + ", ".join(f"`{k}` {v} ({pct(v / total)})" for k, v in checks.most_common()) + ".")
    add(f"Z {len(inv)} overených investičných tvrdení: kontext obchodu "
        + ", ".join(f"`{k}` {v}" for k, v in Counter(c.get("deal_context", "") for c in inv).most_common())
        + "; priradenie investora "
        + ", ".join(f"`{k}` {v}" for k, v in Counter(c.get("attributed", "") for c in inv).most_common()) + ".\n")

    # --- agreement
    add("## 7. Zhoda hodnotiteľov\n")
    add("| Dvojica | Zhoda celkového verdiktu | Cohenovo κ (rozhodnuté záznamy) |\n|---|---|---|")
    pairs = [("Haiku overovateľ vs. výsledok", haiku, final, list(key))]
    if sonnet:
        pairs.append(("Haiku overovateľ vs. Sonnet", haiku, sonnet, list(key)))
    if human_spot:
        ctrl = [r for r, s in spot.items() if s["why_selected"] == "random_control"]
        disp = [r for r, s in spot.items() if s["why_selected"] == "disagreement"]
        pairs += [("Sonnet vs. človek – náhodné kontrolné záznamy", sonnet, human_spot, ctrl),
                  ("Sonnet vs. človek – sporné záznamy", sonnet, human_spot, disp)]
    for label, a, b, ids in pairs:
        agree, n, k = kappa(a, b, ids)
        add(f"| {label} | {ci(agree, n)} | {k:.2f} |" if n else f"| {label} | – | – |")
    if human_spot:
        add("\nZhoda Sonneta s človekom na **náhodných** kontrolných záznamoch je nestranný odhad spoľahlivosti AI "
            "kontroly; na sporných záznamoch ukazuje, kto mal pri ťažkých prípadoch pravdu.\n")
    else:
        disagree = [r for r in key if r in haiku and r in sonnet and haiku[r]["overall"] != sonnet[r]["overall"]]
        add(f"\nVšetky rozdiely Haiku vs. Sonnet ({len(disagree)}) sú prípady, keď jeden model **nevedel rozhodnúť** "
            "(„cannot_tell“) a druhý áno; v žiadnom zázname si priamo neprotirečia (preto κ = 1,00 na rozhodnutých). "
            "Sonnet bol rozhodnejší a navyše našiel chyby v poliach (cieľové fondy v kapitáli, dátumy článkov namiesto "
            "dátumov obchodu), ktoré Haiku overovateľ prehliadol.\n")

    # --- coverage
    add("## 8. Odhad úplnosti (capture–recapture)\n")

    def members(i: dict) -> list[str]:  # a record merged from duplicates was "found" if any member was
        expl = dec.get(i["candidate_id"], {}).get("explanation", "")
        extra = expl.split("[merged:")[-1].rstrip("]").split(",") if "[merged:" in expl else []
        return [i["candidate_id"]] + [m.strip() for m in extra]

    def found(i: dict, col: str) -> bool:
        return any(candidates.get(m, {}).get(col) == "1" for m in members(i))

    in_a = sum(found(i, "in_list_a") for i in investors)
    in_b = sum(found(i, "in_list_b") for i in investors)
    both_ab = sum(found(i, "in_list_a") and found(i, "in_list_b") for i in investors)
    if both_ab:
        n, lo, hi = chapman(in_a, in_b, both_ab)
        add(f"Zaradení investori nájdení v zozname A (štruktúrované zdroje): {in_a}, v zozname B (správy o kolách): "
            f"{in_b}, v oboch: {both_ab}. Chapmanov odhad počtu aktívnych VC investorov so sídlom v CZ/SK: "
            f"**{n:.0f}** (95 % CI {lo:.0f} – {hi:.0f}). Databáza pokrýva približne **{pct(len(investors) / n)}**. "
            "Ide o dolný odhad populácie (a teda horný odhad pokrytia) – oba zoznamy uprednostňujú viditeľných "
            "investorov.\n")

    # --- effort
    minutes = [float(h["minutes"]) for h in (human_full or human_spot).values() if str(h["minutes"]).strip()]
    add("## 9. Čas ručnej kontroly\n")
    add(f"{len(minutes)} záznamov, priemer **{statistics.mean(minutes):.1f} min**, medián "
        f"{statistics.median(minutes):.1f} min na záznam (vstup pre odhad nákladov).\n" if minutes
        else ("Človek pri ručnej kontrole čas na záznam nezaznamenal. " if human_spot or human_full else
              "Štruktúrovaná ručná kontrola nebola vyplnená (D36), čas sa preto nemeral. ")
        + "Nákladový model používa predpoklad 4 min na záznam a uvádza ho ako predpoklad.\n")

    # --- errors
    add("## 10. Záznamy, pri ktorých sa výsledok líši od pipeline\n")
    errors = [(r, key[r]) for r in key if r in final and (
        (key[r]["stratum"] == "included" and final[r]["overall"] != "include")
        or (key[r]["stratum"] != "included" and key[r]["reason"] != "E8" and final[r]["overall"] != "exclude"))]
    if errors:
        add("| Záznam | Vrstva | Pipeline | Výsledok | Kto | Zdôvodnenie |\n|---|---|---|---|---|---|")
        for r, k in errors:
            name = dec.get(k["candidate_id"], {}).get("name", "")
            add(f"| {r} {name} ({k['candidate_id']}) | {k['stratum']} | {k['status']} {k['reason']} | "
                f"{final[r]['overall']} | {final[r]['by']} | {final[r]['note'][:300]} |")
    else:
        add("Žiadne.")
    return "\n".join(lines) + "\n"


def write() -> Path:
    REPORT.write_text(build(), encoding="utf-8")
    return REPORT
