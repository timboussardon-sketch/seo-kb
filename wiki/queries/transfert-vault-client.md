---
type: query
title: Transfert vault client — tout sauf stratégie client
aliases: [transfert-vault, starter-pack-client]
tags: [transfert, client, vault, livrable, procedure]
created: 2026-04-13
updated: 2026-04-13
sources: 0
confidence: high
status: stable
---

# Transfert vault client — tout sauf stratégie client

Procédure factuelle pour livrer un vault Obsidian à un client (participant bootcamp ou client retainer) en excluant la stratégie client Tim (prospects, cas-clients, offre commerciale).

Basée sur l'inventaire complet du vault à date 2026-04-13 (36 sources, 36 entités, 35 concepts).

## ✅ Transféré (doctrine générique + sources publiques)

### `wiki/concepts/` — 30 concepts sur 35

Tous **sauf** les 4 concepts bootcamp/commerciaux (voir §non-transféré).

**Doctrine SEO/GEO** : `aeo`, `grounding-score`, `surprise-metric`, `surprise-gap`, `weight-decay`, `information-gain`, `passage-ranking`, `rrf`, `e-e-a-t`, `fully-meets`, `triade-serp`, `confidence-score`, `answer-first-pattern`, `structural-information-geo`, `4w-deep-reflection`, `metriques-visibilite-geo`, `test-substitution-llm`, `programmatique-pseo`, `product-led-seo`, `data-proprietaire`, `seo-multi-plateforme`, `anti-ai-writing`, `workflow-redaction-8-etapes`, `agentic-search`, `ingenierie-semantique-inversee`

**Méthode KB** : `persistent-wiki-vs-rag`, `obsidian-as-ide`, `ingest-workflow`, `query-synthesis`, `cli-tools-optional`, `memory-llm-vs-wiki-persistant`

### `wiki/entities/` — 24 entités sur 36

**Algos Google** : `bert`, `rankbrain`, `sge`, `mum`, `neural-matching`
**Algos recherche** : `bm25`, `dpr`, `muvera`, `isi`
**Architectures IA** : `titans`, `miras`, `google-deepmind`
**Concepts-marque** : `notebooklm`, `youtube`
**Acteurs** : `karpathy`, `vannevar-bush`, `metehan`
**Quality Raters** : `quality-raters-guidelines`
**Outils SEO** : `obsidian`
**Benchmarks** : `geo-bench`, `product-bench`, `sageo-arena-benchmark`

### `wiki/sources/` — 19 sources sur 36

**Papers** (8) : tous les papers arxiv/KDD/AAAI + QRG 2026 + SEMrush + Titans + MIRAS
**Articles Algorithme publiés** (6) : les 6 newsletters publiques
**Karpathy LLM Wiki** + Tim analyse Titans/MIRAS (doctrine publique)
**Organikk glossaire** (réf terminologique publique)
**Skills proprietary + 2 prompts pSEO** (si cadre bootcamp — sinon à trancher, cf. zone grise)

### `wiki/syntheses/` — 1 sur 3

Seule `doctrine-seo-post-sge` (thèse 4 piliers — doctrine transférable).

### `wiki/queries/` — tout

`2026-04-12-wiki-pattern-vs-grounding-score` et cette query.

### `raw/`

- `raw/articles/` (6 newsletters Algorithme publiées)
- `raw/papers/` (5 PDFs — utiles pour re-ingest ou vérification)
- `raw/etudes-seo/` (5 PDFs + 5 synthèses)
- `raw/assets/` (images)

### Fichiers config

- **`AGENTS.md`** — avec version light optionnelle (retirer les références au bootcamp si client non-bootcamp)
- **`README.md`** — guide humain
- **`wiki/index.md`** — à régénérer après filtre (sinon liens cassés vers pages retirées)
- **`wiki/log.md`** — à vider ou garder une version purgée des entrées bootcamp/clients

## ❌ Non transféré (stratégie client Tim)

### `wiki/sources/` — 12 exclus

- `2026-04-13-analyse-calls-prospects-bootcamp` (stratégie commerciale)
- `2026-04-13-call-01-arnaud` → `-09-julien` (7 transcripts prospects — **confidentiel**)
- `2026-04-13-cas-clients-resultats` (stratégie commerciale)
- `2026-04-13-offre-bootcamp-seo-ia` (produit Tim)
- `2026-04-13-victoria-garden-pseo` (client-note Victoria Garden)

### `wiki/entities/` — 12 exclus

- **Prospects bootcamp** (8) : `arnaud`, `marrusia-cecile`, `jamel`, `dev-web-anon`, `juliette`, `christophe`, `franck`, `julien`
- **Entreprises tierces prospects** (2) : `audopass`, `jumpto`
- **Clients Tim** : `victoria-garden`
- **Produits Tim** : `bootcamp-seo-ia`

### `wiki/concepts/` — 4 exclus

- `avatar-freelance-sans-systeme` (avatar bootcamp Tim)
- `cercle-vicieux-temps-structure` (pattern bootcamp)
- `peur-train-ia` (pattern bootcamp)

