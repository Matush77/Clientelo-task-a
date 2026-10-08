"""Merge discovery outputs (lists A, B and control sets) into one de-duplicated candidate table.

Also records, per candidate, whether it was found by list A and/or list B - the overlap feeds the
capture-recapture estimate of how many investors both lists missed.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

from rapidfuzz import fuzz

from investordb.registries import core_name

ROOT = Path(__file__).resolve().parents[2]
DISCOVERY_DIR = ROOT / "data" / "raw" / "agents" / "discovery"
SEEDS_DIR = ROOT / "data" / "seeds"
OUT = ROOT / "data" / "processed" / "candidates.csv"

# membership labels that sometimes leak into names ("Tilia Impact Ventures – Čestný člen")
NAME_NOISE = re.compile(r"\s+[–-]\s+(čestný člen|honorary member).*$", re.I)
GENERIC_TOKENS = {"management", "gp", "sarl", "sàrl", "scsp", "one", "i", "ii", "iii", "iv", "fund", "the", "vc"}


def match_key(name: str) -> str:
    tokens = [t for t in core_name(NAME_NOISE.sub("", name)).split() if t not in GENERIC_TOKENS]
    return " ".join(tokens)


def domain(url: str | None) -> str:
    if not url:
        return ""
    host = urlparse(url if "://" in url else "https://" + url).netloc.lower()
    return host.removeprefix("www.")


def same_entity(a: str, b: str) -> bool:
    if not a or not b:
        return False
    if a.replace(" ", "") == b.replace(" ", ""):  # "nation1" vs "nation 1"
        return True
    # The first token is the distinctive brand word; a typo-level difference there means a different firm
    # ("innova capital" vs "inovia capital", "j t ventures" vs "jet ventures").
    if a.split()[0] == b.split()[0] and fuzz.ratio(a, b) >= 90:
        return True
    short, long_ = sorted((a, b), key=len)
    # "depo ventures" vs "depo ventures one scsp": a multi-word name that prefixes the other
    return len(short.split()) >= 2 and long_.startswith(short + " ")


@dataclass
class Candidate:
    candidate_id: str
    names: list[str] = field(default_factory=list)
    websites: set[str] = field(default_factory=set)
    hq_claims: Counter = field(default_factory=Counter)
    type_claims: Counter = field(default_factory=Counter)
    lists: set[str] = field(default_factory=set)
    sources: list[str] = field(default_factory=list)
    control_category: str = ""
    company_id: str = ""

    @property
    def key(self) -> str:
        return match_key(self.names[0])

    @property
    def name(self) -> str:
        return min(self.names, key=len)  # shortest variant is usually the brand ("Credo Ventures a.s." -> brand)

    def matches(self, key: str, dom: str) -> bool:
        return same_entity(self.key, key) or bool(dom and dom in {domain(w) for w in self.websites})


def _rows() -> list[dict]:
    rows = []
    for path in sorted(DISCOVERY_DIR.glob("*.json")):
        for r in json.loads(path.read_text(encoding="utf-8")):
            lst = "control" if path.stem == "controls" else path.stem.split("_")[1].upper()  # list_a_cz -> A
            rows.append(dict(
                list=lst,
                name=r.get("name") or r.get("investor_name"),
                website=r.get("website"),
                hq=r.get("hq_country_claimed", "unknown"),
                type=r.get("investor_type_claimed") or r.get("control_category", ""),
                source=r.get("source_url", ""),
                control_category=r.get("control_category", ""),
                company_id="",
            ))
    name_only = SEEDS_DIR / "controls_name_only.csv"
    if name_only.exists():
        with name_only.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows.append(dict(list="control", name=r["name"], website=None, hq=r["country"], type="unknown",
                                 source=r["registry_url"], control_category="name_only", company_id=r["company_id"]))
    return rows


def build() -> list[Candidate]:
    candidates: list[Candidate] = []
    for r in _rows():
        key, dom = match_key(r["name"]), domain(r["website"])
        cand = next((c for c in candidates if c.matches(key, dom)), None)
        if cand is None:
            cand = Candidate(candidate_id=f"C{len(candidates) + 1:03d}")
            candidates.append(cand)
        cand.names.append(NAME_NOISE.sub("", r["name"]).strip())
        if r["website"]:
            cand.websites.add(r["website"])
        cand.hq_claims[r["hq"]] += 1
        cand.type_claims[r["type"]] += 1
        cand.lists.add(r["list"])
        cand.sources.append(r["source"])
        cand.control_category = cand.control_category or r["control_category"]
        cand.company_id = cand.company_id or r["company_id"]
    return candidates


def evidence_scope(c: Candidate) -> str:
    """Pre-evidence triage. Only obviously irrelevant rows are dropped here; everything else gets evidence."""
    known_hq = {h for h in c.hq_claims if h not in ("unknown", "")}
    if "control" in c.lists:
        return "evidence"
    if set(c.type_claims) == {"non_investor"}:
        return "skip:non_investor_member"  # law firms, auditors, banks listed as association associates
    if known_hq == {"other"}:
        return "skip:foreign_hq"
    return "evidence"


def write(candidates: list[Candidate], out: Path = OUT) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["candidate_id", "name", "aliases", "website", "hq_claimed", "type_claimed", "in_list_a",
                    "in_list_b", "control_category", "company_id", "scope", "n_mentions", "first_source"])
        for c in candidates:
            hq = [h for h, _ in c.hq_claims.most_common() if h != "unknown"]
            w.writerow([
                c.candidate_id, c.name, " | ".join(sorted(set(c.names) - {c.name})),
                sorted(c.websites)[0] if c.websites else "", hq[0] if hq else "unknown",
                ",".join(t for t, _ in c.type_claims.most_common()),
                int("A" in c.lists), int("B" in c.lists), c.control_category, c.company_id,
                evidence_scope(c), len(c.names), c.sources[0],
            ])
    return out


if __name__ == "__main__":
    cands = build()
    path = write(cands)
    scopes = Counter(evidence_scope(c) for c in cands)
    print(f"{len(cands)} candidates -> {path}\n{dict(scopes)}")
    ev = [c for c in cands if evidence_scope(c) == "evidence"]
    print("lists among evidence-scope:", dict(Counter("+".join(sorted(c.lists)) for c in ev)))
