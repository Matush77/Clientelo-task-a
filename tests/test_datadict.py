"""The data dictionary must document every column of the delivered database."""

import csv
from pathlib import Path

from investordb.datadict import INVESTOR_COLUMNS, render

ROOT = Path(__file__).resolve().parents[1]


def test_every_column_of_the_final_database_is_documented():
    with (ROOT / "data" / "processed" / "investors_refined.csv").open(encoding="utf-8") as f:
        header = next(csv.reader(f))
    documented = {c for c, _, _ in INVESTOR_COLUMNS}
    assert set(header) - documented == set()
    assert documented - set(header) == set()


def test_data_md_is_up_to_date():
    assert (ROOT / "docs" / "DATA.md").read_text(encoding="utf-8") == render()