→ `tabou-visibilite` est **à trancher** (zone grise — doctrine vente applicable hors bootcamp).

### `wiki/syntheses/` — 2 exclus

- `vendre-seo-ia-2026` (stratégie commerciale Tim)
- `workflow-complet-consultant-seo-ia` (pipeline prospection Tim)

### `raw/`

- **`raw/cas-clients/`** — **tout** (stratégie client)
- **`raw/transcripts/`** — **tout** (calls prospects, confidentiel)
- **`raw/notes/`** — filtrer :
  - Exclure : `tim-about-me`, `tim-my-rules`, `tim-my-voice`, `tim-readme-bot-instructions`, `offre-bootcamp-seo-ia`, `analyse-calls-prospects-bootcamp`, `cas-clients-resultats`
  - Inclure (zone grise cf. ci-dessous) : `skill-*.md` (10 skills), `tim-workflow-redaction`, `tim-prompt-systeme`, `tim-anti-ai-writing-style`, `seo-ia-tim`
- **`raw/data/organikk-*`** — scrape du site commercial Tim, **non** à transférer par défaut

## ⚠️ Zone grise à trancher avec Tim

Avant chaque transfert, 6 décisions explicites à prendre :

| Fichier | Argument pour | Argument contre |
|---|---|---|
| `entities/organikk-co` | Référence utile pour comprendre le positionnement | Expose business model Tim au client |
| `entities/fusionn-io` | Utile si le client utilise Fusion | Outil commercial Tim |
| `concepts/tabou-visibilite` | Doctrine vente applicable à tout SEO | Contient des infos internes du bootcamp |
| `sources/2026-04-12-organikk-blog-scrape` | Référence catalogue articles | Expose stratégie contenu commerciale Tim |
| `sources/2026-04-12-tim-skills-seo-proprietary` | Les skills = ce que le client achète dans le bootcamp | Si client hors-bootcamp : c'est ton offre |
| `raw/notes/skill-*.md` (10 fichiers) | Même logique que ci-dessus | Idem |

**Règle de décision proposée** : transfert complet pour **participant bootcamp** (ils ont payé pour accéder aux skills), transfert limité pour **client retainer simple** (stratégie contenu de leur cas + doctrine générique uniquement).

## Script d'extraction (bash)

Script factuel qui crée un vault filtré dans `~/seo-kb-client-export/`. À exécuter **après** avoir tranché la zone grise.

