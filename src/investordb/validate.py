"""Deterministic (non-AI) checks of agent claims.

A claim is only kept when the quoted text really appears on the cited page and the claimed value
really appears in the quote. This is the main guard against hallucinated sources and numbers.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from rapidfuzz import fuzz

from investordb.fetch import FetchResult, fetch_with_archive_fallback

QUOTE_THRESHOLD = 90  # rapidfuzz partial_ratio, 0-100
TEXT_VALUE_THRESHOLD = 85

_TRANSLATE = str.maketrans(
    {
        "‘": "'", "’": "'", "‚": "'", "‛": "'",
        "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
        "–": "-", "—": "-", "−": "-",
        " ": " ", " ": " ", " ": " ",
        "­": None,  # soft hyphen
    }
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).translate(_TRANSLATE).lower()
    return re.sub(r"\s+", " ", text).strip()


def quote_score(quote: str, page_text: str) -> float:
    q, t = normalize(quote), normalize(page_text)
    if not q or not t:
        return 0.0
    if q in t:
        return 100.0
    return fuzz.partial_ratio(q, t)


# Either a number with 3-digit groups ("3,417", "3 417", "1.254,5") or a plain one ("39400", "1.25").
# Groups may be separated by a single space, but never by ", " - that is a list ("in 2022, 462 funds").
_NUMBER = re.compile(r"\d{1,3}(?:[ .,]\d{3})+(?:[.,]\d+)?(?!\d)|\d+(?:[.,]\d+)?")


def _canonical_number(raw: str) -> str:
    """'3,417' / '3 417' / '3.417' -> '3417'; '1.25' / '1,25' -> '1.25'."""
    s = re.sub(r"\s", "", raw)
    # A separator followed by exactly three digits (and then another separator or the end) groups
    # thousands; anything else is a decimal mark.
    s = re.sub(r"[.,](?=\d{3}(?:[.,]|$))", "", s)
    return s.replace(",", ".")


def numbers_in(text: str) -> set[str]:
    return {_canonical_number(m.group()) for m in _NUMBER.finditer(text)}


def value_in_quote(value: str, quote: str) -> bool:
    value = value.strip()
    if not value:
        return True
    value_numbers = numbers_in(value)
    if value_numbers:
        return value_numbers <= numbers_in(quote)
    return fuzz.partial_ratio(normalize(value), normalize(quote)) >= TEXT_VALUE_THRESHOLD


@dataclass
class ClaimCheck:
    status: str  # ok | url_dead | blocked | quote_not_found | value_not_in_quote
    quote_score: float | None
    http_status: int | None
    text_sha256: str | None
    fetched_at: str
    checked_url: str | None = None  # differs from the claim URL when a Wayback snapshot was used
    detail: str = ""


def check_claim(url: str, quote: str, value: str = "", page: FetchResult | None = None) -> ClaimCheck:
    page = page or fetch_with_archive_fallback(url)
    base = dict(
        http_status=page.status_code, text_sha256=page.sha256, fetched_at=page.fetched_at, checked_url=page.final_url
    )
    if page.outcome != "ok":
        return ClaimCheck(status=page.outcome, quote_score=None, detail=page.error or "", **base)
    score = quote_score(quote, page.text)
    if score < QUOTE_THRESHOLD:
        return ClaimCheck(status="quote_not_found", quote_score=score, **base)
    if not value_in_quote(value, quote):
        return ClaimCheck(status="value_not_in_quote", quote_score=score, detail=f"value={value!r}", **base)
    return ClaimCheck(status="ok", quote_score=score, **base)
