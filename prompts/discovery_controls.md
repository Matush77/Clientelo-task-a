# Discovery agent – control set ("lookalikes") – v1

Placeholders `{OUTPUT_PATH}`, `{TODAY}` are filled in by the orchestrator.

---

We are testing whether our pipeline can tell real venture-capital investors from entities that only **look** like
investors. Find **12–15 Czech or Slovak organisations** that a naive search for "investors" would return, but that
should **not** be in a database of VC investors into companies:

- 3 crowdfunding / crowdinvesting / P2P investment platforms (intermediaries, not investors themselves)
- 3 M&A / corporate-finance advisory boutiques or investment banks (advisors, not investors)
- 2 real-estate investment funds or real-estate investment companies
- 2 fund-of-funds or state programmes that only invest into other funds (LPs)
- 2 investment holdings / groups that buy companies only into their own group (strategic acquirers)
- optionally 1–3 other tricky cases (e.g. an accelerator without own capital, a grant agency)

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed). Budget: at most 30 tool
calls. Skip private individuals.

## Rules

1. Each row needs a public source (preferably the organisation's own website) and a verbatim quote (max 200 chars)
   that shows **what the organisation actually does**. The quote will be machine-checked against the page.
2. Never add organisations from memory without opening a source.

## Output file

Write a UTF-8 JSON array to `{OUTPUT_PATH}` (create the folder if needed) and nothing else into it. Row schema:

```json
{
  "name": "string",
  "website": "string or null",
  "hq_country_claimed": "CZ | SK",
  "control_category": "crowdfunding | advisory | real_estate | fund_of_funds | group_holding | other",
  "expected_rejection": "E3 | E4 | E5 | E6 | E9",
  "source_url": "string",
  "quote": "verbatim, max 200 chars",
  "accessed_date": "{TODAY}"
}
```

Then reply in at most 100 words: number of rows per category and anything surprising.
