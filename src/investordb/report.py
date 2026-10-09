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
    add(f"*Generované skriptom `python -m investordb.cli report` z dát zmrazených tagom `pilot-frozen-v2` "
        f"(`as_of` = {as_of}). Metriky sú definované vopred v [PLAN.md](PLAN.md), kap. 9.*\n")

    # --- who judged
    add("## 1. Kto hodnotil vzorku\n")
    if human_full:
        add(f"Všetkých {len(human_full)} záznamov vzorky ručne overil človek.\n")
    else:
        disputed = [r for r, s in spot.items() if s["why_selected"] == "disagreement"]
        control = [r for r, s in spot.items() if s["why_selected"] == "random_control"]
        add(f"- **Claude Sonnet 5.5** posúdil všetkých {len(sonnet)} záznamov vzorky naslepo (rovnaké informácie ako "
            "formulár pre človeka, zdroje si otváral sám) – [pokyn](../prompts/reviewer_agent.md).")
        add(f"- **Človek** (autor) ručne overil {len(human_spot)} z {len(spot)} vybraných záznamov: všetky, pri "
            f"ktorých sa Sonnet a Haiku overovateľ nezhodli alebo Sonnet nevedel rozhodnúť ({len(disputed)}), a "
            f"{len(control)} náhodných kontrolných záznamov. **Kde sa človek a Sonnet líšia, platí odpoveď človeka.**")
        add(f"- **Claude Haiku 5.5** (nezávislý overovateľ) posúdil tých istých {len(haiku)} záznamov – druhý AI názor.")
        add("- Rozhodnutie a dôvody: [DECISIONS.md](DECISIONS.md) D34. Zadanie žiada ručne overenú vzorku – úplnú ručnú "
            "kontrolu nahradila AI kontrola s ľudským auditom; obmedzenie je uvedené v README.\n")

    # --- pipeline overview
    status = Counter(d["status"] for d in decisions)
    add("## 2. Výsledok pipeline\n")
    add("| Stav | Počet |\n|---|---|")
    for s in ("INCLUDED", "REJECTED", "OOS", "NEEDS_REVIEW"):
        add(f"| {s} | {status.get(s, 0)} |")
    reasons = Counter(d["reason"] for d in decisions if d["status"] in ("REJECTED", "OOS"))
    add("\nDôvody vyradenia: " + ", ".join(f"{r} {n}×" for r, n in reasons.most_common()) + "\n")

    # --- primary metric
    included_ids = [rid for rid, k in key.items() if k["stratum"] == "included" and rid in final]
    add("## 3. Primárna metrika: presnosť zaradených záznamov\n")
    add("Záznam je správny, ak hodnotiteľ zo zdrojov potvrdil **všetky štyri**: skutočný investor ∧ aktívny "
        "v 36 mesiacoch ∧ VC ∧ sídlo CZ/SK.\n")
    correct = [r for r in included_ids if final[r]["overall"] == "include"]
    decided = [r for r in included_ids if final[r]["overall"] != "cannot_tell"]
    add(f"- **Výsledná presnosť** (prísne, „neviem“ = nepotvrdené): {ci(len(correct), len(included_ids))}")
    add(f"- Len rozhodnuté záznamy (bez „neviem“): {ci(len(correct), len(decided))}")
    if not human_full and sonnet:
        s_ok = [r for r in included_ids if sonnet.get(r, {}).get("overall") == "include"]
        add(f"- Pre porovnanie – len podľa Sonnetu (pred ľudským auditom): {ci(len(s_ok), len(included_ids))}")
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
        add(f"| {label} | {ci(len(ok), len(ids))} |")
    dups = [r for r, k in key.items() if k["reason"] == "E8" and r in final]
    if dups:
        def primary_included(rid: str) -> bool:
            expl = dec.get(key[rid]["candidate_id"], {}).get("explanation", "")
            primary = expl.split("duplicate of ")[-1].split(" ")[0] if "duplicate of" in expl else ""
            return dec.get(primary, {}).get("status") == "INCLUDED"
        ok = [r for r in dups if final[r]["real_investor"] == "yes" and primary_included(r)]
        add(f"| duplicity (E8) – firma je v databáze cez zlúčený záznam | {ci(len(ok), len(dups))} |")

    # --- fields
    add("\n## 5. Presnosť a vyplnenosť polí (zaradené záznamy)\n")
    add("| Pole | Presnosť (áno / áno+nie) | Vyplnenosť v databáze |\n|---|---|---|")
    fill = {"sectors_ok": "sectors", "ticket_ok": "ticket_min_eur", "capital_ok": "total_capital_eur"}
    for q in FIELDS:
        c = Counter(final[r][q] for r in included_ids)
        filled = f"{sum(1 for i in investors if i.get(fill[q]))}/{len(investors)}" if q in fill else "–"
        add(f"| {q} | {ci(c['yes'], c['yes'] + c['no'])} | {filled} |")
    if sonnet:
        c = Counter(sonnet[r].get("identity_ok", "cannot_tell") for r in included_ids if r in sonnet)
        add(f"| identity_ok (len Sonnet) | {ci(c['yes'], c['yes'] + c['no'])} | – |")

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
    add("\nZhoda Sonneta s človekom na **náhodných** kontrolných záznamoch je nestranný odhad spoľahlivosti AI kontroly; "
        "na sporných záznamoch ukazuje, kto mal pri ťažkých prípadoch pravdu.\n")

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
        else "Čas zatiaľ nie je k dispozícii.\n")

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
