---
type: concept
title: Data propriétaire (le moat SEO/GEO)
aliases: [data-proprietaire, proprietary-data, donnees-proprietaires]
tags: [doctrine-tim, seo-ia, geo, data, strategie]
created: 2026-04-12
updated: 2026-05-16
sources: 25
confidence: high
status: stable
---

# Data propriétaire (le moat SEO/GEO)

Concept **transversal** dans les newsletters Algorithme de Tim. Cité dans 4 sources. C'est le moat compétitif pour le SEO post-IA.

> Sous test. `confidence: high` tient sur la convergence des sources, pas sur une preuve terrain. La forme falsifiable du moat est instrumentée depuis le 2026-05-16 : [[hypotheses#H-007]] `en-test`, fiche [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] (cohorte pSEO secteur×ville, jalons J+30 ≈ 2026-06-15 / J+90 ≈ 2026-08-14). Si la fiche tranche `non-concluante`, le `confidence:` de cette page baisse — c'est l'enjeu du hub le plus lourd du vault (98 backlinks).

## Définition

Une donnée propriétaire = un chiffre terrain, un résultat client, une observation unique, une mesure que **seul toi détiens**. Pas de la data scrapée, pas du contenu reformulé.

> "Aujourd'hui, ce qui compte, ce n'est pas de savoir rédiger. C'est d'apporter une information que les autres n'ont pas." [[sources/2026-03-04-algorithme-lancer-site-sans-cms]]

## Pourquoi c'est le moat

- L'IA a **déjà lu** tout le contenu générique → [[concepts/surprise-metric]] ≈ 0 pour les reformulations
- Les [[entities/quality-raters-guidelines]] p.42 pénalisent le contenu "sans effort" (note la plus basse) [[sources/2026-03-11-algorithme-data-claude-perplexity]]
- Le benchmark GEO (arxiv:2311.09735) montre que **citations (+41%), statistiques (+30%), sources d'autorité (+30%)** augmentent la visibilité IA [[sources/2026-03-06-algorithme-etude-citation-ia]] → pour avoir des stats uniques, il faut de la data propriétaire
- "Si je crée le même site que vous demain, sans expertise, je serai toujours derrière" — la data propriétaire crée un **avantage structurel non copiable**

## Types de data (classification Tim)

| Type | Exemples | Risque |
|---|---|---|
| **Données internes** | tarifs, services, procédures, résultats clients | Hallucination = fausse promesse commerciale. Validation par toi seul. |
| **Données externes** | météo, événements, distances, données sectorielles | Plus faciles à sourcer (API, .gouv, climate-data.org). Validation par source tierce. |

**Règle** : ne jamais mélanger la validation des deux types.

## Collecte et stockage

- NotebookLM, Gemini, Claude + APIs (Google, data.gouv…) pour agrégation
- Stocker dans un projet Claude ou NotebookLM pour réutilisation multi-articles
- Fact-checker systématiquement avant publication (prompt Perplexity fourni dans [[sources/2026-03-11-algorithme-data-claude-perplexity]])

## Connexion au Surprise Gap

[[concepts/surprise-gap]] = apporter l'info manquante qui force la mémorisation. La data propriétaire est **la matière première** de ce gap — c'est elle qui génère le gradient d'information suffisant ([[concepts/surprise-metric]]) pour que le modèle retienne ton contenu.

## Pages liées

[[sources/2026-04-30-tim-posts-linkedin-batch]] (5 types de data propriétaire formalisés : cas client chiffré, réflexion originale, méthodologie documentée, outil interactif, signaux sociaux) · [[sources/2026-04-30-fg-formation-pseo-cas-client]] (cas client B2B inversé : data inhérente à 10 ans d'accompagnement OF) · [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] (4 modèles pSEO 100 % APIs officielles) · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] (cluster qui matérialise la doctrine sur Organikk) · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] (article pilier — bannit "trafic" comme métrique) · [[sources/2026-04-15-opendecoder-seo-scoring-system]] (scoring 4 axes — S_Pertinence dominant) · [[sources/2026-04-15-scan-arxiv-15-avril]] (Retrieval Collapse NAVER : data propriétaire = signal humain non-fakeable) · [[sources/2026-04-25-scan-arxiv-25-avril]] (validation académique étendue) · [[sources/2026-04-22-algorithme-core-update-fermes-ia]] (−40 à −80 % sur sites IA industrialisés) · [[sources/2026-04-15-algorithme-listicles-chatgpt-30pct-baisse]] (densité de preuves > domain authority) · [[sources/2026-04-11-algorithme-linkedin-2e-source-ia]] (LinkedIn = signal humain prioritaire B2B) · [[sources/2026-04-13-victoria-garden-pseo]] (test substitution LLM = data propriétaire opérationnalisée en filtre binaire) · [[sources/2026-04-13-geo-aggarwal-2024]] (paper primaire benchmark — Quotation +41 %, Stats +34 %) · [[sources/2026-04-13-core-ranking-jin-2025]] (Review-based authentic narrative renverse le ranking en Top-1 80 %+ des cas) · [[sources/2026-04-13-raid-gseo-2025]] (intent-modeling côté créateur — 4W) · [[sources/2026-04-13-sageo-arena-2025]] (structural info = +22 % Hit Rate retrieval) · [[sources/2026-04-13-searchllm-2026]] (factual grounding = gate non-négociable en prod Xiaohongshu) · [[sources/2026-04-13-google-quality-raters-guidelines-2026]] (Experience pillar E-E-A-T) · [[sources/2026-04-13-semrush-llm-conversion-study]] (4x conversion LLM via contenu unique cité) · [[sources/2026-04-13-analyse-calls-prospects-bootcamp]] (argument vente data vs visibilité) · [[sources/2026-04-13-cas-clients-resultats]] (pivot closing 10→50% grâce à roadmap data) · [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]] · [[sources/2026-03-11-algorithme-data-claude-perplexity]] · [[sources/2026-03-06-algorithme-etude-citation-ia]] · [[sources/2026-03-04-algorithme-lancer-site-sans-cms]] · [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/information-gain]] · [[concepts/e-e-a-t]] · [[concepts/tabou-visibilite]] · [[concepts/answer-first-pattern]]
