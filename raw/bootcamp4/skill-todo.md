---
title: "Skill Semaine 4 Jour 2 : todo"
bootcamp: 4
semaine: 4
jour: 2
type: skill-distribuable
usage: "Distribué au J2 de la S4. À mettre sur le Drive + message WhatsApp le matin du J2. Skill installable en 3 minutes, puis activable en /schedule pour reconstruction auto chaque matin."
related:
  - "[[sequencage-semaine-4]]"
  - "[[bundle-todo]]"
  - "[[skill-donnees-structurees]]"
created: 2026-05-27
---

# Skill `todo` : la todo qui se reconstruit seule depuis tes sessions Claude Code

Jour 2 de la S4. Hier le balisage du site se génère seul (`seo-donnees-structurees`). Aujourd'hui c'est ta propre todo qui se reconstruit seule, depuis ce que tu fais réellement dans Claude Code.

Pas un Notion à alimenter. Pas un Linear à maintenir. **Un miroir** de ce que tu as livré, de ce que tu n'as pas fini, et de ce que tu as différé. Reconstruit chaque matin à 8h sans que tu touches à rien.

## Pourquoi c'est utile pour vous

Vous enchaînez 3 à 5 sessions Claude Code par jour (audit, rédaction, prospection). Personne ne tient une vraie todo à côté en parallèle. C'est du double travail, donc personne ne le fait. Résultat : on oublie ce qu'on a dit qu'on ferait, on rouvre 4 fois le même chantier, on arrive au call du vendredi sans savoir ce qu'on a livré.

L'historique de tout ce que vous avez fait est déjà sur votre machine, dans les transcripts JSONL (`~/.claude/projects/`). Le skill `todo` exploite cet historique, vous récupérez le bénéfice :

- ✅ **FAIT** : livrables des 7 derniers jours, datés, sourcés au repo
- 🔄 **EN COURS** : chantiers ouverts, plans validés mais pas implémentés
- 📋 **À FAIRE** : vos intentions différées, priorisées P1 / P2 / P3

Différence vs Notion / Linear / Things : pas de saisie. Pas d'oubli. C'est **généré**.

## Procédure d'install (3 minutes)

