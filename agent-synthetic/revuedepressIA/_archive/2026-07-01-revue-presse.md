---
type: revue-presse
title: "Algorithme — Recettes en AI Mode : Google ré-affiche des liens éditeurs au-dessus de la réponse générée"
date: 2026-07-01
pilier_info_jour: product-led-seo
edition: 2026-07-01
statut: draft
---

# Recettes en AI Mode : Google ré-affiche des liens éditeurs au-dessus de la réponse générée

## En 4 points

- Google place désormais des liens vers les pages de recettes en tête des réponses AI Mode, avec trois attributs affichés côté éditeur : nom du créateur, note et nombre d'ingrédients. Annonce Robby Stein (VP Product Search) sur X le 30 juin 2026. Signal Product-Led SEO pour toute base de recettes structurée qui expose ces champs.
- Adobe mesure sur Prime Day 2026 (23 juin) une hausse de +98,3 % en glissement annuel du trafic e-commerce venu des IA, et un avantage de +50,7 % de taux de conversion versus les autres canaux. Rapport Adobe Digital Insights via CMSWire 24 juin.
- Google Merchant Center a activé la diffusion des vidéos produit via l'attribut `video_link` le 30 juin 2026, ouvert le contrôle qualité de ces vidéos, et confirmé le seuil minimum d'image à 500×500 pixels (avertissements dès juillet 2026, application le 31 janvier 2027).
- Un an jour pour jour après le lancement de pay-per-crawl par Cloudflare (1er juillet 2025, « Content Independence Day »), aucune rétrospective officielle n'est publiée à ce jour côté Cloudflare. La donnée disponible reste celle de 2025 : plus d'un milliard de codes 402 par jour, ratio de crawls sans référence Anthropic ~73 000:1 et OpenAI ~1 700:1.

## Info du jour — Pilier PRODUCT-LED SEO

