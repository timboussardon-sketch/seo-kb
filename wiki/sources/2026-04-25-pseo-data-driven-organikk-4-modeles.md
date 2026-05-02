---
type: source
source_type: doctrine
title: "pSEO data-driven Organikk — 4 modèles validés (Empreinte SERP / Entités / Suggest / Schema)"
aliases: [pseo-data-driven-organikk, organikk-4-modeles-pseo]
tags: [doctrine-tim, organikk, pseo, data-driven, empreinte-serp, suggest, schema-org, conformite]
created: 2026-04-25
updated: 2026-04-25
sources: 1
confidence: high
status: stable
---

# pSEO data-driven pour organikk.co — 4 modèles validés

**Type** : extension pSEO du cluster Organikk — 4 modèles de pages programmatiques **avec zéro réécriture humaine** et stack 100 % conforme APIs officielles.
**Auteur** : Tim · **Fichier raw** : `raw/notes/2026-04-25-pseo-data-driven-organikk-cursor.md`
**Date** : 2026-04-25

## Principe directeur

Chaque modèle suit la règle **template fixe + dataset structuré = N pages organiques uniques**. La valeur vient des **chiffres eux-mêmes**, pas du commentaire éditorial.

**Stack autorisé** : Google Custom Search JSON API · Gemini API · Claude API (avec tool `web_search`) · Google Suggest endpoint · crawl propriétaire avec respect strict des `robots.txt`.

**Stack interdit** : SerpAPI, DataForSEO, Bright Data, Apify Google Search Scraper, et tout intermédiaire qui contourne le `Disallow: /search` de Google.

## Modèle 1 — Empreinte SERP (Google vs Claude vs Gemini)

- **URL** : `organikk.co/empreinte-serp/[slug-requête]`
- **Volume** : 5 000 à 50 000 pages
- **Mécanique** : 3 sources en parallèle (Google Custom Search + 10 runs Claude + 10 runs Gemini avec température 0.7)
- **Fréquence d'apparition** par domaine sur 10 runs → calcul du chevauchement
- **Bloc clé** : graphe de Venn des 3 sources + score de chevauchement + domaines exclusifs (le delta exploitable)
- **Coûts MVP 1 000 pages** : ~195 € initial, refresh hebdo ~800 €/mois
- **Score priorité** : 9/10 — asset signature, format quasi-vide en français

## Modèle 2 — Entités SERP (centroïde sémantique attendu)

