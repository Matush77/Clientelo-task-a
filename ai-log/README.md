# ai-log – export konverzácií s Claude Code

Práca prebiehala v desktopovej aplikácii Claude Code. Namiesto CLI príkazu `/export` sa použil **Export session**
z aplikácie (ten istý obsah, navyše obsahuje aj prepisy všetkých subagentov). Export sa spracúva skriptom
[tools/export_ailog.py](../tools/export_ailog.py) pri každom kontrolnom bode – neskorší export tej istej session
nahradí skorší; staršie verzie zostávajú v histórii gitu.

| Súbor | Obsah |
|---|---|
| `<dátum>_<session>/conversation.md` | hlavná konverzácia v čitateľnej podobe: moje pokyny, odpovede Claude, volania nástrojov (zbalené), moje odpovede na otázky |
| `<dátum>_<session>/subagents/*.md` | každý subagent zvlášť: pokyn, ktorý dostal, jeho postup a výsledok; v nadpise je model (`haiku` pri zbere a overovaní, `sonnet` pri kontrole vzorky, spresnení a kontrole faktov) |
| `<dátum>_<session>/raw/` | pôvodné JSONL prepisy (vrátane spotreby tokenov – zdroj pre odhad nákladov) |

**Čo bolo odstránené:** môj e-mail (skript zlyhá, ak by v exporte zostal), čokoľvek, čo vyzerá ako API kľúč, a mená fyzických osôb, ktoré citovali AI kontrolóri (D37; zoznam mien je len lokálne).
**Čo nie je priložené:** súbory, ktoré agenti stiahli z webu (PDF správy tretích strán – autorské práva) a interné
nastavenia aplikácie.
