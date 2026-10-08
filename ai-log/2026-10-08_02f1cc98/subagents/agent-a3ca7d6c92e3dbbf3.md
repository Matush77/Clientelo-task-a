# Subagent: Red-team the draft plan (Plan, model: haiku)

## 👤 Používateľ · 2026-10-08 19:25:11

You are a critical reviewer (red team) of a project plan. Do NOT write or edit any files; just return your critique as text.

Read the draft plan at: C:\Users\matus\.claude\plans\i-have-received-two-frolicking-valiant.md

Background: it's a job-interview assignment (deadline 16 Oct 2026, today 8 Oct 2026, one person + Claude Code). The assignment (translated from Slovak) says:
"Build a database of investors into companies: VC funds, private equity, family offices, angel investors and large private investors. Data reliability is key: every record must be a real investor, not a random company. Each investor must have: the sector it operates in, what it typically invests in and at what size, its total investment capital, and where this information comes from. Start with a plan. It must make clear who will and won't be in the database, i.e. the rules for including/excluding an entity. Also describe how you will verify authenticity and correct classification of records. Estimate what range of investors can be obtained from public sources, roughly how many, and how reliable the data will be; state what the estimate is based on. Then validate the plan on a smaller sample, e.g. VC funds in one country. For each record give a source and date proving the entity actually invests. Measure precision on a manually verified sample. Finally estimate the cost of expanding worldwide. Use only publicly available data. Repo must contain: plan, sample data with a source for every data point, precision measurement result, code with incremental commit history, and an ai-log folder with Claude Code conversation exports. README must describe how AI was used (instructions given to agents, how output was checked, where agents erred). Unclear points: decide yourself and justify in README."

User decisions already made (do not re-litigate): pilot = VC investors HQ'd in Slovakia + Czechia; engine = Claude Code Haiku subagents for search/extraction + Python deterministic checks (no API key); docs in Slovak; user manually verifies a random stratified subset (~30 included + ~10 rejected).

