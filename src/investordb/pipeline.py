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
from investordb.evidence import CLAIMS_CSV, T4_DOMAINS, _under, domain, load_records
import re

from investordb.money import TARGET_FUND, Money, eur_rate, parse_money, plausible, to_eur
from investordb.registries import RegistryRecord, ares_get, core_name, legal_form, rpo_search
from investordb.rules import Decision, decide
from investordb.candidates import match_key
from investordb.registries import ares_search
from investordb.triage import TRIAGE_CSV, has_investment_signal, registry_name_matches

PROCESSED = CLAIMS_CSV.parent
ALIASES_CSV = CANDIDATES_CSV.parents[1] / "seeds" / "aliases.csv"


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def registry_for(claims: list[dict], triage: dict | None, names: list[str] = ()) -> RegistryRecord | None:
    """Identity in a registry, strongest evidence first:
    1. the IČO the agent found (and the checker verified) on the investor's own pages,
    2. the triage match,
    3. a name search with the verified legal name, then with the brand name(s) - accepted only on a strict match.
    """
    ids: list[tuple[str, str]] = []
    legal_names: list[tuple[str, str]] = []
    hq = ""
    for c in claims:
        if c["auto_check"] != "ok":
            continue
        v = json.loads(c["value"])
        if c["field"] == "identity" and isinstance(v, dict):
            if v.get("company_id"):
                ids.append((str(v["company_id"]).replace(" ", ""), v.get("country", "")))
            elif v.get("legal_name"):
                legal_names.append((v["legal_name"], v.get("country", "")))
        if c["field"] == "hq_country" and v in ("CZ", "SK"):
            hq = v
    if triage and triage.get("company_id"):
        ids.append((triage["company_id"], {"ARES": "CZ", "RPO": "SK"}.get(triage.get("registry", ""), "")))
    for ico, country in ids:
        if country in ("CZ", "") and (rec := ares_get(ico)):
            return rec
        if country in ("SK", ""):
            recs = rpo_search(ico=ico, limit=1)
            if recs:
                return recs[0]
    # a verified legal name is the strongest lead: if there is one, the looser brand-name search is not used
    candidates = legal_names if legal_names else [(n, hq) for n in names if n]
    for name, country in candidates:
        country = country if country in ("CZ", "SK") else hq
        # raw name too: normalising "J&T Ventures" to "j t ventures" makes ARES find nothing
        queries = list(dict.fromkeys(q for q in (name, match_key(name), match_key(name).split(" ")[0]) if q))
        found = []
        for q in queries:
            if country in ("CZ", ""):
                found += ares_search(q, limit=50 if " " not in q else 10)[1]
            if country in ("SK", "") and not found:
                found += rpo_search(name=q, limit=5)
            if any(r.active and registry_name_matches(r.name, name) for r in found):
                break
        matches = [r for r in found if r.active and registry_name_matches(r.name, name)]
        if legal_names and legal_form(name):  # "Czech Founders VC s.r.o." must not match "Czech Founders z.ú."
            matches = [r for r in matches if legal_form(r.name) in ("", legal_form(name))]
        if matches:
            # prefer a name that marks an investment vehicle, then the shortest (management company over sub-funds)
            return min(matches, key=lambda r: (not has_investment_signal(r.name), len(r.name)))
    return None


def _first(claims: list[dict], field: str):
    vals = [json.loads(c["value"]) for c in claims if c["field"] == field and c["auto_check"] == "ok"]
    return vals[0] if vals else None


def _display_date(claim: dict) -> str:
    """Show a date with the precision the source gave: '2024' stays '2024', not '2024-01-01'."""
    d, precision = claim["event_date"], claim.get("event_date_precision", "day")
    return d[:4] if precision == "year" else d[:7] if precision == "month" else d


def _eur(value: float | None) -> str:
    return f"{value:.0f}" if value is not None else ""


def _conversion_note(m: Money, on: str) -> str:
    return "" if m.currency == "EUR" else f"{m.raw} → EUR kurzom ECB {eur_rate(m.currency, on)} ({on})"


