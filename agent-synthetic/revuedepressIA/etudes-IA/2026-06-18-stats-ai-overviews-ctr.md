---
type: query
title: "AI Overviews : l'impact sur le clic, chiffres 2026"
aliases: [stats-ai-overviews, ai-overviews-ctr-2026]
tags: [geo, ai-overviews, statistiques, ctr, sge]
created: 2026-06-18
updated: 2026-06-18
sources: 3
confidence: high
status: draft
skill: seo-page-statistiques
---

# AI Overviews : l'impact sur le clic, chiffres 2026

Quand un AI Overview s'affiche, le clic sortant baisse nettement sur les requêtes informationnelles : 8% des recherches débouchent sur un clic vers un résultat classique, contre 15% sans résumé (Pew Research, 2025). Le constat est réel et mesuré par plusieurs études, mais il est contesté et sa cause n'est pas tranchée : voir la contre-analyse plus bas.

## Les chiffres clés (vérifiés à la source)
- **8% vs 15%** : taux de clic sur un résultat de recherche quand un AI Overview est présent, contre sans. (Pew Research, juillet 2025)
- **1%** : part des recherches où l'utilisateur clique sur un lien source à l'intérieur de l'AI Overview. (Pew Research, juillet 2025)
- **18%** des recherches de l'étude produisent un AI Overview ; **58%** des répondants en ont vu au moins un en mars 2025. (Pew Research, 2025)
- **−61%** : chute du CTR organique sur les requêtes avec AI Overview, de 1,76% à 0,61% entre juin 2024 et septembre 2025. (Seer Interactive, novembre 2025)
- **−68%** : chute du CTR payant sur ces mêmes requêtes, de 19,70% à 6,34%. (Seer Interactive, novembre 2025)
- **−58%** : CTR moyen en première position quand un AI Overview est présent, sur 300 000 mots-clés. (Ahrefs, décembre 2025)
- **26% vs 16%** : taux d'abandon de la navigation après une page vue avec résumé, contre sans. (Pew Research, 2025)

## Le clic vers les sites se contracte
Pew Research, sur un panel de 900 adultes américains et près de 69 000 recherches en mars 2025, mesure que la présence d'un AI Overview fait passer le taux de clic vers un résultat classique de 15% à 8%. Le lien cité dans le résumé lui-même ne capte qu'1% des clics. (Pew Research, 2025)

## La baisse de CTR mesurée côté SEO
Seer Interactive, sur 3 119 termes et 42 organisations, observe un CTR organique divisé par près de trois sur les requêtes avec AI Overview (1,76% à 0,61% entre juin 2024 et septembre 2025), soit −61%. Ahrefs, sur 300 000 mots-clés, mesure −58% de CTR pour la première position lorsqu'un AI Overview est présent (données décembre 2025). (Seer Interactive 2025, Ahrefs 2025)

