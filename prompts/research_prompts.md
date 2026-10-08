# Research and review prompts (phase 0 – planning)

Verbatim prompts given to subagents during planning on 2026-10-08. All subagents ran on **Claude Haiku 5.5**.
Their full transcripts are in `ai-log/`. Evaluation of their output is in `docs/AI_WORKFLOW.md`.

---

## R1 – Global investor universe size (Explore agent)

```
You are doing web research (use WebSearch and WebFetch; load them via ToolSearch "select:WebSearch,WebFetch" if needed). Do NOT write any files.

Goal: find quantitative estimates of how many investors exist worldwide, per category, to size a global investor database built from public data.

Find, with source + year:
(a) Number of active VC firms / VC funds and VC AUM: US (NVCA Yearbook, latest available), Europe (Invest Europe), global (PitchBook, Dealroom, Crunchbase, Preqin).
(b) Number of private equity firms globally (Preqin, PitchBook, Bain Global PE Report).
(c) Number of single-family and multi-family offices globally (Deloitte Private "Family Office Insights", UBS Global Family Office Report, EY, Campden Wealth).
(d) Number of active angel investors: US (UNH Center for Venture Research), Europe (EBAN statistics compendium).
(e) Investor counts on public/free platforms: Crunchbase (number of investor profiles), OpenVC (number of investors listed), Dealroom (investors tracked), AngelList.
(f) SEC: number of registered + exempt reporting investment advisers that advise venture capital funds and private equity funds (SEC "Private Funds Statistics" or Form ADV analyses), and count of VC/PE private funds.

Output: a markdown table with columns: category | estimate | year | source name | URL | definition notes. Then 3-5 bullet points on how definitions differ (why numbers diverge).

Rules: Only report numbers you actually saw on a fetched page or search snippet, and include the URL. Anything from memory must be marked UNVERIFIED. Keep the answer under 600 words.
```

## R2 – Public, free data sources (Explore agent)

```
You are doing web research (use WebSearch and WebFetch; load them via ToolSearch "select:WebSearch,WebFetch" if needed). Do NOT write any files.

Goal: identify publicly available, FREE data sources that can be used to build and verify a database of investors (VC funds, PE firms, family offices, angel investors), prioritizing machine-readable sources and APIs. Only public data may be used (no paid databases).

For each source report: what it contains (esp. fund type, AUM / gross asset value, ticket size, portfolio), coverage (geography, approx. count), access method (bulk download / API / HTML only), licence / ToS restrictions on scraping and reuse, URL.

Must cover:
1. SEC Form ADV bulk data (Schedule D section 7.B.1 — private fund type e.g. "venture capital fund"/"private equity fund", gross asset value) and IAPD; where the bulk CSVs are downloadable.
2. SEC Form D on EDGAR (industry group "Pooled Investment Fund", fund type, offering size) and EDGAR full-text search / API.
3. ESMA registers: EuVECA funds/managers, AIFM register — is there a download or API (registers.esma.europa.eu)?
4. GLEIF LEI data (fund entities, fund managers) — free API.
5. UK Companies House (SIC 64303 "venture and development capital companies") API; FCA register.
6. OpenCorporates (free/open terms), Wikidata (venture capital firm items, SPARQL).
7. Crunchbase free tier and its ToS on scraping; OpenVC; Dealroom public pages; AngelList.
8. EIF list of funds it backs; Invest Europe member directory; national VC association member lists.
9. Public sources for family offices and angels (angel network directories, EBAN members).
10. News/event data: GDELT, press-release wires.

Output: concise markdown table + 3-5 sentence recommendation on which sources are most reliable for (a) proving an entity exists, (b) proving it actually invests (dated evidence), (c) AUM/fund size, (d) ticket size and sector focus.

Rules: mark anything not confirmed on a fetched page or search snippet as UNVERIFIED. Include URLs. Keep under 800 words.
```

## R3 – Slovak (and Czech) VC landscape (Explore agent)

