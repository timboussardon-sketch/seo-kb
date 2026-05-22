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
> Ceci est le rendez-vous de décision du second cerveau. Sans lui, le système accumule sans jamais se reprendre en main : du backlog qui gonfle, des hypothèses qui dorment, des drafts jamais promus. C'est le seul moment où on tranche : quoi promouvoir, quoi tester, quoi ingérer, quoi archiver.
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

Chaque édition est filée dans `revue-hebdo/YYYY-Www.md` et résumée dans cette table.

Pages liées : [[000-home]] · [[hypotheses]] · [[contradictions]] · [[ingest-backlog]] · [[preuves/index]] · [[log]]
