"""Parse money amounts as written in Czech/Slovak/English sources and convert them to EUR (ECB reference rates).

All arithmetic on amounts happens here, in code - the agents are not allowed to compute or convert numbers.
"""

from __future__ import annotations

import functools
import re
from dataclasses import dataclass

import httpx

ECB_URL = "https://data-api.ecb.europa.eu/service/data/EXR/D.{cur}.EUR.SP00.A"

SCALES = [  # longest first, matched right after the number
    (r"miliard\w*|mld\.?|billion|bn|b(?![a-z])", 1e9),
    (r"milion\w*|milión\w*|million\w*|mil\.?|mio\.?|mn|m(?![a-z])", 1e6),
    (r"tisíc\w*|tis\.?|thousand|k(?![a-z])", 1e3),
]
CURRENCIES = [
    (r"€|eur\w*|euro\w*", "EUR"),
    (r"\$|usd|dolar\w*|dolár\w*|dollar\w*", "USD"),
    (r"kč|czk|korun\w*", "CZK"),
    (r"£|gbp|libr\w*|pound\w*", "GBP"),
]
APPROX = re.compile(r"bezmála|takmer|téměř|almost|nearly|about|around|přibližně|približne|cca|~|over|více než|viac ako|přes|vyše", re.I)
NUMBER = re.compile(r"\d{1,3}(?:[  .,]\d{3})+(?:[.,]\d+)?(?!\d)|\d+(?:[.,]\d+)?")


@dataclass
class Money:
    amount: float
    currency: str
    approx: bool
    raw: str


def _to_float(raw: str) -> float:
    s = re.sub(r"[  ]", "", raw)
    s = re.sub(r"[.,](?=\d{3}(?:[.,]|$))", "", s)  # thousands separators
    return float(s.replace(",", "."))


def parse_money(text: str | None, currency_hint: str | None = None) -> Money | None:
    """'bezmála 100 milionů eur' -> Money(100e6, 'EUR', approx=True). None if no amount or no currency."""
    if not text:
        return None
    low = text.lower()
    m = NUMBER.search(low)
    if not m:
        return None
    amount = _to_float(m.group())
    rest = low[m.end():].lstrip()
    for pattern, factor in SCALES:
        if re.match(pattern, rest):
            amount *= factor
            break
    currency = next((code for pattern, code in CURRENCIES if re.search(pattern, low)), None)
    currency = currency or (currency_hint.upper() if currency_hint and currency_hint.lower() != "null" else None)
    if currency is None:
        return None
    return Money(amount, currency, bool(APPROX.search(low)), text)


@functools.lru_cache(maxsize=64)
def eur_rate(currency: str, on: str) -> float:
    """Units of `currency` per 1 EUR on (or last business day before) the date `on` (YYYY-MM-DD)."""
    if currency == "EUR":
        return 1.0
    resp = httpx.get(ECB_URL.format(cur=currency), params={"endPeriod": on, "lastNObservations": 1, "format": "csvdata"},
                     timeout=30)
    resp.raise_for_status()
    header, row = resp.text.splitlines()[:2]
    return float(dict(zip(header.split(","), row.split(",")))["OBS_VALUE"])


def to_eur(money: Money | None, on: str) -> float | None:
    return None if money is None else money.amount / eur_rate(money.currency, on)