```
You are doing web research (use WebSearch and WebFetch; load them via ToolSearch "select:WebSearch,WebFetch" if needed). Do NOT write any files.

Goal: scope a pilot sample "VC funds/investors based in Slovakia" for an investor database where each record must be a real, active investor with dated public evidence.

Find:
1. List sources: SLOVCA (Slovak Venture Capital and Private Equity Association) member list; SAPIE (Slovak Alliance for Innovation Economy) investor list/map; Slovak Investment Holding (SIH) / National Development Fund II (NDF II) — which venture funds it backed; NBS (Národná banka Slovenska) register of alternative investment fund managers (správcovia AIF, registered/sub-threshold AIFMs) and whether it is downloadable; ESMA EuVECA register entries for Slovakia; Dealroom / CEE VC reports mentioning Slovak VCs; Startitup / Forbes Slovakia / StartupInfo lists of Slovak investors.
2. A candidate list of VC investors headquartered in Slovakia (name + website + one evidence URL if found). Estimate how many are active (made an investment in the last ~3 years). Also note notable angel networks and corporate VCs in Slovakia.
3. Slovak public registries useful for verification and their APIs: RPO (Register právnických osôb — Statistical Office API), ORSR (Obchodný register), Register účtovných závierok (registeruz.sk open API), FinStat. Note what each returns (IČO, NACE/SK NACE code, shareholders, financial statements).
4. For comparison: approx. number of VC funds in the Czech Republic (CVCA members) and in Poland.

Output: structured markdown with URLs for everything. Mark items you did not confirm on a fetched page or search snippet as UNVERIFIED. Keep under 900 words.
```

## R4 – Plan red-team review (Plan agent)

```
You are a critical reviewer (red team) of a project plan. Do NOT write or edit any files; just return your critique as text.

Read the draft plan at: <plan file>

Background: it's a job-interview assignment (deadline 16 Oct 2026, today 8 Oct 2026, one person + Claude Code). The assignment (translated from Slovak) says: <full assignment text in English>

User decisions already made (do not re-litigate): pilot = VC investors HQ'd in Slovakia + Czechia; engine = Claude Code Haiku subagents for search/extraction + Python deterministic checks (no API key); docs in Slovak; user manually verifies a random stratified subset (~30 included + ~10 rejected).

Critique the plan on:
1. Gaps vs. the assignment requirements (anything required that the plan doesn't produce).
2. Weak or ambiguous inclusion/exclusion rules or edge cases that will cause misclassification (give concrete CZ/SK-style examples).
3. Statistical soundness of the precision measurement (sample size, what "precision" means, bias, blinding).
4. Feasibility in ~7 days: what is over-engineered and could be cut or simplified without hurting the deliverables; what is the riskiest step.
5. Anything in the cost-estimate or universe-estimate methodology that a skeptical interviewer would attack.

Return at most 12 bullet points, ranked by importance, each with a concrete suggested fix. Be concise (under 500 words).
```

## R5 – Fact-check of universe-size anchors (general-purpose agent)

```
You are a fact-checker. Use WebSearch and WebFetch (load via ToolSearch "select:WebSearch,WebFetch" if they are not loaded). Do NOT create or edit any files.

Task: for each claim below, open the PRIMARY source page (or the closest official page) and confirm or correct the figure. For each claim return:
- status: CONFIRMED / CORRECTED / NOT_FOUND
- the exact figure as stated by the source
- reference year / as-of date of the figure
- URL you actually fetched
- a VERBATIM quote (copy-paste, max 200 characters) from the fetched page that contains the figure. If you could not fetch the page and only saw a search snippet, say "SNIPPET ONLY" and quote the snippet.

Claims:
1. NVCA Yearbook: 3,417 US venture capital firms managing $1.21 trillion AUM at year-end 2023. Also check if a newer NVCA yearbook (2025 or 2026) gives a newer firm count.
2. Invest Europe: 3,095 active private equity/VC firms in Europe and EUR 1.25 trillion AUM in 2024.
3. SEC Private Fund Statistics (Form PF), latest quarter: number of advisers to venture capital funds and number of VC funds; same for private equity funds. (URL hint: sec.gov/data-research/data-visualizations/private-fund-statistics)
4. Preqin: approximately 10,300 active private equity fund managers (any official Preqin page stating number of PE firms/managers).
5. Deloitte Private "Family Office Insights": 8,030 single family offices globally in 2024, projected 10,720 by 2030.
6. UNH Center for Venture Research: number of active angel investors in the US (latest year available).
7. EBAN Statistics Compendium: number of active (networked) business angels in Europe (latest edition).
8. ESMA: number of registered EuVECA funds/managers and number of authorised AIFMs in the EU (any ESMA statistic or register count).
9. Dealroom or Crunchbase: total number of investor profiles they track (official page).

Output a markdown table: # | status | figure | as-of | URL | verbatim quote. Then list in 2-4 bullets any discrepancies with the claims above. Be strict: never fill in a number you did not see. Under 700 words.
```
