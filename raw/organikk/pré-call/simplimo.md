# Pré-audit — Simplimo (simplimo.ca)

## En résumé

Simplimo est une entreprise québécoise qui achète directement des propriétés aux particuliers : maison, immeuble à revenus, terrain. Sans courtier, sans commission, sans rénovation, sans garantie légale, avec une offre annoncée en moins de 24 h et une transaction en moins de 30 jours. Indicatif téléphonique 418, donc la région de Québec plutôt que Montréal.

**Le site n'existe presque pas.** Huit pages en tout, dont trois pages légales et de contact. Aucun article, aucune page ville, aucune page par situation. Le corpus complet tient en environ 3 400 mots. C'est une brochure, pas un site qui capte de la demande.

**Le socle technique est bâclé sur les détails qui comptent.** La fiche entreprise en données structurées déclare le numéro `+1-418-XXX-XXXX`, un placeholder jamais remplacé, servi sur la page d'accueil et sur la page contact, alors que le vrai numéro affiché est le 418-883-0536. La page FAQ ne porte aucun balisage `FAQPage`. Aucun balisage `LocalBusiness` nulle part, sur un business pourtant strictement local. Deux blocs `Organization` concurrents se contredisent sur l'accueil.

**Et surtout, la vraie matière est enterrée.** Les cinq situations qui amènent un vendeur pressé (préavis d'exercice ou saisie, succession ou décès, séparation ou divorce, transfert ou déménagement, vente rapide souhaitée) sont de simples titres H2 sur la page `/avantages/`. Chacune est une intention de recherche à part entière, chargée d'urgence et de conversion. Chacune mérite sa page, croisée avec la ville. C'est le gisement, et il n'est pas exploité du tout.

L'opportunité tient en une phrase : ici on ne répare pas un site, on le construit, sur un marché où l'intention est parmi les plus décisionnelles qui existent. Quelqu'un qui tape « vendre maison rapidement succession Québec » n'est pas en train de se cultiver.

Hook du call : « Votre page FAQ ne dit pas à Google que c'est une FAQ, et votre fiche entreprise déclare un numéro de téléphone qui n'existe pas : +1-418-XXX-XXXX. Ça se corrige en une heure. Le vrai sujet est ailleurs : vos cinq situations de vente sont des sous-titres, alors que ce sont vos cinq pages les plus rentables. »

Sources : relevés le 2026-07-09 sur simplimo.ca (sitemap_index.xml, robots.txt, HTML brut des 6 pages publiques, données structurées, en-têtes HTTP). GSC non disponible (prospect non connecté), à récupérer au call.

## 1. Diagnostic prospect

**Identité.** Simplimo, entreprise québécoise d'investissement immobilier. Téléphone 418-883-0536, courriel contact@simplimo.ca. Présence sociale déclarée en `sameAs` : Facebook, Instagram, TikTok. Aucune adresse postale publiée, aucun numéro d'entreprise (NEQ) trouvé sur le site. Zone desservie déclarée dans les données structurées : `CA-QC`.

**Offre.** Achat direct de la propriété au propriétaire. Les arguments affichés : sans intermédiaire, sans commission, sans rénovations, sans garantie légale, offre en moins de 24 h, transaction en moins de 30 jours, processus en quatre étapes.

**Modèle et conversion.** Le point de conversion unique est « Obtenir mon offre », un formulaire. Un appel téléphonique en secondaire. Deux aimants à emails existent déjà, servis par le plugin Lana Downloads : un « guide de vente » et une « checklist ». Le réflexe de capture est donc déjà là, il n'est simplement adossé à aucun contenu qui amène du monde.

**Positionnement émotionnel.** Le site parle de « préavis d'exercice », de succession, de séparation, de « tourner la page ». Ce sont des moments de vie difficiles, où le vendeur cherche de la vitesse et de la certitude, pas le meilleur prix au marché. C'est une donnée stratégique de premier ordre : la promesse n'est pas « je vous fais gagner de l'argent », c'est « je vous sors de là proprement et vite ».

**Technique.** WordPress 6.9.4, thème Kadence, extension Yoast SEO, derrière Cloudflare. Les 404 sont de vrais 404, ce qui est bon. Le `robots.txt` est soigné et autorise explicitement GPTBot, ClaudeBot, Google-Extended, CCBot, PerplexityBot et consorts. Quelqu'un s'est posé la question de l'IA. Il l'a posée sur le fichier le moins important.

**Pain probable (analyse interne, à ne pas répéter tel quel).** Le site a été refait entre novembre 2025 et avril 2026, et plus rien n'a bougé depuis trois mois. Il est propre, il est joli, il ne ramène personne. Un business d'achat de propriétés sans contenu organique dépend soit de la publicité payante, soit du démarchage, soit des deux. Le coût d'acquisition d'un vendeur en détresse par la publicité est élevé et il augmente. Chaque mois sans contenu organique, ils rachètent la même audience. À vérifier au call : d'où viennent leurs demandes aujourd'hui.

**À récupérer au call (GSC).** Impressions par mois, position moyenne, requêtes qui amènent des formulaires remplis, pages indexées, part du trafic de recherche par rapport au payant et au social. Aucun chiffre avancé tant que la GSC n'est pas lue. Demander aussi la fiche Google Business Profile, centrale pour un business local.

## 2. L'angle : la situation de vente, pas le service

**On ne démarre pas par « vendre sa maison », on démarre par la situation.** La requête générique est disputée par tous les courtiers du Québec et par les portails immobiliers, qui ont vingt ans d'antériorité. Simplimo n'a aucune chance dessus et n'en a pas besoin.

En revanche, personne ne traite sérieusement « je reçois un préavis d'exercice, qu'est-ce que je peux faire », « je dois vendre la maison de mes parents après un décès », « on se sépare, personne ne veut racheter la part de l'autre ». Ces requêtes sont rares individuellement, décisionnelles à 100 %, et le lecteur qui les tape est à quelques jours d'une décision.

**Pourquoi c'est défendable face à l'IA générative.** Une réponse d'IA sait expliquer ce qu'est un préavis d'exercice au Québec. Elle ne sait pas dire combien de jours il reste réellement une fois le préavis inscrit, ce qu'un acheteur direct peut faire dans ce délai, ni ce qui s'est passé sur les dernières transactions comparables. Simplimo possède cette donnée : leurs propres dossiers. Délais réels constatés, types de situations traitées, ce qu'ils achètent et ce qu'ils refusent. C'est de la donnée première, invérifiable ailleurs, et c'est exactement ce qui se fait citer.

**Le second axe : la ville.** Le business est local, l'indicatif 418 le confirme. Le croisement situation × ville est la structure naturelle du site, et il n'existe nulle part aujourd'hui.

**Le troisième axe, immédiat : un outil gratuit.** La question que se pose tout vendeur qui hésite entre un courtier et un acheteur direct est chiffrable : combien me reste-t-il, net, dans chaque scénario. Commission, délai de vente, rénovations à faire, mois de portage. Ils ont déjà deux aimants à emails, mais pas cet outil-là, alors que c'est le seul qui répond à la question au moment exact où elle se pose.

**Ce qu'on ne fait PAS en premier.** Pas de blog immobilier généraliste. Pas de « tendances du marché immobilier québécois », requête que les portails et les médias tiennent déjà et qui n'amène aucun vendeur pressé. Et pas de bataille sur « vendre sa maison sans courtier », trop large pour un site de huit pages sans historique.

**Le timing.** Le site est neuf, tout est encore à écrire, donc l'architecture peut être posée correctement du premier coup. C'est le seul moment où bâtir la structure ne coûte presque rien. Attendre douze mois, c'est devoir démolir. [À vérifier au call : ont-ils une échéance commerciale, une saison forte, un volume de dossiers à remplir.]

## 3. État des lieux SEO (relevé du 2026-07-09)

**Volumétrie.** Le `sitemap_index.xml` déclare trois sitemaps. Le `page-sitemap.xml` contient 8 URLs. Le `kadence_element-sitemap.xml` en contient 0. Le `lana_download-sitemap.xml` en contient 3 (les aimants à emails). Il n'existe aucun sitemap d'articles, parce qu'il n'existe aucun article.

| Page | Mots visibles | H1 servi |
|---|---|---|
| `/` | 516 | « Nous achetons votre maison, immeuble ou terrain rapidement… » |
| `/avantages/` | 965 | « Avantages » |
| `/faq-simplimo/` | 649 | « Foire aux questions » |
| `/a-propos-de-simplimo-vente-rapide-de-propriete-au-quebec/` | 509 | « À propos » |
| `/contact-simplimo/` | 400 | « Contactez-nous » |
| `/processus-vente-simplimo-2/` | 319 | « Comment ça fonctionne ? » |

**Ce qui est bien fait.** Les balises `title` et les meta descriptions sont travaillées, avec le mot-clé et une promesse. Les canoniques sont propres et auto-référentes. Les 404 sont de vrais 404. Le `robots.txt` autorise explicitement les robots d'IA, ce qui est une décision consciente et juste.

**Anomalie n°1 : un numéro de téléphone factice dans les données structurées.** Le bloc `Organization` déclare `"telephone": "+1-418-XXX-XXXX"`. Le placeholder n'a jamais été remplacé. Il est servi sur la page d'accueil et sur la page contact, pendant que le vrai numéro, 418-883-0536, s'affiche en clair juste à côté dans le texte. Pour un business local, la cohérence du nom, de l'adresse et du téléphone est un signal de base. Là, la donnée machine contredit la donnée humaine.

**Anomalie n°2 : deux blocs `Organization` qui se contredisent.** L'accueil en sert deux. Le premier liste Facebook, Instagram et TikTok en `sameAs`. Le second ne liste qu'Instagram et TikTok, et porte le téléphone factice. Deux définitions concurrentes de la même entité sur la même page.

**Anomalie n°3 : une page FAQ sans balisage FAQPage.** `/faq-simplimo/` contient 649 mots de questions et de réponses, et zéro `FAQPage`, zéro `Question`, zéro `Answer` dans les données structurées. Les moteurs de réponse et les IA génératives se nourrissent de ce format. La matière est écrite, elle n'est simplement pas déclarée.

**Anomalie n°4 : aucun balisage `LocalBusiness`.** Le site déclare `Organization` uniquement, alors que l'activité est géographiquement bornée, avec une zone desservie déjà écrite dans le code (`areaServed: CA-QC`). Aucune adresse postale publiée non plus.

**Anomalie n°5 : les H1 sont des libellés de menu.** « Avantages », « À propos », « Contactez-nous », « Foire aux questions ». Le `title` est optimisé, le H1 ne l'est pas. Sur `/avantages/`, dont le `title` est « Vente rapide de propriété sans courtier | Services Simplimo », le H1 dit « Avantages ». Le signal le plus visible de la page est vide.

**Anomalie n°6 : du poids pour rien.** Les pages internes pèsent entre 166 et 226 Ko de HTML pour 300 à 965 mots visibles. La page `/avantages/` fait 226 Ko de HTML pour 965 mots. C'est le coût de l'assemblage WordPress plus Kadence. [À vérifier avec un relevé Core Web Vitals avant de l'affirmer en réunion : le poids HTML seul ne prouve pas un problème de performance ressentie.]

**Le signal qui ouvre le pSEO.** Sur `/avantages/`, les H2 s'appellent : « Préavis d'exercice ou saisie », « Succession ou décès », « Séparation ou divorce », « Transfert ou déménagement », « Vente rapide souhaitée ». Cinq intentions de recherche distinctes, chacune avec son vocabulaire, son urgence et son cadre juridique, empilées comme des paragraphes sur une seule page. Le pattern est identifié par l'entreprise elle-même. Personne ne l'a décliné.

## 4. La stratégie pSEO : le croisement situation × ville

**Le principe.** L'autorité vient du croisement de plusieurs axes de découpe, chacun portant une donnée que les autres n'ont pas. Ici les axes sont évidents et déjà nommés par le client : la situation de vente, la ville, le type de bien. Aucun n'est exploité.

**Préalable.** Les corrections du bloc 3 (téléphone, `FAQPage`, `LocalBusiness`, H1, dédoublonnage `Organization`) se font avant, parce qu'elles prennent quelques heures et qu'elles conditionnent la crédibilité de tout le reste.

**M1. Un outil gratuit : le calcul du net vendeur** (Product-Led, capte l'email au moment de la décision)
- URL : `/outils/calculateur-net-vendeur/`, plus une variante `/outils/delai-vente-vs-offre-directe/`.
- Le calcul : ce qui reste au vendeur dans chaque scénario. D'un côté la vente avec courtier, avec le pourcentage de commission, les rénovations à faire, les mois de portage, les taxes. De l'autre l'offre directe. Le résultat est un chiffre et un nombre de jours.
- Donnée par page : les pourcentages de commission réellement pratiqués au Québec, sourcés. Les délais de vente moyens par région, sourcés. Aucun chiffre inventé, et surtout aucun chiffre qui flatte artificiellement l'offre Simplimo, sinon l'outil se retourne contre eux à la première vérification.
- Conversion : le résultat mène à « Obtenir mon offre », pré-rempli avec la propriété saisie.
- Dédup / anti-thin : deux outils maximum. Un outil, c'est un calcul qui rend un chiffre utilisable, pas un formulaire déguisé.

**M2. Situation × Ville** (le gisement)
- URL : `/vendre-<situation>/<ville>/`. Exemples : `/vendre-succession/quebec/`, `/vendre-preavis-exercice/levis/`, `/vendre-separation/beauport/`.
- Variable : le couple situation × ville. 5 situations connues, une quinzaine de villes crédibles dans la zone 418 pour commencer. On ne produit pas les 75 pages d'un coup.
- Donnée par page : la procédure québécoise réelle qui s'applique à cette situation, avec ses délais légaux et sa source officielle. Ce que Simplimo peut faire dans ce délai précis. Un dossier réel traité dans cette situation, anonymisé, avec le délai constaté. Et la donnée locale : délai de vente moyen constaté dans cette ville.
- Dédup / anti-thin : la page se crée seulement s'il existe une spécificité réelle à dire sur la ville, ou un dossier traité localement. Sinon, la situation reste au niveau régional et la ville n'a pas sa page. Objectif réaliste : 20 à 30 pages sur un an, pas 75.
- Anti-doublon : les cinq H2 de `/avantages/` deviennent cinq pages piliers de situation. `/avantages/` reste, allégée, et renvoie vers elles.

**M3. Les questions qu'on n'ose pas poser** (intention informationnelle à conversion élevée)
- La FAQ existe et fait 649 mots. Elle vaut une famille de pages.
- URL : `/questions/<question>/`. Exemples : vendre sans garantie légale au Québec, ce que ça implique. Combien de temps après un préavis d'exercice peut-on encore vendre. Qui paie le notaire dans une vente directe. Un acheteur direct paie-t-il moins que le marché, et de combien.
- Donnée par page : la réponse franche, y compris quand elle dessert Simplimo. La dernière question est la plus importante : un vendeur qui cherche « est-ce que je vais me faire avoir » et qui trouve une réponse honnête chez l'acheteur lui-même, c'est la seule preuve de confiance qui compte dans ce métier.
- Balisage `FAQPage` sur chacune, et regroupement dans la FAQ pilier.

**M4. Type de bien × Ville** (le dernier axe, le moins urgent)
- URL : `/acheteur-<type>/<ville>/`. Types déjà annoncés sur l'accueil : maison, immeuble à revenus, terrain.
- Donnée par page : ce que Simplimo achète et refuse dans cette catégorie, les critères réels.
- À ne lancer qu'une fois M2 validé, sinon on dilue.

### Priorisation

| Modèle | Pages possibles | Effort | Compétition | Intention / conversion | Données dispo | Priorité |
| --- | --- | --- | --- | --- | --- | --- |
| M0 Correctifs (téléphone, FAQPage, LocalBusiness, H1, schema) | 0 | Faible | n/a | Crédibilité de base | Fortes | 1 |
| M1 Calculateur du net vendeur | 2 | Moyen | Faible | Très forte | Moyennes (à sourcer) | 2 |
| M2 Situation × Ville | 20 à 30 | Moyen | Faible | Très forte | Fortes (leurs dossiers) | 3 |
| M3 Les questions qu'on n'ose pas poser | 10 à 15 | Faible | Faible | Forte | Fortes | 4 |
| M4 Type de bien × Ville | 15 à 20 | Moyen | Moyenne | Forte | Moyennes | 5 |

**Reco.** M0 dans la première semaine, c'est quelques heures de travail et ça remet la fiche entreprise d'aplomb. Puis les cinq pages piliers de situation, sans les villes, pour valider que le format prend. Puis le calculateur, qui donne un point d'entrée mesurable et une adresse email. Puis la déclinaison par ville, uniquement là où on a de la matière locale. M3 tourne en fond, c'est le moins cher à produire. M4 en dernier.

### Exemples de requêtes (volumes à sourcer, jamais inventés)

- M1 : « combien coûte un courtier immobilier Québec », « calcul net vendeur maison », « vendre avec ou sans courtier ».
- M2 : « vendre maison succession Québec », « préavis d'exercice vendre rapidement », « vendre maison séparation qui rachète », « vendre maison rapidement Lévis ».
- M3 : « vente sans garantie légale c'est quoi », « délai préavis d'exercice Québec », « acheteur maison comptant arnaque ».
- M4 : « acheteur immeuble à revenus Québec », « vendre terrain rapidement ».

Aucun volume, aucune position, aucune difficulté n'est avancée ici. On les sort après lecture de la GSC et du Keyword Planner.

### 7 règles pSEO appliquées

Anti-thin : une page ne se publie pas sans sa donnée propre. Données terrain : les délais légaux viennent des textes officiels québécois, les délais constatés viennent des dossiers de Simplimo, aucun chiffre inventé. Sourcing obligatoire sur chaque chiffre. Canonical propre, auto-référent. Maillage différenciant : chaque page de ville remonte vers son pilier de situation, et cite deux villes voisines, jamais la même paire. Un élément de Haute Surprise par page : le délai réel, le dossier anonymisé, la réponse honnête qui dessert Simplimo. Passage ancré de 150 à 200 mots signé par une personne réelle de l'équipe, pas par « Simplimo ».

## 5. Roadmap 90 jours

- **Sem. 1. Les correctifs.** Remplacer `+1-418-XXX-XXXX` par le vrai numéro. Fusionner les deux blocs `Organization`. Ajouter `LocalBusiness` avec l'adresse et la zone desservie. Baliser la FAQ en `FAQPage`. Réécrire les six H1 pour qu'ils portent l'intention et non le libellé du menu. Vérifier la fiche Google Business Profile et l'aligner sur le site. Puis lecture de la GSC pour établir le point de départ.
- **Sem. 2-4. Les piliers de situation.** Les cinq H2 de `/avantages/` deviennent cinq pages, une par situation, avec la procédure légale sourcée et un dossier réel anonymisé chacune. `/avantages/` est allégée et renvoie vers elles. Maillage, soumission du sitemap, contrôle d'indexation page par page.
- **Sem. 5-8. Le calculateur.** Production de l'outil du net vendeur, avec ses sources chiffrées. Branchement sur « Obtenir mon offre ». Mesure du taux de complétion et du taux de passage vers le formulaire, pas seulement du trafic. En parallèle, les six premières pages M3.
- **Sem. 9-12. La déclinaison par ville.** Extension des situations qui indexent et convertissent, uniquement vers les villes où on a une donnée locale à dire. Mesure en GSC : on garde ce qui indexe, on coupe le reste. Décision sur M4 selon les résultats.

## 6. Notes pour le call (45 min)

**Hook d'ouverture.** « J'ai regardé le code de votre site ce matin. Votre fiche entreprise déclare à Google un numéro de téléphone qui n'existe pas, `+1-418-XXX-XXXX`, alors que votre vrai numéro est affiché juste à côté. Et votre page FAQ ne dit nulle part à Google que c'est une FAQ. Ça, c'est une heure de travail. Le vrai sujet, c'est autre chose. »

Puis on ouvre `/avantages/` en direct et on montre les cinq H2 : préavis d'exercice, succession, séparation, transfert, vente rapide. « Voilà vos cinq meilleures pages. Aujourd'hui ce sont cinq sous-titres. »

**Questions à poser.**
- D'où viennent vos demandes aujourd'hui : publicité, social, démarchage, bouche-à-oreille ? Dans quelle proportion ?
- Combien de dossiers traitez-vous par mois, et sur quelles situations principalement ? (Cette réponse décide de l'ordre des cinq piliers.)
- Jusqu'où va votre zone : la ville de Québec, la région 418, tout le Québec ?
- Avez-vous une fiche Google Business Profile, et est-elle vérifiée ?
- Pouvez-vous partager des dossiers réels anonymisés, avec les délais constatés ? (Sans ça, M2 perd sa donnée propriétaire et devient un gabarit vide.)
- Qui a fait le site, et qui peut y toucher ?
- Le TikTok et l'Instagram : qui les alimente, et est-ce que ça ramène des dossiers ?

**Freins probables à lever.**

« Notre publicité fonctionne, pourquoi changer. » → On ne remplace rien. La publicité s'arrête le jour où on arrête de payer. Une page sur le préavis d'exercice qui se positionne continue de ramener des dossiers pendant des années. Les deux se cumulent, et le contenu fait baisser le coût du payant en réchauffant l'audience.

« Le SEO c'est long, nous on a besoin de dossiers maintenant. » → Sur des requêtes génériques, oui, c'est long. Sur « préavis d'exercice vendre maison », il n'y a presque personne en face. Ce sont des requêtes rares, mal servies, et le premier qui répond sérieusement les prend. On saura à la semaine 8 si les piliers indexent.

« On est une petite équipe, on n'a pas le temps d'écrire. » → Vous n'écrivez pas. Vous nous donnez vos dossiers et vos délais réels, c'est la seule chose qu'on ne peut pas produire à votre place. Le reste, c'est notre travail.

« Nos dossiers sont confidentiels. » → Ils le restent. On anonymise à la réception, et le contrat prévoit le cadre de traitement des données. Ce qui sert, c'est le délai et la situation, pas le nom.

**Closing.** Ils repartent avec la roadmap 90 jours datée et la liste des correctifs de la semaine 1, qu'ils peuvent faire vérifier par n'importe qui. La proposition se cale sur leur maturité : ils n'ont ni contenu, ni structure, ni pilotage, mais ils ont la donnée que personne d'autre ne possède. On construit le socle et les cinq piliers, puis on les rend autonomes sur le modèle qui gagne. Le système les assiste, il ne remplace pas leur équipe.

## 7. À vérifier / suite

- Relever les Core Web Vitals réels avant d'affirmer quoi que ce soit sur la performance. Le poids HTML seul (166 à 226 Ko pour moins de 1 000 mots) est un indice, pas une preuve.
- Vérifier l'existence et l'état de la fiche Google Business Profile. Pour un business local, elle pèse autant que le site.
- Confirmer la zone desservie réelle. L'indicatif 418 suggère la région de Québec, les données structurées disent `CA-QC` en entier. Les deux ne peuvent pas être vrais.
- Vérifier le statut juridique et le NEQ. Rien n'est publié sur le site, ce qui est une faiblesse de confiance sur un métier où le vendeur a peur de se faire avoir.
- Vérifier si une version anglaise est prévue. `/en/` renvoie 404, alors que les données structurées déclarent `availableLanguage: ['fr', 'en']`.
- Demander la GSC au call pour caler les cibles et les chiffres à J+90.
- Sortir ensuite la vraie liste de requêtes décisionnelles par situation, et le gabarit de page du pilier « préavis d'exercice ».