def total_capital(ok: list[dict], on: str) -> dict:
    """Stated AUM wins; otherwise the sum of all verified CLOSED fund sizes (D17, D30).
    Target / planned funds and ranges are listed separately, never summed; implausible amounts are dropped + flagged."""
    out = {"eur": None, "method": "", "approx": False, "targets": [], "notes": [], "flags": []}
    aum = _first(ok, "total_capital")
    # only an explicit AUM counts here - a single fund's size must not pose as the firm's total capital
    if aum and aum.get("capital_type") == "aum" and (m := parse_money(aum.get("amount"), aum.get("currency"))):
        eur = to_eur(m, on)
        if plausible("aum", eur) and not m.is_range:
            out.update(eur=eur, method="aum_stated", approx=m.approx, notes=[n for n in [_conversion_note(m, on)] if n])
            return out
        out["flags"].append(f"AUM '{m.raw}' vyradené (rozpätie alebo nereálna hodnota)")
    funds: dict[str, Money] = {}
    for c in ok:
        if c["field"] != "funds":
            continue
        f = json.loads(c["value"]) or {}
        m = parse_money(f.get("size"), f.get("currency"))
        if not m:
            continue
        name = f.get("name") or "fond"
        if m.is_range or TARGET_FUND.search(c["quote"]):
            out["targets"].append(f"{name}: {m.raw} (cieľ / plán)")
            continue
        if not plausible("fund", to_eur(m, on)):
            out["flags"].append(f"fond '{name}: {m.raw}' vyradený (nereálna hodnota)")
            continue
        funds.setdefault(core_name(name), m)  # same fund cited twice counts once
    if funds:
        out.update(eur=sum(to_eur(m, on) for m in funds.values()), method=f"sum_of_{len(funds)}_closed_funds",
                   approx=any(m.approx for m in funds.values()),
                   notes=[n for m in funds.values() if (n := _conversion_note(m, on))])
    return out


def ticket_eur(ticket: dict, on: str) -> tuple[float | None, float | None, list[str]]:
    """Ticket min/max in EUR. 'min 2, max 15 mil. EUR' -> the bare minimum borrows the maximum's scale."""
    flags = []
    t_min = parse_money(ticket.get("min"), ticket.get("currency"))
    t_max = parse_money(ticket.get("max"), ticket.get("currency"))
    if t_min and t_min.is_range and not t_max:  # "€1-3M" written into one field
        t_max = Money(t_min.amount_max, t_min.currency, t_min.approx, t_min.raw)
    if t_min and t_max and t_min.amount < 1000 <= t_max.amount and not re.search(r"[a-z]", str(ticket.get("min")).lower().replace("eur", "")):
        for factor in (1e6, 1e3):
            if t_max.amount >= factor:
                t_min = Money(t_min.amount * factor, t_min.currency, t_min.approx, t_min.raw)
                break
    lo, hi = to_eur(t_min, on), to_eur(t_max, on)
    for label, val, m in (("min", lo, t_min), ("max", hi, t_max)):
        if m and not plausible("ticket", val):
            flags.append(f"tiket {label} '{m.raw}' vyradený (nereálna hodnota)")
    return (lo if plausible("ticket", lo) else None), (hi if plausible("ticket", hi) else None), flags


def wide_row(rec: dict, d: Decision, reg: RegistryRecord | None, ok: list[dict], as_of: date, name: str) -> dict:
    on = as_of.isoformat()
    ticket = _first(ok, "ticket") or {}
    t_min_eur, t_max_eur, ticket_flags = ticket_eur(ticket, on)
    cap = total_capital(ok, on)
    invs = sorted((c for c in ok if c["field"] == "investments" and c["event_date"] and c.get("deal_context") == "deal"),
                  key=lambda c: c["event_date"])
    last = invs[-1] if invs else None
    funds = [json.loads(c["value"]) for c in ok if c["field"] == "funds"]
    return dict(
        candidate_id=d.candidate_id, name=name, legal_name=reg.name if reg else "",
        company_id=reg.company_id if reg else "", registry_url=reg.source_url if reg else "",
        hq_country=d.hq, website=rec.get("website") or "", investor_types=",".join(d.types),
        sectors=",".join(_first(ok, "sectors") or []), stages=",".join(_first(ok, "stages") or []),
        ticket_min=ticket.get("min") or "", ticket_max=ticket.get("max") or "",
        ticket_min_eur=_eur(t_min_eur), ticket_max_eur=_eur(t_max_eur),
        total_capital_eur=_eur(cap["eur"]), capital_method=cap["method"], capital_approx=int(cap["approx"]),
        capital_note="; ".join(cap["notes"]), funds_target="; ".join(cap["targets"]),
        funds="; ".join(f"{f.get('name')} ({f.get('size') or '?'})" for f in funds),
        data_flags="; ".join(cap["flags"] + ticket_flags),
        n_investments=d.n_investments, n_investments_36m=d.n_recent,
        last_investment_date=_display_date(last) if last else "",
        last_investment=(json.loads(last["value"]) or {}).get("company", "") if last else "",
        last_investment_source=last["source_url"] if last else "",
        status=d.status, reason=d.reason, tier=d.tier, explanation=d.explanation, as_of=as_of.isoformat(),
        evidence_ids=" ".join(sorted({c["candidate_id"] for c in ok}) or [d.candidate_id]),
    )


