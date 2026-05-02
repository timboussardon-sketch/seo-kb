---
title: "Créer un check d'indexation automatique avec Claude Code"
slug: check-indexation-claude
type: brief-ops
date: 2026-05-02
auteur: Tim Boussardon (Organikk)
category: Agents IA / Monitoring SEO
keyword: agent IA indexation
readTime: 8 min
status: prêt-à-implémenter
sources_internes:
  - raw/newsletter/newsletter-agent-ia-verifier-indexation-seo.md
  - wiki/concepts/grounding-score.md
  - wiki/concepts/passage-ranking.md
sources_externes:
  - https://claude.ai/code/routines (interface)
  - https://developers.google.com/search/docs/monitor-debug/url-inspection-api
  - https://docs.netlify.com/build/configure-builds/file-based-configuration/ (déploiement)
---

# Créer un check d'indexation automatique avec Claude Code

## Objectif

Automatiser la vérification mensuelle (ou one-shot) que les pages stratégiques d'un site sont **indexées par Google** et **citées par les LLM**, sans ouvrir GSC manuellement chaque mois. Livrable : rapport markdown pushé en PR sur le repo GitHub du site.

## Cas d'usage déclencheurs

- Déploiement d'un nouveau cluster (ex : 30 fiches wiki Organikk → check à J+14)
- Lancement d'une stratégie programmatic SEO (centaines de pages générées)
- Suivi mensuel récurrent sur un site client en accompagnement (gating SLA)
- Audit ponctuel pour un prospect avant call commercial

## Stack technique

| Composant | Rôle | Coût |
|---|---|---|
| Claude Code CLI | Orchestration locale + commande `/schedule` | Plan Pro / Max |
| Routine CCR (cloud) | Exécution distante isolée | Inclus |
| GitHub repo | SOT des URLs à monitorer + dépôt du rapport | Gratuit |
| `gh` CLI | Création PR depuis l'agent | Gratuit |
| (Optionnel) Service account GSC | Statut indexation officiel | Gratuit |

Aucun outil tiers payant. Pas de SerpAPI, pas de Semrush, pas d'Ahrefs.

## Architecture

```
1. Liste URLs (src/data/wiki.ts)
        ↓
2. Routine schedule (cloud Anthropic)
        ↓
3. Agent Claude Sonnet 4.6 (isolé)
        ↓
4. 6 checks séquentiels
        ↓
5. Rapport markdown
        ↓
6. PR GitHub → notification email
```

## Les 6 checks

| # | Check | Source | Fiabilité |
|---|---|---|---|
| 1 | HTTP 200 | curl direct | 100 % |
| 2 | Présence sitemap | sitemap.xml public | 100 % |
| 3 | Indexation Google estimée | scraping `site:` Google | ~40 % (rate-limit) |
| 4 | Maillage interne intègre | parsing /glossaire et /wiki | 100 % |
| 5 | Citation Perplexity | scraping HTML | ~60 % (rendu JS) |
| 6 | Génération rapport + PR | gh CLI | 100 % |

**Variante haute fiabilité** : remplacer check #3 par un appel à la GSC URL Inspection API via service account. Setup 30 min mais passage à 100 % de fiabilité (statut officiel `INDEXED` / `DISCOVERED_NOT_INDEXED` / `CRAWLED_NOT_INDEXED` / `404`).

## Étapes de mise en place

### 1. Single source of truth des URLs

Dans le repo du site, un fichier qui exporte la liste des URLs à monitorer.

```ts
// src/data/wiki.ts
export const WIKI_CONCEPTS = [
  { slug: 'agent-seo', term: 'Agent SEO', ... },
  // 29 autres
]
```

Si pas de stack TypeScript : un simple `urls.txt` à la racine fait l'affaire.

### 2. Prompt agent self-contained

L'agent démarre **sans aucun contexte**. Le prompt doit être autonome. Structure qui marche :

```markdown
## Mission
Produire un rapport de statut sur les N pages, sans tenter aucune
action de forçage d'indexation. Lecture seule, écriture limitée à reports/.

## Étapes
### 1. Charger la liste
Lis `src/data/wiki.ts` et extrais les slugs.

### 2. HTTP check
Pour chaque slug : curl -sI -A "Mozilla/5.0" https://site.fr/wiki/{slug}

### 3. Indexation Google (estimation)
curl -sL "https://www.google.com/search?q=site:site.fr/wiki/{slug}"
Limites à signaler dans le rapport :
- Google bloque après 5-15 requêtes (CAPTCHA / page sorry/)
- Espace les requêtes de 3-5 secondes
- Marque "non testable - rate limit" plutôt que "non indexée"

### 4. Maillage
curl /glossaire et /wiki, vérifie présence des liens.

### 5. Perplexity (best effort)
curl perplexity.ai/search?q=... pour 5 concepts stratégiques.

### 6. Rapport
Crée reports/wiki-indexation-{date}.md avec :
- Synthèse (X/N par dimension)
- Tableau détaillé par slug
- Anomalies + recommandations
- Section "Limites du rapport"

### 7. PR GitHub
gh pr create avec title et body précis.

## Contraintes
- AUCUNE action de soumission/forçage d'indexation
- Toujours via PR, jamais commit direct sur main
- Distinction explicite entre "non indexée" et "non testable"
- Si une étape échoue, continuer les autres et signaler dans le rapport
```

