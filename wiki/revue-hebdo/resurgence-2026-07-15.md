---
type: register
title: "Résurgence — information-gain — 2026-07-15"
aliases: [resurgence-information-gain-2026-07-15]
tags: [resurgence, geo, information-gain, revue-hebdo]
created: 2026-07-15
updated: 2026-07-15
sources: 3
confidence: high
status: stable
---

# Résurgence — [[concepts/information-gain]] — 2026-07-15

## Pourquoi celui-là

`updated: 2026-04-13` — pas touché depuis 93 jours. Hub lourd : 66 backrefs, 14 outlinks (3e concept le plus référencé du vault après [[concepts/agentic-search]] et [[concepts/aeo]]). Jamais ressorti en résurgence : les trois dernières éditions ont pondéré vers [[concepts/surprise-gap]] (2026-06-24), [[concepts/grounding-score]] (2026-06-12), [[concepts/data-proprietaire]] (2026-05-16). C'est le pilier "standard/mesurable" de la doctrine GEO — celui qu'il est le plus coûteux de laisser adossé à une seule source de 2024.

## État vs aujourd'hui

Le concept s'appuie **exclusivement** sur le paper KDD '24 [[sources/2026-04-13-geo-aggarwal-2024]] (GEO-Bench, PAWC : Quotation +41 %, Statistics +34 %, Authoritative +13 %). Sa propre section Limites le dit : *"l'étude arxiv:2311.09735 date de 2024 — les métriques peuvent avoir évolué"*. Depuis avril, trois sources ingérées le confrontent :

1. **Corroboration directe des chiffres dans le contenu publié de Tim.** [[sources/2026-06-02-algorithme-geo-pas-un-scam]] cite *"+41 % de visibilité avec des verbatims sourcés, +34 % avec des statistiques"*. C'est exactement la version **corrigée** du concept (Quotation Addition +41 %, Statistics Addition +34 %), pas la version erronée de la newsletter #3 (+41/+30/+30 pour citations/stats/autorité). La correction que le concept documente a bien migré dans le contenu public. Le wording, lui, dit "visibilité" — [[concepts/tabou-visibilite]] impose "citations IA".

2. **Recoupement par un benchmark 2026 non lié au concept.** [[sources/2026-06-05-algorithme-fin-des-backlinks-llms]] (GEO Benchmark 2026 de ConvertMate) apporte des métriques fraîches qui prolongent le finding "Authoritative ne fait que +13 %" : corrélation backlinks ↔ citation LLM **r = 0,18** vs pertinence sémantique **r = 0,87** (~4× plus déterminante), multimodal **+156 %**, contenu < 3 mois cité **3×** plus. Même direction que Aggarwal (l'autorité/les liens pèsent peu, la matière sémantique et la donnée pèsent), mais data 2026 et non citée dans la page.

3. **Extension conceptuelle.** [[sources/2026-07-08-algorithme-redaction-claude]] pose que *"un modèle régresse vers la moyenne : un texte qui sonne IA est le moins surprenant, donc le moins citable"* — pont explicite information-gain ↔ [[concepts/surprise-gap]] ↔ [[concepts/anti-ai-writing]], déjà cousu dans la section Relations mais sans cette formulation opérationnelle.

Aucune contradiction. Le cœur du concept tient — il est même **doublement confirmé** (chiffres repris correctement en prod + direction recoupée par un benchmark 2026). Le seul vrai drift est de **sourcing** : un hub GEO de 66 backrefs qui repose sur une seule étude de 2024 alors que le vault contient désormais une corroboration 2026 non liée.

## Verdict proposé pour la revue hebdo

- [x] **À mettre à jour** :
  1. Ajouter une sous-section "Corroboration 2026" citant [[sources/2026-06-05-algorithme-fin-des-backlinks-llms]] (r = 0,18 backlinks vs 0,87 sémantique, multimodal +156 %, fraîcheur 3×) comme prolongement du finding Authoritative +13 %, avec `sources: 6 → 7`, `updated: 2026-07-15`.
  2. Lier [[sources/2026-06-02-algorithme-geo-pas-un-scam]] comme point de contrôle : les chiffres corrigés (+41 % / +34 %) sont bien repris en prod — la correction du concept a tenu, rien à re-corriger côté données.
  3. Micro-fix wording : remplacer "visibilité" (ligne Limites) par "citations IA" ([[concepts/tabou-visibilite]]).

Exécution : un ingest léger ou le skill `hypotheses-validation`, pas ici. La résurgence prépare, la revue hebdo tranche.
