---
title: "todo : ta to-do qui se reconstruit seule"
bootcamp: 4
type: exercice
session: 4
skill: todo
cowork: terminal
created: 2026-06-09
---

# todo : ta to-do qui se reconstruit seule

**Pré-requis** : le skill todo installé (terminal uniquement, lit ~/.claude/projects/). Git ou iCloud pour le schedule.

## Le cas

Le skill todo relit tes 7 derniers jours de transcripts Claude Code et reconstruit ta to-do : ce qui est fait, en cours, à faire. Couplé à un cron, elle se met à jour seule chaque matin.

## Ce que tu dois faire

**1. Lance le skill todo**
Il lit tes transcripts locaux.

**2. Lis l'état**
Fait / en cours / à faire, daté.

**3. Schedule**
Un cron lundi-vendredi 8h avec /schedule.

## Ce que tu dois obtenir — le « screen »

```
TODO — auto (7 derniers jours)

FAIT : audit indexation client X, brief page tarifs
EN COURS : rédaction article "facture électronique"
A FAIRE : maillage interne, fact-check des chiffres

(reconstruite seule chaque matin via cron)
```

## Vérifier que tu as réussi

- [ ] La todo distingue fait / en cours / à faire.
- [ ] Chaque item est daté et sourcé d'un transcript.
- [ ] Le cron est posé (lundi-vendredi 8h).
- [ ] Terminal only (pas Cowork).

## Le piège

Croire que ça marche sur Cowork. Le skill lit ton système de fichiers local : il faut le terminal. Sur Cowork, pas de todo auto.

## Comment ça marche

Le skill parse tes transcripts Claude Code locaux et en déduit l'état d'avancement, sans que tu notes rien. Le cron relance l'analyse chaque jour.
