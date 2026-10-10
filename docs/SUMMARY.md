# Zhrnutie – Zadanie A: Spoľahlivá databáza investorov

**Úloha.** Navrhnúť a na pilote overiť postup, ako z verejných zdrojov zostaviť databázu investorov, v ktorej je
každý záznam skutočný investor a každý údaj (sektor, typická investícia, tiket, celkový kapitál) má zdroj. Pilot:
**VC investori so sídlom v Česku a na Slovensku**, stav k 9. 10. 2026.

## Ako to funguje

1. **Pravidlá vopred** ([PLAN.md](PLAN.md)): investor = aspoň 2 doložené investície do firiem, aspoň 1 za posledných
   36 mesiacov, identita v registri; vyradenie s kódom dôvodu (E1–E9). Metriky presnosti definované pred meraním.
2. **AI zbiera, kód overuje.** Agenti Claude Haiku 5.5 vracajú tvrdenia s URL a doslovnou citáciou; program stránku
   stiahne a citáciu na nej hľadá. Identitu berie z registrov ARES a RPO, o zaradení rozhoduje kód.
3. **Kontrola v štyroch vrstvách:** strojová kontrola každého tvrdenia, registre, nezávislý AI overovateľ, slepá
   kontrola vzorky silnejším modelom (Sonnet 5.5) a ľudský audit.
4. **Spresnenie** ([REFINEMENT.md](REFINEMENT.md)): slabé polia (kapitál, dátumy obchodov) zaradených záznamov
   znovu prečítal Sonnet 5.5; zlepšenie zmerala slepá kontrola faktov, ktorá nevedela, ktorá hodnota je nová.

## Výsledky

| | |
|---|---|
| Kandidátov z verejných zdrojov | 206 → **24 zaradených** (20 CZ, 4 SK), 70 vyradených, 35 mimo rozsahu, 4 na ručnú kontrolu |
| Tvrdení overených programom na stránke zdroja | 808 z 852 (95 %) |
| **Presnosť zaradenia** (slepá kontrola) | **23/23** (95 % CI 86–100 %) |
| Ručná kontrola autora (5 záznamov) | 4/4 zaradené potvrdené, návnada správne vyradená; zhoda so Sonnetom 4/5 |
| Správne vyradené | skutočné vyradené 3/3; návnady 3/5 prísne, 5/5 vrátane prípadov, keď dôkaz nenašiel ani kontrolór |
| Dátum obchodu správny (±2 mesiace) | 79 % → **97,5 %** po spresnení |
| Celkový kapitál správny | 53 % → **70 %** po spresnení (vyplnený pri 20 z 24) |
| Identita v registri | 24/24 |
| Povinné polia | sektory a štádiá 24/24, tiket 22/24, kapitál 20/24; zvyšok overene verejne neuvedený, nič neodhadnuté |
| Pokrytie trhu (capture–recapture) | ~78 % z odhadovaných ~31 aktívnych VC v CZ/SK |

## Čo sa ukázalo

- **Kto je investor, sa dá overiť spoľahlivo.** Slabé sú údaje o investíciách: články často len spomínajú staršiu
  investíciu a cieľ fondu sa ľahko zamení s uzavretým fondom.
- **Strojová kontrola citácií chráni pred halucináciou, nie pred zlým výkladom pravdivého textu.** Tri chyby výkladu
  (kapitál „30 €“, plánovaný fond, cudzie IČO) našiel človek za pár minút; každú som opravil systémovo v kóde
  (dáta zmrazené v1 → v2 → v3), nie ručnou úpravou záznamu.
- **Model podľa úlohy:** lacný Haiku na zber, silnejší Sonnet cielene len na zaradené záznamy a len na slabé polia.
  Stálo to 0,75 USD na záznam a dátumy obchodov sa zlepšili zo 79 % na 97,5 %.

## Celý svet

- **Rozsah:** ~32–70 tisíc doložiteľných aktívnych investorov, základný odhad ~45 tisíc (VC 6–11 tis., PE 8–13 tis.,
  family office 1–2,5 tis., angel 15–40 tis.); vychádza zo strojovo overených kotiev (Invest Europe, Preqin, Deloitte,
  UNH, EBAN) a z pilotu.
- **Spoľahlivosť:** VC a PE vysoká (investície zverejňujú), family office a angel nízka (publicite sa vyhýbajú, GDPR).
- **Náklady 1. rok:** ~97 tis. € v základnom scenári, s odporúčaným spresnením Sonnetom ~142 tis. €. Najväčšia
  položka je ľudská kontrola kvality, nie AI ([COST_ESTIMATE.md](COST_ESTIMATE.md)).

## Obmedzenia

- Malá vzorka (23 zaradených) dáva široký interval spoľahlivosti; na ±5 bodov treba ~140 záznamov na segment.
- Ručne overených je len 5 záznamov (D40); celkový kapitál autor z verejných zdrojov neoveril ani pri jednom –
  potvrdzuje, že kapitál je najťažšie overiteľný údaj.
- Spresnenie aj kontrolu faktov robil model tej istej rodiny – korelované chyby nemožno vylúčiť.
- Pilot pokrýva len VC v CZ/SK; odhady pre PE, family office a angel investorov sú hypotézy.

## Kde čo nájsť

[README.md](../README.md) · [PLAN.md](PLAN.md) · [PRECISION_REPORT.md](PRECISION_REPORT.md) ·
[REFINEMENT.md](REFINEMENT.md) · [COST_ESTIMATE.md](COST_ESTIMATE.md) · [AI_WORKFLOW.md](AI_WORKFLOW.md) ·
[DECISIONS.md](DECISIONS.md) · prezentácia [prezentacia.pdf](prezentacia.pdf) · prehliadač investorov [explorer.html](explorer.html) · dáta v
[data/processed/](../data/processed/)
