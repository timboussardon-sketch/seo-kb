# Pré-audit — Horizon CRM (horizoncrm.fr)

## En résumé

Horizon CRM est un SaaS de gestion pour artisans du bâtiment, édité par Horizon CRM inc. (Québec), qui attaque le marché français avec le domaine horizoncrm.fr en miroir de horizoncrm.ca. Les deux domaines servent exactement le même corpus de 151 URLs.

**Les pages sont là, la structure ne suit pas.** 18 pages métier, 14 pages ville, 5 pages conformité, 89 guides. Le volume existe. Rien n'est optimisé : les pages métier et ville plafonnent à 280 mots, avec 59 % de recouvrement en 5-grammes entre Paris et Lyon. Les axes ne sont jamais croisés, aucune page ne combine un métier et une ville. Le corpus mélange deux marchés sur un seul domaine, et un guide sur les obligations CCQ au Québec se lit sur le .fr. En dessous, le cache CloudFront ignore le nom de domaine et sert la balise canonical du .ca sous le .fr, ce que j'ai reproduit dans les deux sens. Le contenu ne manque pas. C'est la structure qui ne tient pas.

**Ensuite : sortir un outil gratuit de chaque fonctionnalité.** Ils ont déjà les briques dans le produit, enfermées derrière l'abonnement à 99 € : calculateur de tonnage, calculateur de patio, devis, suivi des heures, dépenses terrain. Chaque fonctionnalité est un outil gratuit indexable, qui répond à une requête « Do » et qui capte l'email au moment exact de la décision. C'est le levier Product-Led : un artisan qui calcule son coût horaire sur leur outil est à un clic de l'essai gratuit. Aujourd'hui il ne peut même pas y accéder.

**Puis : répondre à toutes les questions produit, pour chaque métier et pour chaque fonctionnalité du CRM.** Chaque artisan pose les mêmes questions avant de choisir, et elles sont spécifiques à son métier. « Est-ce que je peux faire un devis de couverture avec des lignes de main-d'œuvre et de fourniture séparées ? » « Est-ce que le suivi des heures gère les compagnons sur plusieurs chantiers dans la journée ? » Aucune de ces réponses n'existe sur le site. Ce sont des requêtes que l'IA générative ne peut pas traiter à leur place, parce que la réponse est dans leur produit. C'est le croisement métier × fonctionnalité, et c'est le gisement le plus profond.

L'ordre est celui-là et il n'est pas négociable : on répare la structure, sinon les outils et les réponses produit travaillent pour le domaine canadien.

Hook du call : « Vos pages françaises disent à Google que la version de référence est sur votre domaine canadien. Ce n'est pas votre contenu, c'est votre CDN. » Sortie visée : un chantier structurel court, puis les outils gratuits, puis le croisement métier × fonctionnalité.

Sources : relevés le 2026-07-09 sur horizoncrm.fr et horizoncrm.ca (sitemap.xml, robots.txt, HTML brut de 12 pages, en-têtes HTTP). GSC non disponible (prospect non connecté), à récupérer au call.

## 1. Diagnostic prospect

**Identité.** Éditeur : Horizon CRM inc., 660 chemin Seigneurial, L'Épiphanie, Québec. NEQ 1181416083. Représentant légal : Francis Drainville. Téléphone 450-944-3123, contacts info@ et support@horizoncrm.ca. Aucune entité française : les mentions légales décrivent une « Représentation France » à l'adresse québécoise. Elles sont datées du 26 octobre 2023, alors que le site publie des guides sur l'e-facturation 2026.

**Offre.** SaaS tout-en-un pour artisans du BTP : devis, facturation, portail client, planning, suivi des heures, dépenses terrain, inventaire. Arguments de conformité affichés : NF525, e-facturation. Paiement via Stripe.

**Cibles annoncées.** Plombiers, électriciens, paysagistes, couvreurs, maçons, carreleurs, peintres, menuisiers, terrassiers, entrepreneurs généraux.

**Modèle et conversion.** Abonnement mensuel ou annuel. Premier palier « Essentiel » à 99 € / mois jusqu'à 2 utilisateurs, avec environ 15 % d'économie sur l'annuel. Points de conversion sur le site : « Démarrer gratuitement » (essai 7 jours), « Tester gratuitement », « Démo ». Le self-serve et la démo cohabitent, ce qui suppose un cycle court en bas de gamme et un cycle assisté au-dessus.

