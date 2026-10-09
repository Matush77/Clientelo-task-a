"""Refinement of the weak fields of INCLUDED investors by a stronger model (Sonnet 5.5) - decision D38.

The frozen database (tag pilot-frozen-v3) stays as measured. Refinement re-extracts, for every included investor,
(a) each fund with its fundraising status (final close / first close / target) and (b) the real deal date of every
dated investment, in the same claim format. The new claims pass the same machine checks as all other claims, then
the investor rows are rebuilt with the same rules and written next to the frozen ones:

    data/raw/agents/refine/batches/rf_bNN.json   input per agent (what the database currently says)
    data/raw/agents/refine/rf_bNN.json           agent output (raw, immutable)
    data/processed/claims_refined.csv            the new claims, machine-checked (+ the agent's verdict)
    data/processed/investors_refined.csv         investors rebuilt from frozen claims + refined claims
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import date
from pathlib import Path

from investordb.evidence import check, flatten
from investordb.pipeline import wide_row
from investordb.registries import RegistryRecord, core_name
from investordb.rules import ACTIVITY_MONTHS, decide, months_before

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "data" / "processed"
REFINE_DIR = ROOT / "data" / "raw" / "agents" / "refine"
BATCH_DIR = REFINE_DIR / "batches"
CLAIMS_REFINED = PROCESSED / "claims_refined.csv"
INVESTORS_REFINED = PROCESSED / "investors_refined.csv"
BATCH_SIZE = 4
NEW_DEAL_IDX = 100  # idx offset of new deals in claims_refined.csv (deal checks keep their own position)


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _value(c: dict) -> dict:
    v = json.loads(c["value"]) if c.get("value") else None
    return v if isinstance(v, dict) else {}


def claims_by_investor(investors: list[dict], claims: list[dict], only_ok: bool = True) -> dict[str, list[dict]]:
    """Claims of each included investor, including those of merged duplicates (evidence_ids)."""
    by_cand: dict[str, list[dict]] = defaultdict(list)
    for c in claims:
        by_cand[c["candidate_id"]].append(c)
    return {inv["candidate_id"]: [c for m in inv["evidence_ids"].split() for c in by_cand.get(m, [])
                                  if c["auto_check"] == "ok" or not only_ok] for inv in investors}


def counted_deals(claims: list[dict]) -> dict[str, dict]:
    """The dated deal claim that sets each company's investment date (the same rule as rules.investments_from)."""
    out: dict[str, dict] = {}
    for c in claims:
        if c["field"] != "investments" or c.get("auto_check") != "ok":
            continue
        if c.get("deal_context") != "deal" or c.get("attributed") == "0" or not c["event_date"]:
            continue
        company = str(_value(c).get("company") or "").strip()
        key = core_name(company)
        if company and (key not in out or c["event_date"] > out[key]["event_date"]):
            out[key] = c
    return out


# --- 1. batches for the agents ---------------------------------------------------------------------

