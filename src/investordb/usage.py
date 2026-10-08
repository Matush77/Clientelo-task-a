"""Measured token usage of every subagent run, parsed from Claude Code's local transcripts.

This is the measured input of the cost estimate. Claude Code writes one JSONL line per content block, and every
line of the same message repeats that message's usage - so usage must be de-duplicated by message id (a naive sum
over-counts up to ~7x).

The logged usage is the snapshot from the *start* of each response: input and cache tokens are exact, but
output_tokens stays at a few tokens. Output is therefore also estimated from the length of the generated content
(~3.5 characters per token); the logged value is kept as a lower bound.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

CHARS_PER_TOKEN = 3.5
ROOT = Path(__file__).resolve().parents[2]
RUNS_CSV = ROOT / "data" / "raw" / "agents" / "runs.csv"
SESSIONS_DIR = Path.home() / ".claude" / "projects" / "C--Users-matus-Desktop-Interview-Project-Project-a"


def parse_transcript(lines: list[dict]) -> dict:
    usage_by_msg: dict[str, dict] = {}
    model_by_msg: dict[str, str] = {}
    tools: Counter = Counter()
    seen_tool_ids: set[str] = set()
    output_chars = 0
    stamps = [l["timestamp"] for l in lines if l.get("timestamp")]
    for line in lines:
        if line.get("type") != "assistant":
            continue
        msg = line.get("message") or {}
        mid = msg.get("id") or line.get("uuid")
        if msg.get("usage"):
            usage_by_msg[mid] = msg["usage"]  # last line of a message carries its final usage
            model_by_msg[mid] = msg.get("model", "")
        for block in msg.get("content") or []:
            kind = block.get("type")
            if kind == "tool_use" and block.get("id") not in seen_tool_ids:
                seen_tool_ids.add(block.get("id"))
                tools[block.get("name", "")] += 1
                output_chars += len(json.dumps(block.get("input", {}), ensure_ascii=False))
            elif kind == "text":
                output_chars += len(block.get("text", ""))
            elif kind == "thinking":
                output_chars += len(block.get("thinking", ""))

    def total(key: str) -> int:
        return sum(int(u.get(key) or 0) for u in usage_by_msg.values())

    cache = [u.get("cache_creation") or {} for u in usage_by_msg.values()]
    duration = 0.0
    if len(stamps) >= 2:
        t0, t1 = (datetime.fromisoformat(s.replace("Z", "+00:00")) for s in (min(stamps), max(stamps)))
        duration = (t1 - t0).total_seconds()
    return dict(
        model=Counter(model_by_msg.values()).most_common(1)[0][0] if model_by_msg else "",
        api_calls=len(usage_by_msg),
        input_tokens=total("input_tokens"),
        cache_write_5m_tokens=sum(int(c.get("ephemeral_5m_input_tokens") or 0) for c in cache),
        cache_write_1h_tokens=sum(int(c.get("ephemeral_1h_input_tokens") or 0) for c in cache),
        cache_read_tokens=total("cache_read_input_tokens"),
        output_tokens_logged=total("output_tokens"),
        output_tokens_est=max(total("output_tokens"), round(output_chars / CHARS_PER_TOKEN)),
        web_searches=tools["WebSearch"],
        web_fetches=tools["WebFetch"],
        tool_calls=sum(tools.values()),
        duration_s=round(duration),
    )


def collect(sessions_dir: Path = SESSIONS_DIR, out: Path = RUNS_CSV) -> list[dict]:
    rows = []
    for path in sorted(sessions_dir.glob("*/subagents/agent-*.jsonl")):
        meta_path = path.with_name(path.stem + ".meta.json")
        meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        lines = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
        rows.append(dict(session=path.parent.parent.name[:8], agent=path.stem, description=meta.get("description", ""),
                         agent_type=meta.get("agentType", ""), **parse_transcript(lines)))
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return rows


if __name__ == "__main__":
    for r in collect():
        print(f"{r['description'][:36]:<36} {r['model']:<18} out~{r['output_tokens_est']:>7} "
              f"cache_read={r['cache_read_tokens']:>9} searches={r['web_searches']:>3} fetches={r['web_fetches']:>3}")
