"""Evidence-agent output -> one row per claim (claims.csv), each machine-checked against its source.

Every data point in the final database points back to a row here: value, URL, verbatim quote, dates, source tier
and the result of the automatic check.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urlparse

from investordb.fetch import fetch_with_archive_fallback
from investordb.validate import attributed, check_claim, deal_context

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_DIR = ROOT / "data" / "raw" / "agents" / "evidence"
CLAIMS_CSV = ROOT / "data" / "processed" / "claims.csv"

LIST_FIELDS = ("identity", "investments", "funds", "red_flags")
SINGLE_FIELDS = ("hq_country", "investor_type", "sectors", "stages", "ticket", "total_capital")

# T1: registries, regulators and official LP disclosures
T1_DOMAINS = (
    "ares.gov.cz", "justice.cz", "orsr.sk", "statistics.sk", "registeruz.sk", "cnb.cz", "nbs.sk",
    "esma.europa.eu", "gleif.org", "eif.org", "sih.sk", "nrb.cz", "nrinvesticni.cz", "fi-compass.eu",
)
# T4: aggregators and directories - discovery only, never evidence
T4_DOMAINS = (
    "dealroom.co", "crunchbase.com", "pitchbook.com", "tracxn.com", "cbinsights.com", "vestbee.com", "caplight.com",
    "seedtable.com", "nfx.com", "openvc.app", "linkedin.com", "wikipedia.org", "finstat.sk", "finstat.cz",
    "kurzy.cz", "firmy.cz", "zoominfo.com", "owler.com", "golden.com",
    # added in the pre-review audit (D30): startup databases and a registry mirror (funding-NEWS sites such as
    # thesaasnews.com stay T3 - they publish articles about specific rounds; attribution is checked instead, D31)
    "startbase.de", "trysignalbase.com", "podnikatel.cz",
)


def domain(url: str | None) -> str:
    if not url:
        return ""
    return urlparse(url if "://" in url else "https://" + url).netloc.lower().removeprefix("www.")


def _under(host: str, domains: tuple[str, ...]) -> bool:
    return any(host == d or host.endswith("." + d) for d in domains)


def source_tier(url: str, own_website: str | None) -> str:
    host, own = domain(url), domain(own_website)
    if _under(host, T1_DOMAINS):
        return "T1"
    if _under(host, T4_DOMAINS):
        return "T4"
    if own and (host == own or host.endswith("." + own) or own.endswith("." + host)):
        return "T2"
    return "T3"


_DATE = re.compile(r"^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?")


def parse_date(raw: str | None) -> tuple[str, str]:
    """'2025-07' -> ('2025-07-01', 'month'); returns ('', '') when missing or unparsable."""
    m = _DATE.match(str(raw or "").strip())
    if not m:
        return "", ""
    year, month, day = m.group(1), m.group(2), m.group(3)
    if day:
        return f"{year}-{int(month):02d}-{int(day):02d}", "day"
    if month:
        return f"{year}-{int(month):02d}-01", "month"
    return f"{year}-01-01", "year"


@dataclass
class ClaimRow:
    candidate_id: str
    field: str
    idx: int
    value: str  # JSON
    value_text: str
    source_url: str
    quote: str
    published_date: str
    derivation: str
    source_tier: str
    event_date: str  # investments: deal date (or publication date as fallback); others: publication date
    event_date_precision: str
    auto_check: str = ""
    deal_context: str = ""  # investments only: deal | mention | exit (validate.deal_context)
    attributed: str = ""  # investments only: 1 if the candidate is named in the quote / around it (or own site)
    quote_score: str = ""
    checked_url: str = ""
    text_sha256: str = ""
    fetched_at: str = ""


def normalize_claim(claim):
    """Agents wrote claims in two shapes: flat {value, source_url, quote, ...} (as specified) or nested
    {"claim": {source_url, quote, ...}, "value": ...} (one agent read the prompt's shorthand literally)."""
    if isinstance(claim, dict) and isinstance(claim.get("claim"), dict):
        return {**claim["claim"], **{k: v for k, v in claim.items() if k != "claim"}}
    return claim


UNPARSED: list[str] = []  # claims that had to be skipped - reported, never dropped silently


def flatten(record: dict) -> list[ClaimRow]:
    rows: list[ClaimRow] = []
    website = record.get("website")

    def add(field: str, idx: int, claim: dict) -> None:
        claim = normalize_claim(claim)
        if not isinstance(claim, dict) or not claim.get("source_url"):
            if field != "red_flags" and claim:  # "no investment found" red flags legitimately have no source
                UNPARSED.append(f"{record.get('candidate_id')}:{field}[{idx}]")
            return
        value = claim.get("value")
        raw_date = (value or {}).get("date") if field == "investments" and isinstance(value, dict) else None
        event_date, precision = parse_date(raw_date or claim.get("published_date"))
        rows.append(ClaimRow(
            candidate_id=record["candidate_id"], field=field, idx=idx,
            value=json.dumps(value, ensure_ascii=False), value_text=str(claim.get("value_text") or ""),
            source_url=claim["source_url"], quote=str(claim.get("quote") or ""),
            published_date=parse_date(claim.get("published_date"))[0], derivation=claim.get("derivation", ""),
            source_tier=source_tier(claim["source_url"], website), event_date=event_date,
            event_date_precision=precision,
        ))

    for field in LIST_FIELDS:
        for i, claim in enumerate(record.get(field) or []):
            add(field, i, claim)
    for field in SINGLE_FIELDS:
        add(field, 0, record.get(field))
    return rows


def candidate_names() -> dict[str, list[str]]:
    """Every name a candidate is known under (brand, aliases from discovery)."""
    path = ROOT / "data" / "processed" / "candidates.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        return {r["candidate_id"]: [r["name"]] + [a for a in r["aliases"].split(" | ") if a] for r in csv.DictReader(f)}


def check(rows: list[ClaimRow], extra_names: dict[str, list[str]] | None = None) -> None:
    names = candidate_names()
    for cid, more in (extra_names or {}).items():  # e.g. names of merged duplicates (refinement, D38)
        names.setdefault(cid, []).extend(more)
    # legal names the agents verified count as names too ("Biotech Investments, s. r. o.")
    for r in rows:
        if r.field == "identity":
            legal = (json.loads(r.value) or {}).get("legal_name") if r.value.startswith("{") else None
            if legal:
                names.setdefault(r.candidate_id, []).append(legal)
    for r in rows:
        if r.source_tier == "T4":
            r.auto_check = "forbidden_source"
            continue
        result = check_claim(r.source_url, r.quote, r.value_text)
        r.auto_check = result.status
        if r.field == "investments" and result.status == "ok":
            page = fetch_with_archive_fallback(r.source_url).text
            r.deal_context = deal_context(r.quote, page)
            # the candidate's own site implies attribution (its portfolio); elsewhere the name must be near the quote
            own = r.source_tier == "T2"
            r.attributed = "1" if own or attributed(r.quote, page, names.get(r.candidate_id, [])) else "0"
        r.quote_score = f"{result.quote_score:.0f}" if result.quote_score is not None else ""
        r.checked_url, r.text_sha256, r.fetched_at = result.checked_url or "", result.text_sha256 or "", result.fetched_at


def load_records(paths: list[Path] | None = None) -> list[dict]:
    records: list[dict] = []
    for path in paths or sorted(EVIDENCE_DIR.glob("*.json")):
        records += json.loads(path.read_text(encoding="utf-8"))
    return records


def build_claims(paths: list[Path] | None = None, out: Path = CLAIMS_CSV) -> list[ClaimRow]:
    rows = [row for rec in load_records(paths) for row in flatten(rec)]
    check(rows)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()))
        w.writeheader()
        w.writerows(asdict(r) for r in rows)
    return rows
