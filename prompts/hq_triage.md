# HQ-triage agent – v1

Placeholders `{CANDIDATES}`, `{OUTPUT_PATH}`, `{TODAY}` are filled in by the orchestrator.

---

The investors below were named in news about funding rounds of Czech or Slovak startups, but none of them was found
in the Czech (ARES) or Slovak (RPO) company registry under that name. Most are probably foreign funds. For each one,
answer **one question only: in which country does its investment team / headquarters sit?**

Use WebSearch / WebFetch (load them with ToolSearch `select:WebSearch,WebFetch` if needed). Budget: **at most 2 tool
calls per investor** – usually one search is enough (the investor's own website "about"/"contact" page is the best
source). Do not research anything else.

## Investors

{CANDIDATES}

## Rules

1. `hq_country` = ISO-2 country code (e.g. `DE`, `US`, `CZ`, `SK`). If the evidence is unclear, use `"unknown"`.
2. `quote` = verbatim copy-paste (max 200 characters) from the page that states the location. It will be
   machine-checked against the page. Copy only from word-for-word output, never from a summary or search snippet.
3. If the investor turns out to be a Czech or Slovak firm whose legal name differs from the brand, give the legal
   name / company ID if the page shows it.

## Output file

Write a UTF-8 JSON array to `{OUTPUT_PATH}` (create the folder if needed), nothing else into it:

```json
{
  "candidate_id": "as given",
  "name": "as given",
  "hq_country": "ISO-2 or unknown",
  "website": "official website or null",
  "legal_name": "string or null",
  "company_id": "string or null",
  "source_url": "string",
  "quote": "verbatim, max 200 chars",
  "accessed_date": "{TODAY}"
}
```

Then reply in at most 80 words: how many are CZ/SK, how many foreign, how many unknown.