**Preuve sociale affichée.** « 200+ entreprises », note « 4,9/5 », déclarées en données structurées `AggregateRating` sur la page d'accueil. À vérifier au call : d'où viennent ces avis, sont-ils collectés sur une plateforme tierce. Un `AggregateRating` auto-déclaré sans source est un risque de pénalité manuelle.

**Pain probable (analyse interne, à ne pas répéter tel quel).** Ils ont payé (en temps ou en agence) pour un dispositif pSEO complet, et ils n'en voient pas le retour. Le réflexe naturel dans cette situation est d'écrire plus de guides. Ils l'ont fait : 89 guides, dont 29 qui n'ont rien à voir avec le bâtiment. Le problème n'a jamais été le volume de contenu. Chaque nouveau guide dilue un peu plus le sujet du site pendant que la balise canonical envoie l'autorité au domaine canadien. Ils rament dans le mauvais sens depuis probablement des mois.

**À récupérer au call (GSC).** Impressions par mois sur horizoncrm.fr et horizoncrm.ca séparément, position moyenne, pages effectivement indexées, requêtes qui rapportent des essais, nombre d'essais gratuits attribués au canal organique. Le rapport « Pages » de la GSC, section « Alternative avec balise canonique correcte », devrait confirmer le diagnostic technique. Aucun chiffre avancé tant que la GSC n'est pas lue.

## 2. L'angle : niche défendable d'abord

**On démarre par le socle technique, pas par le contenu.** C'est inhabituel et c'est justement ce qui rend l'angle crédible. Tant que le CDN sert une page du .ca sous le domaine .fr, tout contenu ajouté sur le .fr travaille pour le .ca. Chaque euro investi en rédaction est arrosé sur le mauvais domaine.

**La niche défendable, ensuite : la conformité réglementaire française du BTP.** C'est le terrain où Horizon CRM est le plus difficile à attaquer, pour trois raisons.

D'abord l'intention est décisionnelle. Un artisan qui cherche « logiciel de facturation conforme NF525 » ou « facturation électronique obligatoire artisan » est en train de choisir un outil, pas de se cultiver.

Ensuite ce sont des requêtes que l'IA générative ne dévore pas entièrement. Une réponse d'IA peut expliquer ce qu'est la NF525. Elle ne peut pas dire à l'artisan quel logiciel est certifié, à quelle date, sous quel numéro d'attestation. C'est de la donnée vérifiable, datée, qui appartient à l'éditeur.

Enfin ils ont la data propriétaire : leur propre attestation de conformité, leur calendrier d'implémentation de la réforme e-facturation, leurs formats de sortie (Factur-X, UBL), leurs plateformes de dématérialisation partenaires. Personne d'autre ne peut publier ça à leur place.

**Le levier qui vient juste après le socle : les outils gratuits.** Chaque fonctionnalité du produit est un outil indexable qu'ils gardent enfermé derrière l'abonnement. Sortir le calculateur de tonnage, celui de terrasse, le coût horaire d'un compagnon, c'est répondre à une requête « Do » avec un chiffre utilisable, et récupérer l'email d'un artisan qui est déjà en train de chiffrer un chantier. Les briques existent, il s'agit de les exposer.

**Puis le gisement de fond : les questions produit, par métier et par fonctionnalité.** 18 pages métier existent déjà (`/logiciel-plombier`, `/logiciel-carreleur`…), elles font 284 mots et n'énoncent qu'un slogan. Elles ne répondent à aucune des questions qu'un couvreur ou un électricien se pose avant de signer. Ces réponses sont dans leur produit et nulle part ailleurs, donc aucune IA générative ne peut les fabriquer à leur place.

**Ce qu'on ne fait PAS en premier.** On n'écrit pas un guide de plus. On ne va pas se battre sur « logiciel CRM » ni « logiciel gestion entreprise », requêtes génériques tenues par des acteurs installés à budget illimité. Et on ne touche pas aux 29 guides sur la restauration et le bien-être avant d'avoir tranché la question de fond : est-ce que Horizon CRM est un CRM BTP, oui ou non.

