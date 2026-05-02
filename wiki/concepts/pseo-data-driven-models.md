---
type: concept
title: "pSEO data-driven — 4 modèles (Empreinte SERP, Entités SERP, Suggest, Schema secteur)"
aliases: [pseo-data-driven-models, 4-modeles-pseo, modeles-pseo-organikk]
tags: [doctrine-tim, pseo, data-driven, conformite, apis-officielles, anti-thin]
created: 2026-05-01
updated: 2026-05-01
sources: 1
confidence: high
status: stable
---

# pSEO data-driven — 4 modèles

Catalogue de **4 modèles pSEO conformes** où la valeur des pages vient des **chiffres eux-mêmes** (pas du commentaire éditorial). Stack 100 % APIs officielles, zéro réécriture humaine, zéro intermédiaire de scraping non autorisé.

## Stack autorisé / interdit

**Autorisé** : Google Custom Search JSON API · Gemini API · Claude API (avec tool `web_search`) · Google Suggest endpoint · crawl propriétaire avec respect strict des `robots.txt`.

**Interdit** : SerpAPI · DataForSEO · Bright Data · Apify Google Search Scraper · tout intermédiaire qui contourne le `Disallow: /search` de Google.

## Les 4 modèles

| # | Modèle | Variable | Volume | Score |
|---|---|---|---|---|
| 1 | **Empreinte SERP** (Google vs Claude vs Gemini) | requête | 5K–50K pages | 9/10 |
| 2 | **Entités SERP** (centroïde sémantique attendu) | requête | 10K+ pages | 8.5/10 |
| 5 | **Arbre Google Suggest** | seed (mot-clé head) | 20K+ pages | 8/10 |
| 6 | **Adoption Schema.org par secteur** | secteur | 200–500 pages | 7/10 |

## Pourquoi 4 modèles (et pas 1)

Les 4 modèles couvrent des **intentions strictement disjointes** (anti-cannibalisation) :
- 1 : qui rank et qui est cité (sortie de la SERP, comparatif)
- 2 : quelles entités sont attendues (entrée éditoriale)
- 5 : que cherchent les gens (recherche utilisateur, longue traîne)
- 6 : quel balisage est adopté (technique, secteur)

Cross-linking inter-modèles autorisé sur les requêtes communes (ex : page Empreinte SERP "crm" ↔ page Entités SERP "crm" ↔ page Suggest "crm") pour densifier le maillage interne sans cannibaliser.

## Garde-fous appliqués (les 7 règles + anti-thin)

1. **Anti-thin** : >70 % du contenu change entre pages (les chiffres sont les chiffres)
2. **Données terrain uniquement** : zéro hallucination, APIs officielles
3. **Sourcing horodaté** : chaque chiffre = endpoint d'origine + date
4. **Canonical propre** : 1 URL = 1 dataset = 1 canonical
5. **Maillage différenciant** : cross-linking inter-modèles
6. **Surprise Score** : delta IA vs SERP, gap d'entités, profondeur arbre, adoption sectorielle
7. **Grounding Score** : passage ancré méthodologique 150-200 mots + bloc authorship Tim ~50 mots sur chaque page

Cohérent avec les 7 règles non-négociables de [[concepts/programmatique-pseo]].

## Compatibilité avec le cluster Organikk

Chaque modèle pSEO peut alimenter un sous-pilier du cluster ([[sources/2026-04-24-cluster-business-organikk-4-piliers]]) :
- Modèle 1 (Empreinte SERP) → axe AEO (qui est cité par les LLM)
- Modèle 2 (Entités SERP) → axe Grounding Score (centroïde sémantique)
- Modèle 5 (Suggest) → axe Surprise Gap (longue traîne, suggestions négatives = frictions)
- Modèle 6 (Schema secteur) → axe pSEO (technique, structure)

## Coûts MVP (1 000 pages)

| Modèle | Coût initial | Coût mensuel |
|---|---|---|
| 1. Empreinte SERP | ~195 € | ~800 € (refresh hebdo) |
| 2. Entités SERP | ~85 € | ~30 € (refresh trimestriel) |
| 5. Arbre Suggest | gratuit (Suggest) + ~30 €/mois infra | ~35 €/mois |
| 6. Schema secteur | ~150 € (200 secteurs) | ~25 €/mois |

**Modèle à lancer en premier** : Modèle 5 (Arbre Suggest) — coût bas, mécanique simple, validation rapide stack pSEO en 2-3 semaines.
**Modèle pilier 12 mois** : Modèle 1 (Empreinte SERP) — asset signature Organikk, donnée qui s'accumule, format quasi-vide en français.

## Bot identifiable (conformité)

User-Agent identifiable sur tous les fetches : `OrganikkBot/1.0 (+https://organikk.co/bot)`. Crawl-delay respecté + délai minimum 5s entre fetches sur un même domaine. Aucun contournement de paywall, captcha ou protection anti-bot.

## Pages liées

[[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] · [[concepts/programmatique-pseo]] · [[concepts/data-proprietaire]] · [[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/maillage-systeme]] · [[concepts/test-substitution-llm]] · [[entities/organikk-co]] · [[entities/chatgpt-search]] · [[entities/perplexity]] · [[entities/google-ai-mode]]
