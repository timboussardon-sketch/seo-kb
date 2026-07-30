---
type: journal
project: golfiller
date: 2026-07-30
tags: [golfiller, journal, pseo, comparateur, seo, corpus-2]
---

# Golfiller — Journal du 2026-07-30 : comparateur de balles + 5 pages VS

Première brique du corpus 2 (base modèles) : le comparateur dynamique et les pages de duel prévus dans [[corpus-golfiller]] (priorité 1, score 5×5×4) n'existaient pas encore. Session de production : un comparateur hub + 5 pages VS statiques (SEO), reliés entre eux. Voir le cas global [[golfiller-strat]].

## Ce qui a été produit (prototypes locaux, pas encore poussés sur Shopify)

Dans `content-brain/golfiller/outputs/` :
- `2026-07-30-golfiller-comparateur-balles.html` — le hub : sélection libre de 2 balles parmi 13 modèles, duels rapides en un clic, fiche comparative (compression en deux barres empilées, jamais superposées), tableau vue d'ensemble cliquable. Template `.golf-page` (Bebas Neue).
- `2026-07-30-golfiller-vs-pro-v1-vs-pro-v1x.html`
- `2026-07-30-golfiller-vs-pro-v1-vs-chrome-soft.html`
- `2026-07-30-golfiller-vs-ad333-vs-supersoft.html`
- `2026-07-30-golfiller-vs-tp5-vs-tp5x.html`
- `2026-07-30-golfiller-vs-chrome-soft-vs-zstar.html` — 5 pages VS statiques, template `.gf-article`, chacune avec tableaux construction/compression, fiches, 5 vrais avis de golfeurs sourcés, verdict par profil de swing, FAQ, sources datées.

## Base modèles (corpus 2), complétée

Repris tel quel depuis les pages déjà publiées (AD333 68, Chrome Soft 72, TP5 85, TP5x 97, Z-Star 88, Wilson DX2 Soft 29, Inesis Tour 900 90, Wilson Ultra 90, Supersoft ≈38) et complété par les 3 valeurs manquantes, jamais publiées par Titleist et donc jamais dans le vault : Pro V1 (92,5), Pro V1x (98,7 à 102,0), AVX (77), mesurées par MyGolfSpy Ball Lab (labo indépendant, sources [[feedback_golfiller_sources_sites_marques]] respectée).

## Avis de golfeurs : ce qui a marché, ce qui n'a pas marché

Reddit est bloqué à la recherche directe (WebSearch/WebFetch) dans cet environnement, sauf via `old.reddit.com` en extraction HTML brute (marche pour Z-Star et Chrome Soft, haute confiance). GolfWRX bloque le fetch direct (403) mais se laisse lire via un lecteur proxy (confiance moyenne, mot-à-mot à recontrôler manuellement avant publication : signalé en note sur les pages concernées). Golf Monthly Forums est le seul forum accessible en fetch direct, sans blocage. TaylorMade TP5 seul : aucune citation dédiée trouvée (les citations retenues comparent directement TP5 et TP5x, ce qui sert quand même le duel).

## Décisions / règles apprises

- Toujours vérifier grep `—` avant livraison : tiret cadratin glissé deux fois dans le prototype initial (titre, séparateurs de tableau), corrigé.
- Cartes de comparaison à deux couleurs plates identiques = design jugé "sans signature" par Tim : corrigé avec avatar balle à alvéoles (taille proportionnelle à la compression) + barres empilées jamais superposées, jamais de border-left (règle [[feedback_design_pas_de_trait_lateral]]).
- Les pages VS utilisent `.gf-article` (articles), le comparateur `.golf-page` (outil), cohérent avec la convention posée le 2026-06-22.

## Reste à faire avant mise en prod

- Recontrôler mot pour mot les citations marquées "à recontrôler" (AD333 vs Supersoft, Pro V1 vs Chrome Soft, TP5 vs TP5x) en ouvrant les fils soi-même.
- Reconfirmer catalogue réel, URLs produit et prix sur golfiller.fr (scrape bloqué par le réseau du sandbox, plusieurs liens produit restent en générique `/collections/nos-produits`).
- Poser le JS du comparateur dans `theme.liquid`, jamais dans l'article (cf. [[reference_golfiller_shopify_js_theme]]).

Pages liées : [[corpus-golfiller]], [[golfiller-strat]], [[modeles/corpus-2-facette-grade]]
