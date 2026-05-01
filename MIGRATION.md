---
title: Migration du setup vers un autre Mac
date: 2026-05-01
auteur: Timothée Boussardon
statut: protocole opérationnel
---

# Migration du setup vers un autre Mac

Ce doc te permet de reconstruire à l'identique ton vault Obsidian, Claude Code, les skills, les routines et la config cron sur un nouveau Mac. Suis-le dans l'ordre. Tout est vérifié sur l'état réel de la machine au 2026-05-01.

---

## Inventaire à transférer

### 1. Le vault Obsidian — `~/Documents/seo-kb/`

- 23 Mo, 278 fichiers `.md`, 6 PDF
- Sous git, branche `main`, **aucun remote configuré actuellement**
- Wiki structuré : 35 [[concepts]], 37 entities, 37 sources, 5 syntheses
- Doctrine entière dans `AGENTS.md` (20 Ko)
- `.gitignore` exclut `.obsidian/` et `raw/revue-de-presse/` → ces deux blocs se transfèrent à part

### 2. Le sous-repo "revue de presse" — `~/Documents/seo-kb/raw/revue-de-presse/`

Repo git séparé, déjà sur GitHub :
```
https://github.com/Tim9501/seo-kb-revue-de-presse.git
```
Branche `main`. Synchronisé toutes les 15 minutes par un LaunchAgent macOS (voir §LaunchAgent ci-dessous).

### 3. La config Obsidian — `~/Documents/seo-kb/.obsidian/`

Ignorée par git mais critique. Contient :
- `core-plugins.json` (28 plugins activés, dont graph, backlink, dataview-style outline)
- `graph.json` (paramètres custom du graph view : centerStrength `0.52`, repelStrength `10`, linkDistance `250`)
- `workspace.json` (layout des panneaux ouverts)
- `app.json`, `appearance.json`

### 4. Claude Code — `~/.claude/`

À transférer :
- `settings.json` (config minimale, 211 octets — `disableAllHooks: true` + marketplace officiel)
- `skills/` : 15 skills custom indispensables :
  ```
  article-engine-pipeline
  kb-semantic-search
  maillage-interne-gsc
  maillage-systeme
  organikk-blog-article
  organikk-site
  seo-brief-contenu
  seo-cannibalisation
  seo-cluster-aeo
  seo-entites-vectorielles
  seo-peurs-objections
  seo-product-led-seo
  seo-programmatique-pseo
  seo-quick-win
  seo-workflow-article
  ```

