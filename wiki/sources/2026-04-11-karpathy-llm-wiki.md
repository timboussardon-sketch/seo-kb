---
type: source
source_type: article
title: LLM Wiki (Karpathy)
aliases: [karpathy-llm-wiki, llm-wiki-pattern]
tags: [pattern-kb, wiki-persistent, llm, rag, meta, foundational]
created: 2026-04-11
updated: 2026-04-11
sources: 1
confidence: high
status: stable
---

# LLM Wiki (Karpathy)

**Auteur** : [[entities/karpathy]]
**Type** : article d'idée (gist public)
**Fichier raw** : `raw/articles/karpathy-llm-wiki.md`
**Date de publication** : non précisée dans la source
**Source originale** : gist Karpathy (URL mentionnée dans le README du repo)

---

## Contexte

Karpathy propose un pattern pour construire des bases de connaissances personnelles maintenues par un agent LLM. Le document est **explicitement abstrait** — il décrit l'idée, pas une implémentation. Il est pensé pour être collé dans un agent (Claude Code, Codex, OpenCode…) qui co-construira les spécificités avec l'utilisateur.

## Méthode

Le document n'est pas une étude — c'est une spécification narrative. Pas de méthodologie empirique, pas de protocole de test. L'argumentation repose sur :

- Une analogie structurante (IDE / programmeur / codebase)
- Une expérience rapportée (10-15 pages touchées par ingest, ~100 sources avant besoin de tooling)
- Un rattachement historique (Memex de Bush, 1945)

## Chiffres clés

- **10-15 pages** touchées lors de l'ingest d'une seule source. C'est le chiffre central — il sépare un classement manuel d'un ingest LLM.
- **~100 sources** = seuil à partir duquel `index.md` seul ne suffit plus. Au-delà, un moteur de recherche (type `qmd`) devient utile.
- **1945** = année de publication de l'essai de Vannevar Bush sur le Memex, référencé comme ancêtre spirituel du pattern.

Tous les autres claims sont qualitatifs. Aucun benchmark, aucune métrique comparative RAG vs wiki persistant.

## Résumé structuré

### Thèse centrale

**RAG** = le LLM récupère des chunks à la query time et génère une réponse. Rien ne s'accumule entre les questions. Exemples cités : [[entities/notebooklm]], ChatGPT file uploads, la majorité des systèmes RAG.

**Wiki persistant** = le LLM **compile une fois** le savoir dans des markdown interliés puis le **maintient** à jour à chaque nouvelle source. Le wiki devient un **artefact compoundant** — cross-refs, contradictions flaguées, synthèse évolutive déjà prêtes *avant* la question. Cf. [[concepts/persistent-wiki-vs-rag]].

### Architecture en 3 couches

1. **Raw** — sources immuables (articles, papers, images, data). Le LLM lit, n'écrit jamais.
2. **Wiki** — markdown possédé par le LLM seul (sources, entities, concepts, syntheses, queries).
3. **Schéma** — fichier config (`CLAUDE.md`/`AGENTS.md`) qui transforme le LLM de chatbot générique en mainteneur discipliné. Co-évolue avec l'utilisateur au fil des sessions.

### Les 3 opérations

- **Ingest** — touche 10-15 pages en un passage. Détail en [[concepts/ingest-workflow]].
- **Query** — réponse avec citations ; les bonnes réponses sont refilées comme nouvelles pages → les explorations compoundent. Détail en [[concepts/query-synthesis]].
- **Lint** — health check (contradictions, claims stale, orphelins, gaps, cross-refs manquantes).

### Tooling

- **[[entities/obsidian]]** comme IDE — wikilinks, graph view, plugins (Dataview, Marp, Web Clipper). Voir l'analogie complète dans [[concepts/obsidian-as-ide]].
- `index.md` comme catalogue content-oriented, remplace RAG jusqu'à ~100 sources.
- `log.md` comme journal chronologique append-only, parseable `grep "^## \["`.
- CLI tools **optionnels** — émergent avec le besoin, pas pré-construits. Cf. [[concepts/cli-tools-optional]].

### Pourquoi ça marche

Le vrai coût d'un wiki, c'est le **bookkeeping** (cross-refs, consistance, updates), pas la lecture. Les humains abandonnent parce que la maintenance scale plus vite que la valeur. Les LLM ne s'ennuient pas et touchent 15 fichiers en un passage. Le pattern est l'héritier du Memex de [[entities/vannevar-bush]] (1945) — Bush avait la vision, lui manquait "qui maintient ?".

## Extraits verbatim (< 15 mots)

> "the LLM is rediscovering knowledge from scratch on every question"

> "The knowledge is compiled once and then kept current, not re-derived on every query"

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase"

> "Humans abandon wikis because the maintenance burden grows faster than the value"

> "The part he couldn't solve was who does the maintenance. The LLM handles that"

## Limites

