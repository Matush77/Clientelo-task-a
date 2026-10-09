"""Parse money amounts as written in Czech/Slovak/English sources and convert them to EUR (ECB reference rates).

All arithmetic on amounts happens here, in code - the agents are not allowed to compute or convert numbers.
"""

from __future__ import annotations

import functools
import re
from dataclasses import dataclass
from datetime import date, timedelta

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
APPROX = re.compile(r"bezmála|takmer|téměř|almost|nearly|about|around|přibližně|približne|cca|~|over|více než|viac ako|přes|vyše|kolem|okolo|zhruba", re.I)
NUMBER = re.compile(r"\d{1,3}(?:[  .,]\d{3})+(?:[.,]\d+)?(?!\d)|\d+(?:[.,]\d+)?")
# "30 - 50", "od 30 do 50", "30 až 50", "between 30 and 50", "1-3M"
RANGE_TAIL = re.compile(r"\s*(?:-|–|až|do|to|and|a)\s*(" + NUMBER.pattern + r")")

# Number words (CZ / SK / EN) - sources write "dvaadvacet milionů eur" (twenty-two million euros)
_UNITS = {
    # declined forms too: "kolem jednoho milionu eur", "dvou milionů", "troch miliónov"
    1: "jeden jedna jedno jednoho jedné jednomu jedním jedného jednej jedným one",
    2: "dva dvě dve dvou dvěma dvoch dvoma two", 3: "tři tri tří třemi troch tromi three",
    4: "čtyři štyri čtyř čtyřmi štyroch štyrmi four", 5: "pět päť pěti piatich five",
    6: "šest šesť six", 7: "sedm sedem seven", 8: "osm osem eight", 9: "devět deväť nine",
}
_TEENS = {
    10: "deset desať ten", 11: "jedenáct jedenásť eleven", 12: "dvanáct dvanásť twelve", 13: "třináct trinásť thirteen",
    14: "čtrnáct štrnásť fourteen", 15: "patnáct pätnásť fifteen", 16: "šestnáct šestnásť sixteen",
    17: "sedmnáct sedemnásť seventeen", 18: "osmnáct osemnásť eighteen", 19: "devatenáct devätnásť nineteen",
}
_TENS = {
    20: "dvacet dvadsať twenty", 30: "třicet tridsať thirty", 40: "čtyřicet štyridsať forty", 50: "padesát päťdesiat fifty",
    60: "šedesát šesťdesiat sixty", 70: "sedmdesát sedemdesiat seventy", 80: "osmdesát osemdesiat eighty",
    90: "devadesát deväťdesiat ninety",
}
_WORD_VALUE = {w: v for table in (_UNITS, _TEENS, _TENS) for v, words in table.items() for w in words.split()}
_WORD_VALUE.update({"sto": 100, "hundred": 100})
_TENS_WORDS = {w: v for v, words in _TENS.items() for w in words.split()}
_UNIT_WORDS = {w: v for v, words in _UNITS.items() for w in words.split()}


def _word_to_number(word: str) -> int | None:
    if word in _WORD_VALUE:
        return _WORD_VALUE[word]
    # Czech compounds "dvaadvacet" = dva-a-dvacet = 22; English "twenty-two"
    for sep in ("a", "-"):
        for unit, uv in _UNIT_WORDS.items():
            for ten, tv in _TENS_WORDS.items():
                if word in (f"{unit}{sep}{ten}", f"{ten}{sep}{unit}"):
                    return uv + tv
    return None


def words_to_digits(text: str) -> str:
    """'dvaadvacet milionů eur' -> '22 milionů eur'; 'dvacet dva' -> '22'."""
    def repl(m: re.Match) -> str:
        value = _word_to_number(m.group(0))
        return str(value) if value is not None else m.group(0)

    text = re.sub(r"[^\W\d_]+(?:-[^\W\d_]+)?", repl, text)
    return re.sub(r"\b([2-9]0) ([1-9])\b", lambda m: str(int(m.group(1)) + int(m.group(2))), text)  # "20 2" -> "22"


