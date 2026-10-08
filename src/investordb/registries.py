"""Company-registry lookups (tier T1): ARES for Czechia, RPO for Slovakia.

Both are free public APIs without a key. A registry proves that a legal entity exists and whether it is still
active - it does NOT prove that the entity invests (activity codes are unreliable: e.g. a real Slovak VC is
registered under 7020 "management consultancy").
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

import httpx

ARES = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty"
RPO = "https://api.statistics.sk/rpo/v1"
TIMEOUT = 30.0

LEGAL_SUFFIXES = re.compile(
    r"\b(s\.?\s?r\.?\s?o\.?|spol\.?\s?s\s?r\.?\s?o\.?|a\.?\s?s\.?|k\.?\s?s\.?|v\.?\s?o\.?\s?s\.?|se|sicav|"
    r"investi[čc]n[íý] fond|podfond|správ\.?\s?spol\.?|správcovská spoločnosť|investiční společnost|"
    r"gmbh|ltd|llc|b\.?v\.?|s\.?a\.?r\.?l\.?)\b",
    re.I,
)


@dataclass
class RegistryRecord:
    registry: str  # ARES | RPO
    company_id: str  # IČO
    name: str
    country: str  # CZ | SK
    address: str
    legal_form: str
    founded: str | None
    dissolved: str | None
    nace: list[str] = field(default_factory=list)
    source_url: str = ""  # API URL of this exact record, re-fetchable as proof

    @property
    def active(self) -> bool:
        return self.dissolved is None


def core_name(name: str) -> str:
    """'Credo Ventures Management II a.s.' -> 'credo ventures management ii' (for fuzzy matching)."""
    name = LEGAL_SUFFIXES.sub(" ", name.lower())
    return re.sub(r"[^\w]+", " ", name).strip()


# --- ARES (CZ) ---------------------------------------------------------------------------------------

def _ares_record(s: dict) -> RegistryRecord:
    ico = s["ico"]
    return RegistryRecord(
        registry="ARES",
        company_id=ico,
        name=s.get("obchodniJmeno", ""),
        country="CZ",
        address=(s.get("sidlo") or {}).get("textovaAdresa", ""),
        legal_form=s.get("pravniForma", ""),
        founded=s.get("datumVzniku"),
        dissolved=s.get("datumZaniku"),
        nace=s.get("czNace") or [],
        source_url=f"{ARES}/{ico}",
    )


def ares_get(ico: str) -> RegistryRecord | None:
    resp = httpx.get(f"{ARES}/{ico.strip()}", timeout=TIMEOUT)
    return _ares_record(resp.json()) if resp.status_code == 200 else None


def ares_search(name: str, limit: int = 10, offset: int = 0) -> tuple[int, list[RegistryRecord]]:
    """(total matches, records). ARES refuses queries with >1000 matches; the total is then parsed from the error."""
    resp = httpx.post(f"{ARES}/vyhledat", json={"obchodniJmeno": name, "pocet": limit, "start": offset}, timeout=TIMEOUT)
    data = resp.json()
    if resp.status_code != 200:
        match = re.search(r"\(([\d\s\xa0]+)\)", data.get("popis", ""))
        return (int(re.sub(r"\D", "", match.group(1))) if match else -1), []
    # a few records (foreign entities, organisational units) have no IČO and cannot be cited - skip them
    return data.get("pocetCelkem", 0), [_ares_record(s) for s in data.get("ekonomickeSubjekty", []) if s.get("ico")]


# --- RPO (SK) ----------------------------------------------------------------------------------------

def _current(items: list[dict] | None, key: str = "value"):
    """RPO keeps history; the current item is the one without validTo."""
    items = items or []
    current = [i for i in items if not i.get("validTo")] or items
    return current[0].get(key) if current else None


def _rpo_address(addresses: list[dict] | None) -> str:
    items = [a for a in addresses or [] if not a.get("validTo")] or addresses or []
    if not items:
        return ""
    a = items[0]
    street = " ".join(str(x) for x in (a.get("street"), a.get("buildingNumber")) if x)
    city = (a.get("municipality") or {}).get("value", "")
    return ", ".join(x for x in (street, city) if x)


def rpo_get(rpo_id: int | str) -> RegistryRecord | None:
    url = f"{RPO}/entity/{rpo_id}"
    resp = httpx.get(url, params={"showHistoricalData": "false"}, timeout=TIMEOUT)
    if resp.status_code != 200:
        return None
    d = resp.json()
    main = ((d.get("statisticalCodes") or {}).get("mainActivity") or {}).get("code")
    legal_form = _current(d.get("legalForms"))
    termination = d.get("termination")
    return RegistryRecord(
        registry="RPO",
        company_id=_current(d.get("identifiers")) or "",
        name=_current(d.get("fullNames")) or "",
        country="SK",
        address=_rpo_address(d.get("addresses")),
        legal_form=(legal_form or {}).get("value", "") if isinstance(legal_form, dict) else str(legal_form or ""),
        founded=d.get("establishment"),
        dissolved=termination if isinstance(termination, str) else (termination or {}).get("value") if termination else None,
        nace=[main] if main else [],
        source_url=url,
    )


def rpo_search(name: str = "", ico: str = "", limit: int = 10) -> list[RegistryRecord]:
    params = {"identifier": ico} if ico else {"fullName": name}
    resp = httpx.get(f"{RPO}/search", params=params, timeout=TIMEOUT)
    if resp.status_code != 200:
        return []
    ids = [r["id"] for r in resp.json().get("results", [])][:limit]
    return [rec for rec in (rpo_get(i) for i in ids) if rec]


# --- combined ----------------------------------------------------------------------------------------

def lookup(name: str = "", company_id: str = "", country: str = "") -> list[RegistryRecord]:
    """Exact lookup by IČO when known, otherwise name search in the registry of the given country (or both)."""
    out: list[RegistryRecord] = []
    if country in ("", "CZ"):
        if company_id:
            rec = ares_get(company_id)
            out += [rec] if rec else []
        elif name:
            out += ares_search(core_name(name) or name, limit=5)[1]
    if country in ("", "SK"):
        out += rpo_search(name=core_name(name) or name, ico=company_id, limit=5) if (name or company_id) else []
    return out