### 3. Schedule via Claude Code

```bash
/schedule
```

Choix structurants :

- **Récurrence** : `run_once_at` (one-shot daté) vs `cron_expression` (récurrent)
  - Cluster déployé → one-shot à J+14
  - Site client en SLA → cron `0 1 1 * *` (1er de chaque mois, 01h UTC)
- **Modèle** : `claude-sonnet-4-6` (Opus inutile pour ce job)
- **Tools** : `Bash, Read, Write, Edit, Glob, Grep`
- **Environment** : Default Anthropic Cloud
- **MCP** : aucun pour la version basique. Gmail si on veut un email résumé en plus de la PR.

### 4. Réception et lecture du rapport

À l'heure prévue : agent tourne 5-10 min → push branche `report/wiki-indexation-{date}` → ouvre PR → notification email GitHub.

Le rapport markdown est rendu directement dans la PR. 3 sections à lire (10 min max) :
- **Synthèse** : X/N par dimension
- **Anomalies** : ce qui ne va pas + reco par anomalie
- **Recommandations** : 2-5 actions à prioriser

Le détail page par page sert de doc, pas de lecture systématique.

## Variations possibles

### Multi-sites
Un seul agent qui itère sur N repos. Adapter le prompt pour boucler sur plusieurs `WIKI_CONCEPTS` provenant de checkouts différents.

### Multi-sources d'index
Ajouter Bing Webmaster Tools (gratuit, API simple), Yandex (si pertinent). Agrandit la couverture sans complexité majeure.

### Scoring composite
Faire l'agent calculer un "Health Score" par page = HTTP × Sitemap × Indexation × Maillage × Citation. Permet de classer les pages les plus à risque en haut du rapport.

### Pour aller plus loin — GSC API officielle
Procédure (30 min de setup une fois) :
1. Console Google Cloud → IAM → service account, activer `searchconsole.googleapis.com`
2. Télécharger la clé JSON
3. Search Console → settings de la propriété → Users → ajouter l'email du service account, role Owner
4. `gh secret set GSC_SA_JSON < /path/to/service-account.json`
5. Modifier le prompt agent : étape lit le secret via `gh secret env`, signe un JWT, échange contre access token, POST sur `urlInspection.index.inspect`

Pour 30 URLs, l'estimation suffit. Pour 5 000+ URLs, GSC API obligatoire.

## Limites et garde-fous

### Limites techniques
- **Google rate-limit** : scraping `site:` bloque après 5-15 requêtes. Espacement 3-5 secondes minimum.
- **Perplexity rendu JS** : le HTML brut peut ne pas contenir les citations. Marquer "non testable" plutôt que "non cité".
- **Sitemap dynamique** : si le sitemap est généré côté serveur avec pagination, l'agent ne lira que la première page.

### Garde-fous design
- Lecture seule sur le web public
- Écriture limitée à `reports/` dans le repo
- Aucune action sur Google (pas de soumission, pas de force-indexation)
- Pas de commit direct sur main, toujours via PR
- Distinction stricte "non indexée" vs "non testable" dans le rapport

> Un agent qui peut "réparer" automatiquement est un agent qui peut casser à 3h du matin un dimanche. Discipline : observation côté agent, décision côté humain.

## Sortie attendue

Fichier `reports/wiki-indexation-{date}.md` structuré :

```markdown
# Wiki indexation check — 2026-05-16

## Synthèse
- HTTP 200 : X/30
- Présent dans sitemap : X/30
- Indexation Google estimée : X/30 (Y non testables — rate limit)
- Citations Perplexity (échantillon 5) : X/5
- Maillage interne intègre : OUI/NON

## Détail par fiche
[Tableau markdown : slug | HTTP | sitemap | google estim | notes]

## Anomalies détectées
[Liste des problèmes concrets]

## Recommandations (sans action automatique)
[2-5 actions à prendre côté humain]

## Limites de ce rapport
[Ce qui n'a pas pu être testé et pourquoi]
```

PR créée sur GitHub avec le rapport en body, branche `report/wiki-indexation-{date}`.

