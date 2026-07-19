---
type: revue-presse
title: Algorithme, édition 17 juillet 2026 (cloud matin)
date: 2026-07-17
edition: 2026-07-17
pilier: Business SEO
status: draft
sources: 10
confidence: high
tags: [revue-presse, algorithme, business-seo, geo, ai-mode, google, connected-apps]
---

# Google AI Mode intègre Instacart, Canva et YouTube Music. Un pan du parcours d'achat migre dans la réponse générative

## En bref

- Le 16 juillet 2026, Google a lancé aux États-Unis le programme Connected Apps dans AI Mode, avec Instacart, Canva et YouTube Music comme premiers partenaires listés.
- Un utilisateur qui prépare un dîner peut demander à AI Mode d'ajouter les ingrédients à un panier Instacart et passer commande sans quitter Google Search.
- Trois lignes de rupture pour un marchand ou un éditeur. La conversion sort du site pour se faire dans l'interface Google, la porte d'entrée « connecteur » remplace le référencement organique classique sur ces intentions Do, la liste des partenaires est décidée par Google sans procédure publique de candidature.
- Google ne documente ni le protocole d'intégration, ni le calendrier d'ouverture à d'autres marques, ni la présence d'un équivalent hors États-Unis.
- Trois brèves ferment l'édition. Gary Illyes recommande de retirer le champ lastmod du sitemap XML quand les dates sont fausses, un nouvel épisode de Search Off the Record précise ce que veut dire « discovered vs crawled not indexed » en 2026, et Google active par défaut les Local Inventory Ads dans les campagnes Shopping standard au 31 août 2026.

---

## L'info du jour. Google AI Mode connecte des applications tierces : la conversion sort du site, la sélection appartient à Google (pilier Business SEO)

Le 16 juillet 2026, Google a annoncé le déploiement aux États-Unis d'un programme de « Connected Apps » dans AI Mode, qui permet à l'utilisateur de lier son compte à une application tierce pour que la réponse générative puisse déclencher une action à sa place. L'annonce vient du blog Google, signée Chips Mistry (Senior Product Manager Search) et Biharck Araújo (Engineering Lead Search), sous le titre [Connect more of your apps to Search](https://blog.google/products-and-platforms/products/search/connected-apps/). Trois partenaires sont nommés au lancement : Instacart (courses alimentaires), Canva (design), YouTube Music (musique). La disponibilité est limitée aux États-Unis, en anglais, avec un déploiement échelonné sur la semaine du 14 juillet.

Les faits opérationnels sont recoupés sur plusieurs sources indépendantes. [Search Engine Land, Danny Goodwin, 16 juillet](https://searchengineland.com/google-ai-mode-adds-instacart-canva-and-youtube-music-integrations-482547), [TechCrunch, 16 juillet 9h00 PDT](https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/), [Engadget, Matt Tate, 16 juillet](https://www.engadget.com/2216707/google-ai-mode-now-integrates-with-canva-youtube-music-and-instacart/) et [MacRumors, 16 juillet](https://www.macrumors.com/2026/07/16/google-search-app-connectors/) documentent tous le même périmètre. Côté Instacart, un billet dédié [Instacart integrates with AI Mode in Google Search](https://company.instacart.com/updates/instacart-integrates-with-ai-mode-in-google-search) signé Anirban Kundu, CTO d'Instacart, décrit le fait technique côté marchand.

**Premier point, l'expérience d'achat se termine dans Google.** L'exemple récurrent dans les billets Google et Instacart est celui d'un utilisateur qui prépare un barbecue. L'utilisateur pose sa question à AI Mode, obtient une liste d'ingrédients, connecte son compte Instacart et voit la réponse se prolonger par un panier prêt au paiement. Le paiement se fait ensuite dans Instacart. Ce qui change n'est pas la présence d'Instacart dans la réponse, mais le fait que la transition entre l'idée et l'ajout au panier ne passe plus par un clic vers un site marchand. Google déclare, verbatim : « Starting to roll out this week in the U.S. » (rollout en cours au 16 juillet). Aucune projection chiffrée d'adoption n'est publiée par Google ou Instacart à ce stade.

**Deuxième point, l'entrée dans le programme est décidée par Google, sans procédure publique.** Le billet Google indique « working with a range of partners and look forward to launching with more apps soon » sans nommer d'autres marques, sans publier de guide d'inscription et sans procédure de candidature ouverte. L'article TechCrunch confirme l'absence d'information technique publique sur le mécanisme d'intégration (protocole, système d'autorisation, contraintes de conformité). Aucune source recoupée n'indique s'il s'agit du [Model Context Protocol](https://modelcontextprotocol.io/) ou d'une passerelle propriétaire Google. Le résultat est que l'accès à ce nouveau canal de conversion dépend, à cette date, d'un choix commercial de Google et non d'une norme technique ouverte que n'importe quel marchand pourrait implémenter.

