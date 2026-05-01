---
name: kb-semantic-search
description: |
  Recherche sémantique pseudo-vectorielle sur n'importe quelle base de connaissances markdown (vault Obsidian, dossier de notes structurées, repo de doc). Pipeline en 5 phases : expansion de la requête (mots-clés inférés par Claude) → grep multi-passes → chunk read ciblé → suivi 1-hop des wikilinks → synthèse structurée avec citations. Comble l'absence de vector search natif tant que la KB reste sous ~500 fichiers.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "cherche dans ma KB", "qu'est-ce qu'on a sur", "qu'est-ce que je sais sur", "ma base dit quoi sur", "trouve les notes qui parlent de", "concepts liés à", "synthétise ce qu'on a sur", "recherche sémantique sur", "donne-moi tout ce qu'on a sur [sujet]", "que dit ma doctrine sur", "fais une recherche conceptuelle sur".

  Ce skill substitue la vraie vector search (pas disponible nativement Claude Code). Pour des KB > 500 fichiers, passer à un MCP vector search (ChromaDB, Qdrant, OpenAI embeddings). Pour la navigation visuelle Obsidian, le plugin Smart Connections est complémentaire mais non accessible depuis Claude Code.

  Compatible avec n'importe quelle structure markdown : pattern raw/+wiki/ (Karpathy), structure plate, sous-dossiers thématiques, PARA, Zettelkasten. Le skill s'adapte à l'arborescence détectée.
---

# kb-semantic-search — Recherche sémantique pseudo-vectorielle sur une KB markdown

## Mission

Répondre à une question conceptuelle sur une base de connaissances markdown en mobilisant **toutes** les notes pertinentes, pas seulement celles dont le nom matche littéralement la question. Synthèse finale citée par wikilinks, gaps identifiés, suggestions d'approfondissement.

Ce skill est invoqué quand une recherche `Grep` simple ne suffit pas — typiquement quand la question est conceptuelle (*"qu'est-ce qu'on sait sur la mémoire LLM"*) plutôt que littérale (*"trouve le mot RAID"*).

## Pré-requis structurel

Le skill fonctionne sur toute KB markdown qui respecte au minimum :
- Fichiers `.md` organisés dans des dossiers (plat ou hiérarchique)
- Wikilinks `[[...]]` inter-fichiers (idéalement, pour la Phase 4)

