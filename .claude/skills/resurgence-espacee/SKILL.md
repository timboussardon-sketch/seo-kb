---
name: resurgence-espacee
description: |
  Résurgence espacée (mercredi). Remonte un concept stable mais oublié (non touché depuis longtemps, peu de backlinks récents) pour le re-confronter : toujours juste ? à challenger avec une source récente ? à mettre à jour ? Prépare une décision pour la revue hebdo du vendredi.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "résurgence", "concept oublié", "remonte une vieille note", "qu'est-ce que j'ai oublié dans le vault", "spaced repetition vault", ou quand le LaunchAgent com.timboussardon.resurgence se déclenche.
---

# Résurgence Espacée — re-confronter ce que tu sais déjà

Vault : `/Users/timothee/Code/seo-kb/`. Sortie : note du jour dans `wiki/revue-hebdo/resurgence-YYYY-MM-DD.md`.

## OBJECTIF

Un second cerveau qui ne te re-confronte jamais à ses vieilles notes te fait re-découvrir ce que tu savais déjà. Chaque mercredi, on remonte UN concept stable enfoui, on le challenge avec l'état actuel de la KB, et on prépare une décision pour la [[revue-hebdo/index|revue hebdo]] du vendredi.

## ÉTAPE 1 — SÉLECTIONNER LE CONCEPT

Critères de "enfoui mais qui compte" :

```bash
cd /Users/timothee/Code/seo-kb
# concepts stables, triés par ancienneté de updated:
grep -l "status: stable" wiki/concepts/*.md wiki/syntheses/*.md \
  | xargs grep -H "^updated:" | sort -t: -k3 | head -20
```

Choisis un concept `stable` qui réunit : `updated:` ancien (> 60j), backlinks non négligeables (il compte), pas déjà ressorti dans les 8 dernières notes de résurgence (vérifie `wiki/revue-hebdo/resurgence-*.md`). Pondère vers les hubs ([[concepts/data-proprietaire]], [[concepts/surprise-gap]], [[concepts/grounding-score]]) : ce sont eux qu'il est le plus coûteux de laisser dériver.

## ÉTAPE 2 — RE-CONFRONTER

Lis le concept en entier. Confronte-le à ce qui a été ingéré depuis son dernier `updated:` :

- Une source récente le confirme, le nuance, ou le contredit ?
- Une hypothèse de `wiki/hypotheses.md` y est-elle adossée ? A-t-elle bougé ?
- Le wording viole-t-il une règle apparue depuis (anti-AI-writing, vocabulaire) ?
- Toujours juste tel quel, ou drift silencieux ?

## ÉTAPE 3 — VERDICT PRÉPARÉ POUR VENDREDI

Écris `wiki/revue-hebdo/resurgence-YYYY-MM-DD.md` (`type: register`, `status: stable`) :

```markdown
# Résurgence — [[concepts/slug]] — YYYY-MM-DD

## Pourquoi celui-là
[ancienneté, poids, dernière résurgence]

## État vs aujourd'hui
[ce qui a changé dans la KB depuis son updated:]

## Verdict proposé pour la revue hebdo
- [ ] Toujours juste, rien à faire
- [ ] À mettre à jour : [quoi précisément]
- [ ] À challenger : [quelle source/hypothèse l'attaque]
- [ ] Wording à corriger : [quelle règle]
```

Une seule case cochée, tranchée. Pas de "à voir".

## ÉTAPE 4 — LOG + RÉSUMÉ

```
## [YYYY-MM-DD] resurgence | [[concepts/slug]] — verdict proposé
```

Termine par : `Résurgence [date] : concepts/slug — verdict : … (à arbitrer en revue hebdo)`

## CONTRAINTES

- Un seul concept par semaine. La résurgence n'est pas un audit de masse, c'est une re-confrontation profonde et unique.
- Ne pas modifier le concept ici : tu prépares la décision, c'est la revue hebdo du vendredi qui tranche et le skill `hypotheses-validation` ou un ingest qui exécute.
- Pas d'invention : si rien n'a changé depuis le dernier `updated:`, le dire franchement et cocher "toujours juste".
- Éviter de re-sortir un concept déjà ressorti récemment (fenêtre 8 semaines).
