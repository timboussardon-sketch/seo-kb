---
title: "Cadrage Newsletter Trends : Fusionn.co"
projet: fusionn
type: cadrage-strategique
created: 2026-05-27
status: draft, à valider avec Tim avant code
sources-data: [Google Trends (pytrends), Reddit JSON API, Hacker News Algolia, ProductHunt GraphQL]
related:
  - "[[Suivi-Projet]]"
  - "[[Diagnostic-plan-action-2026-05-26]]"
  - "[[Historique]]"
---

# Newsletter Trends Fusionn : cadrage

Doc de cadrage stratégique pour la newsletter quotidienne adossée à Fusionn.co, qui agrège les mots-clés SEO/IA et les secteurs en train d'exploser. À valider point par point avant de coder.

## 1. Promesse

**Une newsletter quotidienne qui dit aux SEO pros sur quels mots-clés sauter cette semaine.**

Pas une revue d'actu. Pas une opinion. De la data agrégée depuis 4 sources publiques (Google Trends, Reddit, Hacker News, ProductHunt), filtrée, scorée, et présentée en moins de 3 minutes de lecture. Chaque trend retenu pointe vers Fusionn pour cadrer la stratégie SEO autour.

Audience cible : consultants SEO indépendants, agences, founders B2B qui veulent voir les opportunités avant les autres. Niveau attendu : ils savent ce qu'est un mot-clé décisionnel et un cluster.

## 2. Pourquoi maintenant pour Fusionn

État Fusionn au 2026-05-26 (cf. [[Diagnostic-plan-action-2026-05-26]]) :
- MRR 696 €, acquisition à l'arrêt (0 inscrit sur 7j)
- Top-funnel cassé, plus de stratégie d'attraction organique
- 46 % s'inscrivent sans chercher → besoin de **chauffer** l'audience avant qu'elle hit le produit

La newsletter répond directement à ce diagnostic : elle alimente le top-funnel avec une audience pré-qualifiée (SEO pros), elle chauffe par exposition répétée, et chaque édition ramène vers une fonctionnalité concrète de Fusionn. C'est un canal d'acquisition réutilisable sur 18 mois.

## 3. Différenciation

| Existant | Angle | Cible | Différenciation Newsletter Fusionn |
|---|---|---|---|
| [[Algorithme]] (newsletter Tim) | Curation d'expert sur l'actu SEO/IA, opinions tranchées, fond | Audience perso Tim (LinkedIn, abonnés) | Newsletter Fusionn = **data brute**, pas d'opinion, agrégation. Branding Fusionn, pas Tim. |
| Exploding Topics | Trends business toutes verticales, paywall 39$/mois | Entrepreneurs en quête de niches | Newsletter Fusionn = **niche SEO/IA only**, gratuit, sourcé public |
| Ahrefs Newsletter | Best-of d'articles SEO de la semaine | Tout SEO | Newsletter Fusionn = **temps réel** (J-1), pas du best-of statique |
| Search Engine Land | Actus du jour rédigées | Tout SEO | Newsletter Fusionn = **agrégation algorithmique**, pas d'éditorialisation longue |

**Ligne éditoriale tranchée** : si une trend est déjà dans Search Engine Journal hier, on ne la sort pas. La valeur est d'être le premier à signaler une niche qui monte.

## 4. Sources et extraction

### 4.1 Google Trends · via pytrends

- **Méthode** : `pytrends.request.TrendReq` (lib Python non-officielle, gratuite). Méthodes utiles : `related_queries(keyword)['rising']` qui retourne les requêtes liées qui montent (% gain vs période).
- **Seeds SEO/IA** (≈30) : `SEO`, `AI Overview`, `ChatGPT`, `Claude`, `Gemini`, `Perplexity`, `GEO consultant`, `generative engine`, `schema markup`, `topical authority`, `programmatic SEO`, `LLM SEO`, `AEO`, `search console`, `Google Search`, `pSEO`, `RAG`, `agentic search`, etc. Liste à figer dans `config/trends-seeds.json`.
- **Critère "explose"** : `rising > +150%` ET volume absolu > 100 (sinon trop bruyant).
- **Rate limit** : ~10-20 req/min avant HTTP 429. Solution : exponential backoff + rotation User-Agent + cache 24h.
- **Pays** : France + global. Deux passes (FR-FR puis global), tag de provenance dans le digest.

