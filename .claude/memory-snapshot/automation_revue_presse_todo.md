---
name: Automatisations seo-kb — agents installés
description: État des automatisations vault (5 agents posés 2026-05-02). 3 GH Actions cron + 2 slash commands locaux. Décisions de stack et évolutions différées.
type: project
originSessionId: 47699f81-7aab-4036-a888-f4235d07c181
---
## Stack actuelle (posée 2026-05-02)

**Revue de presse — auto via GitHub Actions**
- Workflow : `.github/workflows/revue-presse.yml`
- Cron : `0 7 * * *` UTC (≈ 9h Paris été / 8h Paris hiver)
- Skill : `.claude/skills/revue-presse-quotidienne/SKILL.md` (project-scoped, embarqué dans repo)
- Output : `raw/revue-de-presse/YYYY-MM-DD-revue-presse.md`
- Sources scannées : ArXiv, SEL, SEJ, Google Search Central, The Verge, TechCrunch, Substack, LinkedIn, Reddit, X
- Format : multi-piliers SEO+IA+Contenu (1 info principale + 2-3 signaux radar)
- Coût estimé : ~$0.02-0.10/jour
- Pré-requis manuel Tim : ajouter secret `ANTHROPIC_API_KEY` dans repo settings

**Todo — manuel via slash command**
- Commande : `/todo` (déclenchement manuel uniquement, pas de cron, pas de hook)
- Source de données : transcripts JSONL Claude Code locaux (`~/.claude/projects/-Users-timothee-Documents-seo-kb/` + `-Users-timothee-Documents-organikk-next/`)
- Output : `raw/todo/todo-actuelle.md` (fichier unique, overwrite incrémental qui préserve les "à faire" non cochés)
- Format : ✅ Fait / 🔄 En cours / 📋 À faire (priorisé prio 1/2/3)

**Audit vault — auto via GitHub Actions**
- Workflow : `.github/workflows/audit-vault.yml`
- Cron : `0 6 * * 0` UTC (dimanche 08h Paris été / 07h hiver)
- Skill : `.claude/skills/audit-vault-hygiene/SKILL.md`
- Output : `wiki/audit/YYYY-MM-DD-audit.md`
- Détecte : wikilinks cassés, fichiers orphelins, slugs dupliqués, frontmatter cassé
- Pas de réparation auto, juste un rapport actionnable

**Récap hebdo Algorithme — auto via GitHub Actions**
- Workflow : `.github/workflows/algorithme-recap-hebdo.yml`
- Cron : `0 18 * * 0` UTC (dimanche 20h Paris été / 19h hiver — après revue du dimanche)
- Skill : `.claude/skills/algorithme-recap-hebdo/SKILL.md`
- Output : `wiki/syntheses/algorithme-week-YYYY-WNN.md`
- Synthèse transversale : tendance dominante, pilier le plus chaud, consensus, désaccords, signaux faibles, angles à creuser semaine suivante

**Décisions répétées — manuel via slash command**
- Commande : `/repeats` (déclenchement manuel)
- Source : transcripts JSONL Claude Code (seo-kb + organikk-next, fenêtre 30j)
- Output : `wiki/syntheses/decisions-repetees.md` (overwrite, historique dans git)
- 6 catégories de patterns : positions doctrinales, arguments réutilisés, refus récurrents, concepts non-formalisés, process répétés, décisions stratégiques
- Filtre : 3+ occurrences minimum
- Pour chaque pattern : verbatims + type de formalisation suggérée (concept / entity / CLAUDE.md / skill / tim-my-voice.md)

## Why
Tim a explicitement choisi cette stack après évaluation comparative (launchd / GH Actions / Agent SDK / hooks). GH Actions sur la revue de presse pour autonomie 24/7 sans dépendance Mac allumé. Slash command pour la todo car les transcripts JSONL sont locaux au Mac (GH Actions n'y accède pas) et un mécanisme repo-based (commits + log.md) ne capte pas les conversations Claude qui n'aboutissent pas à un fichier.

## How to apply
- Si Tim demande des modifs sur la revue de presse : éditer skill ou workflow YAML, jamais réintroduire les 3 skills legacy archivés (`raw/notes/scheduled-skills/_archive/`).
- Si Tim demande des modifs sur la todo : éditer `.claude/commands/todo.md`, ne pas créer de hook Stop ou cron tant qu'il n'a pas validé l'évolution.

## Évolution différée (à revisiter ~2026-05-22)
Tim veut valider la version 1 sur 2-3 semaines avant de décider :
- Option A : hook SessionEnd dans `~/.claude/settings.json` qui append automatiquement à la fin de chaque session Claude
- Option B : cron launchd local à 23h qui scanne les sessions du jour
À ce moment-là, mesurer combien de fois Tim a tapé `/todo` manuellement pour décider si l'auto vaut la complexité.
