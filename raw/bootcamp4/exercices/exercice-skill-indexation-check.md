---
title: "indexation-check : tes pages sont-elles indexées ?"
bootcamp: 4
type: exercice
session: 3
skill: indexation-check
cowork: oui
created: 2026-06-09
---

# indexation-check : tes pages sont-elles indexées ?

**Pré-requis** : le skill indexation-check installé. Le sitemap.xml de ton client (variante terminal pour Claude Code, variante Cowork sinon).

## Le cas

Une page non indexée ne rank sur rien. Cet exercice vérifie, sur ton sitemap, quelles pages sont indexées, lesquelles ne le sont pas, et lesquelles ne sont pas testables (rate-limit Google), sans jamais confondre les deux.

## Ce que tu dois faire

**1. Récupère le sitemap.xml**
L'URL du sitemap public du client.

**2. Lance le skill**

```text
Lance indexation-check sur ce sitemap : [URL]. Vérifie les 9 points
(HTTP, robots, noindex, sitemap, maillage entrant, longueur, indexation).
Distingue strictement "non indexée" et "non testable".
```

**3. Lis les anomalies critiques**
Un noindex sur une page business passe en tête.

## Ce que tu dois obtenir — le « screen »

```
INDEXATION — site-client.fr

Indexées : 142 / 168
Non indexées : 9 (dont 3 pages business !)
Non testables (rate-limit) : 17

CRITIQUE : /tarifs/ en noindex accidentel.
```

## Vérifier que tu as réussi

- [ ] 9 points vérifiés (HTTP, robots, noindex, sitemap, maillage, longueur...).
- [ ] Distinction stricte non indexée vs non testable.
- [ ] Anomalies critiques (noindex business) en tête.
- [ ] Lecture seule, aucun forçage.

## Le piège

Marquer "non indexée" une page juste non testable (Google a rate-limité). Faux diagnostic = mauvaise action. Le skill distingue les deux.

## Comment ça marche

Le skill croise sitemap, statut HTTP, directives et maillage pour estimer l'indexation de chaque URL, en séparant les causes (technique) du statut (indexée ou pas).
