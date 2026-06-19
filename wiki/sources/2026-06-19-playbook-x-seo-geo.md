---
type: source
source_type: doctrine
title: Playbook X.com (SEO + GEO) — synthèse d'ingest
aliases: [playbook-x-source, x-seo-geo-ingest]
tags: [seo, geo, aeo, x, twitter, grok, phoenix, parasite-seo, citation-ia, qadence]
created: 2026-06-19
updated: 2026-06-19
sources: 12
confidence: medium
status: stable
---

# Playbook X.com (SEO + GEO) — synthèse d'ingest

Source : [[raw/x-playbook/Playbook-X-autorite-SEO-IA]] (doctrine propriétaire de Tim, restructuré le 2026-06-19 en miroir exact du [[sources/2026-06-19-playbook-reddit-seo-geo|playbook Reddit]]). Compagnons techniques : décryptage algo Grok/Phoenix, plan 30 jours, plan de test des formats.

## Contexte

Même structure que le playbook Reddit, appliquée à X au service de Qadence.io. La thèse diverge sur deux points francs : X est **plus faible que Reddit pour le SEO Google** (login wall, pas de deal data), mais **plus fort en GEO via Grok** (algo Phoenix dérivé de Grok, Grok Search nourri par X), et le **cas francophone est inversé** (communauté SEO/IA FR vivante sur X, déserte sur Reddit).

## Chiffres et faits clés

- **Algo Phoenix** : depuis janvier 2026, l'algo de X est un transformer unique dérivé de Grok, open-sourcé (`github.com/xai-org/x-algorithm`). Lit le sens, pas les mots-clés. Poids de scoring NON publiés (feature-switches runtime) : les « réponse = +13.5 », « conversation = 75x un like » sont des estimations communautaires.
- **Grok = source GEO native** : ChatGPT s'appuie sur Bing, Perplexity crawle, AI Overviews puisent dans l'index Google, Grok superpose la data X. Grok intégré à une plateforme d'un milliard d'utilisateurs.
- **Liens externes pénalisés** : déboost 30-50 % de reach, quasi invisible sans Premium.
- **Reply game = moteur** : la réponse pèse beaucoup plus qu'un like ; conversation à double sens = signal le plus fort. 70/30 réponses/posts en démarrage.
- **Cap de diversité par auteur** : décroissance géométrique prouvée dans le code, la rafale de posts se cannibalise.
- **Demi-vie ~6h**, fenêtre critique 30-60 min.

## Mécanique (mirror Reddit)

Quatre leviers, dans l'ordre : citations IA (Grok d'abord), audience d'autorité par le reply game, mining d'insights, ranking Google à la marge. Règle d'or : « tu es un praticien qui a un compte X, pas un compte X qui pousse un produit ». Couche GEO commune au playbook Reddit : écrire comme une documentation, fraîcheur, et [[concepts/parasite-seo|réputation défensive]] (les IA citent le négatif).

## Limites (note de fiabilité)

- Poids de l'algo Phoenix = estimations reverse-engineerées, jamais des chiffres xAI.
- Débats de formats (threads vs solo, vidéo vs texte) ouverts : à trancher sur la data first-party via le plan de test.
- SEO Google de X présenté comme faible et secondaire, assumé.
- Aucune étude de cas X indépendante chiffrée. Le test Qadence.io est le premier cas first-party en cours.

## Test first-party : Qadence.io

Même cadre que sur Reddit. Objectif double : citations GEO de Qadence.io (Grok prioritaire) + autorité/positions sur mots-clés décisionnels, profitant à organikk.co. Deux règles : pas de spam, pas de coup éclair. Cf. [[entities/qadence-seo-agent]].

## Pages liées

[[entities/x-twitter]] · [[entities/grok]] · [[concepts/parasite-seo]] · [[sources/2026-06-19-playbook-reddit-seo-geo]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[entities/perplexity]] · [[entities/chatgpt-search]] · [[concepts/e-e-a-t]]
