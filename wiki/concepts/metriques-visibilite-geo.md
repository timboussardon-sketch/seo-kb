---
type: concept
title: Métriques de visibilité GEO (Imp_wc, Imp_pos, Subjective Impression)
aliases: [metriques-visibilite-geo, imp-wc, imp-pos, pawc, subjective-impression]
tags: [geo, metriques, benchmark, aggarwal, visibilite, citation-ia]
created: 2026-04-13
updated: 2026-04-13
sources: 2
confidence: high
status: stable
---

# Métriques de visibilité GEO

Le ranking classique (position Google) ne mesure pas la visibilité dans les réponses génératives. [[sources/2026-04-13-geo-aggarwal-2024]] formalise 3 métriques spécifiques, reprises et étendues par [[sources/2026-04-13-sageo-arena-2025]].

## 1. `Imp_wc(c,r)` — Word Count Impression

Ratio du nombre de phrases de la réponse `r` qui citent la source `c` sur le total des phrases.

Plus une source est citée sur plusieurs phrases, plus elle est visible. Métrique simple, baseline.

## 2. `Imp_pos(c,r)` — Position-Adjusted Word Count (PAWC)

Identique à `Imp_wc` **mais avec pondération décroissante exponentielle selon la position** de la phrase dans la réponse.

Intuition : une citation au début de la réponse vaut plus qu'une citation en fin — l'utilisateur lit du haut vers le bas, les premières phrases sont extraites en Featured Snippet / AI Overview.

Aligne avec la règle "passage ancré 150-200 mots" des prompts pSEO Tim (cf. [[sources/2026-04-13-prompt-pseo-produit-service]] règle 7) et avec le **answer-first pattern** validé en A/B test prod par [[sources/2026-04-13-searchllm-2026]]. Cf. [[concepts/answer-first-pattern]].

## 3. Subjective Impression — 7 sous-métriques LLM-as-judge

Évaluées par GPT-4 via G-Eval, chaque citation notée sur :

1. Relative — pertinence vs requête
2. Influence — impact sur la réponse finale
3. Uniqueness — unicité du contenu apporté
4. Diversity — diversité des perspectives
5. Follow-up — probabilité de clic
6. Position — proéminence positionnelle
7. Count — nombre d'occurrences

Agrégées en Subjective Impression globale. Métrique plus fine mais coûteuse (1 call LLM par évaluation).

## Métriques étendues par SAGEO Arena

[[sources/2026-04-13-sageo-arena-2025]] ajoute des métriques par étape du pipeline :

- **Hit Rate** (retrieval) — le document cible est-il dans le top-100 BM25 ?
- **ΔRank** (retrieval / reranking / generation) — changement de position après optimisation
- **Cross-stage consistency** — maintien de la cohérence topique entre paragraphes

→ Mesure GEO complète = Aggarwal (métriques de citation finale) + Sageo (métriques par étape).

## Ranking classique ≠ GEO

| Ranking SEO classique | Métriques visibilité GEO |
|---|---|
| 1 URL = 1 position SERP | 1 URL peut être citée 0, 1 ou N fois dans une réponse |
| Position 1 domine | Position début de réponse + richesse de citation comptent |
| Un clic = un utilisateur | Visibilité = exposition même sans clic (réponse directe AI Overview) |
| CTR | Follow-up rate (probabilité clic après lecture citation) |

## Application pratique (brief contenu)

Quand on brief un article GEO-oriented :

1. **Réponse directe** dans les 2-3 premières phrases → maximise `Imp_pos` + Answer Firstness
2. **Densité de phrases citables** → maximise `Imp_wc` + Count
3. **Angle unique** → maximise Uniqueness
4. **Pertinence directe** à l'intention → Relative
5. **Markdown structuré** (Hn, schema) → maximise le retrieval via structural info (cf. [[concepts/structural-information-geo]])

## Limites

- Métriques proposées 2024-2025 — peuvent évoluer avec les générations successives de moteurs
- Subjective Impression coûteuse à reproduire (1 call GPT-4 par évaluation)
- Pas d'outil open-source grand public pour calculer ces métriques sur son propre site
- Pondération λ de `Imp_pos` non précisée dans le paper — à définir empiriquement

## Pages liées

[[sources/2026-04-13-geo-aggarwal-2024]] · [[sources/2026-04-13-sageo-arena-2025]] · [[entities/geo-bench]] · [[entities/sageo-arena-benchmark]] · [[concepts/information-gain]] · [[concepts/grounding-score]] · [[concepts/passage-ranking]] · [[concepts/answer-first-pattern]] · [[concepts/structural-information-geo]] · [[concepts/fully-meets]]
