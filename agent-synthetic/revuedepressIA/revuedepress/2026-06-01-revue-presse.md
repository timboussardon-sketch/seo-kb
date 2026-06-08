# Algorithme — Core update de mai 2026 : le déploiement se termine, le bilan n'est pas encore lisible

*Édition du 2026-06-01. Revue de presse search/IA. Produite par SyntheticBrain. Chaque information renvoie à ses sources.*

## L'essentiel en 5 points

- Le core update de mai 2026, lancé le 21 mai, finit son déploiement autour du 4 juin. Tirer un bilan gagnants/perdants maintenant est prématuré.
- Google n'a pas publié de billet de blog dédié. La seule communication officielle est un message du Search Liaison et l'entrée du tableau de bord d'état de la recherche.
- C'est le deuxième core update de 2026, environ six à sept semaines après celui de mars. La cadence se resserre.
- Les résultats enrichis FAQ disparaissent par étapes : invisibles depuis le 7 mai, rapport et test supprimés en juin, support de l'API Search Console retiré en août.
- Dans les moteurs de réponse, la composition des sources citées se déplace : après le litige Reddit-Perplexity d'octobre 2025, YouTube est passé devant Reddit comme première source sociale citée.

## Info du jour : le core update de mai arrive en fin de déploiement, et c'est trop tôt pour en lire l'impact

*Entité : [[entities/gsc]].*

