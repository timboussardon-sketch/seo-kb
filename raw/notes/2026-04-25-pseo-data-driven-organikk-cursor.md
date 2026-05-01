---
date: 2026-04-25
site: organikk.co
type: pSEO data-driven (4 modèles, zéro réécriture humaine)
auteur: Tim Boussardon
contraintes: respect strict robots.txt + uniquement APIs officielles (Google Custom Search, Gemini, Claude, Suggest)
---

# pSEO data-driven pour organikk.co — 4 modèles validés

## Principe directeur

Chaque modèle suit la règle **template fixe + dataset structuré = N pages organiques uniques**. La valeur de chaque page vient des **chiffres eux-mêmes** (pas du commentaire éditorial). Aucune réécriture humaine n'est nécessaire.

**Stack autorisé** :
- Google Custom Search JSON API (officielle)
- Gemini API (clé propriétaire)
- Claude API (abonnement existant) avec tool `web_search`
- Google Suggest endpoint (autorisé par les CGU Google — utilisé par les navigateurs)
- Crawl propriétaire avec respect strict des `robots.txt` cibles

**Stack interdit** : SerpAPI, DataForSEO, Bright Data, Apify Google Search Scraper, et tout intermédiaire qui contourne le `Disallow: /search` de Google.

---

## Modèle 1 — Empreinte SERP : qui domine sur Google, Claude, Gemini

### Architecture

- **URL pattern** : `organikk.co/empreinte-serp/[slug-requête]`
- **Variable** : requête (commerciale, locale, B2B, e-commerce)
- **Volume potentiel** : 5 000 à 50 000 pages

### Mécanique de données

Pour chaque requête, le pipeline exécute **3 sources en parallèle** :

| Source | API | Méthode |
|---|---|---|
| Google (SERP web) | Google Custom Search JSON API | `GET https://www.googleapis.com/customsearch/v1?q=X&cx=Y&key=Z` → top 10 URLs avec title/snippet |
| Claude | Anthropic Messages API + tool `web_search_20250305` | Prompt : *"Quelles sont les meilleures sources pour [requête] ? Cite tes sources."* → parse `tool_use` + `citations` |
| Gemini | Gemini 2.5 Pro API + `tools: [{google_search: {}}]` | Idem prompt → parse `groundingChunks[].web.uri` |

**Non-déterminisme géré** : pour Claude et Gemini, **N=10 runs par requête** avec température 0.7 → on calcule la **fréquence d'apparition** de chaque domaine sur les 10 runs.

Pour Google Custom Search : 1 snapshot suffit (la SERP est stable à court terme).

### Template de page

- **H1** : *« Empreinte SERP de "[requête]" : Google vs Claude vs Gemini »*
- **Bloc 1** — Tableau comparatif 3 colonnes (Google rank, Claude fréquence /10, Gemini fréquence /10)
- **Bloc 2** — Score de chevauchement : combien de domaines apparaissent dans les 3 sources
- **Bloc 3** — Domaines exclusifs à chaque IA (le delta exploitable)
- **Bloc 4** — Visualisation : graphe de Venn des 3 sources
- **Bloc 5** — Passage ancré méthodologique 150-200 mots : nombre de runs, modèles utilisés, date de capture
- **Bloc authorship** Tim Boussardon (~50 mots)
- **CTA** : audit GEO de mon site sur cette requête

### Schéma DB minimal

```sql
empreinte_serp (
  query_slug PK,
  query_text,
  captured_at,
  google_results JSONB,    -- [{rank, url, title, snippet}]
  claude_runs JSONB,        -- [{run_id, sources: [url]}]
  gemini_runs JSONB,        -- idem
  domain_frequencies JSONB, -- {domain: {google: 1|0, claude: 0..10, gemini: 0..10}}
  overlap_score INT
)
```

### Coûts (1 000 pages MVP)

- Google Custom Search : 1 000 requêtes × 5 $/1K = **5 €**
- Claude API : 10 runs × 1 000 = 10 000 calls × ~0.005 € = **50 €**
- Gemini API (avec grounding) : 10 runs × 1 000 = 10 000 calls × ~0.014 € (grounding) = **140 €**
- **Total MVP : ~195 €**, refresh hebdomadaire : ~195 €/semaine soit **~800 €/mois**

### Refresh

- Google : mensuel (cap budget Custom Search)
- Claude/Gemini : hebdomadaire (la donnée IA bouge plus vite que la SERP)