**Le timing (insight 5).** La réforme de la facturation électronique impose aux entreprises françaises de savoir recevoir des factures électroniques depuis septembre 2026, avec l'obligation d'émission qui suit par paliers. Ils ont déjà les pages `/e-facturation-france`, `/conformite-nf525`, `/devis-facture-conforme-france`. Le sujet est chaud, leurs pages sont en place, et elles pointent leur canonical vers le Canada. C'est le pire moment possible pour laisser ce bug en production, donc le meilleur moment pour appeler. [À vérifier : le calendrier exact des paliers e-facturation à la date du call, avant de l'affirmer devant eux.]

## 3. État des lieux SEO (relevé du 2026-07-09)

**Volumétrie.** 151 URLs au sitemap, identiques sur .fr et .ca. Répartition : 89 guides, 18 pages métier, 14 pages ville, 5 pages conformité, le reste en pages de service (aide, support, légal, tarifs).

**Ce qui est bien fait.** Le rendu est côté serveur : le HTML brut contient le H1, les H2, le titre, la meta description et les données structurées. Un crawler lit la page sans exécuter de JavaScript. Les données structurées sont riches et correctes dans leur forme : `SoftwareApplication`, `Organization`, `BreadcrumbList`, `FAQPage` avec `Question` / `Answer`, `LocalBusiness` sur les pages ville. Le robots.txt est propre et bloque bien les zones applicatives (`/dashboard/`, `/client/`, `/portal/`, `/auth/`). Les guides sont substantiels : 2 000 à 3 750 mots, datés, avec un « sujet principal » déclaré.

**Anomalie critique n°1 : le cache CDN ignore le nom de domaine.**

Reproduit deux fois, dans les deux sens, avec des paramètres d'URL jamais vus :

| Test | Requête | Canonical servie | Cache |
|---|---|---|---|
| A1 | `.fr/crm-construction-montreal?n=a7t3k1` | `www.horizoncrm.fr/...` | Miss |
| A2 | `.ca/crm-construction-montreal?n=a7t3k1` | `www.horizoncrm.fr/...` | Hit |
| B1 | `.ca/conformite-nf525?n=z9q4v8` | `www.horizoncrm.ca/...` | Miss |
| B2 | `.fr/conformite-nf525?n=z9q4v8` | `www.horizoncrm.ca/...` | Hit |

Le premier domaine qui demande une URL remplit le cache. Le second reçoit la copie de l'autre, avec sa balise canonical, ses balises hreflang, et son en-tête `x-cache: Hit from cloudfront`. En clair : la page `/conformite-nf525` servie sur le domaine français a déclaré à mon crawler que sa version de référence était sur le domaine canadien.

Même chose sur les sitemaps : au premier appel, `horizoncrm.ca/sitemap.xml` m'a renvoyé 151 URLs pointant toutes vers `horizoncrm.fr`. Au second appel, après vidage, il renvoyait bien ses propres URLs en `.ca`.

Ce que ça produit côté Google : une consolidation non désirée d'un domaine sur l'autre, non déterministe, invisible dans les outils classiques parce qu'elle dépend de l'état du cache au moment du crawl. Cause probable : la Cache Policy CloudFront n'inclut pas l'en-tête `Host` dans la clé de cache. Correction : ajouter `Host` à la clé, ou séparer les distributions par domaine.


**Anomalie critique n°2 : soft 404 généralisés.**

`https://www.horizoncrm.fr/page-qui-nexiste-pas-xyz123` renvoie **HTTP 200**, une page de 2 mots, sans `noindex`. Toute URL inventée, tout lien cassé, toute vieille URL supprimée renvoie 200. Sur un site qui vise le pSEO, c'est une porte ouverte à l'indexation de pages vides en volume. Correction : vrai 404 sur route inconnue.

**Anomalie n°3 : hreflang et marché mélangés.** `x-default` pointe vers le `.ca`. Surtout, le corpus n'est pas séparé par marché. Le domaine français sert :

