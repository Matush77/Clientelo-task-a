from tools.export_ailog import leaks, redact, render

TERMS = ["someone@example.org"]


def test_redact_terms_case_insensitive_and_secrets():
    text = "mail Someone@Example.org key sk-ant-api03-abcdefghijklmnop token ghp_abcdefghijklmnopqrstuvwxyz123"
    out = redact(text, TERMS)
    assert "example.org" not in out.lower()
    assert "sk-ant-" not in out and "ghp_" not in out
    assert leaks(out, TERMS) == []


def test_leaks_detects_unredacted_term():
    assert leaks("contact someone@example.org", TERMS) == ["someone@example.org"]


def test_render_hides_system_reminders_and_shows_user_answers():
    lines = [
        {"type": "user", "timestamp": "2026-10-08T10:00:00Z",
         "message": {"content": "<system-reminder>internal</system-reminder>Build the plan"}},
        {"type": "assistant", "timestamp": "2026-10-08T10:01:00Z",
         "message": {"content": [
             {"type": "text", "text": "Here is my question."},
             {"type": "tool_use", "id": "t1", "name": "AskUserQuestion", "input": {"questions": []}},
         ]}},
        {"type": "user", "timestamp": "2026-10-08T10:02:00Z",
         "message": {"content": [{"type": "tool_result", "tool_use_id": "t1", "content": "Pilot = CZ + SK"}]}},
        {"type": "attachment", "attachment": {"type": "environment"}},
    ]
    md = render(lines, "Test")
    assert "internal" not in md
    assert "Build the plan" in md
    assert "Odpoveď používateľa" in md and "Pilot = CZ + SK" in md
    assert "environment" not in md
