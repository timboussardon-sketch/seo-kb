---
type: concept
title: Ingest workflow (pattern Karpathy)
aliases: [ingest-pattern, ingest-kb]
tags: [pattern-kb, workflow, ingest, meta]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: high
status: stable
---

# Ingest workflow (pattern Karpathy)

Le *comment* de [[concepts/persistent-wiki-vs-rag]] : ce que fait l'agent LLM quand une nouvelle source arrive. Décrit dans [[sources/2026-04-11-karpathy-llm-wiki]].

**À ne pas confondre** avec la §6.1 du `AGENTS.md` de cette KB — cette §6.1 est une **instanciation** SEO-first du pattern Karpathy (avec détection `source_type`, hooks skills, doctrine §2), pas le pattern lui-même.

## Flow type (version Karpathy)

1. Tu déposes une source dans `raw/` (drag-drop, Obsidian Web Clipper, ou `cp`)
2. Tu dis à l'agent : "ingère cette source"
3. L'agent **lit** le fichier en entier
4. L'agent **discute** les takeaways avec toi — il ne produit rien encore
5. L'agent **écrit** une page résumé dans `wiki/sources/`
6. L'agent **met à jour l'index** (`wiki/index.md`)
7. L'agent **met à jour les pages entities et concepts** pertinentes à travers le wiki
8. L'agent **append une entrée** dans `wiki/log.md`

## Le chiffre qui compte

> "A single source might touch 10-15 wiki pages"

C'est ce qui distingue un ingest LLM d'un classement manuel : une source ne **produit** pas juste une page, elle **touche** tout un réseau de pages existantes (entities enrichies, concepts révisés, contradictions flaguées). Ce compte est **typique**, pas mesuré — aucun benchmark ne le soutient dans la source.

## One-at-a-time vs batch

[[entities/karpathy]] préfère **one-at-a-time avec supervision** : il lit les résumés, inspecte les updates, guide l'emphase. Il mentionne que le batch (plusieurs sources d'un coup, supervision minimale) est possible mais c'est un trade-off contrôle vs vitesse.

Le choix se formalise dans le fichier schéma (`AGENTS.md`) pour que les sessions futures suivent la même discipline.

## Relation au pattern global

L'ingest est **la moitié** du flywheel. L'autre moitié est [[concepts/query-synthesis]] : les bonnes réponses aux questions sont filées dans le wiki → les explorations compoundent au même titre que les sources ingérées.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/query-synthesis]] · [[entities/karpathy]]
