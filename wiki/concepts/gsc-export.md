---
type: concept
title: Export GSC
aliases: [gsc-export, export gsc, gsc export, export Search Console]
tags: [gsc, data, methode, outils]
created: 2026-06-20
updated: 2026-06-20
confidence: medium
status: stable
---

# Export GSC

Récupérer la data **réelle** de la Google Search Console d'un site (pages, requêtes, positions, impressions, clics) pour alimenter une analyse. Principe non négociable : tout chiffre d'un site vient de la GSC, jamais inventé.

## Moyens
- Edge function `admin-gsc-export` côté Fusionn + secret `~/.config/seo-kb/fusionn-gsc-export.secret` : puller la GSC de n'importe quelle propriété connectée (golfiller, fgformation, victoria garden…). Les exports datés vivent dans `wiki/sources/` (ex. `2026-06-11-victoriagarden-gsc-export`).
- Export manuel depuis l'interface GSC pour un coup ponctuel.

Consommé par les skills data : `seo-quick-win`, `maillage-interne-gsc`, `seo-cannibalisation`, `maillage-systeme`. Lié à : [[maillage-interne]], [[cannibalisation]].
