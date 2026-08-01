---
date: 2026-08-01
edition: 2026-08-01-revue-presse-v2
pilier: Actualite SEO
context: cloud
---

# Bloquer les pages de résultats de recherche interne : la consigne officielle disparaît, la recommandation Mueller reste

Résumé
- Google a retiré des Search Essentials la ligne demandant de bloquer les pages de résultats de recherche interne du site, mais John Mueller continue publiquement de le recommander pour raisons de charge serveur et de qualité, dans l'épisode « Should you block your Search result pages? » du podcast Search Off the Record publié le 30 juillet 2026.
- Le déclassement passe de règle explicite dans les consignes à conseil de terrain non contraignant, sans qu'aucun texte officiel n'apparaisse en remplacement dans developers.google.com/search/docs/essentials.
- Google Business Profile connaît depuis le 27 juillet un bug qui remet en statut « Pending » des produits validés depuis plusieurs mois, sans action de l'annonceur ni lien avec Merchant Center (B1 Niche SEO).
- Google a averti fin juillet certains annonceurs qu'un numéro D-U-N-S de Dun & Bradstreet deviendra requis dans le flux de vérification de Local Services Ads pour des verticaux et utilisateurs US non précisés (B2 Business SEO).
- Google a répondu à une réponse d'AI Overviews reconnue comme problématique sur une requête liée à la race en attribuant la formulation aux pages source, en affirmant que le résultat n'apparaissait pas sur toutes les requêtes ni sur Gemini, sans reconnaître de responsabilité de son propre système génératif (B3 GEO).

---

## Info du jour — Actualité SEO

