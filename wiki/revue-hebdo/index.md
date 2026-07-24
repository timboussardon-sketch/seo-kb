---
type: register
title: Revue hebdo — rituel de décision
aliases: [revue-hebdo, weekly-review, rituel-hebdo]
tags: [meta, rituel, revue, decision]
created: 2026-05-16
updated: 2026-07-24
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
| 2026-W26 | [[revue-hebdo/2026-W26]] | **2 promotions entités-référence draft→stable** (karpathy, google-deepmind) exécutées · stable→stale 0 (vault < 3 mois) · **aucune hypothèse forcée en-test** (H-002 garderait le piège Organikk de H-007 — reste `ouvert`), H-009 J+30 le 2026-07-03 à préparer · lot W27 = `etude-ctr` + dossier Leexi **tirés par le travail réel** (newsletter + client), `golfiller-strat` **skip** (2ᵉ non-exécution, doctrine kw-research) · **C-011 `ouverte`→`acceptée`** (garde-fou chiffres glossaire, calque C-007) · rien de mort à archiver · **résurgence surprise-gap exécutée** : `confidence high→medium` (aligné sur la section Limites, H-002 `ouvert`) · fil rouge = **mots-clés non mangés par l'IA**, mûr pour une édition Algorithme |
| 2026-W25 | [[revue-hebdo/2026-W25]] | revue d'**exécution de conditionnels W24** : 3 actions Tim non faites mais pré-arbitrées · **2 promotions `methodes/*` draft→stable** flippées en séance · **H-007 `en-test→ouvert`** (export Organikk jamais déposé, fiche gelée `baseline-jamais-capturee`) · aucune nouvelle hypothèse en test (pas de fiche preuve) · lot ingest golfiller-strat + etude-ctr **1ʳᵉ reconduction (W26)** sinon skip · C-003 corrigée (zéro mesure réel, pas progression fictive) · rien à archiver, mislabel `revues-presse/2026-04-13`→hygiène · **résurgence Grounding Score 06-12 exécutée** (opérationnalisation + sources 6→11 + confidence→medium) · mercredi 06-17 muet (ticket ops) · fil rouge neuf = **parasite SEO/GEO Reddit+X+Grok** (cas test Qadence, gelé sur baseline) |
| 2026-W27 | [[revue-hebdo/2026-W27]] | 0 promotion (rien n'a mûri en 7 jours) · **H-009 au pied du mur** : échéance J+30 Golfiller tombée le 2026-07-03 sans mesure — export GSC à déposer avant le 2026-07-07 sinon `ouvert` en W28 (conditionnel pré-arbitré) · lot W28 = **Leexi en tête** (prestation vivante) + etude-ctr **avec date de mort** (skip si l'édition ne sort pas en W28) + refresh source playbook Reddit (2 versions de retard sur le raw v3) · **C-004 `ouverte`→`résolue` en séance** (entité Qadence vivante = référence d'état, snapshot requalifié photo datée) · recherche kw consultant-startup `draft`→`stale` en séance · **résurgence 01/07 muette** (3ᵉ mercredi muet, ticket ops LaunchAgent) · fil rouge : **édition « mots-clés non mangés » sort en W28 ou se gèle** ; fil Reddit attend les données du programme 30 jours |
| 2026-W28 | [[revue-hebdo/2026-W28]] | les 3 conditionnels W27 tombés, tranchés sans re-débat · 0 promotion (binôme corpus promotable à la 1ʳᵉ page publiée) · **H-009 `en-test`→`ouvert` en séance** (J+30 Golfiller jamais mesuré, clause de falsification appliquée, J+90 seuls actifs) · **H-007 `ouvert`→`en-test` en séance** : GSC organikk.co **enfin branchée** (edge admin-gsc-export) + batch 3 URLs publié le 07/07 → fiche [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]] (J+30 = 2026-08-06) · lot W29 = **refresh playbook Reddit en tête** (source publiée + instrumentée) + Leexi **avec date de mort**, **etude-ctr skippé en séance** (4 votes, édition gelée) · 0 contradiction fermée, **C-003 débloquée** de son « zéro mesure » structurel · jeudi-4-infos : Tim tranche avant W29 sinon `stale` · **résurgence muette ×2** → migration GH Actions avant le 15/07 · fil rouge : **le corpus Organikk publie, la boucle preuves mesure** ; édition « mots-clés non mangés » gelée |

| 2026-W29 | [[revue-hebdo/2026-W29]] | **3 promotions exécutées** (deepseek, mistral, moteurs-ia-chiffres-usage) · **aucune nouvelle hypothèse en test** : H-007 garde la place jusqu'à son J+30 du 2026-08-06 (une à la fois tant qu'aucune échéance n'a été tenue — H-009 est morte de ça) ; **H-009 pré-arbitrée sur Victoria Garden** (2 baselines capturées, `en-test` à la publication client, sortie du programme au 2026-08-31) · lot W30 = **Victoria Garden** ; **Leexi skippé en séance** (3ᵉ non-exécution), refresh playbook Reddit **attaché au J+30 H-007** au lieu d'un 5ᵉ vote, skip `golfiller-strat` **dégelé** (sprint réel constaté) et rattaché au J+90 · règle posée : **le rituel ne fait pas exécuter les ingests, le travail les fait exécuter** · **C-001 + C-010 `ouverte`→`acceptée` en bloc** (77j, garde-fou à l'usage, calque C-007/C-011) · **jeudi-4-infos `stale` par défaut** (conditionnel W28) · **résurgence réparée par la migration GH Actions**, verdict information-gain exécuté (Corroboration 2026, sources 6→7) · fil rouge : **le corpus quitte le pari de publication Organikk pour la production client (Victoria Garden)** ; le pari Organikk passe `stale` le 2026-07-31 s'il ne publie pas |

| 2026-W30 | [[revue-hebdo/2026-W30]] | **1 promotion** (mots-clés-que-les-ia-ne-mangent-pas draft→stable) · aucune hypothèse forcée en-test, H-007 garde la place (J+30 2026-08-06) ; **H-009 s'étend à FG Formation** (candidat parallèle à Victoria Garden, publication dépend de Tim seul, pas d'un client) · lot W31 = **FG-Formation** (ferme C-005 au passage), **vote Victoria Garden retiré** (2ᵉ non-exécution consécutive, même traitement que Leexi en W29) · **C-005 `ouverte`→`en-cours`** (audit blanc Qualiopi, matière citée dans un duel publié cette semaine) · rien à archiver, date de mort du pari Organikk inchangée au 2026-07-31 · **résurgence muette** (1er raté post-migration GH Actions) · fil rouge : **le pattern corpus tourne à 3 clients (Golfiller, Victoria Garden, FG Formation), seul Organikk ne l'exécute pas chez lui** |

Chaque édition est filée dans `revue-hebdo/YYYY-Www.md` et résumée dans cette table.

Pages liées : [[000-home]] · [[hypotheses]] · [[contradictions]] · [[ingest-backlog]] · [[preuves/index]] · [[log]]
