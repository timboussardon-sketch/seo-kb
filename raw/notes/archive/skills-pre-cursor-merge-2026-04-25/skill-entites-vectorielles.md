---
type: skill
source_type: doc-interne
title: "Skill : Entités Vectorielles SEO"
aliases: ["Entités vectorielles", "vecteurs sémantiques", "grounding-score-skill"]
tags: ["skill", "vecteurs-semantiques", "grounding-score", "embeddings", "nlp-seo"]
created: "2026-04-12"
updated: "2026-04-12"
sources: []
confidence: haute
status: actif
---

# Skill — Entités Vectorielles SEO

## Quand déclencher
Cartographier les entités sémantiques nécessaires pour qu'une page s'aligne mathématiquement avec l'intention de recherche ciblée.

> Trigger : "entités sémantiques", "vecteurs SEO", "[[grounding-score]]", "similarité cosinus", "quels termes inclure dans ma page", "optimisation sémantique", "NLP SEO".

## Concepts clés

- **[[grounding-score]]** (Similarité Cosinus) — mesure l'alignement entre le vecteur de la page et le vecteur de l'intention
- **Recherche vectorielle** (Muvera, etc.) — les moteurs comparent sémantiquement les pages aux requêtes via embeddings
- **[[surprise-gap]]** — éléments Haute Surprise qui forcent la mémorisation des modèles IA

## Pipeline (4 étapes)

1. **Définir la requête cible** — requête principale + type d'intention + niveau d'expertise audience
2. **Générer le tableau des entités** (10 termes/concepts par catégorie) :

| Entités Techniques | Preuves Quantitatives | Vecteurs Multimodaux | Divergence (Haute Surprise) |
|---|---|---|---|
| Termes obligatoires >80% top 10 | Statistiques sourcées au format [Chiffre+Unité+Contexte] | Formats attendus (images, outils, vidéos) | Concepts présents chez <10% des concurrents |

3. **Analyser le gap concurrentiel** — entités manquantes / opportunités de divergence / quick wins
4. **Recommandations d'implémentation** — où placer chaque entité (H1, corps, FAQ, sidebar)

## Règles par catégorie

**Preuves Quantitatives** — format obligatoire :
- ✅ "73% des entreprises B2B" / "ROI moyen de 4,2x sur 12 mois"
- ❌ "beaucoup d'entreprises" (non quantifié)

**Divergence (Haute Surprise)** — test :
- Si un concurrent peut copier le concept en 5 min → pas de Haute Surprise

## Output obligatoire

```
Analyse vectorielle — Requête : "[Requête]"
Intention : [Type]

| Entités Techniques | Preuves Quantitatives | Vecteurs Multimodaux | Divergence |
|---|---|---|---|

Gap concurrentiel :
- Manquant : ...
- Opportunité : ...
- Quick win : ...

Implémentation recommandée :
- H1/H2 : entités techniques principales
- Corps : preuves quantitatives contextualisées
- FAQ : éléments de divergence
```

## Règles absolues

- ❌ Entités listées artificiellement (keyword stuffing)
- ❌ Quantité > qualité d'intégration
- ✅ Mettre à jour régulièrement (les vecteurs évoluent)
- ✅ Toujours sourcer les preuves quantitatives

## Concepts liés

[[grounding-score]] · [[surprise-gap]] · [[vecteurs-semantiques]] · [[passage-ranking]] · [[e-e-a-t]]
