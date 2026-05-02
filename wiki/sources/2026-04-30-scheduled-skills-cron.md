---
type: source
source_type: doctrine
title: "Scheduled skills Tim — 6 specs cron (revue presse / scan arxiv / recap hebdo / todo / rappel calls)"
aliases: [scheduled-skills, cron-skills, skills-recurrents]
tags: [doctrine-tim, cron, skills, scheduled, automation, revue-presse, scan-arxiv, recap-hebdo]
created: 2026-04-30
updated: 2026-04-30
sources: 1
confidence: high
status: stable
---

# Scheduled skills Tim — 6 specs cron

**Type** : 6 specs de skills récurrents (cron / scheduled remote agents) qui automatisent la veille, le récap et la maintenance de la KB de Tim.
**Auteur** : Tim · **Fichier raw** : `raw/notes/scheduled-skills/` (6 fichiers SKILL-*)
**Date** : 2026-04-30

## Inventaire des 6 skills

| Skill | Cadence | Rôle |
|---|---|---|
| `SKILL-revue-presse-quotidienne.md` | Quotidien (~9h07 Paris) | Édition Algorithme du jour — newsletter Substack |
| `SKILL-raw-revue-de-presse.md` | Quotidien | Production du fichier raw `raw/revue-de-presse/revue-presse-YYYY-MM-DD.md` |
| `SKILL-scan-arxiv-seo-ia.md` | Hebdo | Scan ArXiv des publications de la semaine impactant SEO/search ranking/LLM |
| `SKILL-recap-hebdo-vendredi.md` | Hebdo (vendredi) | Récap synthétique de la semaine (calls, contenus produits, retours) |
| `SKILL-todo-quotidienne-bilan-tim.md` | Quotidien | Bilan + todo-list quotidienne Tim |
| `SKILL-rappel-calls-1h.md` | À la demande / 1h avant | Rappel automatique avant un call client/prospect |

## Skill `scan-arxiv-seo-ia` (référence détaillée)

Le skill scan-arxiv est documenté précisément (cohérent avec [[sources/2026-04-15-scan-arxiv-15-avril]] et [[sources/2026-04-25-scan-arxiv-25-avril]] qui sont les **outputs** de ce skill).

**Rôle** : Lead Market Intelligence SEO/Digital. Scanne les publications académiques pour détecter les signaux faibles qui vont impacter le SEO et la visibilité digitale.

**Mission** : 5 recherches web différentes minimum :
1. `site:arxiv.org "search ranking" OR "web search" derniere semaine`
2. `site:arxiv.org "LLM retrieval" OR "retrieval augmented" derniere semaine`
3. `site:arxiv.org "content quality" OR "information retrieval" derniere semaine`
4. `site:arxiv.org "generative search" OR "AI search" derniere semaine`
5. `site:arxiv.org "SEO" OR "search engine optimization" derniere semaine`

**Filtre** (passer ≥ 2/3 critères) :
- Impact CONCRET sur la stratégie SEO d'un site ?
- Change la création de contenu / structure / visibilité ?
- Révèle une menace ou une opportunité business ?

**Format de sortie** par étude retenue (max 5) : Titre vulgarisé · Source ArXiv · Impact business 1 ligne · Signal 🔴/🟢/🟡 · Résumé CODIR 3-4 phrases · Lien avec tendances Algorithme.

**Verdict hebdo** obligatoire en clôture : tendance de fond + sujet prioritaire newsletter.

## Articulation avec la routine cloud Anthropic

Cohérent avec [[MIGRATION]] §7 qui mentionne la **routine cloud Algorithme** (`trig_01Q9turzWB81Ck2i4YF3gyzN`, cron `7 7 * * *` UTC, lien https://claude.ai/code/routines/trig_01Q9turzWB81Ck2i4YF3gyzN) — la `revue-presse-quotidienne` et `raw-revue-de-presse` sont vraisemblablement les skills exécutés par cette routine.

## Articulation avec le sous-repo revue-de-presse

Cohérent avec [[MIGRATION]] §2 : le sous-repo `~/Documents/seo-kb/raw/revue-de-presse/` est synchronisé toutes les 15 min via LaunchAgent macOS — la routine cloud écrit dans ce sous-repo, le LaunchAgent le synchronise localement.

## Apports à la KB

- Documente l'**infrastructure d'automation** complète de Tim — boucle quotidienne newsletter + boucle hebdo veille arxiv + boucle hebdo récap + boucles transactionnelles (todo + rappel calls)
- Le skill `scan-arxiv-seo-ia` ici expose les **5 prompts de recherche exacts** qui produisent les outputs [[sources/2026-04-15-scan-arxiv-15-avril]] et [[sources/2026-04-25-scan-arxiv-25-avril]]
- Référence pour comprendre **pourquoi les sources ingérées ont la forme qu'elles ont** (la doctrine du skill formate la sortie : Signal 🔴/🟢/🟡, Lien avec tendances Algorithme, etc.)
- Cohérent avec [[concepts/agentic-search]] côté **infrastructure** — Qadence est l'agent on-demand, ces 6 skills sont les agents scheduled

## Limites

- Specs lues en survol uniquement (pas le détail complet de chaque SKILL-*.md)
- Pas de mesure de fiabilité / taux d'échec sur les routines cron à date
- `SKILL-rappel-calls-1h.md` mentionné mais mécanisme de déclenchement (intégration calendrier ?) non documenté dans cette source
- 2 skills similaires (`revue-presse-quotidienne` vs `raw-revue-de-presse`) — distinction de rôle à clarifier (un produit la version éditoriale, l'autre archive le raw ?)

## Pages liées

[[sources/2026-04-15-scan-arxiv-15-avril]] · [[sources/2026-04-25-scan-arxiv-25-avril]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-30-qadence-seo-agent-snapshot]] · [[concepts/agentic-search]] · [[concepts/data-proprietaire]] · [[entities/organikk-co]]