**Troisième point, le fait touche un pilier différent des deux précédents.** Les deux dernières éditions Algorithme portaient sur la Recherche agentique (Perplexity SPACE, 16 juillet v2) et sur l'Actualité SEO (Google AI Mode s'auto-cite via Business Profiles, 16 juillet matin). Le programme Connected Apps ressort du pilier Business SEO parce que le point d'impact n'est pas l'algorithme de sélection dans la réponse, mais la sortie du site du parcours de conversion sur une catégorie d'intentions Do documentée depuis longtemps par la doctrine [[concepts/mots-cles-actionnels]] : « L'utilisateur attend une action à la fin (prise de contact, demande de démo, téléchargement, devis, achat). Il ne veut pas juste s'informer ». Sur ces intentions, une marque qui n'est ni Instacart, ni Canva, ni YouTube Music n'a plus aujourd'hui de mécanique documentée pour être l'exécutant de l'action, seulement d'être un candidat dans la réponse.

**Effet mesurable côté site marchand.** Trois métriques bougent, dans l'ordre.

Le taux de clic vers le site depuis les requêtes qui portent l'intention servie par un connecteur est destiné à baisser, parce que l'utilisateur n'a plus de raison de sortir de Google pour finir son achat. C'est cohérent avec la lecture opérationnelle déjà publiée dans les éditions précédentes sur la géométrie du trafic généré par les moteurs de réponse.

La conversion par utilisateur, sur les catégories où un partenaire connecteur existe, ne se mesure plus dans l'analytics du site marchand qui héberge le catalogue mais dans le back-office du partenaire (ici Instacart) et, à terme, potentiellement dans un back-office Google. Pour un marchand qui n'est pas partenaire (mais dont les produits sont référencés chez Instacart), la ligne de mesure passe par Instacart et non par une source Google directe. Aucun accès annonceur Google ne documente ce reporting au 16 juillet 2026.

La sélection du produit à l'intérieur de la réponse dépend de deux mécaniques distinctes qu'il faut ne pas confondre. La première est la citation classique dans la partie textuelle d'AI Mode, qui reste régie par les critères de [[concepts/agentic-search]] et [[concepts/metriques-visibilite-geo]] (part de citations, position, densité). La seconde est le contenu du panier Instacart livré par le connecteur, qui dépend du catalogue et des règles d'assortiment d'Instacart, pas d'un critère Google. Un même utilisateur peut voir un produit cité dans le texte et un autre produit ajouté au panier.

**Ce qui n'est pas documenté au 16 juillet.** Quatre points restent en attente.

- Le protocole d'intégration (OAuth, MCP, passerelle propriétaire) n'est pas décrit publiquement par Google. TechCrunch et Engadget le mentionnent explicitement comme absent des billets primaires.
- La procédure d'ajout d'un nouveau partenaire n'est pas publiée. Google ne renvoie ni vers un formulaire d'inscription, ni vers une page produit dédiée aux marchands intéressés.
- La disponibilité hors États-Unis n'est ni annoncée ni datée. Le billet Google précise « limited to AI Mode in the United States, in English ».
- Le mode de partage des revenus, la présence d'une commission ou la présence d'une place payante à côté des connecteurs organiques ne sont pas décrits. La question est distincte des annonces de formats publicitaires dans AI Mode déjà couvertes par les éditions précédentes.

**Lien doctrine.** Le fait modifie trois hubs.

[[concepts/mots-cles-actionnels]]. Le pattern « la seule requête qui compte en B2B est celle qui porte une action » se prolonge en B2C, mais avec un changement d'exécutant : l'action n'est plus exécutée par le site marchand, elle est exécutée par un partenaire connecteur choisi par Google. La cible SEO sur ces intentions se scinde en deux : gagner la citation textuelle dans AI Mode d'un côté, gagner (ou négocier) l'accès au canal connecteur de l'autre.

[[concepts/tabou-visibilite]]. La règle « ne pas vendre de la visibilité mais des leads ou des conversions » gagne une lecture supplémentaire. Sur les catégories couvertes par un connecteur, la conversion ne se mesure plus dans Google Analytics ni dans Search Console. Un consultant SEO qui vend un ROI sur ces intentions doit désormais préciser où la conversion se lit, et distinguer explicitement le canal organique (citation) du canal agentique (connecteur).

[[concepts/agentic-search]]. Le paradigme « être sélectionné par l'agent » gagne une variable supplémentaire : la marque n'est plus sélectionnée uniquement par un agent tiers (Comet, ChatGPT Work) qui vient sur son site. Elle est sélectionnée en interne dans le produit Google, via un connecteur applicatif. La bascule Perplexity SPACE (16 juillet v2) documente le côté runtime agent externe. Le programme Connected Apps documente le côté Google-as-runtime. Les deux dessinent la même ligne : l'interaction avec la marque ne passe plus par le site de la marque.

**Deux prédictions vérifiables.**

