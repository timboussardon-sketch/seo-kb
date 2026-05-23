---
type: doctrine
title: IA Employé Tim — architecture & roadmap
date: 2026-05-02
updated: 2026-05-05
tags: [ia-employe, infrastructure, automation, kb, agents]
status: living-doc
---

# IA Employé Tim — architecture & roadmap

> Document vivant qui suit la construction d'un "employé IA" Tim Boussardon : un agent (ou stack d'agents) qui combine le vault Obsidian, les skills SEO, et la mémoire conversationnelle pour exécuter des actions de manière de plus en plus autonome.

## Vision

Un employé IA n'est pas un chatbot. C'est un **système qui agit** sur la base de :
- **Connaissances** (vault Obsidian = sa mémoire long terme)
- **Compétences** (skills `.md` = ses procédures opérationnelles)
- **Contexte** (conversations passées = sa compréhension de ce qui se passe)
- **Triggers** (cron, signaux externes, demandes Tim = ses déclencheurs d'action)
- **Garde-fous** (budget d'autonomie : que peut-il publier/envoyer sans validation ?)

Deux modes complémentaires à terme :
1. **Réactif** — Tim parle, l'employé bosse (Slack bot, CLI, web UI). Aujourd'hui : Claude Code en local.
2. **Proactif** — l'employé scanne des signaux et agit seul (revue de presse quotidienne, audit hebdo, alertes GSC, etc.). Aujourd'hui : 5 GH Actions tournent déjà.

## Ce qui existe (mai 2026)

### Mémoire (vault Obsidian `seo-kb/`)
Architecture **Karpathy** raw + wiki :
- `raw/` — matière brute non éditée (transcripts clients, todos, données, articles, revue de presse)
- `wiki/` — connaissances stabilisées et maillées (concepts, briefs, syntheses, posts-linkedin)
- `mockups/` — drafts en cours

Sous-dossiers `raw/` actifs : `agents`, `articles`, `assets`, `cas-clients`, `data`, `etudes-seo`, `newsletter`, `notes`, `papers`, `revue-de-presse`, `scoring`, `todo`, `transcripts`.

### Compétences (skills)
**Skills user-globaux** (`~/.claude/skills/`, 15) — tous SEO :
- Recherche & analyse : `kb-semantic-search`, `seo-cannibalisation`, `seo-quick-win`, `maillage-interne-gsc`, `maillage-systeme`
- Stratégie : `seo-cluster-aeo`, `seo-programmatique-pseo`, `seo-product-led-seo`, `seo-entites-vectorielles`, `seo-peurs-objections`
- Production : `seo-brief-contenu`, `seo-workflow-article`, `article-engine-pipeline`
- Site Organikk : `organikk-site`, `organikk-blog-article`

**Skills projet** (`.claude/skills/`, 3) — tous automatisés via GH Actions :
- `revue-presse-quotidienne`
- `audit-vault-hygiene`
- `algorithme-recap-hebdo`

**Skills spécifiés mais non encore matérialisés dans `~/.claude/skills/`** :
- `kw-research-workflow` — orchestrateur 5 phases (KP → GSC → Grok DeepSearch → verbatims → pSEO) + livrable Sheet scoré 5 critères. Spec : [[raw/notes/skill-kw-research-workflow]]. Doctrine doctrinale : [[syntheses/process-keyword-research-5-etapes]]. Premier post LinkedIn : [[posts-linkedin/2026-05-05-workflow-kw-research-5-etapes]]. **À matérialiser** : créer `~/.claude/skills/kw-research-workflow/SKILL.md` à partir de la spec pour rendre le skill exécutable.

### Automatisations actives (GH Actions)
1. **`revue-presse.yml`** — édition quotidienne newsletter Algorithme (cron quotidien)
2. **`audit-vault.yml`** — audit hygiène vault hebdo
3. **`algorithme-recap-hebdo.yml`** — synthèse 7 dernières revues (dimanche soir)

### Slash commands locaux (`.claude/commands/`)
- `/todo` — reconstruit `raw/todo/todo-actuelle.md` depuis transcripts Claude Code (7j, seo-kb + organikk-next)
- `/repeats` — détecte les rabâchages (30j)

### Mémoire conversationnelle (`~/.claude/projects/-Users-timothee-Documents-seo-kb/memory/`)
- `MEMORY.md` (index) + fichiers thématiques
- `canonical_vault_path.md`, `automation_revue_presse_todo.md`
- Persiste entre sessions Claude Code

## Ce qui manque pour un vrai "employé IA"

### 1. Compilation quotidienne du contexte conversationnel ⬅ EN COURS
**Problème** : `/todo` capture les actions, `/repeats` capture les rabâchages, mais **personne ne capture la substance** des conversations (décisions, idées, pivots, questions ouvertes). Les JSONL sont là, mais pas synthétisés.

**Solution en cours** : slash command `/recap-jour` (créé en parallèle de cette note). Lit les transcripts des dernières 24h, écrit `raw/journal/YYYY-MM-DD.md`. Voir `.claude/commands/recap-jour.md`.

**Next step** : automatiser via launchd/cron local (les GH Actions ne peuvent pas lire les JSONL locaux).

### 2. Identité & voix unifiée
**Problème** : la voix Tim est définie dans `raw/notes/tim-my-voice.md` mais doit être systématiquement chargée. Pas de "system prompt employé" central.

**Piste** : créer `wiki/agents/employe-tim/identite.md` avec persona + style + doctrine + garde-fous, qu'on injecte dans tous les agents.

### 3. Triggers proactifs au-delà du cron
**Problème** : les 3 GH Actions actuelles tournent sur cron pur. Pas de trigger sur événement (push GSC anomalie, mention Tim sur LinkedIn, mail client urgent…).

**Pistes** : webhooks GitHub, polling RSS/Atom, Zapier/n8n, ou MCP servers maison.

### 4. Surface d'interaction hors Claude Code
**Problème** : aujourd'hui Tim doit ouvrir Claude Code en CLI. Pas d'accès Slack / mobile / web.

**Pistes** :
- Court terme : raccourcis iOS Shortcuts qui appellent Claude API + skills locales (impossible directement, faudrait packager)
- Moyen terme : Slack bot via Claude Agent SDK qui monte le vault + skills
- Long terme : web UI dédiée (Next.js + Agent SDK)

### 5. Garde-fous & budget d'autonomie
**Problème** : aucun cadre formel pour "ce que l'employé peut publier/envoyer sans validation". Aujourd'hui par défaut = rien (tout est draft).

**À définir** :
- Quels artefacts auto-publiables (drafts dans le vault → oui ; posts LinkedIn → non) ?
- Quels budgets en tokens/€ par run ?
- Quels appels externes autorisés ?

## Roadmap

### Phase 1 — Substrat conversationnel (mai 2026, en cours)
- [x] Vault structuré raw + wiki
- [x] 15 skills SEO opérationnels
- [x] 3 automations GH Actions
- [x] `/todo` + `/repeats`
- [ ] **`/recap-jour`** ⬅ ajouté aujourd'hui
- [ ] Cron local pour `/recap-jour` (launchd Mac)

### Phase 2 — Identité & doctrine (à venir)
- [ ] `wiki/agents/employe-tim/identite.md` (persona unifiée)
- [ ] Convention "qui peut publier quoi" formalisée
- [ ] Mémoire conversationnelle enrichie depuis les journaux quotidiens

### Phase 3 — Surfaces d'interaction (à venir)
- [ ] Décider : Slack bot OU web UI OU les deux
- [ ] Bootstrap Agent SDK avec vault monté + skills
- [ ] Authentification + permissions

### Phase 4 — Triggers proactifs (à venir)
- [ ] Webhook GSC (alertes drops)
- [ ] Polling LinkedIn / Twitter pour mentions
- [ ] Triggers email (mails clients = ouverture session ?)

### Phase 5 — Autonomie cadrée (à venir)
- [ ] Budget tokens par agent/run
- [ ] Whitelist actions auto vs validation requise
- [ ] Dashboard de supervision (que fait l'employé en ce moment ?)

## Décisions à trancher

- **Un employé monolithique ou plusieurs agents spécialisés ?** Aujourd'hui on a un proto-employé distribué (3 GH Actions + slash commands). Faut-il consolider en une entité unique avec mémoire partagée, ou continuer en stack d'agents indépendants qui s'écrivent dans le même vault ?
- **Hosting** : tout reste sur GH Actions + local Mac, ou on dédie un VPS / un service ?
- **Modèle** : Opus pour tout, ou répartir Opus (raisonnement) / Sonnet (production) / Haiku (extraction) selon la tâche pour optimiser coût ?

## Index

- Skills user : `~/.claude/skills/`
- Skills projet : `.claude/skills/`
- Slash commands : `.claude/commands/`
- Workflows : `.github/workflows/`
- Mémoire conversationnelle : `~/.claude/projects/-Users-timothee-Documents-seo-kb/memory/`
- Journal quotidien (à venir) : `raw/journal/YYYY-MM-DD.md`

---

*Document mis à jour manuellement. Reflète l'état au 2026-05-02. Si tu modifies l'archi, mets à jour cette note avant de partir.*
