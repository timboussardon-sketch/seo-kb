---
type: register
title: "Résurgence — Grounding Score — 2026-06-12"
tags: [resurgence, revue-hebdo, grounding-score, geo]
created: 2026-06-12
updated: 2026-06-12
status: stable
---

# Résurgence — [[concepts/grounding-score]] — 2026-06-12

## Pourquoi celui-là

`updated: 2026-04-13`, soit 60 jours sans retouche. 100 backrefs dans `concepts.json` — à égalité avec [[concepts/surprise-gap]] comme hub le plus référencé du vault. C'est le claim le plus technique de la doctrine (similarité cosinus intention↔page) et le socle de l'hypothèse H-003 de [[hypotheses]]. Une seule résurgence passée ([[revue-hebdo/resurgence-2026-05-16|data-proprietaire, 2026-05-16]]), donc hors fenêtre des 8 semaines.

## État vs aujourd'hui

Le concept en est resté au stade spéculatif d'avril : définition canonique + extension Titans/MIRAS + limites honnêtes ("aucun benchmark empirique"). Depuis, la KB a bougé sur trois fronts qu'il ignore :

**1. La doctrine l'a opérationnalisé.** [[sources/2026-04-24-reflexion-organikk-4-piliers]] fait du Grounding Score le pilier 2 de la méthode Organikk, avec un protocole concret absent du concept : embedding via Gemini Embedding, méthode Triade SERP (top 3 → vecteur dominant + divergence contrôlée), framework 4 catégories d'entités (techniques / preuves / multimodal / divergence). [[sources/2026-04-24-cluster-business-organikk-4-piliers]] fixe même des KPI chiffrés (Grounding Score moyen cluster > 0,75 puis > 0,85) et un outil Do (`/outils/audit-grounding-score`). Le concept-hub ne pointe vers rien de tout ça.

**2. Deux sources externes le confirment.** [[sources/2026-04-15-opendecoder-seo-scoring-system]] : le S_Pertinence dominant du scoring LLM-as-Judge "c'est exactement le concept". [[sources/2026-04-25-scan-arxiv-25-avril]] (paper MAGEO) : la fidélité aux sources reste le critère de tri prioritaire des LLM — renforce le grounding comme métrique structurelle, pas comme proxy.

**3. Incohérence interne.** Le frontmatter dit `confidence: high`, la section Limites dit `confidence: medium`. Vu que H-003 est toujours `ouvert` (aucune fiche [[preuves/index|preuve]] adossée, le test corrélation score↔citations à 90j n'a pas tourné), c'est `medium` qui est défendable. `sources: 6` est aussi périmé : au moins 5 sources supplémentaires ont contribué depuis.

Pas de contradiction : rien dans [[contradictions]] n'attaque le concept, et aucune source ingérée ne l'infirme. Le wording respecte l'anti-AI-writing.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : ajouter une section "Opérationnalisation (méthode Organikk)" sourcée sur les 3 fiches 4-piliers (Gemini Embedding, Triade SERP, framework 4 catégories d'entités, KPI > 0,75) ; ajouter les 2 sources confirmantes (opendecoder, MAGEO) ; trancher le confidence à `medium` dans le frontmatter tant que H-003 reste `ouvert` ; passer `sources: 6` → `sources: 11` et `updated: 2026-06-12`
- [ ] À challenger : —
- [ ] Wording à corriger : —