- **Document volontairement abstrait**. Pas de schéma imposé, pas de convention nommée, pas de script d'ingest fourni. Tout est à instancier par le lecteur.
- **Zéro chiffre empirique**. Pas d'étude, pas de benchmark RAG vs wiki, pas de mesure de productivité. Claims par analogie et expérience rapportée.
- **Orienté usage personnel / petit groupe**. Rien sur multi-utilisateurs, gouvernance éditoriale, scale > quelques centaines de pages, fiabilité à 1000+ sources.
- **NotebookLM cité sans être benchmarké**. C'est une étiquette de catégorie ("produit RAG"), pas une évaluation.
- **Pas de comparaison chiffrée** avec des patterns alternatifs (PARA, Zettelkasten, Logseq workflows, etc.).

## Implications SEO

**Angle retenu (4) — Wiki compilé ↔ Grounding Score**.

Hypothèse structurelle — désormais **nourrie** par [[sources/2026-04-11-seo-ia-tim]] qui fournit le mécanisme architectural ([[concepts/surprise-metric]], [[concepts/weight-decay]], neural memory).

### La connexion proposée

Chaque **page entity** d'un wiki persistant tel que décrit par Karpathy agrège, au fil des ingests, toutes les claims connues sur un objet nommé (algo, outil, acteur, concurrent). Structurellement, cette page est une **synthèse vectorisable** — elle condense ce que la KB "sait" de l'entité dans un bloc de texte cohérent, cross-référencé, et continuellement mis à jour.

Cette structure rappelle le **Grounding Score** défini dans la §4.2 d'`AGENTS.md` : similarité cosinus entre le vecteur d'intention d'une requête et le vecteur d'une page. Si on retourne la question — *comment maximise-t-on le grounding score d'une page ?* — une réponse candidate passe par la discipline du wiki persistant : une page qui agrège, consolide et met à jour tous les signaux sur son sujet est **par construction** mieux "grounded" qu'une page statique rédigée une seule fois.

### Ce que l'hypothèse impliquerait si elle tenait

- **Pour le GEO** : si les moteurs génératifs (SGE, ChatGPT Search, Perplexity) fonctionnent sur une logique proche (retrieve + rerank vectoriel), alors produire des pages qui **ressemblent à des pages entity de wiki maintenu** — claims atomiques, cross-refs, updates datés, synthèse consolidée — serait un signal d'optimisation direct, pas une astuce cosmétique.
- **Pour le skill `seo-entites-vectorielles`** : le pattern Karpathy fournirait une **méthodologie de construction** des pages optimisées pour ce skill. Pas une checklist, une discipline de maintenance.
- **Pour le skill `seo-cluster-aeo`** : un cluster AEO est littéralement un sous-ensemble interconnecté d'entities et de concepts du wiki. La structure du wiki persistant devient la structure du cluster.

### Limites explicites de cette hypothèse

- **Rien dans la source Karpathy ne mentionne le Grounding Score.** La connexion est une inférence structurelle faite depuis cette KB, pas un claim de l'auteur.
- **[[concepts/grounding-score]] existe désormais** — créée lors de l'ingest de [[sources/2026-04-11-seo-ia-tim]]. Connectée à [[concepts/surprise-metric]] et [[entities/titans]]. L'hypothèse est devenue testable.
- **Aucun benchmark** ne valide que des "pages entity style wiki" performent mieux en ranking SGE que des pages statiques classiques. C'est une **hypothèse à tester**, pas une doctrine à appliquer. Appliquer aveuglément violerait la §2 d'`AGENTS.md` (preuves atomiques, données > opinion).

### À filer comme query dédiée (session ultérieure)

`wiki/queries/wiki-pattern-vs-grounding-score.md` — matériau disponible via [[sources/2026-04-11-seo-ia-tim]]. Reste à filer comme query dédiée :

1. Un paper sur les architectures de retrieval vectoriel utilisées par SGE / AI Overviews
2. La doc Google officielle sur le neural matching ou le passage ranking
3. Un test terrain : publier une page "style wiki entity" sur un sujet SEO volatile, mesurer son comportement dans SGE vs une page statique de contrôle

### Angles alternatifs non retenus pour cette source

- *Angle 1 (meta fondationnel)* : déjà implicite — le fait même que cette KB existe et que §2 reprend la discipline de sourcing l'acte.
- *Angle 2 (RAG vs wiki dans les génératifs)* : plus directement lié à GEO, mais demande des sources sur les architectures SGE / Perplexity pour être nourri. Reporté.
- *Angle 3 (compoundage appliqué aux exports GSC)* : opérationnel direct, mais demande un export GSC réel ingéré en `raw/data/` pour être instancié. Reporté.
- *Angle 5 (convergence doctrinale)* : déjà absorbé par la §2 d'`AGENTS.md`. Pas de page dédiée nécessaire.

## Pages liées

**Entities** : [[entities/karpathy]] · [[entities/obsidian]] · [[entities/vannevar-bush]] · [[entities/notebooklm]]

**Concepts** : [[concepts/persistent-wiki-vs-rag]] · [[concepts/ingest-workflow]] · [[concepts/query-synthesis]] · [[concepts/cli-tools-optional]] · [[concepts/obsidian-as-ide]]
