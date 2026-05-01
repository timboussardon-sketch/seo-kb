---
type: concept
title: Structural Information GEO (title, meta, headings, schema)
aliases: [structural-information-geo, schema-geo, title-meta-geo]
tags: [geo, schema-markup, title, meta, headings, structural, retrieval]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Structural Information GEO

**Finding clé** de [[sources/2026-04-13-sageo-arena-2025]] : **l'optimisation des champs structurels (title, meta, headings, schema) est le levier GEO le plus efficace au retrieval** — pas le body text.

## Les chiffres

Sur le benchmark SAGEO Arena (170 000 documents web) :

| Cible d'optimisation | Hit Rate retrieval | ΔRank |
|---|---|---|
| Body text seul | **−4.54** (dégrade !) | −16 % |
| Body text (AutoGEO rewrites longues) | −22.35 | −36 % |
| Structural info (title/meta/headings/schema) | **+22 %** | +2.72 |
| Structural info + Statistics Addition | **+35 %** Hit Rate | +4.30 |

**Optimiser seulement le body text dégrade** le retrieval dans toutes les stratégies testées (synonymes rares remplacent termes communs → chevauchement lexical BM25 diminue).

## Pourquoi les champs structurels dominent

1. **BM25 pondère fortement title/meta** au retrieval
2. **Les headings signalent la structure sémantique** au reranker
3. **Schema markup donne accès aux entités typées** (Product, Article, FAQPage, LocalBusiness…)
4. **Density sémantique** : title ≈ 10 mots porte autant de signal que 500 mots de body

## Doctrine Tim convergente

- Le skill `seo-brief-contenu` impose déjà Hn structurés et réponse directe
- Le skill `seo-entites-vectorielles` travaille les entités nommées — nourrit directement title + schema
- Le Schema.org est dans la checklist Règle 4 des prompts pSEO
- Les études de cas Lyon (serrurier / immo) de [[sources/2026-04-12-organikk-blog-scrape]] structurent déjà par cocons sémantiques Hn

## Application pratique

### Title
- Intégrer l'**entité cible** + un **chiffre** ou **modificateur de spécificité**
- Exemple : *"Calculateur budget séjour Bordeaux (appart-hôtel, 2026)"* > *"Séjour à Bordeaux"*

### Meta description
- Réponse directe à la requête (**answer-first** compact, cf. [[concepts/answer-first-pattern]])
- Inclure 1 chiffre sourcé si possible
- Respecter 155 caractères max

### Headings (H1-H3)
- H1 = promesse claire + entité + chiffre si pertinent
- H2 = sections qui répondent à une micro-intention distincte
- Éviter H2 vagues ("Conclusion", "Pour aller plus loin")

### Schema markup
- `Article` + `author` + `datePublished` minimum sur tout article
- `FAQPage` dès qu'il y a une section FAQ
- `Product` / `SoftwareApplication` / `LocalBusiness` selon le type
- `Dataset` si la page héberge une donnée chiffrée réutilisable

## Anti-pattern

- **Body text rewrites longues** (AutoGEO-style) → dilue la densité mots-clés, −22 % Hit Rate
- **Title vague** ("Le guide complet du SEO") → aucun signal pour le retrieval
- **Headings génériques** ("Introduction", "Conclusion") → perdent au reranking
- **Absence de schema** → entités non typées, retrieval sous-optimal

## Limites

- Finding validé sur corpus anglophone SAGEO Arena — à valider sur contenu français
- Le "Shopping" domain dégrade avec toutes les optimisations (paper précise) → pas universel
- BM25 est un retriever spécifique — d'autres retrievers (neural, hybrid) peuvent pondérer différemment
- Schema markup demande un dev / CMS capable — pas toujours trivial pour un site existant

## Pages liées

[[sources/2026-04-13-sageo-arena-2025]] · [[concepts/answer-first-pattern]] · [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/metriques-visibilite-geo]] · [[concepts/ingenierie-semantique-inversee]] · [[sources/2026-04-13-prompt-pseo-produit-service]]
