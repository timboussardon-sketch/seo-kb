---
type: concept
title: "Framework Know-Simple / Know / Do (remplace TOFU/MOFU/BOFU)"
aliases: [know-simple-know-do, framework-know-do, ksk-do]
tags: [doctrine-tim, framework, intentions, aeo, agentic-search, alternative-tofu-mofu-bofu]
created: 2026-05-01
updated: 2026-05-01
sources: 4
confidence: high
status: stable
---

# Framework Know-Simple / Know / Do

**Framework propriétaire Tim** qui remplace les classifications TOFU/MOFU/BOFU (Top/Middle/Bottom Of Funnel) **obsolètes à l'ère de l'Agentic Search**. Trois types d'intentions, chacune liée à un format de page précis.

## Les 3 intentions

| Intention | Description | Format | Schema.org |
|---|---|---|---|
| **Know-Simple** | L'utilisateur veut une **réponse factuelle courte** | FAQ + définition 50-100 mots, réponse directe | `FAQPage` + `DefinedTerm` |
| **Know** | L'utilisateur veut **comprendre en profondeur** | Guide long, méthode, comparatif | `HowTo` + `Article` ou `ScholarlyArticle` |
| **Do** | L'utilisateur veut **accomplir une action** | Outil, simulateur, calculateur, démo, formulaire | `WebApplication` ou `Service` |

## Pourquoi ça remplace TOFU/MOFU/BOFU

- **TOFU/MOFU/BOFU = pensée linéaire de funnel** marketing classique. Suppose un parcours en escalier (sensibilisation → considération → décision)
- **Know-Simple/Know/Do = pensée en intentions atomiques** lisibles par les agents IA autonomes. Un même utilisateur peut déclencher plusieurs intentions sur un même cluster sans suivre un funnel
- À l'ère [[concepts/agentic-search]], l'agent IA cherche un format précis pour résoudre **une** intention, pas un "stade dans le funnel"
- Cohérent avec [[concepts/fully-meets]] : pages "Do" sont les seules à pouvoir obtenir la note maximale Quality Raters

## Cluster Know-Simple → Know → Do

Pour chaque pilier sémantique (3-5 par site), construire des pages aux 3 niveaux :

```
PILIER : "Surprise Score"
├── Know-Simple : "C'est quoi le Surprise Score ?" (FAQ 50 mots)
├── Know : "Mesurer le Surprise Score d'une page" (guide méthode 1500 mots)
├── Know thought leadership : "Architecture Titans / MIRAS et Surprise" (essai technique)
└── Do : "Calculateur Surprise Score" (outil interactif, capture email)
```

Cf. [[sources/2026-04-24-cluster-business-organikk-4-piliers]] pour le cluster complet sur les 4 piliers Organikk.

## Maillage interne (règle skill)

- **Know-Simple → Know** du même axe (l'utilisateur curieux veut creuser)
- **Know → Do** du même axe (l'utilisateur informé veut agir) — **le maillage Know → Do passe avant Know → Know** ([[concepts/maillage-systeme]])
- **Do → Page commerciale** (`/services/...`, `/coaching/...`, `/contact`)
- **Pages commerciales → Pilier uniquement** (pas de fuite vers Know)

## Pourquoi c'est doctrinal pour Tim

- Le **mot-clé actionnel** ([[concepts/mots-cles-actionnels]]) = exactement un mot-clé "Do"
- Le **Product-Led SEO** ([[concepts/product-led-seo]]) = la matérialisation page d'une intention "Do"
- Le **test substitution LLM** ([[concepts/test-substitution-llm]]) filtre par intention : si un Know-Simple peut être répondu par ChatGPT à 80 %, ne pas créer la page sauf data propriétaire unique

## Connecté avec OpenDecoder

Le système de scoring [[sources/2026-04-15-opendecoder-seo-scoring-system]] utilise ce framework dans le sous-score 1.2 (Alignement d'intention). Matrice format × intention :

| Format \ Intention | Know-Simple | Know | Do | Commercial |
|---|---|---|---|---|
| Réponse directe | 1.0 | 0.4 | 0.1 | 0.2 |
| Guide/Article | 0.5 | 1.0 | 0.3 | 0.5 |
| Outil/CTA | 0.1 | 0.3 | 1.0 | 0.4 |
| Comparatif/Classement | 0.2 | 0.5 | 0.4 | 1.0 |

(Note : OpenDecoder ajoute "Commercial" comme 4e intention pour le scoring — formalisation complémentaire au triplet de base.)

## Pages liées

[[sources/2026-04-24-reflexion-organikk-4-piliers]] · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] · [[sources/2026-04-15-opendecoder-seo-scoring-system]] · [[concepts/aeo]] · [[concepts/agentic-search]] · [[concepts/fully-meets]] · [[concepts/mots-cles-actionnels]] · [[concepts/product-led-seo]] · [[concepts/maillage-systeme]] · [[concepts/test-substitution-llm]]
