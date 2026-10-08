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


def main() -> None:
    parser = argparse.ArgumentParser(prog="investordb")
    sub = parser.add_subparsers(required=True)

    p = sub.add_parser("check-quotes", help="verify that quotes exist at their URLs")
    p.add_argument("input")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_check_quotes)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
