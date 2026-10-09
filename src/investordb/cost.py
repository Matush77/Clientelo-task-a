"""Cost estimate for a worldwide rollout, built from what the pilot measured.

Measured in the pilot (data/raw/agents/runs.csv, data/processed/*.csv, data/review/review_results.csv):
tokens / searches / fetches per pipeline stage, candidates per included record, share of records needing review,
minutes of human review per record, AI-verifier vs human agreement.
Assumed (stated in docs/COST_ESTIMATE.md, varied in the low/base/high scenarios): size of the global database,
multilingual overhead, number of QA segments, hourly rate, engineering effort.

Prices: Anthropic API list prices (see data/reference/api_prices.csv), never from memory.
"""

from __future__ import annotations

import csv
import statistics
from dataclasses import dataclass
from pathlib import Path

from investordb.metrics import sample_size

ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "data" / "raw" / "agents" / "runs.csv"
PROCESSED = ROOT / "data" / "processed"
REVIEW = ROOT / "data" / "review" / "review_results.csv"
USD_PER_EUR = 1.1186  # ECB reference rate 2026-10-08 (fetched by money.eur_rate in the pilot)

# Claude Haiku 5.5, USD per million tokens (prompts <= 100K tokens) and per search
PRICES = {"input": 0.10, "output": 0.50, "cache_write_5m": 0.125, "cache_write_1h": 0.20, "cache_read": 0.01,
          "web_search": 10.0 / 1000}
# In Claude Code, WebFetch hands the agent a short extract; an API pipeline's web_fetch returns page text into the
# context. Added as extra input tokens per fetched page so the API cost is not understated.
TOKENS_PER_FETCHED_PAGE = 6000

STAGES = {  # description keywords -> stage (see usage.py / runs.csv)
    "verifier": "verifier", "recent-deal": "recent_deal", "evidence": "evidence", "list a": "discovery",
    "list b": "discovery", "lookalike": "discovery", "hq triage": "hq_triage", "duplicate": "duplicate_check",
}


def stage_of(description: str) -> str:
    d = description.lower()
    return next((s for k, s in STAGES.items() if k in d), "research_planning")


def run_cost(row: dict) -> float:
    """API-equivalent USD cost of one measured agent run at Haiku 5.5 prices."""
    tokens = (int(row["input_tokens"]) + int(row["web_fetches"]) * TOKENS_PER_FETCHED_PAGE) * PRICES["input"]
    tokens += int(row["output_tokens_est"]) * PRICES["output"]
    tokens += int(row["cache_write_5m_tokens"]) * PRICES["cache_write_5m"]
    tokens += int(row["cache_write_1h_tokens"]) * PRICES["cache_write_1h"]
    tokens += int(row["cache_read_tokens"]) * PRICES["cache_read"]
    return tokens / 1e6 + int(row["web_searches"]) * PRICES["web_search"]


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


@dataclass
class Measured:
    cost_by_stage: dict[str, float]
    evidence_runs: int  # candidate-evidence runs incl. rescue / re-runs
    candidates: int  # unique candidates that went through evidence
    included: int
    needs_review_share: float
    verifier_records: int
    review_minutes: float | None  # median minutes per record from the human review
    searches_share: float  # share of AI cost that is web search

    @property
    def per_candidate(self) -> float:
        """Discovery + triage + evidence + recent-deal cost per candidate."""
        stages = ("discovery", "hq_triage", "evidence", "recent_deal", "duplicate_check")
        return sum(self.cost_by_stage.get(s, 0) for s in stages) / self.candidates

    @property
    def verifier_per_record(self) -> float:
        return self.cost_by_stage.get("verifier", 0) / max(self.verifier_records, 1)


