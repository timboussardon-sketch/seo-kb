---
title: "seo-preparation-semantique : la matière du brief sans Surfer"
bootcamp: 4
type: exercice
session: 2
skill: seo-preparation-semantique
cowork: oui
created: 2026-06-09
---

# seo-preparation-semantique : la matière du brief sans Surfer

**Pré-requis** : le skill seo-preparation-semantique installé. Une requête + du contexte client (calls, verbatims).

## Le cas

Remplace Surfer / NeuronWriter. À partir d'une requête et de ta data, le skill sort la matière sémantique (entités pondérées, gap, Surprise Score) qui alimente le brief et la rédaction, sans scraper le SERP.

## Ce que tu dois faire

**1. Donne la requête + ta data**
La requête et tes verbatims/calls.

**2. Lance le skill**

```text
Lance seo-preparation-semantique sur [requête]. Voici ma data : [colle].
Sors les entités pondérées, le gap, le Surprise Score et une reco H1/H2.
```

**3. Verse dans ton brief**
Cette matière nourrit seo-brief-contenu.

## Ce que tu dois obtenir — le « screen »

```
PRÉPARATION SÉMANTIQUE — [requête]

Entités pondérées : facture (1.0), URSSAF (0.8), mention légale (0.7)...
Gap : personne ne traite "facture électronique obligatoire 2026".
Surprise Score : moyen → ajouter un angle data propriétaire.
Reco : H1 sur l'intention principale, H2 sur le gap.
```

## Vérifier que tu as réussi

- [ ] Entités pondérées par importance.
- [ ] Gap analysis (ce qui manque).
- [ ] Surprise Score estimé.
- [ ] Reco H1/H2.

## Le piège

Croire que c'est l'article. C'est la matière brute, pas le contenu final. Elle nourrit le brief, elle ne le remplace pas.

## Comment ça marche

Le skill modélise l'espace sémantique de la requête à partir de ta data plutôt que du SERP, ce qui te donne l'angle (gap + surprise) que les outils qui copient le SERP ne voient pas.
