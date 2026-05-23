---
type: concept
title: "Entités vectorielles — cartographier le vecteur sémantique d'une page"
aliases: [entites-vectorielles, entites-semantiques, vecteurs-semantiques, cartographie-entites-vectorielles]
tags: [doctrine-tim, geo, aeo, embedding, grounding-score, nlp-seo, redaction]
created: 2026-05-21
updated: 2026-05-21
sources: 1
confidence: high
status: stable
---

# Entités vectorielles

Cartographie des entités sémantiques qu'une page doit contenir pour que son vecteur s'aligne mathématiquement avec le vecteur de l'intention de recherche ciblée. C'est la matière première de l'optimisation par [[concepts/grounding-score|similarité cosinus]] : on ne vise plus une densité de mots-clés, on construit un nuage d'entités qui rapproche la page du barycentre attendu par Google et les moteurs de réponse. Opérationnalisé par le skill `seo-entites-vectorielles`.

## Les 4 catégories d'entités

Toute analyse vectorielle d'une requête produit un tableau à 4 colonnes, 10 entités par colonne :

1. **Entités techniques (vecteurs de base)** — le vocabulaire obligatoire du champ lexical, présent chez plus de 80 % des pages du top 10. Sans elles, la page n'est même pas jugée pertinente. C'est le socle qui fait passer la Phase 1 [[concepts/triade-serp|Document Ranking]].
2. **Preuves quantitatives (entités numériques)** — chiffres sourcés, benchmarks, fourchettes. Elles augmentent le [[concepts/confidence-score]] de l'IA. Format : `[chiffre] + [unité] + [contexte]`, jamais « beaucoup ».
3. **Vecteurs multimodaux** — les formats attendus par l'intention (schémas, outils interactifs, vidéos, tableaux, téléchargeables). Une intention « Do » sans format interactif a un vecteur incomplet. Cf. [[concepts/product-led-seo]].
4. **Éléments de divergence (Haute Surprise)** — concepts experts présents chez moins de 10 % des concurrents. Ils forcent la mémorisation du modèle. Test : si un concurrent les copie en 5 minutes, ce n'est pas de la Haute Surprise. Cf. [[concepts/surprise-gap]].

## Pourquoi ça compte

Les moteurs modernes comparent les pages aux requêtes via des embeddings, pas par correspondance lexicale ([[entities/muvera]], [[entities/dpr]]). Une page dont le vecteur reste générique = même vecteur que tout le monde = invisible dans la SERP. La divergence (catégorie 4) éloigne le vecteur du corpus moyen ; les entités techniques (catégorie 1) le gardent dans la zone de pertinence. L'optimisation consiste à tenir les deux à la fois.

## Articulation avec la doctrine

- **Vs [[concepts/grounding-score]]** — les entités vectorielles sont les leviers concrets qui font monter le Grounding Score d'une page.
- **Vs [[concepts/surprise-gap]]** — la 4ᵉ catégorie (divergence) est la traduction opérationnelle du Surprise Gap au niveau des entités.
- **Vs le brief éditorial** — le tableau d'entités alimente le brief : où placer chaque entité (H1, corps, FAQ, CTA).
- **Vs [[concepts/passage-ranking]]** — chaque H2 est un vecteur évalué séparément ; les entités se répartissent par passage.
- **Vs [[concepts/data-proprietaire]]** — les preuves quantitatives et la divergence viennent de la data propriétaire, pas des outils SEO.

## Implémentation par zone de page

- **H1 / H2** — entités techniques principales
- **Corps** — preuves quantitatives contextualisées
- **Sidebar / CTA** — vecteurs multimodaux (outils interactifs)
- **FAQ** — éléments de divergence

Règle : intégration naturelle, jamais de keyword stuffing. La qualité de l'intégration prime sur le nombre d'entités.

## Pages liées

[[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/confidence-score]] · [[concepts/triade-serp]] · [[concepts/passage-ranking]] · [[concepts/product-led-seo]] · [[concepts/data-proprietaire]] · [[concepts/information-gain]] · [[entities/muvera]] · [[entities/dpr]]
