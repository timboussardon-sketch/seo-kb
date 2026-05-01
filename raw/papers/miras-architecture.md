# MIRAS : Multi-Resolution Adaptive Summarization

## Référence
- Auteurs : Équipes de recherche IA (Google / affiliés)
- Date : 2024-2025
- Source : Publication recherche
- Lien : non disponible

## Résumé
- Extension des architectures type Titans pour le traitement de contenu à résolutions multiples
- Permet aux LLM de résumer et prioriser le contenu à différents niveaux de granularité
- Connexion avec le **Passage Ranking** : chaque section (H2) est évaluée indépendamment comme un vecteur sémantique
- Optimise le **Grounding Score** en permettant un matching plus fin entre intention de requête et segments de contenu
- Renforce l'importance de la structure du contenu (hiérarchie Hn) pour le référencement IA

## Concepts clés extraits
- [[passage-ranking]] — classement par passage individuel, H2 = vecteur sémantique
- [[grounding-score]] — matching cosine query ↔ page, affiné par résolution multiple
- [[ingenierie-semantique-inversee]] — reverse engineering de la structure documentaire

## Pertinence pour la KB
Complète la compréhension de comment les LLM traitent les contenus longs. Justifie l'approche de Tim sur les briefs de contenu structurés (chaque H2 doit porter un vecteur sémantique distinct, au moins un H2 doit créer un Surprise Gap). Renforce la doctrine : la structure du contenu est aussi importante que le contenu lui-même.

## Citations dans la KB
- raw/notes/seo-ia-tim.md
- wiki/concepts/passage-ranking.md
- wiki/concepts/grounding-score.md
