"""Fetch a source URL and turn it into plain text that quotes can be matched against.

Pages are cached in data/cache/ (gitignored: third-party content). Only the sha256 of the
extracted text is meant to be committed, as proof of what was seen and when.
"""

from __future__ import annotations

import hashlib
import io
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import httpx
import trafilatura
from pypdf import PdfReader

CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "cache"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36 investordb-research/0.1"
)
BLOCKED_STATUS = {401, 403, 429, 451, 503}
MIN_TEXT_CHARS = 200  # below this the page is most likely rendered by JavaScript


@dataclass
class FetchResult:
    url: str
    final_url: str | None
    status_code: int | None
    content_type: str | None
    text: str
    sha256: str | None
    fetched_at: str
    error: str | None = None

    @property
    def outcome(self) -> str:
        """ok | url_dead | blocked"""
        if self.error and self.status_code is None:
            return "url_dead"
        if self.status_code in BLOCKED_STATUS:
            return "blocked"
        if self.status_code is not None and self.status_code >= 400:
            return "url_dead"
        if len(self.text) < MIN_TEXT_CHARS:
            return "blocked"
        return "ok"


def _cache_path(url: str) -> Path:
    return CACHE_DIR / (hashlib.sha1(url.encode("utf-8")).hexdigest() + ".json")


def _pdf_to_text(content: bytes) -> str:
    reader = PdfReader(io.BytesIO(content))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def _html_to_text(html: str) -> str:
    # Main-content extraction drops navigation and tables' context; html2txt keeps everything.
    # Quotes can come from either, so both are kept.
    main = trafilatura.extract(html, include_tables=True, favor_recall=True) or ""
    full = trafilatura.html2txt(html) or ""
    return main + "\n\n" + full


WAYBACK_AVAILABLE = "https://archive.org/wayback/available"


def archived_snapshot_url(url: str, timeout: float = 30.0) -> str | None:
    """Closest existing Wayback Machine snapshot (read-only lookup; nothing is submitted)."""
    try:
        resp = httpx.get(WAYBACK_AVAILABLE, params={"url": url}, timeout=timeout)
        closest = resp.json().get("archived_snapshots", {}).get("closest") or {}
    except (httpx.HTTPError, ValueError):
        return None
    if not closest.get("available"):
        return None
    # "id_" returns the original page bytes without the Wayback toolbar
    return f"https://web.archive.org/web/{closest['timestamp']}id_/{url}"


def fetch_with_archive_fallback(url: str, use_cache: bool = True) -> FetchResult:
    """Live page first; if the site blocks us, the closest Wayback snapshot (final_url shows which)."""
    live = fetch(url, use_cache=use_cache)
    if live.outcome != "blocked":
        return live
    snapshot = archived_snapshot_url(url)
    if not snapshot:
        return live
    archived = fetch(snapshot, use_cache=use_cache)
    return archived if archived.outcome == "ok" else live


def fetch(url: str, use_cache: bool = True, timeout: float = 30.0) -> FetchResult:
    cache_file = _cache_path(url)
    if use_cache and cache_file.exists():
        return FetchResult(**json.loads(cache_file.read_text(encoding="utf-8")))

    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        resp = httpx.get(
            url,
            headers={"User-Agent": USER_AGENT, "Accept-Language": "sk,cs;q=0.9,en;q=0.8"},
            follow_redirects=True,
            timeout=timeout,
        )
    except httpx.HTTPError as exc:
        return FetchResult(url, None, None, None, "", None, fetched_at, error=f"{type(exc).__name__}: {exc}")

    content_type = resp.headers.get("content-type", "")
    text = ""
    error = None
    try:
        if "pdf" in content_type or resp.content[:5] == b"%PDF-":
            text = _pdf_to_text(resp.content)
        elif resp.status_code < 400:
            text = _html_to_text(resp.text)
    except Exception as exc:  # malformed PDF/HTML must not crash a batch run
        error = f"extract: {type(exc).__name__}: {exc}"

    result = FetchResult(
        url=url,
        final_url=str(resp.url),
        status_code=resp.status_code,
        content_type=content_type,
        text=text,
        sha256=hashlib.sha256(text.encode("utf-8")).hexdigest() if text else None,
        fetched_at=fetched_at,
        error=error,
    )
    if result.outcome == "ok":
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(asdict(result), ensure_ascii=False), encoding="utf-8")
    return result
