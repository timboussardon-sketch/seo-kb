---
type: register
title: Revue hebdo — rituel de décision
aliases: [revue-hebdo, weekly-review, rituel-hebdo]
tags: [meta, rituel, revue, decision]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: living-doc
---

# Revue hebdo — rituel de décision

> À ne pas confondre avec deux choses voisines, laissées hors scope : la revue de presse quotidienne (newsletter Algorithme, skill `revue-presse-quotidienne`), et le lint d'hygiène hebdo (orphelins, frontmatter cassé, skill `audit-vault-hygiene` sur GH Actions). Ni l'`algorithme-recap-hebdo` qui synthétise les 5 revues de presse de la semaine.
>
> Ceci est le rendez-vous de décision du système. Sans lui, le système accumule sans jamais se reprendre en main : du backlog qui gonfle, des hypothèses qui dorment, des drafts jamais promus. C'est le seul moment où on tranche : quoi promouvoir, quoi tester, quoi ingérer, quoi archiver.
>
> Cadence : vendredi, via le skill `revue-hebdo`. Le mercredi, la résurgence (skill `resurgence-espacee`) prépare le terrain en remontant un concept oublié.

## Ce que la revue hebdo décide

1. **Promotions** : quels `draft` passent `stable`, quels `stable` deviennent `stale` (sujet SEO volatil > 12 mois)
2. **Hypothèses** : laquelle passe `en-test` cette semaine (une suffit), quelle [[preuves/index|fiche preuve]] ouvrir, voir [[hypotheses]]
3. **Backlog** : quel lot de [[ingest-backlog]] on ingère la semaine prochaine (P1 d'abord)
4. **Contradictions** : laquelle on ferme cette semaine, voir [[contradictions]]
5. **Archivage** : quel draft mort ou note périmée on sort du chemin
6. **Résurgence** : le concept remonté mercredi est-il toujours juste, à challenger, à mettre à jour ?
7. **Fil rouge** : un sujet revient-il assez pour mériter un pilier, un post, une prise de position ?

## Distinction avec les autres routines hebdo

| Routine | Quand | Rôle | Hors scope ici |
|---|---|---|---|
| `revue-presse-quotidienne` | quotidien 09:00 | newsletter Algorithme | oui (Tim) |
| `audit-vault-hygiene` | dimanche (GH Actions) | lint technique du vault | oui (Tim) |
| `algorithme-recap-hebdo` | dimanche (GH Actions) | synthèse des 5 revues presse | non, existant |
| **`revue-hebdo`** | **vendredi** | **décisions PKM** | **c'est cette page** |
| `resurgence-espacee` | mercredi | remonte 1 concept oublié | nourrit cette page |

## Éditions

| Semaine | Édition | Décisions clés |
|---|---|---|
| 2026-W20 | [[revue-hebdo/2026-W20]] | rrf draft→stable · H-007 en-test · lot ingest = keyword-research 2026-05-02 · C-002 à fermer (OpenDecoder) · data-proprietaire frontmatter corrigé · fil rouge = moat mis à l'épreuve |
| 2026-W21 | [[revue-hebdo/2026-W21]] | semaine de consolidation · 0 promotion · aucune hypothèse en-test (déblocage H-007/baseline GSC priorisé) · lot ingest = report keyword-research 2026-05-02 · C-007 à fermer · brief info-gain archivé · résurgence non tournée · fil rouge = doctrine de sélection des mots-clés |
| 2026-W22 | [[revue-hebdo/2026-W22]] | 3 carry-overs W21 tous non exécutés → tranche le mécanisme d'exécution (déc. 8) · brief info-gain **archivé en séance** · H-007 débloquée par export GSC manuel (pas service account) · lot ingest kw-research 3ᵉ reconduction + relancer sweep · C-007 = poser la définition « skill propriétaire » avant le décompte · résurgence muette 2 mercredis (diag ops) · fil rouge sélection mots-clés **productisé** (Fusionn + lead magnet) |
| 2026-W23 | — | **pas d'édition** (rituel sauté, constaté en W24) |
| 2026-W24 | [[revue-hebdo/2026-W24]] | 7 mouvements de registre **exécutés en séance** · H-009 `en-test` (fiche [[preuves/2026-06-12-golfiller-instrumentation-client]], 1ʳᵉ baseline capturée avant décision) · H-007 dernière fenêtre 72 h sinon `ouvert` en W25 · binôme kw-research → skip documenté (4ᵉ non-exécution) · lot W25 = golfiller-strat + etude-ctr-ai-overviews · C-012 fermée, C-007 `acceptée`, C-002 requalifiée `ouverte` · post LinkedIn 2026-05-05 archivé · reco 2 promotions `methodes/*` draft→stable · fil rouge = **instrumentation client** (déclencheur éditorial J+30 Golfiller 2026-07-03) |
| 2026-W25 | [[revue-hebdo/2026-W25]] | revue d'**exécution de conditionnels W24** : 3 actions Tim non faites mais pré-arbitrées · **2 promotions `methodes/*` draft→stable** flippées en séance · **H-007 `en-test→ouvert`** (export Organikk jamais déposé, fiche gelée `baseline-jamais-capturee`) · aucune nouvelle hypothèse en test (pas de fiche preuve) · lot ingest golfiller-strat + etude-ctr **1ʳᵉ reconduction (W26)** sinon skip · C-003 corrigée (zéro mesure réel, pas progression fictive) · rien à archiver, mislabel `revues-presse/2026-04-13`→hygiène · **résurgence Grounding Score 06-12 exécutée** (opérationnalisation + sources 6→11 + confidence→medium) · mercredi 06-17 muet (ticket ops) · fil rouge neuf = **parasite SEO/GEO Reddit+X+Grok** (cas test Qadence, gelé sur baseline) |

Chaque édition est filée dans `revue-hebdo/YYYY-Www.md` et résumée dans cette table.

Pages liées : [[000-home]] · [[hypotheses]] · [[contradictions]] · [[ingest-backlog]] · [[preuves/index]] · [[log]]