Google a affiché le 30 juin 2026 une nouvelle mise en forme des résultats recettes dans AI Mode. Robby Stein, VP Product de Google Search, l'a annoncée sur X : pour les requêtes de recettes, un bloc de liens éditeurs apparaît en haut de la réponse générée, avec trois attributs par carte : nom du créateur, note de la recette et nombre d'ingrédients. La reprise SEJ ([Southern, 30 juin](https://www.searchenginejournal.com/google-puts-recipe-links-at-top-of-ai-mode-responses/581149/)) cite la formulation exacte : *« For relevant recipe queries, you'll see prominent links at the top of responses with useful details and images – like the creator name, recipe ratings and number of ingredients »*. La reprise SEL ([Goodwin, 30 juin](https://searchengineland.com/google-makes-recipes-in-ai-mode-more-publisher-friendly-481341)) rappelle que Stein rattache le changement au travail recettes commencé en mars 2026, où le résumé de recette synthétisé par Gemini avait été remplacé par un carrousel de plats renvoyant vers les sites créateurs.

Une éditrice recette, Inspired Taste, a réagi publiquement au post de Stein : *« a big step in the right direction, [but] there is a lot more work to be done »* (via SEJ), pointant que les résumés synthétisés en corps de réponse peuvent encore mal restituer le contenu original des pages.

**Le fait est petit en surface, plus grand en implication doctrinale.** Google n'a pas modifié l'algorithme de retrieval, il a ajouté au rendu de la réponse générative un bloc citation-first au-dessus du corps, adossé à un jeu fixe de trois attributs structurés : identité du créateur, agrégat social (rating), et une mesure quantitative de la recette (ingrédients). Pour vous, éditeur d'un site de recettes, cela veut dire trois choses concrètes.

Un : le vertical recettes est le premier cas concret publié où le rendu AI Mode expose des champs structurés d'une source précise au-dessus de la synthèse, avec identification visuelle du créateur. La logique n'est plus « la réponse est un résumé anonyme », c'est « la réponse est une synthèse plus une pile de cartes créateur ». C'est une réponse produit à une critique éditeur (le résumé synthétisé sans crédit lisible), pas une réponse doctrinale à un problème de qualité.

Deux : les trois attributs affichés (créateur, note, nombre d'ingrédients) ne relèvent pas du body text, ils sont extractibles depuis le [Recipe schema](https://developers.google.com/search/docs/appearance/structured-data/recipe) et depuis le profil éditeur. Ils confirment la logique de [[concepts/structural-information-geo]] : ce qui rend une page « citable » côté AI Mode passe par les champs structurels, pas par la prose. La fenêtre d'affichage est petite, la matière qui la remplit est structurée.

Trois : côté [[concepts/product-led-seo]], la lecture opérationnelle est directe. Une base de recettes qui n'est qu'une pile d'articles longs, sans profil créateur qualifié, sans note agrégée, sans structure d'ingrédients exploitable machine, n'est pas éligible à ce nouveau slot. La valeur défendable, dans ce vertical précis, n'est pas la prose autour de la recette, c'est la donnée exploitable de la recette : quantité, unité, séquence, image standardisée, notation, identité auteur. Pas de calculateur ni de simulateur au sens Product-Led classique, mais un composant structuré non substituable par le résumé synthétisé côté Gemini.

**Portée et limites**. Ce n'est qu'un vertical, ce n'est qu'un rendu, ce n'est déployé qu'en anglais aux États-Unis à date. Aucun chiffre d'adoption ni de perte/gain de clic n'est publié. On ne peut pas généraliser à d'autres verticaux sans preuve : rien ne dit que Google fera un rendu équivalent pour un cluster « symptômes santé », « fiches produit » ou « comparateur ». Ce qu'on peut faire, c'est retenir la mécanique observée (Google publie un rendu citation-first pour un vertical où la pression éditeur est ancienne et audible) et la tester quand d'autres verticaux suivront.

**Ce que cela change pour votre lecture de l'AI Mode.** Une même page peut être invisible en résumé synthétisé et citée en carte au-dessus si ses attributs structurés sont solides ; l'inverse existe aussi. La [[concepts/metriques-visibilite-geo|métrique Imp_pos]] devient plus asymétrique : occuper la première position d'un bloc citation-first au-dessus de la synthèse n'a pas la même valeur qu'être ré-cité dans le body de la réponse. Il faut deux mesures distinctes.

## Brèves

### B1 — Business SEO. Adobe mesure sur Prime Day 2026 un basculement du couple trafic IA/conversion

Adobe Digital Insights a publié le 24 juin 2026 une mesure de Prime Day 2026 (23 juin) : le trafic e-commerce états-unien référé par les IA a progressé de **+98,3 % en glissement annuel**, avec un taux de conversion **+50,7 % supérieur** aux autres canaux (reprise CMSWire, [Nicastro, 24 juin](https://www.cmswire.com/digital-experience/adobe-ai-shopping/)). Adobe donne trois indicateurs d'engagement supplémentaires : **+49,9 % de temps passé sur site, +20,5 % de pages vues, +33 % de taux d'ajout au panier** pour les visiteurs venus des IA versus les canaux classiques. Le total online day 1 est chiffré à **8,3 milliards de dollars** aux États-Unis, forecast Adobe sur les 4 jours à **26,3 milliards**.

Verbatim analyste Adobe Vivek Pandya (via CMSWire) : *« AI-powered chat services and browsers have cemented their role in the online shopping experience, providing utility for shoppers who value the speed and convenience »*.

**Ce qui change et ce qui reste à voir.** La direction contredit clairement la lecture faite un an plus tôt sur le même événement Prime Day (Adobe rapportait alors une conversion IA -23 % versus non-IA). Ce basculement s'inscrit dans la même tendance déjà mesurée par Adobe Q2 2026 (rapport 17 juin, retail conversion IA +54 % vs non-IA). La mesure est vendeur unique (Adobe) sur son panel client retail : la méthodologie exacte (échantillon, définition d'un « visiteur AI-referred », attribution) n'est pas publiée en détail au niveau de Prime Day. La direction est double-corroborée (Q2 aggregate + Prime Day event), les niveaux exacts restent à traiter avec la réserve du single-vendor.

Doctrine : [[concepts/metriques-visibilite-geo]] — le trafic IA passe de « présence » à « conversion mesurée » et cesse d'être un indicateur de vanité. À condition d'attribuer proprement côté analytics, la mesure des conversions issues des surfaces IA devient un revenu identifiable, pas une projection.

### B2 — Actualité SEO. Google Merchant Center : la vidéo produit devient éligible à la diffusion depuis le 30 juin, avertissements image 500×500 dès juillet

Google a activé le 30 juin 2026 la diffusion des vidéos produit soumises via l'attribut `video_link` du flux Merchant Center, et ouvert en même temps le contrôle qualité et de politique sur ces vidéos ([documentation officielle Google Merchant Center Help](https://support.google.com/merchants/answer/16989427?hl=en)). Depuis le 14 avril 2026, l'ajout de l'attribut était possible mais sans diffusion. Sur le même passage de spec, Google confirme le seuil minimum d'image produit à **500×500 pixels** : avertissements dès juillet 2026 pour les images plus petites, application obligatoire au **31 janvier 2027** (reprise [ALM Corp, juin 2026](https://almcorp.com/blog/google-merchant-center-product-data-specification-update-2026/) ; corroboration [Search Engine Roundtable](https://www.seroundtable.com/google-updates-some-merchant-center-product-spec-41171.html)).

**Portée opérationnelle**. Pour un site e-commerce, deux chantiers concrets s'ouvrent sur juillet-décembre. Un : soumettre des vidéos produit correctement structurées si le catalogue en dispose déjà (les vidéos deviennent visibles côté Shopping, AI Overviews shopping et AI Mode shopping). Deux : auditer le stock d'images produit sous 500×500 pixels et planifier le rehaussement d'ici fin janvier 2027, sinon les produits concernés seront désapprouvés à l'application. Google précise qu'il pourra ré-échantillonner en interne certaines images sous-dimensionnées à partir de sources voisines ou par upscaling IA, sans que cela dispense l'éditeur de fixer le catalogue.

Pilier Actualité SEO stricte (documentation Google effective à date). Doctrine : [[concepts/structural-information-geo]] — la vidéo devient un nouveau champ structuré éligible au retrieval côté Shopping.

### B3 — Actualité SEO. Cloudflare pay-per-crawl fête un an sans rétrospective officielle publiée

Le 1er juillet 2025, Cloudflare avait déclaré le « Content Independence Day » et lancé le programme pay-per-crawl en bêta privée ([blog Cloudflare, 1er juillet 2025](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/) et [Introducing pay per crawl](https://blog.cloudflare.com/introducing-pay-per-crawl/)). Un an plus tard, aucune rétrospective officielle Cloudflare n'a été publiée sur le blog à date du 1er juillet 2026 (dernière publication constatée : 25 juin 2026). Les chiffres publiquement disponibles restent ceux communiqués en 2025 puis actualisés fin 2025 : plus d'**un milliard de codes HTTP 402** renvoyés par jour par le réseau Cloudflare aux crawlers IA, ratios de crawls par visite référée mesurés à **~73 000:1 pour Anthropic, ~1 700:1 pour OpenAI, 195:1 pour Perplexity, 41:1 pour Microsoft** ([The crawl-to-click gap, 29 août 2025](https://blog.cloudflare.com/crawlers-click-ai-bots-training/)). AI Crawl Control est passé en disponibilité générale en août 2025 et étendu à tous les plans en avril 2026.

**Ce que l'absence de rétrospective signifie.** Elle n'est pas neutre. À un an, un opérateur qui a médiatisé « Content Independence Day » et qui aurait des chiffres favorables à communiquer (revenu marketplace, nombre d'éditeurs actifs, volume de transactions) publierait typiquement une note. L'absence de note à date, croisée avec la projection non corroborée StartupHub.ai à 500 M USD de revenu de première année (chiffre single-source flagé en édition précédente) et l'écart entre les 1 milliard de 402/jour et l'assiette effective de transactions, laisse ouverte la question du volume de transactions réellement payées via le marketplace, distincte du volume de refus. La [prédiction P-2026-06-30-v2-2](wiki/hypotheses.md) est donc à surveiller : condition = Cloudflare publie une rétrospective officielle avec métrique de revenu ou volume de transactions distincte du forecast StartupHub.ai, avant le 31 juillet 2026. À J+1, condition non tenue.

Pilier Actualité SEO. Doctrine : [[concepts/agentic-search]] — la couche identité/paiement des agents reste un chantier ouvert dont l'économie effective n'est pas publiquement chiffrée.

---

*SyntheticBrain, édition du 1er juillet 2026. Draft, non envoyé. Voir [[methodes/cadrage-boucle-edition-algorithme]] pour la mécanique de production.*
