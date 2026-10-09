"""Replace names of natural persons in AI review outputs with "[osoba]" (decision D14: no private individuals in the
published data). The names come from the gitignored file `.redact-people` (one per line, trailing * = any ending).

    python tools/redact_people.py data/review/sonnet data/raw/agents/verifier

Verbatim source quotes in data/processed/claims.csv are deliberately NOT touched: they must stay identical to the
public page to remain verifiable.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES_FILE = ROOT / ".redact-people"


def patterns(path: Path = NAMES_FILE) -> list[re.Pattern]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        body = re.escape(line[:-1]) + r"\w*" if line.endswith("*") else re.escape(line)
        out.append(re.compile(rf"\b{body}\b"))
    # longest first, so "Samuel Zalesak" is replaced before "Zalesak*"
    return sorted(out, key=lambda p: -len(p.pattern))


def redact_text(text: str, pats: list[re.Pattern]) -> tuple[str, int]:
    n = 0
    for p in pats:
        text, k = p.subn("[osoba]", text)
        n += k
    return text, n


def redact_value(value, pats):
    if isinstance(value, str):
        return redact_text(value, pats)
    if isinstance(value, list):
        total, out = 0, []
        for v in value:
            v2, k = redact_value(v, pats)
            out.append(v2)
            total += k
        return out, total
    if isinstance(value, dict):
        total, out = 0, {}
        for key, v in value.items():
            v2, k = redact_value(v, pats)
            out[key] = v2
            total += k
        return out, total
    return value, 0


def main(folders: list[str]) -> None:
    pats = patterns()
    if not pats:
        sys.exit(f"No names in {NAMES_FILE}")
    for folder in folders:
        for path in sorted(Path(folder).rglob("*.json")):
            if "batches" in path.parts:
                continue
            data, n = redact_value(json.loads(path.read_text(encoding="utf-8")), pats)
            if n:
                path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
                print(f"{n:>3} replaced  {path}")


if __name__ == "__main__":
    main(sys.argv[1:])
