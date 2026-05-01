---
type: entity
title: Obsidian
aliases: [obsidian-md]
tags: [outil, markdown, ide, wiki]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: high
status: stable
---

# Obsidian

**Sous-catégorie taxonomique** : Outils SEO (§4.1 AGENTS.md — explicitement listé).

Éditeur markdown utilisé comme **IDE** pour le wiki dans le pattern LLM Wiki ([[sources/2026-04-11-karpathy-llm-wiki]]).

## Rôle dans le pattern

Cité dans [[concepts/obsidian-as-ide]] via la formule de [[entities/karpathy]] : *Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase*.

En pratique : l'agent LLM modifie les markdown d'un côté, l'utilisateur lit en temps réel dans Obsidian de l'autre — suit les liens, consulte la graph view, lit les pages mises à jour.

## Features utilisées par le pattern

- **Wikilinks** `[[page]]` — syntaxe native, pas de chemins relatifs
- **Graph view** — visualisation de la forme du wiki : connecté, hubs, orphelins
- **Web Clipper** (extension navigateur) — convertit les articles web en markdown, dépose dans `raw/`
- **Download attachments** (hotkey configurable) — télécharge les images en local vers `raw/assets/` après clipping

## Plugins recommandés par la source

- **Dataview** — requêtes dynamiques sur frontmatter YAML (tables, listes générées)
- **Marp** — slide decks depuis markdown
- **Graph Analysis** — visualiser la structure du wiki

## Limite notée

Les LLM ne peuvent pas lire nativement un markdown avec images inline en un seul passage. Workaround : lire le texte d'abord, puis consulter les images séparément. "Un peu clunky mais ça marche assez bien" selon [[sources/2026-04-11-karpathy-llm-wiki]].

## Usage SEO potentiel (à développer avec d'autres sources)

Obsidian est listé dans la §4.1 d'`AGENTS.md` comme "Outil SEO" aux côtés d'Ahrefs, Semrush, Screaming Frog, GSC. C'est une classification **de cette KB**, pas de la source Karpathy — elle reflète l'usage qu'en fait Tim pour structurer ses notes et son wiki de veille. Les features SEO-spécifiques (Dataview pour requêter les exports GSC, maillage de notes de clients) sont à documenter dans des sources ultérieures.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/obsidian-as-ide]] · [[concepts/persistent-wiki-vs-rag]] · [[entities/karpathy]]
