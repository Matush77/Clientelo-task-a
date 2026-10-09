"""Cheap, deterministic pre-triage before the (expensive) evidence agents.

Every evidence-scope candidate is looked up in the Czech (ARES) and Slovak (RPO) registries. A foreign fund is not
registered there, so candidates with an unknown HQ and no registry match go to a cheap HQ-triage agent instead of the
full evidence agent. A registry match is accepted generously (it only decides who gets *more* scrutiny); the match
is recorded so the evidence step can confirm or reject it.
"""

from __future__ import annotations

import csv
from pathlib import Path

import re

from investordb.candidates import OUT as CANDIDATES_CSV, match_key, same_entity
from investordb.registries import RegistryRecord, ares_search, core_name, rpo_search

TRIAGE_CSV = CANDIDATES_CSV.with_name("triage.csv")


INVESTMENT_WORDS = {"investment", "investments", "ventures", "venture", "capital", "partners", "management", "fund",
                    "funds", "holding", "invest", "vc", "gp", "advisors", "advisers"}


INVESTMENT_VEHICLE = re.compile(r"rizikového kapitálu|sicav|investi[čc]n[íý] fond|podílový fond", re.I)


def has_investment_signal(registry_name: str) -> bool:
    """Does the registered name itself say it is an investment vehicle?"""
    return bool(INVESTMENT_VEHICLE.search(registry_name)) or bool(set(core_name(registry_name).split()) & INVESTMENT_WORDS)


def registry_name_matches(registry_name: str, name: str) -> bool:
    reg, cand = match_key(registry_name), match_key(name)
    if not reg or not cand:
        return False
    # One-word company names collide: "KAYA, spol. s r.o." and "ZAKA, s.r.o." are unrelated firms that merely share
    # a VC's brand. Such a name only counts if the registered name itself marks an investment vehicle.
    if len(reg.split()) == 1 and not has_investment_signal(registry_name):
        return False
    if same_entity(reg, cand):
        return True
    # one name is the other plus extra words, in either direction ("ZAKA Ventures" brand vs "ZAKA VC I" entity)
    short, long_ = sorted((reg, cand), key=len)
    if not long_.startswith(short + " "):
        return False
    # multi-word prefix ("Reflex Capital" -> "Reflex Capital Partners s.r.o."), or a one-word name whose extra words are
    # only investment words: "Nation1" -> "Nation1 Investment" yes, "KAYA" -> "KAYA CONSTRUCTION" no
    extra = set(long_[len(short):].split())
    return (len(short.split()) >= 2 and short == cand) or extra <= INVESTMENT_WORDS


def _accept(rec: RegistryRecord, name: str) -> bool:
    return registry_name_matches(rec.name, name)


def registry_matches(name: str, hq: str) -> list[RegistryRecord]:
    query = match_key(name) or name
    found = [r for r in ares_search(query, limit=10)[1] if _accept(r, name)] if hq in ("CZ", "unknown", "") else []
    if hq in ("SK", "unknown", "") and not found:
        found = [r for r in rpo_search(name=query, limit=3) if _accept(r, name)]
    return found


def run(path: Path = CANDIDATES_CSV, out: Path = TRIAGE_CSV) -> Path:
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["scope"] == "evidence"]
    results = []
    for r in rows:
        if r["company_id"]:  # name-only controls come with their registry ID already
            matches, next_step = [], "evidence"
        else:
            matches = registry_matches(r["name"], r["hq_claimed"])
            unknown_hq = r["hq_claimed"] in ("unknown", "")
            only_b = r["in_list_a"] == "0" and not r["control_category"]
            next_step = "hq_triage" if (unknown_hq and only_b and not matches) else "evidence"
        best = next((m for m in matches if m.active), matches[0] if matches else None)
        results.append(dict(
            candidate_id=r["candidate_id"], name=r["name"], hq_claimed=r["hq_claimed"], next_step=next_step,
            registry=best.registry if best else "", company_id=r["company_id"] or (best.company_id if best else ""),
            legal_name=best.name if best else "", registry_active=int(best.active) if best else "",
            n_registry_matches=len(matches), registry_url=best.source_url if best else "",
        ))
        print(f"{next_step:<10} {r['candidate_id']} {r['name'][:40]:<40} -> {best.name if best else '-'}")
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)
    return out


HQ_TRIAGE_DIR = TRIAGE_CSV.parents[1] / "raw" / "agents" / "triage"


def apply_hq_triage(path: Path = TRIAGE_CSV) -> dict[str, int]:
    """Second triage step: an HQ-triage agent's answer only counts if its quote is verified on the page.

    verified foreign HQ -> skip (OOS_HQ); CZ/SK or unknown/unverified -> full evidence step (never drop a possible
    CZ/SK investor on weak evidence - the evidence agent settles the HQ first and exits early if foreign).
    """
    import json

    from investordb.validate import check_claim

    answers = {}
    for f in sorted(HQ_TRIAGE_DIR.glob("*.json")):
        for a in json.loads(f.read_text(encoding="utf-8")):
            answers[a["candidate_id"]] = a
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r.setdefault("hq_triage", "")
        r.setdefault("hq_triage_check", "")
        r.setdefault("hq_triage_url", "")
        a = answers.get(r["candidate_id"])
        if r["next_step"] != "hq_triage" or not a:
            continue
        hq = (a.get("hq_country") or "unknown").upper()
        status = check_claim(a["source_url"], a["quote"]).status if a.get("source_url") and a.get("quote") else "no_quote"
        r.update(hq_triage=hq, hq_triage_check=status, hq_triage_url=a.get("source_url") or "")
        if status == "ok" and hq not in ("CZ", "SK", "UNKNOWN"):
            r["next_step"] = "skip:foreign_hq_verified"
        else:
            r["next_step"] = "evidence"
        print(f"{r['next_step']:<26} {hq:<8} {status:<16} {r['name']}")
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    return dict(Counter(r["next_step"] for r in rows))


if __name__ == "__main__":
    import sys

    if sys.argv[1:] == ["--apply-hq-triage"]:
        print(apply_hq_triage())
    else:
        print(run())
