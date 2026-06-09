---
title: "seo-cannibalisation : deux pages qui se battent"
bootcamp: 4
type: exercice
session: 3
skill: seo-cannibalisation
cowork: oui
created: 2026-06-09
---

# seo-cannibalisation : deux pages qui se battent

**Pré-requis** : le skill seo-cannibalisation installé. Un export GSC.

## Le cas

Quand deux pages visent le même mot-clé, elles se cannibalisent : Google ne sait pas laquelle classer, les deux perdent. Cet exercice les repère depuis ta GSC et dit quoi faire.

## Ce que tu dois faire

**1. Exporte ta GSC**
Requêtes + Pages.

**2. Lance le skill**

```text
Lance seo-cannibalisation sur cet export GSC. Classe les conflits
(Type A mot-clé exact, B même intention, C proximité), donne la root cause
et l'action par conflit.
```

**3. Applique l'action**
301, fusion, différenciation ou maillage croisé.

## Ce que tu dois obtenir — le « screen »

```
CANNIBALISATION — export GSC

Type A : /facture-auto/ et /logiciel-facture/ sur "logiciel facture"
  → fusionner, 301 vers la plus forte
Type C : /devis/ et /facture/ (proximité) → différencier + maillage

(une Triade SERP légitime n'est PAS une cannibalisation)
```

## Vérifier que tu as réussi

- [ ] Conflits classés (Type A / B / C).
- [ ] Root cause identifiée (contenu vs maillage).
- [ ] Une action par conflit.
- [ ] Pas de fausse alerte sur une Triade SERP légitime.

## Le piège

Fusionner deux pages qui ne se cannibalisent pas vraiment (intentions différentes). Vérifie l'intention avant de 301.

## Comment ça marche

Le skill repère dans la GSC les URLs qui se disputent les mêmes requêtes, qualifie le type de conflit et recommande la résolution qui consolide l'autorité sur une seule page.
