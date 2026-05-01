---
type: concept
title: Confidence Score (AI Overviews)
aliases: [confidence-score, score-confiance-aio]
tags: [geo, ai-overviews, ranking, verification]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: medium
status: evolving
---

# Confidence Score (AI Overviews)

Score interne de Google [[entities/sge|AI Overviews]] déterminant si un résumé IA est suffisamment soutenu par des sources vérifiables pour être affiché.

## Ce que cette KB sait

- Google ne génère un AI Overview que si le Confidence Score dépasse un seuil interne (non public)
- Le score mesure la **convergence des sources** : plus les top-résultats convergent sur une réponse, plus le score est élevé
- Les requêtes YMYL (Your Money Your Life) ont un seuil plus élevé → moins d'AI Overviews sur la santé, la finance, le juridique
- Si les sources se contredisent, le Confidence Score chute → pas d'AI Overview affiché

## Pertinence SEO/GEO

- **Pour être cité dans un AI Overview**, le contenu doit être aligné avec le consensus (80%) ET apporter un élément différenciant vérifiable (20%)
- Le [[concepts/grounding-score]] est le mécanisme côté contenu : plus le contenu est ancré dans des faits vérifiables, plus il contribue au Confidence Score global
- Le fact-checking (pipeline Grok + Perplexity, cf. blog organikk.co/blog/grok-seo-pipeline-data) produit des données avec un haut Confidence Score
- Connexion directe avec [[concepts/e-e-a-t]] : les signaux de confiance (auteur identifié, sources citées, date à jour) augmentent la probabilité que Google retienne le contenu comme source fiable

## Implication pratique

Quand Tim recommande le double fact-check (Grok + Perplexity) avec classification ✅/⚠️/❌, il optimise directement le Confidence Score : seules les données ✅ Vérifiées entrent dans le contenu final.

## Pages liées

[[entities/sge]] · [[concepts/grounding-score]] · [[concepts/e-e-a-t]] · [[concepts/data-proprietaire]] · [[concepts/information-gain]]
