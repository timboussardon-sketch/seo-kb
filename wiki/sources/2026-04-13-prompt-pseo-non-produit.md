---
type: source
source_type: doctrine
title: Prompt pSEO — Sites Non-Produit (Média / Éditorial / Communautaire)
aliases: [prompt-pseo-non-produit, mega-prompt-pseo-media]
tags: [doctrine, prompt, pseo, programmatique, media, editorial, test-substitution-llm]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Prompt pSEO — Sites Non-Produit (Média / Éditorial / Communautaire)

**Auteur** : Timothée Boussardon
**Type** : prompt opérationnel (`source_type: doctrine`)
**Fichier raw** : `raw/notes/prompt-pseo-non-produit.md`
**Cible d'usage** : médias, blogs d'autorité, annuaires, comparateurs indépendants, communautés, bases de données publiques — **revenu publicitaire / affiliation / notoriété, sans offre produit/service directe**

---

## Contexte

Variante du méga-prompt [[sources/2026-04-13-prompt-pseo-produit-service]] adaptée aux sites **sans moat naturel produit**. Différence structurante : intègre une **Étape 0 — Test de Substitution LLM obligatoire** avant de valider tout modèle de page, et une **Règle 0 anti-substitution** non-négociable.

## Pourquoi ce prompt existe séparément

Un site non-produit n'a aucun moat défensif naturel : tout son contenu textuel est reproductible par un LLM. Sans composant interactif ou données temps réel, la page n'a aucune raison d'exister face à ChatGPT. Le test de substitution devient **vital, pas optionnel**.

> *"Un site produit/service a un moat naturel : ses données propriétaires (prix, stock, clients). Le produit lui-même est la valeur. Un site non-produit n'a aucun moat naturel."* — Tim

## Étape 0 — Test ChatGPT en 3 questions

Pour chaque idée de modèle, AVANT toute production :

1. *"Un utilisateur peut-il obtenir un résultat ÉQUIVALENT en tapant un prompt sur ChatGPT/Claude/Gemini ?"* → Si OUI → **éliminé**
2. *"Est-ce que la page propose un OUTIL INTERACTIF, une DATA VIZ, un COMPARATIF STRUCTURÉ ou une FONCTIONNALITÉ EMBARQUÉE qu'un LLM textuel ne peut pas reproduire ?"* → Si NON → **éliminé**
3. *"Est-ce que la page a une raison d'EXISTER dans un navigateur plutôt que dans un chat IA ?"* → Si NON → **éliminé**

Cf. [[concepts/test-substitution-llm]] (concept formalisé à partir de [[sources/2026-04-13-victoria-garden-pseo]], étendu ici en méthode systémique).

### Ce qui passe (7 exemples)

Calculateurs interactifs · Comparateurs côte à côte temps réel · Data viz (graphes, timelines, cartes) · Outils fonctionnels embarqués · Agrégateurs multi-sources avec filtres · Templates/générateurs téléchargeables · Simulateurs avec variables ajustables.

### Ce qui ne passe pas (7 exemples)

Listes "Top X" · Résumés/explications de concepts · Q/R textuelles · *"Que dit X sur Y"* · Guides étape par étape pur texte · Biographies/fiches descriptives · Définitions/glossaires textuels.

→ Tous ces formats : *"ChatGPT fait mieux"*.

## 7 règles non-négociables (vs prompt produit/service : +1 règle)

**Règle 0 nouvelle** — **Anti-substitution LLM** : chaque page DOIT contenir au moins UN élément interactif ou data-driven non reproductible par un LLM textuel. 7 formes acceptables documentées : outil interactif, data viz, comparatif structuré, produit embarqué, données propriétaires agrégées, fonctionnalité de persistance, contenu multimodal.

Règles 1 à 7 identiques au prompt produit/service (contenu unique, zéro hallucination, sourcing, canonical, maillage, Surprise Score, Grounding Score).

## Output attendu — différences vs prompt produit/service

- Section initiale obligatoire : **Test de Substitution LLM (Étape 0)** avec tableau de validation/élimination de chaque idée
- Pour chaque modèle : ajout d'un champ **"Composant Interactif Central"** dans le template
- Pour chaque modèle : ajout d'un **"Score de substitution LLM"** dans la section SEO & Intent
- Pour chaque modèle : ajout d'un **"Avantage compétitif vs LLM"** explicite
- Matrice de priorisation : ajout colonne **"Moat vs LLM"**

## Tableau différentiel (du prompt lui-même)

| Aspect | Prompt produit/service | Ce prompt non-produit |
|---|---|---|
| Étape 0 — Test LLM | Absente | **Obligatoire** avant tout modèle |
| Règle 0 — Anti-substitution | Absente | **Règle 0** non-négociable |
| Composant interactif | Recommandé | **Obligatoire** par modèle |
| Colonne "Moat vs LLM" | Non | Oui matrice |
| Score substitution | Non | Oui section SEO |
| Exemples pass/fail | Non | 7 + 7 documentés |

## Limites

- Le test ChatGPT en 3 questions repose sur une **évaluation humaine subjective** — pas de seuil quantifiable
- Risque d'éliminer prématurément des modèles dont la valeur tient au volume + maillage + autorité plutôt qu'à un composant interactif
- Pas d'évaluation économique du composant interactif (coût de dev parfois > ROI SEO sur un modèle nichée)
- Test à refaire périodiquement : capacités LLM évoluent

## Pages liées

**Concepts** : [[concepts/test-substitution-llm]] (méthode formalisée) · [[concepts/programmatique-pseo]] · [[concepts/product-led-seo]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/fully-meets]]

**Sources** : [[sources/2026-04-13-prompt-pseo-produit-service]] (variante produit/service sans étape 0) · [[sources/2026-04-13-victoria-garden-pseo]] (cas où le test substitution a éliminé 2/7 idées) · [[sources/2026-04-12-tim-skills-seo-proprietary]]
