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
        if not any(c["field"] == "investments" and c["event_date"] >= window and c.get("deal_context") == "deal"
                   for c in mine):
            problems.append(f"{inv['candidate_id']}: no verified, dated deal since {window}")
        if inv["total_capital_eur"] and float(inv["total_capital_eur"]) < 5e5:
            problems.append(f"{inv['candidate_id']}: implausible total capital {inv['total_capital_eur']} EUR")
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


def cmd_cost(args: argparse.Namespace) -> None:
    """Write docs/COST_ESTIMATE.md from the pilot's measured usage."""
    from investordb.cost import write

    print(write())


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


def cmd_spotcheck(args: argparse.Namespace) -> None:
    """Build the human spot-check form from the Sonnet review and the Haiku verifier (D34)."""
    from investordb.sample import build_spotcheck, build_spotcheck_refined

    print(build_spotcheck_refined() if args.refined else build_spotcheck())


def cmd_refine(args: argparse.Namespace) -> None:
    """Refinement stage (D38): batches -> (Sonnet agents) -> machine checks -> rebuilt rows -> blind fact-check."""
    from datetime import date

    from investordb import refine

    as_of = date.fromisoformat(args.as_of)
    if args.step == "batches":
        for p in refine.make_batches():
            print(p)
        return
    if args.step == "check":
        claims = refine.check_outputs()
        print(f"{len(claims)} refined claims checked -> {refine.CLAIMS_REFINED}")
    if args.step == "gapfill-check":
        claims = refine.check_gapfill()
        print(f"{len(claims)} gap-fill claims checked -> {refine.CLAIMS_GAPFILL}")
    result = refine.rebuild_all(as_of)
    print(f"{len(result['rows'])} investors rebuilt -> {refine.INVESTORS_REFINED}; missing output: {result['missing']}")
    for p in result["problems"]:
        print("  integrity: " + p)
    if args.step == "gapfill-batches":
        for p in refine.make_gapfill_batches(result):
            print(p)
    if args.step == "judge-batches":
        for p in refine.make_judge_batches(result, as_of):
            print(p)
    if args.step == "report":
        from investordb.refine_report import write

        print(write(result, as_of))


def cmd_explorer(args: argparse.Namespace) -> None:
    """Write docs/explorer.html - every included investor with the sources and quotes behind each value."""
    from datetime import date

    from investordb.explorer import write

    data = write(date.fromisoformat(args.as_of), {"precision": args.precision, "footer": args.footer},
                 artifact_out=Path(args.artifact) if args.artifact else None)
    print(f"{len(data['investors'])} investors -> docs/explorer.html")


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

    p = sub.add_parser("spotcheck", help="build the human spot-check form (Sonnet vs Haiku disagreements + random)")
    p.add_argument("--refined", action="store_true", help="the 5-record form with refined values (D40)")
    p.set_defaults(func=cmd_spotcheck)

    p = sub.add_parser("cost", help="write docs/COST_ESTIMATE.md from measured usage")
    p.set_defaults(func=cmd_cost)

    p = sub.add_parser("report", help="compute metrics and write docs/PRECISION_REPORT.md")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("refine", help="refinement D38/D41: batches | check | rebuild | judge-batches | gapfill-batches | "
                                      "gapfill-check | report")
    p.add_argument("step", choices=["batches", "check", "rebuild", "judge-batches", "gapfill-batches", "gapfill-check",
                                    "report"])
    p.add_argument("--as-of", default="2026-10-09")
    p.set_defaults(func=cmd_refine)

    p = sub.add_parser("explorer", help="write docs/explorer.html (interactive view of the included investors)")
    p.add_argument("--as-of", default="2026-10-09")
    p.add_argument("--precision", default="")
    p.add_argument("--footer", default="")
    p.add_argument("--artifact", default="", help="also write a version without the HTML skeleton to this path")
    p.set_defaults(func=cmd_explorer)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