## Pourquoi ces chiffres ne disent pas la même chose (lecture originale)
Les trois études sont citées en boucle comme si elles mesuraient la même chose. Elles ne le font pas, et c'est ce qui explique l'écart apparent entre « 8% » et « −61% » :
- **Pew** mesure un comportement d'usager : sur 100 recherches avec AIO, combien finissent par un clic. C'est un taux absolu (8%), pas une variation.
- **Seer** mesure une variation de CTR dans le temps sur les mêmes requêtes (−61%), incluant l'effet d'autres changements de SERP sur 15 mois.
- **Ahrefs** isole la première position et compare requêtes avec et sans AIO à un instant donné (−58%).
Conclusion honnête : les trois convergent sur le sens (l'AIO réduit fortement le clic sortant) mais ne sont pas additionnables. Le bon raccourci n'est pas « le CTR baisse de 61% » tout court, c'est « selon la méthode, la perte de clic se situe entre la moitié et deux tiers ».

## Contre-analyse : et si le clic ne s'effondrait pas ?
Quatre arguments sérieux nuancent le constat. À garder, ils renforcent la crédibilité de la page plutôt que de l'affaiblir.
- **Google conteste la lecture.** Liz Reid (VP Search) soutient que les AI Overviews coupent surtout les clics « de rebond » (l'usager prend un fait et repart) et que le volume total de recherches augmente, ce qui stabilise la performance. Réserve : Google n'a publié aucune donnée à l'appui. (Search Engine Land, 2026)
- **Corrélation n'est pas causalité.** En suivant les mêmes mots-clés avant et après l'apparition d'un AIO, le zéro-clic bouge à peine : Google activerait les AIO surtout sur des requêtes déjà peu cliquées. L'AIO accompagnerait le zéro-clic plus qu'il ne le causerait. (analyses de cohorte rétrospective, 2026)
- **Être cité fait remonter le clic.** Les pages citées dans un AIO afficheraient +35% de CTR organique face aux pages classées mais non citées. L'AIO peut donc augmenter le clic quand on y est. Réserve : on ne peut pas prouver que la citation cause ce gain, les sites cités ayant souvent déjà plus d'autorité. (Seer Interactive)
- **Signe de reprise.** Après sa chute, le CTR organique sur requêtes AIO remonterait partiellement début 2026, encore sous le niveau de départ. Le « collapse » se tasse. (Seer, Search Engine Journal)
Lecture honnête : l'effet baissier est réel et mesuré, mais ni uniforme, ni forcément causal, ni définitif. La bonne formulation n'est pas « le clic s'effondre », c'est « le clic sortant baisse fortement sur les requêtes informationnelles, inégalement, et le débat sur la cause reste ouvert ».
*(Chiffres de contre-analyse à repasser au même fetch primaire que les chiffres principaux avant publication.)*

## Nos propres chiffres (données de première main)
Mesure maison sur notre portefeuille GSC (23 propriétés exploitables, 9 798 requêtes hors marque, 1,76M impressions, mars à mai 2026, CTR pondéré par impressions). Source : notre étude `CTR réel × AI Overviews sur portefeuille GSC` (`raw/etudes-seo/`).
- **CTR réel en position 1 : 34,2%**, puis falaise immédiate à **5,6% en position 2** et 4,6% en position 3. Sur les courbes publiques classiques, la position 2 tourne plutôt autour de 15%.
Lecture : sur nos sites, tout ce qui n'est pas la première place est massivement sous-cliqué. Cohérent avec la nuance « corrélation n'est pas causalité » de la contre-analyse : l'effondrement du clic sous la première position est large, les AI Overviews en sont un facteur parmi les features de SERP, pas la cause unique. C'est notre lecture des métriques de visibilité GEO.
Honnêteté : la GSC ne dit pas quelles requêtes ont déclenché un AI Overview. Cette mesure est donc une courbe de CTR par position (niveau 1), pas un CTR avec AIO vs sans AIO (niveau 2, qui exige un signal de présence d'AIO, en cours). Données agrégées et anonymisées, aucun site nommé.

## FAQ
**De combien baisse le clic avec un AI Overview ?** Selon la méthode de mesure, entre la moitié et deux tiers du CTR sortant. Pew : 8% de clic contre 15% sans. Seer : −61%. Ahrefs : −58% en position 1.
**Combien de recherches affichent un AI Overview ?** 18% des recherches du panel Pew en mars 2025. Les outils de suivi de SERP rapportent des taux plus élevés selon leur méthode. [À SOURCER : taux primaire 2026]

## Sources
- Pew Research Center, « Google users are less likely to click on links when an AI summary appears », 22 juillet 2025 — pewresearch.org. Panel 900 adultes US, ~69 000 recherches, mars 2025. Consulté le 2026-06-18.
- Seer Interactive, « AIO Impact on Google CTR, September 2025 Update », 4 novembre 2025 — seerinteractive.com. 3 119 termes, 42 organisations, 25,1M impressions organiques. Consulté le 2026-06-18.
- Ahrefs, « AI Overviews Reduce Clicks Update », décembre 2025 — ahrefs.com/blog/ai-overviews-reduce-clicks-update. 300 000 mots-clés. Consulté le 2026-06-18.

*(Schema Dataset + dateModified. Page actualité, à rafraîchir à chaque nouvelle étude primaire.)*