def entity_keys(rec: dict, claims: list[dict]) -> set[str]:
    """Keys that identify the same firm: a verified company ID, or the official website domain."""
    keys = set()
    for c in claims:
        if c["field"] == "identity" and c["auto_check"] == "ok":
            ico = str((json.loads(c["value"]) or {}).get("company_id") or "").replace(" ", "")
            if ico:
                keys.add(f"ico:{ico}")
    dom = domain(rec.get("website"))
    if dom and not _under(dom, T4_DOMAINS):
        keys.add(f"web:{dom}")
    return keys


def merge_duplicates(records: list[dict], claims_by_cand: dict[str, list[dict]]) -> dict[str, str]:
    """Union-find over entity keys -> {candidate_id: primary candidate_id} (E8, decision D4)."""
    parent = {r["candidate_id"]: r["candidate_id"] for r in records}

    def find(x: str) -> str:
        while parent[x] != x:
            x = parent[x]
        return x

    # documented manual merges (data/seeds/aliases.csv) for brands without their own website or company ID
    manual = {a["candidate_id"]: a["same_as"] for a in _read_csv(ALIASES_CSV)}
    owner: dict[str, str] = {}
    for r in sorted(records, key=lambda r: r["candidate_id"]):  # lowest id becomes the primary
        cid = r["candidate_id"]
        keys = entity_keys(r, claims_by_cand.get(cid, []))
        if cid in manual:
            keys.add(f"alias:{manual[cid]}")
        if cid in manual.values():
            keys.add(f"alias:{cid}")
        for key in keys:
            if key in owner:
                a, b = sorted((find(owner[key]), find(cid)))
                parent[b] = a
            else:
                owner[key] = cid
    return {cid: find(cid) for cid in parent}


def run(as_of: date, records: list[dict] | None = None) -> list[dict]:
    records = records or load_records()
    claims_by_cand: dict[str, list[dict]] = defaultdict(list)
    for c in _read_csv(CLAIMS_CSV):
        claims_by_cand[c["candidate_id"]].append(c)
    triage = {t["candidate_id"]: t for t in _read_csv(TRIAGE_CSV)}
    cand_rows = {c["candidate_id"]: c for c in _read_csv(CANDIDATES_CSV)}
    names = {cid: c["name"] for cid, c in cand_rows.items()}

    def all_names(cids: list[str]) -> list[str]:
        out = []
        for m in cids:
            c = cand_rows.get(m) or {}
            out += [c.get("name", "")] + [a for a in (c.get("aliases") or "").split(" | ") if a]
        return [n for n in dict.fromkeys(out) if n]
    # later runs for the same candidate (rescue, recent-deal pass) add to the earlier record field by field;
    # a non-empty later value wins, an empty one never erases (the recent-deal pass only returns investments)
    latest: dict[str, dict] = {}
    for r in records:
        merged = latest.setdefault(r["candidate_id"], {})
        merged.update({k: v for k, v in r.items() if v not in (None, "", [], {})})
    records = list(latest.values())
    primary_of = merge_duplicates(records, claims_by_cand)
    members: dict[str, list[str]] = defaultdict(list)
    for cid, p in primary_of.items():
        members[p].append(cid)

    rows = []
    for rec in records:
        cid = rec["candidate_id"]
        primary = primary_of[cid]
        if primary != cid:  # E8: decided once, on the merged evidence of the primary record
            d = Decision(cid, "REJECTED", "E8", "", f"duplicate of {primary} - evidence merged there", [], "", 0, 0, "")
            rows.append(wide_row(rec, d, None, [], as_of, names.get(cid) or ""))
            continue
        claims = [c for m in members[cid] for c in claims_by_cand.get(m, [])]
        web_name = domain(rec.get("website")).rsplit(".", 1)[0].replace(".", " ").replace("-", " ")  # zaka.vc -> "zaka"
        web_name = f"{web_name} {domain(rec.get('website')).rsplit('.', 1)[-1]}" if web_name else ""  # -> "zaka vc"
        reg = registry_for(claims, triage.get(cid), all_names(members[cid]) + ([web_name] if web_name else []))
        d = decide(cid, claims, reg, as_of)
        if d.reason == "E7" and rec.get("early_exit") == "foreign_hq":
            # the agent stopped because the firm is foreign but could not quote the address: out of scope, not "name only"
            d = Decision(**{**asdict(d), "status": "OOS", "reason": "OOS_HQ_UNVERIFIED",
                            "explanation": "agent reports a foreign HQ; no verified quote"})
        if len(members[cid]) > 1:
            d.explanation += f" [merged: {', '.join(sorted(m for m in members[cid] if m != cid))}]"
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