## Exemple d'output réel

Voici à quoi ressemblerait le rapport généré par l'agent sur le wiki Organikk au 16 mai 2026 (J+14 après le déploiement du 2 mai). Données plausibles, fenêtre serrée.

---

```markdown
# Wiki indexation check — 2026-05-16

Déploiement initial : 2026-05-02 (30 fiches)
Fenêtre d'observation : 14 jours
Agent : claude-sonnet-4-6 · routine wiki-indexation-check (trig_018QinqfTpMemJBBAbpdyW8v)
Durée d'exécution : 7 min 24 s

## Synthèse

- HTTP 200            : **30 / 30** ✅
- Présent dans sitemap : **30 / 30** ✅
- Indexation Google estimée : **18 / 30** (8 non testables — rate limit Google)
- Citations Perplexity (échantillon 5) : **1 / 5**
- Maillage interne intègre : **OUI** ✅

## Détail par fiche

| # | Slug | HTTP | Sitemap | Google estim. | Notes |
|---|------|------|---------|---------------|-------|
| 1 | agent-seo | 200 | ✅ | indexée | top 12 sur "agent SEO IA" |
| 2 | grounding-score | 200 | ✅ | indexée | top 6 sur "grounding score SEO" |
| 3 | passage-ranking | 200 | ✅ | indexée | top 9 sur "passage ranking google" |
| 4 | rag-retrieval-augmented-generation | 200 | ✅ | indexée | requête longue tail OK |
| 5 | rrf-reciprocal-rank-fusion | 200 | ✅ | non indexée | Discovered, pas encore crawlé |
| 6 | embedding-seo | 200 | ✅ | indexée | — |
| 7 | similarite-cosinus | 200 | ✅ | non testable | rate limit Google (#6) |
| 8 | ai-overviews | 200 | ✅ | indexée | top 18 sur "ai overviews définition" |
| 9 | aeo-answer-engine-optimization | 200 | ✅ | indexée | — |
| 10 | geo-generative-engine-optimization | 200 | ✅ | indexée | top 14 sur "GEO SEO" |
| 11 | llm-large-language-model | 200 | ✅ | non testable | rate limit Google (#11) |
| 12 | triade-serp | 200 | ✅ | indexée | concept rare, peu de concurrence |
| 13 | information-gain | 200 | ✅ | indexée | top 8 sur "information gain SEO" |
| 14 | surprise-score | 200 | ✅ | non indexée | Discovered, pas encore crawlé |
| 15 | muvera | 200 | ✅ | non testable | rate limit Google (#15) |
| 16 | titans-architecture | 200 | ✅ | non indexée | Discovered, pas encore crawlé |
| 17 | dpr-dense-passage-retrieval | 200 | ✅ | non testable | rate limit Google (#17) |
| 18 | topical-authority | 200 | ✅ | indexée | top 24 sur "topical authority" |
| 19 | maillage-interne | 200 | ✅ | indexée | top 11 sur "maillage interne SEO" |
| 20 | eeat | 200 | ✅ | indexée | — |
| 21 | featured-snippet | 200 | ✅ | non testable | rate limit Google (#21) |
| 22 | zero-click-search | 200 | ✅ | indexée | — |
| 23 | intention-de-recherche | 200 | ✅ | indexée | — |
| 24 | pillar-page | 200 | ✅ | non indexée | Discovered, pas encore crawlé |
| 25 | silo-seo | 200 | ✅ | non testable | rate limit Google (#25) |
| 26 | cocon-semantique | 200 | ✅ | indexée | top 32 sur "cocon sémantique" |
| 27 | clustering-semantique | 200 | ✅ | non testable | rate limit Google (#27) |
| 28 | programmatic-seo | 200 | ✅ | non indexée | Discovered, pas encore crawlé |
| 29 | audit-seo | 200 | ✅ | non testable | rate limit Google (#29) |
| 30 | core-web-vitals | 200 | ✅ | indexée | — |

## Citations Perplexity (échantillon)

| Concept testé | organikk.co cité ? | URL si citée |
|---|---|---|
| grounding-score | ❌ non | — |
| agent-seo | ❌ non | — |
| geo-generative-engine-optimization | ✅ **oui** | /wiki/geo-generative-engine-optimization |
| aeo-answer-engine-optimization | ❌ non | — |
| triade-serp | ⚠️ non testable | rendu JS, HTML vide |

## Maillage interne — vérification

- /glossaire : 30/30 liens vers /wiki/{slug} présents ✅
- /wiki (hub) : 30/30 fiches listées ✅
- Échantillon 5 fiches (sampled : grounding-score, agent-seo, eeat, cocon-semantique, audit-seo) :
  - Concepts voisins (≥3) : 5/5 ✅
  - Article blog lié (≥1) : 5/5 ✅
  - CTA outil/service : 5/5 ✅

## Anomalies détectées

1. **5 fiches en "Discovered, pas encore crawlé"** : `rrf-reciprocal-rank-fusion`, `surprise-score`, `titans-architecture`, `pillar-page`, `programmatic-seo`. Google les a découvertes via le sitemap mais ne les a pas encore explorées. Comportement normal à J+14 sur un site à autorité moyenne. Pas d'action requise sauf si toujours non-indexées à J+30.

2. **8 fiches non testables (rate limit Google)** : Google a déclenché une page sorry/ après la requête #6. Marquées comme inconnues, pas comme non-indexées. Pour fiabilité 100 %, voir section "GSC API officielle" du brief.

3. **1 seule citation Perplexity sur 5 testées** (`geo-generative-engine-optimization`). Normal à J+14 — les LLM mettent typiquement 3 à 8 semaines pour intégrer du contenu nouveau dans leurs réponses, même quand les pages sont indexées chez Google.

## Recommandations (sans action automatique)

1. **Forcer recrawl des 5 fiches "Discovered"** depuis Google Search Console (Inspection URL → "Demander une indexation"). Action manuelle, 5 min total. Cible : passer de 18/30 à 23/30 indexées sous 10 jours.

2. **Ajouter 1 backlink externe** vers `/wiki/surprise-score` et `/wiki/titans-architecture` (concepts les plus pointus, faible autorité externe). Un post LinkedIn ou un commentaire sur un article tiers pertinent suffit.

3. **Re-déclencher cet agent à J+30** (1er juin 2026) pour mesurer la progression. Si l'indexation stagne sous 25/30, examiner la qualité du contenu des fiches non-indexées : titre trop long, definition trop courte, manque de schema DefinedTerm.

4. **Brancher la GSC URL Inspection API** avant le prochain check récurrent pour passer les 8 "non testable" en statut officiel (`INDEXED` / `DISCOVERED` / `CRAWLED_NOT_INDEXED`). Setup 30 min une fois. Voir section dédiée du brief.

5. **Pour les citations LLM** : attendre 4 semaines supplémentaires avant de tirer une conclusion. Si à J+45 toujours 1/5, le frein n'est pas l'indexation mais la sélection des sources par les LLM — investiguer le `Surprise score` du contenu des 4 fiches non citées.

## Limites de ce rapport

- Indexation Google estimée par scraping public (`site:` query). Fiabilité ~40 % en raison du rate-limit. Source de vérité officielle = GSC URL Inspection API (non branchée sur ce check).
- Citations Perplexity testées sur 5 concepts seulement (sample). Le HTML rendu côté JS limite la fiabilité du parsing — une citation présente visuellement peut être marquée "non" ici.
- Aucune action de forçage d'indexation tentée (sur consigne explicite du prompt).
- Maillage interne vérifié sur 5 fiches au hasard (sample), pas sur les 30 — un check exhaustif demanderait 30 requêtes supplémentaires.
- Les positions Google indiquées sont indicatives (extraites de la SERP scrapée), pas des positions GSC réelles.
```

