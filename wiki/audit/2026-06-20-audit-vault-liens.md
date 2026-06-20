---
type: audit
title: Audit vault et wikiliens — 2026-06-20
tags: [audit, maillage, wikiliens, vault]
created: 2026-06-20
updated: 2026-06-20
status: draft
---

# Audit vault et wikiliens — 2026-06-20

Audit déterministe des wikiliens du vault (862 notes hors `.git/.venv/.claude/.agents`, blocs de code et templates exclus du comptage). Le vault est sain : ~6 135 liens réels, **~130 cassés (~2 %)**, orphelins quasi tous légitimes.

## En résumé

- **Cause n°1 : des noms de skills écrits comme wikiliens.** `[[ton-de-voix-tim]]` ×23 + `[[article-engine-pipeline]]`, `[[maillage-interne-gsc]]`, `[[seo-cannibalisation]]`. Ils pointaient vers des skills (`.claude/skills/`), pas des notes → cassés dans le graphe.
- **Cause n°2 : notes-concepts manquantes** (`geo`, `maillage-interne`, `intention-recherche`, `preuve-atomique`, `gsc-export`).
- **Cause n°3 : liens « en avance »** vers des livrables clients pas encore écrits (normal, backlog ci-dessous).
- **Orphelins : 448**, mais ~371 sont des feuilles légitimes (`raw/` journal/drafts, `agent-synthetic/` newsletters). Seulement **5 dans `wiki/`** (dashboard, log, index, 2 health) = points d'entrée Obsidian, OK.
- **32 basenames ambigus** (même nom dans plusieurs dossiers) : résolution Obsidian non déterministe.

## Correctifs appliqués ce jour

Création de 6 notes-concepts canoniques dans `wiki/concepts/` (résolvent ~40 liens cassés, dont les 23 `ton-de-voix-tim`) :
[[ton-de-voix-tim]] · [[geo]] · [[maillage-interne]] · [[intention-recherche]] · [[preuve-atomique]] · [[gsc-export]]

## Reste à traiter (non bloquant)

- **Cross-refs vers la mémoire `feedback_*`** (ex. dans `fusionn/Historique.md`) : vivent dans `~/.claude`, hors vault → resteront cassés tant qu'on n'a pas de notes vault équivalentes. À ignorer ou convertir.
- **Placeholders de templates** (`[[wikilink]]`, `[[lien]]`, `[[decisions/XXXX-…]]`) : intentionnels.
- **Basenames ambigus** : `golfiller` (×3), `leexi` (×2), `_template`, `index`, `log`, `dashboard`, `score-grid`, `directives`. Préférer des liens par chemin (`[[entities/golfiller]]`) quand l'ambiguïté compte.

## Backlog client — notes référencées mais pas encore écrites

Liens « en avance » détectés (à créer quand le livrable existe) :

- **Leexi** : `[[leexi-brief]]`, `[[analyse-gsc-leexi]]`, `[[analyse-gsc-approfondie-leexi]]`, `[[audit-thematique-leexi]]`, `[[etude-marche-notetakers-fr]]`, `[[etude-rgpd-souverainete-leexi]]`
- **Alexia** : `[[alexia-call-cadrage]]`, `[[alexia-resume-call-envoye]]`
- **Catherine** : `[[catherine-call-decouverte]]`
- **Victoria Garden** : `[[strat-victoria-garden-pseo]]`
- **Données** : `[[raw/data/keyword-research-2026-05-02]]`

## Méthode

Script ad hoc : collecte des `.md`, index par basename (résolution façon Obsidian), strip des blocs de code (` ``` ` et inline) pour éviter les faux positifs `[[ … ]]` bash, exclusion des templates et des notes d'audit. Comptage des liens entrants pour les orphelins.