- 6 pages ville québécoises (`/crm-construction-montreal`, `/crm-construction-laval`, `/crm-construction-gatineau`, `/crm-construction-sherbrooke`, `/crm-construction-trois-rivieres`, `/crm-construction-quebec`) ;
- une vingtaine de guides purement québécois : obligations CCQ 2026, licence RBQ, loi R-20, TPS/TVQ, CNESST, loi 25, recours pour impayé au Québec, contrat de déneigement saisonnier, calcul de tonnage de gravier.

Le guide « Obligations CCQ pour les entrepreneurs en construction au Québec en 2026 » fait 3 750 mots et il est servi sur horizoncrm.fr. Un plombier de Toulouse n'a aucun usage de la CCQ. Symétriquement, le `.ca` sert `/conformite-nf525` et `/e-facturation-france`. Chaque domaine porte le contenu de l'autre.

**Anomalie n°4 : les pages pSEO sont trop courtes.**

| Page                              | Mots visibles |
| --------------------------------- | ------------- |
| `/crm-batiment-paris`             | 284           |
| `/crm-batiment-lyon`              | 278           |
| `/crm-construction-montreal`      | 271           |
| `/logiciel-plombier`              | 284           |
| `/logiciel-plombier-chauffagiste` | 288           |

Recouvrement mesuré en 5-grammes : 59 % entre Paris et Lyon, 38 % entre `/logiciel-plombier` et `/logiciel-plombier-chauffagiste`. Les H1 et les titles sont bien différenciés, le corps ne l'est pas assez. À 280 mots dont une FAQ, ces pages n'ont pas de quoi se distinguer. Elles existent, elles ne prouvent rien.

**Le signal qui ouvre le pSEO.** Le pattern ville × métier est déjà là, mais jamais croisé. 14 villes et 18 métiers sont dans le sitemap comme deux listes parallèles. Aucune page `/logiciel-plombier-lyon`. Le gabarit existe, les données structurées `LocalBusiness` sont posées, personne n'a fait le croisement. C'est exactement la configuration où le pSEO paie.

## 4. La stratégie pSEO : le croisement d'axes

**Le principe.** L'autorité ne vient pas d'un modèle unique décliné à l'infini. Elle vient du croisement de plusieurs axes de découpe, chacun apportant une donnée que les autres n'ont pas. Aujourd'hui Horizon CRM a des axes isolés. On les croise, et surtout on remplit chaque page avec du réel.

**Préalable absolu.** Aucun modèle ci-dessous ne se lance avant la correction de la clé de cache CloudFront et des soft 404. Publier avant, c'est écrire pour le domaine canadien.

