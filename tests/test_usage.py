from investordb.usage import parse_transcript


def line(mid, usage, content, ts):
    return {"type": "assistant", "timestamp": ts, "message": {"id": mid, "model": "claude-haiku-5-5", "usage": usage, "content": content}}


U1 = {"input_tokens": 10, "cache_read_input_tokens": 1000, "output_tokens": 50,
      "cache_creation": {"ephemeral_5m_input_tokens": 200, "ephemeral_1h_input_tokens": 0}}
U2 = {"input_tokens": 5, "cache_read_input_tokens": 3000, "output_tokens": 70,
      "cache_creation": {"ephemeral_5m_input_tokens": 0, "ephemeral_1h_input_tokens": 0}}


def test_usage_is_deduplicated_per_message():
    lines = [
        # message m1 is written as three lines (thinking, text, tool_use) - each repeats the same usage
        line("m1", U1, [{"type": "thinking", "thinking": "..."}], "2026-10-08T10:00:00Z"),
        line("m1", U1, [{"type": "text", "text": "..."}], "2026-10-08T10:00:01Z"),
        line("m1", U1, [{"type": "tool_use", "id": "t1", "name": "WebSearch"}], "2026-10-08T10:00:02Z"),
        {"type": "user", "timestamp": "2026-10-08T10:00:05Z", "message": {"content": []}},
        line("m2", U2, [{"type": "tool_use", "id": "t2", "name": "WebFetch"}], "2026-10-08T10:01:00Z"),
    ]
    r = parse_transcript(lines)
    assert r["api_calls"] == 2
    assert r["input_tokens"] == 15 and r["output_tokens_logged"] == 120 and r["cache_read_tokens"] == 4000
    assert r["output_tokens_est"] >= r["output_tokens_logged"]
    assert r["cache_write_5m_tokens"] == 200
    assert (r["web_searches"], r["web_fetches"], r["tool_calls"]) == (1, 1, 2)
    assert r["duration_s"] == 60
    assert r["model"] == "claude-haiku-5-5"
