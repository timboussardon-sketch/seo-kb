---
type: proof
title: "Preuve — Organikk, batch publié 2026-07-07 (data propriétaire vs exposition réelle)"
aliases: [preuve-organikk-batch-juillet, preuve-h007-batch-0707, preuve-guide-reddit]
tags: [preuve, terrain, organikk, gsc, data-proprietaire, geo, reddit, product-led]
created: 2026-07-10
updated: 2026-07-10
sources: 2
confidence: medium
status: gelée
hypothese: H-007
contenu: "https://organikk.co/blog/guide-reddit-seo-geo/"
publie_le: 2026-07-07
jalon_30j: 2026-08-06
jalon_90j: 2026-10-05
---

# Preuve — Organikk, batch publié le 2026-07-07

> Fiche ouverte sur décision [[revue-hebdo/2026-W28]] point 2. Elle relance le test de [[hypotheses#H-007]] dans les conditions exigées par [[revue-hebdo/2026-W25]] : attachée à un sprint de contenu Organikk réel (le batch est publié, pas planifié), avec une baseline qui existe avant la décision. Contrairement à [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] (gelée, baseline jamais capturée), l'instrument de mesure est en place : la propriété GSC `organikk.co` est connectée via l'edge `admin-gsc-export` de Fusionn, première donnée réelle servie au run indexation du 2026-07-10 ([[log]] 2026-07-10).

## Ce qu'on teste

Hypothèse liée : [[hypotheses#H-007]]. Le Retrieval Collapse (67 % du pool capte 80 % de l'exposition, NAVER, [[sources/2026-04-25-scan-arxiv-25-avril]]) frappe moins les pages qui portent une donnée propriétaire unique. Le batch du 2026-07-07 est le premier contenu Organikk publié avec de la data propriétaire explicite depuis que la mesure est possible.

## Cohorte

3 URLs publiées le 2026-07-07 ([[log]] 2026-07-07, entrée `publication`) :

| URL | Data propriétaire portée | Rôle dans le test |
|---|---|---|
| `/blog/guide-reddit-seo-geo/` | Playbook propriétaire (36 sources, captures GSC Qadence réelles), hub Do du sous-pilier GEO, 6 liens entrants déclarés | Page à data propriétaire forte |
| `/outils/probabilite-citation-llm` | Outil interactif sur data AI Overviews (product-led, [[queries/product-led-2026-07-07-organikk-anti-chatgpt]]) | Page outil, clic obligatoire |
| `/blog/automatiser-audit-seo-claude-code` | Méthode propriétaire, sans donnée chiffrée unique | Comparateur interne (data faible) |

Le comparateur externe (pages du site sans data propriétaire, ancienneté comparable) sera fixé au J+30 à partir du pull site entier, pas avant — on ne choisit pas son comparateur après avoir vu les chiffres de la cohorte seule.

## Baseline (avant intervention)

Structurelle : les 3 URLs sont neuves, publiées le 2026-07-07. Aucun historique GSC antérieur possible. État du site au moment de la publication, mesuré au run indexation du 2026-07-10 : 437 impressions et 17 clics sur 28 jours pour les 146 URLs du sitemap, exposition quasi intégralement brandée (`reports/indexation-organikk-2026-07-10.md`). Toute impression non brandée captée par la cohorte sera donc un delta net, pas une continuation.

## Ce qui tranche

À J+30 (2026-08-06) et J+90 (2026-10-05), archiver ici pour chaque URL : impressions, clics, position, part de requêtes non brandées (pull edge `admin-gsc-export`), et les citations IA constatées sur les requêtes de la grappe Reddit/GEO ([[concepts/metriques-visibilite-geo]]). H-007 avance si les mesures sont archivées aux échéances **quelles qu'elles soient** — et elle se renforce si les deux pages à data propriétaire sur-exposent le comparateur interne à data faible.

Falsification : si à une échéance aucun pull n'est archivé dans cette fiche, la clause [[revue-hebdo/2026-W27]]/W28 s'applique sans nouveau débat — fiche gelée, H-007 repasse `ouvert`. Aucun chiffre estimé, jamais (§5.4).

## Mesure J+30

Échéance 2026-08-06 — **manquée, fiche gelée** ([[revue-hebdo/2026-W32]] point 2). Aucun pull `searchAnalytics` archivé à l'échéance : la table reste vide. `reports/indexation-organikk-2026-08-03.md` confirme l'edge `admin-gsc-export` inaccessible depuis l'environnement de run du loop `indexation-check` (24 jours d'ouverture au 08-03, `loops/indexation-check/memory/questions.md`), mais le pull manuel via `preuves/SETUP-GSC` n'a pas non plus été fait. H-007 repasse `ouvert`. J+90 reste actif.

| URL | Impressions | Clics | Position | Part non brandée | Citations IA |
|---|---|---|---|---|---|
| … | — | — | — | — | — |

## Mesure J+90

Échéance 2026-10-05.

| URL | Impressions | Clics | Position | Part non brandée | Citations IA |
|---|---|---|---|---|---|
| … | — | — | — | — | — |

## Verdict

_En attente. `concluante` / `non-concluante` / `bruitée` après le J+90 du 2026-10-05, ancré sur les chiffres GSC._

## Répercussion doctrine

- Effet sur [[hypotheses#H-007]] : `ouvert → en-test` (statut posé par cette fiche + revue-hebdo W28).
- Effet sur [[contradictions#C-003]] : l'instrument de mesure existe désormais — la contradiction reste `en-cours` mais son blocage « zéro mesure » n'est plus structurel.
- Pages doctrine concernées : [[concepts/data-proprietaire]] · [[concepts/retrieval-collapse]] · [[sources/2026-06-19-playbook-reddit-seo-geo]] · [[queries/pseo-2026-07-07-organikk-corpus]].
- Entrée [[log]] : `## [2026-07-10] preuve | organikk-batch-juillet → en-cours (H-007 en-test)`

Pages liées : [[preuves/index]] · [[hypotheses]] · [[revue-hebdo/2026-W28]] · [[entities/qadence-seo-agent]] · [[concepts/parasite-seo]]