**M1. Un outil gratuit par fonctionnalité** (Product-Led, capte l'email au moment de la décision)
- Le produit contient déjà les briques. Le plan « Essentiel » liste noir sur blanc un « Calculateur tonnage/patio », en plus des devis, du suivi des heures, des dépenses terrain et de la gestion d'inventaire. Tout est enfermé derrière l'abonnement à 99 € par mois. Aucun de ces outils n'est indexable aujourd'hui.
- URL : `/outils/<calcul>/`. Exemples : tonnage de gravier, surface et matériaux d'une terrasse, coût horaire d'un compagnon chargé, marge réelle d'un chantier, montant d'un acompte conforme, TVA applicable selon le type de travaux.
- Variable : la fonctionnalité du produit. Volume estimé : 6 à 10 outils, un par brique existante.
- Donnée par page : le calcul réel, les taux en vigueur datés et sourcés, le résultat exportable en devis pré-rempli. Le passage de l'outil à l'essai gratuit se fait sur le résultat, pas sur une bannière.
- Dédup / anti-thin : un outil, c'est un calcul qui rend un chiffre utilisable. Pas un formulaire qui affiche une brochure. Aucun outil publié qui ne soit adossé à une fonctionnalité réellement dans le produit.

**M2. Questions produit × Métier × Fonctionnalité** (le gisement le plus profond)
- Le principe : chaque artisan pose les mêmes questions avant de choisir un logiciel, et elles changent selon son métier. La réponse est dans leur produit, donc l'IA générative ne peut pas la produire à leur place. C'est de la donnée propriétaire pure.
- URL : `/<metier>/<fonctionnalite>/`. Exemples : `/couvreur/devis`, `/plombier/suivi-des-heures`, `/electricien/portail-client`, `/paysagiste/gestion-inventaire`.
- Variable : le couple métier × fonctionnalité. 18 métiers × 10 fonctionnalités = 180 combinaisons possibles. On n'en produit pas 180.
- Donnée par page : les questions réelles que se pose ce métier sur cette fonctionnalité, et la réponse exacte du produit. Est-ce qu'un devis de couverture sépare la main-d'œuvre de la fourniture, ligne par ligne. Est-ce que le suivi des heures gère un compagnon réparti sur trois chantiers dans la même journée. Ce que le produit sait faire, et surtout ce qu'il ne sait pas faire. Captures d'écran du produit sur le cas du métier.
- Source des questions : le support et les appels de démo d'abord, les forums métier ensuite. Jamais une liste inventée.
- Dédup / anti-thin : page créée seulement si on a au moins trois questions réelles remontées du terrain et une réponse produit vérifiable. Sinon la paire métier × fonctionnalité n'existe pas. Objectif réaliste : 50 à 70 pages sur un an.

**M3. Conformité × Métier** (intention décisionnelle, la niche défendable)
- URL : `/conformite/<norme>-<metier>/`. Exemples : `/conformite/nf525-plombier`, `/conformite/e-facturation-electricien`, `/conformite/decennale-couvreur`.
- Variable : le métier. Environ 18 pages par norme, 3 normes solides (NF525, e-facturation, décennale). Environ 40 pages après filtrage.
- Donnée par page : le numéro et la date de leur attestation de conformité, les mentions obligatoires réellement exigées sur un devis de ce métier, un exemple de facture conforme, le calendrier d'obligation qui s'applique à la taille d'entreprise typique du métier, les formats de sortie supportés.
- Dédup / anti-thin : `/conformite-nf525` devient la page pilier et reçoit un lien de chaque page fille. Pas de page sans au moins une mention obligatoire propre au métier et un exemple de document.

**M4. Migration depuis l'outil actuel** (intention transactionnelle, très haute conversion)
- URL : `/migrer-depuis-<outil>/`. Ils ont déjà `/guides/remplacer-excel-gestion-construction`, `/guides/jobber-vs-horizon-crm-comparatif`, `/guides/integration-quickbooks-construction`. Le pattern est amorcé et jamais systématisé.
- Variable : l'outil quitté (tableur, logiciel de facturation, logiciel de devis, outil comptable).
- Donnée par page : le format d'export réel de l'outil source, ce qui se transfère et ce qui ne se transfère pas, la durée de reprise, le mapping des champs. Seul l'éditeur possède cette donnée.
- Dédup / anti-thin : une page par outil réellement supporté par leur import. Aucune page pour un outil qu'ils ne savent pas importer.

**M5. Métier × Ville** (intention décisionnelle locale, le croisement jamais fait)
- URL : `/logiciel-<metier>-<ville>/`. Exemples : `/logiciel-plombier-lyon`, `/logiciel-couvreur-nantes`.
- Variable : le couple métier × ville. 18 × 14 = 252 combinaisons possibles. On n'en produit pas 252.
- Donnée par page : le nombre d'entreprises du métier immatriculées dans le département (source ouverte : base Sirene de l'Insee), les règles locales qui changent le devis (zone ABF, PLU, aides locales à la rénovation), et un client réel du métier dans la région quand il existe.
- Dédup / anti-thin : page créée seulement si la donnée Sirene existe ET qu'il y a une spécificité locale à dire. Objectif réaliste : 60 à 80 pages. Les 6 pages ville québécoises sortent du domaine `.fr`.

### Priorisation

| Modèle | Pages possibles | Effort | Compétition | Intention / conversion | Données dispo | Priorité |
| --- | --- | --- | --- | --- | --- | --- |
| M0 Structure (cache, 404, séparation des marchés) | 0 | Faible | n/a | Débloque tout le reste | Fortes | 1 |
| M1 Un outil gratuit par fonctionnalité | 6 à 10 | Moyen | Faible | Très forte | Fortes | 2 |
| M2 Questions produit × Métier × Fonctionnalité | 50 à 70 | Moyen | Faible | Très forte | Fortes (support) | 3 |
| M3 Conformité × Métier | ~40 | Moyen | Faible | Très forte | Fortes | 4 |
| M4 Migration depuis l'outil actuel | ~6 | Faible | Faible | Très forte | Fortes | 5 |
| M5 Métier × Ville | 60 à 80 | Fort | Moyenne | Forte | Moyennes | 6 |

