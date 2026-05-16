---
type: proof
title: "Preuve — [titre du contenu]"
aliases: []
tags: [preuve, terrain]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: 1
confidence: low
status: en-cours
hypothese: H-XXX
contenu: "[[sources/... ou raw/...]]"
publie_le: YYYY-MM-DD
jalon_30j: YYYY-MM-DD
jalon_90j: YYYY-MM-DD
---

# Preuve — [titre du contenu]

> Template. Copier vers `preuves/YYYY-MM-DD-slug.md`, remplir, ne jamais publier d'estimation non mesurée (règle §5.4 AGENTS.md).

## Ce qu'on teste

Hypothèse liée : [[hypotheses#H-XXX]]. En une phrase, la prédiction opérationnelle que ce contenu doit vérifier.

## Prédiction chiffrée

Quoi, de combien, à quelle échéance. Exemple de gabarit : "à J+90, la page est citée par au moins un moteur génératif sur la requête cible, et atteint le top 5 Google." La prédiction doit être falsifiable. Si on ne sait pas l'écrire de façon falsifiable, l'hypothèse n'est pas mûre.

## Baseline (avant publication)

| Métrique | Valeur de départ | Source de mesure |
|---|---|---|
| Position Google requête cible | — | GSC |
| Citations IA (ChatGPT / Perplexity / AI Mode) | — | constat manuel |
| Conversion / lead / réservation | — | mesure client |

## Mesure J+30

| Métrique | Valeur | Δ vs baseline |
|---|---|---|
| … | — | — |

Observations : ce qui bouge, ce qui ne bouge pas, variables confondantes éventuelles.

## Mesure J+90

| Métrique | Valeur | Δ vs baseline |
|---|---|---|
| … | — | — |

## Verdict

`concluante` / `non-concluante` / `bruitée`. Justification en deux phrases, ancrée sur les chiffres ci-dessus, sans enrobage.

## Répercussion doctrine

- Effet sur [[hypotheses#H-XXX]] : statut → … (et `confidence:` ajusté sur la/les pages doctrine concernées)
- Si `non-concluante` : ouvrir une entrée [[contradictions]] pour la dette doctrinale à corriger
- Entrée [[log]] : `## [YYYY-MM-DD] preuve | slug → verdict`

Pages liées : [[preuves/index]] · [[hypotheses]] · [[concepts/data-proprietaire]]