def batch_record(inv: dict, claims: list[dict]) -> dict:
    deals = counted_deals(claims)
    funds = [{"name": f.get("name"), "size": f.get("size"), "currency": f.get("currency"), "vintage": f.get("vintage"),
              "source_url": c["source_url"]} for c in claims if c["field"] == "funds" for f in [_value(c)]]
    dealt = {str(_value(d).get("company")).strip() for d in deals.values()}
    portfolio = sorted({str(_value(c).get("company") or "").strip() for c in claims if c["field"] == "investments"}
                       - {""} - dealt)
    return {
        "candidate_id": inv["candidate_id"],
        "name": inv["name"],
        "website": inv["website"] or None,
        "legal_name": inv["legal_name"] or None,
        "known_funds": funds,
        "deals_to_check": [{"company": _value(d)["company"], "listed_date": d["event_date"][:10],
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


# --- 2. agent output -> checked claims ---------------------------------------------------------------

def load_outputs() -> list[dict]:
    out = []
    for path in sorted(REFINE_DIR.glob("rf_b*.json")):
        out += json.loads(path.read_text(encoding="utf-8"))
    return out


def deal_checks(record: dict) -> list[dict]:
    """One entry per checked deal (+ new deals): company, verdict, note and - if the agent cited a source - the
    index of its claim among the record's investment claims."""
    out = []
    for i, d in enumerate(record.get("deal_checks") or []):
        company = d.get("company") or (d.get("value") or {}).get("company") or ""
        out.append({"company": company, "listed_date": d.get("listed_date") or "", "verdict": d.get("verdict") or "",
                    "note": d.get("note") or "", "idx": i if d.get("source_url") and d.get("quote") else None})
    for i, d in enumerate(record.get("new_deals") or []):
        out.append({"company": (d.get("value") or {}).get("company") or "", "listed_date": "", "verdict": "new",
                    "note": d.get("note") or "", "idx": NEW_DEAL_IDX + i})
    return out


def as_evidence_record(record: dict, website: str | None) -> dict:
    """Agent output -> the evidence-record shape, so flatten() and check() apply unchanged."""
    investments = {}
    for i, d in enumerate(record.get("deal_checks") or []):
        if d.get("source_url") and d.get("quote"):
            value = dict(d.get("value") or {})
            value.setdefault("company", d.get("company"))
            value["verdict"] = d.get("verdict")
            investments[i] = {**d, "value": value}
    for i, d in enumerate(record.get("new_deals") or []):
        investments[NEW_DEAL_IDX + i] = {**d, "value": {**(d.get("value") or {}), "verdict": "new"}}
    return {"candidate_id": record["candidate_id"], "website": website, "funds": record.get("funds") or [],
            "investments": investments}


def checked_claims(outputs: list[dict], investors: dict[str, dict], names: dict[str, list[str]]) -> list[dict]:
    rows = []
    for rec in outputs:
        ev = as_evidence_record(rec, investors[rec["candidate_id"]]["website"])
        invs = ev.pop("investments")
        rows += [r for r in flatten({**ev, "investments": []})]
        for idx, claim in invs.items():
            got = flatten({"candidate_id": ev["candidate_id"], "website": ev["website"], "investments": [claim]})
            for r in got:
                r.idx = idx
            rows += got
    check(rows, names)
    return [asdict(r) for r in rows]


# --- 3. frozen claims + refined claims -> rebuilt rows -------------------------------------------------

def merge(old: list[dict], new: list[dict], checks: list[dict]) -> tuple[list[dict], list[str]]:
    """Frozen claims of one investor + its refined claims -> the claim set the rules see after refinement.
    Funds: a verified refined claim about a known fund supersedes the frozen claims about it.
    Deals: a verified refined date replaces the frozen one; a date the agent could not confirm stops counting."""
    notes: list[str] = []
    good = [c for c in new if c["auto_check"] == "ok"]
    covered = set()
    for c in good:
        if c["field"] == "funds":
            v = _value(c)
            covered |= {core_name(v.get("known_as") or ""), core_name(v.get("name") or "")} - {""}
    merged = []
    for c in old:
        if c["field"] == "funds" and core_name(_value(c).get("name") or "") in covered:
            continue
        if c["field"] == "funds" and c["auto_check"] == "ok":
            notes.append(f"fond {_value(c).get('name')} znovu neoverený")
        merged.append(dict(c))
    merged += [c for c in good if c["field"] == "funds"]

    by_idx = {int(c["idx"]): c for c in new if c["field"] == "investments"}
    for chk in checks:
        r = by_idx.get(chk["idx"]) if chk["idx"] is not None else None
        r_ok = bool(r) and r["auto_check"] == "ok" and r["attributed"] != "0" and r["deal_context"] == "deal"
        verdict, key = chk["verdict"], core_name(chk["company"])
        if verdict == "new":
            if r_ok:
                merged.append(r)
                notes.append(f"nový obchod {chk['company']} ({r['event_date'][:7]})")
            continue
        olds = [c for c in merged if c["field"] == "investments" and core_name(str(_value(c).get("company") or "")) == key]
        if verdict in ("confirmed", "corrected") and r_ok:
            for c in olds:
                if c.get("deal_context") == "deal":
                    c["deal_context"] = "mention"
            merged.append(r)
            if verdict == "corrected":
                notes.append(f"{chk['company']}: dátum {chk['listed_date'][:7]} -> {r['event_date'][:7]}")
            continue
        if verdict == "confirmed":  # the agent agrees, but its own quote failed the check: the frozen claim stays
            continue
        for c in olds:
            if c.get("deal_context") == "deal":
                c["deal_context"] = "mention"
            if verdict == "not_this_investor":
                c["attributed"] = "0"
        label = {"not_this_investor": "investor sa na kole nepodieľal",
                 "not_found": "dátum obchodu sa nepotvrdil"}.get(verdict, "opravený dátum sa nepodarilo overiť")
        notes.append(f"{chk['company']}: {label}")
    return merged, notes


def registry_of(inv: dict) -> RegistryRecord | None:
    """The registry identity of the frozen row (already verified, D35) - refinement does not touch identity."""
    if not inv["registry_url"]:
        return None
    sk = "rpo" in inv["registry_url"] or "statistics.sk" in inv["registry_url"]
    return RegistryRecord(registry="RPO" if sk else "ARES", company_id=inv["company_id"], name=inv["legal_name"],
                          country="SK" if sk else "CZ", address="", legal_form="", founded=None, dissolved=None,
                          source_url=inv["registry_url"])


def rebuild(inv: dict, merged: list[dict], notes: list[str], as_of: date) -> dict:
    reg = registry_of(inv)
    d = decide(inv["candidate_id"], merged, reg, as_of)
    ok = [c for c in merged if c["auto_check"] == "ok"]
    row = wide_row({"website": inv["website"]}, d, reg, ok, as_of, inv["name"])
    row["evidence_ids"] = inv["evidence_ids"]
    if d.status != "INCLUDED":  # refinement never silently drops a record: a human decides
        row.update(status="NEEDS_REVIEW", reason="REVIEW_REFINED", tier="",
                   explanation=f"after refinement the rules say {d.status} {d.reason}: {d.explanation}")
    row["refine_notes"] = "; ".join(notes)
    return row


def integrity(row: dict, merged: list[dict]) -> list[str]:
    """The check-db rules on the rebuilt row: an INCLUDED record needs a verified, attributed, dated deal in the window."""
    problems = []
    window = months_before(date.fromisoformat(row["as_of"]), ACTIVITY_MONTHS).isoformat()
    if row["status"] == "INCLUDED" and not any(c["event_date"] >= window for c in counted_deals(merged).values()):
        problems.append(f"{row['candidate_id']}: no verified, dated deal since {window}")
    if row["total_capital_eur"] and not any(c["field"] in ("funds", "total_capital") and c["auto_check"] == "ok"
                                            for c in merged):
        problems.append(f"{row['candidate_id']}: capital without a verified claim")
    return problems


def run(as_of: date) -> dict:
    investors = {r["candidate_id"]: r for r in _read(PROCESSED / "investors.csv")}
    outputs = {r["candidate_id"]: r for r in load_outputs()}
    cand = {c["candidate_id"]: c for c in _read(PROCESSED / "candidates.csv")}
    names = {cid: [n for m in inv["evidence_ids"].split() if m in cand
                   for n in [cand[m]["name"], *[a for a in cand[m]["aliases"].split(" | ") if a]]]
             for cid, inv in investors.items()}
    new = checked_claims(list(outputs.values()), investors, names)
    checks = {cid: deal_checks(rec) for cid, rec in outputs.items()}
    old = claims_by_investor(list(investors.values()), _read(PROCESSED / "claims.csv"), only_ok=False)

    rows, problems, merged_by = [], [], {}
    for cid, inv in investors.items():
        mine = [c for c in new if c["candidate_id"] == cid]
        merged, notes = merge(old[cid], mine, checks.get(cid, [])) if cid in outputs else (old[cid], ["nespracované"])
        row = rebuild(inv, merged, notes, as_of)
        rows.append(row)
        merged_by[cid] = merged
        problems += integrity(row, merged)

    with CLAIMS_REFINED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(new[0].keys()) + ["verdict"])
        w.writeheader()
        for c in new:
            w.writerow({**c, "verdict": _value(c).get("verdict") or (_value(c).get("status") or "")})
    with INVESTORS_REFINED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["candidate_id"]))
    return {"rows": rows, "claims": new, "checks": checks, "merged": merged_by, "problems": problems,
            "missing": sorted(set(investors) - set(outputs))}


def summary(result: dict) -> dict:
    """Counts for the before/after report."""
    claims, checks = result["claims"], result["checks"]
    return {
        "fund_status": Counter(_value(c).get("status") for c in claims if c["field"] == "funds"),
        "auto_check": Counter(c["auto_check"] for c in claims),
        "verdicts": Counter(chk["verdict"] for chks in checks.values() for chk in chks),
    }
