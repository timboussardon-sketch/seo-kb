---
type: register
title: Banque de preuves
aliases: [preuves, banque-preuves, proof-bank, boucle-preuves]
tags: [meta, preuves, validation, terrain, moat, gsc]
created: 2026-05-16
updated: 2026-07-10
sources: 0
confidence: high
status: living-doc
---

# Banque de preuves

> La KB nourrit les articles, les newsletters, les briefs. Mais la performance de ces sorties ne revenait jamais dans le wiki : `gsc-export` à zéro fichier, `test-terrain` à un seul. La boucle qui rendrait la doctrine auto-corrigeante n'était pas branchée. On affirmait "data propriétaire" sans la prouver dans le vault.
>
> Une fiche preuve relie un contenu publié à l'hypothèse de [[hypotheses|doctrine]] qu'il teste, et suit sa performance à J+30 et J+90. C'est le seul mécanisme qui transforme [[concepts/data-proprietaire]] d'un argument commercial en fait opposable, et qui fait passer une [[hypotheses|hypothèse]] de `ouvert` à `validé` ou `invalidé`.
>
> Remplissage manuel pour l'instant : pas de pull GSC automatisé. Le skill `preuves-feedback` crée et met à jour les fiches à la demande, à partir de la data que Tim fournit (export GSC, citations IA constatées, mesures client). Quand un pull GSC sera branché, il alimentera ces mêmes fiches.

## Comment ça marche

1. Un contenu est publié (article Organikk, newsletter, page pSEO, livrable client)
2. On crée une fiche `preuves/YYYY-MM-DD-slug.md` depuis [[preuves/_template]]
3. On déclare l'hypothèse testée ([[hypotheses#H-XXX]]) et la prédiction chiffrée
4. On note la baseline (positions, citations IA, conversions avant)
5. À J+30 et J+90, on remplit la mesure réelle
6. On tranche : la prédiction tient ou pas
7. On répercute sur [[hypotheses]] (statut + `confidence:` sur les pages doctrine) et sur [[log]]

## Statuts des fiches

- `en-cours` : publié, en attente des jalons J+30 / J+90
- `concluante` : la prédiction tient, l'hypothèse liée avance vers `validé`
- `non-concluante` : la prédiction ne tient pas, l'hypothèse liée recule ou passe `invalidé`
- `bruitée` : mesure non exploitable (trop peu de volume, variable confondante), à rejouer

## Fiches

> Première fiche ouverte le 2026-05-16 (revue mensuelle `hypotheses-validation`, sur décision [[revue-hebdo/2026-W20]] point 2). Elle teste [[hypotheses#H-007]] (data propriétaire vs Retrieval Collapse) sur la cohorte pSEO secteur×ville déjà publiée. Statut `en-cours` : baseline GSC en attente du dépôt du service account ([[preuves/SETUP-GSC]]), aucune mesure inventée. Les newsletters récentes du [[ingest-backlog#priorité-2-contenu-publié-non-bouclé-boucle-preuves|backlog P2]] suivront.

| Fiche | Contenu | Hypothèse | Publié | Statut |
|---|---|---|---|---|
| [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] | 5 pages pSEO secteur×ville Organikk | [[hypotheses#H-007]] | ≤ 2026-05-13 | `en-cours` (gelée, baseline jamais capturée) |
| [[preuves/2026-06-12-golfiller-instrumentation-client]] | 2 pages Golfiller instrumentées (ledger content-brain + exports GSC) | [[hypotheses#H-009]] | 2026-06-10 | `en-cours` (J+30 non mesuré, J+90 seuls actifs) |
| [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]] | 3 URLs Organikk publiées le 2026-07-07 (guide Reddit, outil citation LLM, article audit) | [[hypotheses#H-007]] | 2026-07-07 | `en-cours` |
| [[preuves/2026-07-17-organikk-directories-guide-google]] | 129 URLs Organikk : guide des évaluateurs Google (101 pages) + mises à jour datées (26 pages) | [[hypotheses#H-011]] | 2026-07-17 | `en-cours` (baseline capturée à J0) |

## Données minimales par fiche

Pour qu'une fiche soit exploitable, il faut au moins une de ces sources de vérité (jamais d'estimation inventée, règle §5.4) :

- Export GSC sur l'URL (positions, impressions, CTR) avant / J+30 / J+90
- Citations IA constatées (ChatGPT, Perplexity, AI Mode) sur les requêtes cibles, croise [[concepts/metriques-visibilite-geo]]
- Mesure client tierce (réservations, leads, closing), croise [[sources/2026-04-13-cas-clients-resultats]] et [[hypotheses#H-009]]

Pas de data = la fiche reste `en-cours`, l'hypothèse reste `ouvert`. On ne valide jamais sur du ressenti.

Pages liées : [[hypotheses]] · [[contradictions]] · [[ingest-backlog]] · [[concepts/data-proprietaire]] · [[concepts/metriques-visibilite-geo]] · [[index]]
