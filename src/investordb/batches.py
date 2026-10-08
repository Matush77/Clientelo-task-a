"""Split evidence-scope candidates into random waves and batches of 5 for the evidence agents.

Each agent gets a batch file (candidate list) and reads the versioned prompt from prompts/evidence_agent.md
itself, so every agent works from exactly the instructions committed in git.
"""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path

from investordb.candidates import OUT as CANDIDATES_CSV
from investordb.triage import TRIAGE_CSV

ROOT = Path(__file__).resolve().parents[2]
BATCH_DIR = ROOT / "data" / "raw" / "agents" / "evidence" / "batches"
CALIBRATION_IDS = {"C002", "C012", "C206"}  # used to tune the prompt at CP2 -> excluded from waves and review
SEED = 20261009
BATCH_SIZE = 5


def _read(path: Path) -> dict[str, dict]:
    with path.open(encoding="utf-8") as f:
        return {r["candidate_id"]: r for r in csv.DictReader(f)}


def make_waves(wave1_size: int = 50) -> dict[str, list[Path]]:
    cands, triage = _read(CANDIDATES_CSV), _read(TRIAGE_CSV)
    ids = sorted(cid for cid, t in triage.items() if t["next_step"] == "evidence" and cid not in CALIBRATION_IDS)
    random.Random(SEED).shuffle(ids)
    waves = {"w1": ids[:wave1_size], "w2": ids[wave1_size:]}
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    out: dict[str, list[Path]] = {}
    for wave, wave_ids in waves.items():
        out[wave] = []
        for n, start in enumerate(range(0, len(wave_ids), BATCH_SIZE), 1):
            batch = []
            for cid in wave_ids[start:start + BATCH_SIZE]:
                c, t = cands[cid], triage[cid]
                batch.append({
                    "candidate_id": cid,
                    "name": c["name"],
                    "other_names": [a for a in c["aliases"].split(" | ") if a],
                    "known_website": c["website"] or None,
                    "registry_hint": (
                        f"possible registry match (unconfirmed, may be a different company): {t['legal_name']}, "
                        f"IČO {t['company_id']}" if t["company_id"] else None
                    ),
                })
            path = BATCH_DIR / f"{wave}_b{n:02d}.json"
            path.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
            out[wave].append(path)
    return out


def make_rescue(ids: list[str], prefix: str) -> list[Path]:
    """Re-run candidates whose rejection came from too little evidence (not from evidence against them)."""
    cands, triage = _read(CANDIDATES_CSV), _read(TRIAGE_CSV)
    paths = []
    for n, start in enumerate(range(0, len(ids), BATCH_SIZE), 1):
        batch = [{
            "candidate_id": cid, "name": cands[cid]["name"],
            "other_names": [a for a in cands[cid]["aliases"].split(" | ") if a],
            "known_website": cands[cid]["website"] or None,
            "registry_hint": None if not triage[cid]["company_id"] else
            f"possible registry match (unconfirmed, may be a different company): {triage[cid]['legal_name']}, IČO {triage[cid]['company_id']}",
        } for cid in ids[start:start + BATCH_SIZE]]
        path = BATCH_DIR / f"{prefix}_b{n:02d}.json"
        path.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding="utf-8")
        paths.append(path)
    return paths


if __name__ == "__main__":
    for wave, paths in make_waves().items():
        n = sum(len(json.loads(p.read_text(encoding="utf-8"))) for p in paths)
        print(f"{wave}: {len(paths)} batches, {n} candidates")