```bash
#!/bin/bash
# Transfert vault client — tout sauf stratégie client
# À exécuter depuis ~/Documents/seo-kb/

set -e

SRC="$HOME/Documents/seo-kb"
DST="$HOME/seo-kb-client-export"
MODE="${1:-bootcamp}"   # bootcamp ou retainer

rm -rf "$DST"
mkdir -p "$DST"

# 1. Structure de base
cp "$SRC/AGENTS.md" "$DST/"
cp "$SRC/README.md" "$DST/" 2>/dev/null || true
mkdir -p "$DST/wiki/"{sources,entities,concepts,syntheses,queries,briefs,clusters,quick-wins,cannibalisation,maillage,posts-linkedin,revues-presse}
mkdir -p "$DST/raw/"{articles,papers,etudes-seo,notes,data,assets}

# 2. Concepts — tous sauf 4 bootcamp
EXCLUDE_CONCEPTS=(
  "avatar-freelance-sans-systeme"
  "cercle-vicieux-temps-structure"
  "peur-train-ia"
)
# tabou-visibilite : zone grise. Par défaut transféré (doctrine vente générique).
for f in "$SRC/wiki/concepts/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_CONCEPTS[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/concepts/"
done

# 3. Entities — tous sauf prospects + clients + produits Tim
EXCLUDE_ENTITIES=(
  "arnaud" "marrusia-cecile" "jamel" "dev-web-anon" "juliette"
  "christophe" "franck" "julien" "audopass" "jumpto"
  "victoria-garden" "bootcamp-seo-ia"
)
# Zone grise : organikk-co, fusionn-io → par défaut exclus
[[ "$MODE" == "bootcamp" ]] && EXCLUDE_ENTITIES+=() || EXCLUDE_ENTITIES+=("organikk-co" "fusionn-io")

for f in "$SRC/wiki/entities/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_ENTITIES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/entities/"
done

# 4. Sources — exclure prospects + client-note + stratégie commerciale
EXCLUDE_SOURCES=(
  "2026-04-13-analyse-calls-prospects-bootcamp"
  "2026-04-13-call-01-arnaud" "2026-04-13-call-04-jamel"
  "2026-04-13-call-05-dev-web" "2026-04-13-call-06-juliette"
  "2026-04-13-call-07-christophe" "2026-04-13-call-08-franck"
  "2026-04-13-call-09-julien"
  "2026-04-13-cas-clients-resultats"
  "2026-04-13-offre-bootcamp-seo-ia"
  "2026-04-13-victoria-garden-pseo"
)
# Mode retainer : exclure aussi skills proprietary + prompts pSEO (offre Tim)
if [[ "$MODE" != "bootcamp" ]]; then
  EXCLUDE_SOURCES+=(
    "2026-04-12-tim-skills-seo-proprietary"
    "2026-04-13-prompt-pseo-produit-service"
    "2026-04-13-prompt-pseo-non-produit"
    "2026-04-12-organikk-blog-scrape"
    "2026-04-12-organikk-glossaire-scrape"
  )
fi

for f in "$SRC/wiki/sources/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_SOURCES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/sources/"
done

# 5. Syntheses — seule doctrine-seo-post-sge
cp "$SRC/wiki/syntheses/doctrine-seo-post-sge.md" "$DST/wiki/syntheses/"

# 6. Queries — tout
cp "$SRC/wiki/queries/"*.md "$DST/wiki/queries/" 2>/dev/null || true

# 7. Raw — filtrer
cp "$SRC/raw/articles/"*.md "$DST/raw/articles/" 2>/dev/null || true
cp "$SRC/raw/papers/"*.md "$DST/raw/papers/" 2>/dev/null || true
cp "$SRC/raw/papers/"*.pdf "$DST/raw/papers/" 2>/dev/null || true
cp "$SRC/raw/etudes-seo/"* "$DST/raw/etudes-seo/" 2>/dev/null || true

# Raw notes : exclure les perso et stratégie commerciale
EXCLUDE_NOTES=(
  "tim-about-me" "tim-my-rules" "tim-my-voice"
  "tim-readme-bot-instructions"
  "offre-bootcamp-seo-ia"
  "analyse-calls-prospects-bootcamp"
  "cas-clients-resultats"
)
for f in "$SRC/raw/notes/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_NOTES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/raw/notes/"
done

# 8. Régénérer index.md et log.md (vides, à reconstruire côté client)
cat > "$DST/wiki/index.md" <<INDEX
# Index du wiki SEO/IA/GEO

> Index à régénérer au fil de l'ingestion de vos propres sources.
> Structure attendue : voir AGENTS.md §8.

## Sources (N)
## Entities (N)
## Concepts (N)
## Syntheses (N)
## Queries (N)
INDEX

cat > "$DST/wiki/log.md" <<LOG
# Log

> Journal chronologique append-only. Parseable via \`grep "^## \[" wiki/log.md\`.

## [$(date +%Y-%m-%d)] bootstrap | Vault reçu de Timothée Boussardon
- doctrine SEO/GEO + papers de référence + méthode Karpathy/Obsidian
- à personnaliser avec vos propres sources clients et cas terrain
LOG

# 9. .gitkeep pour dossiers vides
for dir in "$DST/wiki/"{briefs,clusters,quick-wins,cannibalisation,maillage,posts-linkedin,revues-presse} "$DST/raw/"{data,assets}; do
  touch "$dir/.gitkeep"
done

echo "✅ Vault exporté : $DST"
echo "   Mode : $MODE"
echo "   À vérifier manuellement avant envoi au client :"
echo "   - wiki/sources/ : plus de transcripts, cas-clients, offre bootcamp"
echo "   - wiki/entities/ : plus de prospects, clients, produits Tim"
echo "   - raw/cas-clients/ et raw/transcripts/ : absents"
```

**Usage** :
```bash
bash export-client-vault.sh bootcamp    # Participant bootcamp (inclut skills, prompts pSEO)
bash export-client-vault.sh retainer    # Client retainer (doctrine générique uniquement)
```

## Procédure post-export

Avant livraison au client :

1. **Audit manuel** du dossier exporté — `ls -la $HOME/seo-kb-client-export/wiki/sources/` pour vérifier qu'aucun fichier sensible n'a fuité
2. **grep sur les wikilinks cassés** : `grep -r "\[\[.*\]\]" $HOME/seo-kb-client-export/wiki/ | grep -oE "\[\[[^]]+\]\]" | sort -u` → vérifier que les liens pointent vers des pages existantes
3. **Zip + transfert** : `zip -r seo-kb-starter.zip seo-kb-client-export/`
4. **Guide d'installation** (doc séparée à fournir) : prérequis (Obsidian, Node.js, Claude Code, Claude Pro), setup en 5 étapes

## Limites

- Le script dépend de la structure actuelle — si la KB évolue (nouveaux concepts bootcamp, nouveaux clients), la liste d'exclusion doit être mise à jour manuellement
- **Les wikilinks internes** peuvent pointer vers des pages exclues → liens cassés côté client. L'étape 2 de l'audit post-export les détecte.
- L'historique git complet **contient tous les commits** y compris les pages ensuite exclues. Pour un transfert propre, `git init` un nouveau repo depuis le dossier exporté.
- Le client reçoit un **snapshot figé** — il ne bénéficiera pas des mises à jour futures de ta doctrine sans un second transfert.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/persistent-wiki-vs-rag]] · [[entities/obsidian]]
