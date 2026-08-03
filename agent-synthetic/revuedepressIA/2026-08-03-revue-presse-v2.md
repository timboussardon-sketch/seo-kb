# Algorithme — édition du 3 août 2026 (v2)

*Pilier info du jour : Business SEO*
*Pilier brèves : Actualité SEO, GEO, Recherche agentique*

**Résumé**

- Kevin Lee publie le 3 août sur Search Engine Land un texte qui découple citation IA et revenu : « A citation is visibility. A booked opportunity, incremental sales, and a new customer. That's performance. »
- Une étude Orbit Media du 22 juillet 2026 (97 sites B2B, 28,9 millions de sessions, juillet 2025-juin 2026) mesure un trafic IA à 0,5 % du total mais un taux de conversion médian par site 7 fois supérieur au référencement naturel de Google.
- Deux mesures convergent avec l'édition du matin (Aleyda Solis, 84-93 % de citations tierces sur le SaaS) : les citations ne sont pas la vente, elles filtrent la présence dans un écosystème tiers avant la vente.
- Barry Schwartz confirme le 3 août une volatilité SERP marquée les 1er, 2 et 3 août sur Semrush Sensor et Mozcast, sans confirmation Google, dans une cadence 2026 qui rend probable un core update en août ou septembre.
- Trois articles Search Engine Land publiés le 3 août (Lee, Casey Nifong sur Gemini, Adam Tanguay sur la recherche par prompts) convergent sur un même déplacement : la mesure ne peut plus reposer sur les impressions et les positions.

---

## Info du jour — Business SEO : ce que rapporte une citation IA n'est pas ce que rapporte un client

