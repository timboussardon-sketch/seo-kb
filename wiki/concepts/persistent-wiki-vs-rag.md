---
type: concept
title: Wiki persistant vs RAG
aliases: [persistent-wiki, rag-vs-wiki, wiki-vs-rag]
tags: [pattern-kb, wiki, rag, meta, fondation]
created: 2026-04-11
updated: 2026-08-07
sources: 1
confidence: high
status: stable
---

# Wiki persistant vs RAG

Le contraste central du pattern proposé par [[entities/karpathy]] dans [[sources/2026-04-11-karpathy-llm-wiki]].

> **Mise à jour 2026-08-07** ([[revue-hebdo/2026-W32]] point 6, résurgence [[revue-hebdo/resurgence-2026-08-05]]) : le cadrage binaire ci-dessous date du bootstrap du vault. `wiki/sources/` compte aujourd'hui 110 fichiers — le seuil « ~100 sources » que la source elle-même désignait comme point de bascule (§ Argument d'échelle) est franchi. Et le tooling a effectivement émergé : `.claude/vector-store/` (ChromaDB, embeddings `paraphrase-multilingual-mpnet-base-v2`) + `.claude/index/concepts.json`, exposés via `./kb` (AGENTS.md §7ter, skill `kb-semantic-search`), commit du 2026-05-26. Ce n'est pas un remplacement du wiki par du RAG, c'est une superposition : `./kb search` fait de la recherche cosinus sur des embeddings (RAG au sens strict), mais chaque chunk garde ses métadonnées frontmatter (type, tags, status, confidence) pour un filtrage déterministe avant la recherche sémantique, et `concepts.json` (wikilinks, backrefs) reste la structure atomique de référence. Le clivage qui compte n'est plus « wiki **ou** RAG » mais « qui compile » (le wiki, une fois, en continu) vs « qui récupère » (le vector store, à chaque query) — deux couches complémentaires, pas deux architectures concurrentes. Voir [[concepts/cli-tools-optional]], mis à jour en miroir le même jour.

## Les deux approches

### RAG (approche standard)

- Upload d'une collection de fichiers
- Le LLM récupère des chunks à la query time
- Il génère une réponse à partir de ces chunks
- **Rien ne s'accumule** : chaque question repart de zéro
- Exemples cités : [[entities/notebooklm]], ChatGPT file uploads, la plupart des systèmes RAG

### Wiki persistant (la proposition)

- Le LLM **lit une nouvelle source** et l'intègre dans un wiki existant
- Il met à jour les pages entities, révise les résumés, flag les contradictions
- Le savoir est **compilé une fois** et ensuite **maintenu à jour**
- Le wiki est un **artefact compoundant** : cross-refs, contradictions, synthèse déjà prêtes *avant* la question

## Le point clé

> "The knowledge is compiled once and then kept current, not re-derived on every query"

Dans RAG, la synthèse se fait **au moment** de la question. Dans le wiki persistant, la synthèse est **déjà faite** et elle compose avec chaque nouvelle source ingérée.

## Argument d'échelle

[[entities/karpathy]] affirme que pour ~100 sources / quelques centaines de pages, un simple `index.md` suffit pour router vers les bonnes pages — **pas besoin d'infrastructure RAG à base d'embeddings**. La KB devient un problème d'organisation markdown, pas un problème d'ingénierie vectorielle. Cf. [[concepts/cli-tools-optional]] pour ce qui émerge au-delà.

## Limite importante

La source **ne benchmarke pas** les deux approches. Pas de métrique comparative sur MRR, latence, coût de maintenance, qualité des réponses. L'argument est **structurel et qualitatif**, pas empirique. À vérifier avec d'autres sources avant d'en faire une doctrine.

## Relation à d'autres concepts

- [[concepts/ingest-workflow]] — le *comment* de la compilation persistante
- [[concepts/query-synthesis]] — le *comment* des questions contre le wiki
- [[concepts/obsidian-as-ide]] — l'interface humaine au-dessus du wiki
- Présenté comme l'héritier du Memex de [[entities/vannevar-bush]] (1945)

## Implications SEO (ouvertes)

À creuser dans une query dédiée : **les moteurs génératifs (SGE, ChatGPT Search, Perplexity) sont-ils du RAG stateless ou maintiennent-ils un état persistant ?** La réponse change fondamentalement ce que signifie "être cité" dans le GEO.

- Si stateless → chaque query est une nouvelle chance et une nouvelle compétition, l'optimisation se concentre sur la retrouvabilité
- Si état persistant → certains contenus sont "fixés" dans le modèle, l'optimisation se concentre sur l'entrée dans cet état

Non résolu par cette seule source — à croiser avec des papers sur les architectures de SGE, les docs Google Bing, des tests terrain, et des sources comparant les comportements de Perplexity et ChatGPT Search.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[entities/karpathy]] · [[entities/notebooklm]] · [[entities/vannevar-bush]] · [[concepts/ingest-workflow]] · [[concepts/query-synthesis]]
