# AGENTS.md — Knowledge Base SEO/IA/GEO de Timothée Boussardon

> Configuration pour les agents LLM (Claude Code, etc.) qui maintiennent ce wiki.
> Tu lis ce fichier **au démarrage de chaque session**, puis tu l'appliques strictement.
>
> **Cette KB n'est pas générique**. Elle est pensée pour le SEO, l'IA générative, le GEO, l'AEO, et les processus propriétaires de Tim. Respecter ces processus est **obligatoire**.

---

## 1. Mission

Construire une base de connaissances **persistante, compoundante et interconnectée** qui sert Tim dans son travail de consultant SEO/IA/GEO :

- Veille technique quotidienne (algos Google, papers IA, outils SEO)
- Analyse de données GSC, Ahrefs, Semrush
- Production de briefs, clusters, articles, revues de presse
- Capitalisation des retours clients et des intuitions terrain
- Doctrine propriétaire sur le SEO post-SGE / Agentic Search

---

## 2. Doctrine SEO propriétaire de Tim

**À respecter strictement dans TOUT contenu produit par l'agent** (wiki, briefs, synthèses, queries, posts) :

- **Factuel avant tout** — données chiffrées, sources vérifiables, benchmarks quantitatifs
- **Zéro bullshit** — pas de buzzwords creux, pas de "game-changer", pas de "next-level"
- **Angle original** — toujours chercher l'inversion expertise, l'insight que les concurrents ratent
- **Données > opinion** — toute affirmation technique doit pointer vers une source (étude, GSC, test, doc Google)
- **Preuves atomiques** — chaque claim = un fact source séparé et traçable
- **Phrases courtes** — pas de langue de bois, prose directe
- **Pas de condescendance** — le lecteur est un pair, pas un débutant
- **Ton technique mais accessible** — expliquer le fond, pas masquer par le jargon

---

## 3. Architecture — 3 couches

```
seo-kb/
├── raw/                   ← sources immuables (lecture seule pour l'agent)
│   ├── articles/          ← clippings web (Obsidian Web Clipper)
│   ├── auteurs/           ← posts verbatim d'auteurs externes (LinkedIn, X, newsletters) — règle d'attribution stricte (§13)
│   ├── papers/            ← papers académiques (PDFs)
│   ├── data/              ← exports GSC, Ahrefs, Semrush, Screaming Frog
│   ├── clients/           ← notes client, briefs reçus, audits
│   ├── notes/             ← notes brutes, voice memos transcrits
│   └── assets/            ← images téléchargées
│
├── wiki/                  ← domaine de l'agent (écriture exclusive)
│   ├── 000-home.md        ← carte d'entrée curée (MOC racine, lecture humaine)
│   ├── index.md           ← catalogue de toutes les pages
│   ├── log.md             ← append-only chronologique
│   ├── hypotheses.md      ← registre des claims non validés (boucle validation)
│   ├── contradictions.md  ← registre de la dette doctrinale (boucle validation)
│   ├── ingest-backlog.md  ← raw non digéré, trié P1/P2/P3 (boucle capture)
│   ├── moc/               ← Maps of Content thématiques (navigation humaine)
│   ├── preuves/           ← fiches contenu publié ↔ doctrine (boucle apprentissage)
│   ├── decisions/         ← ADR, décisions structurantes du système
│   ├── revue-hebdo/       ← éditions du rituel de décision + résurgences
│   ├── sources/           ← résumé structuré par source ingérée
│   ├── entities/          ← algos, outils, acteurs, concurrents, Google, Quality Raters
│   ├── concepts/          ← AEO, GEO, pSEO, Grounding Score, RRF, E-E-A-T, Agentic Search…
│   ├── syntheses/         ← synthèses multi-sources, thèses évolutives
│   ├── queries/           ← outputs de questions filées comme pages permanentes
│   ├── briefs/            ← briefs de contenu (skill: seo-brief-contenu)
│   ├── clusters/          ← cocons sémantiques AEO (skill: seo-cluster-aeo)
│   ├── quick-wins/        ← opportunités GSC (skill: seo-quick-win)
│   ├── cannibalisation/   ← audits de cannibalisation (skill: seo-cannibalisation)
│   ├── maillage/          ← analyses de liens internes (skill: maillage-interne-gsc)
│   ├── posts-linkedin/    ← posts LinkedIn (skill: linkedin-post-tim)
│   └── revues-presse/     ← éditions Algorithme (skill: revue-presse-iteration)
│
└── README.md              ← guide humain
```

