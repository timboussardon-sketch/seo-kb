---
title: "maillage-systeme : le plan de liens internes"
bootcamp: 4
type: exercice
session: 3
skill: maillage-systeme
cowork: oui
created: 2026-06-09
---

# maillage-systeme : le plan de liens internes

**Pré-requis** : le skill maillage-systeme installé. Une liste d'URLs/articles (titre, slug, mots-clés) et idéalement le contenu.

## Le cas

Le maillage interne est un système, pas une passe. Cet exercice construit l'architecture (piliers, hub/satellite), repère les pages orphelines, et propose des ancres diversifiées, sans dépendre de la GSC.

## Ce que tu dois faire

**1. Donne ta liste d'URLs**
Avec titre, slug, mots-clés. Le contenu en plus si tu l'as.

**2. Lance le skill**

```text
Lance maillage-systeme sur cette liste. Donne l'architecture (3-5 piliers,
hub/satellite), les pages orphelines et dead-end, et 3 propositions d'ancres
par lien (un seul exact match par cible).
```

**3. Pose les liens prioritaires**
Hub → satellite, et Know → Do.

## Ce que tu dois obtenir — le « screen »

```
MAILLAGE — architecture

Pilier "Facturation" (hub : guide complet)
  ├─ orpheline : /mentions-legales/ (0 lien entrant) → à relier
  └─ Know → Do : guide facture → page outil

Ancres vers /logiciel/ : 1 exact, 2 partielles, 2 sémantiques.
```

## Vérifier que tu as réussi

- [ ] 3 à 5 piliers (pas plus).
- [ ] Pages orphelines et dead-end identifiées.
- [ ] 5 liens vers une cible = 5 ancres différentes (un seul exact match).
- [ ] Liens in-body, pas de "Voir aussi".

## Le piège

Lier vers la home depuis le contenu, ou répéter la même ancre. La home a déjà tout le PageRank ; garde le jus pour les pages business.

## Comment ça marche

Le skill classe chaque page par intention (Know/Do), regroupe en piliers, et propose des liens justifiés par 3 signaux (topique, intention, autorité). Une page Know pointe toujours vers une page Do.
