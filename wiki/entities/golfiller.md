---
type: entity
title: "Golfiller (golfiller.fr)"
aliases: [golfiller, golfiller.fr]
tags: [cas-seo, pseo, product-led, e-commerce, sans-backlink]
created: 2026-06-06
updated: 2026-06-06
sources: 0
confidence: medium
status: stable
---

# Golfiller (golfiller.fr)

Site e-commerce de balles de golf d'occasion. Sert de cas de référence interne pour la combinaison [[concepts/programmatique-pseo]] + Product-Led SEO : le site se classe en tête sur la requête « balle de golf » devant des acteurs majeurs (type Décathlon, Amazon) sans achat de lien.

## Pourquoi c'est un cas étudié

- **pSEO sur catalogue** : des pages générées à partir des variables produit (marque, modèle, état, lot) qui captent la longue traîne transactionnelle, selon les modèles décrits dans [[concepts/pseo-data-driven-models]].
- **Product-Led** : la valeur d'usage (stock réel, tri par état, prix au lot) tient lieu de contenu et obtient la pertinence transactionnelle, plutôt qu'un blog éditorial.
- **Sans backlink acheté** : la position se gagne par densité sémantique et adéquation à l'intention, pas par netlinking.

Cas mobilisé dans [[syntheses/audit-doctrine-2026]] comme preuve terrain de la doctrine pSEO + Product-Led.

## Liens

- [[methodes/ranker-verticale-niche-sans-backlink]] — la méthode générale extraite de ce cas (verticale défendable + pSEO + Do-intent + Product-Led, sans backlink).
- [[golfiller-strat]] — la note brute de stratégie et l'analyse GSC du site.
- [[golfiller-conversations]] — le log de travail brut d'où la réflexion est tirée.
- [[concepts/product-led-seo]] — le levier qui transforme la page Do en outil et porte le ranking.

## Articles produits

- « Balle de golf pour la distance » (template usage) — brief [[briefs/2026-06-10-balle-golf-distance]], draft markdown + version HTML/CSS prête à coller (Shopify) dans `content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.{md,html}`. Data : table distance/vitesse + prix catalogue réels.
- Set « modèle directory usage/besoin » complet en HTML/CSS prêt Shopify : distance, contrôle, vent, durabilité, budget (`content-brain/golfiller/outputs/2026-06-10-balle-golf-*.html`). Sélection catalogue réelle par besoin, CSS scopé `.gf-article`, cross-links anti-cannibalisation.
