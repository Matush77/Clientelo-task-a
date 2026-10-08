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

from investordb.validate import check_claim

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
    quote_score: str = ""
    checked_url: str = ""
    text_sha256: str = ""
    fetched_at: str = ""


def flatten(record: dict) -> list[ClaimRow]:
    rows: list[ClaimRow] = []
    website = record.get("website")

    def add(field: str, idx: int, claim: dict) -> None:
        if not isinstance(claim, dict) or not claim.get("source_url"):
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


def check(rows: list[ClaimRow]) -> None:
    for r in rows:
        if r.source_tier == "T4":
            r.auto_check = "forbidden_source"
            continue
        result = check_claim(r.source_url, r.quote, r.value_text)
        r.auto_check = result.status
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
