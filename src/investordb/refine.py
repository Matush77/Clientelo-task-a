"""Refinement of the weak fields of INCLUDED investors by a stronger model (Sonnet 5.5) - decision D38.

The frozen database (tag pilot-frozen-v3) stays as measured. Refinement re-extracts, for every included investor,
(a) each fund with its fundraising status (final close / first close / target) and (b) the real deal date of every
dated investment, in the same claim format. The new claims pass the same machine checks as all other claims, then
the investor rows are rebuilt with the same rules and written next to the frozen ones:

    data/raw/agents/refine/batches/rf_bNN.json   input per agent (what the database currently says)
    data/raw/agents/refine/rf_bNN.json           agent output (raw, immutable)
    data/processed/claims_refined.csv            the new claims, machine-checked
    data/processed/investors_refined.csv         investors rebuilt from frozen claims + refined claims
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from investordb.registries import core_name

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "data" / "processed"
REFINE_DIR = ROOT / "data" / "raw" / "agents" / "refine"
BATCH_DIR = REFINE_DIR / "batches"
BATCH_SIZE = 4


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def claims_by_investor(investors: list[dict], claims: list[dict]) -> dict[str, list[dict]]:
    """Verified claims of each included investor, including those of merged duplicates (evidence_ids)."""
    by_cand: dict[str, list[dict]] = defaultdict(list)
    for c in claims:
        by_cand[c["candidate_id"]].append(c)
    return {inv["candidate_id"]: [c for m in inv["evidence_ids"].split() for c in by_cand.get(m, [])
                                  if c["auto_check"] == "ok"] for inv in investors}


def counted_deals(claims: list[dict]) -> dict[str, dict]:
    """The dated deal claim that sets each company's investment date (the same rule as rules.investments_from)."""
    out: dict[str, dict] = {}
    for c in claims:
        if c["field"] != "investments" or c.get("deal_context") != "deal" or c.get("attributed") == "0":
            continue
        if not c["event_date"]:
            continue
        company = str((json.loads(c["value"]) or {}).get("company") or "").strip()
        key = core_name(company)
        if company and (key not in out or c["event_date"] > out[key]["event_date"]):
            out[key] = c
    return out


def batch_record(inv: dict, claims: list[dict]) -> dict:
    deals = counted_deals(claims)
    funds = []
    for c in claims:
        if c["field"] == "funds":
            f = json.loads(c["value"]) or {}
            funds.append({"name": f.get("name"), "size": f.get("size"), "currency": f.get("currency"),
                          "vintage": f.get("vintage"), "source_url": c["source_url"]})
    portfolio = sorted({str((json.loads(c["value"]) or {}).get("company") or "").strip() for c in claims
                        if c["field"] == "investments"} - {"", *(json.loads(d["value"])["company"].strip()
                                                                 for d in deals.values())})
    return {
        "candidate_id": inv["candidate_id"],
        "name": inv["name"],
        "website": inv["website"] or None,
        "legal_name": inv["legal_name"] or None,
        "known_funds": funds,
        "deals_to_check": [{"company": json.loads(d["value"])["company"], "listed_date": d["event_date"][:10],
                            "source_url": d["source_url"]}
                           for d in sorted(deals.values(), key=lambda d: d["event_date"], reverse=True)],
        "other_portfolio_companies": portfolio,
    }


def make_batches() -> list[Path]:
    investors = _read(PROCESSED / "investors.csv")
    claims = claims_by_investor(investors, _read(PROCESSED / "claims.csv"))
    records = [batch_record(inv, claims[inv["candidate_id"]]) for inv in sorted(investors, key=lambda r: r["candidate_id"])]
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    paths = []
    for n, start in enumerate(range(0, len(records), BATCH_SIZE), 1):
        path = BATCH_DIR / f"rf_b{n:02d}.json"
        path.write_text(json.dumps(records[start:start + BATCH_SIZE], ensure_ascii=False, indent=2), encoding="utf-8")
        paths.append(path)
    return paths