- P-2026-07-17-1 : d'ici le 31 décembre 2026, Google publie une procédure publique (page produit, page pour les développeurs, formulaire de candidature) pour l'inscription d'un nouveau partenaire au programme Connected Apps dans AI Mode. Résolution positive : URL publique documentée par une source secondaire. Résolution négative : absence de page publique à cette échéance, l'entrée reste sur invitation Google.
- P-2026-07-17-2 : d'ici le 31 mars 2027, au moins un marchand nommé publie une mesure interne du trafic référral ou des ventes attribuables au canal Connected Apps de Google AI Mode (au-delà des trois partenaires du lancement), avec un chiffre distinct de la mesure Google organique classique.

**Lecture opérationnelle** (à considérer comme lecture, pas comme consigne définitive).

- Marchands US concernés par une des trois catégories (courses, design, musique) : documenter en interne, avant élargissement du programme, comment se mesure la conversion générée par le connecteur et où elle s'attribue dans le stack analytics.
- Marchands hors des trois catégories mais sur intentions Do proches (livraison, planning, e-commerce d'ingrédients) : suivre la liste des futurs partenaires ajoutés au programme et se préparer à un scénario où l'accès au canal dépend d'une négociation commerciale avec Google.
- Consultants SEO qui portent la brique GEO : ajouter la ligne « présence dans un connecteur » à la cartographie [[concepts/metriques-visibilite-geo]], distinct de la ligne « part de citations ».

---

## Brèves

### Gary Illyes recommande de retirer le champ lastmod du sitemap XML quand les dates sont fausses (pilier Actualité SEO)

Sur Bluesky, Gary Illyes de Google répond à une question de Jason Kilgore qui demandait s'il valait mieux publier aucun `lastmod` ou un `lastmod` qui n'est pas fiable. Réponse verbatim rapportée par [Search Engine Roundtable, Barry Schwartz, 16 juillet, article 41697](https://www.seroundtable.com/google-lastmod-dates-incorrect-41697.html) et reprise par [Digital Phablet](https://digitalphablet.com/digital-marketing/google-skip-incorrect-lastmod-dates-for-better-results/) : « probably better off without the lastmods. at least you save a few bytes ». Le fait n'est pas une nouvelle politique documentée dans [developers.google.com/search](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), mais une clarification opérationnelle qui rejoint la position historique de Google sur la valeur d'un signal fiable versus un signal bruité. Pour un site qui produit des `lastmod` automatiques par le CMS sans lien avec un vrai changement de contenu, la recommandation est explicite : retirer le champ plutôt que le maintenir. À ne pas confondre avec une invalidation générale du sitemap ou du signal `lastmod` lui-même. Le sujet touche le cœur du travail d'un SEO technique, sans être une bascule d'algorithme.

### Search Off the Record précise ce que veut dire « Discovered vs Crawled Not Indexed » en 2026, en pointant explicitement l'AI-generated content (pilier Actualité SEO)

Google Search Central a publié le 16 juillet 2026 un nouvel épisode de son podcast [Search Off the Record intitulé « How to read the Indexing Report »](https://search-off-the-record.libsyn.com/), avec John Mueller et Martin Splitt. Repris par [Search Engine Roundtable, article 41701](https://www.seroundtable.com/google-crawled-not-indexed-quality-ai-content-41701.html) et [Optimixed](https://www.optimixed.com/google-on-discovered-vs-crawled-not-indexed-quality-issues-ai-generated-content/). Deux points sont utiles à retenir. D'abord, Mueller ne présente pas les statuts « Discovered - currently not indexed » et « Crawled - currently not indexed » comme des bugs à corriger par des ajustements techniques, mais comme le signal que Google a réduit son intérêt pour un site à cause d'un doute de qualité. Ensuite, l'épisode nomme explicitement le contenu généré par IA comme une cause probable de cette réduction quand le contenu « screams AI-generated and lacks anything new and unique ». Aucun chiffre n'est publié, aucune règle nouvelle n'est annoncée. Le fait vaut par sa position (canal officiel Google Search Central) et par la précision de la formulation, qui recoupe la doctrine [[concepts/data-proprietaire]].

### Google active par défaut les Local Inventory Ads dans les campagnes Shopping standard au 31 août 2026 (pilier Actualité SEO)

Le [changement documenté par Search Engine Land, article 482556](https://searchengineland.com/google-changes-default-local-inventory-ads-behavior-482556) précise que Google supprime le paramètre « Local products » et le remplace par un filtre « Inventory » à deux valeurs, Channel = Local et Channel = Online. La bascule prend effet le 31 août 2026. Deux effets à anticiper. Les annonceurs qui ont l'add-on Local Inventory Ads voient leurs LIA activés par défaut si aucune modification n'est faite avant cette date. Les annonceurs qui séparent leurs budgets in-store et online doivent reconfigurer explicitement leurs campagnes avec le filtre Channel pour préserver la répartition actuelle. Le fait est une modification de paramètre par défaut, sans annonce chiffrée sur l'impact attendu ni possibilité d'opt-out du nouveau système de filtres. Le sujet touche les marchands multi-canal (physique et en ligne). Pour un pur pure-player e-commerce sans magasin, le filtre Channel = Online préserve la logique actuelle sans effort particulier.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