**Reco.** M0 d'abord, seul, et on mesure la reprise d'indexation avant d'écrire une ligne. Puis M1 : les briques existent déjà dans le produit, il s'agit de les exposer, pas de les inventer, et chaque outil devient un point d'entrée vers l'essai gratuit. Puis M2, le chantier de fond, celui qui construit l'autorité sur le croisement métier × fonctionnalité. M3 en parallèle de M2 tant que le sujet e-facturation est chaud. M4 quand on veut six pages à forte conversion pour un effort faible. M5 en dernier : le sourcing Sirene ne se bâcle pas, et c'est le modèle le moins défendable.

### Exemples de requêtes (volumes à sourcer, jamais inventés)

- M1 : « calcul coût horaire ouvrier bâtiment », « calculer tonnage gravier », « calculer marge chantier », « acompte devis travaux pourcentage ».
- M2 : « logiciel devis couvreur main d'oeuvre fourniture », « suivi heures compagnons plusieurs chantiers », « portail client artisan électricien », « gestion stock paysagiste logiciel ».
- M3 : « logiciel facturation conforme NF525 », « facture électronique obligatoire artisan bâtiment », « devis plombier mentions obligatoires ».
- M4 : « alternative Excel gestion chantier », « migrer de Jobber vers », « export devis logiciel facturation ».
- M5 : « logiciel plombier Lyon », « logiciel devis couvreur Nantes », « CRM artisan bâtiment Toulouse ».

Aucun volume, aucune position, aucune difficulté n'est avancée ici. On les sort après lecture de la GSC et du Keyword Planner.

### 7 règles pSEO appliquées

Anti-thin : une page ne se publie pas sans sa donnée propre. Données terrain : zéro chiffre inventé, la volumétrie d'entreprises vient de Sirene, les taux et calendriers viennent des textes officiels. Sourcing obligatoire sur chaque chiffre. Canonical propre : self-canonical, une seule version par domaine, `Host` dans la clé de cache. Maillage différenciant : chaque page fille remonte vers son pilier et cite deux pages sœurs pertinentes, jamais la même paire. Un élément de Haute Surprise par section : le numéro d'attestation, la donnée Sirene, le format d'export réel. Passage ancré de 150 à 200 mots par page, signé par un vrai auteur, pas « L'équipe Horizon CRM ».

## 5. Roadmap 90 jours

- **Sem. 1-2. La structure.** Correction de la Cache Policy CloudFront (`Host` dans la clé de cache) et vrai 404 sur route inconnue. Séparation des corpus : les guides et pages ville québécois quittent le `.fr`, les pages NF525 et e-facturation quittent le `.ca`. Chaque URL retirée part en 301 vers la page la plus proche, jamais en 410. Vérification hreflang et `x-default`. Puis lecture de la GSC pour établir le point de départ.
- **Sem. 3-4. Contrôle et cadrage.** On vérifie que l'indexation repart : rapport « Pages » de la GSC, disparition des « Alternative avec balise canonique correcte ». En parallèle, inventaire des fonctionnalités du produit qui peuvent devenir un outil gratuit (M1), et collecte des questions réelles remontées par le support et les appels de démo (M2). Cette collecte conditionne tout le reste, elle démarre tôt.
- **Sem. 5-8. Les outils gratuits.** Production de 3 à 4 outils M1, en commençant par ceux qui existent déjà dans le produit (tonnage, terrasse, coût horaire). Chaque outil rend un chiffre utilisable et propose l'export en devis. En parallèle, densification des 18 pages métier existantes, qui passent de 284 mots à un contenu qui prouve quelque chose. Maillage croisé, resoumission du sitemap, contrôle d'indexation page par page.
- **Sem. 9-12. Les questions produit.** Pilote M2 sur 3 métiers × 3 fonctionnalités, alimenté par les questions collectées en semaine 3. Mesure en GSC sur les outils et sur le pilote : on garde ce qui indexe et convertit, on coupe le reste. Extension du modèle gagnant. M3 (conformité) démarre si le calendrier e-facturation le justifie à ce moment-là.