Google a lancé le core update de mai 2026 le 21 mai. Le déploiement annoncé prend jusqu'à deux semaines, ce qui place sa fin autour du 4 juin, donc dans les prochains jours. C'est confirmé par [Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rolling-out-now-478430), [Search Engine Journal](https://www.searchenginejournal.com/google-begins-rolling-out-may-2026-core-update/575589/), [Search Engine Roundtable](https://www.seroundtable.com/google-may-2026-core-update-landed-41380.html) et, côté francophone, [Abondance](https://www.abondance.com/20260521-2298953-google-core-update-mai-2026.html).

Trois faits méritent d'être notés, parce qu'ils décrivent comment Google conduit cet update plutôt que ses effets supposés.

D'abord, la communication. Google n'a pas publié de billet de blog dédié à ce core update. La seule source officielle est un message du Search Liaison et l'entrée du tableau de bord d'état de la recherche ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rolling-out-now-478430), [Search Engine Journal](https://www.searchenginejournal.com/google-begins-rolling-out-may-2026-core-update/575589/)). Le contenu de ce message est volontairement minimal : il s'agit d'« une mise à jour habituelle destinée à mieux faire ressortir un contenu pertinent et satisfaisant, pour des sites de tous types », et il n'y a « rien de nouveau ou de spécial à faire pour les créateurs tant qu'ils produisent un contenu satisfaisant pensé pour les personnes ». L'absence de billet reproduit ce que Google a fait pour le core update de mars 2026 ([Search Engine Journal](https://www.searchenginejournal.com/google-begins-rolling-out-may-2026-core-update/575589/), [Digital Applied](https://www.digitalapplied.com/blog/google-may-2026-core-update-rolling-out)).

Ensuite, la cadence. C'est le deuxième core update de 2026. Le précédent, celui de mars, s'est déroulé du 27 mars au 8 avril. Six à sept semaines séparent donc la fin de l'un du lancement de l'autre ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rolling-out-now-478430), [Digital Applied](https://www.digitalapplied.com/blog/google-may-2026-core-update-rolling-out)). Deux updates rapprochés réduisent le temps disponible pour mesurer l'effet du premier avant que le second ne commence à modifier les classements. Pour un site qui a perdu de la visibilité en mars, distinguer la part de mars de celle de mai devient plus difficile.

Enfin, le calendrier de lecture. Le déploiement n'est pas terminé, donc les données ne sont pas stables. Des observations préliminaires côté francophone évoquent des secteurs touchés (finance, santé, e-commerce, SaaS, services locaux), selon [premiere.page](https://premiere.page/blog/actualites/core-update-mai-2026-impact-secteurs/) et [Abondance](https://www.abondance.com/20260521-2298953-google-core-update-mai-2026.html). Nous ne les reprenons pas comme un constat établi : ce sont des remontées de quelques jours, sur un déploiement en cours, et elles relèvent encore de l'impression de terrain. Les analyses construites sur un échantillon large arrivent en général après la fin du déploiement. Notre lecture : attendre la stabilisation avant de réorganiser quoi que ce soit, et se méfier des listes gagnants/perdants publiées avant le 4 juin.

Sur le fond, le seul levier que Google répète à chaque core update est la qualité et la pertinence du contenu, sans liste de signaux précis. Cela rejoint un constat de doctrine que nous tenons par ailleurs : au retrieval, ce sont les champs structurels (title, meta, headings, données structurées) qui comptent le plus au retrieval, davantage que la réécriture du corps de texte (voir `wiki/concepts/structural-information-geo.md`). Un site dont le contenu est correctement structuré et attribué est plus lisible pour les systèmes de classement, et cette lisibilité ne dépend pas de la sortie d'un core update. C'est une base à tenir indépendamment des updates, pas une réaction à celui-ci.

## Brèves

### Résultats enrichis FAQ : l'échéancier de retrait se concrétise en juin

Google a annoncé le 7 mai 2026 l'arrêt du support des résultats enrichis FAQ. Le retrait se fait par étapes, et c'est en juin qu'il devient concret côté outils. Les résultats enrichis FAQ ne s'affichent plus dans la recherche depuis le 7 mai. Le rapport « résultats enrichis » FAQ, l'apparence dans la recherche et le support dans le test de résultats enrichis disparaissent en juin 2026. Le support dans l'API Search Console s'arrête en août 2026 ([Search Engine Land](https://searchengineland.com/google-to-no-longer-support-faq-rich-results-476957), [Search Engine Journal](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/), [Passionfruit](https://www.getpassionfruit.com/blog/what-changed-with-google-drops-faq-rich-results-and-what-to-do-now)). Concrètement : le balisage FAQPage reste valide et peut rester en place sans risque, mais il ne produit plus d'affichage enrichi. Les équipes qui récupèrent des données FAQ via l'API Search Console ont jusqu'en août pour adapter ces appels.

### Moteurs de réponse : la composition des sources citées se déplace après le litige Reddit-Perplexity

Reddit a poursuivi Perplexity en octobre 2025 pour récupération non autorisée de contenu, en lui reprochant de contourner son API payante et d'ignorer les instructions robots.txt ([Search Engine Journal](https://www.searchenginejournal.com/perplexity-responds-to-reddit-lawsuit-over-data-access/559148/)). Depuis, la part de citations issues de Reddit dans les moteurs de réponse a fortement baissé. Une analyse de Conductor relayée par [CMSWire](https://www.cmswire.com/digital-marketing/reddits-rise-in-ai-citations-what-marketers-must-know-about-aeo-strategy/) mesure une chute d'environ 23 % de la part de Reddit en un seul mois entre octobre et novembre 2025. Sur la même période, YouTube est passé devant Reddit comme première source sociale citée, et apparaîtrait désormais dans environ 16 % des réponses générées contre environ 10 % pour Reddit ([PikaSEO](https://pikaseo.com/articles/youtube-overtakes-reddit-ai-citations)). Ce que ça dit pour la visibilité : la liste des sources qu'un moteur de réponse accepte de citer peut changer vite, sous l'effet d'une décision juridique ou d'un changement d'accès aux données, indépendamment de la qualité du contenu. Bâtir une stratégie de citation sur une seule plateforme tierce reste fragile.

### Part de marché : le search par IA progresse vite mais reste minoritaire en volume de visites

Au-delà des annonces, l'ordre de grandeur mérite d'être rappelé. Selon les données StatCounter de mars 2026, Google reste autour de 90 % du trafic de recherche mondial et Bing autour de 5 % ([Digital Applied](https://www.digitalapplied.com/blog/search-engine-market-share-2026-global-data), [Searchlab](https://searchlab.nl/en/statistics/search-engine-market-share-statistics-2026)). Les renvois de trafic provenant des moteurs IA, eux, sont mesurés autour de 0,9 % du total des visites en mars 2026, en hausse forte sur un an mais à partir d'un niveau bas ([Digital Applied](https://www.digitalapplied.com/blog/search-engine-market-share-2026-global-data)). Ces chiffres viennent d'agrégateurs de mesure d'audience, à manier comme des ordres de grandeur. Ils ne contredisent pas l'importance de la visibilité dans les réponses IA, mais ils situent l'enjeu : la croissance est rapide, la part absolue de visites apportées reste faible. Les deux constats sont vrais en même temps.

---

*Rien n'a été envoyé. Ceci est un draft produit par SyntheticBrain. Les informations du corps reposent sur au moins deux sources indépendantes, sauf mention explicite de caractère préliminaire.*
