---
type: source
source_type: article
title: Scrape glossaire Organikk.co — 78 termes SEO/GEO/LLM (2026-04-12)
aliases: [organikk-glossaire, glossaire-organikk, glossaire-seo-tim]
tags: [organikk, glossaire, terminologie, seo, geo, llm, reference-publique]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Scrape glossaire Organikk.co — 78 termes SEO/GEO/LLM

**Auteur** : Timothée Boussardon (organikk.co/glossaire)
**Type** : glossaire publié (`source_type: article`)
**Fichier raw** : `raw/data/organikk-glossaire-scrape-2026-04-12.md`
**Date scrape** : 2026-04-12

---

## Contexte

78 définitions publiées par Tim. Sert de **source normative publique** pour la terminologie SEO/GEO/LLM de la KB — permet de vérifier la cohérence entre définitions internes et version publique. Overlap massif avec les concepts et entities déjà créés.

## Mapping glossaire → KB existante

### Concepts déjà couverts en wiki (avec page dédiée)

| Terme glossaire | Page KB |
|---|---|
| AEO | [[concepts/aeo]] |
| E-E-A-T | [[concepts/e-e-a-t]] |
| GEO | (dans §4.2 AGENTS, couvert transversalement par [[concepts/aeo]] + [[syntheses/doctrine-seo-post-sge]]) |
| Grounding Score | [[concepts/grounding-score]] |
| Surprise Metric | [[concepts/surprise-metric]] |
| Weight Decay | [[concepts/weight-decay]] |
| Passage Ranking | [[concepts/passage-ranking]] |
| Reciprocal Rank Fusion (RRF) | [[concepts/rrf]] |
| Triade SERP | [[concepts/triade-serp]] |
| Confidence Score | [[concepts/confidence-score]] |
| Featured Snippet / Position zéro | absorbé par [[concepts/passage-ranking]] |

### Entities déjà couvertes

| Terme glossaire | Page KB |
|---|---|
| Titans (architecture) | [[entities/titans]] |
| MIRAS | [[entities/miras]] |
| Neural Memory (Titans) | (dans [[entities/titans]] structure 3 couches) |
| BM25 | [[entities/bm25]] |
| DPR | [[entities/dpr]] |
| Muvera | [[entities/muvera]] |
| ISI | [[entities/isi]] |

### Termes glossaire non encore créés en KB (candidats futurs)

- **Perplexity AI** — cité dans glossaire avec "> 15 M requêtes/jour, cite sources avec liens". Candidat à entité Concepts-marque. Pas prioritaire tant que pas de source primaire dédiée.
- **HCU (Helpful Content Update)** — 2022-2023, cible contenus "créés pour les moteurs". Candidat Algos Google.
- **Knowledge Graph personnel** (concept Tim) — ensemble entités/faits/relations publiés sur ses propres canaux. Candidat concept.
- **Topical Authority** — cité dans skills cluster-aeo mais pas de page concept dédiée.
- **Entity SEO** / **Embedding** / **Similarité cosinus** — termes vectoriels de base, couverts transversalement par [[concepts/grounding-score]] et [[concepts/ingenierie-semantique-inversee]].
- **AI Overviews 40 % clics** : chiffre du glossaire à croiser avec [[sources/2026-02-27-algorithme-youtube-ai-overviews]]
- **Fraîcheur sémantique / Freshness Score** : Tim les définit publiquement — à rapprocher de [[concepts/weight-decay]] (mécanisme architectural) et du biais de récence

## Cohérence définitionnelle (vérifications clés)

### Grounding Score

- **Glossaire Tim** : *"similarité cosinus entre le vecteur d'une requête et le vecteur d'un passage de contenu"*
- **AGENTS.md §4.2** : *"similarité cosinus entre le vecteur d'intention d'une requête et le vecteur d'une page"*
- **[[concepts/grounding-score]]** : reprend AGENTS.md + ajoute extension MIRAS multi-résolution
- **Cohérence** : oui. Léger affinement "passage" (glossaire) vs "page" (AGENTS) — le glossaire est plus précis (aligné sur [[concepts/passage-ranking]] / [[entities/miras]]).

### Surprise Metric

- **Glossaire** : *"mesure de la nouveauté informationnelle d'un contenu selon l'architecture Titans/MIRAS"*
- **[[concepts/surprise-metric]]** : gradient d'information, détail mécanique + interprétation SEO Tim
- **Cohérence** : oui, la définition publique est une version synthétique.

### MIRAS

- **Glossaire** : *"Cadre théorique de Google DeepMind généralisant les architectures de mémoire long-terme pour les LLMs"*
- **[[entities/miras]]** : Multi-Resolution Adaptive Summarization, extension Titans
- **Divergence mineure** : le raw paper MIRAS parle de multi-résolution ; le glossaire met l'accent sur "mémoire long-terme". À surveiller — peut-être que le glossaire simplifie pour un public non-expert.

## Chiffres notables du glossaire

- **AI Overviews** = *"jusqu'à 40 % des clics"* (glossaire, non sourcé)
- **Perplexity AI** = *"plus de 15 M requêtes/jour"* (glossaire, non sourcé)
- **Redirect 301** = *"transfère 90-99 % de l'autorité"* (glossaire, non sourcé)

→ Ces chiffres sont publics mais **sans source primaire dans le glossaire** : à flagger si jamais utilisés dans un brief → il faut une source externe confirmante.

## Usage prescrit

1. **Lint terminologique** : si une page wiki emploie un terme du glossaire, vérifier qu'elle n'entre pas en contradiction avec la définition publique de Tim.
2. **Backlink naturel** : Tim peut linker organikk.co/glossaire#<terme> depuis ses briefs / articles publiés, renforçant la cohérence de marque.
3. **Gaps à combler** : les 7-8 termes non encore créés en KB (Perplexity, HCU, Topical Authority, Knowledge Graph personnel) sont des TODO pour de futurs ingests de sources primaires.

## Limites

- **Glossaire auto-sourcé** : les définitions reflètent le point de vue de Tim, pas un consensus académique
- **Chiffres non sourcés dans le glossaire** (40 % AI Overviews, 15 M Perplexity, 90-99 % 301)
- **Scrape d'un état figé** (2026-04-12) — le glossaire évoluera

## Pages liées

**Entity** : [[entities/organikk-co]]

**Sources** : [[sources/2026-04-12-organikk-blog-scrape]]

**Concepts majeurs** (définitions cohérentes vérifiées) : [[concepts/grounding-score]] · [[concepts/surprise-metric]] · [[concepts/weight-decay]] · [[concepts/passage-ranking]] · [[concepts/triade-serp]] · [[concepts/aeo]] · [[concepts/e-e-a-t]] · [[concepts/rrf]] · [[concepts/confidence-score]]

**Entities** (architectures/outils confirmés) : [[entities/titans]] · [[entities/miras]] · [[entities/bm25]] · [[entities/dpr]] · [[entities/muvera]] · [[entities/isi]]