### Conformité

- Google Custom Search : API officielle, ToS respecté
- Claude/Gemini : APIs officielles, prompts neutres, comptes propres
- Aucun scraping de la SERP Google directe

---

## Modèle 2 — Entités sémantiques attendues sur [requête]

### Architecture

- **URL pattern** : `organikk.co/entites-serp/[slug-requête]`
- **Variable** : requête informationnelle ou transactionnelle
- **Volume potentiel** : 10 000+ pages

### Mécanique de données

Pour chaque requête, le pipeline :

1. **Récupérer les 10 URLs ranking** via **Google Custom Search JSON API** (`q=requête&num=10`)
2. **Crawler chaque URL** avec un crawler propriétaire (Playwright headless) en respectant son `robots.txt`
3. **Extraction d'entités** via **Gemini 2.5 Pro API** avec un prompt structuré :
   ```
   Extrait toutes les entités nommées de ce texte.
   Catégorise : technique / preuve_quantitative / multimodal / divergence.
   Renvoie en JSON.
   ```
4. **Agrégation** : pour chaque entité, fréquence d'apparition sur les 10 pages (1 à 10)
5. **Calcul du centroïde SERP** : entités présentes dans ≥6/10 pages = vecteur attendu
6. **Gap exploitable** : entités présentes dans 5-7 pages mais absentes dans la première = opportunité

### Template de page

- **H1** : *« Les [N] entités sémantiques attendues par Google sur "[requête]" »*
- **Bloc 1** — Tableau d'entités : nom, fréquence /10, catégorie, top 3 pages où elle apparaît
- **Bloc 2** — Carte du centroïde SERP (entités cœur)
- **Bloc 3** — Gap exploitable : entités présentes ailleurs mais absentes dans la 1ʳᵉ position
- **Bloc 4** — Densité moyenne : nombre d'entités par 1 000 mots, par page
- **Bloc 5** — Score de couverture sémantique de chaque page de la SERP (0-100)
- **Passage ancré 150-200 mots** : modèle d'extraction utilisé, taille échantillon, méthodologie de catégorisation
- **Bloc authorship**
- **CTA** : générer un brief contenu sur cette requête

### Schéma DB

```sql
entites_serp (
  query_slug PK,
  query_text,
  captured_at,
  serp_urls JSONB,        -- [{rank, url}]
  entities JSONB,          -- [{name, category, frequency, source_urls}]
  centroide JSONB,         -- entités du cœur sémantique
  gap_entities JSONB       -- opportunités
)
```

### Coûts (1 000 pages MVP)

- Google Custom Search : 1 000 calls = **5 €**
- Crawl propriétaire (Playwright sur VM Hetzner) : 10 000 pages → **~30 €** compute
- Gemini API NLP : 10 000 extractions × ~0.005 € = **50 €**
- **Total MVP : ~85 €**, refresh trimestriel : **~85 €/trimestre soit ~30 €/mois**

### Refresh

Trimestriel — la composition sémantique de la SERP bouge lentement.

### Conformité

- Google Custom Search : API officielle
- Crawl des pages cibles : `User-Agent: OrganikkBot/1.0 (+https://organikk.co/bot)` + check `robots.txt` avant chaque fetch + respect `Crawl-delay` + cache 7j pour éviter la sur-sollicitation
- Gemini : API officielle

---

## Modèle 5 — Arbre Google Suggest sur [requête]

### Architecture

- **URL pattern** : `organikk.co/suggest-google/[slug-requête]`
- **Variable** : requête seed (mot-clé head)
- **Volume potentiel** : 20 000+ pages

### Mécanique de données

Pipeline récursif sur l'endpoint **Google Suggest** (autorisé, utilisé par les navigateurs) :

```
GET https://suggestqueries.google.com/complete/search?client=firefox&q=X&hl=fr&gl=fr
→ JSON : ["X", ["X suggestion 1", "X suggestion 2", ...]]
```

**Algorithme d'arbre** :
1. **Niveau 0** : seed brute (`crm`)
2. **Niveau 1** : pour chaque caractère a-z et 0-9, requêter `crm a`, `crm b`, ... → ~36 calls → ~360 suggestions uniques
3. **Niveau 2** : pour chaque suggestion niveau 1, requêter à nouveau avec a-z → ~36 × 360 = ~13 000 calls → ~5 000 suggestions niveau 2 uniques
4. **Niveau 3** (optionnel) : sur les top suggestions à fort volume

