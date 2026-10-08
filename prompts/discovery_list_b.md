# Discovery agent – List B (deal news snowball) – v1

Placeholders `{COUNTRY}`, `{MEDIA}`, `{OUTPUT_PATH}`, `{TODAY}` are filled in by the orchestrator.

---

You build an **independent** list of investors that put money into startups / young companies from {COUNTRY}
between **2023-10-01 and {TODAY}**, by reading news about **specific funding rounds**.

Independence matters: your list will be compared with a list built from association member lists and registers,
to estimate how many investors both lists miss. Therefore you must **NOT** use: association member lists, investor
directories, "top VC funds in …" listicles, or aggregator databases (Dealroom, Crunchbase, PitchBook, Vestbee,
Caplight…). Only news articles and press releases about individual funding rounds.

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed).
Search local media ({MEDIA}) and international tech press. Aim for **25–40 distinct funding rounds** spread across
different sectors, round sizes and years (2023, 2024, 2025, 2026).

## What to output

One row per (investor, round) pair: every **organisation** named as an investor in the round – VC funds, corporate
investors, state funds, angel networks / syndicates, family offices. **Skip private individuals** (natural persons)
entirely – do not record their names.

## Rules

1. Only what the article says. Never add investors or rounds from memory.
2. `quote` = verbatim copy-paste (max 200 characters) from the article that names the investor (and ideally the
   company). It will be machine-checked against the page; a paraphrase counts as an error.
3. `deal_date` = announcement date of the round as stated in or on the article (`YYYY-MM-DD`); `null` if unknown.
4. `hq_country_claimed` = the investor's home country only if the article states it or it is explicit in the text;
   otherwise `"unknown"`. Do not guess.
5. Budget: at most 40 tool calls in total.

## Output file

Write a UTF-8 JSON array to `{OUTPUT_PATH}` (create the folder if needed) and nothing else into it.
Row schema:

```json
{
  "investor_name": "string, as written in the article",
  "investor_type_claimed": "vc | pe | cvc | public_vc | family_office | angel_network | accelerator | other | unknown",
  "hq_country_claimed": "CZ | SK | other | unknown",
  "company": "startup / company that raised money",
  "company_country": "CZ | SK | other",
  "round": "pre_seed | seed | series_a | series_b_plus | growth | unknown",
  "amount": "as written in the article, or null",
  "deal_date": "YYYY-MM-DD or null",
  "source_url": "article URL",
  "source_published": "YYYY-MM-DD or null",
  "quote": "verbatim, max 200 chars",
  "accessed_date": "{TODAY}"
}
```

Then reply in at most 150 words: number of rounds and rows, which media worked, anything surprising.
