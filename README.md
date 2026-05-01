# SEO Knowledge Base

Une base de connaissances personnelle SEO/IA/GEO construite et maintenue par un agent LLM.

Inspirée du pattern [LLM Wiki d'Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Principe

- `raw/` = tes sources (articles, papers, data). **Immuable**.
- `wiki/` = le wiki markdown entièrement écrit par Claude Code. Tu le lis dans Obsidian.
- `AGENTS.md` = le schéma qui me dit comment construire et maintenir le wiki.

## Workflow quotidien

1. Tu trouves une source → glisse dans `raw/articles/`
2. Tu me dis : "ingère raw/articles/foo.md"
3. Je lis, je crée `wiki/sources/...md`, je mets à jour entities/concepts, je mets à jour index.md + log.md
4. Tu ouvres Obsidian et tu explores les nouvelles connexions dans le graph view

## Quick start

```bash
# Init git
git init
git add .
git commit -m "bootstrap: AGENTS.md v1.0 + stubs wiki"

# Ouvre comme vault Obsidian
open -a Obsidian .

# Lance Claude Code
claude
```

Puis dis-moi : "ingère raw/articles/karpathy-llm-wiki.md"

## Stack

- **Editor** : Obsidian (wikilinks `[[...]]`, graph view, plugins)
- **Agent** : Claude Code (lit AGENTS.md, exécute workflows)
- **Versioning** : git (markdown files, history)

## Plugins recommandés

- Dataview (queries dynamiques sur frontmatter)
- Marp (slide decks depuis markdown)
- Graph Analysis (visualiser la structure)