1. Va dans le dossier des skills : `~/.claude/skills/` (Mac/Linux) ou `%USERPROFILE%\.claude\skills\` (Windows). S'il n'existe pas, crée-le.
2. Crée un sous-dossier : `~/.claude/skills/todo/`
3. Dedans, crée un fichier `SKILL.md` et colle **tout le bloc ci-dessous** (entre les deux lignes `=====`).
4. Relance Claude Code. Vérifie avec `/skills` que `todo` apparaît dans la liste.

**Premier test** : tape `/todo` dans n'importe quel repo Claude Code. Le skill scanne tes 7 derniers jours de transcripts et écrit `raw/todo/todo-actuelle.md` (ou un autre chemin que tu peux préciser). Ouvre le fichier, lis. Si tu reconnais ce que tu as fait, c'est gagné.

## Setup `/schedule` (le vrai déclic)

Le skill en one-shot c'est bien. En cron quotidien, c'est ce qui change ta journée.

1. Dans Claude Code, tape `/schedule`
2. Crée une routine avec :
   - **Cron** : `0 8 * * 1-5` (du lundi au vendredi à 8h)
   - **Repo** : ton vault Obsidian ou ton dossier de notes (sous Git)
   - **Prompt** : `/todo`
3. Active

Le lendemain matin 8h, la todo se reconstruit toute seule, commit auto dans le repo. Tu ouvres Claude Code à 9h, tu sais ce que tu as à faire avant même de poser les mains sur le clavier.

**Pourquoi `/schedule` plutôt qu'un cron local** :

- Tourne sur l'infra Anthropic, pas sur ta machine. Tu pars en weekend, ta todo de lundi matin est quand même prête.
- Commit auto dans le repo cible (pas de bug "le cron a tourné mais le commit a foiré").
- Pilotable depuis `/schedule list` (modifier, suspendre, supprimer).

> ⚠️ **Cas vault iCloud** : si ton vault Obsidian est sur iCloud (pas sous Git), `/schedule` ne peut pas écrire dedans. Soit tu passes le vault sous Git, soit tu lances un launchd local à la place. MP si tu es dans ce cas, on cadre votre version.

## Pré-requis et limites

- Tourne dans **Claude Code en terminal**. Les transcripts JSONL sont stockés en local sur ta machine, le skill les lit là.
- Si tu travailles **uniquement** dans Claude Cowork ou l'extension Chrome (donc pas en terminal), le skill n'a rien à lire chez toi. MP cette semaine si c'est ton cas, on cadre une alternative (export manuel de tes sessions, ou skill adapté).
- Si tu rédiges aussi dans Notion / Cursor / autre IDE, ces sessions ne sont pas dans `~/.claude/projects/`, donc pas dans la todo. À compléter à la main si nécessaire (les annotations manuelles sont préservées entre runs).

## Pièges à éviter

| Piège | Conséquence | Garde-fou |
|---|---|---|
| Croire que le skill **invente** des tâches | Tâches fantômes, perte de confiance dans la todo | Le skill ne reporte que ce qu'il voit dans les transcripts. Pas d'inférence. Règle absolue du skill. |
| Bosser 100% hors Claude Code | Todo vide ou trompeuse | Le skill ne voit que ce qui passe par Claude Code. Notion, Cursor, autres IDE sont invisibles pour lui. |
| Annotations manuelles écrasées | Si tu commentes ta todo à la main, un re-run brut pourrait effacer | Le skill préserve les annotations type `✅ done manuel`. Relis quand même avant overwrite si tu as bossé directement dans le fichier. |
| Fenêtre 7 jours trop courte après congés | À ton retour, le skill ne voit plus les chantiers d'il y a 10 jours | Au retour, augmente temporairement la fenêtre via prompt (`/todo --fenetre 14`). |
| Cron sur vault iCloud | Erreurs silencieuses, todo jamais à jour | Vault sous Git pour `/schedule`. iCloud → launchd local uniquement. |

## Livrable J2

À la fin de la journée, ce qui doit tourner chez vous :

- [ ] Skill `todo` installé, `/skills` le liste
- [ ] Premier `/todo` lancé, fichier `raw/todo/todo-actuelle.md` créé et lisible
- [ ] Routine `/schedule` active avec cron du matin (ou launchd local si vault iCloud)
- [ ] Capture de votre `todo-actuelle.md` envoyée sur le WhatsApp du groupe

Vendredi au call : on regarde comment chacun a structuré sa todo, et surtout quel geste manuel chacun a tué grâce à elle (relevé d'activité hebdo client, point de la semaine, rapport facturation).

## Cas d'usage côté client

Le skill peut tourner sur un repo client dédié. Les sessions Claude Code liées à ce repo (audit, rédaction, suivi) nourrissent une todo client claire :

- **Rapport hebdo automatique** au client : « voilà ce qu'on a livré cette semaine sur ton site ». Le skill génère, vous éditez, vous envoyez.
- **Suivi de facturation** : croisé avec votre data d'heures, ça vous dit qui consomme combien.
- **Continuité** : si vous reprenez un client après 2 semaines de pause, `/todo` sur le repo client vous remet en selle en 30 secondes.

C'est le J2 + le J5 du bootcamp combinés : un skill qui sert votre quotidien ET un livrable que vous facturez côté client.

=====

````markdown
---
name: todo
description: |
  Reconstruit une todo personnelle à partir des transcripts Claude Code locaux (7 derniers jours). Distingue ce qui est ✅ FAIT, 🔄 EN COURS, 📋 À FAIRE (priorisé sur récence × fréquence × blocage). Snapshot frais, overwrite d'un fichier unique (pas d'archivage par date).

  Le skill ne te demande pas de te souvenir de ta todo : il la *reconstruit* depuis ce que tu as réellement fait dans Claude Code. Pas d'inférence, pas de tâche fantôme, pas de fluff.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "ma todo", "fais-moi la todo", "où j'en suis", "qu'est-ce qu'il me reste", "actualise ma todo", "reprends ma todo", "bilan de la semaine", "récupère ce que j'ai fait cette semaine", "/todo", ou quand il enchaîne plusieurs sessions Claude Code et veut un point clair.
---

# Skill — Todo depuis transcripts Claude Code

## Automatiser avec `/schedule` (à lire en premier)

Ce skill est utile en one-shot (« fais-moi le point »), mais il devient puissant quand il tourne **chaque matin à 8h, automatiquement**, pour t'ouvrir ta journée avec une todo fraîche reconstruite depuis tes sessions Claude Code de la veille.

**Setup en 3 étapes** :

1. Dans Claude Code, tape `/schedule`
2. Choisis « Créer une routine » et configure :
   - **Cron** : `0 8 * * 1-5` (du lundi au vendredi à 8h)
   - **Repo** : le repo Obsidian / vault où la todo doit être écrite (ex. `seo-kb`)
   - **Prompt** : `/todo` (sans paramètre, scan auto des 7 derniers jours)
3. Active la routine

**Ce que ça change vs un cron local** :
- La routine tourne sur l'infra Anthropic, pas sur ta machine. Tu pars en weekend, ta todo de lundi matin est quand même prête.
- Commit auto dans le repo cible (si configuré). Pas de bug type « le launchd a tourné mais le commit a foiré ».
- Tu pilotes depuis `/schedule list` (modifier le cron, suspendre, supprimer).

**Quand préférer un launchd local** : si ton vault Obsidian n'est pas sous Git (typique iCloud Obsidian) — `/schedule` ne peut pas y écrire. Soit tu mets ton vault sous Git, soit tu passes par launchd local + sync iCloud.

## Logique

Tu travailles déjà dans Claude Code tous les jours. Tes transcripts JSONL contiennent l'historique exact de ce que tu as livré, débuggé, différé. Le skill lit ces transcripts pour reconstruire ta todo, sans que tu aies à la maintenir à la main.

**3 catégories** :
- ✅ FAIT — livraisons concrètes (fichiers écrits, commits, validations)
- 🔄 EN COURS — sessions ouvertes, plans validés mais pas implémentés, multi-étapes incomplètes
- 📋 À FAIRE — intentions explicites de Tim, deadlines reportées, tasks pending

## Étape 1 — Récupérer les transcripts

Les transcripts JSONL Claude Code sont dans :

```
~/.claude/projects/-Users-<user>-<chemin-repo>/*.jsonl
```

Le chemin du repo est encodé : les `/` deviennent `-`. Exemple : `/Users/timothee/Code/seo-kb` → `-Users-timothee-Code-seo-kb`.

Demande à l'utilisateur quels repos il veut scanner si ce n'est pas évident depuis le `pwd` courant ou si plusieurs projets sont actifs.

Date du jour :
```bash
date +%Y-%m-%d
```

Fenêtre : 7 derniers jours.

```bash
find ~/.claude/projects/ -name "*.jsonl" -mtime -7 2>/dev/null
```

## Étape 2 — Parser chaque transcript

Pour chaque fichier JSONL, lis-le avec Read (utiliser offset/limit si gros — les fichiers peuvent dépasser plusieurs Mo). Chaque ligne est un objet JSON : entrée user, message assistant, tool_use, tool_result.

### A) ✅ FAIT

Signaux à chercher :
- Tool calls `Write` / `Edit` réussis → fichier créé / modifié
- Tool calls `Bash` avec `git commit` réussis
- Messages assistant qui annoncent une livraison concrète : « j'ai créé X », « j'ai publié Y », « sauvegardé dans Z »
- Phrases user qui valident une livraison : « parfait », « ok merci », « tu valides », « ça marche », « nickel »

Format : `[YYYY-MM-DD] Action concrète (source : nom-repo)`

### B) 🔄 EN COURS

Signaux :
- Sessions dont la dernière entrée est un travail non clôturé (pas de validation user, pas de commit final)
- Phrases user : « je vais faire », « je dois finir », « on continue demain », « je reprends ça plus tard »
- `TaskCreate` avec tasks `pending` non clôturées dans la session
- Plans validés (`ExitPlanMode`) mais pas exécutés

Format : `[démarrée YYYY-MM-DD] Action — où ça en est`

### C) 📋 À FAIRE (priorisé)

Signaux :
- Tim dit explicitement : « à faire », « TODO », « il faudra », « je dois », « prochaine étape », « rappelle-moi de », « note-toi de »
- Fins de session avec « next steps » listés mais non exécutés
- Décisions différées : « on verra plus tard », « pour l'instant on laisse », « pas urgent »
- `TaskCreate` pending non clôturées entre sessions

Format : `- [ ] Action (raison de la prio si déductible)`

**Priorité** :
- **P1** = mentionnée dans la session la plus récente OU deadline proche OU bloque autre chose
- **P2** = mentionnée dans plusieurs sessions
- **P3** = mentionnée une seule fois, ancienne

## Étape 3 — Fusion avec la todo existante

Lis le fichier todo cible (par défaut `raw/todo/todo-actuelle.md`, ou chemin demandé par l'utilisateur) s'il existe.

Logique de fusion :
- **À FAIRE non datés ou plus anciens que la fenêtre 7j, toujours présents dans l'existant** → conserver tels quels (Tim ne les a pas faits, ils restent valides)
- **À FAIRE de l'existant qui apparaissent maintenant en FAIT** → déplacer en FAIT (avec la date où ils ont été faits, lue dans les transcripts)
- **Annotations manuelles** (`✅ done manuel`, commentaires Tim) → préserver telles quelles

Si le fichier n'existe pas → repartir de zéro.

## Étape 4 — Rédiger le fichier

Format final (overwrite total) :

```markdown
# Todo — MAJ YYYY-MM-DD HH:MM

> Source : transcripts Claude Code locaux (7 derniers jours)
> Reconstruit via skill `todo`

## ✅ Fait récemment (7 derniers jours)

- [YYYY-MM-DD] Action complétée (source : repo)
- [YYYY-MM-DD] Action complétée (source : repo)
...

## 🔄 En cours

- [démarrée YYYY-MM-DD] Action — où ça en est
- [démarrée YYYY-MM-DD] Action — où ça en est
...

## 📋 À faire

### P1 (cette semaine)
- [ ] Action (raison)
- [ ] Action

### P2 (mois)
- [ ] Action
- [ ] Action

### P3 (backlog)
- [ ] Action
```

Chemin par défaut : `raw/todo/todo-actuelle.md` (cohérent avec la structure vault Tim). Adapter si l'utilisateur précise un autre chemin.

## Règles absolues

- **Overwrite, pas d'archivage daté.** Un seul fichier vivant. Si Tim veut un historique → c'est git, pas un fichier par date.
- **Pas d'inférence créative.** Si tu n'arrives pas à classifier proprement, mets en `🔄 En cours` plutôt que d'inventer une priorité.
- **Pas de tâche fantôme.** Ne pas écrire « à faire : X » si X n'est mentionné nulle part dans les transcripts. Le skill rapporte ce qu'il voit, il n'imagine pas.
- **Date du jour systématique** dans les timestamps : `date +%Y-%m-%d`.
- **Pas d'emoji autre que les 3 catégories** (✅ 🔄 📋). On garde sec.
- **Si > 7 jours sans aucune session Claude Code détectée** → le signaler en haut du fichier (« ⚠️ Aucune session récente, snapshot peut être périmé »).

## Variante : todo par projet

Si l'utilisateur ne veut la todo que pour UN projet (ex. seo-kb seul, ou organikk-next seul), filtrer les transcripts au scan initial — ne lire que `~/.claude/projects/-Users-<user>-<projet>/*.jsonl`.

Format alors : `raw/todo/todo-actuelle-[projet].md`.

## Enchaînement

- Pas d'amont, pas d'aval. Skill autonome.
- Peut être branché en cron quotidien (ex. tous les matins à 8h) pour un snapshot frais à l'ouverture de la session.
````

=====

## Pour Tim (interne)

- **Statut** : skill distribuable, à coller sur le Drive bootcamp + relayer en WhatsApp le matin du J2.
- **Contenu identique au skill canonique** `~/.claude/skills/todo/SKILL.md` (version du 2026-05-27). Si tu modifies le skill canonique, régénère ce fichier.
- **Em-dashes dans le SKILL.md verbatim** : conservés tels quels parce que c'est le skill installé chez toi. Si tu veux normaliser (règle maison anti em-dash), il faut éditer le skill canonique d'abord, puis régénérer ce fichier ensuite.
- **Bascule J2** : ce skill remplace nettement le module « revue-presse client » initialement prévu au J2. Voir [[sequencage-semaine-4]] à mettre à jour (section Jour 2 + notes internes : retirer la ligne « J2 à confirmer / bundle revue-presse client à produire »).
- **Risque audience Cowork / Chrome-only** : pour un participant qui ne tourne JAMAIS en terminal, le skill ne lit rien. Pré-requis annoncé clair dans la section dédiée + invite MP. Estimer 1 à 2 personnes concernées max dans la cohorte.
- **Connexion J5** : le livrable J5 (« le système qui bosse pendant que tu dors ») gagne une brique avec ce skill : la todo qui se reconstruit chaque matin pendant que tu dors. À démo au call.
- **`[[bundle-todo]]`** créé hier (2026-05-26) reste utile comme bundle pédagogique « long » avec les cas d'usage. Ce fichier `skill-todo.md` est la version « distribuable propre » au format des autres skills S3-S4.
