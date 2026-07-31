---
title: "Algorithme — édition 2026-07-31 (v2)"
date: 2026-07-31
type: revue-presse
pilier_info_du_jour: GEO
piliers_breves: [Product-Led SEO, Niche SEO, GEO]
author: SyntheticBrain
status: draft
---

# Algorithme — édition du 31 juillet 2026 (v2)

## Résumé

- Une étude Writesonic publiée le 29 juillet 2026 dans Search Engine Land, portant sur environ 16 millions d'apparitions de marque sur 30 jours, publie pour la première fois un classement par moteur du taux de « citation fantôme » (URL citée mais nom de marque absent du texte de la réponse) : Perplexity 52 %, Google AI Mode 49 %, Google AI Overviews 41 %, ChatGPT 37 %, Gemini 25 %, Grok 22 %, Microsoft Copilot 19 %.
- Cette hiérarchie inverse l'intuition dominante : le moteur le plus « cite-heavy » du marché (Perplexity) est aussi celui qui nomme le moins souvent la marque source dans le texte final.
- Microsoft Bing teste l'affichage du prix directement sur la vignette produit dans les résultats organiques, et deux lignes de vignettes sous un même snippet, changement documenté par Barry Schwartz sur seroundtable.com le 29 juillet 2026.
- Google Discover teste sur mobile un carrousel « Read Later Queue » en tête de la page d'accueil qui remonte les articles enregistrés par l'utilisateur, signalé par Damien Andell et repris par Barry Schwartz le 30 juillet 2026.
- Le rapport Similarweb « 2026 Generative AI Landscape », couvert par TechCrunch le 27 juillet 2026, chiffre les visites vers AI Mode à 279 millions en mai 2026 contre 126 millions en juin 2025 et une multiplication par plus de cinq du nombre de citations dans les réponses IA de Google sur un an.

## Info du jour — GEO

**Une étude Writesonic sur 16 millions d'apparitions de marque publie pour la première fois un classement par moteur du taux de citation fantôme, Perplexity en tête à 52 %**

Nikki Lam, SVP Head of Earned Media chez NP Digital U.S., et Samanyou Garg, fondateur et CEO de Writesonic, ont publié le 29 juillet 2026 à 10h00 sur Search Engine Land une analyse chiffrée de ce qu'ils nomment la « citation fantôme » ([Search Engine Land](https://searchengineland.com/ghost-citation-problem-ai-483794)). La définition, verbatim dans l'article : « an AI engine links to your page as a source but doesn't mention your brand in the answer itself ». La marque a fourni la source, mais son nom n'apparaît pas dans la réponse générative que lit l'utilisateur.

Le corpus, verbatim dans l'article : « Writesonic analyzed a recent 30-day window of AI answer data across thousands of brands » et « across roughly 16 million brand appearances ». Le nombre exact de marques et la liste des industries ne sont pas publiés.

La hiérarchie par moteur, publiée pour la première fois à cette échelle :

- Perplexity : 52 %
- Google AI Mode : 49 %
- Google AI Overviews : 41 %
- ChatGPT : 37 %
- Gemini : 25 %
- Grok : 22 %
- Microsoft Copilot : 19 %

Trois lectures se dégagent de ces chiffres. La première tient à Perplexity. C'est le moteur qui affiche le plus de citations par réponse et qui structure toute son interface autour du lien source. C'est aussi celui qui, dans plus d'une réponse sur deux, cite l'URL sans nommer la marque dans le texte. La reformulation générative reprend le contenu et conserve la source dans la liste de citations, mais elle ne réutilise pas le nom de marque dans la phrase que l'utilisateur lit. Ce n'est pas un défaut technique, c'est un choix de rédaction assumé du moteur.

La deuxième lecture porte sur l'écart entre les deux surfaces Google. Google AI Mode (49 %) est presque à parité avec Perplexity, quand Google AI Overviews (41 %) est nettement en dessous. Les deux surfaces exposent des réponses génératives sur des corpus qui se recoupent largement, avec des politiques de citation formellement proches. L'écart de 8 points suggère des politiques de gabarit distinctes entre AI Mode (mode conversationnel, réponse plus longue, plus reformulée) et AI Overviews (bloc résumé au-dessus des résultats, phrasing plus contraint qui préserve mieux le nom de source).

La troisième lecture concerne le bas du classement. Copilot (19 %), Grok (22 %) et Gemini (25 %) sont significativement plus littéraux dans leur reprise. Un consultant qui priorise la visibilité de marque nommée dans le texte n'a pas la même feuille de route selon la surface visée : sur Perplexity et AI Mode, obtenir la citation URL ne suffit pas à obtenir la visibilité de marque ; sur Copilot ou Grok, la citation implique quasi systématiquement le nom.

