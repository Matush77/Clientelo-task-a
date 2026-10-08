"""Name-only control candidates: random registry companies whose only 'investor signal' is their name.

They test rule E7 (the "random company" problem). Drawn with a fixed seed so the sample is reproducible.
"""

from __future__ import annotations

import csv
import random
from datetime import date
from pathlib import Path

from investordb.registries import ares_search, rpo_search

SEEDS_DIR = Path(__file__).resolve().parents[2] / "data" / "seeds"
FIELDS = ["candidate_source", "name", "company_id", "country", "legal_form", "founded", "registry_url", "name_term", "drawn_on"]


def draw_ares(term: str, n: int, rng: random.Random) -> list[dict]:
    total, _ = ares_search(term, limit=1)
    if total > 1000:
        # ARES refuses any query matching >1000 companies (e.g. "Capital": 2,477), so it cannot be paged
        print(f"ARES: '{term}' matches {total} companies, too many to sample - skipped")
        return []
    rows: list[dict] = []
    offsets = list(range(total))
    rng.shuffle(offsets)
    for offset in offsets:
        if len(rows) == n:
            break
        _, recs = ares_search(term, limit=1, offset=offset)
        if recs and recs[0].active:
            r = recs[0]
            rows.append(dict(name=r.name, company_id=r.company_id, country="CZ", legal_form=r.legal_form,
                             founded=r.founded, registry_url=r.source_url, name_term=term))
    return rows


def draw_rpo(term: str, n: int, rng: random.Random) -> list[dict]:
    recs = [r for r in rpo_search(name=term, limit=50) if r.active]
    rng.shuffle(recs)
    return [dict(name=r.name, company_id=r.company_id, country="SK", legal_form=r.legal_form,
                 founded=r.founded, registry_url=r.source_url, name_term=term) for r in recs[:n]]


def build_name_only_controls(seed: int = 20261008) -> Path:
    rng = random.Random(seed)
    rows = draw_ares("Ventures", 5, rng) + draw_ares("Capital", 3, rng) + draw_rpo("Capital", 2, rng) + draw_rpo("Invest", 2, rng)
    out = SEEDS_DIR / "controls_name_only.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({"candidate_source": "control_name_only", "drawn_on": date.today().isoformat(), **r})
    return out


if __name__ == "__main__":
    print(build_name_only_controls())
