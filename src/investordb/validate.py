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


# Words that show a quote (or its surroundings on the page) is about an actual deal (EN / CZ / SK)
DEAL_WORDS = re.compile(
    # "invest" only as a verb or the act ("invested", "investment", "investuje", "investice") - never "investor":
    # "Miton, an investor in Boataround" (2026 article) describes a 2020 deal, it is not a 2026 deal
    r"rais(?:e|es|ed|ing)\b|\brounds?\b|\bseed\b|series [a-d]|invest(?:ed|s|ing|ment|ments)\b|investuj|investov|"
    r"investic|investíc|\bkol[aeouo]?\b|získal|získala|získali|"
    r"vybral|vybrala|vložil|vložila|poslal|vstoup|vstúp|\bled\b|\blead|particip|joined|backed|funding|financ|"
    r"welcome\w*\b.{0,60}portfolio|spája sily|spojil|připojil|pripojil|capital injection|stake|podíl|podiel|"
    r"navýšen|navýšil",
    re.I,
)
EXIT_WORDS = re.compile(
    r"\bexit|acquired by|acquisition|akvizic|odkoupil|odkúpil|prodal|predal|sold to|merger|\bipo\b|went public",
    re.I,
)
WINDOW = 250  # characters of page context on each side of the quote
# A sentence that lists EXISTING investors is a mention even inside an article about a new round:
# "Zu den Investoren der Firma gehören ... Miton" (2026 article, the Miton deal was in 2020)
INVESTOR_LIST = re.compile(  # investors OF THE COMPANY (existing shareholders) - not investors IN THIS ROUND
    r"zu den investoren\b|\b(?:its|existing|current|the company's)\s+investors\b|among \S+ investors\b|"
    r"among (?:its|the company's|the startup's) investors|"
    r"mezi (?:její|jeho|stávající|dosavadní)?\s*investory|mezi investory (?:firmy|společnosti|startupu)|"
    r"medzi (?:jej|jeho|existujúcich|doterajších)?\s*investormi|"
    r"investoři (?:firmy|společnosti|startupu)|investormi (?:firmy|spoločnosti|startupu)",
    re.I,
)


def deal_context(quote: str, page_text: str) -> str:
    """'exit'    - the quote describes an exit / acquisition, not an investment;
    'deal'    - the quote or its page context describes an actual deal (its date may count as the deal date);
    'mention' - the company is only named (portfolio list, overview article): investment yes, date not a deal date."""
    q = normalize(quote)
    if EXIT_WORDS.search(q) and not DEAL_WORDS.search(q):
        return "exit"
    if INVESTOR_LIST.search(q) and not re.search(r"\bnew investors?\b|nov[íý] investo", q):
        return "mention"
    if DEAL_WORDS.search(q):
        return "deal"
    t = normalize(page_text)
    pos = t.find(q)
    if pos < 0:
        alignment = fuzz.partial_ratio_alignment(q, t)
        pos = alignment.dest_start if alignment and alignment.score >= QUOTE_THRESHOLD else -1
    if pos >= 0 and DEAL_WORDS.search(t[max(0, pos - WINDOW): pos + len(q) + WINDOW]):
        return "deal"
    return "mention"


ATTRIBUTION_WINDOW = 400


def _plain(text: str) -> str:
    """Lowercase words only: 'J&T Ventures' -> 'j t ventures' (so names compare across punctuation)."""
    return re.sub(r"[^\w]+", " ", normalize(text)).strip()


GENERIC_TAIL = {"ventures", "venture", "capital", "investments", "investment", "partners", "fund", "funds", "vc", "gp",
                "management", "group", "holding", "invest", "sicav", "as", "sro", "s", "r", "o", "a", "se"}


def name_variants(names: list[str]) -> set[str]:
    """Full names plus their distinctive core ('Presto Ventures' -> 'presto', 'i&i Biotech Investments' -> 'i i biotech'),
    because articles write 'Presto Tech Horizons', 'i&i Biotech Fund', 'Zaka VC'. A core must be >= 4 characters or
    contain a digit ('gi21'), so short brands ('J&T', 'Jet') are only matched by their full name."""
    out = set()
    for n in names:
        full = _plain(n)
        if len(full) >= 3:
            out.add(full)
        tokens = full.split()
        while tokens and tokens[-1] in GENERIC_TAIL:
            tokens.pop()
        core = " ".join(tokens)
        if core and (len(core) >= 4 or any(ch.isdigit() for ch in core)):
            out.add(core)
    return out


def attributed(quote: str, page_text: str, names: list[str]) -> bool:
    """Is the candidate (any of its names) named in the quote or in the page text around it?
    An article that says 'Ranketta raised EUR 1m' proves a round, not that this candidate took part in it."""
    variants = name_variants(names)

    def named(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(v)}\b", text) for v in variants)
    q, t = _plain(quote), _plain(page_text)
    if named(q):
        return True
    pos = t.find(q)
    if pos < 0:
        alignment = fuzz.partial_ratio_alignment(q, t)
        pos = alignment.dest_start if alignment and alignment.score >= QUOTE_THRESHOLD else -1
    if pos < 0:
        return False
    return named(t[max(0, pos - ATTRIBUTION_WINDOW): pos + len(q) + ATTRIBUTION_WINDOW])


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