L'article assume ses limites, verbatim : « The results represent a snapshot of engine behavior during the measurement window and don't establish the causes of ghost citations or their effect on clicks, brand recall, trust, or conversions. » L'étude mesure la fréquence, pas la conséquence. Elle ne dit rien du taux de clic sur les liens fantômes, ni de la mémorisation de marque après exposition à une réponse avec ou sans nom.

Deux caveats supplémentaires méritent d'être posés en tête de lecture, non énoncés dans l'article. Un, Writesonic vend une plateforme de mesure de visibilité IA (AI Visibility Tracker), la métrique publiée est cohérente avec la valeur commerciale du produit, ce qui crée un biais de valorisation à documenter. Deux, la co-signature de Nikki Lam (NP Digital, agence indépendante de l'éditeur) est un mécanisme de crédibilisation partiel : elle atteste que la méthodologie a été relue par un praticien tiers, elle ne remplace pas une réplication indépendante sur un panel distinct.

Le phénomène est corroboré par une étude antérieure indépendante de Writesonic. Kevin Indig, dans Growth Memo en avril 2026 avec la Semrush AI Visibility Toolkit, mesurait 61,7 pct de citations fantômes sur un corpus de 3 981 domaines, 115 prompts, 14 pays et 4 moteurs ([Growth Memo](https://www.growth-memo.com/p/the-ghost-citation-problem), reprise chez [AuthorityTech](https://authoritytech.io/curated/ghost-citations-ai-brand-visibility-2026)). Les deux mesures ne sont pas directement comparables (échantillons, définitions, moteurs suivis distincts), mais elles établissent indépendamment l'existence du phénomène à grande échelle et son ordre de grandeur.

Le rattachement à la doctrine est direct. La fiche [[concepts/metriques-visibilite-geo]] documente déjà cinq dimensions de mesure de la présence en moteurs génératifs (apparition, densité, position de citation, persistance temporelle, taux de recommandation nominative documenté par Ahrefs Brand Radar 34 pages 43 pct dans l'édition du [14 juillet 2026 v2](../../revuedepressIA/2026-07-14-revue-presse-v2.md)). L'étude Writesonic vient renforcer et chiffrer à grande échelle une sixième dimension distincte des cinq premières : la présence nominale de la marque dans le texte de la réponse, indépendante de la présence de l'URL en source. Ce n'est pas une redite de la mesure Ahrefs (qui portait sur la recommandation d'une marque concurrente à la place de la marque source, sur 34 pages autopromotionnelles). Ici la mesure porte sur le simple fait de nommer ou pas la marque, sur 16 millions d'apparitions et sept moteurs distincts.

La conclusion opérationnelle pour un consultant GEO. Suivre un taux de citation URL n'est pas suivre la visibilité de marque : la métrique « citation fantôme » doit être ajoutée aux tableaux de bord, avec une ventilation par moteur, parce que la même page peut être « très citée » et « jamais nommée » simultanément. Un moteur qui cite beaucoup et nomme peu (Perplexity, AI Mode) exige un travail éditorial spécifique sur la structure du contenu : phrasing en tête de section avec le nom de marque intégré à la formulation de la réponse-type, positionnement du nom en début de phrase des passages potentiellement extractibles, mention de la marque dans les H2/H3 plutôt que uniquement dans le corps ou l'auteur.

Ce que l'étude ne dit pas et qu'il reste à mesurer : le taux de clic sur une citation fantôme, la mémorisation de marque post-exposition, la vitesse à laquelle une marque nouvellement citée voit son taux de mention rejoindre son taux de citation. Trois prédictions vérifiables datées.

- P-2026-07-31-v2-1 : au moins un des trois autres outils de mesure GEO indépendants (Ahrefs Brand Radar, Semrush AI Toolkit, BrightEdge) publie avant le 31 mars 2027 une mesure de taux de mention de marque distincte du taux de citation URL, avec ventilation par moteur et corpus supérieur à 5 millions d'apparitions. Confidence 0,55.
- P-2026-07-31-v2-2 : le taux de citation fantôme sur Perplexity mesuré à 52 pct au 29 juillet 2026 varie de moins de 5 points (bande 47-57 pct) sur une nouvelle mesure à échelle équivalente publiée avant le 31 décembre 2026. Confidence 0,50.
- P-2026-07-31-v2-3 : au moins un dirigeant nommé d'un des sept moteurs mesurés (Perplexity, Google, OpenAI, xAI, Microsoft) prend position publiquement sur la citation fantôme avant le 31 décembre 2026 (billet blog, tweet, interview presse), soit pour la justifier (choix éditorial), soit pour l'atténuer (change de gabarit). Confidence 0,35.

---

## Brève 1 — Product-Led SEO

### Microsoft Bing teste l'affichage du prix directement sur la vignette produit et deux lignes de vignettes sous un même snippet organique

Barry Schwartz documente sur Search Engine Roundtable le 29 juillet 2026 un test de Bing repéré par Sachin Patel qui a publié une capture sur X ([Search Engine Roundtable](https://www.seroundtable.com/bing-pricing-product-images-41765.html), [Optimixed](https://www.optimixed.com/microsoft-bing-testing-pricing-on-product-images/)). Deux changements sont observés simultanément sur la SERP organique Bing. Un, le prix est affiché directement sur la vignette du produit, superposé à l'image, à la place des étoiles de review qui apparaissaient précédemment à cet endroit et laissaient le prix en dessous, en texte séparé. Deux, deux lignes de vignettes produit sont affichées sous un même snippet de résultat, contre une ligne dans l'affichage standard.

Ce que ça déplace côté Product-Led SEO. La SERP organique Bing devient plus explicitement une page de comparaison prix, sans passer par un onglet Shopping ou une intégration Merchant Center. Pour un marchand qui optimise une fiche produit, l'unité pertinente n'est plus la carte-produit visible dans le tab Shopping, mais la vignette organique elle-même : l'image doit rester lisible avec un cartouche de prix superposé (pas de packshot chargé, pas de bordures fines, pas de texte publicitaire déjà présent sur l'image), et le prix communiqué à Bing via schema.org/Product doit être à jour au fil du flux, parce qu'un écart entre le prix affiché sur la vignette et le prix à l'atterrissage renvoie une friction plus visible qu'avant.

Le test n'est pas généralisé au 29 juillet et Microsoft n'a pas fait de commentaire public. Bing avait déjà testé mi-juin 2026 un « product detail overlay » avec pricing et price insights ([Search Engine Roundtable overlay](https://www.seroundtable.com/bing-product-detail-overlay-41623.html)) ; le test du 29 juillet est plus léger (pas d'overlay, pricing directement sur la vignette organique).

Prédiction vérifiable. P-2026-07-31-v2-4 : Bing sort ce test du stade preview et le déploie de façon stable sur au moins un vertical (e-commerce généraliste ou électronique) avant le 31 décembre 2026, confirmé par une deuxième source indépendante que Barry Schwartz. Confidence 0,50.

---

## Brève 2 — Niche SEO

### Google Discover teste sur mobile un carrousel « Read Later Queue » qui remonte en tête de page d'accueil les articles enregistrés par l'utilisateur

Damien Andell repère et publie une vidéo d'un test Google Discover : sur mobile, en haut de la page d'accueil Google, un carrousel intitulé « Read Later Queue » remonte les articles que l'utilisateur a préalablement enregistrés via le bouton « save » ([Search Engine Roundtable](https://www.seroundtable.com/google-discover-read-later-queue-41718.html), [Optimixed](https://www.optimixed.com/google-discover-read-later-queue-carousel/)). Barry Schwartz couvre le test le 30 juillet 2026. Le carrousel n'est pas activé pour tous les utilisateurs à cette date.

Ce que ça change pour un éditeur qui compte sur Discover. Discover a toujours été un flux algorithmique de découverte basé sur les intérêts inférés. Un carrousel « Read Later » superpose à ce flux une couche de rétention, qui remonte le contenu enregistré indépendamment du signal d'intérêt Discover courant. Un article enregistré aujourd'hui redevient une impression demain, sans nouvelle décision de la couche découverte. Ça élargit la fenêtre de conversion d'un article Discover : le clic peut arriver 24-48h après l'exposition initiale, sur une intention distincte (retour à un article prévu pour plus tard, pas découverte).

La conclusion opérationnelle pour un éditeur, dans l'hypothèse d'un déploiement large. Il devient rationnel de mesurer non seulement le taux de clic en Discover, mais aussi le taux d'enregistrement (signal fort d'intention de lecture différée). Un article qui produit un taux d'enregistrement élevé mais un taux de clic initial modeste peut redevenir traficant sur la fenêtre 24-72h via ce carrousel. Ce que le rapport « Discover clicks » de Search Console ne saura pas décomposer tant que Google ne publie pas de dimension « source du clic Discover » (algorithmique vs carrousel Read Later).

Trois caveats. Un, test non activé pour tous, ni annoncé officiellement. Deux, le bouton « save » Discover reste peu utilisé par l'utilisateur moyen, l'audience adressable de ce carrousel est un sous-ensemble minoritaire des lecteurs Discover. Trois, pas de calendrier de généralisation, ni de statistique sur la part d'utilisateurs qui enregistrent des articles dans Discover.

Prédiction vérifiable. P-2026-07-31-v2-5 : Google confirme officiellement l'expansion du carrousel « Read Later Queue » à au moins une zone géographique ou une cohorte d'utilisateurs identifiable (annonce Search Central ou billet Google blog ou compte Google Search Liaison) avant le 31 décembre 2026. Confidence 0,40.

---

## Brève 3 — GEO complémentaire

### Similarweb « 2026 Generative AI Landscape » chiffre à 279 millions les visites mensuelles vers Google AI Mode en mai 2026 contre 126 millions en juin 2025, et une multiplication par plus de cinq des citations dans les réponses IA de Google sur un an

Sarah Perez publie le 27 juillet 2026 sur TechCrunch une couverture du rapport Similarweb « 2026 Generative AI Landscape » ([TechCrunch](https://techcrunch.com/2026/07/27/googles-ai-search-is-rapidly-becoming-the-default-new-data-shows/), reprise indépendante le 28 juillet chez [The AI Insider](https://theaiinsider.tech/2026/07/28/googles-ai-overviews-nearly-triple-in-search-coverage-reshaping-web-search-behavior/)). Trois chiffres verbatim dans l'article. Un, les visites mensuelles vers Google AI Mode passent de 126 millions en juin 2025 à 279 millions en mai 2026, soit une multiplication par 2,2 sur onze mois. Deux, le taux d'apparition des AI Overviews sur les requêtes Google passe de 15 pct il y a un an à 43 pct au moment de la mesure. Trois, le nombre de citations dans les réponses IA de Google a été multiplié par plus de cinq sur un an.

Un chiffre à part sur ChatGPT. Selon Similarweb, la part des requêtes ChatGPT desktop US qui incluent une citation reste faible à 6,8 pct en mai 2026, malgré la mise à jour Search du 7 mai qui a fait passer les visites depuis ChatGPT vers des pages web de 25 pct (mars 2026) à près de 60 pct (30 mai 2026).

Ce que ça déplace côté doctrine. Deux mouvements simultanés se lisent dans ces chiffres. Un, la surface générative Google grossit vite (43 pct des requêtes, +2,2x en visites AI Mode sur onze mois). Deux, le volume de citations a été multiplié par plus de cinq sur la même période, ce qui suggère que Google cite plus par réponse quand il y a réponse générative. Combinés avec le résultat de l'étude Writesonic publiée deux jours plus tard (info du jour de cette édition), cela produit un tableau cohérent : sur la surface Google, la citation devient plus fréquente, mais le nommage de la marque dans le texte reste ratable dans 41 à 49 pct des cas selon la surface (AI Overviews ou AI Mode).

Le chiffre ChatGPT à 6,8 pct de citations est également important : ChatGPT cite beaucoup moins que Perplexity ou les surfaces Google génératives, mais quand il cite (la mise à jour Search du 7 mai a poussé le trafic sortant à 60 pct), la mesure Writesonic établit qu'il nomme la marque source dans 63 pct des cas (100 - 37 pct de citation fantôme).

Une limite explicite : Similarweb mesure des visites au niveau URL (clickstream et panels), pas des requêtes ni des impressions dans la SERP, ce qui compte visites vers AI Mode mais ne dit rien du volume de requêtes traitées par AI Mode sans clic sortant, la valeur qui compte le plus pour un consultant SEO qui optimise pour la présence sans clic. Le rapport est un instantané vendeur (Similarweb vend AI Search Intelligence), corroboré partiellement par des mesures BrightEdge, Semrush, Conductor qui donnent des taux différents (25 à 48 pct) selon les corpus et méthodologies.

Prédiction vérifiable. P-2026-07-31-v2-6 : Google publie avant le 31 décembre 2026 un chiffre officiel de volume de requêtes mensuelles traitées par AI Mode ou AI Overviews, distinct des visites Similarweb, dans un billet Search Central, un rapport financier ou un keynote officiel Sundar Pichai ou Liz Reid. Confidence 0,30 (Google est historiquement peu bavard sur les volumes par surface).

---

Draft SyntheticBrain. Rien n'a été envoyé.
