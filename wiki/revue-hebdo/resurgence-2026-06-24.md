---
type: register
title: Résurgence — surprise-gap — 2026-06-24
aliases: [resurgence-surprise-gap]
tags: [resurgence, doctrine, surprise-gap]
created: 2026-06-24
updated: 2026-06-24
status: stable
---

# Résurgence — [[concepts/surprise-gap]] — 2026-06-24

## Pourquoi celui-là

- `updated:` 2026-04-13, soit 72 jours sans révision (seuil > 60j tenu).
- Hub massif : 74 backrefs dans le vault. C'est l'un des trois concepts les plus coûteux à laisser dériver, listé comme prioritaire par le skill aux côtés de [[concepts/data-proprietaire]] et [[concepts/grounding-score]].
- Jamais ressorti en résurgence. Les deux précédentes ont sorti data-proprietaire (2026-05-16) et grounding-score (2026-06-12). Fenêtre 8 semaines respectée.

## État vs aujourd'hui

Rien n'a touché le concept frontalement depuis le 2026-04-13. Les sources ingérées depuis (playbooks Reddit et X du 2026-06-19, exports GSC golfiller et victoria garden des 10-11/06) ne portent pas sur le Surprise Gap. Aucune source ne le confirme, ne le nuance ni ne le contredit.

Le mouvement réel est ailleurs : la boucle preuve s'est ouverte. Les exports GSC (golfiller sur 6 mois, victoria garden 3 mois vs N-1) sont arrivés dans le vault. L'argument qui rendait [[concepts/surprise-gap]] intestable — « aucune data terrain, thèse construite par transfert architecture → métier » — perd sa force. Le test A/B décrit dans H-002 (deux contenus Organikk comparables, un avec Surprise Gap propriétaire net, mesure citations IA + positions à J+30/J+90 via [[preuves/index]]) est désormais instrumentable. Il n'a jamais été lancé : `grep` sur `wiki/preuves/` pour `surprise-gap` = vide.

Le drift silencieux est dans le frontmatter. `confidence: high` sur un concept dont la propre section Limites dit « thèse propriétaire, non validée empiriquement. Aucun test A/B dans cette KB », adossé à [[hypotheses|H-002]] toujours `ouvert`. Le `high` n'a jamais été gagné par de la data — il décrit la conviction de Tim, pas le niveau de preuve. C'est exactement ce que la boucle doctrine → validation (§14) interdit : un statut ne monte que via une fiche preuve adossée à de la data réelle, jamais sur du ressenti.

## Verdict proposé pour la revue hebdo

- [x] À mettre à jour : passer `confidence: high` → `confidence: medium` sur [[concepts/surprise-gap]] tant que H-002 reste `ouvert` et qu'aucune fiche preuve ne l'adosse à de la data. Aligner le frontmatter sur ce que dit déjà la section Limites. Le `high` se regagne uniquement quand le test A/B Organikk (H-002) a tourné et qu'une preuve à J+30/J+90 confirme la corrélation Surprise Gap ↔ citation IA. Action concrète à programmer : lancer ce test maintenant que la plomberie GSC existe (golfiller, victoria garden ont prouvé que la data arrive).
- [ ] Toujours juste, rien à faire
- [ ] À challenger : —
- [ ] Wording à corriger : —
