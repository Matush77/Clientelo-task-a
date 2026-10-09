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
# gap filling (D41): only the fields the assignment names that are still empty after refinement
GAPFILL_DIR = ROOT / "data" / "raw" / "agents" / "gapfill"
CLAIMS_GAPFILL = PROCESSED / "claims_gapfill.csv"
GAP_FIELDS = {"sectors": "sectors", "stages": "stages", "ticket": "ticket_min_eur", "total_capital": "total_capital_eur"}
GAP_SK = {"sectors": "sektory", "stages": "štádiá", "ticket": "tiket", "total_capital": "celkový kapitál"}


def filled(row: dict, field: str) -> bool:
    """A required field has a value; a ticket stated only as a maximum ('up to EUR 15 million') counts too."""
    if field == "ticket":
        return bool(row.get("ticket_min_eur") or row.get("ticket_max_eur"))
    return bool(row.get(GAP_FIELDS[field]))


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
        if verdict == "corrected" and r and r["event_date"][:10] > chk["listed_date"][:10]:
            # a LATER date is a follow-on round, not a dispute of the listed one (an article date only ever comes
            # after the deal); the follow-on could not be verified, so the frozen claim stays as it was
            notes.append(f"{chk['company']}: novšie kolo ({r['event_date'][:7]}) sa nepodarilo overiť, pôvodný dátum ostáva")
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


def check_outputs() -> list[dict]:
    """Machine-check every refined claim (downloads the pages) -> claims_refined.csv."""
    investors = {r["candidate_id"]: r for r in _read(PROCESSED / "investors.csv")}
    cand = {c["candidate_id"]: c for c in _read(PROCESSED / "candidates.csv")}
    names = {cid: [n for m in inv["evidence_ids"].split() if m in cand
                   for n in [cand[m]["name"], *[a for a in cand[m]["aliases"].split(" | ") if a]]]
             for cid, inv in investors.items()}
    new = checked_claims(load_outputs(), investors, names)
    with CLAIMS_REFINED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(new[0].keys()) + ["verdict"])
        w.writeheader()
        for c in new:
            w.writerow({**c, "verdict": _value(c).get("verdict") or (_value(c).get("status") or "")})
    return new


def _codes(c: dict) -> list[str]:
    v = json.loads(c["value"]) if c.get("value") else None
    return [v] if isinstance(v, str) else [x for x in (v or []) if isinstance(x, str)]


def complete_gaps(row: dict, merged: list[dict], gap_claims: list[dict], not_public: list[str]) -> None:
    """Gap-fill claims (D41) on top of the rebuilt row: sectors and stages may come as one claim per inferred value,
    so the row lists all of them; every row says whether its sectors/stages are stated or inferred, and which
    required fields were searched for but are not public."""
    added = []
    for field in ("sectors", "stages"):
        claims = [c for c in merged if c["field"] == field and c["auto_check"] == "ok"]
        if any(c in gap_claims for c in claims):
            row[field] = ",".join(dict.fromkeys(code for c in claims for code in _codes(c)))
        row[f"{field}_basis"] = ("stated" if any(c.get("derivation") == "stated" for c in claims)
                                 else "inferred" if claims else "")
    for field in GAP_FIELDS:
        if any(c["field"] == field or (field == "total_capital" and c["field"] == "funds") for c in gap_claims) \
                and filled(row, field):
            inferred = field in ("sectors", "stages") and row[f"{field}_basis"] == "inferred"
            added.append(GAP_SK[field] + (" (odvodené z portfólia)" if inferred else ""))
    if added:
        row["refine_notes"] = "; ".join(n for n in [row["refine_notes"], "doplnené: " + ", ".join(added)] if n)
    row["not_public"] = "; ".join(f for f in dict.fromkeys(not_public) if f in GAP_FIELDS and not filled(row, f))


def load_gapfill() -> list[dict]:
    out = []
    for path in sorted(GAPFILL_DIR.glob("gf_b*.json")):
        out += json.loads(path.read_text(encoding="utf-8"))
    return out