Critique the plan on:
1. Gaps vs. the assignment requirements (anything required that the plan doesn't produce).
2. Weak or ambiguous inclusion/exclusion rules or edge cases that will cause misclassification (give concrete CZ/SK-style examples).
3. Statistical soundness of the precision measurement (sample size, what "precision" means, bias, blinding).
4. Feasibility in ~7 days: what is over-engineered and could be cut or simplified without hurting the deliverables; what is the riskiest step.
5. Anything in the cost-estimate or universe-estimate methodology that a skeptical interviewer would attack.

Return at most 12 bullet points, ranked by importance, each with a concrete suggested fix. Be concise (under 500 words).

<details><summary>🔧 Read – C:\Users\matus\.claude\plans\i-have-received-two-frolicking-valiant.md</summary>

````text
{
  "file_path": "C:\\Users\\matus\\.claude\\plans\\i-have-received-two-frolicking-valiant.md"
}
````

</details>

<details><summary>↳ výsledok nástroja</summary>

````text
1	# Plan — Zadanie A: Spoľahlivá databáza investorov (pilot CZ + SK)
2	
3	## Context
4	
5	Interview assignment (deadline **16. 10. 2026**, today 8. 10.). Build a *reliable* investor database
6	(VC, PE, family offices, angels, large private investors) where every record is a real investor with
7	**sector, typical investment + ticket size, total capital and source**. Required deliverables in a
8	public GitHub repo:
9	
10	1. **Plan**: inclusion/exclusion rules, verification method, size and reliability estimate of the
11	   publicly reachable universe, plus what that estimate is based on.
12	2. **Pilot**: VC funds in one country, with a **source and date proving each entity invests**. All data public only.
13	3. **Precision** measured on a manually verified sample.
14	4. **Cost estimate** for worldwide expansion.
15	5. **README**: how AI was used (agent instructions, how output was checked, where agents erred),
16	   judgment calls with reasoning, and what's missing.
17	6. Code with **incremental commit history**, and `ai-log/` holding the `/export` of Claude Code sessions.
18	
19	The user wants to understand and present every step, so the plan has explicit review checkpoints.
20	
21	**Decisions made with the user (8. 10.)**
22	
23	- Pilot scope: **VC investors headquartered in Slovakia + Czechia**. Slovakia alone has only ~5–10 active VCs
24	  (research), which is too few for a meaningful precision CI.
25	- Engine: **Claude Code subagents (Haiku 5.5 only)** do search and extraction, and **Python** does the deterministic
26	  checks. No API key is needed. Cost is extrapolated from measured agent token usage × current API prices.
27	- Language: **Slovak** for PLAN, README and reports. Code, identifiers and comments are in English.
28	- Manual check: **the user verifies a random stratified subset** (~30 included + ~10 rejected records).
29	
30	**Environment**: Python 3.13, git 2.49 and Node 22 are installed. `gh` and `uv` are not, so we'll use a venv + pip.
31	The GitHub repo is created by the user on github.com, or by installing gh with the user's approval.
32	
33	---
34	
35	## Core idea: a claim–evidence data model
36	
37	Every data point is a **claim**: `(investor_id, field, value, source_url, publisher, published_date,
38	accessed_date, verbatim_quote, source_tier, derivation [stated|inferred], auto_check_status)`.
39	`investors.csv` is the wide, human-readable view, and `claims.csv` is the long table that proves each cell.
40	This directly satisfies "zdroj pri každom údaji". It also lets code verify mechanically that the quote really
41	exists at the URL, which catches hallucinations.
42	
43	**Source tiers**
44	
45	| Tier | Sources | Use |
46	|---|---|---|
47	| T1 | Regulators and registries: ARES (CZ), RPO/ORSR (SK), ČNB/NBS fund registers, ESMA EuVECA, GLEIF; official LP disclosures (EIF, SIH/NDF II, NRB) | Can stand alone as evidence |
48	| T2 | The investor's own website, portfolio pages and press releases | Evidence, but self-reported |
49	|
… [skrátené, 13044 znakov – plné znenie v raw/]
````

</details>

### 🤖 Claude · 2026-10-08 19:26:51

1. **[Rules/GDPR]** I1 admits self-declared natural persons, yet names and ticket sizes would be published on public GitHub. Fix: exclude private individuals from the published data or pseudonymise them, and record the legal basis in DECISIONS.md.

2. **[Stats]** "Precision" is undefined, and the reviewer sees the pipeline's own quotes, which anchors them. Fix: pre-register the primary metric (confirmed real, active, correct type and HQ), have the reviewer open the URLs, and report self-made decoys separately from real rejects. Zero errors in 10 rejects still allows about 28% error (Wilson).

3. **[Stats]** If the pilot yields about 40–60 INCLUDED records, sampling 30 is nearly a census. Fix: review all of them. Even 27/30 gives a Wilson 95% CI of 74–97%. Exclude the calibration records and the CP2 prompt-tuning candidates from the review frame.

4. **[Scope]** The "SK has 5–10 VCs" rationale uses the research figures the plan itself says it does not trust (line 189). Fix: verify against the SLOVCA member list and the NBS register before CP1.

5. **[Universe]** Anchor × pilot inclusion rate is invalid. A CZ/SK rate does not transfer to US/EU anchors, and the seed list favours press-visible investors. PitchBook and Preqin figures are not publicly reproducible. Fix: use dated register counts (ESMA AIFMD/EuVECA, ČNB, NBS, SEC Form ADV) and estimate coverage by capture–recapture between two independent seed lists.

6. **[Cost/ai-log]** `/export` may omit token counts, and subagent transcripts are stored separately, so runs.csv and ai-log may be incomplete. Fix: parse `usage` from the local session JSONL files, state costs as equivalent API cost at dated prices, and export subagent logs too.

7. **[Cost]** "Multilingual overhead" is a placeholder, and human QA dominates cost. For ±5 pp at p=0.9, n = z²p(1−p)/E² ≈ 140 checked records per segment. Fix: measure the multiplier on a 10–15-record PL or DE slice and show 1×/2×/4× sensitivity.

8. **[Rules]** Undefined edge cases: (a) state LP programmes (SIH, NRB) are "public VC" under I4 but fund-of-funds under E5; (b) a Prague team running a Luxembourg SICAV: is HQ the AIFM seat?; (c) a bank's venture arm investing externally versus E6 group-internal; (d) fund IČO versus manager IČO versus a same-brand sister s.r.o. Fix: a decision table with one test fixture per case.

9. **[Rules]** Sector, ticket and capital labels are subjective ("deep tech" from marketing copy) and will dominate errors. Fix: keep them out of the primary metric and have the user re-code 10 records blind a week later to compute Cohen's kappa.

10. **[Feasibility, riskiest step]** The fetch and quote firewall will fail on JS sites, 403s and PDFs, and RPO API access is assumed rather than checked. Fix: spike 20 URLs and the RPO API on Day 2, and archive each claim's URL in the Wayback Machine so proofs survive link rot.

11. **[Feasibility]** Over-engineered for 7 days: 11+ modules, a verifier on every record, cost.py and five checkpoints. Fix: reduce cost.py to a spreadsheet, run the verifier only on the review set, merge dedup into rules.py, and cap the agent run (for example, 60 candidates) to avoid subscription limits.

12. **[Stats]** The 36-month "active" test has no reference date. Fix: set as_of to the pilot-frozen tag date and store it in every record.
