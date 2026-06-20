---
type: proof
title: "Preuve — pSEO secteur×ville Organikk vs Retrieval Collapse"
aliases: [preuve-pseo-secteur-ville-data-proprietaire]
tags: [preuve, terrain, pseo, organikk, data-proprietaire, gsc]
created: 2026-05-16
updated: 2026-06-19
sources: 1
confidence: low
status: baseline-jamais-capturee
hypothese: H-007
contenu: "[[queries/pseo-2026-05-13-organikk-secteur-ville]]"
publie_le: 2026-05-13
jalon_30j: 2026-06-15
jalon_90j: 2026-08-14
---

# Preuve — pSEO secteur×ville Organikk vs Retrieval Collapse

> Fiche ouverte sur décision [[revue-hebdo/2026-W20]] point 2. Cohorte de test disponible sans attendre le déploiement du cluster ([[contradictions#C-003]]) : les pages pSEO secteur×ville déjà en ligne sur Organikk.
>
> **Baseline jamais capturée — fiche gelée le 2026-06-19 ([[revue-hebdo/2026-W25]]).** Aucun export GSC `organikk.co` n'a été déposé entre l'ouverture (2026-05-16) et le J+30 (2026-06-15). H-007 est repassée `ouvert`. La fiche reste ici comme trace ; elle ne se rouvre qu'attachée à un sprint de contenu Organikk réel, avec capture de baseline AVANT intervention (le modèle qui a marché pour [[preuves/2026-06-12-golfiller-instrumentation-client|Golfiller]]).

## Ce qu'on teste

Hypothèse liée : [[hypotheses#H-007]]. Une page qui porte une donnée propriétaire unique (chiffres INSEE/CCI sourcés ville par ville, simulateur sectoriel codé, inversions de doctrine Boussardon) est moins frappée par le Retrieval Collapse qu'une page générique sur la même intention : elle garde une exposition réelle (citations IA, impressions) là où le contenu reformulable se noie dans le pool synthétique.

## Cohorte

5 pages pSEO secteur×ville publiées sur Organikk (réf. [[queries/pseo-2026-05-13-organikk-secteur-ville]]) :

- `strategie-seo-serrurier-lyon`
- `strategie-seo-agence-immobiliere-lyon`
- `paysagiste-paris`
- `hotel-paris`
- `avocat-paris`

Cohorte live au plus tard le 2026-05-13 (date de la query + constat revue-hebdo W20). Dates exactes de publication par page à relever dans `organikk-next/src/data/articles.ts` au moment de la baseline GSC. Critère d'inclusion : chaque page porte au moins 2 des 4 leviers propriétaires (données terrain ville, simulateur Product-Led, inversions doctrine, authorship Organikk) — test de substitution LLM passé, cf. query §0.

Comparatif : exposition de ces pages sur leurs requêtes cibles (`stratégie seo {secteur} {ville}` + cluster décisionnel Pattern A) vs le contenu générique déjà en place sur les mêmes requêtes (incumbents SERP / réponses IA sans data terrain).

## Prédiction chiffrée

À J+90, sur la requête cible primaire de chaque page, la page propriétaire atteint **soit une position Google ≤ 15, soit ≥ 1 citation par un moteur génératif** (ChatGPT / Perplexity / AI Mode), pour **au moins 3 des 5 pages**, avec une part d'exposition (citations + impressions GSC) strictement supérieure au contenu générique concurrent sur la même requête.

Falsification : si à J+90 aucune page propriétaire ne dépasse le contenu générique concurrent en exposition (citations et impressions indiscernables, ou pages absentes de l'index), H-007 est invalidé — le `confidence: high` de [[concepts/data-proprietaire]] doit baisser et une entrée [[contradictions]] s'ouvre.

Périmètre : la prédiction falsifiable porte sur H-007 seule (décision revue-hebdo W20 : « une seule, et c'est celle-là »). La même cohorte pourra plus tard alimenter [[hypotheses#H-002]] (Surprise Gap) et [[hypotheses#H-003]] (Grounding Score) — hors scope de cette fiche tant que H-007 n'a pas tranché.

## Baseline (avant publication)

Non capturée. La boucle GSC est inerte tant que le service account n'est pas déposé ([[preuves/SETUP-GSC]]) — log 2026-05-16, fermeture des 3 boucles. Aucune estimation inventée (règle §5.4).

| Métrique | Valeur de départ | Source de mesure |
|---|---|---|
| Position Google requête cible | _en attente baseline GSC_ | GSC |
| Citations IA (ChatGPT / Perplexity / AI Mode) | _en attente constat manuel_ | constat manuel |
| Impressions GSC requêtes cibles | _en attente baseline GSC_ | GSC |

Action déclenchante : déposer le service account GSC, capturer la baseline rétroactive sur les 5 URLs, renseigner ce tableau. Tant que la baseline manque, la fiche reste `en-cours` et H-007 ne peut pas passer `validé`/`invalidé` — seulement `en-test`.

## Mesure J+30

Échéance 2026-06-15.

| Métrique | Valeur | Δ vs baseline |
|---|---|---|
| … | — | — |

## Mesure J+90

Échéance 2026-08-14.

| Métrique | Valeur | Δ vs baseline |
|---|---|---|
| … | — | — |

## Verdict

_En attente. `concluante` / `non-concluante` / `bruitée` à trancher après J+90, ancré sur les chiffres, sans enrobage._

## Répercussion doctrine

- Effet sur [[hypotheses#H-007]] : `ouvert → en-test` (statut posé par cette fiche + revue-hebdo W20). Passage à `validé`/`invalidé` conditionné à la baseline GSC puis aux jalons.
- Pages doctrine concernées si verdict : [[concepts/data-proprietaire]] (hub 98 backlinks, `confidence: high` non falsifié à ce jour), [[concepts/retrieval-collapse]].
- Si `non-concluante` : ouvrir une entrée [[contradictions]] pour la dette doctrinale du moat.
- Entrée [[log]] : `## [2026-05-16] preuve | pseo-secteur-ville-data-proprietaire → en-cours (H-007 en-test)`

Pages liées : [[preuves/index]] · [[hypotheses]] · [[contradictions]] · [[revue-hebdo/2026-W20]] · [[concepts/data-proprietaire]] · [[concepts/retrieval-collapse]]
