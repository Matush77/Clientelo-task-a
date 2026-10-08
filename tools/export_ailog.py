"""Turn a Claude Code desktop session export (zip) into a redacted, readable ai-log entry.

    python tools/export_ailog.py <session-export.zip> [--out ai-log]

The desktop app's Export is the equivalent of the CLI `/export`, but it also contains every subagent
transcript. Output per session:

    ai-log/<date>_<session>/conversation.md          main conversation, readable
    ai-log/<date>_<session>/subagents/<agent>.md     one file per subagent (prompt + work + answer)
    ai-log/<date>_<session>/raw/...                  redacted JSONL transcripts (+ subagent meta)

Not copied: files the agents downloaded (third-party PDFs) and the app's internal state/config.
Terms to redact (e.g. the author's e-mail) are read from the gitignored file `.redact-terms`
(one per line), so they never appear in the public repo themselves. The script fails if any of them,
or anything that looks like an API key/token, survives in the output.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REDACT_FILE = ROOT / ".redact-terms"

SECRET_PATTERNS = [
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{10,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"),
]
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
SYSTEM_REMINDER = re.compile(r"<system-reminder[^>]*>.*?</system-reminder[^>]*>", re.S)
USER_FACING_TOOLS = {"AskUserQuestion", "ExitPlanMode"}  # their results carry the user's own answers


# --- redaction -----------------------------------------------------------------------------------

def load_terms(path: Path = REDACT_FILE) -> list[str]:
    if not path.exists():
        return []
    return [t.strip() for t in path.read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")]


def redact(text: str, terms: list[str]) -> str:
    for term in terms:
        text = re.sub(re.escape(term), "[REDACTED]", text, flags=re.I)
    for pattern in SECRET_PATTERNS:
        text = pattern.sub("[REDACTED_SECRET]", text)
    return text


def leaks(text: str, terms: list[str]) -> list[str]:
    found = [t for t in terms if t.lower() in text.lower()]
    found += [m.group() for p in SECRET_PATTERNS for m in p.finditer(text)]
    return found


# --- rendering -----------------------------------------------------------------------------------

def _clean_user_text(text: str) -> str:
    return SYSTEM_REMINDER.sub("", text).strip()


def _details(summary: str, body: str, limit: int) -> list[str]:
    if len(body) > limit:
        body = body[:limit] + f"\n… [skrátené, {len(body) - limit} znakov – plné znenie v raw/]"
    summary = summary.replace("<", "&lt;").replace(">", "&gt;")
    return ["<details><summary>" + summary + "</summary>", "", "````text", body, "````", "", "</details>", ""]


def _result_text(block: dict) -> str:
    content = block.get("content")
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if c.get("type") == "text")
    return str(content or "")


def _tool_summary(name: str, tool_input: dict) -> str:
    hint = tool_input.get("description") or tool_input.get("file_path") or tool_input.get("pattern") or ""
    return f"🔧 {name}" + (f" – {str(hint)[:120]}" if hint else "")


def render(lines: list[dict], title: str) -> str:
    out = [f"# {title}", ""]
    tool_names: dict[str, str] = {}
    for entry in lines:
        role = entry.get("type")
        if role not in ("user", "assistant"):
            continue
        ts = entry.get("timestamp", "")[:19].replace("T", " ")
        content = entry.get("message", {}).get("content")
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for block in content or []:
            kind = block.get("type")
            if kind == "text" and role == "user":
                text = _clean_user_text(block.get("text", ""))
                if text:
                    out += [f"## 👤 Používateľ · {ts}", "", text, ""]
            elif kind == "text":
                out += [f"### 🤖 Claude · {ts}", "", block.get("text", ""), ""]
            elif kind == "thinking" and block.get("thinking"):
                out += _details("💭 Úvaha modelu", block["thinking"], limit=6000)
            elif kind == "tool_use":
                tool_names[block.get("id", "")] = block.get("name", "")
                body = json.dumps(block.get("input", {}), ensure_ascii=False, indent=2)
                out += _details(_tool_summary(block.get("name", ""), block.get("input", {})), body, limit=4000)
            elif kind == "tool_result":
                text = _clean_user_text(_result_text(block))
                if tool_names.get(block.get("tool_use_id", "")) in USER_FACING_TOOLS:
                    out += [f"## 👤 Odpoveď používateľa · {ts}", "", text, ""]
                else:
                    out += _details("↳ výsledok nástroja", text, limit=3000)
    return "\n".join(out)


# --- export --------------------------------------------------------------------------------------

def _jsonl(raw: str) -> list[dict]:
    return [json.loads(line) for line in raw.splitlines() if line.strip()]


def export(zip_path: Path, out_root: Path, terms: list[str]) -> Path:
    z = zipfile.ZipFile(zip_path)
    main_raw = redact(z.read("transcript.jsonl").decode("utf-8"), terms)
    main = _jsonl(main_raw)
    session = next(e["sessionId"] for e in main if e.get("sessionId"))
    date = next(e["timestamp"][:10] for e in main if e.get("timestamp"))
    target = out_root / f"{date}_{session[:8]}"
    if target.exists():
        shutil.rmtree(target)  # a later export of the same session supersedes the earlier one
    (target / "raw" / "subagents").mkdir(parents=True)
    (target / "subagents").mkdir()

    (target / "raw" / "transcript.jsonl").write_text(main_raw, encoding="utf-8")
    (target / "conversation.md").write_text(render(main, f"Konverzácia – session {session[:8]} ({date})"), encoding="utf-8")

    for name in sorted(n for n in z.namelist() if re.search(r"/subagents/agent-[^/]+\.jsonl$", n)):
        agent = Path(name).stem
        raw = redact(z.read(name).decode("utf-8"), terms)
        meta_name = name[: -len(".jsonl")] + ".meta.json"
        meta = json.loads(z.read(meta_name)) if meta_name in z.namelist() else {}
        (target / "raw" / "subagents" / f"{agent}.jsonl").write_text(raw, encoding="utf-8")
        if meta:
            (target / "raw" / "subagents" / f"{agent}.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        title = f"Subagent: {meta.get('description', agent)} ({meta.get('agentType', '?')}, model: {meta.get('model', '?')})"
        (target / "subagents" / f"{agent}.md").write_text(render(_jsonl(raw), title), encoding="utf-8")

    problems, emails = [], set()
    for f in target.rglob("*"):
        if f.is_file():
            text = f.read_text(encoding="utf-8")
            problems += [f"{f.relative_to(target)}: {hit[:12]}…" for hit in leaks(text, terms)]
            emails |= set(EMAIL.findall(text))
    if problems:
        shutil.rmtree(target)
        sys.exit("Redaction check FAILED, nothing written:\n  " + "\n  ".join(problems))
    if emails:
        print("Other e-mail addresses left in the log (review that they are public/business ones):")
        for e in sorted(emails):
            print("  ", e)
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("zip", type=Path)
    parser.add_argument("--out", type=Path, default=ROOT / "ai-log")
    args = parser.parse_args()
    terms = load_terms()
    if not terms:
        sys.exit(f"No redaction terms found in {REDACT_FILE} - refusing to export without them.")
    target = export(args.zip, args.out, terms)
    print(f"ai-log written to {target}")


if __name__ == "__main__":
    main()