---

**Lecture du rapport — 30 secondes pour le décideur** :
- 30/30 HTTP + sitemap = déploiement technique parfait
- 18/30 indexées en 14 jours = courbe d'indexation normale, pas de blocage
- 5 fiches à recrawler manuellement = action concrète identifiée
- 1 seule citation LLM = trop tôt pour conclure, re-checker à J+45
- Setup GSC API recommandé avant le prochain check récurrent

C'est exactement ce que le rapport doit produire : un constat chiffré, une action prioritaire (recrawl manuel des 5 Discovered), un calendrier de re-vérification.

## Liens utiles

- Newsletter dérivée : [[newsletter-agent-ia-verifier-indexation-seo|Newsletter — L'audit d'indexation qui se fait sans vous, chaque mois]]
- Concept lié : [[passage-ranking|Passage Ranking]] · [[grounding-score|Grounding Score]]
- Routine de référence : `wiki-indexation-check` (trig_018QinqfTpMemJBBAbpdyW8v) — fire le 16 mai 2026 sur le wiki Organikk

## Réutilisation client

Pour appliquer ce système à un client en accompagnement :
1. Créer un fichier `urls-prio.ts` ou `urls-prio.txt` dans son repo (top 30 pages business)
2. Adapter le prompt agent (URLs, période, critères)
3. Schedule cron mensuel
4. Inclure le rapport mensuel dans la note de suivi

Coût marginal par client : ~15 min de setup, 0 € récurrent. À facturer dans la rétro mensuelle ou comme bonus différenciant en pitch.
