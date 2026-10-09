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


@pytest.mark.parametrize(
    "text,amount,amount_max,currency",
    [
        # regressions from the pre-review audit (Reflex Capital showed "30 €")
        ("dvaadvacet milionů eur", 22e6, None, "EUR"),
        ("od 30 do 50 milionů eur", 30e6, 50e6, "EUR"),
        ("čtyřicet milionů eur", 40e6, None, "EUR"),
        ("€1-3M", 1e6, 3e6, "EUR"),
        ("30 až 50 mil. Kč", 30e6, 50e6, "CZK"),
        ("twenty-two million euros", 22e6, None, "EUR"),
    ],
)
def test_number_words_and_ranges(text, amount, amount_max, currency):
    m = parse_money(text)
    assert m.amount == pytest.approx(amount)
    assert (m.amount_max == pytest.approx(amount_max)) if amount_max else m.amount_max is None
    assert m.currency == currency


def test_no_currency_no_amount():
    assert parse_money("30 million") is None
    assert parse_money("undisclosed", "EUR") is None
    assert parse_money(None) is None


def test_eur_rate_uses_the_last_rate_published_before_the_as_of_day(monkeypatch):
    # on the freeze day itself the ECB rate appears only in the afternoon: asking for it made morning and evening runs
    # of the same as_of differ (24.403 vs 24.369 CZK/EUR on 2026-10-09)
    import investordb.money as money

    seen = {}

    class Resp:
        text = "KEY,OBS_VALUE\nEXR.D.CZK.EUR.SP00.A,24.403"

        def raise_for_status(self):
            pass

    def fake_get(url, params, timeout):
        seen.update(params)
        return Resp()

    monkeypatch.setattr(money.httpx, "get", fake_get)
    money.eur_rate.cache_clear()
    assert money.eur_rate("CZK", "2026-10-09") == 24.403
    assert seen["endPeriod"] == "2026-10-08"
    money.eur_rate.cache_clear()
