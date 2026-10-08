import pytest

from investordb.fetch import FetchResult
from investordb.validate import _canonical_number, check_claim, quote_score, value_in_quote

PAGE = (
    "Navigation | About us\n"
    "There are an estimated 8,030 single family offices in the world today, up from 6,130 in 2019, "
    "a near third (31%) increase. Footer text. "
    + "Lorem ipsum dolor sit amet. " * 10  # real pages are longer than the JS-shell threshold
)


def page(text=PAGE, status=200):
    return FetchResult("https://x.test", "https://x.test", status, "text/html", text, "h", "2026-10-08T00:00:00+00:00")


def test_exact_quote_scores_100():
    assert quote_score("8,030 single family offices in the world", PAGE) == 100


def test_quote_survives_typographic_differences():
    # curly quotes, en dash, non-breaking space and case must not matter
    assert quote_score("There are an Estimated 8,030 single family offices", PAGE) == 100


def test_slightly_paraphrased_quote_is_fuzzy_match():
    assert quote_score("there are an estimated 8,030 single-family offices in the world today", PAGE) >= 90


def test_invented_quote_is_rejected():
    assert quote_score("There are 12,500 multi family offices managing $6 trillion", PAGE) < 90


@pytest.mark.parametrize(
    "raw,expected",
    [("3,417", "3417"), ("3 417", "3417"), ("3.417", "3417"), ("1.25", "1.25"), ("1,25", "1.25"), ("445,535", "445535"), ("2023", "2023")],
)
def test_canonical_number(raw, expected):
    assert _canonical_number(raw) == expected


def test_value_in_quote_numbers():
    assert value_in_quote("8030", PAGE)
    assert value_in_quote("8 030", PAGE)
    assert not value_in_quote("8300", PAGE)


def test_numbers_separated_by_comma_space_are_distinct():
    # regression: "December 2022, 462 EuVECA funds" was parsed as the single number 2022462
    assert value_in_quote("462", "As of December 2022, 462 EuVECA funds and 15 EuSEFs funds were registered")
    assert value_in_quote("3417", "the U.S. had 3,417 VC firms, which closed 13,608 deals")


def test_value_in_quote_text():
    assert value_in_quote("single family offices", PAGE)
    assert not value_in_quote("hedge funds", PAGE)


def test_footer_text_is_kept():
    # regression: trafilatura dropped <footer>, so correct imprint quotes (legal name, address) failed the check
    from investordb.fetch import _html_to_text

    html = ("<html><body><main><p>We invest in seed-stage startups.</p></main><footer><div>Jet Investment, a.s."
            "<br/>Pisárecká 271/13<br/>634 00 Brno</div><script>var x='hidden';</script></footer></body></html>")
    text = _html_to_text(html)
    assert quote_score("Jet Investment, a.s.", text) == 100
    assert quote_score("Pisárecká 271/13 634 00 Brno", text) == 100
    assert "hidden" not in text


def test_check_claim_statuses():
    assert check_claim("u", "8,030 single family offices", "8030", page=page()).status == "ok"
    assert check_claim("u", "8,030 single family offices", "9999", page=page()).status == "value_not_in_quote"
    assert check_claim("u", "we invest in biotech", "", page=page()).status == "quote_not_found"
    assert check_claim("u", "anything", "", page=page(status=403)).status == "blocked"
    assert check_claim("u", "anything", "", page=page(status=404)).status == "url_dead"
    assert check_claim("u", "anything", "", page=page(text="<div id=root></div>")).status == "blocked"