## 6. Notes pour le call (45 min)

**Hook d'ouverture.** « J'ai crawlé vos deux domaines ce matin. Vos pages françaises disent à Google que la version de référence est sur votre domaine canadien. Et parfois l'inverse, ça dépend de l'heure. Ce n'est pas votre contenu, c'est la configuration de votre CDN. Je vous montre. »

Puis on montre le tableau des quatre tests. C'est reproductible en direct, en trente secondes, avec un paramètre d'URL au hasard. C'est la démonstration la plus forte du call, elle ne coûte rien et elle est vérifiable devant eux.

**Questions à poser.**
- Qui décide ici, et qui a la main sur la configuration AWS ? (Le correctif est chez un dev ou un devops, pas chez un rédacteur.)
- Les deux domaines sont-ils déclarés séparément en Search Console ? Que dit le rapport « Pages » sur les canoniques ?
- Quelle part des essais gratuits vient du canal organique, en France et au Canada séparément ?
- Le marché français, c'est quel poids dans l'objectif de l'année ? Une expansion sérieuse ou un test ?
- Les guides restauration, coiffure, ostéopathie : c'est un pivot produit assumé ou un essai de contenu ? (29 guides sur 89. Question de fond, à poser sans jugement.)
- Les « 200+ entreprises » et le « 4,9/5 » déclarés en données structurées : ils viennent d'où ?
- Y a-t-il une entité juridique française prévue ? (Les mentions légales datent d'octobre 2023 et ne décrivent qu'une représentation.)

**Freins probables à lever.**

« On a déjà fait le SEO, on a 150 pages. » → Exact, et c'est ce qui rend la situation frustrante. Le travail est fait. Il est servi sous le mauvais nom de domaine la moitié du temps. Écrire la page 151 n'y changera rien.

« C'est notre dev qui gère l'infra, on ne va pas y toucher. » → Le correctif est une ligne dans la Cache Policy CloudFront. Le risque de ne pas le faire est de continuer à financer du contenu qui travaille pour l'autre domaine.

« Le SEO c'est long. » → La partie longue, c'est de construire l'autorité sur un sujet. Ils l'ont déjà fait. Ce qu'on répare en premier, c'est un blocage technique, et la reprise d'indexation se mesure en semaines dans la GSC, pas en trimestres. On saura à la semaine 4 si le diagnostic était bon.

« On veut d'abord voir des résultats avant de s'engager. » → Justement. Le chantier des semaines 1 à 4 est court, borné, et son résultat est binaire : soit les canoniques se corrigent dans la GSC, soit je me suis trompé. C'est la meilleure porte d'entrée possible.

**Closing.** Ils repartent avec la roadmap 90 jours datée et le tableau des quatre tests, qu'ils peuvent refaire eux-mêmes. La proposition se cale sur leur maturité : ils ont l'équipe technique et le contenu, ils n'ont pas le pilotage. On démarre sur la structure, puis les outils gratuits, puis les questions produit par métier et par fonctionnalité. On les rend autonomes sur le modèle qui gagne. Le système les assiste, il ne remplace pas leur équipe.

## 7. À vérifier / suite

- Rejouer les quatre tests de cache la veille du call. Si le correctif a été déployé entre-temps, tout l'angle change, et il faut le savoir avant d'ouvrir la bouche.
- Confirmer le calendrier exact des paliers de la facturation électronique à la date du call, avant de l'affirmer devant eux. Marqué [à vérifier] tant que ce n'est pas sourcé sur un texte officiel.
- Vérifier ce que renvoie `/blog` : le sitemap le liste mais aucun article n'y est rattaché, les 89 guides vivent sous `/guides/`. Page vide ou page de listing ?
- Vérifier la présence d'un `noindex` sur les 6 pages ville québécoises côté `.fr`, et réciproquement. Aucun relevé pour l'instant, aucune meta robots trouvée sur les pages testées.
- Récupérer la GSC au call pour caler les volumes, la hiérarchie des cibles et les chiffres à J+90. Demander les deux propriétés, `.fr` et `.ca`.
- Sortir ensuite la vraie liste de requêtes décisionnelles sur l'axe conformité, et le gabarit de page du modèle M1.
