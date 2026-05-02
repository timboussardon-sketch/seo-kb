---
type: source
source_type: doctrine
title: "Tim posts LinkedIn — batch 11 fichiers (idées + posts publiés)"
aliases: [tim-posts-linkedin-batch, posts-linkedin-batch]
tags: [linkedin, posts, batch, tim, type-A, retour-terrain, vente, anti-ai-writing]
created: 2026-04-30
updated: 2026-05-01
sources: 1
confidence: high
status: stable
---

# Tim posts LinkedIn — batch 11 fichiers

**Type** : ingestion batch des 11 posts LinkedIn de Tim (idées et posts publiés) — corpus de référence pour le format LinkedIn Tim et le **pattern signature "Type A" (retour terrain factuel)**.
**Fichiers raw** : `raw/articles/posts-linkedin/` (11 fichiers)
**Date** : 2026-04-30

## Inventaire

| Fichier | Type | Sujet |
|---|---|---|
| `idees-posts-linkedin-type-A.md` | Idées | 8 idées de posts pattern "J'ai fait X. Voici ce qui s'est passé." |
| `linkedin-trend-research-SEO-LLM-semaine-2-avril-2026.md` | Veille | Tendances SEO/LLM mi-avril 2026 |
| `linkedin-trend-research-semaine-2-avril-2026.md` | Veille | Tendances générales mi-avril 2026 |
| `post-linkedin-audit-sans-semrush.md` | Publié | Remplacer Semrush par Claude (120€ → 20€) |
| `post-linkedin-episode-2-site-claude.md` | Publié | Lancer un site avec Claude — épisode 2 |
| `post-linkedin-grok-seo.md` | Publié | Grok + SEO pour la recherche de data |
| `post-linkedin-linkedin-source-ia.md` | Publié | LinkedIn 2e source citée par les IA |
| `post-linkedin-mots-cles-llm.md` | Publié | Mots-clés LLM (24 mots vs 4 mots Google) |
| `post-linkedin-role-seo-claude.md` | Publié | Rôle de Claude dans le SEO |
| `post-linkedin-seo-kb-obsidian.md` | Publié | Knowledge base SEO sur Obsidian + Claude |
| `post-linkedin-surprise-score-workflow.md` | Publié | Surprise Score + workflow propriétaire |

## Pattern dominant — "Type A : J'ai fait X"

Les 8 idées documentées dans `idees-posts-linkedin-type-A.md` partagent un canevas :
- **Hook** : "J'ai fait/remplacé/construit/lancé [X]"
- **Setup** : ce que tu as fait (1 phrase factuelle)
- **Angle** : la leçon / différenciation
- **Données** : 2-3 chiffres concrets

Exemples :
1. "J'ai remplacé Semrush par Claude. 120€/mois → 20€."
2. "J'ai construit Fusionn. Gratuit."
3. "J'ai créé un système pSEO qui génère 150 pages à partir de 5 templates. Pour un client formation."
4. "J'ai fait passer mon taux de closing de 10 % à 50 % en changeant une chose dans mes calls de vente."
5. "Un client a reçu 3 demandes de démo via ChatGPT. Son site fait 1000 visites/mois."
6. "J'ai documenté 8 calls clients. Et j'en ai tiré tout mon contenu SEO."
7. "J'ai lancé un bootcamp SEO + Claude. 8 places. Rempli en X jours."
8. "J'ai testé le prompt 'Écris un article sur [sujet]' vs mon workflow en 8 étapes. Comparaison."

## Post signature — "Surprise Score + Workflow propriétaire"

Verbatim ouverture :
> "Tu utilises l'IA pour rédiger. Mais tu recommences de zéro à chaque contenu. Pas de process. Quelques prompts par-ci par-là. Et à chaque article tu te demandes : 'On en était où la semaine dernière ?' Résultat : tu rédiges avec les mêmes données que tout le monde. Surprise Score = 0."

Verbatim closing :
> "Aujourd'hui Claude permet une chose qu'aucun autre LLM ne fait aussi bien : construire ton workflow propriétaire. 80 % fixe, 20 % adaptable par client. Tu capitalises sur chaque expérience au lieu de repartir de zéro. C'est la fin du SEO des petits hacks. Et c'est tant mieux."

→ Cohérent avec [[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]] (closing pattern "C'est la fin de X. Et c'est tant mieux.")

## 5 types de data propriétaire (formalisés dans le post Surprise Score)

1. Le **cas client chiffré** ("40 % de réduction du cycle de vente")
2. La **réflexion originale** (si quelqu'un qui n'a jamais fait ton métier ne peut pas l'écrire, c'est propriétaire)
3. La **méthodologie documentée** (pas "on est humain et personnalisé")
4. L'**outil interactif** (simulateur, calculateur, quiz)
5. Les **signaux sociaux** (Perplexity, Reddit, Grok)

→ Cohérent avec [[concepts/data-proprietaire]] (déjà 19 sources, +1 source convergente)

## Post "LinkedIn 2e source IA"

Réplique LinkedIn de l'INFO Algorithme [[sources/2026-04-11-algorithme-linkedin-2e-source-ia]] : signal humain non-fakeable B2B, profils individuels > pages corporate, 5 posts / 4 semaines suffisent.

## Apports à la KB

- Confirme empiriquement le pattern "Type A" (retour terrain factuel) comme **format LinkedIn signature** — corrobore l'analyse [[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]]
- 5 types de data propriétaire formalisés — actualise/précise [[concepts/data-proprietaire]] (originellement classification "internes vs externes")
- 11 posts = matériau de réutilisation pour le skill `linkedin-post-tim` (pas encore de skill output formel dans `wiki/posts-linkedin/`)
- Cohérence inter-canaux : les patterns Substack ([[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]]) se retrouvent dans les posts LinkedIn (même closings, même renversements, même CTA "ps : … dis-le en com'")

## Limites

- 2 fichiers de "trend research" non lus en détail (linkedin-trend-research-* x2) — sources de veille, pas de posts publiés
- Pas de métriques de performance LinkedIn (likes, saves, reach) sur les 8 posts publiés
- Pattern "Type A" identifié mais autres types (Type B "Voici la donnée", Type C "Renversement", etc.) non explicités dans le corpus

## Pages liées

[[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]] · [[sources/2026-04-11-algorithme-linkedin-2e-source-ia]] · [[concepts/data-proprietaire]] · [[concepts/anti-ai-writing]] · [[concepts/seo-multi-plateforme]] · [[concepts/surprise-gap]] · [[entities/linkedin]] · [[entities/organikk-co]] · [[entities/bootcamp-seo-ia]] · [[sources/2026-04-12-tim-skills-seo-proprietary]]
