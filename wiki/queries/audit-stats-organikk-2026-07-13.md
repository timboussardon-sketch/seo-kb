---
type: audit
title: "Audit de cohérence des statistiques publiées sur organikk.co"
aliases: [audit-stats-organikk, audit-pourcentages-site]
tags: [organikk, fact-check, stats, coherence, doctrine]
created: 2026-07-13
updated: 2026-07-13
sources: 4
confidence: high
status: stable
---

# Audit de cohérence des statistiques publiées sur organikk.co

Déclencheur : audit externe relayé par Tim (« 127 phrases contenant un pourcentage », FAQ à 99,9 %, Reddit 46 % vs 24 % à deux clics d'écart). Règle posée le jour même : jamais deux stats contradictoires en ligne sans arbitrage. Extraction complète : **411 phrases uniques à pourcentage** sur 16 fichiers de contenu publié, regroupées en 17 familles + 271 hors famille.

## Corrections appliquées (arbitrage Tim, 2 passes)

| Famille | Problème | Correction |
|---|---|---|
| AIO × informationnelles | 99,9 % (FAQ, newsletter), 91 %/2 % (article, fiche wiki), « quasiment toutes / 5-10 % » (même article) : 3 versions, aucune vérifiable à la source | Tout retiré. Seuls les chiffres vérifiés de l'étude zero-clic restent : 68 % global (58,5 % en 2024), CTR position 1 à 2,6 % avec résumé vs 4,0 % attendu sans |
| Reddit × Perplexity | 46,7 % (Profound), ~24 % (sans source), fourchette 20-47 % (guide Reddit), YouTube n°1 à 32,4 % (Ahrefs) : 4 versions | Canonique = « 20 à 47 % selon les mesures (Evertune, Profound) » sur les surfaces evergreen ; la fiche wiki documente la divergence, mesure Ahrefs incluse |
| Conversion IA | « 14,2 % vs 2,8 % : ratio de 23x » : fusion de deux études (Opollo = 5x ; Ahrefs 23x = ses propres inscriptions SaaS). Vérifié via AirOps/Pixis | Les deux chiffres séparés et attribués dans les deux récaps |
| GEO-bench | Newsletter #3 publiait +30 % autorité ; le paper donne +13 % (correction documentée au vault en avril, jamais répercutée sur le site) | Valeurs exactes rétablies : +41 verbatim, +34 stats, +29 sources, +13 autorité (newsletter + résumé) |
| CTR simulateur ROI | 32 %/15 %/<0,1 % : ne correspondait à aucune courbe publiée | Courbe First Page Sage mai 2025 (39,8/18,7/10,2), positions 6-9 interpolées, hypothèse prudente >10, sourcée dans la copy |
| « Google préconise 60 % » | Invérifiable | Conservé sur décision Tim |
| Divers | 94 % vs 93,6 % dans la même newsletter | Unifié à 93,6 % |

## Politique arbitrée

- **Newsletters archivées** : les chiffres d'époque restent datés tels quels (Gemini 0,1 %, YouTube ~30 % AIO, 90 % pages non indexées). On ne corrige que les erreurs de citation à la publication (cas GEO-bench) et les surfaces evergreen : pages, wiki, articles, résumés.
- **Métriques à dénominateurs différents** : « 24 % des citations *sociales* » (Tinuiti) n'est pas « 24 % des citations » ; toujours nommer le dénominateur.

## Constats non problématiques

- Les claims commerciaux repérés par l'audit externe (« +47 % de leads », « dashboard connecté au CRM ») sont des **exemples pédagogiques** dans un template d'article, pas des promesses d'Organikk.
- Les stats sectorielles des pages stratégies (DGCCRF, UNEP, DREES, Coach Omnium) sont sourcées et sans doublon conflictuel.
- La famille « 80/20 » (l'IA fait 80 % du travail) est un positionnement doctrinal, cohérent partout.
- Le guide Reddit était déjà le traitement le plus honnête du site (fourchettes + divergences nommées) : il devient la référence de style.

## À surveiller

- `articles.ts` (~3687) : « le contenu IA édité par un expert performe à 4 % du contenu 100 % humain » : formulation ambiguë (4 % de la performance ? à 4 % près ?), source « étude 16 mois, 4 200 articles » à retrouver avant de trancher.
- Les résumés de newsletters mélangent parfois des chiffres de plusieurs éditions : vigilance à la prochaine production.
- Toute nouvelle stat : appliquer la règle (grep du corpus avant publication, dénominateur nommé, source datée).

## Liens

[[concepts/information-gain]] · [[concepts/data-proprietaire]] · [[concepts/requete-cliquable-vs-clic]] · [[queries/pseo-2026-07-07-organikk-corpus]]
