"""Checked claims + registry identity + rules -> decisions and the final tables.

    investors.csv     INCLUDED records (wide, one row per investor; every cell traceable to claims.csv)
    rejected.csv      REJECTED and OOS records with reason code
    needs_review.csv  records the rules could not decide automatically
    decisions.csv     all of the above in one table
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from dataclasses import asdict
from datetime import date
from pathlib import Path

from investordb.candidates import OUT as CANDIDATES_CSV
from investordb.evidence import CLAIMS_CSV, load_records
from investordb.money import Money, parse_money, to_eur
from investordb.registries import RegistryRecord, ares_get, core_name, rpo_search
from investordb.rules import Decision, decide
from investordb.triage import TRIAGE_CSV

PROCESSED = CLAIMS_CSV.parent


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def registry_for(claims: list[dict], triage: dict | None) -> RegistryRecord | None:
    """Prefer the IČO the agent found (and the checker verified) on the investor's own pages; else the triage match."""
    ids: list[tuple[str, str]] = []
    for c in claims:
        if c["field"] == "identity" and c["auto_check"] == "ok":
            v = json.loads(c["value"]) or {}
            if v.get("company_id"):
                ids.append((str(v["company_id"]).replace(" ", ""), v.get("country", "")))
    if triage and triage.get("company_id"):
        ids.append((triage["company_id"], {"ARES": "CZ", "RPO": "SK"}.get(triage.get("registry", ""), "")))
    for ico, country in ids:
        if country in ("CZ", "") and (rec := ares_get(ico)):
            return rec
        if country in ("SK", ""):
            recs = rpo_search(ico=ico, limit=1)
            if recs:
                return recs[0]
    return None


def _first(claims: list[dict], field: str):
    vals = [json.loads(c["value"]) for c in claims if c["field"] == field and c["auto_check"] == "ok"]
    return vals[0] if vals else None


def _eur(value: float | None) -> str:
    return f"{value:.0f}" if value is not None else ""


def total_capital(ok: list[dict], on: str) -> tuple[float | None, str, bool]:
    """(EUR amount, method, approx). Stated AUM wins; otherwise the sum of all verified fund sizes (D17)."""
    aum = _first(ok, "total_capital")
    # only an explicit AUM counts here - a single fund's size must not pose as the firm's total capital
    if aum and aum.get("capital_type") == "aum" and (m := parse_money(aum.get("amount"), aum.get("currency"))):
        return to_eur(m, on), "aum_stated", m.approx
    funds: dict[str, Money] = {}
    for c in ok:
        if c["field"] != "funds":
            continue
        f = json.loads(c["value"]) or {}
        m = parse_money(f.get("size"), f.get("currency"))
        if m:
            funds.setdefault(core_name(f.get("name") or c["source_url"]), m)  # same fund cited twice counts once
    if not funds:
        return None, "", False
    total = sum(to_eur(m, on) for m in funds.values())
    return total, f"sum_of_{len(funds)}_funds", any(m.approx for m in funds.values())


def wide_row(rec: dict, d: Decision, reg: RegistryRecord | None, ok: list[dict], as_of: date, name: str) -> dict:
    on = as_of.isoformat()
    ticket = _first(ok, "ticket") or {}
    t_min = parse_money(ticket.get("min"), ticket.get("currency"))
    t_max = parse_money(ticket.get("max"), ticket.get("currency"))
    capital_eur, capital_method, capital_approx = total_capital(ok, on)
    invs = sorted((c for c in ok if c["field"] == "investments" and c["event_date"]), key=lambda c: c["event_date"])
    last = invs[-1] if invs else None
    funds = [json.loads(c["value"]) for c in ok if c["field"] == "funds"]
    return dict(
        candidate_id=d.candidate_id, name=name, legal_name=reg.name if reg else "",
        company_id=reg.company_id if reg else "", registry_url=reg.source_url if reg else "",
        hq_country=d.hq, website=rec.get("website") or "", investor_types=",".join(d.types),
        sectors=",".join(_first(ok, "sectors") or []), stages=",".join(_first(ok, "stages") or []),
        ticket_min=ticket.get("min") or "", ticket_max=ticket.get("max") or "",
        ticket_min_eur=_eur(to_eur(t_min, on)), ticket_max_eur=_eur(to_eur(t_max, on)),
        total_capital_eur=_eur(capital_eur), capital_method=capital_method, capital_approx=int(capital_approx),
        funds="; ".join(f"{f.get('name')} ({f.get('size') or '?'})" for f in funds),
        n_investments=d.n_investments, n_investments_36m=d.n_recent, last_investment_date=d.last_investment,
        last_investment=(json.loads(last["value"]) or {}).get("company", "") if last else "",
        last_investment_source=last["source_url"] if last else "",
        status=d.status, reason=d.reason, tier=d.tier, explanation=d.explanation, as_of=as_of.isoformat(),
    )


def run(as_of: date, records: list[dict] | None = None) -> list[dict]:
    records = records or load_records()
    claims_by_cand: dict[str, list[dict]] = defaultdict(list)
    for c in _read_csv(CLAIMS_CSV):
        claims_by_cand[c["candidate_id"]].append(c)
    triage = {t["candidate_id"]: t for t in _read_csv(TRIAGE_CSV)}
    names = {c["candidate_id"]: c["name"] for c in _read_csv(CANDIDATES_CSV)}

    rows, seen_ids = [], {}
    for rec in records:
        cid = rec["candidate_id"]
        claims = claims_by_cand.get(cid, [])
        reg = registry_for(claims, triage.get(cid))
        d = decide(cid, claims, reg, as_of)
        if d.status == "INCLUDED" and reg:
            if reg.company_id in seen_ids:  # E8: the same legal entity reached us under two names
                d = Decision(**{**asdict(d), "status": "REJECTED", "reason": "E8",
                                "explanation": f"duplicate of {seen_ids[reg.company_id]}"})
            else:
                seen_ids[reg.company_id] = cid
        ok = [c for c in claims if c["auto_check"] == "ok"]
        rows.append(wide_row(rec, d, reg, ok, as_of, names.get(cid) or rec.get("name", "")))

    _write(PROCESSED / "decisions.csv", rows)
    _write(PROCESSED / "investors.csv", [r for r in rows if r["status"] == "INCLUDED"])
    _write(PROCESSED / "rejected.csv", [r for r in rows if r["status"] in ("REJECTED", "OOS")])
    _write(PROCESSED / "needs_review.csv", [r for r in rows if r["status"] == "NEEDS_REVIEW"])
    return rows


def _write(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.unlink(missing_ok=True)
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
