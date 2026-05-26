---
title: Bundle Todo automatisée — depuis transcripts Claude Code
bootcamp: 4
jour: J2 bis (ou intégrable J5 call)
skill: todo
related:
  - "[[sequencage-semaine-4]]"
  - "[[bundle-revue-presse-seo]]"
created: 2026-05-26
---

# Bundle — Todo automatisée depuis tes transcripts Claude Code

**Objectif** : arrêter de maintenir une todo à la main. Le skill `todo` lit tes transcripts Claude Code locaux des 7 derniers jours et reconstruit automatiquement ce qui est ✅ FAIT / 🔄 EN COURS / 📋 À FAIRE.

Pas un task manager qu'on alimente. **Un miroir de ce que tu as réellement fait.**

---

## 1. Pourquoi c'est intéressant pour le bootcamp

Vous enchaînez des sessions Claude Code toute la journée (audit client, rédaction, prospection). Personne ne maintient une vraie todo en parallèle — c'est du double travail. Or l'historique de ce que vous faites EST déjà dans vos transcripts JSONL (`~/.claude/projects/`).

Le skill `todo` exploite cet historique pour vous rendre :
- Un point clair de **ce que vous avez livré** cette semaine (utile pour le call J5, pour facturer un client, ou pour votre propre suivi)
- Les **chantiers en cours** non clôturés (à reprendre)
- Les **intentions différées** que vous avez verbalisées mais pas exécutées (priorisées)

Différence vs un Notion / Linear / Things : pas de saisie. Pas d'oubli. **C'est généré.**

---

## 2. Installation du skill

```bash
mkdir -p ~/.claude/skills/todo
# Copier SKILL.md (fourni dans le Drive bootcamp) dans ce dossier
```

Vérification : dans Claude Code, tape `/` et cherche `todo` dans la liste. S'il apparaît, l'install est OK.

---

## 3. Premier run manuel

Dans n'importe quel repo (le skill scanne TOUS tes projets Claude Code, pas seulement celui où tu es) :

```
/todo
```

**Output** dans `raw/todo/todo-actuelle.md` :

```markdown
# Todo — MAJ 2026-05-26 09:14

> Source : transcripts Claude Code locaux (7 derniers jours)

## ✅ Fait récemment (7 derniers jours)
- [2026-05-22] Audit indexation client Caroline (source : seo-kb)
- [2026-05-23] Rédaction article passage ranking (source : organikk-next)
...

## 🔄 En cours
- [démarrée 2026-05-24] Refonte cluster AEO Franck — Phase 3 sur 5
...

## 📋 À faire
### P1 (cette semaine)
- [ ] Caser le skill sémantique dans la grille S4 (mentionné session 2026-05-23)
- [ ] Bundle J2 revue-presse client (mentionné 2026-05-25)
### P2 (mois)
- [ ] Audit GEO Organikk
### P3 (backlog)
- [ ] Tester MCP WordPress sur site Romain
```

**Variante par projet** : si tu ne veux pas le scan global mais juste un projet précis :

```
/todo seo-kb
```

Sortie : `raw/todo/todo-actuelle-seo-kb.md`.

---

## 4. Automatiser avec `/schedule` (le vrai livrable)

L'usage le plus puissant : la todo se reconstruit chaque matin à 8h, avant que tu ouvres Claude Code. Tu démarres ta journée avec un point à jour, sans rien faire.

**Setup 3 étapes** :

1. Dans Claude Code, tape `/schedule`
2. Crée une routine :
   - **Cron** : `0 8 * * 1-5` (lundi à vendredi à 8h)
   - **Repo** : ton vault Obsidian (typiquement `seo-kb`)
   - **Prompt** : `/todo`
3. Active

**Avantages vs un launchd local** :
- Tourne sur l'infra Anthropic. Tu peux travailler sur 3 machines, la todo reflète l'activité de toutes (les transcripts sont sync via Anthropic).
- Commit auto dans ton vault Obsidian (si sous Git).
- Pilotage centralisé via `/schedule list`.

**⚠️ Cas où le launchd local reste obligatoire** : si ton vault Obsidian est sur **iCloud** (typiquement le vault Bible 🙏🏼 de Tim). `/schedule` ne peut pas écrire dans iCloud, il écrit dans le repo Git. Soit le vault passe sous Git, soit tu lances un launchd local + sync iCloud via Obsidian.

---

## 5. Pièges à éviter

| Piège | Conséquence | Garde-fou |
|---|---|---|
| Penser que le skill INVENTE des tâches | Tâches fantômes, perte de confiance dans la todo | Le skill ne rapporte que ce qu'il VOIT dans les transcripts. Pas d'inférence. Règle absolue. |
| Travailler 100% en dehors de Claude Code | Le skill ne voit rien, todo vide | Le skill exploite TES transcripts. Si tu rédiges dans Notion ou Cursor, ces sessions ne sont pas dans `~/.claude/projects/`. À combiner manuellement. |
| Fenêtre 7 jours trop courte si tu pars en congés | À ton retour, le skill ne voit plus les chantiers d'il y a 10 jours | À l'ouverture après congés, augmente temporairement la fenêtre via prompt (`/todo --fenetre 14`) |
| Écraser tes annotations manuelles | Si tu ajoutes des commentaires Tim-style (`✅ done manuel`), un re-run brut peut les effacer | Le skill préserve les annotations manuelles. Mais relis avant chaque overwrite si tu as bossé directement dedans. |
| Lancer en cron sur un vault iCloud | Erreurs silencieuses, todo jamais à jour | Garder un vault sous Git pour ce skill. iCloud → launchd local uniquement. |

---

## 6. Cas d'usage pour le bootcamp

**Pour TOI (participant)** :
- Démarrer chaque journée avec le point clair
- Préparer ton call J5 en 2 minutes (la todo dit exactement ce que tu as fait cette semaine)
- Ne plus perdre les intentions différées (« je dois penser à X »)

**Pour TES CLIENTS** :
- Le skill peut tourner sur un repo client dédié. Les transcripts liés à ce repo nourrissent une todo client claire.
- Idéal pour générer un rapport hebdo automatique (« voilà ce qu'on a livré cette semaine sur ton site »).

**Pour TON BUSINESS** :
- Croisé avec ta data de facturation, ça te dit qui consomme combien d'heures.

---

## 7. Démo call J5

Pour le vendredi :
- Ta `todo-actuelle.md` à jour, générée le matin même par `/schedule`
- 1 cas où la todo t'a évité d'oublier une intention différée (« j'avais dit X il y a 4 jours, je l'ai vu en ouvrant Claude Code »)
- Optionnel : un rapport hebdo client généré depuis la même méthode

Format démo : *« voilà ma todo de ce matin, voilà ce que j'ai livré cette semaine, voilà ce qu'il me reste — tout est généré, je n'ai rien tapé »*.

---

## Annexe — SKILL.md (référence)

Chemin d'install : `~/.claude/skills/todo/SKILL.md`

Le contenu complet du skill est dans le Drive bootcamp (fichier `SKILL-todo.md`). À copier verbatim dans le dossier ci-dessus.

---

*Bundle Todo — Bootcamp 4. Skill `todo` livré en bonus (J2 ou J5). Méthodologie Timothée Boussardon, mai 2026. À distribuer aux participants via le Drive bootcamp.*