**Rate limiting strict** : 1 requête / seconde max, depuis plusieurs IPs (proxies résidentiels propres) pour respecter l'usage normal de l'endpoint.

### Template de page

- **H1** : *« Toutes les questions et autocomplétions Google sur "[requête]" »*
- **Bloc 1** — Arbre déroulant niveau 1, 2, 3 (UI accordéon)
- **Bloc 2** — Suggestions catégorisées par préfixe interrogatif : *comment, pourquoi, quel, quand, combien, est-ce que*
- **Bloc 3** — Carte de chaleur des thèmes (clustering NLP via Gemini sur les suggestions)
- **Bloc 4** — Volume estimé via Google Trends API (intérêt relatif normalisé) pour les top 50 suggestions
- **Bloc 5** — Suggestions négatives (`crm sans`, `crm gratuit alternative`, etc.) qui révèlent les frictions
- **Passage ancré 150-200 mots** : méthodologie de l'arbre, profondeur, fraîcheur
- **Bloc authorship**
- **CTA** : générer un brief depuis cet arbre

### Schéma DB

```sql
suggest_tree (
  query_slug PK,
  query_seed,
  captured_at,
  tree_l1 JSONB,         -- [{prefix, suggestions: [string]}]
  tree_l2 JSONB,
  tree_l3 JSONB,
  total_suggestions INT,
  question_clusters JSONB,
  trends_volumes JSONB
)
```

### Coûts (1 000 pages MVP)

- Google Suggest : gratuit (mais infra de queue obligatoire)
- Infra : 1 worker Cloudflare Worker + Redis queue → **~30 €/mois**
- Google Trends : non-officielle, on bascule sur **Google Trends "Embed"** ou via la nouvelle API `Trends API alpha` si l'accès est ouvert (sinon on retire le bloc volume)
- Gemini pour clustering : 1 000 × ~0.002 € = **2 €**
- **Total MVP : ~35 €/mois**

### Refresh

Mensuel — Google Suggest évolue avec les tendances.

### Conformité

- Endpoint Suggest est public et utilisé par tous les navigateurs (Firefox, Chrome). Pas de `Disallow` qui le concerne.
- Rate limiting strict pour ne pas créer une charge anormale
- User-Agent identifiable : `OrganikkBot-Suggest/1.0`

---

## Modèle 6 — Adoption Schema.org par [secteur]

### Architecture

- **URL pattern** : `organikk.co/schema-secteur/[slug-secteur]`
- **Variable** : secteur d'activité (NACE / SIRET / verticale métier)
- **Volume potentiel** : 200 à 500 pages (un par secteur)

### Mécanique de données

Pour chaque secteur, le pipeline :

1. **Constituer un échantillon** de 200-500 sites du secteur (sources : Société.com export, listes Linkedin Sales, annuaires sectoriels publics, OpenCorporates API)
2. **Crawler chaque site** avec respect strict `robots.txt` (Playwright + middleware `robots-parser`)
3. **Extraire les blocs JSON-LD** des pages crawlées : home + 5 pages internes représentatives
4. **Catégoriser les schemas** : `Organization`, `LocalBusiness`, `Product`, `FAQPage`, `Article`, `BreadcrumbList`, `Review`, `HowTo`, `Service`, `Event`, etc.
5. **Croiser avec présence dans Rich Results** : test via la Search Console API sur les sites qui ont une property publique, ou via Google Custom Search en cherchant le domaine + filtrer par snippet enrichi

### Template de page

- **H1** : *« Adoption Schema.org en [secteur] : qui en utilise, lequel, comment »*
- **Bloc 1** — Tableau % d'adoption par type de schema (FAQPage : 23%, Product : 64%, etc.)
- **Bloc 2** — Top 10 sites les plus structurés du secteur (par nombre de schemas distincts détectés — pas un classement éditorial)
- **Bloc 3** — Exemples de balisage extraits : code JSON-LD réel, URL d'origine, date de capture
- **Bloc 4** — Erreurs fréquentes : schemas mal structurés, propriétés manquantes, types obsolètes
- **Bloc 5** — Corrélation présence Schema ↔ volume organique (si la donnée est dispo via crawl + estimation tiers conforme)
- **Passage ancré 150-200 mots** : taille de l'échantillon, méthodologie de constitution, outils de crawl
- **Bloc authorship**
- **CTA** : audit Schema.org de mon site