Dans l'épisode « Should you block your Search result pages? » du podcast Search Off the Record publié le 30 juillet 2026, Martin Splitt et John Mueller confirment que la consigne demandant de bloquer les pages de résultats de recherche interne à Googlebot ne figure plus dans Google Search Essentials, l'ensemble des règles officielles qui a remplacé les anciennes Webmaster Guidelines. Barry Schwartz couvre l'épisode dans [Search Engine Roundtable le 31 juillet](https://www.seroundtable.com/internal-search-results-google-guidelines-41794.html), Digital Phablet publie une reprise le 1er août avec des extraits verbatim ([lien](https://digitalphablet.com/digital-marketing/blocking-internal-search-results-guidelines-potential-issues/)), et Optimixed en fait un item de son [recap quotidien du 31 juillet 2026](https://www.optimixed.com/). Le podcast est référencé sur la page officielle Google [developers.google.com/search/podcasts/search-off-the-record](https://developers.google.com/search/podcasts/search-off-the-record) et sur l'archive publique [libsyn](https://search-off-the-record.libsyn.com/).

Mueller rappelle que la mention d'origine remonte aux premières Webmaster Guidelines, où les pages de résultats internes étaient rangées soit comme contenu généré automatiquement, soit comme espaces théoriquement infinis dans lesquels Googlebot pouvait rester coincé. Il précise que cette ligne a été supprimée du document, sans annonce dédiée dans le changelog developers.google.com/search/updates, et que la page Search Essentials actuelle n'y fait plus référence.

Sa recommandation personnelle, en revanche, ne change pas. Il conseille de continuer à bloquer ces URL par robots.txt ou noindex pour trois raisons qu'il détaille dans l'épisode. Un espace d'URL potentiellement infini généré par les combinaisons de requêtes internes consomme du budget de crawl sans contrepartie de contenu utile. Un site laissé ouvert à l'indexation de ces URL peut voir apparaître dans son index des combinaisons irrelevantes qui diluent la qualité perçue de la propriété. Une page de résultats internes qui affiche des termes injectés depuis l'extérieur peut faire apparaître dans l'index des URL contenant du vocabulaire de spam ou de pharmacie non liée, avec pour conséquence documentée un étiquetage « hacked content » du site dans Search Console.

L'écart entre la consigne retirée et la recommandation maintenue mérite d'être lu littéralement. La page Search Essentials, [developers.google.com/search/docs/essentials](https://developers.google.com/search/docs/essentials), ne contient plus la clause, ce qui signifie qu'un site indexant ses pages de résultats internes n'est plus en infraction avec un point nommé du document. Aucune sanction procédurale automatique n'est associée à cette pratique en elle-même. Mais les mécanismes cités par Mueller (dilution du crawl, dilution de la qualité, exposition au signal « hacked ») restent des voies indirectes par lesquelles ces URL peuvent affecter le classement.

Pour un consultant qui audite un site avec des pages de résultats internes non bloquées, la lecture opérationnelle est la suivante. Retirer la référence à la clause Search Essentials dans un rapport de recommandation, elle n'y figure plus. Conserver la recommandation technique de blocage, elle est portée en direct par le représentant Google le plus visible sur ces sujets. Distinguer les deux dans le livrable, en séparant « ce que le document officiel demande » de « ce que Google recommande dans une communication non-normative ».

Ce déplacement d'une consigne officielle vers une communication non-normative n'est pas isolé. Il rappelle le mouvement continu de simplification des Search Essentials engagé depuis leur renommage en 2022, avec plusieurs types de données structurées supprimés en janvier 2026 (practice problem, learning video, course info, estimated salary, special announcement, vehicle listing, dataset), un travail que Search Engine Land a documenté à mesure ([exemple](https://searchengineland.com/google-to-remove-more-search-features-including-practice-problems-nutrition-facts-nearby-offers-and-more-464255)). La page des consignes devient plus courte, tandis qu'une partie de la doctrine se retrouve exprimée uniquement dans le blog Search Central, dans le podcast Search Off the Record ou dans les prises de parole individuelles de Mueller, Illyes, Splitt et Sassman. Pour un consultant SEO qui se réfère aux consignes comme source de vérité opposable, l'implication pratique est de tracer chaque recommandation à un document et de dater son origine, plutôt que d'appuyer une exigence sur un souvenir des Webmaster Guidelines.

Novelty à assumer honnêtement : le fait lui-même (suppression de la ligne) date probablement d'une révision antérieure à l'épisode, non explicitement datée par Mueller. La publication du 30 juillet 2026 rend le fait visible et discuté publiquement, mais le changement de documentation n'est pas relié à une entrée précise du changelog Google Search Central. C'est une limite documentaire à porter dans un livrable.

---

## Brèves

### B1 — Niche SEO : bug de statut « Pending » sur les produits Google Business Profile depuis lundi 27 juillet 2026

Depuis le lundi 27 juillet 2026, des produits validés et publiés depuis plusieurs mois dans Google Business Profile repassent en statut « Pending », sans que l'annonceur ne les édite ni ne les resoumette. Le SEO local Bryan Bloom signale le problème sur [Local Search Forum le 30 juillet](https://localsearchforum.com/threads/all-gbp-products-stuck-in-pending-status-across-multiple-client-profiles.63330/), en indiquant que le bug touche l'ensemble de son portefeuille clients. Barry Schwartz reprend le signalement dans [Search Engine Roundtable le 31 juillet 2026](https://www.seroundtable.com/google-business-profiles-products-pending-status-bug-41793.html). Des fils d'utilisateurs ouverts dans la [communauté Google Business Profile](https://support.google.com/business/thread/425707118/products-stuck-in-%E2%80%9Cpending%E2%80%9D?hl=en) et [ici](https://support.google.com/business/thread/408893617/products-are-not-approving-and-approved-products-are-also-showing-pending?hl=en) rapportent la même chose sans réponse Google publiée à date.

Deux précisions factuelles importantes. Les profils affectés cités dans les fils publics n'ont pas de compte Google Merchant Center connecté, ce qui exclut une désynchronisation depuis un flux produit tiers. Le bug touche à la fois des produits nouvellement ajoutés et des produits déjà en ligne depuis plusieurs mois. Aucun communiqué officiel Google n'est publié à ce jour sur le forum Google Business Profile Help ni dans le fil Barry Schwartz.

Pour un consultant local qui gère plusieurs profils Business, l'implication concrète est de surveiller les tickets clients ouverts au motif « produits disparus des fiches », de ne pas retenter des soumissions massives qui pourraient déclencher des filtres anti-spam supplémentaires, et de conserver un journal des dates de statut pour reconstruire la fenêtre d'incident quand Google publiera une note technique. La récurrence de bugs Google Business Profile depuis juin 2026 (avis en « No Reviews Yet », WhatsApp bulk auto-attribution, avis disparaissant, produits en Pending) suggère une révision non communiquée du système de gestion des profils. C'est un signal terrain, pas une preuve.

### B2 — Business SEO : Google prépare l'exigence d'un numéro D-U-N-S pour la vérification de Local Services Ads sur des verticaux et utilisateurs US

Fin juillet 2026, Google a commencé à alerter certains annonceurs Local Services Ads qu'un numéro D-U-N-S obtenu auprès de Dun & Bradstreet deviendra requis dans le flux de vérification, pour des verticaux et utilisateurs US non précisés à ce stade. Barry Schwartz documente l'alerte dans [Search Engine Roundtable](https://www.seroundtable.com/google-local-service-ads-duns-41760.html). La page officielle [support.google.com/adspolicy/answer/13650402](https://support.google.com/adspolicy/answer/13650402?hl=en-GB) précise que Google s'appuie sur Dun & Bradstreet pour ses processus de vérification et qu'un D-U-N-S peut être demandé, sans que ce soit un pré-requis universel à la souscription.

Le fait franchement neuf ici est le passage annoncé d'un dispositif « peut être demandé » à un « sera requis » sur un sous-ensemble de verticaux et d'utilisateurs. Le document Google Ads Help [answer/85961](https://support.google.com/google-ads/answer/85961?hl=en) mentionne l'usage du D-U-N-S dans la vérification annonceur mais ne détaille pas la liste des verticaux concernés par le durcissement. La distinction opérationnelle importante : le D-U-N-S est un identifiant d'entreprise, il ne se confond pas avec le badge Google Verified (renommage de Google Guaranteed / Google Screened / License Verified by Google) déployé le 20 octobre 2025 pour les services locaux.

Pour un consultant qui gère des Local Services Ads pour des annonceurs US en verticaux « home & storefront » (plomberie, électricité, HVAC, entretien de pelouse, toiture, antinuisibles), il est utile de vérifier dès maintenant si le compte annonceur dispose déjà d'un D-U-N-S, et si non, d'initier la demande gratuite auprès de Dun & Bradstreet, dont le délai standard varie entre quelques jours et plusieurs semaines. Sans D-U-N-S enregistré dans le flux de vérification, une future demande peut ralentir la migration prévue vers Performance Max Pay-Per-Lead qui commence en août 2026 pour ces mêmes verticaux (annoncée par SEJ le 21 juillet dans [cet article](https://www.searchenginejournal.com/google-is-bringing-local-services-ads-into-google-ads/582816/)).

### B3 — GEO : Google renvoie une réponse d'AI Overviews sur une requête liée à la race aux pages sources plutôt qu'à son propre système génératif

Le 29 juillet 2026, Google a répondu à un cas signalé publiquement de réponse d'AI Overviews formulée en langue différenciée selon la race concernée par la requête. La couverture [Search Engine Roundtable](https://www.seroundtable.com/google-race-ai-overview-response-41787.html) documente la réponse Google, reprise dans un item du [recap Optimixed](https://www.optimixed.com/google-blames-website-for-race-based-ai-overview-error/). Google indique que la formulation contestée résulte des pages sources auxquelles AI Overviews se réfère, que le motif n'est pas présent sur toutes les requêtes, qu'il n'apparaît pas dans Gemini standalone, et qu'une enquête interne se poursuit.

L'angle éditorial se situe dans la nature de la réponse Google. Le mécanisme AI Overviews sélectionne des passages depuis un corpus de pages, les résume, et présente la réponse avec des citations. En attribuant la formulation aux pages sources, Google déplace la responsabilité rédactionnelle du système génératif vers les documents cités, sans documenter publiquement le mécanisme d'agrégation ou de pondération qui a produit cette formulation particulière. C'est la même ligne de défense articulée précédemment sur des cas d'hallucination visible (« nos systèmes se réfèrent aux pages », voir [Wikipedia AI Overviews](https://en.wikipedia.org/wiki/AI_Overviews)), transposée à un cas où la formulation contient un biais qui n'est pas dans une page source précise mais dans le résumé produit.

Pour un consultant GEO qui audite la présence de son client dans les AI Overviews, la lecture pratique est en trois points. Le fait qu'une phrase apparaisse dans AI Overviews ne signifie pas qu'elle est extraite verbatim d'une page citée : le résumé peut synthétiser plusieurs sources et introduire des formulations qui n'existent dans aucune. Vérifier la traçabilité claim-par-page-citée est un travail manuel non automatisable par la seule liste des URL de citation. La position Google d'attribuer la sortie du système à ses inputs a une portée doctrinale plus large que le cas race : elle borne à l'avance ce qu'AI Overviews reconnaîtra comme son propre problème.

---

Sources primaires et reprises consultées cette édition :
- [Search Off the Record — Should you block your Search result pages? — 30 juillet 2026](https://search-off-the-record.libsyn.com/)
- [Google Search Central — page podcast Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record)
- [Google Search Essentials — page officielle](https://developers.google.com/search/docs/essentials)
- [Search Engine Roundtable — internal search results — 31 juillet 2026](https://www.seroundtable.com/internal-search-results-google-guidelines-41794.html)
- [Digital Phablet — blocking internal search results — 1er août 2026](https://digitalphablet.com/digital-marketing/blocking-internal-search-results-guidelines-potential-issues/)
- [Optimixed — recap SEO daily news](https://www.optimixed.com/)
- [Search Engine Roundtable — GBP products pending bug — 31 juillet 2026](https://www.seroundtable.com/google-business-profiles-products-pending-status-bug-41793.html)
- [Local Search Forum — Bryan Bloom — 30 juillet 2026](https://localsearchforum.com/threads/all-gbp-products-stuck-in-pending-status-across-multiple-client-profiles.63330/)
- [Google Business Profile Community — thread 425707118](https://support.google.com/business/thread/425707118/products-stuck-in-%E2%80%9Cpending%E2%80%9D?hl=en)
- [Search Engine Roundtable — Google LSA D-U-N-S requirement](https://www.seroundtable.com/google-local-service-ads-duns-41760.html)
- [Google Ads Policy — D-U-N-S enrolment](https://support.google.com/adspolicy/answer/13650402?hl=en-GB)
- [Search Engine Roundtable — Google race AI Overview response — 30 juillet 2026](https://www.seroundtable.com/google-race-ai-overview-response-41787.html)
- [Optimixed — Google blames website for race based AI Overview error](https://www.optimixed.com/google-blames-website-for-race-based-ai-overview-error/)

---

Draft SyntheticBrain. Rien n'a été envoyé.