def make_gapfill_batches(result: dict) -> list[Path]:
    """Investors whose required fields are still empty after refinement, with what the database already knows."""
    records = []
    for cid in sorted(result["rows"]):
        row = result["rows"][cid]
        missing = [f for f in GAP_FIELDS if not filled(row, f)]
        if not missing:
            continue
        ok = [c for c in result["merged"][cid] if c["auto_check"] == "ok"]
        companies = sorted({str(_value(c).get("company") or "").strip() for c in ok if c["field"] == "investments"} - {""})
        funds = [{"name": v.get("name"), "size": v.get("size"), "status": v.get("status")}
                 for c in ok if c["field"] == "funds" for v in [_value(c)]]
        records.append({"candidate_id": cid, "name": row["name"], "website": row["website"] or None, "missing": missing,
                        "known_sectors": [x for x in row["sectors"].split(",") if x],
                        "known_stages": [x for x in row["stages"].split(",") if x],
                        "portfolio_companies": companies[:20], "known_funds": funds})
    (GAPFILL_DIR / "batches").mkdir(parents=True, exist_ok=True)
    paths = []
    for n, start in enumerate(range(0, len(records), BATCH_SIZE), 1):
        path = GAPFILL_DIR / "batches" / f"gf_b{n:02d}.json"
        path.write_text(json.dumps(records[start:start + BATCH_SIZE], ensure_ascii=False, indent=2), encoding="utf-8")
        paths.append(path)
    return paths


def check_gapfill() -> list[dict]:
    """Machine-check every gap-fill claim (downloads the pages) -> claims_gapfill.csv."""
    investors = {r["candidate_id"]: r for r in _read(PROCESSED / "investors.csv")}
    cand = {c["candidate_id"]: c for c in _read(PROCESSED / "candidates.csv")}
    names = {cid: [n for m in inv["evidence_ids"].split() if m in cand
                   for n in [cand[m]["name"], *[a for a in cand[m]["aliases"].split(" | ") if a]]]
             for cid, inv in investors.items()}
    rows = []
    for rec in load_gapfill():
        cid, web = rec["candidate_id"], investors[rec["candidate_id"]]["website"]
        for field in ("sectors", "stages"):
            for i, claim in enumerate(rec.get(field) or []):
                for r in flatten({"candidate_id": cid, "website": web, field: claim}):
                    r.idx = i
                    rows.append(r)
        for field in ("ticket", "total_capital"):
            if rec.get(field):
                rows += flatten({"candidate_id": cid, "website": web, field: rec[field]})
        rows += flatten({"candidate_id": cid, "website": web, "funds": rec.get("funds") or []})
    check(rows, names)
    out = [asdict(r) for r in rows]
    with CLAIMS_GAPFILL.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    return out


def rebuild_all(as_of: date) -> dict:
    """Frozen claims + claims_refined.csv + the agents' verdicts -> investors_refined.csv (no downloads)."""
    investors = {r["candidate_id"]: r for r in _read(PROCESSED / "investors.csv")}
    outputs = {r["candidate_id"]: r for r in load_outputs()}
    new = _read(CLAIMS_REFINED) if CLAIMS_REFINED.exists() else []
    checks = {cid: deal_checks(rec) for cid, rec in outputs.items()}
    old = claims_by_investor(list(investors.values()), _read(PROCESSED / "claims.csv"), only_ok=False)

    gapfill = defaultdict(list)
    for c in (_read(CLAIMS_GAPFILL) if CLAIMS_GAPFILL.exists() else []):
        gapfill[c["candidate_id"]].append(c)
    not_public = {r["candidate_id"]: [n.get("field") for n in r.get("not_public") or []] for r in load_gapfill()}

    rows, problems, merged_by = [], [], {}
    for cid, inv in investors.items():
        mine = [c for c in new if c["candidate_id"] == cid]
        merged, notes = merge(old[cid], mine, checks.get(cid, [])) if cid in outputs else (old[cid], ["nespracované"])
        filled = [c for c in gapfill.get(cid, []) if c["auto_check"] == "ok"]
        merged = merged + filled
        row = rebuild(inv, merged, notes, as_of)
        complete_gaps(row, merged, filled, not_public.get(cid, []))
        rows.append(row)
        merged_by[cid] = merged
        problems += integrity(row, merged)
    with INVESTORS_REFINED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["candidate_id"]))
    return {"before": investors, "rows": {r["candidate_id"]: r for r in rows}, "claims": new, "checks": checks,
            "merged": merged_by, "old": old, "problems": problems, "missing": sorted(set(investors) - set(outputs))}


def summary(result: dict) -> dict:
    """Counts for the before/after report."""
    claims, checks = result["claims"], result["checks"]
    return {
        "fund_status": Counter(_value(c).get("status") for c in claims if c["field"] == "funds"),
        "auto_check": Counter((c["field"], c["auto_check"]) for c in claims),
        "verdicts": Counter(chk["verdict"] for chks in checks.values() for chk in chks),
    }


# --- 4. blind fact-check of before vs. after (prompts/refine_judge_agent.md) ----------------------------

