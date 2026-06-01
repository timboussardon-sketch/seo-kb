---
name: macOS launchd + TCC bloquent ~/Documents
description: Sur macOS Sequoia, les LaunchAgents (cron locaux) ne peuvent ni exécuter ni lire dans ~/Documents/. Garder tout repo qui doit être touché par cron hors de ce dossier (~/Code/, ~/work/, etc.).
type: feedback
originSessionId: 3793f4e3-3113-4543-8bb6-f7bbcdcbc4bd
---
Sur macOS Sequoia, **TCC bloque toutes les opérations file/dir dans `~/Documents/` quand elles viennent du contexte launchd** (LaunchAgents auto). L'exec du wrapper, les `ls`, `mkdir`, `cd` réussissent ou échouent de façon inconsistante, et le job sort avec un exit non-zéro silencieux (souvent 78). Donner Full Disk Access à `/bin/zsh` via System Settings ne suffit PAS car TCC évalue le "responsible process" (= launchd lui-même), pas zsh.

**Why:** découvert le 2026-05-04 en migrant `revue-presse` de GH Actions vers cron local. Les LaunchAgents `recap-jour` et `refresh-snapshots` souffraient déjà du même bug en silence depuis le 2 mai — Tim ne voyait pas les fails parce qu'il déclenchait les jobs à la main pour les tester. Première tentative (déplacer juste les wrappers vers `~/.local/bin/seo-kb/`) a échoué parce que le wrapper exécutait ensuite des `ls .claude/memory-snapshot/` etc. dans `~/Documents/seo-kb/`, eux-mêmes bloqués. **Solution finale** : déplacer le repo entier vers `~/Code/seo-kb/` (zone non-TCC). Test concluant : `LastExitStatus = 0` après mv, vs `LastExitStatus = 78` avant.

**How to apply:**
1. Tout repo qui doit être touché par un LaunchAgent (cron auto) doit vivre **hors de `~/Documents/`**. `~/Code/`, `~/work/`, `~/projects/` sont OK.
2. Wrappers dans `.claude/bin/run-*.sh` (canonique versionné) et copie active dans `~/.local/bin/seo-kb/run-*.sh` (la copie est l'historique du premier workaround partiel — le repo hors `~/Documents` rend cette copie redondante mais inoffensive).
3. Plists dans `.claude/launchd/*.plist` (canonique versionné) + copie chargée dans `~/Library/LaunchAgents/`.
4. Si Tim relance Claude Code pour la première fois après le mv, le slug projet devient `-Users-timothee-Code-seo-kb` (la mémoire a été copiée depuis l'ancien slug `-Users-timothee-Documents-seo-kb` le 2026-05-04).
5. Ne JAMAIS proposer "ajouter /bin/zsh à FDA via System Settings" comme fix : ça ne marche pas dans le contexte launchd Sequoia, et Tim a déjà essayé sans succès.

Si un jour Tim veut remettre un repo sous cron auto et qu'il est dans `~/Documents/` : la seule option est `mv` vers `~/Code/`. Pas de bricolage TCC à essayer.
