---
type: concept
title: Query + synthesis (filing back)
aliases: [query-filing-back, explorations-compound]
tags: [pattern-kb, workflow, query, meta]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: high
status: stable
---

# Query + synthesis (filing back)

Le **second moteur** du pattern wiki persistant : comment les questions deviennent elles-mêmes des artefacts. Décrit dans [[sources/2026-04-11-karpathy-llm-wiki]].

**À ne pas confondre** avec la §6.2 du `AGENTS.md` de cette KB — celle-ci est l'instanciation SEO-first du pattern Karpathy, avec en plus les hooks vers les 12 skills propriétaires.

## Flow standard (version Karpathy)

1. Tu poses une question au wiki
2. L'agent lit `index.md` pour identifier les pages pertinentes
3. Il drill dans 3-8 pages
4. Il synthétise une réponse **avec citations** `[[...]]`

## Les formats de sortie possibles

La réponse n'est pas forcément un texte inline en chat. Elle peut prendre la forme :

- Une **page markdown** (synthèse textuelle)
- Une **table de comparaison**
- Un **slide deck** via Marp
- Un **graphique** via matplotlib
- Un **canvas Obsidian**

Le format suit la question.

## L'insight clé : filing back

> "good answers can be filed back into the wiki as new pages"

Une comparaison que tu as demandée, une analyse, une connexion que tu as découverte — ce sont des artefacts **précieux qui ne doivent pas disparaître dans l'historique de chat**. En les filant dans `wiki/queries/` ou `wiki/syntheses/`, elles deviennent réutilisables, linkables, et elles nourrissent les queries suivantes.

**Conséquence** : les *explorations* compoundent exactement comme les *sources ingérées*. Le wiki grossit dans deux dimensions — ce que tu lis **et** ce que tu demandes.

## Relation au pattern global

- Pendant du [[concepts/ingest-workflow]] — ingest = sources en entrée ; query = questions en entrée ; les deux produisent des pages filées
- Repose sur la discipline de [[concepts/persistent-wiki-vs-rag]] : sans index bien maintenu, la phase "drill dans 3-8 pages" casse

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/ingest-workflow]] · [[entities/obsidian]]
