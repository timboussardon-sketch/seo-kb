---
type: source
source_type: article
title: 5 skills SEO technique à ajouter sur Claude
aliases: [5-skills-seo-technique-claude]
tags: [organikk, blog, tim, skills, seo, claude]
created: 2026-05-27
updated: 2026-07-05
sources: 1
confidence: high
status: stable
---

# 5 skills SEO technique à ajouter sur Claude

**Auteur** : Timothée Boussardon (organikk.co/blog)
**Type** : article de blog
**URL** : https://organikk.co/blog/5-skills-seo-technique-claude/
**Date publication** : 2026-05-27

## Contexte
L'auteur partage 5 skills Claude qu'il utilise pour remplacer les outils SEO payants et couvrir la couche infra du SEO technique. Sous-ensemble cohérent et interdépendant : indexation d'abord, puis données structurées, cannibalisation, maillage, performance. Prolonge un guide précédent sur 9 skills SEO complets.

## Chiffres / faits clés
- Les 5 skills : indexation-check ; seo-donnees-structurees (JSON-LD auto sur Next.js App Router) ; seo-cannibalisation (depuis GSC) ; maillage-systeme + maillage-interne-gsc ; seo-core-web-vitals (Lighthouse mobile).
- 90 % des audits SEO ne testent pas vraiment l'indexation, juste le statut HTTP.
- 90 % des sites posent le JSON-LD à la main, ce qui désynchronise au premier edit.
- Indexation estimée par scraping : ~40-60 % de fiabilité (rate-limit) ; variante GSC API = 100 %, limite officielle 2 000 inspections/jour/propriété.
- Architecture : 3 à 5 piliers maximum. Densité maillage : 2-5 liens internes par 1000 mots. 1 lien entrant = page sous-maillée, 0 = orpheline, 5 citations mini pour une page mère "active".
- Seuils Core Web Vitals visés : LCP < 2500 ms, CLS < 0.1, TBT/INP < 200 ms. Lighthouse en 3 workers : ~5-10 min pour 50 URLs.

## Citations marquantes
> "Un site parfaitement optimisé peut devenir invisible si la technique est catastrophique." (attribution: Tim, 2026-05-27)
> "Tu n'es plus l'assistant de Claude, c'est lui qui exécute ta méthode." (attribution: Tim, 2026-05-27)
> "Une ancre, ce n'est pas un mot-clé. C'est une promesse de continuité." (attribution: Tim, 2026-05-27)
> "Deux pages qui visent la même requête = zéro page qui ranke." (attribution: Tim, 2026-05-27)
> "Discipline : observation côté agent, décision côté humain." (attribution: Tim, 2026-05-27)

## Angle SEO à retenir
Le SEO technique n'est plus une commodité : il doit être encodé dans une méthode personnelle via un SKILL.md, sinon tout agent IA produit un audit générique. Avec un skill bien conçu, Claude exécute la méthode de l'utilisateur et tient sa position sous pression. Les 5 skills couvrent la couche infra et sont interdépendants : inutile d'optimiser une page non indexée, d'où l'ordre indexation → balisage → maillage → perf. Chaque skill produit un `.claude/skills/[nom]/SKILL.md`, ~15 min de setup, 0 € récurrent, plusieurs exécutables en cron via /schedule.

## Limites
Article de démonstration produit (skills Organikk). Les "90 %" sont des affirmations de l'auteur sans source. Les seuils CWV sont ceux de Google, mais les temps d'exécution et taux de fiabilité dépendent du setup local. Aucune mesure de résultat SEO chiffrée.

## Pages liées
**Entity** : [[entities/gsc]] · [[entities/organikk-co]]
**Concepts** : [[concepts/maillage-interne]] · [[concepts/cannibalisation]] · [[concepts/passage-ranking]] · [[concepts/e-e-a-t]] · [[concepts/grounding-score]] · [[concepts/aeo]]