@dataclass
class Money:
    amount: float
    currency: str
    approx: bool
    raw: str
    amount_max: float | None = None  # set for ranges ("od 30 do 50 milionů eur")

    @property
    def is_range(self) -> bool:
        return self.amount_max is not None and self.amount_max != self.amount


def _to_float(raw: str) -> float:
    s = re.sub(r"[  ]", "", raw)
    s = re.sub(r"[.,](?=\d{3}(?:[.,]|$))", "", s)  # thousands separators
    return float(s.replace(",", "."))


def parse_money(text: str | None, currency_hint: str | None = None) -> Money | None:
    """'bezmála 100 milionů eur' -> Money(100e6, 'EUR', approx=True). None if no amount or no currency."""
    if not text:
        return None
    low = words_to_digits(text.lower())
    m = NUMBER.search(low)
    if not m:
        return None
    amount = _to_float(m.group())
    amount_max = None
    end = m.end()
    rng = RANGE_TAIL.match(low, end)
    if rng:
        amount_max = _to_float(rng.group(1))
        end = rng.end()
    # the scale word may follow the second number of a range: "od 30 do 50 milionů" -> both ends are millions
    rest = low[end:].lstrip()
    for pattern, factor in SCALES:
        if re.match(pattern, rest):
            amount *= factor
            amount_max = amount_max * factor if amount_max is not None else None
            break
    currency = next((code for pattern, code in CURRENCIES if re.search(pattern, low)), None)
    currency = currency or (currency_hint.upper() if currency_hint and currency_hint.lower() != "null" else None)
    if currency is None:
        return None
    return Money(amount, currency, bool(APPROX.search(low)), text, amount_max)


# A fund that is planned / being raised is not capital yet: "Aiming to raise €20 million", "cílová velikost 100 milionů",
# "by měl mít od 30 do 50 milionů", "chce investovat 10 milionů". ("má objem 40 milionů" - has a volume - is closed.)
TARGET_FUND = re.compile(
    r"aim(?:s|ing)?\b|target(?:ed|ing| size)?\b|plans? to raise|seek(?:s|ing)? to raise|hop(?:es|ing) to raise|"
    r"looking for investors|currently raising|cílov\w* velikost|cieľov\w* veľkos|by měl mít|by mal mať|"
    r"chce\b.{0,40}(?:získat|vybrat|investovat|uzavřít)|plánuje\b.{0,40}(?:získat|vybrat|fond)|má v plánu|"
    r"chce\b.{0,40}(?:získať|investovať)|plánuje\b.{0,40}(?:získať)",
    re.I,
)

# plausibility bounds in EUR - outside them a parsed amount is a parsing or extraction error, not data
BOUNDS_EUR = {"fund": (5e5, 2e10), "aum": (1e6, 5e11), "ticket": (5e3, 5e8)}


def plausible(kind: str, eur: float | None) -> bool:
    lo, hi = BOUNDS_EUR[kind]
    return eur is not None and lo <= eur <= hi


@functools.lru_cache(maxsize=64)
def eur_rate(currency: str, on: str) -> float:
    """Units of `currency` per 1 EUR: the last ECB reference rate published BEFORE the date `on` (YYYY-MM-DD).
    The rate of day `on` itself appears only in its afternoon, so using it would make a run on the freeze day give
    different numbers in the morning and in the evening."""
    if currency == "EUR":
        return 1.0
    end = (date.fromisoformat(on) - timedelta(days=1)).isoformat()
    resp = httpx.get(ECB_URL.format(cur=currency), params={"endPeriod": end, "lastNObservations": 1, "format": "csvdata"},
                     timeout=30)
    resp.raise_for_status()
    header, row = resp.text.splitlines()[:2]
    return float(dict(zip(header.split(","), row.split(",")))["OBS_VALUE"])


def to_eur(money: Money | None, on: str) -> float | None:
    return None if money is None else money.amount / eur_rate(money.currency, on)