À NE PAS transférer (état perso de la machine, regénéré à l'usage) :
```
cache/   sessions/   history.jsonl   projects/   paste-cache/
shell-snapshots/   telemetry/   todos/   tasks/   debug/
file-history/   plans/   session-env/   backups/
mcp-needs-auth-cache.json
```

### 5. LaunchAgent macOS — `~/Library/LaunchAgents/`

Un seul fichier perso :
```
co.organikk.seo-kb-revue-presse-pull.plist
```
Il fait un `git pull --rebase` sur le sous-repo revue de presse toutes les 900 secondes (15 min). Logs dans `~/Library/Logs/seo-kb-revue-presse-pull.log`.

### 6. Scripts cron locaux — `~/Documents/seo-kb/tools/cron/`

Trois scripts shell : `revue-presse.sh`, `scan-arxiv.sh`, `todo-bilan.sh`.
**Pas de crontab utilisateur actif actuellement** (vérifié : `crontab -l` est vide). Si tu veux activer ces scripts sur le nouveau Mac, c'est manuel.

### 7. Routine cloud Anthropic — RIEN à transférer côté machine

La routine `algorithme-newsletter-quotidien` (ID `trig_01Q9turzWB81Ck2i4YF3gyzN`, cron `7 7 * * *` UTC) tourne côté cloud Anthropic. Elle est liée à ton compte Claude, pas à la machine. Elle continuera à tourner toute seule. Lien : https://claude.ai/code/routines/trig_01Q9turzWB81Ck2i4YF3gyzN

### 8. Connecteurs MCP

Figma, Gmail, Google Calendar, Google Drive, WordPress.com, Windsor. Liés au compte Claude → ils suivent quand tu te reconnectes sur le nouveau Mac. Aucun fichier local à copier.

### 9. À vérifier toi-même avant le départ

Je n'ai pas eu les permissions pour explorer ces zones — vérifie-les manuellement :
- `~/Documents/CLAUDE/` (mentionné dans tes memories, contient peut-être des skills locaux Scheduled)
- `~/.zshrc`, `~/.zprofile` (variables d'environnement, alias, PATH)
- `~/.ssh/` (clés SSH si tu utilises GitHub en SSH)
- Trousseau (token GitHub, mots de passe apps tierces)

---

## Avant le départ — sur l'ancien Mac

### Étape 1. Commiter l'état du vault

```bash
cd ~/Documents/seo-kb
git status              # tu as ~20 fichiers modifiés non commités
git add -A
git commit -m "snapshot avant migration vers nouveau Mac"
```

### Étape 2. Pousser le vault sur GitHub privé

Ton repo n'a pas de remote. Crée un repo GitHub privé `seo-kb` (interface web ou `gh repo create Tim9501/seo-kb --private`), puis :

```bash
cd ~/Documents/seo-kb
git remote add origin https://github.com/Tim9501/seo-kb.git
git push -u origin main
```

### Étape 3. Sauvegarder la config Obsidian (ignorée par git)

```bash
cd ~/Documents/seo-kb
tar -czf ~/Desktop/obsidian-config.tgz .obsidian/
```

### Étape 4. Sauvegarder Claude Code (skills + settings)

```bash
mkdir -p ~/Desktop/claude-backup
cp -R ~/.claude/skills ~/Desktop/claude-backup/
cp ~/.claude/settings.json ~/Desktop/claude-backup/
```

### Étape 5. Sauvegarder le LaunchAgent

```bash
cp ~/Library/LaunchAgents/co.organikk.seo-kb-revue-presse-pull.plist ~/Desktop/
```

### Étape 6. Vérifier que le sous-repo est à jour

```bash
cd ~/Documents/seo-kb/raw/revue-de-presse
git status
git pull --rebase
```
S'il y a des commits locaux non poussés, `git push`.

### Étape 7. Transfert des fichiers Desktop

Choisis ta méthode :
- **AirDrop** — `obsidian-config.tgz`, le dossier `claude-backup/`, le `.plist`
- **Disque externe** — copier les mêmes
- **iCloud Drive** — déposer dans iCloud le temps du transfert puis supprimer

---

## Sur le nouveau Mac — étape par étape

### Étape 1. Pré-requis à installer

```bash
# Homebrew (si pas déjà là)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git, gh, node
brew install git gh node

# Auth GitHub
gh auth login
```

Installer aussi via DMG :
- **Obsidian** — https://obsidian.md
- **Claude Code** — `npm install -g @anthropic-ai/claude-code` (ou via leur installer officiel)

### Étape 2. Cloner le vault

```bash
mkdir -p ~/Documents
cd ~/Documents
git clone https://github.com/Tim9501/seo-kb.git
```

### Étape 3. Restaurer la config Obsidian

```bash
cd ~/Documents/seo-kb
tar -xzf ~/Desktop/obsidian-config.tgz
```

Vérifie :
```bash
ls .obsidian/
# doit contenir : app.json appearance.json core-plugins.json graph.json workspace.json
```

### Étape 4. Cloner le sous-repo revue de presse

```bash
cd ~/Documents/seo-kb/raw
git clone https://github.com/Tim9501/seo-kb-revue-de-presse.git revue-de-presse
```

### Étape 5. Restaurer Claude Code

```bash
mkdir -p ~/.claude
cp -R ~/Desktop/claude-backup/skills ~/.claude/
cp ~/Desktop/claude-backup/settings.json ~/.claude/
```

Lance `claude` dans le terminal pour finir l'authentification (login compte Anthropic). Les routines cloud et les MCP suivront automatiquement.

### Étape 6. Restaurer le LaunchAgent

```bash
cp ~/Desktop/co.organikk.seo-kb-revue-presse-pull.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/co.organikk.seo-kb-revue-presse-pull.plist
```

Vérifie qu'il tourne :
```bash
launchctl list | grep organikk
tail -f ~/Library/Logs/seo-kb-revue-presse-pull.log
```

### Étape 7. Reconnecter les MCP

Dans Claude Code, lance `/mcp` puis suis les flows d'auth pour Figma, Gmail, Calendar, Drive, WordPress, Windsor. Tu te reconnectes une fois par service.

### Étape 8. Ouvrir le vault dans Obsidian

```bash
open -a Obsidian ~/Documents/seo-kb
```

Si Obsidian ne reconnaît pas le vault automatiquement : `File → Open vault → Open folder as vault → choisir ~/Documents/seo-kb`.

Plugins recommandés (à installer via "Community plugins" si pas déjà actifs) :
- Dataview
- Marp
- Graph Analysis

---

## Vérifications post-migration

Une fois tout en place, fais ces 6 tests :

1. **Vault** — Obsidian s'ouvre, le graph view affiche le réseau de [[concepts]], les wikilinks ne sont pas cassés (cliquer sur un lien dans `AGENTS.md` doit ouvrir la page cible).
2. **Git** — `git -C ~/Documents/seo-kb status` doit être clean.
3. **Sous-repo** — `git -C ~/Documents/seo-kb/raw/revue-de-presse status` doit être clean et pull-able.
4. **LaunchAgent** — laisser passer 15 min puis vérifier que le log se met à jour.
5. **Claude Code** — `claude` lance la session, `/skills` liste les 15 skills custom.
6. **Routine cloud** — vérifier que la prochaine édition Algorithme arrive dans `raw/revue-de-presse/` à l'heure prévue (9h07 Paris).

Si l'un des 6 fail, on debug ce point avant d'utiliser la machine en prod.

---

## Ce qui n'a pas besoin d'être migré

- **Mémoire Claude Code** — `~/.claude/projects/` contient les memories de cette machine. Tu peux la copier si tu veux garder le contexte (les memories sur tes préférences, ta doctrine, les routines actives), mais c'est optionnel. Si tu copies, prends `~/.claude/projects/-Users-boussardontimothee/memory/` à part.
- **Les caches** — tout sera regénéré à la première utilisation.
- **L'historique de session** — `history.jsonl`, `sessions/` : pas utile sur le nouveau Mac.

---

## Récapitulatif minimal — la commande unique

Si tu veux tout faire vite sur l'ancien Mac, lance ce bloc en une fois :

```bash
cd ~/Documents/seo-kb
git add -A && git commit -m "snapshot pré-migration" 2>/dev/null
gh repo create Tim9501/seo-kb --private --source=. --remote=origin --push 2>/dev/null \
  || git push -u origin main

mkdir -p ~/Desktop/migration
tar -czf ~/Desktop/migration/obsidian-config.tgz .obsidian/
cp -R ~/.claude/skills ~/Desktop/migration/skills/
cp ~/.claude/settings.json ~/Desktop/migration/
cp ~/Library/LaunchAgents/co.organikk.seo-kb-revue-presse-pull.plist ~/Desktop/migration/

echo "OK : transfère ~/Desktop/migration vers le nouveau Mac"
```

Sur le nouveau Mac :

```bash
brew install git gh node && gh auth login
cd ~/Documents && git clone https://github.com/Tim9501/seo-kb.git
cd seo-kb && tar -xzf ~/Desktop/migration/obsidian-config.tgz
cd raw && git clone https://github.com/Tim9501/seo-kb-revue-de-presse.git revue-de-presse

mkdir -p ~/.claude
cp -R ~/Desktop/migration/skills ~/.claude/
cp ~/Desktop/migration/settings.json ~/.claude/
cp ~/Desktop/migration/co.organikk.seo-kb-revue-presse-pull.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/co.organikk.seo-kb-revue-presse-pull.plist

open -a Obsidian ~/Documents/seo-kb
```

---

**Connecté avec :** [[concepts/obsidian-as-ide]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/ingest-workflow]] · [[AGENTS]]
