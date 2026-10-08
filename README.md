# Clientelo – Zadanie A: Spoľahlivá databáza investorov

> **Stav:** rozpracované (deň 1 – plán). README sa dopĺňa priebežne; finálna verzia bude obsahovať
> výsledky pilotu, meranie presnosti a odhad nákladov.

## O čo ide

Cieľom je navrhnúť a overiť postup, ako z verejných zdrojov zostaviť databázu investorov do firiem
(VC, PE, family office, angel investori, veľkí súkromní investori), v ktorej je **každý záznam skutočný
investor** a **každý údaj má zdroj a dátum**.

| Časť zadania | Kde v repozitári |
|---|---|
| Plán (pravidlá zaradenia/vyradenia, overovanie, odhad rozsahu a spoľahlivosti) | [docs/PLAN.md](docs/PLAN.md) |
| Rozhodnutia pri nejasnostiach zadania | [docs/DECISIONS.md](docs/DECISIONS.md) |
| Ako som pracoval s AI (pokyny agentom, kontrola výstupov, chyby agentov) | [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) |
| Dáta zo vzorky (VC fondy CZ + SK) so zdrojom pri každom údaji | `data/processed/` *(pripravuje sa)* |
| Meranie presnosti | `docs/PRECISION_REPORT.md` *(pripravuje sa)* |
| Odhad nákladov na rozšírenie na celý svet | `docs/COST_ESTIMATE.md` *(pripravuje sa)* |
| Export konverzácií s Claude Code | [ai-log/](ai-log/) |

## Spustenie

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"
.venv/Scripts/python -m pytest
```
