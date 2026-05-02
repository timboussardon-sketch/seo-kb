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

# 3. LaunchAgent /recap-jour
cp ~/Documents/seo-kb/.claude/launchd/com.timboussardon.recap-jour.plist ~/Library/LaunchAgents/
launchctl load -w ~/Library/LaunchAgents/com.timboussardon.recap-jour.plist

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

Les snapshots `memory-snapshot/` et `transcripts-archive/` ne se mettent PAS à jour automatiquement. Pour les rafraîchir (ex: tous les mois) :

```bash
# Memory
cp -r ~/.claude/projects/-Users-timothee-Documents-seo-kb/memory/. ~/Documents/seo-kb/.claude/memory-snapshot/

# Transcripts
cd ~/.claude/projects
tar czf ~/Documents/seo-kb/.claude/transcripts-archive/transcripts-$(date +%Y-%m-%d)-snapshot.tar.gz \
  -- "-Users-timothee-Documents-seo-kb" "-Users-timothee-Documents-organikk-next"

cd ~/Documents/seo-kb
git add .claude/memory-snapshot .claude/transcripts-archive
git commit -m "Refresh memory + transcripts snapshot $(date +%Y-%m-%d)"
git push
```

## Pourquoi tout n'est pas dans `~/.claude/`

Les répertoires sous `~/.claude/` (skills, projects, credentials) sont **runtime**, pas du code. Les snapshoter dans le vault permet :
- Un backup complet sur GitHub
- Une reconstruction d'identité numérique sur n'importe quel Mac neuf en < 10 min
- Une mémoire à long terme indépendante de la machine

Voir `wiki/agents/ia-employe.md` pour la doctrine globale "IA employé".
