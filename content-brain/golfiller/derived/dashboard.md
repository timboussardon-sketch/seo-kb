# Dashboard golfiller — prédictions vs réalisé

Régénéré à chaque production et à chaque pull GSC. `open` = en attente de la GSC à l'échéance.

| Prédiction | Page | Baseline | Pari | Échéance | Statut |
|---|---|---|---|---|---|
| P-…-1 | quelle-balle-de-golf-choisir | pos 8,45 | position moyenne < 5 | 2026-07-03 (J+30) | open |
| P-…-2 | quelle-balle-de-golf-choisir | CTR baseline | CTR +20 % | 2026-09-01 (J+90) | open |

## Comment résoudre
Déposer un export GSC dans `raw/data/exports-gsc/` → `gsc-watcher` met à jour le `status` des prédictions (`hit`/`miss`/`partial`) et régénère ce dashboard. À ce moment, on saura, mesuré, si l'angle « page décisionnelle answer-first » a tenu.

## Pages produites
- 2026-06-03 · quelle-balle-de-golf-choisir · gate NO-PASS (2 bloqueurs : data clients du tableau, décision remplacement page existante)
