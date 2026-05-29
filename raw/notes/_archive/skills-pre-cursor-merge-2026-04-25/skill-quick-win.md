---
type: skill
source_type: doc-interne
title: "Skill : Quick Win SEO"
aliases: ["Quick Win", "quick-win-gsc"]
tags: ["skill", "gsc", "ctr", "optimisation", "quick-win"]
created: "2026-04-12"
updated: "2026-04-12"
sources: []
confidence: haute
status: actif
---

# Skill — Quick Win SEO

## Quand déclencher
Pages en position 3–12, impressions élevées, CTR sous-performant. Priorité : optimiser l'existant avant de créer du contenu.

> Trigger : "quick win", "gains rapides", "pages proches du top 3", "CTR faible", export GSC uploadé.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages — URL, Clics, Impressions, CTR, Position (90j) | ✅ Oui |
| Contexte secteur | Recommandé |

Minimum viable : export GSC 30j minimum, position 4–15, tri impressions décroissant.

## Pipeline (6 étapes)

1. **Filtrer** — positions 3.0 à 15.0, exclure branded + homepage
2. **Trier** — top 10 par impressions décroissantes
3. **Calculer le gap CTR** — CTR attendu (pos 4 = 7%, 5 = 5%, 6-10 = 2-3%) vs CTR réel
4. **Croiser avec l'intention** — décisionnel P1 > transactionnel P2 > informationnel P3
5. **Prioriser** — décisionnel + impressions >500/mois + CTR <3% + gap >1.5%
6. **Lister les leviers** — title, méta, H1, FAQ top de page, densification atomique

## Output obligatoire

Tableau 5–10 pages + fiche action par page (min 2 actions dont 1 [[preuve-atomique]]).

```
QUICK WIN — Top N Opportunités GSC
| # | URL | Position | Impressions | CTR réel | CTR attendu | Delta | Intent |

→ Page /url
Action 1 : [type] — [description concrète]
Action 3 : Densification atomique — [avant/après]
```

## Règles absolues

- ❌ Proposer du nouveau contenu avant d'épuiser les quick wins existants
- ❌ Conseils génériques sans URL concernée
- ❌ Confondre volume de recherche et impressions GSC
- ✅ Toujours inclure au moins 1 exemple avant/après de densification atomique

## Concepts liés

[[preuve-atomique]] · [[grounding-score]] · [[intention-recherche]] · [[gsc-export]]