### Schéma DB

```sql
schema_secteur (
  secteur_slug PK,
  secteur_label,
  captured_at,
  sample_size INT,
  schema_adoption JSONB,    -- {OrganizationType: %, FAQPage: %, ...}
  top_structured_sites JSONB, -- [{domain, distinct_schemas: int}]
  examples JSONB,             -- {schema_type: [{domain, json_ld_extract}]}
  common_errors JSONB
)
```

### Coûts (200 secteurs MVP)

- Source de la liste de sites : Société.com / annuaires publics → manuel, **gratuit**
- Crawl Playwright sur VM Hetzner : 200 × 300 sites × 6 pages = 360 000 fetches → **~150 €** one-shot
- Stockage S3 + Postgres : **~20 €/mois**
- Refresh semestriel : **~150 €/semestre soit 25 €/mois**

### Refresh

Semestriel.

### Conformité

- `User-Agent: OrganikkBot/1.0 (+https://organikk.co/bot)`
- Vérification `robots.txt` avant chaque domaine, respect `Crawl-delay`
- Délai 5 secondes entre fetches sur un même domaine
- Pas de `noindex` cible : on extrait l'HTML rendu, pas du contenu protégé

---

## Matrice de priorisation finale

| Modèle | Pages possibles | Effort initial | Coût mensuel run | Impact SEO | Conversion | Score |
|---|---|---|---|---|---|---|
| 1. Empreinte SERP (Google/Claude/Gemini) | 5K–50K | Élevé (pipeline 3 sources × N runs) | ~800 € | **Très haut** | **Très haut** | **9/10** |
| 2. Entités SERP | 10K+ | Moyen (Custom Search + crawl + NLP) | ~30 € | Haut | Haut | **8.5/10** |
| 5. Arbre Suggest Google | 20K+ | Faible (queue + récursion) | ~35 € | Haut | Moyen | **8/10** |
| 6. Schema secteur | 200–500 | Élevé (crawl + sample) | ~25 € | Moyen | Haut | **7/10** |

**Modèle à lancer en premier** : **Modèle 5 (Arbre Suggest)** — coût bas, mécanique simple, validation rapide de la stack pSEO en 2-3 semaines.
**Modèle pilier 12 mois** : **Modèle 1 (Empreinte SERP)** — asset signature d'Organikk, donnée qui s'accumule, format quasi-vide en français.

---

## Mots-clés exemples par modèle

### Modèle 1 — Empreinte SERP (Google + Claude + Gemini)
1. `qui est cité par chatgpt sur crm`
2. `claude recommande quel logiciel paie`
3. `gemini source agence seo`
4. `comparaison sources ia google [thématique]`
5. `quel site cite chatgpt assurance pro`
6. `gemini cite quoi sur hébergement`
7. `chevauchement google ia [thématique]`
8. `delta serp ia [thématique]`
9. `visibilité ia [marque]`
10. `qui rank dans claude sur [requête]`

### Modèle 2 — Entités SERP
1. `entités sémantiques [thématique]`
2. `quoi mettre dans une page sur [requête]`
3. `champ lexical seo [thématique]`
4. `vecteurs sémantiques [requête]`
5. `topical map [thématique]`
6. `mots-clés latents [requête]`
7. `vocabulaire seo [secteur]`
8. `centroïde sémantique [requête]`
9. `entités google nlp [thématique]`
10. `cooccurrences seo [mot-clé]`

### Modèle 5 — Arbre Suggest Google
1. `autocompletion google [requête]`
2. `suggestions google sur [thématique]`
3. `que cherchent les gens sur [requête]`
4. `tendances autocomplétion [thématique]`
5. `arbre de mots-clés [requête]`
6. `longue traîne google [thématique]`
7. `suggest fr [requête]`
8. `combien de variations [requête]`
9. `idées d'articles sur [thématique]`
10. `mots associés à [requête] google`

### Modèle 6 — Schema secteur
1. `schema.org [secteur]`
2. `balisage json-ld [secteur]`
3. `rich snippet [secteur]`
4. `% sites avec faqpage [secteur]`
5. `donnees structurees [secteur]`
6. `schema product [secteur]`
7. `organization schema [secteur]`
8. `localbusiness schema taux`
9. `breadcrumb schema [secteur]`
10. `review schema adoption france`

