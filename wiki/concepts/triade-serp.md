---
type: concept
title: Triade SERP
aliases: [triade-serp, 3-phases-serp, document-passage-generation]
tags: [ranking, serp, passage-ranking, document-ranking, geo]
created: 2026-04-12
updated: 2026-04-12
sources: 2
confidence: high
status: stable
---

# Triade SERP

Modèle propriétaire de Tim décrivant les 3 phases de sélection et d'affichage d'un résultat dans les SERP Google en 2026. Présenté dans l'article "Ma stratégie SEO du moment" (organikk.co/blog/ma-strategie-seo-du-moment).

## Les 3 phases

### Phase 1 — Document Ranking
Sélection d'un sous-ensemble de documents parmi l'index Google en fonction de :
- **Autorité du domaine** (PageRank, backlinks, historique)
- **Pertinence macro** (title, H1, URL, premier paragraphe contiennent le mot-clé)
- C'est le "filtre d'admission" : si le document ne passe pas cette phase, rien d'autre ne compte
- Mécanisme sous-jacent : [[entities/bm25]] + [[entities/rankbrain]]

### Phase 2 — Passage Ranking
Évaluation de chaque passage individuellement pour sa **densité sémantique** :
- Chaque bloc H2 (150-200 mots) est un vecteur sémantique évalué séparément
- Un article peut ranker grâce à un seul passage pertinent
- Mécanisme sous-jacent : [[entities/dpr]] / [[entities/muvera]] + [[entities/bert]]
- Cf. [[concepts/passage-ranking]]

### Phase 3 — Micro-Contextualisation / Passage Generation
Le passage sélectionné est utilisé pour :
- Générer un **Featured Snippet** (position 0)
- Alimenter un **AI Overview** ([[entities/sge]])
- Être cité par un **LLM** (ChatGPT, Perplexity, Gemini)
- Mécanisme sous-jacent : [[concepts/grounding-score]] + [[concepts/confidence-score]]

### + Authorship Algorithmique (4ème corpus)
Tim ajoute un 4ème corpus transversal : les signaux d'auteur (bio, LinkedIn, publications, Wikipedia) qui renforcent la confiance à chaque phase. Cf. [[concepts/e-e-a-t]].

## Pertinence SEO/GEO

- La Triade explique pourquoi il faut optimiser **à 3 niveaux** simultanément : domaine (autorité), passage (contenu), citation (vérifiabilité)
- Le [[concepts/surprise-gap]] agit en Phase 2 (force la mémorisation du passage) et Phase 3 (augmente la probabilité de citation)
- La [[concepts/data-proprietaire]] agit en Phase 3 : données uniques = haute probabilité de citation car non disponibles ailleurs
- Le maillage interne agit en Phase 1 : distribue l'autorité pour que plus de pages passent le filtre d'admission

## Implication pratique pour le workflow

1. **Phase 1** → Vérifier que title, H1, URL, premier paragraphe contiennent le mot-clé cible
2. **Phase 2** → Structurer chaque H2 comme un vecteur sémantique distinct avec au moins 1 Surprise Gap
3. **Phase 3** → Intégrer data propriétaire vérifiable + citations sourcées pour maximiser le Grounding Score

## Pages liées

[[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/confidence-score]] · [[concepts/surprise-gap]] · [[entities/bm25]] · [[entities/dpr]] · [[entities/muvera]] · [[entities/sge]] · [[concepts/e-e-a-t]]
