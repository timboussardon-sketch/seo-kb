---
type: revue-presse
title: "Algorithme, 15 juillet 2026"
date: 2026-07-15
pilier: Actualité SEO
info_du_jour: Google Merchant Center AI Performance Insights, pilote élargi 14 juillet 2026
status: draft
generated_by: SyntheticBrain (agent-synthetic)
---

# Algorithme, édition du 15 juillet 2026

**Merchant Center devient le premier point d'entrée Google à afficher une donnée de requête pour AI Mode et AI Overviews. Les éditeurs, eux, n'y ont toujours pas droit.**

## Les points capitaux

- Google a élargi le 14 juillet 2026 le pilote de son rapport **AI Performance Insights** dans Merchant Center, disponible sur un nombre limité de comptes marchands aux États-Unis, avec extension annoncée à l'Australie, au Canada, à l'Inde et à la Nouvelle-Zélande.
- Le rapport est le premier produit Google à donner aux marques du **query data** (fréquence des termes recherchés, part de voix contre marques comparables) sur les surfaces IA de Google : AI Mode, AI Overviews, application Gemini.
- Le rapport Search Console AI performance report, ouvert le 3 juin 2026 à un sous-ensemble de sites au Royaume-Uni, ne fournit toujours ni clics, ni CTR, ni requêtes aux éditeurs. L'asymétrie de traitement entre marchands et éditeurs se creuse.
- ChatGPT Ads Manager a ajouté le 14 juillet des colonnes **Attributed Sales Value** et **Sales ROAS** au tableau des campagnes, signal net d'un passage de la logique de portée à la logique de revenu attribué.
- Étude CiteLens (8 juillet 2026) sur 320 requêtes acheteur en marché turc : les citations de Google AI Mode et Perplexity suivent le classement Google à ~90 % de corrélation, celles de ChatGPT ne le suivent pas.

---

## Info du jour. Google Merchant Center devient le premier produit Google à exposer une donnée de requête pour AI Mode et AI Overviews

**Pilier : Actualité SEO.**