def measure() -> Measured:
    runs = _read(RUNS)
    cost_by_stage: dict[str, float] = {}
    search_cost = 0.0
    for r in runs:
        s = stage_of(r["description"])
        cost_by_stage[s] = cost_by_stage.get(s, 0) + run_cost(r)
        search_cost += int(r["web_searches"]) * PRICES["web_search"]
    decisions = _read(PROCESSED / "decisions.csv")
    minutes = [float(r["minutes_spent"]) for r in _read(REVIEW) if (r.get("minutes_spent") or "").strip()]
    verifier_records = sum(1 for _ in _read(ROOT / "data" / "review" / "review_key.csv"))
    return Measured(
        cost_by_stage=cost_by_stage,
        evidence_runs=145,
        candidates=len(decisions),
        included=sum(d["status"] == "INCLUDED" for d in decisions),
        needs_review_share=sum(d["status"] == "NEEDS_REVIEW" for d in decisions) / max(len(decisions), 1),
        verifier_records=verifier_records,
        review_minutes=statistics.median(minutes) if minutes else None,
        searches_share=search_cost / max(sum(cost_by_stage.values()), 1e-9),
    )


@dataclass
class Scenario:
    name: str
    target_records: int  # verified investors in the global database (docs/PLAN.md 11.2)
    candidates_per_record: float  # pilot: candidates / included
    language_factor: float  # extra searches / tokens outside EN/CZ/SK
    qa_segments: int  # country x investor-type segments that each get a precision estimate
    qa_margin: float  # +- precision margin per segment (95 %)
    review_minutes: float
    eur_per_hour: float
    engineering_days: int
    eur_per_day: float


def scenarios(m: Measured) -> list[Scenario]:
    minutes = m.review_minutes or 4.0
    cpr = m.candidates / max(m.included, 1)
    return [
        Scenario("nízky", 32_000, max(3.0, cpr * 0.6), 1.0, 80, 0.07, minutes * 0.8, 20, 30, 350),
        Scenario("základný", 45_000, cpr, 1.5, 150, 0.05, minutes, 30, 45, 450),
        Scenario("vysoký", 70_000, cpr * 1.5, 3.0, 250, 0.05, minutes * 1.5, 50, 70, 600),
    ]


STAGE_LABELS = {
    "research_planning": "prieskum a plánovanie (jednorazovo)", "discovery": "objavovanie kandidátov",
    "hq_triage": "triáž sídla", "evidence": "zber dôkazov (vrátane opakovaní)", "recent_deal": "etapa „nedávna investícia“",
    "duplicate_check": "kontrola duplicít", "verifier": "nezávislý AI overovateľ", "pricing_check": "overenie cenníka",
}


def _eur(x: float) -> str:
    return f"{x:,.0f} €".replace(",", " ")