Patterns d'arborescence supportés (le skill s'adapte automatiquement) :
- **raw/ + wiki/** (pattern Karpathy/LLM Wiki)
- **Structure plate** (tous les .md à la racine)
- **Sous-dossiers thématiques** (concepts/, sources/, daily-notes/, etc.)
- **Pattern PARA** (Projects/Areas/Resources/Archives)
- **Pattern Zettelkasten** (notes atomiques numérotées)

Avant de lancer le pipeline, l'agent identifie l'arborescence (`ls` ou `Glob`) pour adapter les passes de Phase 2.

## Pipeline en 5 phases

```
QUESTION
  │
  ├─► Phase 1 — Expansion de la requête (Claude infère 8-12 mots-clés probables)
  │
  ├─► Phase 2 — Grep multi-passes sur la KB (priorisé par dossier)
  │
  ├─► Phase 3 — Chunk read ciblé sur les candidats (top 5-10 fichiers)
  │
  ├─► Phase 4 — Suivi 1-hop des wikilinks (découvre les nœuds connexes)
  │
  ├─► Phase 5 — Synthèse structurée (réponse + sources + gaps + queries dérivées)
  │
RÉPONSE CITÉE
```

L'agent ne saute aucune phase. L'ordre est strict.

## Phase 1 — Expansion de la requête

Avant tout grep, Claude infère la palette sémantique de la question :

- **8-12 mots-clés probables** : la question elle-même + synonymes + hyperonymes + hyponymes + formulations alternatives + termes techniques associés
- **3-5 entités nommées attendues** : noms propres (personnes, papers, outils, organisations) qui pourraient être mobilisés
- **3-5 concepts probables** : noms de notes/concepts existants dans la KB qui pourraient cadrer la question
- **Hiérarchisation P1 / P2 / P3** :
  - **P1** = mots-clés qui DOIVENT matcher (cœur de la question)
  - **P2** = mots-clés probables (élargissent le contexte)
  - **P3** = mots-clés tangentiels (à explorer si peu de résultats)

Output Phase 1 : tableau structuré P1/P2/P3 avec mots-clés + entités + concepts attendus.

## Phase 2 — Grep multi-passes

L'ordre des passes va du plus précis (notes atomiques conceptuelles) au plus large (sources brutes). L'agent adapte selon l'arborescence détectée.

**Pour une KB structurée Karpathy-style (raw/ + wiki/)** :
1. `wiki/concepts/` — grep P1 sur tous les `.md`
2. `wiki/entities/` — grep entités attendues + P1+P2
3. `wiki/syntheses/` — toutes les syntheses lues rapidement
4. `wiki/sources/` — grep entités attendues + P1+P2 (top 10 candidats)
5. `wiki/briefs/`, `wiki/queries/`, `wiki/revues-presse/` — vérifier qu'aucun output déjà produit ne couvre la question
6. `raw/` — optionnel, si peu de résultats, signaler les sources brutes pertinentes non encore ingérées

**Pour une structure plate ou autre pattern** :
- Identifier les dossiers les plus probablement pertinents par leur nom
- Grep en cercles concentriques (le plus probable d'abord)

Output Phase 2 : liste hiérarchisée de fichiers candidats avec score qualitatif.

## Phase 3 — Chunk read ciblé

Pour chaque fichier candidat (top 5-10 selon score) :

- Si fichier court (<200 lignes) : lire entièrement avec `Read`
- Si fichier long (>200 lignes) : utiliser `Grep` avec `output_mode: content` et `-C 5` pour extraire les passages pertinents
- Pour les PDFs : lire avec `Read` + `pages: "X-Y"` sur les pages identifiées

Ne JAMAIS lire un fichier en entier sans nécessité. Économiser les tokens.

Output Phase 3 : extraits cités de chaque source pertinente, avec numéro de ligne et wikilink vers le fichier.

## Phase 4 — Suivi des wikilinks (1-hop)

Pour chaque chunk lu en Phase 3, identifier les `[[wikilinks]]` mentionnés. Pour chaque wikilink **non encore exploré** :

- Lire la page cible (ou ses passages pertinents)
- Limiter à 1 hop (ne pas suivre les wikilinks des wikilinks — explosion combinatoire)
- Filtrer : ne suivre que les wikilinks **sémantiquement liés à la question** (l'agent juge)

Si la KB n'utilise pas de wikilinks, sauter cette phase.

Output Phase 4 : extraits supplémentaires des nœuds connexes, citations wikilinks.

## Phase 5 — Synthèse structurée

Format de sortie obligatoire :

### Réponse synthétique (200-300 mots)

Réponse directe à la question, en prose continue, avec citations `[[...]]` sur chaque claim factuel. Pattern Tension → Résolution → Preuve sur chaque idée. Anti-patterns IA bannis : pas de "crucial", "pivotal", pas de règle de 3 systématique, pas de bullet décoratif dans le corps, pas de méta-intro.

### Sources mobilisées

```
[[concepts/X]] — résumé en 1 ligne de ce qu'apporte cette note à la réponse
[[sources/Y]] — résumé en 1 ligne
[[entities/Z]] — résumé en 1 ligne
```

Adapter le préfixe selon l'arborescence de la KB.

### Gaps identifiés

```
- [Gap 1] — pourquoi c'est un gap, source potentielle suggérée pour combler
- [Gap 2] — ...
```

### Queries dérivées

```
- "Comment X impacte Y selon ma doctrine ?"
- "Quel est le finding empirique le plus solide sur Z ?"
```

## Limites factuelles

- **Pas une vraie vector search** — l'expansion de mots-clés en Phase 1 est faite par inférence Claude, pas par cosinus sur embeddings. Marche bien jusqu'à ~500 fichiers.
- **Dépend de la qualité des wikilinks** — si la KB a peu de cross-références, la Phase 4 ne découvre rien.
- **Pas de scoring numérique précis** — le ranking des candidats Phase 2 est qualitatif.
- **Tokens consommés non triviaux** — privilégier ce skill pour les questions à fort enjeu.
- **Pas de cache** — chaque invocation refait l'expansion + le grep + la lecture.

## Règles d'or

1. **Toujours citer wikilinks** — chaque claim de la synthèse a sa source `[[...]]`
2. **Toujours flagger les gaps** — la KB n'est jamais exhaustive
3. **Jamais inventer un finding** — si la KB ne couvre pas, le dire
4. **Jamais lire un fichier entier sans nécessité**
5. **Prose continue dans la synthèse** — pas de bullet décoratif, pas de bold excessif, pas de règle de 3
6. **Output sauvegardable** — la synthèse finale doit être structurée pour pouvoir devenir une note permanente

## Sauvegarde optionnelle

Si l'utilisateur juge la réponse réutilisable, créer la note dans le dossier `queries/` (ou équivalent selon l'arborescence) avec frontmatter standard et logger l'opération dans le journal de la KB si présent.
