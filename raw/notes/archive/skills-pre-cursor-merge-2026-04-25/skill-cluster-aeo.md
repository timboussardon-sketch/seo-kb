---
type: skill
source_type: doc-interne
title: "Skill : Clusters Sémantiques AEO"
aliases: ["Cluster AEO", "cocon AEO", "cluster-semantique"]
tags: ["skill", "cluster", "aeo", "agentic-search", "rrf", "architecture-contenu"]
created: "2026-04-12"
updated: "2026-04-12"
sources: []
confidence: haute
status: actif
---

# Skill — Clusters Sémantiques AEO / Agentic Search

## Quand déclencher
Construire une architecture de contenu optimisée pour les moteurs de réponse (SGE, Perplexity, ChatGPT) et les agents IA autonomes.

> Trigger : "cluster sémantique", "cocon SEO", "AEO", "Agentic Search", "quelles pages créer autour de [mot-clé]", "topical authority", maillage thématique.

## Concepts clés

- **[[aeo]]** (Answer Engine Optimization) — optimisation pour les moteurs qui génèrent des réponses directes
- **[[agentic-search]]** — agents IA autonomes qui effectuent des recherches et actions
- **[[rrf]]** (Reciprocal Rank Fusion) — un cluster couvrant toutes les sous-intentions améliore le score global
- **Principe MECE** — Mutuellement Exclusif, Collectivement Exhaustif

## Framework : 3 types d'intentions (remplace TOFU/MOFU/BOFU)

| Type | Définition | Format idéal | Distribution |
|------|-----------|--------------|-------------|
| **Know-Simple** | Questions factuelles, réponse <50 mots | Définition, chiffre, FAQ courte | 20–30% |
| **Know** | Explication approfondie avec preuves | Guide, tutoriel, comparatif | 40–50% |
| **Do** | Micro-tâches à accomplir (ou exécutables par un agent) | Calculateur, simulateur, générateur, audit | 20–30% |

## Pipeline (5 étapes)

1. **Définir le mot-clé pilier** — requête principale + secteur + ressources disponibles
2. **Mapper les intentions** selon le framework Know-Simple / Know / Do
3. **Générer le tableau du cluster** — minimum 15 pages satellites
4. **Définir le maillage interne** — liens entrants/sortants + ancres par page
5. **Prioriser et roadmap** — volume + difficulté + potentiel conversion + effort

## Output obligatoire

```
Cluster sémantique — '[Mot-clé pilier]'

| Requête cible | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| ... | Know-Simple | FAQ + définition | FAQPage | Haute |
| ... | Do | Calculateur interactif | WebApplication | Haute |

Maillage interne : [schéma connexions]
Roadmap : Mois 1 → Know-Simple | Mois 2 → Know | Mois 3 → Do + pilier
```

## Règles absolues

- ❌ Utiliser TOFU/MOFU/BOFU — obsolète pour l'AEO
- ❌ Deux pages sur le même angle (principe MECE)
- ✅ Pages "Do" = outils interactifs, pas du contenu textuel
- ✅ Pages Know pointent systématiquement vers une page Do (maillage intentionnel)
- ✅ Réviser le cluster tous les 6 mois

## Concepts liés

[[aeo]] · [[agentic-search]] · [[rrf]] · [[maillage-interne]] · [[topical-authority]] · [[fully-meets]]
