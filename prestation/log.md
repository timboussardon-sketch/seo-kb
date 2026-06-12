# Log roadmap-prestation

Append-only. Format : ## [YYYY-MM-DD] <client> | étape N | action

## [2026-06-10] système | bootstrap
- création prestation/ (roadmap.md maître, clients/, _template.md, log.md)
- roadmap seedée : 15 étapes en 5 phases (cadrage, diagnostic data, stratégie, production, système+autonomie)
- skill roadmap-prestation créé dans ~/.claude/skills/

## [2026-06-10] golfiller | étape 3 | analyse GSC 90j + 6 mois comparée
## [2026-06-10] golfiller | étape 8 | 7 modèles pSEO scorés

## [2026-06-10] golfiller | étape 10 | entités vectorielles page Money « balle de golf »
- output: [[queries/entites-2026-06-10-golfiller-balle-de-golf]]
- skill: seo-entites-vectorielles ; étape 10 doctrine -> éprouvée
- next: B modèle page par marque, C titres fiches produit, puis brief Hn -> content-brain

## [2026-06-10] golfiller | étape 8 | scrape blog + nouveau modèle directory usage/besoin
- méthode: lire le blog (directory déjà publiés) + croiser GSC non couvert
- output: [[clusters/modeles-pseo-2026-06-10-golfiller]] (section modèle additionnel usage/besoin)
- retenu par Tim: usage/besoin uniquement (écarté: local magasin, handicap, perso)
- next: étape 11 brief Hn page « balle de golf pour la distance » (template usage)

## [2026-06-10] golfiller | étape 11 | brief Hn page usage « balle de golf pour la distance »
- output: [[briefs/2026-06-10-balle-golf-distance]]
- skill: seo-brief-contenu ; template réplicable (contrôle, vent, durabilité, budget)
- next: prod via content-brain (étape 12)

## [2026-06-10] golfiller | étape 12 | article rédigé (draft) « balle de golf pour la distance »
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.md
- skill: content-brain ; gate PASS-sous-réserve (distances par profil [À SOURCER] = bloqueur publication)
- claims verified: tech compression (3 sources), prix catalogue (proprio). écarté: distances par profil
- prédiction P-golfiller-2026-06-10-1 ouverte (pos <10 sur « balle pour la distance » à J+90)

## [2026-06-10] golfiller | étape 12 | enrichissement article (scrape data site)
- ajout table distance/vitesse de swing (claim 014, scrapée de la page vitesse-de-swing du site = data propriétaire)
- gate passe à PASS (~95%) ; reste seul [À SOURCER] : distance comparée PAR modèle (launch monitor)

## [2026-06-10] golfiller | étape 12 | version HTML/CSS de l'article (Shopify-ready)
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.html (CSS scopé .gf-article, tableaux stylés, liens internes réels, bloc Sources)
- référencé dans entities/golfiller.md (section Articles produits)

## [2026-06-10] golfiller | étape 12 | set usage complet HTML/CSS (4 pages dupliquées)
- pages: contrôle, vent, durabilité, budget (+ distance déjà faite) = modèle directory usage complet
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-*.html (Shopify-ready, CSS scopé)
- said_index: 4 lignes (anti-cannib, 1 page = 1 besoin)

## [2026-06-11] alexia | étape 1 | premier email d'onboarding capturé
- création prestation/emails.md (modèles d'emails vivants)
- §1 premier email (envoi dashboard + 3 docs contexte + vidéo) = exemple Alexia verbatim
- roadmap.md étape 1 enrichie : renvoi vers emails.md §1

## [2026-06-12] leexi | tracker | création du tracker prestation (reprise client)
- état consolidé depuis leexi-seo/Journal.md (session 1 du 2026-06-09)
- étapes 1-3 faites + amorce 6 + étape 14 (espace client DA Leexi)
- en attente d'arbitrage : Bloc 1 réparation refonte vs Bloc 3 souveraineté

## [2026-06-12] leexi | étape 3 | restitution GSC en Google Doc (5 points clés en intro)
- doc : https://docs.google.com/document/d/1iVnT2wtNeS617iYQIXTCCuRi8kkdDYANNwEJChRR99E/
- roadmap.md étape 3 enrichie : format de restitution Google Doc + En résumé
- arbitrage bloc 1 (refonte) vs bloc 3 (souveraineté) toujours en attente

## [2026-06-12] leexi | étape 3+14 | diagnostic GSC publié dans l'onglet Audit de l'espace client
- même contenu que le Google Doc, en DA Leexi (tiles, sections numérotées, plan 4 blocs)
- déployé sur organikk.co (noindex)