JUDGE_DIR = ROOT / "data" / "review" / "refine_judge"
JUDGE_SEED = 20261010
JUDGE_BATCH = 4


def _capital_item(row: dict, ok: list[dict], on: str) -> dict | None:
    from investordb.pipeline import total_capital
    cap = total_capital(ok, on)
    if cap["eur"] is None:
        return None
    # no fund status and the same date precision in both versions: only refined claims carry a status and day dates,
    # which would tell the fact-checker which version an item comes from (D39)
    basis = []
    for c in cap["counted"]:
        v = _value(c)
        label = v.get("name") or "AUM"
        amount = v.get("size") or v.get("amount") or ""
        basis.append({"fund": label, "amount": amount, "source_url": c["source_url"]})
    return {"type": "capital", "total_eur": round(cap["eur"]), "basis": basis,
            "key": (round(cap["eur"]), tuple(sorted(b["source_url"] + b["amount"] for b in basis)))}


def _deal_items(ok: list[dict]) -> list[dict]:
    out = []
    for key, c in counted_deals(ok).items():
        shown = c["event_date"][:4] if c.get("event_date_precision") == "year" else c["event_date"][:7]
        out.append({"type": "deal", "company": _value(c).get("company"), "date": shown, "source_url": c["source_url"],
                    "key": (key, shown, c["source_url"])})
    return out


def make_judge_batches(result: dict, as_of: date) -> list[Path]:
    """Items from both versions, de-duplicated and shuffled; which version an item came from goes to key.csv only."""
    import random
    rng = random.Random(JUDGE_SEED)
    on = as_of.isoformat()
    records, key_rows = [], []
    n = 0
    for cid in sorted(result["before"]):
        before_ok = [c for c in result["old"][cid] if c["auto_check"] == "ok"]
        after_ok = [c for c in result["merged"][cid] if c["auto_check"] == "ok"]
        inv = result["before"][cid]
        items: dict[tuple, dict] = {}
        for version, ok in (("before", before_ok), ("after", after_ok)):
            found = _deal_items(ok)
            cap = _capital_item(inv, ok, on)
            for it in found + ([cap] if cap else []):
                k = (it["type"],) + it.pop("key")
                items.setdefault(k, {**it, "versions": set()})["versions"].add(version)
        listed = list(items.values())
        rng.shuffle(listed)
        out_items = [{"item_id": f"{cid}-I00", "type": "identity", "legal_name": inv["legal_name"],
                      "company_id": inv["company_id"], "registry_url": inv["registry_url"]}]
        key_rows.append({"item_id": f"{cid}-I00", "candidate_id": cid, "type": "identity", "before": 1, "after": 1})
        for it in listed:
            n += 1
            item_id = f"{cid}-I{len(out_items):02d}"
            versions = it.pop("versions")
            out_items.append({"item_id": item_id, **it})
            key_rows.append({"item_id": item_id, "candidate_id": cid, "type": it["type"],
                             "before": int("before" in versions), "after": int("after" in versions)})
        records.append({"investor": inv["name"], "website": inv["website"], "items": out_items})
    JUDGE_DIR.mkdir(parents=True, exist_ok=True)
    (JUDGE_DIR / "batches").mkdir(exist_ok=True)
    with (JUDGE_DIR / "key.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(key_rows[0].keys()))
        w.writeheader()
        w.writerows(key_rows)
    paths = []
    for b, start in enumerate(range(0, len(records), JUDGE_BATCH), 1):
        path = JUDGE_DIR / "batches" / f"j_b{b:02d}.json"
        path.write_text(json.dumps(records[start:start + JUDGE_BATCH], ensure_ascii=False, indent=2), encoding="utf-8")
        paths.append(path)
    return paths


def judge_metrics() -> dict:
    """Accuracy of the frozen vs. the refined values, from the blind fact-check (strict: cannot_tell = not confirmed)."""
    key = {r["item_id"]: r for r in _read(JUDGE_DIR / "key.csv")}
    answers = {}
    for path in sorted(JUDGE_DIR.glob("j_b*.json")):
        for a in json.loads(path.read_text(encoding="utf-8")):
            answers[a["item_id"]] = a
    out: dict = {"answered": len(answers), "items": len(key)}
    for typ in ("capital", "deal", "identity"):
        for version in ("before", "after"):
            ids = [i for i, k in key.items() if k["type"] == typ and k[version] == "1" and i in answers]
            got = Counter(answers[i]["answer"] for i in ids)
            out[(typ, version)] = {"n": len(ids), "yes": got.get("yes", 0), "answers": dict(got)}
    out["answers"] = answers
    out["key"] = key
    return out
