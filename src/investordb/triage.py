"""Cheap, deterministic pre-triage before the (expensive) evidence agents.

Every evidence-scope candidate is looked up in the Czech (ARES) and Slovak (RPO) registries. A foreign fund is not
registered there, so candidates with an unknown HQ and no registry match go to a cheap HQ-triage agent instead of the
full evidence agent. A registry match is accepted generously (it only decides who gets *more* scrutiny); the match
is recorded so the evidence step can confirm or reject it.
"""

from __future__ import annotations

import csv
from pathlib import Path

from investordb.candidates import OUT as CANDIDATES_CSV, match_key, same_entity
from investordb.registries import RegistryRecord, ares_search, rpo_search

TRIAGE_CSV = CANDIDATES_CSV.with_name("triage.csv")


def _accept(rec: RegistryRecord, name: str) -> bool:
    reg, cand = match_key(rec.name), match_key(name)
    # registry names are often longer than brands: "Reflex Capital" -> "Reflex Capital Partners s.r.o."
    return same_entity(reg, cand) or (len(cand.split()) >= 2 and reg.startswith(cand + " "))


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


if __name__ == "__main__":
    print(run())
