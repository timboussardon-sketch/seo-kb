---
type: proof
title: "Preuve — Directories Data IA : guide des évaluateurs + mises à jour Google"
aliases: [preuve-directories-guide-google, preuve-qrg-organikk]
tags: [preuve, terrain, organikk, directories-data-ia, geo, gsc, quality-raters]
created: 2026-07-17
updated: 2026-07-17
sources: 1
confidence: low
status: baseline-capturee
hypothese: H-011
contenu: "https://organikk.co/guide-evaluateurs-google"
publie_le: 2026-07-17
jalon_30j: 2026-08-16
jalon_90j: 2026-10-15
---

# Preuve — Directories Data IA : guide des évaluateurs + mises à jour Google

> Fiche ouverte à la publication, le jour même. Baseline capturée par construction : 129 URLs neuves, zéro historique GSC. C'est exactement ce qui a manqué à [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]], gelée « baseline jamais capturée ».

## Ce qu'on teste

Hypothèse liée : [[hypotheses#H-011]]. La doctrine [[concepts/directories-data-ia]] dit qu'on ne part pas du volume de recherche humain mais du manque de l'IA : quelle matière cite-t-elle, et où cette matière manque-t-elle ou est-elle mal structurée ? On la produit datée, sourcée, extractible, et on devient la source citée.

Le cas est net parce que le manque se mesure. Google publie ses *General Guidelines* en un PDF anglais de 182 pages, version du 11 septembre 2025. Les moteurs génératifs le citent de mémoire, se trompent de version et mélangent les critères. Personne ne le publie en français, section par section, daté et lié à la page exacte.

## Cohorte

Deux directories, 129 URLs publiées le 2026-07-17 (commit `53e6cdd`, repo `organikk-next`).

**Guide des évaluateurs, 101 pages + page de référence** : `https://organikk.co/guide-evaluateurs-google`. Une page par section utile du PDF, avec la traduction française, le texte d'origine en regard et un lien vers la page exacte du document. Les pages les mieux notées à l'audit interne : `fully-meets` (9,6), `notation-sur-l-echelle-needs-met` (9,6), `experience-expertise-authoritativeness-trust` (9,6), `sujets-your-money-or-your-life` (9,0), les quatre sections sur les abus (9,3).

**Mises à jour Google, 26 pages + page de référence** : `https://organikk.co/mises-a-jour-google`. Une page par déploiement, calculée depuis les 41 entrées du Search Status Dashboard.

## Ce qui est mesurable, et ce qui ne l'est pas

Mesurable : impressions, clics et positions GSC sur les requêtes où l'IA répond aujourd'hui de travers (« fully meets », « needs met », « quality rater guidelines », « scaled content abuse », « site reputation abuse »). Propriété `organikk.co` connectée via l'edge `admin-gsc-export` de Fusionn, le même instrument que [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]].

Non mesurable proprement : les citations IA elles-mêmes. Tim a déjà rejeté les relevés de citations comme modèle industrialisable (trop cher, trop périssable, cf. [[feedback-corpus-avant-pages]] côté mémoire agent). Un relevé ponctuel daté reste possible au J+90, en étude, pas en routine.

## Baseline au 2026-07-17

| Métrique | Valeur | Source |
|---|---|---|
| URLs publiées | 129 | build Next, 362 pages générées |
| Impressions GSC sur ces URLs | 0 | URLs neuves, zéro par construction |
| Positions | aucune | idem |
| Indexation | 0 | sitemap soumis, indexation manuelle sur 7 URLs prioritaires |

## Ce qui rend cette cohorte propre

Le corpus sert le produit et la page. Le JSON des 151 sections alimente déjà le moteur `/outils/quality-rater-guidelines` ; les pages en sont le sous-produit, coût marginal quasi nul. C'est le pattern « corpus d'abord, pages ensuite ».

Aucune prose n'est rédigée dans ces pages. Les mises à jour se calculent depuis la donnée (chevauchements, classement par durée, voisins). Le guide rend le texte de Google et sa traduction. L'hallucination est structurellement impossible : il n'y a rien à halluciner.

Le travail a corrigé deux erreurs du corpus au passage : la fiche `raw/papers/google-quality-raters-guidelines-2026.md` datait le document « Édition 2026 » alors que la version en ligne est celle du 11 septembre 2025, et deux titres français ne correspondaient pas à leur section (11.0 et 12.0).

## Clause de falsification

Pré-arbitrée, même règle que [[hypotheses#H-007]] : pas de pull GSC archivé au J+30 (2026-08-16) → fiche gelée, H-011 repasse `ouvert` sans débat.

## Jalons

- **J0, 2026-07-17** : baseline capturée, ci-dessus.
- **J+30, 2026-08-16** : à renseigner. Indexation effective des 129 URLs, premières impressions.
- **J+90, 2026-10-15** : à renseigner. Positions, et relevé ponctuel de citations IA sur les 5 requêtes cibles.

## Pages liées

[[concepts/directories-data-ia]] · [[concepts/information-gain]] · [[concepts/data-proprietaire]] · [[entities/quality-raters-guidelines]] · [[entities/organikk-co]] · [[hypotheses#H-011]] · [[preuves/index]]