def render(m: Measured) -> str:
    sc = scenarios(m)
    est = [estimate(m, s) for s in sc]
    total_usd = sum(m.cost_by_stage.values())
    minutes_note = (f"**{m.review_minutes:.1f} min** (medián z ručnej kontroly)" if m.review_minutes
                    else "**4 min – predpoklad**, nahradí sa meraním z ručnej kontroly")
    L: list[str] = []
    add = L.append
    add("# Odhad nákladov na rozšírenie na celý svet\n")
    add("*Generované skriptom `python -m investordb.cli cost` z meraní v pilote. Ceny: oficiálny cenník Anthropic API "
        "(overený strojovo, [api_prices_md_checked.csv](../data/reference/api_prices_md_checked.csv), 9. 10. 2026); "
        f"kurz ECB 1 € = {USD_PER_EUR} USD.*\n")
    add("## 1. Čo stál pilot (namerané)\n")
    add("Všetci subagenti bežali na **Claude Haiku 5.5**. Náklad je prepočítaný na ceny API (pilot bežal v rámci "
        "predplatného Claude Code), podľa skutočnej spotreby tokenov zo záznamov agentov (`usage.py`).\n")
    add("| Etapa | Náklad (USD) |\n|---|---|")
    for stage, cost in sorted(m.cost_by_stage.items(), key=lambda kv: -kv[1]):
        add(f"| {STAGE_LABELS.get(stage, stage)} | {cost:.2f} |")
    add(f"| **spolu** | **{total_usd:.2f}** |\n")
    add(f"- Na jedného kandidáta (objavovanie + triáž + dôkazy + nedávna investícia): **{m.per_candidate:.3f} USD**")
    add(f"- Nezávislý overovateľ na jeden záznam: **{m.verifier_per_record:.3f} USD**")
    add(f"- **Vyhľadávanie na webe tvorí {100 * m.searches_share:.0f} % nákladov na AI** – samotné tokeny Haiku sú "
        "zanedbateľné.")
    add(f"- Na 1 zaradeného investora pripadlo **{m.candidates / max(m.included, 1):.1f} kandidátov**; "
        f"{100 * m.needs_review_share:.1f} % kandidátov skončilo v ručnej kontrole.")
    add(f"- Ručná kontrola: {minutes_note} na záznam.\n")
    add("*Nezapočítané:* orchestrácia v hlavnej session (Claude Opus 5.5) – v produkčnom postupe ju nahrádza kód; "
        "a prístup k stránkam cez WebFetch v Claude Code vracia agentovi len výťah, kým API vracia celý text – preto "
        f"je v modeli pripočítaných {TOKENS_PER_FETCHED_PAGE} vstupných tokenov na každú stiahnutú stránku.\n")

    add("## 2. Scenáre pre celý svet\n")
    add("| Predpoklad | " + " | ".join(s.name for s in sc) + " | Odkiaľ |")
    add("|---|" + "---|" * len(sc) + "---|")
    rows = [
        ("Overených investorov v databáze", [f"{s.target_records:,}".replace(",", " ") for s in sc], "PLAN.md, kap. 11.2"),
        ("Kandidátov na 1 zaradený záznam", [f"{s.candidates_per_record:.1f}" for s in sc], "pilot (základ); lepšie zdroje / horšie trhy"),
        ("Viacjazyčnosť / ťažšie trhy (násobok AI)", [f"{s.language_factor:.1f}×" for s in sc], "predpoklad"),
        ("Segmenty kontroly kvality (krajina × typ)", [str(s.qa_segments) for s in sc], "predpoklad"),
        ("Presnosť odhadu na segment (±, 95 %)", [f"{100 * s.qa_margin:.0f} p. b." for s in sc], "voľba"),
        ("Minút ručnej kontroly na záznam", [f"{s.review_minutes:.1f}" for s in sc], "pilot (základ)"),
        ("Hodinová sadzba kontrolóra", [f"{s.eur_per_hour:.0f} €" for s in sc], "predpoklad (analytik CEE / západná Európa)"),
        ("Vývoj produkčnej pipeline", [f"{s.engineering_days} dní × {s.eur_per_day:.0f} €" for s in sc], "predpoklad"),
    ]
    for label, vals, src in rows:
        add(f"| {label} | " + " | ".join(vals) + f" | {src} |")
    add("\n| Výsledok (1. rok) | " + " | ".join(s.name for s in sc) + " |")
    add("|---|" + "---|" * len(sc))
    for key, label in (("candidates", "Kandidátov na spracovanie"), ("ai_eur", "AI (Haiku 5.5 + vyhľadávanie)"),
                       ("qa_records", "Záznamov na ručnú kontrolu"), ("human_eur", "Ľudská kontrola kvality"),
                       ("engineering_eur", "Vývoj (jednorazovo)"), ("year1_eur", "**Spolu 1. rok**"),
                       ("per_record_eur", "Na 1 overený záznam"), ("refresh_eur", "Ročná aktualizácia (od 2. roka)")):
        vals = [f"{e[key]:,.0f}".replace(",", " ") if key in ("candidates", "qa_records") else
                (f"{e[key]:.2f} €" if key == "per_record_eur" else _eur(e[key])) for e in est]
        add(f"| {label} | " + " | ".join(vals) + " |")
    add("")
    add("## 3. Čo z toho vyplýva\n")
    base = est[1]
    add(f"- **Hlavný náklad nie je AI, ale ľudská kontrola kvality.** V základnom scenári AI stojí "
        f"{_eur(base['ai_eur'])}, ľudská kontrola {_eur(base['human_eur'])}.")
    add("- **Najväčšia páka je zhoda AI overovateľa s človekom** (meraná v [PRECISION_REPORT.md](PRECISION_REPORT.md)). "
        "Ak je vysoká, človek kontroluje len segmentovú vzorku a záznamy, kde sa AI overovateľ a pravidlá nezhodnú; "
        "ak nízka, počet ručne kontrolovaných záznamov rastie.")
    add("- **Druhá páka je vyhľadávanie:** tvorí väčšinu nákladov na AI. Štruktúrované zdroje (registre SEC Form ADV, "
        "ESMA, národné registre, zoznamy asociácií) znižujú počet kandidátov na 1 zaradený záznam aj počet vyhľadávaní.")
    add("- **Tretia páka je kvalita zoznamu kandidátov:** v pilote bolo 5,3 kandidáta na 1 zaradeného investora; "
        "v krajinách bez dobrých zoznamov (a pri family office / angel investoroch) to bude viac.")
    add("- Model Haiku 5.5 stačí: všetky kroky, kde záleží na presnosti, robí deterministický kód (kontrola citácií, "
        "pravidlá, registre). Drahší model by zvýšil cenu AI ~20× bez zmeny tejto architektúry.\n")
    add("## 4. Obmedzenia odhadu\n")
    add("- Pilot meral VC investorov v CZ/SK. Pre PE, family office a angel investorov bude pomer kandidátov k zaradeným "
        "a čas kontroly iný (family office sú menej verejné).")
    add("- Prístup k registrom: ARES (CZ) a RPO (SK) sú zadarmo; v niektorých krajinách sú registre platené alebo bez API – "
        "v odhade nie sú zahrnuté poplatky za výpisy.")
    add("- Limity nástrojov (rate limit vyhľadávania) určujú skôr čas behu než cenu; pri ~240 tis. kandidátoch a ~10 "
        "paralelných agentoch ide o týždne behu, nie hodiny.")
    return "\n".join(L) + "\n"


