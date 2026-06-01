---
name: Canonical SEO KB Obsidian vault path
description: The single source of truth for all SEO KB edits is /Users/timothee/Code/seo-kb/ (Obsidian vault, moved from ~/Documents on 2026-05-04). Never edit copies elsewhere.
type: feedback
originSessionId: fcb3d870-d9e9-4689-ac81-bc37f188e359
---
Toujours éditer la SEO KB dans le vault Obsidian canonique : **`/Users/timothee/Code/seo-kb/`** (présence d'un dossier `.obsidian` confirmée).

**Why:** Le 2026-05-02, Tim avait 3 copies du fichier `wiki/briefs/reddit-pour-geo-2026.md` sur son Mac (vault canonique + 2 dossiers `tim-claude-transfer` snapshots de transferts passés). Il lisait depuis une copie obsolète et croyait que mes edits n'avaient pas été appliqués. Les dossiers `tim-claude-transfer` ont été supprimés à sa demande pour éviter la confusion.

**Le 2026-05-04, le repo a été migré de `/Users/timothee/Documents/seo-kb/` vers `/Users/timothee/Code/seo-kb/`** parce que macOS Sequoia bloque les LaunchAgents (cron locaux) qui tentent d'accéder à `~/Documents/` via TCC. Le déplacement vers `~/Code/` (zone non-TCC) débloque les 3 LaunchAgents (`revue-presse`, `recap-jour`, `refresh-snapshots`).

**How to apply:**
- Tous les edits de fichiers markdown SEO/GEO (briefs, concepts, entités, sources, syntheses, etc.) doivent cibler `/Users/timothee/Code/seo-kb/`.
- Si une recherche `find` remonte plusieurs copies d'un même fichier ailleurs (Desktop, autres dossiers, ou ancien path `~/Documents/seo-kb/` qui ne devrait plus exister), **flagger la duplication** avant d'éditer — ne pas propager les edits sur des copies sans confirmation explicite.
- Le vault iCloud Obsidian `timSEO` (sous `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/timSEO/`) est un vault **séparé** de la SEO KB : ne pas le confondre, ne pas y écrire sauf demande explicite.
- Pour les implémentations site Next.js (Organikk), c'est un autre repo (`organikk-next`), pas la KB — la KB contient les briefs, le repo contient le code.

**Diagnostic "Tim ne voit pas mon edit" :** quand Tim affirme que les modifs n'apparaissent pas alors que le fichier sur disque est bien à jour, vérifier d'abord :
1. **Quel vault Obsidian est ouvert** : `cat ~/Library/Application\ Support/obsidian/obsidian.json` — si le path n'est pas `/Users/timothee/Code/seo-kb/`, c'est la cause. Tim doit "Open another vault" sur le bon path.
2. **Doublons sur le disque** : `find ~ -name "<filename>" 2>/dev/null` pour repérer des copies parallèles.
3. **Cache éditeur** : refresh manuel (`Cmd+R` Obsidian, "Revert File" VS Code).

Faire ce diagnostic AVANT de re-démontrer le contenu du fichier — sinon on tourne en rond plusieurs messages.
