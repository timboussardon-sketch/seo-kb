---
type: source
source_type: doc-interne
title: "Connexion API Search Console — organikk.co"
aliases: ["GSC API organikk", "gsc-organikk"]
tags: [infra, organikk, search-console, api, mcp]
created: 2026-08-01
updated: 2026-08-01
sources: 0
confidence: high
status: draft
---

# Connexion API Search Console — organikk.co

Mise en place le 2026-08-01, déclenchée par un audit d'indexation d'organikk.co (site à 4 mois, 420 URLs au sitemap mais quasi invisible sur `site:organikk.co`, à comparer à qadence.io qui rankait déjà). Les recherches `site:` via l'outil web se sont révélées peu fiables (résultats pollués par des homonymes, ex. le paquet Python quantique "qadence" de Pasqal) — nécessité d'une vraie donnée Search Console plutôt qu'une estimation.

## Ce qui a été monté

**Projet GCP dédié** : `organikk-gsc` (pattern un projet par produit, comme `FUSIONN`, `EEAT` déjà existants sur le compte `tim.boussardon@gmail.com`).

**Compte de service** : `organikk-gsc-reader@organikk-gsc.iam.gserviceaccount.com`, clé JSON stockée dans `~/.config/organikk-gsc/service-account.json` (chmod 600, hors repo) — même convention que [[reference_youtube_api_key|la clé YouTube]].

**API activée** : Search Console API (`searchconsole.googleapis.com`), pas de compte de facturation requis.

**Étape manuelle obligatoire** (pas d'API pour ça) : ajouter l'email du compte de service comme utilisateur (Restreint suffit, lecture seule) sur la propriété organikk.co dans Search Console → Paramètres → Utilisateurs et autorisations.

**Serveur MCP** : [`ahonn/mcp-server-gsc`](https://github.com/ahonn/mcp-server-gsc) (255⭐, MIT, maintenu) plutôt qu'un script maison — s'authentifie directement via `GOOGLE_APPLICATION_CREDENTIALS`, pas besoin d'OAuth browser-based comme d'autres alternatives testées (`crunchtools/mcp-google-search-console`, plus lourd). Outils exposés : `list_sites`, `search_analytics`, `enhanced_search_analytics`, `detect_quick_wins`, `index_inspect`, `list_sitemaps`, `get_sitemap`, `submit_sitemap`.

Enregistré dans Claude Code :
```
claude mcp add gsc-organikk \
  --env GOOGLE_APPLICATION_CREDENTIALS=/Users/timothee/.config/organikk-gsc/service-account.json \
  -- npx -y mcp-server-gsc
```

## Reproductible pour un autre site

Le compte de service `organikk-gsc-reader` peut être ajouté comme utilisateur sur n'importe quelle autre propriété Search Console que Tim possède (qadence.io, bxble, etc.) — pas besoin de recréer un projet GCP par site, un seul projet + un seul compte de service suffisent pour lire plusieurs propriétés, tant que l'email est ajouté utilisateur sur chacune.

## Non vérifié / à suivre

- Statut réel d'indexation d'organikk.co (420 URLs sitemap) pas encore récupéré : la connexion technique est faite mais le compte de service n'était pas encore confirmé comme utilisateur ajouté côté GSC au moment de la rédaction de cette note.
- Comparatif qadence.io vs organikk.co (positions/impressions réelles) à faire une fois la donnée `search_analytics` disponible pour les deux propriétés.
