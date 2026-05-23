---
type: entity
title: "Google Search Console (GSC)"
aliases: [gsc, google-search-console, search-console]
tags: [outil-seo, google, data, gsc]
created: 2026-05-21
updated: 2026-05-21
sources: 2
confidence: high
status: stable
---

# Google Search Console (GSC)

Outil gratuit de Google qui expose la donnée de performance organique réelle d'un site : requêtes, pages, clics, impressions, CTR, position moyenne. Dans la doctrine de Tim, c'est la **seule source de vérité** pour la recherche de mots-clés et l'audit — par opposition aux outils tiers ([[entities/semrush]], Ahrefs) qui travaillent sur de la donnée projetée.

## Pourquoi c'est central

La GSC montre ce que Google a déjà compris du site. Le signal clé n'est pas le volume mais le **delta impressions / clics** : une page en position 3-12 avec de grosses impressions et un CTR au sol est un quick win ; une requête à fortes impressions sans page dédiée est un content gap. Cohérent avec la [[concepts/triade-serp]] — on travaille avec l'alignement SERP réel, pas une projection d'outil.

## Usages dans la méthode

- **Recherche de mots-clés** — étape 2 du [[syntheses/process-keyword-research-5-etapes|process KW research]] : export requêtes + pages + croisement.
- **Quick wins** — pages position 3-12 à fort potentiel (skill `seo-quick-win`).
- **Cannibalisation** — détection des requêtes qui déclenchent 2+ URLs (skill `seo-cannibalisation`).
- **Maillage** — hiérarchie mère/fille à partir des impressions par page (skill `maillage-interne-gsc`).
- **Preuves** — baseline et mesure J+30 / J+90 des fiches preuve (cf. [[preuves/SETUP-GSC]]).

## Accès

Export CSV manuel (Google Sheet) ou API / MCP. L'API officielle est « pas évidente à décrocher » — l'export CSV reste le défaut opérationnel.

## Pages liées

[[concepts/triade-serp]] · [[concepts/grounding-score]] · [[syntheses/process-keyword-research-5-etapes]] · [[concepts/mots-cles-actionnels]] · [[entities/semrush]]