- **URL** : `organikk.co/entites-serp/[slug-requête]`
- **Volume** : 10 000+ pages
- **Mécanique** : Custom Search (10 URLs ranking) → crawl Playwright respecte robots.txt → extraction entités via Gemini (4 catégories : techniques / preuves quantitatives / multimodal / divergence) → centroïde SERP (entités présentes ≥ 6/10) + gap exploitable (5-7/10 mais absente du #1)
- **Coûts MVP 1 000 pages** : ~85 € initial, refresh trimestriel ~30 €/mois
- **Score priorité** : 8.5/10

## Modèle 5 — Arbre Google Suggest

- **URL** : `organikk.co/suggest-google/[slug-requête]`
- **Volume** : 20 000+ pages
- **Mécanique** : récursion sur l'endpoint `suggestqueries.google.com/complete/search` (autorisé, utilisé par les navigateurs). Niveau 0 (seed), niveau 1 (a-z + 0-9 → ~36 calls), niveau 2 (~13 000 calls → ~5 000 suggestions uniques), niveau 3 optionnel
- **Rate limit strict** : 1 req/seconde max, multi-IP propres, User-Agent identifiable `OrganikkBot-Suggest/1.0`
- **Bloc clé** : arbre déroulant + clustering par préfixe interrogatif (comment/pourquoi/quel/quand/combien) + heatmap thèmes via Gemini + suggestions négatives (frictions)
- **Coûts MVP** : ~35 €/mois (Suggest gratuit, infra queue Cloudflare Worker + Redis)
- **Score priorité** : 8/10 — modèle à lancer en premier (validation rapide stack pSEO)

## Modèle 6 — Adoption Schema.org par secteur

- **URL** : `organikk.co/schema-secteur/[slug-secteur]`
- **Volume** : 200 à 500 pages (1 par secteur NACE/SIRET/verticale)
- **Mécanique** : sample 200-500 sites du secteur (Société.com, OpenCorporates) → crawl avec respect `robots.txt` → extraction JSON-LD home + 5 pages internes → catégorisation (Organization, LocalBusiness, Product, FAQPage, etc.) → croisement présence Rich Results
- **Bloc clé** : % d'adoption par schema + top 10 sites les plus structurés + exemples JSON-LD réels + erreurs fréquentes + corrélation Schema ↔ volume organique
- **Coûts MVP 200 secteurs** : ~150 € one-shot crawl + ~25 €/mois stockage refresh semestriel
- **Score priorité** : 7/10

## Matrice de priorisation finale

| Modèle | Pages | Effort | Coût/mois | Impact SEO | Conversion | Score |
|---|---|---|---|---|---|---|
| 1. Empreinte SERP | 5K–50K | Élevé | ~800 € | Très haut | Très haut | **9/10** |
| 2. Entités SERP | 10K+ | Moyen | ~30 € | Haut | Haut | **8.5/10** |
| 5. Arbre Suggest | 20K+ | Faible | ~35 € | Haut | Moyen | **8/10** |
| 6. Schema secteur | 200–500 | Élevé | ~25 € | Moyen | Haut | **7/10** |

- **Modèle à lancer en premier** : Modèle 5 (Arbre Suggest) — coût bas, mécanique simple
- **Modèle pilier 12 mois** : Modèle 1 (Empreinte SERP) — asset signature

## Plan d'exécution 90 jours

- **S1-2** : fondations techniques (Next.js ISR + Postgres Supabase/Neon + cron Cloudflare Workers + crawler Playwright + sitemap dynamique + IndexNow + GSC)
- **S3-4** : Modèle 5 MVP (Arbre Suggest) — 1 000 pages live
- **S5-7** : Modèle 1 MVP (Empreinte SERP) — 500 pages pilotes commerciales B2B + refresh hebdo cron
- **S8-10** : Modèle 2 (Entités SERP) — 2 000 pages + cross-linking vers Modèle 1
- **S11-12** : Modèle 6 (Schema secteur) — 50 secteurs pilotes + audit GSC global

## Garde-fous appliqués (7)

1. Anti-thin (>70 % du contenu change)
2. Données terrain uniquement (zéro hallucination, APIs officielles)
3. Sourcing horodaté (chaque chiffre = endpoint d'origine + date)
4. Canonical propre (1 URL = 1 dataset = 1 canonical)
5. Maillage différenciant (cross-linking inter-modèles sur même requête)
6. Surprise Score (delta IA vs SERP, gap d'entités, profondeur arbre, adoption sectorielle)
7. Grounding Score (passage ancré méthodologique 150-200 mots + bloc authorship Tim ~50 mots)

## Anti-cannibalisation

Les 4 modèles couvrent des **intentions disjointes** :
- 1 : qui rank et qui est cité (sortie SERP, comparatif)
- 2 : quelles entités sont attendues (entrée éditoriale)
- 5 : que cherchent les gens (recherche utilisateur, longue traîne)
- 6 : quel balisage est adopté (technique, secteur)

Aucun chevauchement de centroïde SERP. Cross-linking inter-modèles autorisé pour densifier le maillage interne sans cannibaliser.

## Apports à la KB

- 4 nouveaux **modèles pSEO data-driven** opérationnels, conformes APIs officielles → matérialise les 7 règles de [[concepts/programmatique-pseo]]
- Concept candidat : `pseo-data-driven-models` (4 modèles documentés ici)
- Stack interdit explicite (SerpAPI, DataForSEO, Bright Data, Apify Google) — précision juridique nouvelle dans la doctrine
- Compatible avec l'architecture cluster ([[sources/2026-04-24-cluster-business-organikk-4-piliers]]) — chaque modèle pSEO peut alimenter un sous-pilier
- Argument vente direct : "à 195 € MVP / 800 € mois Modèle 1, on parle d'un asset défendable face à toute agence pSEO 'spammy'"

## Limites

- 4 modèles **non encore implémentés** au 2026-04-25 — c'est un plan
- Coûts estimés sans validation réelle (potentiel sur-/sous-estimation)
- Modèle 1 dépend fortement de la stabilité tarifaire APIs Claude/Gemini grounding
- Pas de mesure post-déploiement

## Pages liées

[[sources/2026-04-24-reflexion-organikk-4-piliers]] · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] · [[sources/2026-04-13-prompt-pseo-produit-service]] · [[sources/2026-04-13-prompt-pseo-non-produit]] · [[concepts/programmatique-pseo]] · [[concepts/data-proprietaire]] · [[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[entities/organikk-co]] · [[entities/chatgpt-search]] · [[entities/perplexity]] · [[entities/google-ai-mode]]
