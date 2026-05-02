# `.claude/` — Claude Code config + backups

Layout :

```
.claude/
├── bin/                     # Wrappers exécutés par launchd / cron
│   └── run-recap-jour.sh
├── commands/                # Slash commands projet (/todo, /repeats, /recap-jour)
├── skills/                  # Skills projet (revue-presse, audit-vault, recap-hebdo)
├── settings.json            # Permissions Claude Code
├── launchd/                 # Snapshot des LaunchAgents macOS (pour restore)
├── memory-snapshot/         # Snapshot manuel de ~/.claude/projects/.../memory/
├── transcripts-archive/     # Snapshots tarball des transcripts JSONL (one-shot)
└── logs/                    # Runtime logs (gitignored)
```

## Restore complet sur un nouveau Mac

```bash
# 1. Vault (ce repo)
git clone https://github.com/timboussardon-sketch/seo-kb.git ~/Documents/seo-kb

# 2. Skills user-globaux (repo séparé)
git clone https://github.com/timboussardon-sketch/tim-claude-skills.git ~/.claude/skills

# 3. LaunchAgents (recap-jour quotidien + refresh-snapshots mensuel)
cp ~/Documents/seo-kb/.claude/launchd/com.timboussardon.*.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/com.timboussardon.recap-jour.plist
launchctl load -w ~/Library/LaunchAgents/com.timboussardon.refresh-snapshots.plist

# 4. Mémoire conversationnelle (au moment du snapshot)
mkdir -p ~/.claude/projects/-Users-timothee-Documents-seo-kb/memory
cp -r ~/Documents/seo-kb/.claude/memory-snapshot/. ~/.claude/projects/-Users-timothee-Documents-seo-kb/memory/

# 5. Transcripts JSONL archivés (au moment du snapshot)
cd ~/.claude/projects
tar xzf ~/Documents/seo-kb/.claude/transcripts-archive/transcripts-YYYY-MM-DD-snapshot.tar.gz

# 6. Auth Claude Code (à refaire manuellement)
claude  # déclenche le flow d'auth
```

## Re-snapshoter périodiquement

**Automatisé** : le LaunchAgent `com.timboussardon.refresh-snapshots` tourne le **1er de chaque mois à 8h** et lance `bin/run-refresh-snapshots.sh` qui :

1. Refresh `memory-snapshot/`
2. Crée un nouveau tarball dans `transcripts-archive/transcripts-YYYY-MM-DD-snapshot.tar.gz`
3. Prune les tarballs > 180 jours (garde ~6 mois d'historique)
4. Commit + push si changements

Logs dans `.claude/logs/refresh-snapshots-YYYY-MM-DD.log`.

**Manuel** (si besoin de forcer un snapshot maintenant) :

```bash
~/Documents/seo-kb/.claude/bin/run-refresh-snapshots.sh
```

## Pourquoi tout n'est pas dans `~/.claude/`

Les répertoires sous `~/.claude/` (skills, projects, credentials) sont **runtime**, pas du code. Les snapshoter dans le vault permet :
- Un backup complet sur GitHub
- Une reconstruction d'identité numérique sur n'importe quel Mac neuf en < 10 min
- Une mémoire à long terme indépendante de la machine

Voir `wiki/agents/ia-employe.md` pour la doctrine globale "IA employé".
