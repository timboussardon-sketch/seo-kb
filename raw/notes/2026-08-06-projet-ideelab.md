---
type: source
source_type: test-terrain
title: Projet Ideelab — outil de validation d'idée business
tags: [side-project, hors-scope-seo, ideelab]
created: 2026-08-06
---

# Projet Ideelab

Note hors-scope SEO/IA/GEO, conservée ici à la demande explicite de Tim malgré la règle `AGENTS.md` (vault normalement scopé SEO). Pas d'ingestion wiki à prévoir, pas de skill SEO concerné.

## Le produit

Ideelab (ideelab.co, propriété de Tim, ownership confirmé en session) : outil qui vérifie si une idée business existe déjà en scannant plusieurs bases en une recherche. Positionnement du site en prod : « Quelqu'un fait deja ton truc. Ou pas. Tape pour savoir. »

5 bases annoncées sur le site en prod : App Store, GitHub, Product Hunt, Google, INPI.

## Ce qui a été construit (2026-08-06)

Repo : `~/Code/ideelab` (Next.js 16 App Router, TypeScript, Tailwind v4, police IBM Plex Mono).

- **Landing pixel-perfect** de la DA existante d'ideelab.co : nav sticky, hero, barre de recherche (bordure noire 2px, bouton GO désactivé si champ vide), chips de suggestions, 5 carrés colorés, footer 4 colonnes + logo géant en filigrane. Tokens extraits par capture Playwright + inspection DOM (pas de re-création à l'œil) : fond `#F5F0EB`, encre `#1A1A1A`, accent `#FF2D55`, bleu `#4285F4`, violet `#7B61FF`, orange `#FF6154`, rayons 12px partout.
- **Recherche fonctionnelle** : saisie → route vers `/scanner?q=...`.
- **`/scanner`** : squelette listant 5 sources (App Store, GitHub, Google Ads, Product Hunt, INPI) en statut « connexion pas encore branchée ». Aucune intégration réelle branchée à ce stade.

## API gratuites repérées pour brancher les sources (session du 2026-08-06)

Vérifiées à date de session (plusieurs infos volatiles, à re-checker si repris plus tard) :

- **App Store** : iTunes Search API, gratuite, sans clé.
- **GitHub** : REST/GraphQL, gratuite, 60 req/h sans token / 5000 req/h avec.
- **npm / RubyGems** : registres gratuits sans clé, utile pour détecter un outil déjà codé.
- **Product Hunt API v2** (GraphQL) : gratuite après inscription app, quota 6250 points/15 min.
- **Hacker News via Algolia HN Search** : gratuite, sans clé, full-text sur tout HN (Show HN / Ask HN inclus).
- **Reddit API** : gratuite mais **usage non commercial uniquement**, et pré-approbation obligatoire depuis la Responsible Builder Policy (nov. 2025). Incompatible tel quel avec Ideelab qui est un produit payant (offres Pro/Agence) — nécessiterait l'offre payante Reddit.
- **Recherche d'entreprises (data.gouv.fr)** : gratuite, sans clé, agrège INSEE Sirene + RNE. Vérifie si un nom d'entreprise existe déjà en France.
- **INSEE Sirene API** : gratuite avec compte.
- **Data INPI** (marques/brevets/dessins) : gratuite, sans clé, maj hebdomadaire pour les marques. Couvre FR + EUIPO + désignations OMPI en France.
- **EUIPO Trademark Search API** : gratuite avec inscription développeur.
- **RDAP, Wayback Machine Availability API, Common Crawl CDX** : gratuites sans clé, pour vérifier l'existence/l'historique d'un nom de domaine.
- **Google Custom Search JSON API** : gratuite, 100 requêtes/jour.
- **Brave Search API** : gratuite, ~2000 requêtes/mois, index indépendant.
- **YouTube Data API v3** : gratuite, quota 10 000 unités/jour (~100 recherches/jour). Tim a déjà une clé YouTube réutilisable.
- **OpenCorporates API** : gratuite, ~500 requêtes/mois, registre d'entreprises international.

**Écartées** : Bing Search API (fermée par Microsoft le 11 août 2025, aucun remplaçant officiel) ; X/Twitter API (n'est plus gratuite du tout depuis le 6 février 2026) ; Google Trends (pas d'API officielle, seulement du scraping non officiel) ; Google Play (pas d'API officielle de recherche, seulement des libs de scraping non officielles, zone grise CGU).

## Prochaine étape

Brancher une première source réelle dans `/scanner`. Candidats les plus simples (zéro clé, zéro friction) : Recherche d'entreprises (data.gouv.fr) et Hacker News/Algolia.
