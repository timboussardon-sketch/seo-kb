---
type: proof
title: "Preuve — Golfiller, résultats client instrumentés (avant/après mesuré)"
aliases: [preuve-golfiller-instrumentation, preuve-h009-golfiller]
tags: [preuve, terrain, client, golfiller, gsc, content-brain, data-proprietaire]
created: 2026-06-12
updated: 2026-07-10
sources: 2
confidence: medium
status: en-cours
hypothese: H-009
contenu: "[[briefs/2026-06-10-balle-golf-distance]]"
publie_le: 2026-06-10
jalon_30j: 2026-07-03
jalon_90j: 2026-09-08
---

# Preuve — Golfiller, résultats client instrumentés

> Fiche ouverte sur décision [[revue-hebdo/2026-W24]] point 2. Première fiche preuve adossée à un client payant : la baseline est déjà capturée (export GSC déposé le 2026-06-10, prédictions datées dans le ledger content-brain) — contrairement à [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] qui attend sa baseline depuis 4 semaines.

## Ce qu'on teste

Hypothèse liée : [[hypotheses#H-009]]. Les résultats commerciaux du discours Tim ([[sources/2026-04-13-cas-clients-resultats]], `confidence: medium`) doivent tenir sur un échantillon mesuré par une instrumentation tierce, pas seulement auto-rapporté. Golfiller est le cas test : chaque intervention sur le site est précédée d'une baseline GSC archivée et d'une prédiction chiffrée datée, résolue à échéance par la donnée — jamais par le ressenti.

## Cohorte et instrumentation

2 pages [[entities/golfiller]] instrumentées par le ledger content-brain (`content-brain/golfiller/ledgers/predictions.jsonl`), baselines issues de l'export `raw/data/exports-gsc/golfiller-2026-06-10/` :

| Prédiction | Page | Baseline GSC | Cible | Échéance |
|---|---|---|---|---|
| P-golfiller-2026-06-03-1 | `quelle-balle-de-golf-choisir` (refonte décisionnelle answer-first) | pos. 8,45 · 1 330 clics · 23 151 impressions | position moyenne < 5 sur la grappe « quelle balle de golf choisir » | J+30 = 2026-07-03 |
| P-golfiller-2026-06-03-2 | `quelle-balle-de-golf-choisir` | idem | CTR +20 % | J+90 = 2026-09-01 |
| P-golfiller-2026-06-10-1 | `balle-golf-distance` (page usage dédiée, [[briefs/2026-06-10-balle-golf-distance]]) | pos. 14,5 · 0 clic · 265 impressions | position < 10 sur « meilleure balle de golf pour la distance » | J+90 = 2026-09-08 |

## Prédiction chiffrée

Les prédictions falsifiables sont celles du ledger, reprises telles quelles ci-dessus (aucun chiffre ajouté par cette fiche). H-009 avance si, aux échéances, les résultats constatés en GSC sont archivés dans cette fiche **quels qu'ils soient** — c'est l'existence de la mesure tierce avant/après qui teste H-009, pas la réussite des prédictions elles-mêmes (qui, elles, nourrissent la doctrine answer-first / pages décisionnelles).

Falsification : si aux échéances aucune mesure n'est relevée (export non déposé, ledger non résolu), H-009 reste `en-test` puis repasse `ouvert` — le discours commercial reste auto-rapporté.

## Baseline (avant intervention)

Capturée. Source : export GSC manuel `golfiller-2026-06-10` (4 CSV : pages, requêtes, comparaisons 6 mois), répliquée dans le ledger content-brain au moment de chaque prédiction. Voir tableau cohorte ci-dessus.

## Mesure J+30

Échéance 2026-07-03 (P-golfiller-2026-06-03-1). **J+30 non mesuré.**

| Prédiction | Valeur constatée | Δ vs baseline | Verdict ledger |
|---|---|---|---|
| P-golfiller-2026-06-03-1 | non relevée (aucun export Golfiller déposé après le 2026-06-10) | — | `open`, non résolu à échéance |

Clause de falsification appliquée le 2026-07-10 ([[revue-hebdo/2026-W28]], conditionnel pré-arbitré [[revue-hebdo/2026-W27]] point 2) : [[hypotheses#H-009]] repasse `ouvert`. La fiche reste `en-cours` pour les seules échéances J+90 (2026-09-01 et 2026-09-08) : si les mesures sont relevées à ces dates, H-009 peut repasser `en-test` sur décision de revue.

## Mesure J+90

Échéances 2026-09-01 et 2026-09-08.

| Prédiction | Valeur constatée | Δ vs baseline | Verdict ledger |
|---|---|---|---|
| … | — | — | — |

## Verdict

_En attente. `concluante` / `non-concluante` / `bruitée` après le J+90 du 2026-09-08, ancré sur les chiffres GSC._

## Répercussion doctrine

- Effet sur [[hypotheses#H-009]] : `ouvert → en-test` (statut posé par cette fiche + revue-hebdo W24).
- Si les 3 prédictions sont résolues par la data aux échéances : H-009 passe `validé` pour le périmètre Golfiller — le discours commercial peut citer « résultats instrumentés », plus seulement « résultats constatés ». Extension à Victoria Garden (export `victoriagarden-2026-06-11` déjà déposé) à décider alors.
- Pages doctrine concernées : [[sources/2026-04-13-cas-clients-resultats]] · [[methodes/ranker-verticale-niche-sans-backlink]] · [[concepts/data-proprietaire]] · [[concepts/answer-first-pattern]].
- Entrée [[log]] : `## [2026-06-12] preuve | golfiller-instrumentation-client → en-cours (H-009 en-test)`

Pages liées : [[preuves/index]] · [[hypotheses]] · [[revue-hebdo/2026-W24]] · [[entities/golfiller]] · [[clusters/modeles-pseo-2026-06-10-golfiller]]
