---
type: concept
title: Obsidian as IDE, LLM as programmer
aliases: [obsidian-ide, llm-programmer-analogy]
tags: [pattern-kb, analogie, obsidian, ide, meta]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: high
status: stable
---

# Obsidian as IDE, LLM as programmer

L'analogie opérationnelle que [[sources/2026-04-11-karpathy-llm-wiki]] utilise pour cadrer le pattern.

## La formule

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase"

Trois rôles clairement séparés :

- **[[entities/obsidian]]** = environnement de lecture + édition humaine + visualisation (wikilinks, graph view, plugins)
- **Le LLM** = celui qui *écrit* et *modifie* le code (les pages markdown)
- **Le wiki** = l'artefact manipulé, versionnable (git), navigable

## Le workflow qu'elle implique

[[entities/karpathy]] décrit le setup physique : **agent LLM ouvert d'un côté, Obsidian de l'autre**. L'agent édite, l'utilisateur lit en temps réel — il suit les liens, regarde la graph view, lit les pages mises à jour. Le feedback humain-agent est quasi-instantané.

## Ce que l'analogie cache

L'IDE (Obsidian) est **passif** — il affiche ce que l'agent écrit, il ne *supervise* pas l'agent. Le contrôle humain se fait à deux niveaux :

- **Avant** — en donnant la direction à l'agent
- **Après** — en lisant les diffs, la graph view, et en corrigeant

C'est bien la dynamique programmeur / IDE : l'IDE n'empêche pas un bug, il rend le bug visible.

## Pourquoi Obsidian plutôt qu'autre chose

La source **ne compare pas explicitement** Obsidian à VS Code, Logseq, ou autres. Les features importantes ne sont pas propres à Obsidian mais y sont toutes assemblées : wikilinks natifs, graph view, plugins (Dataview, Marp), stockage markdown plain, git-friendly. Voir [[entities/obsidian]].

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[entities/obsidian]] · [[entities/karpathy]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/ingest-workflow]]