Le 3 août 2026 à 8h ET, Kevin Lee, cofondateur de BlitzMetrics et signataire régulier de Search Engine Land, publie [GEO for people who have to hit revenue targets](https://searchengineland.com/geo-hit-revenue-targets-484144). L'article attaque de front un flottement doctrinal : la plupart des conseils GEO optimisent une métrique de présence dans les réponses génératives, alors que la question demandée aux équipes SEO en interne est le pipeline commercial. Verbatim de l'article : « A citation is visibility. A booked opportunity, incremental sales, and a new customer. That's performance. The gap between them is where a lot of GEO budget goes to die. »

Le texte est une opinion éditoriale, pas une étude. Il ne s'appuie sur aucune donnée nouvelle. Nous le retenons pour deux raisons. Un, l'angle recoupe une doctrine que nous documentons depuis avril 2026 : le mot « visibilité » a une valeur zéro dans un pitch commercial parce qu'il ne se rattache à aucune unité mesurable côté chiffre d'affaires (voir [[concepts/tabou-visibilite]] dans le vault). Deux, l'article prescrit des tests opérationnels rares dans la littérature GEO : construire un « money-query set » de 50 à 100 requêtes de recommandation issues d'entretiens acheteurs réels, ne suivre les citations que sur ces requêtes, et relier ces citations au pipeline via balisage d'URL et CRM. Lee ajoute un délai attendu de « plusieurs semaines » entre la publication d'un contenu et son apparition dans une réponse générée, ce qui contredit l'attente d'un impact rapide.

Cette opinion prend du poids quand on la lit contre une mesure empirique publiée deux semaines plus tôt. Le 22 juillet 2026, Andy Crestodina, cofondateur d'Orbit Media Studios, publie [AI Traffic Conversion Rates: New Research from 97 B2B Websites and 29M visits](https://www.orbitmedia.com/blog/conversion-rates-ai-search/). Périmètre déclaré : 97 sites B2B ou générateurs de leads, 28,9 millions de sessions, fenêtre 1er juillet 2025-30 juin 2026, seuil d'inclusion 100 sessions référées IA par site. La catégorisation des conversions distingue événements de forte intention et faible intention, à partir des key events GA4 taggés manuellement. Trois chiffres tenus par les données publiées :

| Mesure | Valeur | Source |
| --- | --- | --- |
| Part du trafic IA dans le trafic total | 0,5 % (140 000 sessions sur 29 M) | Orbit Media 22 juillet 2026 |
| Taux de conversion ChatGPT | 2,08 % | Orbit Media 22 juillet 2026 |
| Taux de conversion référencement naturel Google | 0,5 % | Orbit Media 22 juillet 2026 |
| Rapport de conversion médian par site (IA vs organique) | 7x | Orbit Media 22 juillet 2026 |
| Rapport moyen agrégé sur l'échantillon | 3x | Orbit Media 22 juillet 2026 |
| Part de ChatGPT dans le trafic IA | 82,3 % | Orbit Media 22 juillet 2026 |

Deux lectures se combinent proprement. Le trafic IA reste marginal en volume : sur cet échantillon B2B, un demi pourcent des sessions. Le trafic IA convertit fortement au niveau site, avec un rapport médian par site qui domine la moyenne agrégée, ce qui indique que la plupart des sites de l'échantillon ont un trafic IA plus qualifié que leur trafic organique classique, mais qu'une minorité de sites tire la moyenne vers le bas. Andy Crestodina précise que ce motif tient sur environ deux tiers des sites de l'échantillon.

Trois caveats méthodologiques restent à documenter côté Orbit. Un, les 97 sites sont B2B et lead-gen, donc le résultat ne se transporte pas tel quel sur du ecommerce grand public ni sur du média. Deux, le seuil de 100 sessions référées IA par site exclut la longue traîne des petits sites où le trafic IA n'a pas atteint ce plancher. Trois, l'étude ne publie pas la distribution des conversions par site : impossible de savoir si les 7x médian sont tirés par une queue haute ou par un effet transverse.

Le lien avec l'édition du matin est direct. Aleyda Solis a mesuré le 2 août que 84 à 93 % du poids des citations en réponse générative pour le SaaS vient de sources tierces ([synthèse](https://www.optimixed.com/ai-search-is-a-3rd-party-citation-problem-with-an-on-page-corroboration-base-the-data-across-saas-ecommerce-and-finance-international-seo-consultant-author-speaker-aleyda-solis/) + [étude SaaS](https://www.aleydasolis.com/en/ai-search/saas-ai-search-optimization/)). Si l'écosystème tiers fabrique la citation et que le trafic IA converti au bout de la chaîne représente 0,5 % du volume mais plusieurs fois le taux de conversion organique, les deux mesures se complètent au lieu de se contredire. La citation est une condition de présence dans le mécanisme de recommandation. Le clic qui suit, quand il arrive, arrive prêt à convertir. Compter les citations sans compter les conversions revient à mesurer le premier morceau d'une chaîne et à ignorer le seul morceau qui paie les factures.

Trois implications opérationnelles ressortent pour un consultant qui doit défendre un budget devant une direction.

Un, la métrique attendue en revue de campagne ne peut pas rester la part de citations sur un échantillon large de requêtes. Sur des requêtes non commerciales, la citation est du bruit corrélé au trafic sans intention. La sélection d'un « money-query set » de 50 à 100 requêtes de recommandation, sélectionnées à partir d'entretiens buyers ou de tickets sales, filtre le signal utile.

Deux, la mesure du bout de chaîne demande un rattachement CRM. Les urls citées dans les réponses génératives ne portent pas de paramètre UTM par défaut, et Google Analytics n'attribue pas la source « ChatGPT » ou « Perplexity » de manière fiable sans paramètre. Kevin Lee recommande un balisage explicite par « money-query set » et un rattachement à une opportunité CRM. Nous ajoutons que ce balisage doit être fait avant la publication du contenu, pas après, sinon on perd la fenêtre de plusieurs semaines qu'il annonce.

Trois, la doctrine du contenu se durcit sur trois piliers déjà présents dans les mesures Solis et Indig : contenu de sélection acheteur, pas d'explainer générique ; données propriétaires publiées comme aimant à citation tierce (voir [[concepts/data-proprietaire]] dans le vault) ; auteur nommé avec expertise vérifiable, pas de byline anonyme. Kevin Lee juge le fichier `llms.txt` sans valeur et le schema.org comme « hygiène » sans effet de levier, ce qui est cohérent avec les mesures Vishwakarma et Digital Applied déjà documentées mais reste une opinion à corroborer.

Le déplacement décrit par Kevin Lee prolonge la nouvelle dimension pré-recherche identifiée dans l'édition geoSurge (v2 du 2 août) : la citation elle-même dépend d'un filtre d'éligibilité en amont, mais elle n'est pas la mesure finale. Nous ajoutons la 8e dimension à [[concepts/metriques-visibilite-geo]] : le rendement conversion par citation, mesuré sur un money-query set, avec un délai d'apparition attendu de plusieurs semaines. Une prédiction dérive : un outil de mesure GEO du marché ajoutera avant fin 2026 une colonne « conversion par citation » distincte de la colonne « part de citation », en réponse à ce déplacement.

---

## Brèves

### Actualité SEO — signal d'un core update Q3 : volatilité SERP marquée les 1er, 2 et 3 août

Le 3 août, Barry Schwartz [documente](https://www.seroundtable.com/google-search-ranking-volatility-august-1-41811.html) une volatilité SERP amorcée le samedi 1er août et prolongée les 2 et 3 août. Deux trackers indépendants confirment le pic : Semrush Sensor et Mozcast. Aucune confirmation Google, aucune signature de nom d'update. La discussion communautaire, forums cités par Schwartz, mentionne un remaniement des résultats avec préférence marquée pour les vidéos YouTube dans des verticaux non-vidéo. Rappel de contexte : les deux core updates confirmés de 2026 sont tombés en mars puis en mai. La cadence tenue depuis le début d'année rend probable un troisième update dans la fenêtre août-septembre. La volatilité mesurée les 1er-3 août pourrait signaler soit un précurseur non annoncé, soit un update de spam ou de qualité indépendant du core, soit une turbulence isolée sans annonce.

Le fait strictement neuf ici est la coïncidence entre un pic simultané sur deux trackers indépendants et un début de mois au calendrier Google historiquement propice aux updates. Ce que la donnée publique ne dit pas encore : les verticaux touchés (au-delà de la mention YouTube), l'ampleur mesurée sur des échantillons SISTRIX ou Similarweb, la persistance sur J+7. Nous suivrons dès qu'une lecture stabilisée sort, en cohérence avec la règle de sept jours d'attente que Google recommande pour interpréter un update.

### GEO — Search Engine Land publie le 3 août un cadre de mesure de la présence dans Gemini

Le 3 août à la même fenêtre éditoriale que Kevin Lee, Casey Nifong publie sur Search Engine Land [How to measure your brand's visibility in Gemini](https://searchengineland.com/measure-brand-visibility-gemini-484116). Le texte est une méthodologie, pas une étude. Nifong pose un constat opérationnel utile : les mentions dans Gemini n'apparaissent ni dans Google Search Console ni dans Google Analytics, et deux utilisateurs qui posent la même question à Gemini peuvent recevoir des réponses différentes selon la personnalisation, la localisation, l'historique conversationnel et la version du modèle. Trois méthodes prescrites : suivi manuel sur une bibliothèque de prompts par étape d'entonnoir, outils de mesure IA nommés (Profound, Scrunch AI, Otterly.AI, Peec AI, Semrush, Ahrefs), intégration analytics via trafic de renvoi, requêtes de marque et conversions assistées. L'article reconnaît une limite : aucune de ces mesures, prise seule, ne prouve l'influence de Gemini sur une conversion.

L'utilité pour un consultant qui bâtit une revue trimestrielle GEO tient à la superposition avec l'info du jour. Nifong prescrit la mesure de la présence dans Gemini. Kevin Lee prescrit la mesure du revenu par citation. La combinaison des deux couvre les deux étapes de la chaîne : présence côté génération, conversion côté site. Mono-source à ce stade, méthodologie non validée empiriquement dans l'article, à corroborer par une seconde étude qui compare l'un des outils cités à une mesure de conversion CRM.

### Recherche agentique — la recherche par prompts devient une couche de priorisation topique

Le même jour, Adam Tanguay publie sur Search Engine Land [Keyword research meets prompt research: A smarter way to prioritize topics](https://searchengineland.com/keyword-research-prompt-research-prioritize-topics-484128). L'article positionne la recherche par prompts comme une couche complémentaire de la recherche par mots-clés, pas comme un remplacement. La proposition opérationnelle est de croiser les intentions extraites de conversations réelles avec un assistant génératif et les volumes de recherche classiques, pour prioriser les sujets qui remontent des deux méthodes simultanément. Adam Tanguay dirige la croissance chez Jordan Digital Marketing et publie régulièrement dans Search Engine Land, la lecture est donc une opinion structurée par un praticien, pas une étude à échantillon. Ce que le texte apporte : une articulation opérationnelle entre les deux registres de la demande (requête à un moteur, prompt à un assistant), en évitant le piège de « prompt research remplace keyword research » qui circule depuis fin 2025.

Trois articles Search Engine Land publiés dans la même fenêtre le 3 août 2026 convergent sur un même déplacement : mesurer la présence dans les systèmes génératifs, mesurer le rendement conversion, mesurer les intentions par prompts. La convergence éditoriale d'une source de référence dans la même journée est un signal d'agenda plus qu'un fait empirique isolé.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