Google a élargi le 14 juillet 2026 le pilote de son rapport **AI Performance Insights** dans Merchant Center, d'après le recap quotidien de Barry Schwartz sur [Search Engine Roundtable](https://www.seroundtable.com/google-merchant-center-ai-performance-insights-41675.html) et le recap [Optimixed du 14 juillet](https://www.optimixed.com/daily-search-forum-recap-july-14-2026/). Le rapport avait été annoncé le 20 mai à Google Marketing Live ([Search Engine Land, Anu Adegbola](https://searchengineland.com/google-launches-ai-performance-insights-and-conversational-attributes-in-merchant-center-478108) ; [blog.google](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/)) et documenté par Google dans un [article d'aide Merchant Center](https://support.google.com/merchants/answer/17117204?hl=en).

Le rapport est accessible dans Merchant Center sous **Analytics > Products > AI Performance**. Il regroupe quatre vues :

1. **Share of voice** : indicateur qui mesure la fréquence à laquelle les produits d'une marque apparaissent dans les réponses IA de Google Search et Gemini, comparée à un ensemble de marques jugées similaires par Google.
2. **Shopping funnel performance** : décomposition de la performance par phase (découverte, évaluation, achat).
3. **Product term insights** : liste des termes que les utilisateurs formulent dans une conversation IA autour des produits.
4. **Product attributes insights** : attributs de fiche produit les plus fréquemment recherchés et attributs manquants.

Le rapport reste en pilote limité aux comptes Merchant Center aux États-Unis. Google indique une extension progressive à l'Australie, au Canada, à l'Inde et à la Nouvelle-Zélande dans les mois à venir. Aucun calendrier plus précis n'est communiqué. Le SEO Brodie Clark, qui indique avoir obtenu l'accès à un sous-compte pour un client, décrit la nouveauté comme **le premier produit Google à donner aux marchands une donnée de requête pour AI Overviews et AI Mode** (voir la reprise de son observation par plusieurs sources dont [Semrush](https://www.semrush.com/blog/google-to-add-ai-performance-report-to-merchant-center/) et [Paz.ai](https://www.paz.ai/blog/google-ai-performance-insights-share-of-voice)).

Le fait notable est le décalage avec le rapport Search Console AI performance ouvert le 3 juin 2026 à un sous-ensemble de sites au Royaume-Uni ([billet Google Search Central du 3 juin 2026](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) ; [Search Engine Land 479298](https://searchengineland.com/google-search-console-ai-performance-reports-and-controls-to-block-your-content-in-ai-responses-479298)). Le rapport GSC AI performance fournit aux éditeurs les impressions, pages, pays et appareils pour AI Overviews, AI Mode et Discover. Il ne fournit ni clics, ni CTR, ni requêtes. Google a indiqué ajouter davantage de métriques dans le temps sans donner de calendrier.

Le décalage se lit littéralement : côté marchands, Google expose une part de voix et des termes de requête sur les surfaces IA. Côté éditeurs, Google expose une impression et rien qui permette de relier une requête à un contenu. Deux populations, deux niveaux d'information, sur les mêmes surfaces IA.

**Lien doctrine.** Le rapport ajoute une septième dimension à [[metriques-visibilite-geo]] : **share of voice mesurée nativement par Google** sur AI Mode / AI Overviews / Gemini shopping, à côté de `Imp_wc`, `Imp_pos`, Subjective Impression, référral traçable en session GA4, persistance temporelle et durée de vie de citation. La dimension nouvelle est spécifique au périmètre marchand et à un panier de marques comparables défini par Google. Elle n'est pas transférable au périmètre éditorial tant que le rapport GSC AI performance n'ajoutera pas de query data.

Deuxième lien doctrine : [[data-proprietaire]]. La donnée exposée dans le rapport n'est disponible ni via un scrape ni via un tiers ; elle est produite par Google à partir de logs internes et exposée à un marchand nommé sur son propre compte. Pour la durée du pilote, un marchand américain participant obtient une donnée que ses concurrents extérieurs au pilote n'ont pas. C'est un actif d'observation exclusif à horizon court, limité par la levée progressive de la restriction géographique.

Troisième lien doctrine : [[tabou-visibilite]]. Google emploie le vocabulaire « share of voice » et « visibility ». Le rapport donne un chiffre chiffré et daté, sur une population de marques comparables définie par Google. Le mot est ici associé à une mesure. En parallèle, il reste inopérant en pitch de vente hors du périmètre du rapport, où « part de voix IA » n'a ni unité ni référentiel stable.

**Limites documentaires.** Un point n'est pas confirmé publiquement : la méthode de constitution du panier de marques comparables. La [documentation Google](https://support.google.com/merchants/answer/17117204?hl=en) précise que le benchmarking est fait « against brands similar to yours on shopping journeys » sans détailler ni la source (catégorie GMC, historique de requêtes, catégorisation Product Taxonomy Google) ni la fréquence de recomposition du panier. Aucun échantillon n'a été publié pour l'instant. La [période couverte](https://support.google.com/merchants/answer/17117204?hl=en) n'est pas non plus documentée. Toute décision opérationnelle prise à partir du rapport doit tenir compte de ces zones d'ombre.

**Prédictions.**

- **P-2026-07-15-1** : d'ici le 31 mars 2027, Google ajoute des clics ou du CTR aux données AI Overviews et AI Mode du rapport Search Console AI performance. Résolution positive : mention explicite dans une release note Google Search Central ou un billet Google Search Central. Résolution négative : silence sur cette métrique dans les documents Google jusqu'à cette date.
- **P-2026-07-15-2** : d'ici le 31 décembre 2026, une agence ou un cabinet nommé publie une étude comparant part de voix Merchant Center AI et part de voix Ahrefs Brand Radar ou Semrush AI Visibility sur au moins 20 marques e-commerce US. Résolution positive : étude signée avec échantillon documenté. Résolution négative : aucune étude comparative de ce type publiée d'ici fin 2026.

## Brèves

**ChatGPT Ads Manager passe aux métriques de revenu, 14 juillet 2026.**
Barry Schwartz sur [Search Engine Roundtable](https://www.seroundtable.com/chatgpt-ads-attributed-sales-value-and-sales-roas-41674.html) et le [recap Optimixed](https://www.optimixed.com/chatgpt-ads-manager-adds-attributed-sales-value-sales-roas-and-product-reporting/) rapportent l'ajout de trois éléments au tableau des campagnes du ChatGPT Ads Manager : une colonne **Attributed Sales Value**, une colonne **Sales ROAS** (return on ad spend), et un rapport au niveau du produit. Aucune donnée chiffrée n'est publiée par OpenAI dans les captures d'écran diffusées. L'ajout confirme le passage d'un panneau d'annonceur orienté « portée » vers un panneau orienté « revenu attribué », dans la ligne de la mise en production du tracking de conversion le 11 juillet 2026 rapportée par Barry Schwartz. Le pas suivant à guetter reste la publication par un annonceur nommé d'un premier ROAS chiffré côté ChatGPT Ads.

**Bloc de mises à jour de documentation Google, semaine du 7 juillet.**
La [page What's new de Google Search Central](https://developers.google.com/search/updates) enregistre quatre modifications de documentation sur la semaine du 7 au 14 juillet 2026, listées en primaire par Google : le 14 juillet, mise à jour de la documentation package tracking (l'early adopters program n'accepte plus de nouveaux partenaires) ; le 10 juillet, ajustement du guide de troubleshooting sur la canonicalisation (délai attendu explicité) ; le 7 juillet, extension du champ `Product.category` du merchant listing structured data à un usage texte ou code aligné sur les spécifications Merchant Center, et introduction d'un guide sur les dates d'effet des prix promotionnels (`validFrom`, `validThrough`, `priceValidUntil`). Les quatre changements convergent vers un renforcement du feed produit comme surface indexable, cohérent avec le déploiement du rapport AI Performance Insights côté Merchant Center.

**CiteLens : le classement Google prédit les citations d'AI Mode et de Perplexity, mais pas celles de ChatGPT. Étude publiée le 8 juillet 2026.**
CiteLens a publié le 8 juillet 2026 une étude relayée par [EIN Presswire](https://www.einpresswire.com/article/925230382/citelens-study-seo-decides-ai-citations-on-google-and-perplexity-not-chatgpt) et reprise par [QuickSEO](https://quickseo.ai/blog/chatgpt-vs-perplexity-for-ai-visibility-in-2026-citations-traffic-and-conversion-compared) : 320 requêtes acheteurs types sur trois secteurs de consommation en marché turc, exécutées en juin 2026 sur ChatGPT, Perplexity, Claude et Google AI Mode, puis chaque source citée comparée aux résultats Google et Bing organiques sur la même requête. Résultat central : les citations Google AI Mode et Perplexity suivent le classement Google avec un coefficient de corrélation de 0,92 et 0,87 respectivement, celles de ChatGPT ne le suivent pas et ne dépendent ni du classement ni de la taille de marque. Limites déclarées par l'étude : marché turc, périmètre trois secteurs consommation, 320 requêtes seulement, mesure en juin 2026 sur un état donné des moteurs. À rapprocher de la mesure Averi sur 680 millions de citations qui trouvait 11 % de recouvrement de domaines entre ChatGPT et Perplexity ([mesurée dans l'édition Algorithme v5](https://averi.ai/)) : deux méthodes différentes, deux échelles différentes, une même conclusion sur l'écart structurel entre les deux moteurs.

**Volatilité de classement Google autour du 11 juillet, non confirmée.**
Barry Schwartz signale sur [Search Engine Roundtable](https://www.seroundtable.com/google-search-ranking-volatility-july-11th-41676.html) et le [recap Optimixed du 13 juillet](https://www.optimixed.com/google-search-ranking-volatility-around-july-11th/) une variation de volatilité repérée par les outils AccuRanker, Algoroo, Mozcast, Semrush, Serpstat autour du 11 juillet 2026, informellement nommée « 7-Eleven update » dans les forums. La chatter communautaire est faible et Google n'a rien confirmé. À ranger comme signal outillé sans confirmation ni bilan gagnants/perdants, à surveiller sans en tirer de règle opérationnelle avant qu'une source de mesure de visibilité (Sistrix, Semrush Sensor) ne publie une analyse à large échantillon.

---

*Draft SyntheticBrain, édition 2026-07-15. Aucune diffusion.*
