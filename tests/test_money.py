import pytest

from investordb.money import parse_money


@pytest.mark.parametrize(
    "text,hint,amount,currency,approx",
    [
        ("$88 million", None, 88e6, "USD", False),
        ("75 milionů eur", None, 75e6, "EUR", False),
        ("bezmála 100 milionů eur", None, 100e6, "EUR", True),
        ("53 milionů eur", None, 53e6, "EUR", False),
        ("$1M", None, 1e6, "USD", False),
        ("€500k", None, 500e3, "EUR", False),
        ("1,2 mld. Kč", None, 1.2e9, "CZK", False),
        ("EUR 25 mil.", None, 25e6, "EUR", False),
        ("200 000 EUR", None, 200e3, "EUR", False),
        ("€1.5M", None, 1.5e6, "EUR", False),
        ("2 miliardy korun", None, 2e9, "CZK", False),
        ("30 million", "EUR", 30e6, "EUR", False),  # currency only given separately in the claim
        ("viac ako 15 miliónov eur", None, 15e6, "EUR", True),
    ],
)
def test_parse_money(text, hint, amount, currency, approx):
    m = parse_money(text, hint)
    assert m is not None
    assert m.amount == pytest.approx(amount)
    assert (m.currency, m.approx) == (currency, approx)


def test_no_currency_no_amount():
    assert parse_money("30 million") is None
    assert parse_money("undisclosed", "EUR") is None
    assert parse_money(None) is None
