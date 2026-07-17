---
type: concept
title: Information Gain (standard Google + benchmark GEO)
aliases: [information-gain, gain-information]
tags: [seo, geo, quality-raters, benchmark, ranking, aeo]
created: 2026-04-12
updated: 2026-07-17
sources: 7
confidence: high
status: stable
---

# Information Gain (standard Google + benchmark GEO)

Le standard officiel Google pour évaluer la valeur ajoutée d'un contenu. Confirmé par le QRG p.42 et quantifié par un benchmark GEO. C'est la version **mesurable** et **standard** de ce que [[concepts/surprise-gap]] théorise via l'architecture Titans.

## Définition (QRG + Tim)

Un contenu apporte un "information gain" quand il **ajoute quelque chose que le corpus existant n'a pas** : un chiffre, un fait vérifié, un angle unique, une donnée terrain. Le contraire = contenu "sans effort" ([[entities/quality-raters-guidelines]] p.42) qui reprend mécaniquement des infos existantes → note la plus basse.

## Le benchmark — source primaire [[sources/2026-04-13-geo-aggarwal-2024]]

Paper KDD '24, arxiv 2311.09735 — benchmark GEO-Bench de **10 000 requêtes, 25 domaines, 9 types de requêtes**. Baseline "No Optimization" = 19.3 sur Position-Adjusted Word Count (PAWC).

**Chiffres exacts du paper** (≠ chiffres imprécis cités précédemment via source secondaire [[sources/2026-03-06-algorithme-etude-citation-ia]]) :

| Méthode | PAWC | Gain vs baseline |
|---|---|---|
| **Quotation Addition** (citations verbatim) | 27.2 | **+41 %** |
| Statistics Addition | 25.9 | **+34 %** |
| Fluency Optimization | 25.1 | +30 % |
| **Cite Sources** (ajout de sources) | 24.9 | **+29 %** |
| Technical Terms | 23.1 | +20 % |
| Easy-to-Understand | 22.2 | +15 % |
| **Authoritative** | 21.8 | **+13 %** |

**Correction importante** : la newsletter Algorithme #3 citait *"+41 % / +30 % / +30 %"* pour citations / stats / autorité. En réalité le **+41 %** correspond à **Quotation Addition** (citations verbatim — extraire une phrase d'une source dans sa réponse), pas à Cite Sources (qui fait +29 %). Authoritative ne fait **que +13 %**, pas +30 %.

### Méthodes qui dégradent

- **Keyword Stuffing** : **−8 % PAWC** sur GEO-Bench, **−9 %** sur Perplexity.ai en production. Contreproductif — confirme la doctrine [[concepts/anti-ai-writing]].
- Unique Words : +7 % (marginal).

### Combinaison optimale

**Fluency + Statistics** = +5.5 % au-dessus de toute stratégie single. Sur Perplexity in the wild, Statistics donne **+37 %** en Subjective Impression (c'est le "+37 %" de l'abstract).

### Finding démocratisation

Les sites bas-ranking gagnent massivement, les sites top-1 perdent :

| Méthode | Rank 1 | Rank 5 |
|---|---|---|
| Cite Sources | −30.3 % | +115.1 % |
| Quotation Addition | −22.9 % | +99.7 % |
| Statistics Addition | −20.6 % | +97.9 % |

→ GEO = levier anti-monopole pour petits sites.

### Corroboration 2026

Le benchmark primaire date de 2024. Un second benchmark, le GEO Benchmark 2026 de ConvertMate [[sources/2026-06-05-algorithme-fin-des-backlinks-llms]], mesure sur de la data fraîche et prolonge le finding « Authoritative ne fait que +13 % » : la corrélation entre backlinks et citation LLM tombe à r = 0,18, contre r = 0,87 pour la pertinence sémantique — environ 4× plus déterminante. Il ajoute deux leviers absents du paper de 2024 : le multimodal (+156 %) et la fraîcheur (un contenu de moins de 3 mois est cité 3× plus, ce qui recoupe [[concepts/weight-decay]]).

Les deux études sont indépendantes et pointent dans la même direction : l'autorité et les liens pèsent peu, la matière sémantique et la donnée pèsent. C'est la corroboration qui manquait à un concept adossé à une seule source.

Point de contrôle côté production : [[sources/2026-06-02-algorithme-geo-pas-un-scam]] reprend les chiffres du benchmark sous leur forme **corrigée** (+41 % Quotation Addition, +34 % Statistics Addition), pas sous la forme erronée de la newsletter #3. La correction documentée sur cette page a bien migré dans le contenu publié — rien à re-corriger côté données.

## Forme atomique

L'IA vérifie les claims par **atomisation** : chaque affirmation est découpée en fait isolé et vérifié indépendamment [[sources/2026-03-11-algorithme-data-claude-perplexity]].

Exemple Tim : "La Tesla Model S a une autonomie de 600 km et coûte 90 000 €" → 3 atomes vérifiés séparément (modèle, autonomie, prix). Écrire "La Tesla est une voiture chère avec une bonne autonomie" → **pas cité** (pas assez atomique).

## Relation aux autres concepts

- **[[concepts/surprise-gap]]** = l'interprétation Tim/Titans de l'information gain : l'info manquante qui force la mise à jour des poids
- **[[concepts/surprise-metric]]** = le mécanisme architectural qui rend l'information gain mesurable par le modèle
- **[[concepts/data-proprietaire]]** = la matière première de l'information gain (sans data unique, pas de gain)

L'information gain est le **concept standardisé** (Google QRG, étude académique). Le Surprise Gap est le **concept doctrinal** (Tim, via Titans). Ils décrivent le même phénomène sous deux angles.

## Limites

- L'étude arxiv:2311.09735 date de 2024 — les métriques peuvent avoir évolué. Atténué depuis le 2026-07-17 : le GEO Benchmark 2026 recoupe la direction du finding (section Corroboration 2026), sans rejouer le protocole
- Le benchmark couvre les citations IA dans les réponses génératives, pas le ranking Google classique
- LLM-as-judge (G-Eval) = variance admise par les auteurs
- Top 5 sources seulement par requête, corpus anglais majoritaire
- Les gains dépendent fortement du **domaine** (Law & Gov aime Authoritative, Business aime Fluency, etc.) — pas de règle universelle

## Pages liées

[[sources/2026-04-13-geo-aggarwal-2024]] (source primaire paper) · [[sources/2026-04-13-google-quality-raters-guidelines-2026]] (source primaire QRG) · [[sources/2026-03-06-algorithme-etude-citation-ia]] (source secondaire newsletter avec chiffres imprécis) · [[sources/2026-03-11-algorithme-data-claude-perplexity]] · [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]] · [[sources/2026-03-13-algorithme-agents-seo-consultants]] · [[entities/geo-bench]] · [[entities/quality-raters-guidelines]] · [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/data-proprietaire]] · [[concepts/metriques-visibilite-geo]] · [[concepts/answer-first-pattern]] · [[sources/2026-06-05-algorithme-fin-des-backlinks-llms]] (corroboration 2026) · [[sources/2026-06-02-algorithme-geo-pas-un-scam]] (point de contrôle production)