### 4.2 Reddit · via API JSON publique

- **Endpoint** : `https://www.reddit.com/r/<sub>/top.json?t=day&limit=25` (pas d'auth requise pour le read public).
- **Subreddits cibles** :
  - r/SEO (520k), r/bigseo (115k), r/TechSEO (15k)
  - r/Anthropic, r/OpenAI, r/LocalLLaMA, r/MachineLearning, r/PromptEngineering
  - r/marketing, r/digital_marketing, r/SaaS (filtre sur sujets SEO/IA)
- **Métriques** : `score` (upvotes), `num_comments`, `upvote_ratio`, `created_utc`. Momentum = `score / max(age_hours, 1) * upvote_ratio`.
- **Détection "qui explose"** : croiser `top?t=day` vs `top?t=week` : posts qui apparaissent dans `day` mais pas en haut de `week` = signal frais.
- **⚠️ Cas Fusionn** : le serveur Fusionn lui-même est bloqué par Reddit côté Edge Functions Supabase (IP datacenter, cf. [[Suivi-Projet]] feat YouTube/Reddit). Pour la newsletter, l'extraction tourne ailleurs (GH Action, IP différentes), donc à priori OK. Si rebond : fallback API OAuth client_credentials (gratuit, app installée, 100 req/min).
- **Anti-bruit** : filtre posts < 50 upvotes, ratio comments/upvotes < 0,02 (signaux engagement faible), flairs `Question`/`Help` exclus.

### 4.3 Hacker News · via Algolia API

- **Endpoint** : `https://hn.algolia.com/api/v1/search?tags=front_page&numericFilters=created_at_i>{ts_24h}` + filtres `query=AI|LLM|SEO|search`.
- **Pas d'auth**, fair use, rate très large.
- **Métriques** : `points`, `num_comments`, `created_at_i`. Momentum = même formule que Reddit.
- **Filtre éditorial** : retenir seulement les stories `points > 100` ET au moins un mot du dico `[AI, LLM, GPT, Claude, Gemini, search, SEO, RAG, embedding, retrieval]` dans le titre.

### 4.4 ProductHunt · via API GraphQL v2

- **Endpoint** : `https://api.producthunt.com/v2/api/graphql`, OAuth developer token (gratuit, 6000 req/h).
- **Query** : `posts(featured: true, order: VOTES, postedAfter: today)` filtrés par topics `Artificial Intelligence`, `SEO`, `Marketing automation`, `Productivity`.
- **Métriques** : `votesCount`, `commentsCount`, `topics`, `tagline`, `description`.
- **Critère** : top 10 launches du jour ayant au moins un topic dans la whitelist.

## 5. Pipeline (5 étapes)

Cohérent avec le pattern `revue-presse-quotidienne` (skill qui fait tourner Algorithme), adapté trends.

1. **Scan** : tirer brut depuis les 4 sources en parallèle (Promise.all, timeout 30s par source). Stocker en JSON daté dans `data/scans/{YYYY-MM-DD}.json`. Fail-soft : si une source plante, le pipeline continue avec les autres et flagge l'incident en bas du digest.

2. **Normalisation** : chaque entrée brute devient un objet uniforme :
   ```ts
   type TrendItem = {
     source: 'gtrends' | 'reddit' | 'hn' | 'ph';
     label: string;            // mot-clé ou titre
     url: string;
     captured_at: string;      // ISO
     metrics: Record<string, number>;
     raw_score: number;        // métrique native
     momentum: number;         // métrique calculée
     category: 'keyword' | 'discussion' | 'launch' | 'paper';
   };
   ```

3. **Scoring** : calculer un `MomentumScore` global = pondération des metrics + Freshness Guard (entrée > 7j out) + Confidence Score (combien de signaux corroborent dans les 4 sources). Une trend qui apparaît dans 2 sources le même jour passe en top, c'est le signal le plus fort.

4. **Filtrage et éditorialisation** :
   - Deduplication (sémantique, pas exacte : "AI Overview" et "Google AI Overview" sont fusionnés)
   - Anti-redondance Algorithme : si l'item est déjà sorti dans Algorithme ces 7 derniers jours, écarter ou flagger
   - Anti-bruit : règles spécifiques par source (cf. section 4)
   - Sélection top N par catégorie : 5 trends Google Trends, 3 posts Reddit, 2 stories HN, 2 launches ProductHunt

5. **Rédaction** : Gemini (ou Claude via SDK) rédige le digest avec ton-de-voix-tim pour le copy bridge entre items, intègre les CTA Fusionn (deep links), génère titre + preview email, output Markdown. Output dans `out/newsletters/{YYYY-MM-DD}.md`.

## 6. Format de sortie (template du digest)

```markdown
# Trends SEO/IA · [JJ mois AAAA]

> Lecture 3 min. Édition #[N]. [12 sources scannées ce matin à 7h.]

## 🚀 Mots-clés qui montent sur Google

**1. `gpt store agents` · +340 % sur 7 jours**
Pourquoi maintenant : la sortie publique de la marketplace Agents d'OpenAI a déclenché une vague de recherche "comment publier un agent". Volume absolu encore bas, fenêtre courte.
À cibler pour : agences IA, devs freelance, formateurs.
→ [Cadrer une stratégie sur ce mot-clé dans Fusionn](https://fusionn.co/score-semantique?keyword=gpt+store+agents)

**2. `GEO consultant` · +180 %**
[...]

## 💬 Ce dont les SEO pros parlent (Reddit)

**r/SEO · 412 upvotes · 89 commentaires**
"Google AI Overviews mange 23 % de mon trafic sur les requêtes informationnelles, voici ce qui reste"
Résumé : retour d'expérience sur 6 mois de chute SGE, stratégies qui ont compensé.
[Lire le post](https://reddit.com/r/SEO/...)

## 🛠 Outils SEO/IA lancés hier

**Topical Map AI · ProductHunt #3 du jour · 247 votes**
[Description courte + lien]

## 📰 Le débat technique du moment (Hacker News)

**Front page · 412 points**
"Show HN: I built a semantic SEO tool using GPT-4 embeddings"
Discussion vive sur la viabilité des embeddings pour le clustering de mots-clés.
[Voir la discussion](https://news.ycombinator.com/...)

---

*Cette édition est gratuite. Pour aller plus loin sur les mots-clés ci-dessus, [Fusionn](https://fusionn.co) construit la stratégie complète en 5 minutes.*

*Méthodologie : agrégation quotidienne de 4 sources publiques (Google Trends, Reddit, HN, ProductHunt), filtrage anti-bruit, scoring par momentum. [Détails de la méthode](https://fusionn.co/newsletter/methode)*

*[Se désabonner] · [Voir l'archive]*
```

## 7. Intégration produit Fusionn

C'est le levier qui transforme la newsletter en outil d'acquisition, pas juste en média.

- **CTA par trend** : chaque mot-clé "qui explose" a un lien deep `https://fusionn.co/score-semantique?keyword={url-encoded}`. Quand le lecteur clique, il atterrit dans le workspace Fusionn avec le mot-clé pré-rempli, prêt à générer un brief.
- **Tracking** : utm tags `utm_source=newsletter-trends&utm_campaign={date}&utm_term={trend-slug}` pour mesurer la conversion en base.
- **Onboarding différencié** : si l'utilisateur s'inscrit après un clic newsletter (cookie / param), bypass de l'écran "exemple" et atterrissage direct sur la recherche du mot-clé qu'il avait cliqué. Casse 2 frictions d'un coup.
- **Boucle preuves** : remonter dans la fiche preuve de chaque édition (cf. doctrine seo-kb) le nombre de clics → inscriptions → générations de brief → abonnement.

## 8. Architecture technique (à trancher)

**3 options évaluées :**

| Option | Comment | Pro | Con |
|---|---|---|---|
| A. Tout sur fusionn.co | Route `/newsletter`, route `/newsletter/[slug]`, Edge Function `generate-daily-trends`, envoi via Resend depuis Supabase | Contrôle total, archive indexable SEO sur fusionn.co, blog grossit, branding pur | Plus de dev (gestion abonnés, opt-in, désabo RGPD, template HTML emails) |
| B. Substack / Beehiiv | GH Action génère MD, push via API tierce | Zero plomberie, audience portable | Pas d'indexation SEO sur fusionn.co, dépendance plateforme, branding mixte |
| C. Hybride (recommandé) | GH Action → MD dans `~/Code/newFusionn/src/content/newsletter/` → build statique sur `fusionn.co/newsletter/[date]` ; envoi via Loops.so depuis Supabase | SEO + envoi avec contrôle, infra existante réutilisée | 1 sprint dev pour wiring Loops + emails transactionnels |

**Recommandation : Option C.**

Justification :
- Le diag Fusionn dit "top-funnel cassé". Indexer chaque édition sur fusionn.co/newsletter/[date] crée 200+ pages SEO/an, alimente le maillage interne, et ramène du trafic organique sur les recherches `[mot-clé] trend` ou `[mot-clé] tendance`.
- Loops.so est leader sur le segment SaaS B2B SEO friendly, intégration Supabase via webhook, prix raisonnable (49 $/mois après 1000 abonnés).
- Réutilise le pattern Fusionn déjà en place : Edge Function + Gemini + push HTML.

**Détail technique option C** :
- **Cron** : GitHub Action `daily-trends.yml`, schedule `0 5 * * 1-5` UTC (7h Paris lun-ven).
- **Script** : Node ou Python dans `~/Code/newFusionn/scripts/generate-trends.{js,py}`.
- **Sortie** :
  - `src/content/newsletter/[YYYY-MM-DD].md` (commité auto par bot)
  - POST vers Loops.so `/v1/transactional` avec template ID et payload variables
- **Pages générées** : `/newsletter` (liste paginée), `/newsletter/[slug]` (édition), `/newsletter/methode` (page méthodologie SEO friendly), `/newsletter/inscription` (form opt-in double).
- **Stockage abonnés** : table `newsletter_subscribers` sur Supabase, RGPD compliant, double opt-in via Resend transactional.

## 9. Cadence et lifecycle

- **Quotidien lundi-vendredi**, envoi à 7h Paris. Pas le weekend (data Reddit/HN moins éditorialisable, audience B2B absente).
- **Édition spéciale dimanche** (V2 plus tard) : best-of de la semaine, format plus long, vrai SEO sur fusionn.co (1000 mots, optimisé pour `[meta-niche] tendances semaine`).
- **Archivage** : chaque édition reste indexée sur `/newsletter/[date]` ad vitam, lien dans la base de donnée du knowledge graph Fusionn.

## 10. KPIs et boucle preuves

KPIs à mesurer dès le sprint 2 :
- Inscrits / semaine (objectif M+1 : 50, M+2 : 200, M+3 : 500)
- Open rate (benchmark Loops B2B SaaS : 35-45 %)
- CTR vers fusionn.co (benchmark : 4-7 %)
- Conversion newsletter inscription → inscription Fusionn (objectif : 5 %)
- Conversion inscription Fusionn → MRR (objectif boucle complète : 1 % des abonnés newsletter deviennent payants à M+6)

Boucle preuves : à chaque jalon (M+1, M+3, M+6) une fiche preuve dans seo-kb/fusionn/ qui confronte les chiffres aux objectifs, mesure le coût acquisition vs LTV.

## 11. Phasage MVP → V1 → V2

**Sprint 0 (cette semaine, 1 journée)**
Skill local `fusionn-trends-quotidien` dans `~/.claude/skills/fusionn-trends-quotidien/SKILL.md`. Tim le lance à la main chaque matin, relit, poste sur LinkedIn pour tester l'angle et la rédaction. Pas d'envoi email. Pas d'archive site. Objectif : valider l'angle éditorial AVANT de coder l'infra.

**Sprint 1 (S+1, 3 jours)**
- GH Action cron 7h, agrégation 4 sources, génération MD
- Route `/newsletter` + `/newsletter/[slug]` sur fusionn.co (build statique)
- Formulaire inscription double opt-in, table Supabase
- Pas encore d'envoi auto

**Sprint 2 (S+2, 3 jours)**
- Wiring Loops.so : sync abonnés Supabase ↔ Loops, envoi auto trigger après build
- Template HTML email, désabonnement
- Analytics open / CTR via Loops + Plausible

**Sprint 3 (S+3, 2 jours)**
- Boucle preuves : reporting hebdo automatique dans seo-kb
- A/B test 2 angles éditoriaux pour optim open rate
- Indexation des éditions sur sitemap, balisage Schema NewsArticle

## 12. Risques et pièges

| Risque | Probabilité | Mitigation |
|---|---|---|
| Redondance avec Algorithme | Moyenne | Différencier strictement : Algorithme = expert + opinion, Newsletter Fusionn = data + agrégation. Pas de signature Tim sur les éditions Fusionn. |
| Rate limit Google Trends | Élevée | Cache 24h, fallback exponential backoff, dégradation graceful si 429 (le pipeline continue avec 3 sources) |
| Pollution Reddit | Élevée | Filtre score + ratio engagement + flairs exclus. Audit manuel mensuel des subreddits. |
| Anti-spam emails au démarrage | Élevée | Resend / Loops avec warm-up IP, double opt-in obligatoire, désabo 1 clic |
| Surprise Score nul (trends banales) | Moyenne | Critère explicite : retenir seulement les trends qu'un SEO senior n'aurait pas vues. Audit mensuel sur 10 éditions au hasard. |
| Charge dev Fusionn vs roadmap activation | Élevée | Bien séquencer : sprint 0 valide l'angle SANS toucher au code Fusionn. Si l'angle ne prend pas en 2 semaines, on arrête. |

## 13. Décisions à prendre avant code

1. **Hosting** : on valide l'Option C hybride ?
2. **Nom de la newsletter** : différencier d'Algorithme. Proposition : `Trends · Fusionn` ou `Le tableau de bord SEO/IA` ou autre. À trancher.
3. **Cadence** : 5j/7 (lun-ven 7h) confirmé ? Édition dimanche en V2 ?
4. **Outil d'envoi** : Loops.so vs Resend vs Brevo vs autre ? Recommandation Loops pour la simplicité SaaS B2B + intégration Supabase.
5. **Signature** : "L'équipe Fusionn" ou nom de Tim ? Recommandation : `L'équipe Fusionn`, garder Tim pour Algorithme.
6. **CTA produit** : deep link `/score-semantique?keyword=X` sur chaque trend ? Ou plus subtil (CTA général en bas) ? Recommandation : deep link strict, c'est la valeur ajoutée vs un Substack lambda.
7. **Cible** : prospects froids (volume, large funnel) ou audience pré-qualifiée (déjà clients ou warm) ? Recommandation : froids, c'est le diag qui le demande.
8. **Sprint 0** : on lance le skill local cette semaine pour tester l'angle ?

## 14. Prochaines étapes (si validé)

1. Tim tranche les 8 points ci-dessus
2. Si feu vert : sprint 0 lancé, je code le skill local `fusionn-trends-quotidien`, premier digest généré dans 24-48h
3. Tim relit, poste un échantillon sur LinkedIn, mesure l'engagement
4. Si engagement OK, sprint 1 démarre (infra fusionn.co)
5. Tracker hebdo dans [[Historique]] de Fusionn pour suivre la cadence et les KPIs