**Règle d'or** : `raw/` est **immuable**. L'agent lit, ne modifie jamais. Tout le reste est dans `wiki/`.

---

## 4. Taxonomie SEO — Types de pages

### 4.1 Entities (`wiki/entities/`)

Une entité = un objet nommé identifiable. Sous-catégories :

- **Algos Google** : `bert`, `rankbrain`, `sge`, `mum`, `neural-matching`, `rrf`
- **Outils SEO** : `ahrefs`, `semrush`, `screaming-frog`, `gsc`, `qmd`, `obsidian`
- **Acteurs/personnes** : `karpathy`, `john-mueller`, `danny-sullivan`, `fabrice-canel`
- **Concurrents** : `semji`, `contentking`, `clearscope`
- **Quality Raters** : référence au Search Quality Rater Guidelines
- **Concepts-marque** : `google`, `bing`, `chatgpt-search`, `perplexity`, `notebooklm`, `google-deepmind`
- **Architectures IA** : `titans`, `miras`, `mamba-2`, `transformer`, `gpt-4` — architectures / modèles de recherche IA cités dans les analyses SEO/GEO (distinct des Algos Google qui sont en production dans la recherche)

Chaque entité a au moins : description, dernière update connue, sources citées, 2+ liens sortants.

### 4.2 Concepts (`wiki/concepts/`)

Un concept = une idée, méthode ou mécanique. Exemples :

- **AEO** (Answer Engine Optimization)
- **GEO** (Generative Engine Optimization)
- **pSEO** (programmatic SEO)
- **Grounding Score** (similarité cosinus vecteur intention ↔ page)
- **Reciprocal Rank Fusion (RRF)**
- **Passage Ranking**
- **E-E-A-T**
- **Fully Meets** (Quality Raters)
- **Agentic Search**
- **Intentions Know-Simple / Know / Do**
- **Inversion expertise**
- **Surprise Gap**

### 4.3 Sources (`wiki/sources/`)

Une page par source ingérée. Sous-types dans le frontmatter (`source_type`) :

- `article` — article de blog / news
- `paper` — paper académique (arxiv, ACL…)
- `doc-google` — documentation officielle Google / Bing
- `gsc-export` — export de données GSC
- `client-note` — note client, brief reçu, audit
- `transcript` — podcast, conférence, vidéo
- `test-terrain` — test SEO perso / expérimentation
- `doctrine` — note doctrinale / analyse propriétaire de Tim (thèse perso, cross-référence de papers, hypothèses SEO/IA non encore validées)

---

## 5. Conventions de fichiers

### 5.1 Frontmatter YAML obligatoire

Le frontmatter est **obligatoire pour `wiki/` ET `raw/`**. Les scripts d'index (concepts.json + vector store) s'appuient dessus pour le filtrage déterministe (`./kb search "..." --type concept --tag aeo`). Sans frontmatter, un fichier reste indexé en recherche vectorielle pure mais devient invisible aux filtres.

Pour `raw/`, un schéma minimal suffit : `type: source` + `source_type` + `created` + `title`. Le backfill auto est dispo via `./kb backfill --apply` (génère le frontmatter manquant à partir du nom de fichier, du sous-dossier et du premier H1).

Chaque page `wiki/` (et `raw/`) commence par :

```yaml
---
type: source | entity | concept | synthesis | query | brief | cluster | quick-win | doctrine | revue-presse | pseo-strategy | audit | register | moc | decision | proof | proposition | methode | post
source_type: article | paper | doc-google | gsc-export | client-note | transcript | test-terrain | doctrine  # pour type=source uniquement
# proposition : propale/template commercial (propositions/) ; methode : fiche méthode (methodes/) ; post : post LinkedIn (posts-linkedin/)
# register : pages-index vivantes (hypotheses, contradictions, ingest-backlog, decisions/index, revue-hebdo)
# moc : carte d'entrée / Map of Content (000-home, moc/*)
# decision : ADR (decisions/NNNN-*)
# proof : fiche preuve (preuves/*)
title: Titre lisible
aliases: [alias1, alias2]
tags: [seo, ia, aeo, geo, pseo, gsc, algo-google, quality-raters, ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: N              # nombre de sources qui ont contribué
confidence: high | medium | low
status: draft | stable | stale
---
```

