---
type: concept
title: Memory LLM vs Wiki persistant
aliases: [memory-vs-wiki, chatgpt-memory-vs-obsidian, claude-memory-vs-wiki]
tags: [memory, wiki-persistant, claude-code, chatgpt, ownership, exportabilite]
created: 2026-04-13
updated: 2026-04-13
sources: 2
confidence: high
status: stable
---

# Memory LLM vs Wiki persistant

Distinction factuelle à tenir dans tout contenu public Tim : **Memory (ChatGPT, Claude Code) ≠ Wiki persistant (pattern Karpathy)**. Les deux persistent entre sessions. Ils ne font pas la même chose.

## Ce qui est factuellement vrai sur Memory

### ChatGPT Memory

- Lancée par OpenAI en février 2024
- Opt-in initialement, déploiement élargi en 2024-2025
- Mémorise des **faits courts sur l'utilisateur** entre conversations (préférences, contexte récurrent)
- Format propriétaire interne OpenAI
- **Non exportable** en markdown / fichier possédé par l'utilisateur

### Claude Code Memory

Depuis v2.1.59, Claude Code a deux mécanismes documentés officiellement ([code.claude.com/docs/fr/memory](https://code.claude.com/docs/fr/memory)) :

- **`CLAUDE.md`** — instructions écrites par l'utilisateur, chargées à chaque session
- **Mémoire automatique** — Claude écrit lui-même des notes dans `~/.claude/projects/<project>/memory/MEMORY.md`
- Activée par défaut
- **Plafond chargement** : 200 premières lignes ou 25 Ko de `MEMORY.md`. Au-delà, Claude ouvre les fichiers de sujet à la demande.

**La formulation "Claude repart de zéro à chaque session" est factuellement fausse** dans ce contexte. À corriger dans les productions Tim.

## Ce qui distingue un Wiki persistant (Karpathy / cette KB)

| Axe | Memory LLM | Wiki persistant |
|---|---|---|
| **Propriété** | Format interne LLM | Fichiers markdown bruts possédés |
| **Taille** | 200 lignes / 25 Ko (Claude) ou faits courts (ChatGPT) | Non limité (cette KB : 36 sources, 36 entités, 30+ concepts, centaines de pages) |
| **Cross-références** | Plate, peu ou pas de liens | Wikilinks `[[...]]`, graphe navigable |
| **Navigation sans IA** | Non consultable hors chat | Obsidian, VSCode, n'importe quel éditeur markdown |
| **Versioning** | Non exposé | `git` standard |
| **Exportabilité** | Format propriétaire LLM | Markdown = portable sur n'importe quel outil |
| **Lint / contradictions** | Non géré | Workflow explicite (cf. AGENTS.md §6.3) |
| **Cohabitation multi-IA** | Verrou éditeur (OpenAI ou Anthropic) | Changer d'IA demain sans perdre le wiki |
| **Finalité** | Contexte injecté pour que l'IA te réponde mieux | Artefact autonome que tu consultes avec ou sans IA |

## Formulation correcte à adopter

**❌ Faux** : *"Claude repart à zéro à chaque conversation."*

**❌ Trop absolu** : *"Chaque session est isolée."*

**✅ Factuel** : *"Claude Code et ChatGPT Memory stockent bien des préférences entre sessions. Mais elles ne maintiennent pas un artefact que tu possèdes et navigues en autonomie."*

**✅ Précis** : *"Claude Memory charge 200 lignes au start. Un wiki Karpathy/Obsidian en charge autant que nécessaire et surtout te donne un graphe navigable sans IA."*

## Argument robuste face à un fact-check

1. **Reconnaître la précision** : oui, Memory existe et persiste. Ne pas nier un fait vérifiable.
2. **Recentrer sur la bonne distinction** : Memory = pour l'IA / Wiki = pour toi. C'est une différence de finalité, pas de présence/absence.
3. **Ancrer dans les limites techniques documentées** : 200 lignes Claude Memory, format propriétaire ChatGPT Memory = limites publiées par les vendeurs eux-mêmes, pas des inventions.
4. **Rappeler le cas du changement d'IA** : si tu changes de LLM demain (Claude → Gemini → autre), Memory disparaît avec l'éditeur. Un dossier markdown reste.

## Limites de cette distinction

- **Claude Code Memory et Wiki peuvent coexister** : rien n'empêche d'utiliser les deux en même temps. Memory est un complément, pas un concurrent
- **Pour un usage très léger** (quelques préférences, pas de KB), Memory suffit — construire un wiki serait du sur-engineering
- **Le pattern Karpathy demande une discipline** (ingest, lint, log) que Memory évite — tradeoff réel

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[sources/2026-04-13-titans-architecture-google-deepmind]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/obsidian-as-ide]] · [[concepts/ingest-workflow]] · [[revues-presse/2026-04-13-claude-code-obsidian-sans-complexite]]