---

## Plan d'exécution 90 jours

### Semaines 1-2 — Fondations techniques
- Stack : Next.js ISR (pages statiques régénérées) + Postgres (Supabase ou Neon) + cron via Cloudflare Workers
- Provisionner les clés : Google Custom Search, Gemini, Claude
- Crawler propriétaire : Playwright headless + middleware `robots-parser` + queue Redis (Upstash)
- AGENTS.md décrivant le pipeline d'ingestion par modèle
- Sitemap dynamique + IndexNow + soumission GSC

### Semaines 3-4 — Modèle 5 MVP (Arbre Suggest)
- Worker Cloudflare qui requête Suggest avec rate limit 1 req/s
- Récursion arbre niveau 2 sur 1 000 seeds priorisées
- Template de page (UI accordéon + heatmap clustering Gemini)
- 1 000 pages live + sitemap soumis

### Semaines 5-7 — Modèle 1 MVP (Empreinte SERP)
- Pipeline 3 sources (Google Custom Search + Claude API + Gemini API)
- 10 runs par requête sur Claude/Gemini, 1 snapshot Google
- 500 pages pilotes sur des requêtes commerciales B2B
- Refresh hebdo via cron

### Semaines 8-10 — Modèle 2 (Entités SERP)
- Pipeline Custom Search + crawl 10 URLs + extraction Gemini
- 2 000 pages générées
- Cross-linking vers les pages du Modèle 1 (même requête)

### Semaines 11-12 — Modèle 6 (Schema secteur) + audit global
- Constitution liste sites par secteur (50 secteurs pilotes)
- Crawl + extraction JSON-LD
- 50 pages sectorielles live
- Audit GSC global : pages indexées, impressions, clics, conversions CTA, cannibalisation interne

### Pré-requis techniques transverses
- Edge hosting (Cloudflare Pages ou Vercel) pour TTFB < 200 ms
- Schema.org dynamique par modèle :
  - Modèle 1 : `Dataset` schema
  - Modèle 2 : `Dataset` + `DefinedTermSet`
  - Modèle 5 : `ItemList`
  - Modèle 6 : `Dataset` + `Article`
- Open Graph dynamique avec preview image générée serverside
- Monitoring : Plausible + GSC API + Sentry
- Robot interne `OrganikkBot/1.0` documenté sur `organikk.co/bot`

---

## Garde-fous appliqués

- **Anti-thin** : chaque page change >70% du contenu (les chiffres sont les chiffres)
- **Données terrain uniquement** : aucune hallucination, uniquement APIs officielles
- **Sourcing horodaté** : chaque chiffre = endpoint d'origine + date
- **Canonical propre** : 1 URL = 1 dataset = 1 canonical
- **Maillage différenciant** : cross-linking entre modèles sur la même requête (ex : page Empreinte SERP "crm" ↔ page Entités SERP "crm" ↔ page Suggest "crm")
- **Surprise Score** : delta IA vs SERP, gap d'entités, profondeur de l'arbre, adoption sectorielle
- **Grounding Score** : passage ancré méthodologique 150-200 mots + bloc authorship Tim Boussardon ~50 mots sur chaque page

## Conformité légale et éthique

- **Aucun intermédiaire de scraping non autorisé** (DataForSEO, SerpAPI, Bright Data, Apify Google scraper exclus)
- **Robots.txt respecté** sur 100% des crawls cibles
- **APIs officielles uniquement** : Google Custom Search, Gemini, Claude, Google Suggest
- **User-Agent identifiable** sur tous les fetches : `OrganikkBot/1.0 (+https://organikk.co/bot)`
- **Crawl-delay respecté** + délai minimum 5s entre fetches sur un même domaine
- **Aucun contournement** de paywall, captcha, ou protection anti-bot

---

## Anti-cannibalisation

Les 4 modèles couvrent des intentions strictement disjointes :
- 1 : qui rank et qui est cité (sortie de la SERP, comparatif Google/Claude/Gemini)
- 2 : quelles entités sont attendues (entrée éditoriale, brief)
- 5 : que cherchent les gens (recherche utilisateur, longue traîne)
- 6 : quel balisage est adopté (technique, secteur)

Aucun chevauchement de centroïde SERP entre modèles. Cross-linking inter-modèles autorisé sur les requêtes communes pour densifier le maillage interne sans cannibaliser.