### 5.2 Nommage

- `kebab-case` strict : `grounding-score.md`, `seo-post-sge.md`
- Pas d'accents, pas d'espaces, pas de majuscules
- Un concept/entité/source = un fichier

### 5.3 Liens internes — Wikilinks Obsidian

- **Toujours `[[nom-de-page]]`** — jamais de markdown `[text](./path.md)`
- Chaque page = minimum **2 liens sortants**
- Citations inline : `Le RRF améliore X% [[sources/2026-google-rrf-paper]]`

### 5.4 Citations et sourcing (DOCTRINE)

- **Toute donnée chiffrée a une source** : `[[sources/...]]`
- **Pas de source = pas d'affirmation**
- Quand une source est vague, marquer `confidence: low` + noter l'incertitude
- Jamais d'invention de chiffres, benchmarks ou pourcentages

---

## 6. Workflows

### 6.1 Ingest — Ajouter une source

**Déclencheur** : `"ingère raw/articles/foo.md"` ou équivalent.

**Étapes** (dans l'ordre, sans raccourcis) :

1. **Lire** le fichier en entier
2. **Détecter** `source_type` selon le contexte (article, paper, gsc-export, etc.)
3. **Discuter** : résumer en 5 bullets les takeaways à Tim, et demander : "angle SEO à creuser ?"
4. **Créer** `wiki/sources/YYYY-MM-DD-slug.md` :
   - Frontmatter avec `source_type`
   - Résumé structuré (contexte, méthode, chiffres clés, limites, implications SEO)
   - Extraits verbatim marquants (< 15 mots par citation directe, copyright)
5. **Entities/Concepts** : pour chaque entité ou concept mentionné :
   - Si la page existe → ajouter l'info, flaguer contradictions, `sources: N+1`, `updated:`
   - Si pas encore → créer avec frontmatter + 2 backlinks + placer dans la bonne sous-catégorie taxonomique
6. **Update** `wiki/index.md` avec les nouveaux liens
7. **Append** dans `wiki/log.md` :
   ```
   ## [YYYY-MM-DD] ingest | Titre de la source
   - source_type: article
   - source: [[sources/YYYY-MM-DD-slug]]
   - entities touchées: N
   - concepts touchés: N
   - pages créées: N / mises à jour: N
   - contradictions: Y/N
   - angle SEO identifié: court résumé
   ```
8. **Report** à Tim : résumé inline de ce qui a été fait.

**Règle** : un source à la fois par défaut. Pas de batch sans demande explicite.

### 6.2 Query — Poser une question

**Déclencheur** : Tim pose une question substantielle au wiki.

**Étapes** :

1. **Lire `wiki/index.md`** d'abord pour cartographier les pages pertinentes
2. **Drill** dans 3-8 pages les plus relevantes
3. **Synthétiser** avec citations `[[...]]` obligatoires sur chaque claim
4. **Détecter si un skill SEO doit être déclenché** (voir section 7)
5. **Proposer** de filer la réponse dans `wiki/queries/YYYY-MM-DD-slug.md` si valeur réutilisable
6. **Log** :
   ```
   ## [YYYY-MM-DD] query | Question en 10 mots
   - output: [[queries/YYYY-MM-DD-slug]]
   - skill déclenché: seo-cluster-aeo (ou none)
   ```

### 6.3 Lint SEO — Health check

**Déclencheur** : `"fais un lint"` ou tâche périodique.

**Vérifications spécifiques SEO** :

- **Contradictions techniques** : deux pages qui disent l'inverse sur un algo ou un outil
- **Claims sans données** : affirmations vagues sans `[[sources/...]]`
- **Données stale** : sources > 12 mois sur sujet SEO volatil → `status: stale`
- **Entities orphelines** : concept cité sans page `[[entities/...]]`
- **Concepts mal catégorisés** : ex. un cluster qui devrait être dans `clusters/` mais est dans `queries/`
- **Frontmatter invalide** : `source_type` manquant pour une `source`
- **Doctrine violée** : ton buzzword, absence de chiffres, claims non sourcés

**Output** : `wiki/queries/lint-YYYY-MM-DD.md` + résumé inline + propositions d'actions.

---

## 7. Hooks vers les 13 skills SEO propriétaires

**Règle impérative** : quand une requête matche un trigger, **activer le skill correspondant** et **filer l'output dans la bonne sous-catégorie du wiki**. Ne jamais répondre en chat volatile.

| Skill | Triggers | Output file |
|---|---|---|
| **seo-brief-contenu** | "brief", "plan de page", "structure Hn", "rédiger un article sur" | `wiki/briefs/YYYY-MM-DD-slug.md` |
| **seo-cluster-aeo** | "cluster", "cocon", "AEO", "pages satellites", "topical authority" | `wiki/clusters/YYYY-MM-DD-slug.md` |
| **seo-programmatique-pseo** | "pSEO", "programmatique", "template + variable", "pages scalables" | `wiki/queries/pseo-YYYY-MM-DD-slug.md` |
| **seo-product-led** | "Product-Led SEO", "calculateur", "outil gratuit", "Fully Meets" | `wiki/queries/product-led-YYYY-MM-DD-slug.md` |
| **seo-entites-vectorielles** | "entités sémantiques", "Grounding Score", "vecteur", "intention" | `wiki/queries/entites-YYYY-MM-DD-slug.md` |
| **seo-peurs-objections** | "objections", "peurs prospects", "pain points", "verbatims" | `wiki/queries/peurs-YYYY-MM-DD-slug.md` |
| **seo-workflow-article** | "écrire un article complet", "workflow article" | `wiki/queries/article-YYYY-MM-DD-slug.md` |
| **seo-cannibalisation** | "cannibalisation", "deux pages sur le même mot-clé", "keyword cannibalism" | `wiki/cannibalisation/YYYY-MM-DD-slug.md` |
| **seo-quick-win** | "quick win", "gains rapides", "pages position 3-12", "CTR faible" | `wiki/quick-wins/YYYY-MM-DD-slug.md` |
| **maillage-interne-gsc** | "maillage", "liens internes", "cocon SEO", "GSC + SEO" | `wiki/maillage/YYYY-MM-DD-slug.md` |
| **linkedin-post-tim** | "post LinkedIn", "contenu LinkedIn", "idée de post" | `wiki/posts-linkedin/YYYY-MM-DD-slug.md` |
| **revue-presse-iteration** | "revue de presse", "newsletter Algorithme", "édition du jour" | `wiki/revues-presse/YYYY-MM-DD-slug.md` |
| **kw-research-workflow** | "recherche mots-clés", "workflow keyword research", "j'ai un nouveau client à analyser", "fais-moi le workflow complet", upload Keyword Planner / GSC + verbatims | `wiki/queries/kw-research-YYYY-MM-DD-slug.md` (+ Google Sheet `KW_Research_[Client]_[Date]`) |

### 7bis. Skills système (boucles + rituel) — cf. §14

| Skill | Triggers | Cadence | Output |
|---|---|---|---|
| **ingest-backlog-sweep** | "sweep backlog", "quoi ingérer", "raw non traité" | lundi 08:00 | `wiki/ingest-backlog.md` |
| **hypotheses-validation** | "validation hypothèses", "revue mensuelle doctrine" | 1er du mois 08:30 | `wiki/hypotheses.md` + `wiki/contradictions.md` |
| **preuves-feedback** | "fiche preuve", "qu'est-ce que cet article a donné", data perf sur URL publiée | à la demande | `wiki/preuves/YYYY-MM-DD-slug.md` |
| **gsc-watcher** | "traite la GSC", "j'ai déposé un export GSC" | 1er du mois 07:00 | `wiki/preuves/` (depuis `raw/data/exports-gsc/`) |
| **revue-hebdo** | "revue hebdo", "on fait le point", "qu'est-ce qu'on décide" | vendredi 17:30 | `wiki/revue-hebdo/YYYY-Www.md` |
| **resurgence-espacee** | "résurgence", "concept oublié" | mercredi 09:00 | `wiki/revue-hebdo/resurgence-YYYY-MM-DD.md` |

**Après chaque déclenchement de skill** :
1. Appliquer le skill avec toute son expertise
2. Sauver l'output dans le bon dossier du wiki (pas dans le chat)
3. Appeler les entities/concepts pertinents du wiki pour enrichir
4. Update `wiki/index.md` + `wiki/log.md`

---

## 7ter. Infra d'index local : `./kb`

Le vault expose un CLI `./kb` à la racine qui matérialise le graphe et la sémantique du vault dans deux structures persistées :

- **`.claude/index/concepts.json`** : index inversé des `wiki/concepts/` + `wiki/entities/`. Pour chaque nœud : `title`, `aliases`, `tags`, `outlinks` (wikilinks sortants), `backrefs` (chemins de tous les fichiers du vault qui pointent vers ce nœud). C'est le graphe atomique exploitable en lecture O(1).
- **`.claude/vector-store/`** : collection ChromaDB persistée, embeddings sentence-transformers (modèle `paraphrase-multilingual-mpnet-base-v2`, multilingue FR-friendly, local, gratuit). Un document = un chunk H2 d'un fichier markdown. Les métadonnées du frontmatter (type, source_type, tags, status, confidence, created) sont stockées dans chaque chunk pour permettre le filtrage déterministe avant la recherche cosinus.

### Commandes

```bash
./kb rebuild              # audit frontmatter + concepts.json + index vectoriel incrémental
./kb rebuild --full       # idem, mais rebuild from scratch de l'index vectoriel
./kb search "ma requête"  # recherche sémantique top-5
./kb search "RRF" --type concept --tag aeo --k 8
./kb audit-frontmatter    # liste les fichiers raw/ sans frontmatter
./kb backfill --apply     # backfill auto des frontmatters manquants
./kb concepts             # rebuild concepts.json uniquement
```

### Quand rebuild ?

Manuel, à déclencher après une session d'ingestion ou un batch d'édition (`./kb rebuild`). Pas de hook git ni de file watcher : le rebuild est rapide en incrémental (skip les fichiers dont `mtime+size` n'a pas changé depuis le dernier index).

### Lifecycle des chunks

L'index incrémental supprime tous les anciens chunks d'un fichier modifié puis ré-upsert les nouveaux. Pour repartir de zéro : `./kb rebuild --full`.

### Quand utiliser `./kb search` vs le skill `kb-semantic-search` ?

- **`./kb search`** : lookup rapide, déterministe, scoring numérique. Idéal pour "trouve-moi les notes qui parlent de X".
- **Skill `kb-semantic-search`** : pipeline complet avec synthèse citée, gaps identifiés, queries dérivées. Le skill court-circuite maintenant ses Phases 1-3 via `./kb search` (Phase 0) si l'index est dispo, puis enchaîne sur Phase 4 (wikilinks 1-hop) + Phase 5 (synthèse).

---

## 8. Index.md — Structure attendue

```markdown
# Index du wiki SEO/IA/GEO

## Sources (N)
### Articles (N)
- [[sources/2026-04-11-karpathy-llm-wiki]] — Pattern LLM Wiki (article)

### Papers (N)
### GSC Exports (N)
### Client Notes (N)
### Transcripts (N)

## Entities (N)
### Algos Google (N)
- [[entities/sge]] — Search Generative Experience (3 sources)

### Outils SEO (N)
- [[entities/gsc]] — Google Search Console (5 sources)

### Acteurs (N)
### Concurrents (N)

## Concepts (N)
### AEO/GEO (N)
- [[concepts/grounding-score]] — Similarité cosinus intention↔page (4 sources)

### SEO technique (N)
### Stratégie contenu (N)

## Syntheses (N)
## Queries (N)

## Outputs skills
### Briefs (N)
### Clusters (N)
### Quick Wins (N)
### Cannibalisation (N)
### Maillage (N)
### Posts LinkedIn (N)
### Revues de presse (N)
```

---

## 9. Log.md — Format append-only

Format strict : `## [YYYY-MM-DD] action | titre`

Parseable via `grep "^## \[" wiki/log.md | tail -10`

```markdown
# Log

## [2026-04-11] bootstrap | Init du vault SEO KB
- AGENTS.md v2.0 (SEO-first, 12 skills hookés)
- doctrine propriétaire de Tim appliquée
- taxonomie SEO définie (algos, outils, concepts AEO/GEO)
- prochaine étape : ingest karpathy-llm-wiki.md
```

---

## 10. Règles strictes (résumé)

1. **Jamais toucher `raw/`** — lecture seule
2. **Wikilinks `[[...]]` partout** — pas de markdown `[...](...)`
3. **Tous les chiffres ont une source** — `[[sources/...]]` obligatoire
4. **Pas d'invention** — pas de source = pas d'affirmation
5. **Doctrine de Tim appliquée partout** — factuel, zéro bullshit, angle original
6. **Skills hookés automatiquement** — ne jamais répondre "à la main" si un skill matche
7. **Outputs filés dans le wiki** — jamais en chat volatile
8. **`source_type` obligatoire** pour type=source
9. **Frontmatter YAML valide** sur chaque page
10. **Log entry strict** : `## [YYYY-MM-DD] action | titre`
11. **[[concepts/anti-ai-writing]] systématique pour toute rédaction** — cf. §11 ci-dessous
12. **Skill `seo-workflow-article` obligatoire pour rédiger ou réécrire un article** — cf. §12 ci-dessous
13. **Attribution stricte pour tout contenu issu de `raw/auteurs/`** — cf. §13 ci-dessous

---

## 11. Règle de rédaction — anti-AI-writing obligatoire

À chaque fois que Tim demande une rédaction (newsletter, brief, post LinkedIn, article, email, proposition, titre, intro, réécriture) : **relire [[concepts/anti-ai-writing]] avant de produire ET auto-vérifier après produit**.

### Déclencheurs de la règle

Toute demande contenant un de ces verbes ou formats implique la règle :
- "rédige", "écris", "réécris", "reformule", "propose un titre/hook/intro/passage", "améliore", "draft", "corrige"
- Toute sortie destinée à être publiée (Substack, LinkedIn, email client, blog organikk, doc commerciale)

### Auto-check avant livraison

Avant de livrer un contenu rédigé, vérifier factuellement :

1. **Zéro mot banni** — "crucial", "pivotal", "groundbreaking", "comprehensive", "landscape", "vibrant", "nestled", "renowned", "il est important de noter", "n'oublions pas que", "dans un monde en pleine évolution"
2. **Zéro pattern Wikipedia** — "stands as", "is a testament", "a vital/significant/crucial role", "underscores its importance", "reflects broader", "evolving landscape", "indelible mark"
3. **Zéro participiale décorative** en "-ing" / "-ant" ("highlighting", "ensuring", "en soulignant", "en reflétant")
4. **Pas de règle de 3 systématique** — ni dans le texte, ni dans la structure des titres H2, ni dans les listes
5. **Prose continue dans le corps** — bullet points réservés aux vraies comparaisons structurelles (tableau comparatif, protocole numéroté). Pas de bullets décoratifs qui remplacent la prose.
6. **Pas de bold excessif** en début de ligne ni sur les premiers mots de chaque paragraphe
7. **Pas de méta-intro** ("Dans cet article, nous allons voir...", "Voici ce qu'on va aborder...")
8. **Pas de conclusion-résumé redondante** qui répète ce qui vient d'être dit
9. **Pas d'émojis** dans les titres ou le corps, sauf si Tim demande explicitement
10. **Pas de "visibilité"** — remplacer par "citations IA", "positions", "leads", "conversions" (cf. [[concepts/tabou-visibilite]])

### Workflow obligatoire

1. Avant de rédiger : ouvrir [[concepts/anti-ai-writing]] mentalement (lire les 3 sections : patterns interdits / Wikipedia Signs / règles Tim)
2. Produire en prose continue par défaut
3. Relire sa sortie en cochant les 10 points ci-dessus
4. Flagger explicitement tout point où la règle n'a pas pu être tenue (ex : *"j'ai utilisé une liste à 3 éléments car la source comporte exactement 3 méthodes mesurées"*)

### Cas d'exception documentés

- **Tableau comparatif structurel** (ex : Cowork vs Claude+Obsidian) : bullet/tableau autorisé
- **Protocole numéroté** (ex : 5 étapes d'installation) : liste autorisée si chaque étape est atomique
- **Code / commande shell** : toujours en bloc de code
- **Citation verbatim** : toujours en blockquote `>`
- **Quote auteur** : toujours en blockquote avec attribution

### Articulation avec les autres règles

- Règle 5 (§10) *"doctrine de Tim partout"* = niveau stratégique (angle, ton, sourcing)
- Règle 11 / §11 (nouvelle) = niveau **mécanique d'écriture** (syntaxe, forme, structure)

Les deux sont non-négociables et se cumulent.

---

## 12. Règle article — workflow `seo-workflow-article` obligatoire

À chaque fois que Tim demande de **rédiger un article** ou de **réécrire un article complet** : invoquer obligatoirement le skill `seo-workflow-article` (installé dans `~/.claude/skills/seo-workflow-article/`). Jamais répondre "à la main" sur un article.

### Déclencheurs de la règle

Toute demande contenant l'un de ces verbes ou formats :
- "rédige un article", "écris un article", "produis un article", "draft un article"
- "réécris cet article", "améliore cet article", "passe cet article dans le workflow"
- "article complet", "article de A à Z", "pipeline éditorial", "long-form"
- Toute sortie destinée à devenir un article publié (blog organikk, Medium, LinkedIn long-form > 1500 mots)

### Distinction avec §11

- **§11 (anti-AI-writing)** = règles de **forme** sur toute rédaction (titre, hook, intro, paragraphe, post court, email, brief, doc commerciale)
- **§12 (workflow article)** = règle de **process** sur les articles longs spécifiquement (1500+ mots, structure Hn, publication)

Les deux se cumulent. Un article = §12 (workflow 8 étapes) + §11 (anti-AI-writing à chaque étape).

### Cas d'exception

Pas d'invocation du workflow si :
- Tim demande explicitement *"juste un brouillon rapide, sans le workflow"*
- Format court non-article : titre seul, hook seul, paragraphe d'intro, post LinkedIn court (<500 mots), email
- Réécriture mineure d'un paragraphe existant (correction de style, sans changement de fond)

Dans ces cas, appliquer §11 seule.

### Articulation avec `article-engine-pipeline`

`article-engine-pipeline` (skill séparé) = pipeline complet 5 phases qui invoque `seo-workflow-article` en phase 4. Si Tim demande un article complet "bout en bout" (avec décodage RRF + FAQ stratégique + factcheck), utiliser `article-engine-pipeline`. Si Tim demande juste l'article (sans le RRF en amont ou le factcheck en aval), utiliser `seo-workflow-article` seul.

### Workflow obligatoire

1. Détecter le déclencheur dans la demande de Tim
2. Confirmer mentalement : article ou format court ? Workflow oui/non ?
3. Si workflow oui → invoquer `seo-workflow-article` (ou `article-engine-pipeline` si scope plus large)
4. Suivre les 8 étapes sans en sauter
5. Auto-vérifier §11 à chaque étape de rédaction
6. Livrer

---

## 13. Règle d'attribution — contenu issu de `raw/auteurs/`

`raw/auteurs/` archive des posts verbatim d'auteurs externes (LinkedIn, X, Substack, newsletters, blogs). Voir [[raw/auteurs/README]] pour les conventions de stockage.

**Règle non négociable** : toute citation, paraphrase, reformulation ou réutilisation d'une idée tirée d'un fichier de `raw/auteurs/` doit attribuer explicitement l'auteur, comme on cite une étude.

### Ce qui déclenche la règle

- Reprise verbatim d'une phrase ou d'un paragraphe
- Paraphrase ou reformulation d'une idée
- Reprise d'un cadre conceptuel, d'une métaphore ou d'un chiffre venant de l'auteur
- Usage de la prise de parole comme accroche, contre-argument ou pivot d'analyse

### Format imposé

- **Citation directe** : blockquote markdown + attribution inline avec nom de l'auteur, titre du post (italique), date.
  > "The new buyer on the internet is an agent." — Greg Isenberg, *Notes on the agent economy*, 2026-05-13
- **Paraphrase** : nom de l'auteur en clair dans la phrase + wikilink vers la source `[[auteurs/{auteur}/{slug}]]`.
- **Reprise d'idée** : préciser "selon X" / "X observe que" / "X soutient que" avant l'argument, puis lien.

### Ce qui est interdit

- Faire passer une phrase d'auteur pour une idée de Tim
- Faire passer une phrase d'auteur pour une vérité neutre ou un consensus
- Diluer l'attribution avec "des experts disent que…", "on observe que…", "il est bien connu que…"
- Mélanger une voix d'auteur avec la voix de Tim sans marquer la frontière

### Articulation avec les autres règles

- §10 règle 4 *"pas de source = pas d'affirmation"* — s'applique aussi, l'attribution remplit l'exigence de sourcing
- §11 anti-AI-writing — s'applique sur la rédaction qui entoure la citation
- §12 workflow article — s'applique sur les articles longs ; toute citation d'un auteur `raw/auteurs/` dans un article doit respecter §13 en plus

Cette règle s'applique partout : wiki, briefs, articles, posts LinkedIn, revues de presse, réponses inline en chat.

---

## 14. Les trois boucles fermées + le rituel

Décision fondatrice : [[decisions/0001-fermeture-boucles-second-cerveau]]. Le système capture et compile bien, mais sans ces boucles il accumule sans se reprendre en main.

### Boucle capture → traitement

`raw/` se remplit plus vite qu'il ne se digère. [[ingest-backlog]] rend le retard visible et trié (P1 data terrain > P2 contenu publié non bouclé > P3 reste). Le skill `ingest-backlog-sweep` régénère le registre chaque lundi. **Il cartographie, il n'ingère pas** : l'ingest reste le workflow §6.1, déclenché par Tim, qui décide l'angle. Les skips documentés ne se re-litigent pas.

### Boucle doctrine → validation

Toute la doctrine repose sur des transferts d'architecture non prouvables directement. [[hypotheses]] rassemble les claims "non validé" en programme de recherche, [[contradictions]] consolide la dette. **Règle dure : une hypothèse ne passe `validé`/`invalidé` que via une [[preuves/index|fiche preuve]] adossée à de la data réelle. Jamais sur du ressenti.** Skill `hypotheses-validation`, 1er du mois.

### Boucle sortie → apprentissage

Le contenu publié doit revenir mesuré dans le wiki, sinon "data propriétaire" reste un argument et pas un fait. [[preuves/index]] relie chaque contenu à l'hypothèse qu'il teste, à J+30 et J+90. Deux alimentations, un seul traitement (`gsc-watcher`) : dépôt manuel d'un export dans `raw/data/exports-gsc/`, ou pull API autonome via service account (`gsc-fetch.py`, voir [[preuves/SETUP-GSC]]). Jamais de chiffre inventé (§5.4).

### Le rituel

Mercredi, `resurgence-espacee` remonte un concept stable oublié et prépare un verdict. Vendredi, `revue-hebdo` tranche : promotions `draft`→`stable`, hypothèse à tester, lot d'ingest, contradiction à fermer, archivage, fil rouge. Distinct de la revue de presse quotidienne, du lint d'hygiène et de l'`algorithme-recap-hebdo`. C'est le seul moment de décision : l'agent propose à 95%, Tim arbitre les 5% de jugement irréductible.

### Qui nourrit quoi

Auto (agent, cron, zéro effort) : sweeps, résurgence, maintenance des registres, recap-jour. Agent propose / Tim décide (~15 min/semaine) : revue hebdo, validation mensuelle. Irréductiblement Tim ou pull GSC : la data de preuve. Sans elle, la boucle apprentissage ne tourne pas et les hypothèses restent `ouvert`.

### Navigation humaine

[[index]] est un catalogue (agent, recherche). [[000-home]] + `moc/` sont les portes d'entrée curées quand on veut *penser* dans le vault. Les MOCs pointent vers les hubs et signalent ce qui n'est pas tranché ([[hypotheses]], [[contradictions]]).

---

**Version** : 2.6 SEO-first — 2026-05-16 (ajout §14 trois boucles + rituel ; nouveaux types `register|moc|decision|proof` en §5.1 ; nouveaux dossiers wiki en §3 ; §7bis skills système ; cf. [[decisions/0001-fermeture-boucles-second-cerveau]])
**Maintainer humain** : Timothée Boussardon
**Maintainer LLM** : Claude Code (et tout agent qui lit ce fichier)
