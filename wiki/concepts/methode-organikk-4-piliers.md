---
type: concept
title: "Méthode Organikk — 4 piliers (Surprise / Grounding / pSEO / AEO)"
aliases: [methode-organikk-4-piliers, framework-organikk, 4-piliers-organikk]
tags: [doctrine-tim, organikk, framework, surprise-gap, grounding-score, pseo, aeo, umbrella]
created: 2026-05-01
updated: 2026-05-01
sources: 3
confidence: high
status: stable
---

# Méthode Organikk — 4 piliers

Concept umbrella qui formalise la **doctrine SEO/AEO Organikk** comme un système cohérent à 4 piliers + 6 interconnexions + matrice skills + cadre de décision séquentiel.

## Les 4 piliers

| # | Pilier | Question | Concept lié | KPI |
|---|---|---|---|---|
| 1 | **Surprise Gap** | *Pourquoi on lit* | [[concepts/surprise-gap]] | Surprise Score par passage / page |
| 2 | **Grounding Score** | *Pourquoi on rank* | [[concepts/grounding-score]] | Grounding Score vs top 3 SERP |
| 3 | **pSEO** | *Comment on scale* | [[concepts/programmatique-pseo]] | Pages indexées / créées > 85 % |
| 4 | **AEO** | *Comment on gagne les moteurs de réponse* | [[concepts/aeo]] | Taux de citation dans réponses génératives |

## Pyramide d'exécution

```
            AEO (architecture)
           ↑
     pSEO (scale)
    ↑
  GROUNDING (pertinence)
 ↑
SURPRISE (fondation)
```

**Règle de dépendance stricte** :
- Sans **Surprise** → pages pertinentes mais génériques, ignorées par les LLM
- Sans **Grounding** → pSEO produit du thin → pénalités
- Sans **pSEO** → AEO ne couvre pas l'étendue de l'intention
- Sans **AEO** → tout le reste reste du SEO classique → invisible en Agentic Search

## 6 interconnexions

| Croisement | Produit |
|---|---|
| Surprise × Grounding | Contenu différenciant ET extractible |
| Surprise × pSEO | Anti-thin content par design |
| Surprise × AEO | Citation préférentielle par les LLM |
| Grounding × pSEO | Pertinence vectorielle garantie à l'échelle |
| Grounding × AEO | Alignement sur l'intention à chaque niveau du cluster |
| pSEO × AEO | Scalabilité × couverture MECE des intentions |

## Cadre de décision (par où commencer un audit)

1. **Audit Grounding** → s'aligne avec l'intention ? (`seo-entites-vectorielles`)
2. **Audit Surprise** → angle unique vs SERP ? (`seo-workflow-article`, étape 1)
3. **Audit AEO** → citable par un LLM ? (bloc authorship, passage ranking)
4. **Audit pSEO** → scalable ce format ? (`seo-programmatique-pseo`)

Toujours dans cet ordre. Fondation (Surprise + Grounding) avant scalabilité (pSEO + AEO).

## Cas d'application

- Cluster sémantique Organikk ([[sources/2026-04-24-cluster-business-organikk-4-piliers]]) — 16 pages satellites + 3 commerciales + roadmap 90j organisées par les 4 piliers
- 4 modèles pSEO data-driven ([[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]]) — implémentent le pilier 3 (pSEO) avec garde-fous Surprise + Grounding
- Article pilier `process-seo-b2b-2026` ([[sources/2026-04-17-organikk-process-seo-b2b-2026]]) — opérationnalise les 4 piliers en process B2B 2400 mots
- Process KW research 5 étapes ([[syntheses/process-keyword-research-5-etapes]]) — pipeline outillé Keyword Planner → GSC → Grok → propriétaires → pSEO, sous le contrôle des 4 piliers

## Articulation avec la doctrine globale

- Cohérent avec [[syntheses/doctrine-seo-post-sge]] (4 piliers : grounding score, surprise gap, information gain, data propriétaire) — la méthode Organikk est l'**opérationnalisation skills** de cette synthèse
- Le pilier "data propriétaire" de la synthèse est ici **transversal** aux 4 piliers (alimente Surprise + Grounding + pSEO + AEO)
- Le cadre de décision séquentiel inverse la logique commerciale typique : on ne commence pas par "comment scaler", on commence par "est-ce que ça mérite d'exister"

## Pages liées

[[sources/2026-04-24-reflexion-organikk-4-piliers]] · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] · [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/programmatique-pseo]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[concepts/agentic-search]] · [[syntheses/doctrine-seo-post-sge]] · [[entities/organikk-co]]
