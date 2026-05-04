---
name: macOS launchd + TCC bloquent ~/Documents
description: Tout LaunchAgent qui exécute un script depuis ~/Documents échoue silencieusement sur macOS Sequoia ; mettre les wrappers dans ~/.local/bin/seo-kb/
type: feedback
originSessionId: 3793f4e3-3113-4543-8bb6-f7bbcdcbc4bd
---
Sur macOS Sequoia, `launchd` en contexte service ne peut PAS exécuter un script situé dans `~/Documents/` — TCC bloque l'accès et le job échoue avec `/bin/zsh: can't open input file: ...`. Le script peut quand même `cd` dans `~/Documents/` et y lire/écrire une fois lancé : c'est uniquement le `exec` initial du wrapper qui est bloqué.

**Why:** découvert le 2026-05-04 en migrant `revue-presse` de GH Actions vers cron local. Les LaunchAgents `recap-jour` et `refresh-snapshots` souffraient déjà du même bug en silence — Tim ne voyait pas les fails parce qu'il déclenchait les jobs à la main pour les tester. Donner Full Disk Access à `/bin/zsh` via System Settings fonctionnerait aussi mais nécessite une action GUI manuelle et n'est pas reproductible sur une autre machine.

**How to apply:** pour tout nouveau LaunchAgent dans le vault seo-kb (ou tout repo dans `~/Documents/`) :
1. Garder le wrapper canonique versionné dans `.claude/bin/run-*.sh` (source de vérité)
2. Copier vers `~/.local/bin/seo-kb/run-*.sh` (zone non-TCC)
3. Pointer le `ProgramArguments` du plist vers la copie hors-TCC, pas la version repo
4. Le wrapper peut ensuite `cd /Users/timothee/Documents/seo-kb` sans problème

Ne jamais pointer un plist directement vers un script dans `~/Documents/`.
