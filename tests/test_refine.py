"""Refinement stage (D38): fund status in total capital, and how refined claims replace frozen ones.
The fund cases are the capital errors the blind Sonnet review found in pilot v3."""

import json

import pytest

from investordb.pipeline import target_near, total_capital
from investordb.refine import counted_deals, merge

ON = "2026-10-09"


def fund(name, size, quote, status=None, status_date=None, value_text=None, known_as=None):
    value = {"name": name, "size": size, "currency": "EUR"}
    if status:
        value.update(status=status, status_date=status_date, known_as=known_as)
    return {"field": "funds", "auto_check": "ok", "source_url": "https://x.example", "value": json.dumps(value),
            "quote": quote, "value_text": value_text or size, "published_date": status_date or ""}


def deal(company, day, idx=0, context="deal", attributed="1", check="ok", verdict=None):
    value = {"company": company, "date": day}
    if verdict:
        value["verdict"] = verdict
    return {"field": "investments", "auto_check": check, "source_url": f"https://news.example/{company}",
            "value": json.dumps(value), "quote": f"{company} raised", "event_date": day, "deal_context": context,
            "attributed": attributed, "idx": idx}


@pytest.mark.parametrize("quote, amount, expected", [
    ("e15: contracts for EUR 27M of the targeted EUR 40M are signed", "EUR 27M", False),  # Purple Ventures
    ("e15: contracts for EUR 27M of the targeted EUR 40M are signed", "EUR 40M", True),
    ("With a target size of EUR 150 million, the fund will back tech companies", "EUR 150 million", True),  # Presto
    ("Nový fond by měl mít až 150 milionů eur", "150 milionů eur", True),
    ("Rockaway uzavřel fond ve výši bezmála 55 milionů eur", "55 milionů eur", False),
])
def test_target_near_reads_the_words_before_the_amount(quote, amount, expected):
    assert target_near(quote, amount) is expected


def test_first_close_counts_until_a_final_close_replaces_it():
    # ZAKA: first close EUR 10.5M (2024-07), the record had counted the EUR 15M target as a closed fund
    first = fund("ZAKA Fund I", "EUR 10.5M", "first closing of EUR 10.5M", "first_close", "2024-07-01")
    target = fund("ZAKA Fund I", "EUR 15M", "targeting EUR 15M", "target", "2024-07-01")
    cap = total_capital([first, target], ON)
    assert cap["eur"] == pytest.approx(10.5e6)
    assert any("prvé uzavretie" in n for n in cap["notes"])
    final = fund("ZAKA Fund I", "EUR 17M", "final close at EUR 17M", "final_close", "2025-09-01")
    assert total_capital([first, target, final], ON)["eur"] == pytest.approx(17e6)


def test_status_final_close_is_refused_when_the_quote_calls_the_amount_a_target():
    # Presto Tech Horizons: an agent mislabelling a target as closed must not reach total capital
    wrong = fund("Presto Tech Horizons", "EUR 150 million", "With a target size of EUR 150 million", "final_close",
                 "2025-01-01")
    cap = total_capital([wrong], ON)
    assert cap["eur"] is None and cap["targets"]


def test_older_funds_are_summed():
    # Tilia: only fund I (CZK 43M) was counted, fund II's EUR 26M first close was missing
    cap = total_capital([
        fund("Tilia Impact Ventures I", "EUR 1.7M", "fund of EUR 1.7M closed", "final_close", "2018-06-01"),
        fund("Tilia Impact Ventures II", "EUR 26M", "first close of EUR 26M", "first_close", "2024-05-01"),
    ], ON)
    assert cap["eur"] == pytest.approx(27.7e6)
    assert cap["method"] == "sum_of_2_closed_funds"


