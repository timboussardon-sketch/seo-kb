---
type: source
source_type: article
title: "L'étude qui nous dit comment être cité par les IA (Algorithme #3)"
aliases: [algorithme-etude-citation-ia]
tags: [newsletter-algorithme, geo, citation-ia, ai-overview, benchmark, e-e-a-t, source-secondaire]
created: 2026-04-12
updated: 2026-04-13
sources: 1
confidence: medium
status: stable
---

⚠️ **Source secondaire** : cette newsletter vulgarise le paper [[sources/2026-04-13-geo-aggarwal-2024]] (arxiv 2311.09735) mais les chiffres *"+41 % / +30 % / +30 %"* (citations / stats / autorité) sont **imprécis** par rapport au paper primaire. Chiffres exacts : Quotation +41 % / Statistics +34 % / Fluency +30 % / Cite Sources +29 % / Authoritative +13 %. Confidence downgradée medium.

# L'étude qui nous dit comment être cité par les IA

**Newsletter** : Algorithme #3 · **Date** : 6 mars 2026 · **Auteur** : Tim
**URL** : `https://algorithme.substack.com/p/letude-qui-nous-dit-comment-etre`
**Fichier raw** : `raw/articles/algorithme-etude-citation-ia.md`

## Données clés — LA source empirique

### Google March 2026 Core Update
- Qualité évaluée **au niveau du site**, pas juste page par page
- Contenus superficiels ou IA sans insight original → pénalisés
- Produire des études, tests, outils interactifs (quiz, simulateur)
- **"Information gain + content gap"** = le mantra

### Benchmark GEO (arxiv 2311.09735) — **10 000 requêtes, 25 domaines, 9 types**
- **+41 % visibilité** avec ajout de citations → [[concepts/information-gain]]
- **+30 % visibilité** avec ajout de statistiques
- **+30 % visibilité** avec ajout de sources d'autorité
- C'est **la donnée empirique** que [[concepts/surprise-gap]] attendait : la surprise informationnelle (citations, stats) a un effet mesurable sur la visibilité IA.

### Impact AI Overview sur Wikipedia (arxiv 2602.18455) — **161 382 articles**
- **-15 % trafic** en moyenne avec AI Overview
- Culture/lifestyle/société : **perte élevée** (requêtes simples → IA répond entièrement)
- Sciences/tech/médecine : **perte faible** (requêtes complexes → IA répond partiellement → clic)
- Confirme : contenu généraliste perd, contenu expert/niche résiste → [[concepts/surprise-gap]]
- "Moins de trafic, mais plus qualifié"

### Paradigme shift
- Avant : requête → liens → clic → site
- Après : requête → réponse IA → (parfois) clic → site
- Il faut créer du **contenu actionnel** et se préparer au **SEO agentique**

## Apports à la KB — source cruciale

- **Première donnée empirique** dans cette KB sur l'impact des stratégies de contenu sur la visibilité IA. Les +41/+30/+30 sont le benchmark de référence pour valider [[concepts/surprise-gap]] et [[concepts/information-gain]] quantitativement.
- Le split complexe/simple confirme l'architecture Titans : les queries complexes (High Surprise potentiel) conservent le clic, les queries simples (Low Surprise) sont absorbées par l'IA.
- Renforce [[concepts/weight-decay]] : le contenu statique simple est structurellement condamné à être absorbé par AI Overview.

## Limites

- L'étude arxiv:2311.09735 date de 2024 (Tim le note). Les métriques ont pu évoluer.
- L'étude Wikipedia (arxiv:2602.18455) est spécifique à Wikipedia — transférabilité aux sites commerciaux non garantie.
- Tim ne fournit pas les détails méthodologiques des deux études — juste les chiffres headline.

## Pages liées

[[concepts/information-gain]] · [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/weight-decay]] · [[concepts/grounding-score]] · [[concepts/data-proprietaire]]
