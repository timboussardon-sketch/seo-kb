---
type: entity
title: NotebookLM
aliases: [notebook-lm, google-notebook-lm]
tags: [produit-ia, rag, google, ia]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: low
status: draft
---

# NotebookLM

**Sous-catégorie taxonomique** : Concepts-marque / Produits IA (§4.1 AGENTS.md — aux côtés de `google`, `bing`, `chatgpt-search`, `perplexity`).

Produit Google cité dans [[sources/2026-04-11-karpathy-llm-wiki]] comme **exemple de système RAG classique** — contre-exemple au pattern wiki persistant.

## Ce que dit la source

Une seule mention, groupée avec "ChatGPT file uploads, and most RAG systems". [[entities/karpathy]] les classe dans la catégorie où le LLM **redécouvre le savoir à chaque question** plutôt que de le **compiler et maintenir**.

> "NotebookLM, ChatGPT file uploads, and most RAG systems work this way"

Le *"this way"* = charger des fichiers, récupérer des chunks à la query time, générer une réponse. Rien n'est accumulé entre les questions. Voir [[concepts/persistent-wiki-vs-rag]] pour le contraste complet.

## Statut de la page

Stub de contraste. La source **ne décrit pas NotebookLM en détail** (features réelles, limitations, cas d'usage) — elle l'utilise uniquement comme étiquette pour une catégorie conceptuelle. `confidence: low` : aucune vérification indépendante du comportement de NotebookLM n'est encore faite dans cette KB.

## À investiguer (implications GEO)

- NotebookLM fait-il vraiment du RAG stateless, ou maintient-il une forme d'état persistant entre sessions (notebooks sauvegardés, citations générées, notes d'audio) ?
- Comment ce produit influence-t-il l'attention des utilisateurs côté recherche Google ? Est-ce un signal pour le comportement de SGE ?
- Les sources citées par NotebookLM apparaissent-elles dans les réponses SGE / AI Overviews, et selon quels critères ?

Ces questions restent ouvertes jusqu'à ce qu'une source dédiée les traite.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/persistent-wiki-vs-rag]]
