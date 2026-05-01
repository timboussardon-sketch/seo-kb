---
type: concept
title: Test de substitution LLM (filtre 80%)
aliases: [test-substitution-llm, filtre-80-pourcent, substitution-test]
tags: [methode, doctrine-tim, pseo, product-led, qualification-page, geo, aeo]
created: 2026-04-13
updated: 2026-04-13
sources: 2
confidence: high
status: stable
---

# Test de substitution LLM (filtre 80%)

**Méthode propriétaire** formalisée à partir du livrable [[sources/2026-04-13-victoria-garden-pseo]]. Filtre binaire de qualification de page **avant** production.

## La règle

> Pour chaque idée de page, demander à un LLM de produire la même réponse.
> **Si le LLM peut produire 80 % de la page → ne pas la créer.**

Une page substituable par un LLM n'a aucun avantage défensif : le moteur génératif y répondra directement, l'utilisateur n'a aucune raison de cliquer.

## Pourquoi ce filtre tient

- Il **opérationnalise** [[concepts/data-proprietaire]] en décision binaire (créer / ne pas créer) au lieu de critère qualitatif flou
- Il **anticipe** la mécanique [[concepts/surprise-metric]] : un contenu reproductible par le modèle = gradient d'information ≈ 0 = oublié
- Il **canalise l'effort** vers les pages qui apportent un signal défensif réel (data terrain, pricing propriétaire, partenariats locaux, configurations stock)
- Il **élimine les pages-commodité** (FAQ génériques, guides quartiers, listes "10 choses à faire à X") qui consomment du budget de production sans ROI

## Application — cas Victoria Garden

7 idées de pages testées, 5 validées, 2 rejetées :

| Validées (data propriétaire requise) | Rejetées (substituable LLM) |
|---|---|
| Calculateur budget (prix réels + dispo) | Guide quartiers Bordeaux |
| Simulateur configuration (stock réel) | FAQ hébergement générique |
| Comparateur coût total (pricing vs marché) | |
| Planificateur séjour (partenariats locaux) | |
| Calendrier événements (offres VG liées) | |

## Connexion aux skills

- [[sources/2026-04-12-tim-skills-seo-proprietary]] — skill **product-led-seo** : le test de substitution est le critère d'entrée du skill (si une page passe le filtre, c'est qu'elle a une dimension produit / data / outil)
- skill **programmatique-pseo** : le test élimine les variantes de pages à variable creuse
- skill **brief-contenu** : à appliquer en amont du brief, pas après

## Articulation avec [[concepts/fully-meets]]

Une page qui passe le test de substitution est structurellement plus proche du Fully Meets : elle apporte une réponse que l'utilisateur ne pouvait obtenir ailleurs, donc il n'a pas besoin de continuer sa recherche.

## Limites

- **Seuil 80 % qualitatif** — pas de mesure objective. À calibrer par expérience du praticien.
- Test à refaire **périodiquement** : ce qu'un LLM ne sait pas générer aujourd'hui, il pourra le générer dans 6 mois (sauf si la donnée est strictement propriétaire et non scrapable).
- Ne dit rien sur le **volume de recherche** — une page peut passer le test mais cibler une intention sans demande.
- Un LLM peut sous-estimer ce qu'il produirait avec plus de contexte client → demander la production réelle, pas une description.

## Pages liées

[[sources/2026-04-13-victoria-garden-pseo]] (cas d'application : 5 validés / 2 rejetés) · [[sources/2026-04-13-prompt-pseo-non-produit]] (formalisation systémique : Étape 0 obligatoire + Test ChatGPT en 3 questions + 7 exemples pass/fail) · [[entities/victoria-garden]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/fully-meets]] · [[concepts/programmatique-pseo]] · [[concepts/product-led-seo]] · [[sources/2026-04-12-tim-skills-seo-proprietary]]
