---
type: source
source_type: doctrine
title: Prompt pSEO — Sites Produit / Service (méga-prompt opérationnel Tim)
aliases: [prompt-pseo-produit-service, mega-prompt-pseo-produit]
tags: [doctrine, prompt, pseo, programmatique, product-led, template, e-commerce, saas]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Prompt pSEO — Sites Produit / Service

**Auteur** : Timothée Boussardon
**Type** : prompt opérationnel (`source_type: doctrine`)
**Fichier raw** : `raw/notes/prompt-pseo-produit-service.md`
**Cible d'usage** : sites e-commerce, SaaS, agences, prestataires, hébergement, formation — **toute offre produit/service identifiée**

---

## Contexte

Méga-prompt système qui produit une **stratégie pSEO complète** à partir d'un site avec offre produit/service. Pendant doctrinal du livrable Victoria Garden ([[sources/2026-04-13-victoria-garden-pseo]]) — c'est le prompt qui peut générer ce type de stratégie sur n'importe quel client e-commerce/SaaS/service.

## Structure du prompt

Le prompt est encadré par 5 balises XML :

- **`<role>`** — Stratège pSEO + Growth Engineering (data → template → pages + intent → SERP → conversion)
- **`<context>`** — URL, description, datasets, pages existantes, concurrents, objectifs business, personas
- **`<task>`** — 5 étapes : modèles scalables (min 5) → matrice de priorisation → mots-clés par modèle → plan 90j → résumé exécutif
- **`<rules>`** — 7 règles non-négociables (cf. ci-dessous)
- **`<constraints>`** — exclusions, anti-cannibalisation, cible précise, ton

## 7 règles non-négociables

1. **Contenu unique obligatoire** — template = structure, jamais texte. Si 2 pages partagent >30% de texte → échec.
2. **Données terrain, zéro hallucination** — aucune donnée non vérifiable n'apparaît. Pas d'invention de chiffres.
3. **Sourcing obligatoire** — toute donnée chiffrée a sa source datée <3 ans. Sinon : qualitatif ou placeholder `[DONNÉE À SOURCER]`.
4. **Canonical propre** — 1 URL = 1 contenu = 1 canonical, zéro doublon technique.
5. **Maillage interne différenciant** — graphe de liens unique par page.
6. **Surprise Score** — chaque section apporte au moins 1 élément High Surprise. Application directe de [[concepts/surprise-metric]] et [[concepts/surprise-gap]] (Titans/MIRAS).
7. **Grounding Score** — passage ancré 150-200 mots + bloc authorship algorithmique ~50 mots par page. Application directe de [[concepts/grounding-score]] et [[concepts/passage-ranking]] (Triade SERP).

## Output attendu (format strict)

Le prompt impose un format de sortie verrouillé : Principe (3 lignes) → Modèle 1 à 5 (architecture / template / SEO & intent / avantage compétitif) → Matrice de priorisation → Mots-clés par modèle → Plan 90j → Métriques → Résumé exécutif.

## Pourquoi ce prompt n'a PAS d'étape 0 substitution LLM

Tim distingue explicitement deux cas (cf. [[sources/2026-04-13-prompt-pseo-non-produit]]) : un site produit/service a un **moat naturel** dans ses données propriétaires (prix, stock, clients). Le produit lui-même est la valeur. Le test de substitution est moins critique car le LLM ne peut pas vendre le produit du client.

## Position dans le système

Les 2 prompts pSEO ([[sources/2026-04-13-prompt-pseo-produit-service]] et [[sources/2026-04-13-prompt-pseo-non-produit]]) opérationnalisent le **skill `seo-programmatique-pseo`** et le **skill `seo-product-led-seo`** documentés dans [[sources/2026-04-12-tim-skills-seo-proprietary]]. Ils sont l'interface concrète skill → livrable.

## Limites

- Prompt template — performance dépend du remplissage rigoureux des `[CROCHETS]` du `<context>`
- Pas de mécanisme de fallback si une donnée propriétaire annoncée n'existe pas vraiment côté client
- Ne définit pas le format des wireframes attendus (laissé libre au modèle)
- Sourcing règle 3 : <3 ans peut être trop strict pour certains secteurs réglementaires stables

## Pages liées

**Concepts** : [[concepts/programmatique-pseo]] · [[concepts/product-led-seo]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/passage-ranking]] · [[concepts/anti-ai-writing]]

**Sources** : [[sources/2026-04-13-prompt-pseo-non-produit]] (variante non-produit avec étape 0 substitution) · [[sources/2026-04-13-victoria-garden-pseo]] (premier livrable client de ce type) · [[sources/2026-04-12-tim-skills-seo-proprietary]]
