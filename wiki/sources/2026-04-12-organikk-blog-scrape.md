---
type: source
source_type: article
title: Scrape blog Organikk.co — 12 articles (2026-04-12)
aliases: [organikk-blog-scrape, organikk-articles]
tags: [organikk, blog, tim, skills, audit, bootcamp, pseo, bibliotheque-publique]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Scrape blog Organikk.co — 12 articles (2026-04-12)

**Auteur** : Timothée Boussardon (organikk.co/blog)
**Type** : scrape de 12 articles publiés (`source_type: article`)
**Fichier raw** : `raw/data/organikk-blog-scrape-2026-04-12.md`
**Date scrape** : 2026-04-12

---

## Contexte

Inventaire des 12 articles publiés sur organikk.co/blog au 2026-04-12. Fonctionne comme **bibliothèque publique** de Tim : chaque article = version publiée d'un skill ou workflow déjà documenté en interne (cf. [[sources/2026-04-12-tim-skills-seo-proprietary]]). Intérêt pour la KB : source de citation + quelques chiffres nouveaux + structure de liens internes du site.

## Les 12 articles — résumé matriciel

| # | URL | Thème | Connexion KB |
|---|---|---|---|
| 1 | /blog/audit-seo-claude | Audit SEO 7 phases avec Claude | Skill `seo-agent-audit` (défini en config) |
| 2 | /blog/semrush-contenu-ia | SEMrush 42k pages analysées | [[concepts/anti-ai-writing]] + [[concepts/data-proprietaire]] |
| 3 | /blog/grok-seo-pipeline-data | Pipeline Grok 7 use cases | [[concepts/surprise-gap]] + [[concepts/grounding-score]] |
| 4 | /blog/ma-strategie-seo-du-moment | Stratégie 3 blocs + Triade SERP | [[concepts/triade-serp]] |
| 5 | /blog/creer-bot-ia-seo | NotebookLM → Gemini GEM | Skill `brief-contenu` + `entites-vectorielles` |
| 6 | /blog/agent-seo-ia-simple | Premier agent SEO (Claude Projects) | [[sources/2026-04-12-tim-skills-seo-proprietary]] |
| 7 | /blog/roadmap-seo-2026 | Roadmap 2026 en 6 étapes | [[syntheses/workflow-complet-consultant-seo-ia]] |
| 8 | /blog/mots-cles-seo-2026 | Process mots-clés 2026 | Skill `cluster-aeo` + `entites-vectorielles` |
| 9 | /blog/strategie-seo-serrurier-lyon | Étude cas serrurier Lyon | Skill `programmatique-pseo` + `product-led-seo` |
| 10 | /blog/strategie-seo-agence-immobiliere-lyon | Étude cas immo Lyon | Skill `programmatique-pseo` |
| 11 | /blog/analyse-niche-seo | Méthode analyse niche 4 étapes | Skill `quick-win` + `cluster-aeo` |
| 12 | /blog/seo-entreprise-locale | SEO local 3 blocs | Skill `product-led-seo` |

## Chiffres nouveaux à retenir

### Étude SEMrush contenu humain vs IA (article #2)

- **80 % des positions #1 = contenu humain ; 9 % = IA pure**
- Contenu IA **double** entre position 1 et position 4
- Corrélation usage IA ↔ pénalité Google = **0.011** (quasi nulle → pas de pénalité directe systématique)
- Contenu IA **édité** performe à **4 %** du contenu 100 % humain
- Contenu IA **brut** ranke **23 % plus bas** en moyenne
- **Thèse** : *"Ce n'est pas 'IA ou pas IA'. C'est le niveau d'effort éditorial."* Rejoint directement la p.42 QRG (effort-less) — cf. [[sources/2026-04-13-google-quality-raters-guidelines-2026]] et [[concepts/anti-ai-writing]].

### Marché serrurerie France (article #9)

- 80,2 Md€, 139 436 entreprises, 97 % < 10 salariés
- Cas d'école product-led : simulateur coût interactif comme différenciant

## Citations marquantes

> "Aujourd'hui, la moyenne acceptable est générée par l'IA en 30 secondes. Ce n'est plus l'humain qui produit la médiocrité, c'est l'automatisation." — article #4

> "La majorité des problèmes avec l'IA en SEO vient d'un seul endroit : l'IA ne connaît pas votre client." — article #5

## Structure du site (extraite)

Pages principales : /methode · /accompagnement · /accompagnement-seo-geo · /coaching-seo-lyon · /etudes-de-cas · /blog · /bootcamp (+ /bootcamp-candidature) · /a-propos
Outils : /outils/simulateur-roi-seo · /outils/analyse-geo · /glossaire (78 termes cf. [[sources/2026-04-12-organikk-glossaire-scrape]])
Canaux externes : linkedin.com/in/timothee-boussardon · youtube.com/@ethicseo · algorithme.substack.com · cal.com/tim-boussardon-yzrrb1/30min

## Tagline et CTA

**Tagline** : *"Le SEO qui génère des emails qualifiés, pas du trafic."* — alignement doctrine [[concepts/tabou-visibilite]] (on ne vend pas du trafic, on vend des leads).

**CTA récurrents** : "Prendre un call" (toutes pages) · "Voir le bootcamp →" (majorité articles) · "Demander l'audit gratuit" (certains articles).

## Limites

- **Scrape d'un état figé** (2026-04-12) — le site évolue, la source deviendra stale
- **Chiffres SEMrush 42k pages** : non vérifiés indépendamment (étude SEMrush ≠ étude académique peer-reviewed)
- **Études de cas Lyon** présentent une méthodologie mais pas de résultats chiffrés de clients ayant suivi la roadmap

## Implications SEO (meta)

Organikk.co = **le terrain d'application** de la doctrine interne de la KB. Les articles sont à la fois :
1. Contenu commercial (CTA bootcamp)
2. Preuve de méthode (chaque article applique les skills sur un cas concret)
3. Signal d'autorité ([[concepts/e-e-a-t]] Experience + Expertise)

## Pages liées

**Entity** : [[entities/organikk-co]]

**Sources** : [[sources/2026-04-12-organikk-glossaire-scrape]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-13-offre-bootcamp-seo-ia]] · [[sources/2026-04-13-semrush-llm-conversion-study]] (autre étude SEMrush — complémentaire sur conversion LLM)

**Concepts** : [[concepts/anti-ai-writing]] · [[concepts/data-proprietaire]] · [[concepts/triade-serp]] · [[concepts/tabou-visibilite]]
