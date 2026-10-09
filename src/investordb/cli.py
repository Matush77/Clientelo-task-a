"""Command-line entry point: python -m investordb.cli <command> ..."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from investordb.validate import check_claim


def cmd_check_quotes(args: argparse.Namespace) -> None:
    """Check every (url, quote, value) row of a CSV and write the result columns next to it."""
    src = Path(args.input)
    out = Path(args.output) if args.output else src.with_name(src.stem + "_checked.csv")
    with src.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        result = check_claim(row["url"], row["quote"], row.get("value", ""))
        row.update(
            check_status=result.status,
            quote_score=f"{result.quote_score:.0f}" if result.quote_score is not None else "",
            http_status=result.http_status or "",
            text_sha256=result.text_sha256 or "",
            fetched_at=result.fetched_at,
            checked_url=result.checked_url or "",
        )
        print(f"{result.status:<20} {row.get('id', '')}")

    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n{dict(Counter(r['check_status'] for r in rows))} -> {out}")


DISCOVERY_DIR = Path(__file__).resolve().parents[2] / "data" / "raw" / "agents" / "discovery"


def cmd_check_discovery(args: argparse.Namespace) -> None:
    """Machine-check every quote the discovery agents returned (does the quote, with the entity's name, exist?)."""
    import json

    out_rows = []
    for path in sorted(DISCOVERY_DIR.glob("*.json")):
        for i, row in enumerate(json.loads(path.read_text(encoding="utf-8"))):
            name = row.get("name") or row.get("investor_name") or ""
            # control quotes describe what the organisation does; they need not contain its name
            result = check_claim(row["source_url"], row["quote"], "" if path.stem == "controls" else name)
            out_rows.append(
                dict(file=path.stem, row=i, name=name, source_url=row["source_url"], check_status=result.status,
                     quote_score=f"{result.quote_score:.0f}" if result.quote_score is not None else "",
                     http_status=result.http_status or "", checked_url=result.checked_url or "")
            )
            print(f"{result.status:<20} {path.stem:<12} {name[:50]}")
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)
    by_file: dict[str, Counter] = {}
    for r in out_rows:
        by_file.setdefault(r["file"], Counter())[r["check_status"]] += 1
    for name, counts in by_file.items():
        print(f"{name:<12} {dict(counts)}")


def cmd_evidence(args: argparse.Namespace) -> None:
    """Flatten evidence-agent output into claims.csv and machine-check every claim."""
    from investordb.evidence import UNPARSED, build_claims

    rows = build_claims([Path(p) for p in args.files] or None)
    print(f"{len(rows)} claims: {dict(Counter(r.auto_check for r in rows))}")
    if UNPARSED:
        print(f"WARNING: {len(UNPARSED)} claims could not be parsed (no source_url): {UNPARSED[:10]}")
    for field, n in sorted(Counter((r.field, r.auto_check) for r in rows).items()):
        print(f"  {field[0]:<14} {field[1]:<20} {n}")


def cmd_decide(args: argparse.Namespace) -> None:
    """Apply the inclusion/exclusion rules and write investors / rejected / needs_review tables."""
    from datetime import date

    from investordb.pipeline import run

    rows = run(date.fromisoformat(args.as_of))
    for r in rows:
        print(f"{r['status']:<13} {r['reason']:<16} {r['tier']:<2} {r['candidate_id']} {r['name'][:40]:<40} {r['explanation']}")
    print(dict(Counter(r["status"] for r in rows)))


def cmd_check_db(args: argparse.Namespace) -> None:
    """Integrity checks promised in docs/PLAN.md before the freeze:
    1. every INCLUDED record has >= 1 verified, dated investment inside the 36-month window,
    2. every filled cell of investors.csv is backed by a verified claim in claims.csv."""
    import json
    from datetime import date

    from investordb.rules import ACTIVITY_MONTHS, months_before

    root = Path(__file__).resolve().parents[2] / "data" / "processed"
    with (root / "investors.csv").open(encoding="utf-8") as f:
        investors = list(csv.DictReader(f))
    with (root / "claims.csv").open(encoding="utf-8") as f:
        claims = [c for c in csv.DictReader(f) if c["auto_check"] == "ok"]
    # hq_country may also come from the registry record (T1) - its source is then the registry_url column
    cell_fields = {"investor_types": ["investor_type"], "sectors": ["sectors"],
                   "stages": ["stages"], "ticket_min": ["ticket"], "ticket_max": ["ticket"],
                   "total_capital_eur": ["total_capital", "funds"], "funds": ["funds"],
                   "last_investment": ["investments"]}
    problems = []
    for inv in investors:
        ids = set(inv["evidence_ids"].split())
        mine = [c for c in claims if c["candidate_id"] in ids]
        window = months_before(date.fromisoformat(inv["as_of"]), ACTIVITY_MONTHS).isoformat()
        if not any(c["field"] == "investments" and c["event_date"] >= window for c in mine):
            problems.append(f"{inv['candidate_id']}: no verified investment since {window}")
        for col, fields in cell_fields.items():
            if inv[col] and not any(c["field"] in fields for c in mine):
                problems.append(f"{inv['candidate_id']}: '{col}' has no verified claim")
        if inv["hq_country"] and not any(c["field"] == "hq_country" for c in mine) and not inv["registry_url"]:
            problems.append(f"{inv['candidate_id']}: hq without claim or registry record")
    print(f"{len(investors)} investors checked, {len(problems)} problems")
    for p in problems:
        print("  " + p)
    if problems:
        raise SystemExit(1)


def cmd_report(args: argparse.Namespace) -> None:
    """Compute the pre-registered metrics and write docs/PRECISION_REPORT.md."""
    from investordb.report import write

    print(write())


def cmd_sample(args: argparse.Namespace) -> None:
    """Draw the review sample, build the blind review form and the verifier batches."""
    from investordb.sample import build, make_verifier_batches

    print(build())
    for p in make_verifier_batches():
        print(p)


def main() -> None:
    parser = argparse.ArgumentParser(prog="investordb")
    sub = parser.add_subparsers(required=True)

    p = sub.add_parser("check-quotes", help="verify that quotes exist at their URLs")
    p.add_argument("input")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_check_quotes)

    p = sub.add_parser("check-discovery", help="verify quotes returned by discovery agents")
    p.add_argument("-o", "--output", default="data/processed/discovery_checks.csv")
    p.set_defaults(func=cmd_check_discovery)

    p = sub.add_parser("evidence", help="flatten + machine-check evidence-agent output into claims.csv")
    p.add_argument("files", nargs="*", help="evidence JSON files (default: all in data/raw/agents/evidence)")
    p.set_defaults(func=cmd_evidence)

    p = sub.add_parser("decide", help="apply rules, write investors/rejected/needs_review tables")
    p.add_argument("--as-of", default="2026-10-08", help="reference date for the 36-month activity window")
    p.set_defaults(func=cmd_decide)

    p = sub.add_parser("check-db", help="integrity checks on investors.csv against claims.csv")
    p.set_defaults(func=cmd_check_db)

    p = sub.add_parser("sample", help="draw the review sample + blind review form + verifier batches")
    p.set_defaults(func=cmd_sample)

    p = sub.add_parser("report", help="compute metrics and write docs/PRECISION_REPORT.md")
    p.set_defaults(func=cmd_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
