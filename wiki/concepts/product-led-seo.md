---
type: concept
title: Product-Led SEO
aliases: [product-led-seo, pls, product-led]
tags: [pseo, product-led, fully-meets, calculateur, simulateur, doctrine-tim]
created: 2026-04-13
updated: 2026-04-13
sources: 4
confidence: high
status: stable
---

# Product-Led SEO

**Définition opérationnelle Tim** : produire des pages dont **le produit lui-même** (calculateur, simulateur, comparateur, outil interactif, configurateur) est la valeur — pas le contenu écrit autour. La page est la fonctionnalité.

## Principe

Au lieu d'écrire *"comment calculer son budget vacances"*, on **embarque le calculateur dans la page**. L'utilisateur n'a plus besoin de lire un article puis de chercher un outil — la réponse à sa requête est l'outil lui-même.

Score [[concepts/fully-meets]] structurellement maximisé : la requête Do (*"calculer X"*, *"comparer Y"*, *"simuler Z"*) trouve sa réponse dans la page sans recherche supplémentaire — exactement la définition normative QRG ([[sources/2026-04-13-google-quality-raters-guidelines-2026]]).

## Articulation avec [[concepts/test-substitution-llm]]

Le Product-Led SEO est l'**extrême du test de substitution** : la page contient un composant interactif fonctionnel que ChatGPT ne peut pas reproduire, par construction. C'est la stratégie défensive la plus solide face aux LLM génératifs.

Formes acceptables de produit embarqué (cf. [[sources/2026-04-13-prompt-pseo-non-produit]]) :

- Calculateur avec inputs personnalisés
- Simulateur avec variables ajustables
- Comparateur côte à côte avec données temps réel
- Configurateur (le produit du site directement dans la page)
- Générateur (template à télécharger après inputs)
- Data viz interactive (graphes, cartes, timelines)
- Fonctionnalité de persistance (sauvegarde, tracking, progression)

## Sources ingérées (4)

- [[sources/2026-04-12-tim-skills-seo-proprietary]] — skill `seo-product-led-seo` officiel
- [[sources/2026-04-13-prompt-pseo-produit-service]] — méga-prompt produit/service
- [[sources/2026-04-13-prompt-pseo-non-produit]] — méga-prompt non-produit (Règle 0 = product-led obligatoire)
- [[sources/2026-04-13-victoria-garden-pseo]] — 4 des 5 modèles validés sont product-led (calculateur budget, simulateur configuration, comparateur coût, planificateur séjour)

## Cas Victoria Garden

5 modèles validés sur 7, dont 4 product-led purs :

| Modèle | Composant produit-led |
|---|---|
| Calculateur Budget Séjour | calculateur avec inputs durée/personnes/type/saison |
| Simulateur Configuration | simulateur recommandant config parmi stock réel |
| Comparateur Coût Total | tableau interactif comparatif VG / hôtel / Airbnb |
| Planificateur Séjour Thématique | planning généré par thème + offres associées |

Le 5e modèle (Calendrier Événements) est **mixte** : product-led partiel (offres VG dynamiques par événement) + contenu éditorial (description événements).

## Différence avec contenu éditorial standard

| Éditorial | Product-Led |
|---|---|
| Texte qui décrit comment faire X | Outil qui fait X |
| Conversion : lien CTA en bas | Conversion : à la fin de l'usage de l'outil |
| Reproductible par LLM textuel | Non reproductible (composant fonctionnel) |
| Coût rédactionnel | Coût de dev (souvent + élevé en initial, < en marginal) |

## Limites

- **Coût de dev** non trivial : un calculateur qui marche demande dev front + données back + maintenance
- Pas tous les sujets s'y prêtent (un sujet purement informationnel ne devient pas un outil)
- Risque de complexité UX : un outil mal conçu performe moins bien qu'un article clair
- Données nécessaires temps réel pour certains modèles (dispo, prix) — implique intégration API

## Pages liées

[[sources/2026-04-13-prompt-pseo-produit-service]] · [[sources/2026-04-13-prompt-pseo-non-produit]] · [[sources/2026-04-13-victoria-garden-pseo]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-13-google-quality-raters-guidelines-2026]] · [[concepts/programmatique-pseo]] · [[concepts/test-substitution-llm]] · [[concepts/fully-meets]] · [[concepts/data-proprietaire]]