def test_merge_corrected_date_replaces_the_article_date():
    # Rockaway: Apaleo was dated by a 2025 fund-close article; the real round was announced in 2023
    old = [deal("Apaleo", "2025-05-16"), deal("Apptronik", "2026-02-10")]
    new = [deal("Apaleo", "2023-03-07", idx=0, verdict="corrected")]
    checks = [{"company": "Apaleo", "listed_date": "2025-05-16", "verdict": "corrected", "note": "", "idx": 0},
              {"company": "Apptronik", "listed_date": "2026-02-10", "verdict": "confirmed", "note": "", "idx": None}]
    merged, notes = merge(old, new, checks)
    dates = {k: c["event_date"] for k, c in counted_deals(merged).items()}
    assert dates == {"apaleo": "2023-03-07", "apptronik": "2026-02-10"}  # confirmed without own quote: frozen stays
    assert any("2025-05 -> 2023-03" in n for n in notes)


def test_merge_unconfirmed_date_stops_counting_but_keeps_the_portfolio_mention():
    old = [deal("Signi", "2023-11-27")]
    checks = [{"company": "Signi", "listed_date": "2023-11-27", "verdict": "not_found", "note": "", "idx": None}]
    merged, _ = merge(old, [], checks)
    assert counted_deals(merged) == {}
    assert merged[0]["deal_context"] == "mention" and merged[0]["attributed"] == "1"


def test_merge_not_this_investor_removes_the_deal():
    old = [deal("Xund", "2025-03-05")]
    checks = [{"company": "Xund", "listed_date": "2025-03-05", "verdict": "not_this_investor", "note": "", "idx": None}]
    merged, _ = merge(old, [], checks)
    assert merged[0]["attributed"] == "0"


def test_merge_unverified_refined_claim_is_not_used():
    old = [deal("NOLD", "2023-10-18")]
    new = [deal("NOLD", "2023-10-18", idx=0, check="quote_not_found", verdict="confirmed")]
    checks = [{"company": "NOLD", "listed_date": "2023-10-18", "verdict": "confirmed", "note": "", "idx": 0}]
    merged, _ = merge(old, new, checks)
    assert [c["event_date"] for c in counted_deals(merged).values()] == ["2023-10-18"]
    assert len(merged) == 1


def test_merge_refined_fund_supersedes_the_frozen_claim_about_the_same_fund():
    old = [fund("Purple Ventures 2", "EUR 40M", "fund of EUR 40M")]
    new = [fund("Purple Ventures II", "EUR 27M", "contracts for EUR 27M of the targeted EUR 40M are signed",
                "first_close", "2025-06-01", known_as="Purple Ventures 2")]
    merged, notes = merge(old, new, [])
    assert [json.loads(c["value"])["size"] for c in merged] == ["EUR 27M"]
    assert total_capital(merged, ON)["eur"] == pytest.approx(27e6)


def test_judge_items_are_deduplicated_and_carry_no_version(tmp_path, monkeypatch):
    from datetime import date

    import investordb.refine as refine
    monkeypatch.setattr(refine, "JUDGE_DIR", tmp_path)
    inv = {"name": "X Ventures", "website": "", "legal_name": "X a.s.", "company_id": "1", "registry_url": ""}
    same = deal("Alfa", "2025-03-10")
    old_only = deal("Beta", "2025-05-16")
    new_only = dict(deal("Beta", "2023-03-07"), event_date_precision="day")
    result = {"before": {"C1": inv}, "old": {"C1": [same, old_only]}, "merged": {"C1": [same, new_only]}}
    refine.make_judge_batches(result, date(2026, 10, 9))
    items = json.loads((tmp_path / "batches" / "j_b01.json").read_text(encoding="utf-8"))[0]["items"]
    deals = [i for i in items if i["type"] == "deal"]
    assert sorted((d["company"], d["date"]) for d in deals) == [("Alfa", "2025-03"), ("Beta", "2023-03"), ("Beta", "2025-05")]
    assert all(set(i) <= {"item_id", "type", "company", "date", "source_url", "legal_name", "company_id",
                          "registry_url"} for i in items)
    key = (tmp_path / "key.csv").read_text(encoding="utf-8")
    assert key.count(",deal,1,1") == 1 and key.count(",deal,1,0") == 1 and key.count(",deal,0,1") == 1
