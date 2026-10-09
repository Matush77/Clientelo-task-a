"""Inclusion/exclusion rules from docs/PLAN.md (I1-I5, E1-E9, OOS) and confidence tiers A/B/C.

Pure functions: input = machine-checked claims + registry record + reference date; output = Decision.
Only claims whose quote was found on the source page (auto_check == "ok") count as evidence.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date

from investordb.evidence import domain
from investordb.registries import RegistryRecord, core_name

INVESTING_TYPES = {"vc", "cvc", "public_vc", "pe", "family_office", "angel_network", "accelerator"}
PILOT_TYPES = {"vc", "cvc", "public_vc"}
PILOT_COUNTRIES = {"CZ", "SK"}
# order = priority when an entity has several non-investor types
NON_INVESTOR_TYPES = {
    "crowdfunding_platform": "E3", "advisory": "E3", "real_estate": "E4", "lender": "E4",
    "fund_of_funds": "E5", "group_holding": "E6", "grant_agency": "E9",
}
ACTIVITY_MONTHS = 36
NEW_FUND_MONTHS = 24


def months_before(d: date, months: int) -> date:
    y, m = divmod(d.year * 12 + d.month - 1 - months, 12)
    return date(y, m + 1, min(d.day, 28))


@dataclass
class Investment:
    company: str
    date: str  # ISO, '' if unknown
    sources: set[str] = field(default_factory=set)  # source domains


@dataclass
class Decision:
    candidate_id: str
    status: str  # INCLUDED | REJECTED | OOS | NEEDS_REVIEW
    reason: str  # E1..E9, OOS_HQ, OOS_TYPE, REVIEW_*, or "" when included
    tier: str  # A | B | C | ""
    explanation: str
    types: list[str]
    hq: str
    n_investments: int
    n_recent: int
    last_investment: str


def _values(claims: list[dict], name: str) -> list:
    return [json.loads(c["value"]) for c in claims if c["field"] == name]


def investments_from(claims: list[dict]) -> list[Investment]:
    by_company: dict[str, Investment] = {}
    for c in claims:
        if c["field"] != "investments":
            continue
        context = c.get("deal_context") or "deal"  # older claims / tests without context are treated as deals
        if context == "exit":  # "Taikun's exit to Cloudera" is not an investment
            continue
        if c.get("attributed") == "0":  # the article proves a round, but not that this candidate took part
            continue
        value = json.loads(c["value"]) or {}
        company = str(value.get("company") or "").strip()
        if not company:
            continue
        inv = by_company.setdefault(core_name(company), Investment(company=company, date=""))
        # a bare mention (portfolio list, overview article) proves the investment, but its date is not a deal date
        if context == "deal":
            inv.date = max(inv.date, c.get("event_date") or "")
        inv.sources.add(domain(c["source_url"]))
    return list(by_company.values())


def decide(candidate_id: str, claims: list[dict], registry: RegistryRecord | None, as_of: date) -> Decision:
    ok = [c for c in claims if c.get("auto_check") == "ok"]
    unverifiable = [c for c in claims if c.get("auto_check") == "blocked"]

    types = sorted({t for v in _values(ok, "investor_type") for t in (v if isinstance(v, list) else [v])})
    hq_values = [v for v in _values(ok, "hq_country") if v]
    hq = hq_values[0] if hq_values else (registry.country if registry else "")

    investments = investments_from(ok)
    dated = [i for i in investments if i.date]
    window_start = months_before(as_of, ACTIVITY_MONTHS).isoformat()
    recent = [i for i in dated if i.date >= window_start]
    last = max((i.date for i in dated), default="")
    new_fund_start = months_before(as_of, NEW_FUND_MONTHS).isoformat()
    new_fund = any(c.get("event_date", "") >= new_fund_start for c in ok if c["field"] == "funds")

    def out(status: str, reason: str, why: str, tier: str = "") -> Decision:
        return Decision(candidate_id, status, reason, tier, why, types, hq, len(investments), len(recent), last)

    # E2 (registry): the legal entity no longer exists
    if registry and not registry.active:
        return out("REJECTED", "E2", f"entity dissolved per {registry.registry} ({registry.dissolved})")
    # OOS: a real investor, but the investment team sits outside CZ/SK
    if hq and hq not in PILOT_COUNTRIES:
        return out("OOS", "OOS_HQ", f"HQ outside CZ/SK ({hq})")
    # E3-E9: what the entity does is not investing into companies
    non_investor = [t for t in NON_INVESTOR_TYPES if t in types]
    if non_investor and not set(types) & INVESTING_TYPES:
        return out("REJECTED", NON_INVESTOR_TYPES[non_investor[0]], f"evidence shows type {types}, not an investor into companies")
    # E1 / E7: no verified investment at all
    if not investments:
        if any(c["field"] == "investments" for c in unverifiable):
            return out("NEEDS_REVIEW", "REVIEW_BLOCKED", "investment sources block automatic checking")
        if set(types) & INVESTING_TYPES:
            return out("REJECTED", "E1", "describes itself as an investor, but no verified investment")
        return out("REJECTED", "E7", "no evidence of any investment - investor-like name only")
    if not dated:
        return out("REJECTED", "E1", "investments found, but none is dated")
    # E2 (activity): nothing in the last 36 months
    if not recent:
        return out("REJECTED", "E2", f"no investment since {window_start} (last {last})")
    # I2: repeated investing (>= 2), unless it is a new fund
    if len(investments) < 2 and not new_fund:
        return out("REJECTED", "E1", "only one documented investment and not a new fund")
    # I4/I5: type must be verified, and the pilot covers VC only
    if not types:
        return out("NEEDS_REVIEW", "REVIEW_TYPE", "active investor, but its type could not be verified")
    if not set(types) & PILOT_TYPES:
        return out("OOS", "OOS_TYPE", f"real investor but not VC (type {types or 'unknown'})")
    # I1: identity confirmed in a registry
    if registry is None:
        return out("NEEDS_REVIEW", "REVIEW_IDENTITY", "no registry record found for the management company")

    independent = {d for i in dated for d in i.sources}
    if len(dated) >= 2 and len(independent) >= 2:
        tier = "A"
    elif recent:
        tier = "B"
    else:
        tier = "C"
    if tier == "C":
        return out("NEEDS_REVIEW", "REVIEW_TIER_C", "evidence too weak for automatic inclusion", tier)
    return out("INCLUDED", "", f"{len(investments)} investments ({len(recent)} since {window_start}), "
                                f"{len(independent)} source domains", tier)
