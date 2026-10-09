"""Compute the pre-registered metrics (docs/PLAN.md, chapter 9) and write docs/PRECISION_REPORT.md (Slovak).

Inputs: data/review/review_results.csv (human, exported from review.html), data/review/review_key.csv (sample key),
data/raw/agents/verifier/*.json (AI verifier), data/processed/{claims,investors,decisions,candidates}.csv.
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


def human_answers() -> dict[str, dict]:
    out = {}
    for r in _read(REVIEW_DIR / "review_results.csv"):
        a = {k: SK.get((r.get(k) or "").strip(), "cannot_tell") for k in PRIMARY + FIELDS}
        a["minutes"] = r.get("minutes_spent", "")
        a["note"] = r.get("note", "")
        a["overall"] = overall(a)
        out[r["review_id"]] = a
    return out


def verifier_answers() -> dict[str, dict]:
    out = {}
    for path in sorted(VERIFIER_DIR.glob("*.json")):
        for r in json.loads(path.read_text(encoding="utf-8")):
            a = {k: (r.get(k) or {}).get("answer", "cannot_tell") for k in PRIMARY + FIELDS}
            a["overall"] = r.get("overall") or overall(a)
            out[r["review_id"]] = a
    return out


def pct(p: float) -> str:
    return f"{100 * p:.1f} %"


def ci(k: int, n: int) -> str:
    p, lo, hi = wilson(k, n)
    return f"**{k}/{n} = {pct(p)}** (95 % CI {pct(lo)} – {pct(hi)})" if n else "–"


def build() -> str:
    key = {r["review_id"]: r for r in _read(REVIEW_DIR / "review_key.csv")}
    human, ai = human_answers(), verifier_answers()
    investors = _read(PROCESSED / "investors.csv")
    decisions = _read(PROCESSED / "decisions.csv")
    claims = _read(PROCESSED / "claims.csv")
    candidates = {c["candidate_id"]: c for c in _read(PROCESSED / "candidates.csv")}
    lines: list[str] = []
    add = lines.append

    as_of = investors[0]["as_of"] if investors else "?"
    add("# Meranie presnosti – pilot VC investori CZ + SK\n")
    add(f"*Generované skriptom `python -m investordb.cli report` z dát zmrazených k `as_of` = {as_of}. "
        "Metriky sú definované vopred v [PLAN.md](PLAN.md), kap. 9.*\n")

    # --- pipeline overview
    status = Counter(d["status"] for d in decisions)
    add("## 1. Výsledok pipeline\n")
    add("| Stav | Počet |\n|---|---|")
    for s in ("INCLUDED", "REJECTED", "OOS", "NEEDS_REVIEW"):
        add(f"| {s} | {status.get(s, 0)} |")
    reasons = Counter(d["reason"] for d in decisions if d["status"] in ("REJECTED", "OOS"))
    add("\nDôvody vyradenia: " + ", ".join(f"{r} {n}×" for r, n in reasons.most_common()) + "\n")

    # --- primary metric
    included_ids = [rid for rid, k in key.items() if k["stratum"] == "included" and rid in human]
    correct = [rid for rid in included_ids if human[rid]["overall"] == "include"]
    decided = [rid for rid in included_ids if human[rid]["overall"] != "cannot_tell"]
    add("## 2. Primárna metrika: presnosť zaradených záznamov\n")
    add("Záznam je správny, ak kontrolór zo zdrojov potvrdil **všetky štyri**: skutočný investor ∧ aktívny "
        "v 36 mesiacoch ∧ VC ∧ sídlo CZ/SK.\n")
    add(f"- Prísne (odpoveď „neviem“ = nepotvrdené): {ci(len(correct), len(included_ids))}")
    add(f"- Len rozhodnuté záznamy (bez „neviem“): {ci(len(correct), len(decided))}\n")
    add("| Otázka | Áno | Nie | Neviem |\n|---|---|---|---|")
    for q in PRIMARY:
        c = Counter(human[rid][q] for rid in included_ids)
        add(f"| {q} | {c['yes']} | {c['no']} | {c['cannot_tell']} |")

    # --- rejections
    add("\n## 3. Správnosť vyradenia\n")
    add("Vyradenie je správne, ak kontrolór pri aspoň jednej zo štyroch otázok odpovedal „nie“.\n")
    add("Duplicity (E8) sa hodnotia zvlášť (rozhodnutie D29): vyradenie duplicity je správne, ak ide o skutočného "
        "investora **a** jeho zlúčený hlavný záznam je v databáze zaradený – firma je tam teda práve raz.\n")
    add("| Vrstva | Správne vyradené |\n|---|---|")
    dec = {d["candidate_id"]: d for d in decisions}
    for stratum, label in (("real_reject", "skutočné vyradené záznamy (bez duplicít)"),
                           ("control_reject", "kontrolná sada (návnady)")):
        ids = [rid for rid, k in key.items() if k["stratum"] == stratum and rid in human and k["reason"] != "E8"]
        ok = [rid for rid in ids if human[rid]["overall"] == "exclude"]
        add(f"| {label} | {ci(len(ok), len(ids))} |")
    dups = [rid for rid, k in key.items() if k["reason"] == "E8" and rid in human]
    if dups:
        def primary_included(rid: str) -> bool:
            expl = dec.get(key[rid]["candidate_id"], {}).get("explanation", "")
            primary = expl.split("duplicate of ")[-1].split(" ")[0] if "duplicate of" in expl else ""
            return dec.get(primary, {}).get("status") == "INCLUDED"
        ok = [rid for rid in dups if human[rid]["real_investor"] == "yes" and primary_included(rid)]
        add(f"| duplicity (E8) – firma je v databáze cez zlúčený záznam | {ci(len(ok), len(dups))} |")

    # --- fields
    add("\n## 4. Presnosť a vyplnenosť polí\n")
    add("| Pole | Presnosť (áno / áno+nie) | Vyplnenosť v databáze |\n|---|---|---|")
    fill = {"sectors_ok": "sectors", "ticket_ok": "ticket_min_eur", "capital_ok": "total_capital_eur"}
    for q in FIELDS:
        c = Counter(human[rid][q] for rid in included_ids)
        n = c["yes"] + c["no"]
        filled = f"{sum(1 for i in investors if i.get(fill[q]))}/{len(investors)}" if q in fill else "–"
        add(f"| {q} | {ci(c['yes'], n)} | {filled} |")

    # --- automatic checks
    checks = Counter(c["auto_check"] for c in claims)
    total = sum(checks.values())
    add("\n## 5. Strojová kontrola citácií (všetky tvrdenia agentov)\n")
    add(f"{total} tvrdení: " + ", ".join(f"`{k}` {v} ({pct(v / total)})" for k, v in checks.most_common()) + "\n")

    # --- AI verifier vs human
    both = [rid for rid in key if rid in human and rid in ai]
    add("## 6. Zhoda AI overovateľa s človekom\n")
    if both:
        agree = sum(human[r]["overall"] == ai[r]["overall"] for r in both)
        decided_both = [r for r in both if "cannot_tell" not in (human[r]["overall"], ai[r]["overall"])]
        kappa = cohen_kappa([human[r]["overall"] for r in decided_both], [ai[r]["overall"] for r in decided_both]) \
            if decided_both else float("nan")
        add(f"- Zhoda celkového verdiktu: {ci(agree, len(both))}")
        add(f"- Cohenovo κ (len záznamy, kde obaja rozhodli, n = {len(decided_both)}): **{kappa:.2f}**\n")
        disagree = [r for r in both if human[r]["overall"] != ai[r]["overall"]]
        if disagree:
            add("| Záznam | Človek | AI | Poznámka človeka |\n|---|---|---|---|")
            for r in disagree:
                add(f"| {r} | {human[r]['overall']} | {ai[r]['overall']} | {human[r]['note']} |")
    else:
        add("*Výsledky overovateľa zatiaľ nie sú k dispozícii.*")

    # --- coverage
    add("\n## 7. Odhad úplnosti (capture–recapture)\n")

    def members(inv: dict) -> list[str]:  # a record merged from duplicates was "found" if any member was
        expl = dec.get(inv["candidate_id"], {}).get("explanation", "")
        extra = expl.split("[merged:")[-1].rstrip("]").split(",") if "[merged:" in expl else []
        return [inv["candidate_id"]] + [m.strip() for m in extra]

    def found(inv: dict, col: str) -> bool:
        return any(candidates.get(m, {}).get(col) == "1" for m in members(inv))

    in_a = sum(found(i, "in_list_a") for i in investors)
    in_b = sum(found(i, "in_list_b") for i in investors)
    both_ab = sum(found(i, "in_list_a") and found(i, "in_list_b") for i in investors)
    if both_ab:
        n, lo, hi = chapman(in_a, in_b, both_ab)
        add(f"Zaradení investori nájdení v zozname A (štruktúrované zdroje): {in_a}, v zozname B (správy o kolách): "
            f"{in_b}, v oboch: {both_ab}. Chapmanov odhad celkového počtu: **{n:.0f}** (95 % CI {lo:.0f} – {hi:.0f}). "
            f"Databáza teda pokrýva približne **{pct(len(investors) / n)}** odhadnutej populácie. Ide o dolný odhad "
            "populácie – oba zoznamy uprednostňujú viditeľných investorov.\n")
    else:
        add("Žiadny zaradený investor nie je v oboch zoznamoch – odhad nie je možný.\n")

    # --- effort
    minutes = [float(h["minutes"]) for h in human.values() if str(h["minutes"]).strip()]
    add("## 8. Čas ručnej kontroly\n")
    if minutes:
        add(f"{len(minutes)} záznamov, priemer **{statistics.mean(minutes):.1f} min**, medián "
            f"{statistics.median(minutes):.1f} min na záznam (vstup pre odhad nákladov).\n")

    # --- errors
    add("## 9. Chyby nájdené ručnou kontrolou\n")
    errors = [(rid, key[rid]) for rid in key if rid in human and (
        (key[rid]["stratum"] == "included" and human[rid]["overall"] != "include")
        or (key[rid]["stratum"] != "included" and key[rid]["reason"] != "E8" and human[rid]["overall"] != "exclude"))]
    if errors:
        add("| Záznam | Vrstva | Pipeline | Človek | Poznámka |\n|---|---|---|---|---|")
        for rid, k in errors:
            add(f"| {rid} ({k['candidate_id']}) | {k['stratum']} | {k['status']} {k['reason']} | "
                f"{human[rid]['overall']} | {human[rid]['note']} |")
    else:
        add("Žiadne.")
    return "\n".join(lines) + "\n"


def write() -> Path:
    REPORT.write_text(build(), encoding="utf-8")
    return REPORT