def write() -> Path:
    out = ROOT / "docs" / "COST_ESTIMATE.md"
    out.write_text(render(measure()), encoding="utf-8")
    return out


def estimate(m: Measured, s: Scenario) -> dict[str, float]:
    candidates = s.target_records * s.candidates_per_record
    ai_usd = candidates * m.per_candidate * s.language_factor + s.target_records * m.verifier_per_record
    qa_records = s.qa_segments * sample_size(0.9, s.qa_margin) + candidates * m.needs_review_share
    human_eur = qa_records * s.review_minutes / 60 * s.eur_per_hour
    engineering_eur = s.engineering_days * s.eur_per_day
    # yearly refresh: quarterly recent-deal check of every record + re-QA of 25 % of the segments
    refresh_ai_usd = 4 * s.target_records * (m.cost_by_stage.get("recent_deal", 0) / 8) * s.language_factor
    refresh_human_eur = 0.25 * s.qa_segments * sample_size(0.9, s.qa_margin) * s.review_minutes / 60 * s.eur_per_hour
    ai_eur = ai_usd / USD_PER_EUR
    year1 = ai_eur + human_eur + engineering_eur
    return dict(candidates=candidates, ai_eur=ai_eur, qa_records=qa_records, human_eur=human_eur,
                engineering_eur=engineering_eur, year1_eur=year1, per_record_eur=year1 / s.target_records,
                refresh_eur=refresh_ai_usd / USD_PER_EUR + refresh_human_eur)
