# leenq IA AUTO : agent autonome de SEO technique

> Cadrage produit, 2026-07-09. Statut : spec, rien n'est codé. Évolution de leenq du module « maillage interne » vers l'agent qui tient la technique du site.

## En résumé

leenq ne détecte pas des problèmes, il les corrige, il vérifie que la correction tient, et il recommence chaque nuit.

Les outils du marché s'arrêtent au constat. Le pari de leenq est d'aller jusqu'à l'écriture, dans le code source du client, en pull request, avec une vérification avant la fusion et un droit de retour.

Le maillage interne, déjà construit, devient une règle parmi les autres dans le même moteur. Il n'est plus le produit.

Ce qui rend l'autonomie possible n'est pas la puissance du modèle. C'est le fait qu'on peut vérifier qu'une correction est juste **avant** que Google la voie.

## Le pari

Deux positions techniques, et elles sont liées.

**On écrit dans la source, jamais à l'edge.** L'injection entre le serveur et Google crée une divergence permanente entre ce que le dépôt contient et ce que le moteur voit. Les équipes techniques la refusent, elle se perd au changement d'hébergeur, elle ne survit pas au fournisseur qui la vend. Un correctif posé en pull request est relu, versionné, et il reste au client le jour où il part.

**On vérifie avant de fusionner, pas après avoir cassé.** Toute la sécurité du produit tient dans cette inversion.

## Les deux questions à ne jamais confondre

*Ma correction est-elle juste ?* Ça se vérifie en quelques minutes. On reconstruit le site, on crawle le déploiement de préversion, on rejoue les règles. Google n'intervient pas.

*Ma correction a-t-elle rapporté ?* Ça prend trente à quatre-vingt-dix jours dans la GSC, avec du bruit et une mise à jour d'algorithme qu'on ne contrôle pas.

Un agent qui agit seul n'a pas besoin de la seconde réponse. Il a besoin de la première, plus une garantie que la classe d'action qu'il exécute a une espérance positive par construction. Aplatir une chaîne de redirections n'est jamais négatif. Ça ne se mesure pas, ça se vérifie.

C'est ce découplage qui rend l'autonomie atteignable aujourd'hui.

## Le critère d'autonomie

Trois axes, aucun ne s'appelle « difficulté ».

**Rayon d'explosion.** Combien de pages une erreur touche.

**Réversibilité.** Un revert de commit suffit, ou l'index met des mois à revenir.

**Latence de détection.** L'erreur se voit en lisant la page, ou seulement dans la GSC au trimestre suivant.

Un H1 médiocre : une page, réversible en un commit, visible immédiatement. Trois voyants au vert, l'agent y va seul, alors même que le H1 demande un jugement sémantique.

Un 301 vers la mauvaise cible : signal consolidé au mauvais endroit, index lent à revenir, découverte à J+90. Trois voyants au rouge, validation humaine obligatoire.

La ligne ne passe pas entre déterministe et sémantique. Elle passe entre le coût de se tromper.

## Règle dure : l'autonomie n'est pas décidée par le modèle

Un modèle ne dit jamais « je suis sûr, je peux appliquer ».

La confiance auto-déclarée d'un LLM n'est pas un signal de sécurité, elle est mal calibrée par construction. Le modèle dira « sûr » sur un H1 faux et « incertain » sur un canonical trivialement correct.

Le droit d'agir est une propriété **de la classe d'action**, pas de l'inférence. Il est inscrit dans une table, hors ligne, et il se met à jour à partir du journal des actions passées et de leurs résultats mesurés.

Le modèle formule. La table autorise.

## Les modules

**0. Correspondance URL vers source.** Le module le plus dur, absent de toutes les specs naïves. Le crawl donne le HTML servi, la correction s'écrit dans le source. Il faut savoir que `/blog/balle-de-golf` est produite par tel objet, tel fichier, telle ligne. C'est du parsing d'arbre syntaxique sur un dépôt, ou une correspondance vers un `post_id` sur WordPress. Ce module décide quels sites leenq accepte, donc quel marché il adresse. C'est la barrière à l'entrée.

**1. Observation.** Crawl brut et crawl rendu, sitemap, robots, hreflang, canonicals, graphe de liens, profondeur, orphelines, GSC. Commodity, rien à inventer.

**2. Détection.** Moteur de règles déterministe. Pas de modèle, pas d'hallucination, coût nul.

**3. Décision.** Gabarit déterministe quand la cible est calculable. Modèle quand il faut formuler. La classe d'action détermine si la sortie part en application directe ou en proposition.

**4. Application.** Dans la source. Pull request sur Git, révision sur WordPress. Jamais d'écriture directe en production sans revue.

**5. Vérification avant fusion.** Build, crawl du déploiement de préversion, rejeu de toutes les règles, contrôle des invariants. Si un invariant saute, la PR se ferme d'elle-même. Quelques minutes.

**6. Mesure après fusion.** Chaque action est un pari daté, résolu à J+30 et J+90 en différence de différences contre des pages témoins. Cette mesure ne conditionne pas l'action. Elle conditionne l'élargissement du périmètre.

Le module 5 est la pièce qui manque à leenq aujourd'hui, et c'est celle qui autorise l'agent à se passer de l'humain.

## Le moteur de règles : ne pas courir après le nombre

Cinq cents règles est un piège. C'est le terrain de Screaming Frog et de Sitebulb, ils ont vingt ans d'avance sur les cas tordus, et sur un site de cinquante mille pages ça produit deux cent mille constats sur lesquels personne n'agit. C'est exactement pour ça que les audits meurent dans un tableur.

leenq ne sort pas des constats. Il sort **une file de diffs applicables**.

Le nombre qui compte n'est pas le nombre de règles, c'est le nombre de correcteurs vérifiés. Une règle sans correcteur est du bruit qu'on paie à crawler.

Trente règles avec trente correcteurs battent cinq cents règles avec douze correcteurs. Et la phrase qui vend n'est pas « je détecte 500 problèmes ». C'est « j'en ai réglé 43 cette nuit, et j'ai vérifié chacun ».

## La table des classes d'action

Le cœur du produit. Chaque ligne porte son niveau d'autonomie, et ce niveau se gagne, il ne se décrète pas.

| Zone | Classes d'action |
|---|---|
| **Verte** : l'agent applique seul | H1 manquant ou multiple, hiérarchie Hn désordonnée, meta description absente, ALT manquant, Open Graph, sitemap incohérent, chaîne de redirections aplatie, canonical pointant vers un 404, `nofollow` interne accidentel, directives contradictoires, lien interne mort, dimensions d'images |
| **Orange** : l'agent propose, l'humain valide | cible d'un 301, modification d'un canonical existant, ancres de maillage, liens internes ajoutés, cannibalisation, pagination et facettes, contenu dupliqué |
| **Rouge** : l'agent ne touche jamais | élagage, `robots.txt`, migration de masse, toute action qui retire une page de l'index |
| **Hors périmètre** | Core Web Vitals, rendu JavaScript, configuration serveur et CDN |

Deux nuances qui coûtent cher si on les rate.

**Ajouter un canonical n'est pas modifier un canonical.** Poser un self-canonical là où il n'y en a pas est bénin. Changer un canonical existant peut désindexer la page. Deux classes distinctes, deux zones différentes.

**Poser un 301 n'est pas choisir sa cible.** La pose est mécanique et va en zone verte. Le choix de la cible est un jugement à rayon large et à retour lent, il reste orange.

## Les invariants de préversion

« Le problème a-t-il disparu ? » ne suffit pas. Un agent qui corrige un H1 peut casser trois canonicals sans le savoir.

Le jeu minimal, vérifié sur le déploiement de préversion, avant la fusion :

la violation ciblée a disparu.

aucune nouvelle violation n'est apparue, sur l'ensemble du site et pas seulement sur la page touchée.

le nombre de pages indexables est inchangé.

le build passe.

la page répond en 200 et se rend.

le volume de contenu n'a pas bougé au-delà d'une tolérance.

Un seul invariant qui saute ferme la pull request.

## Données structurées : extraction, jamais génération

C'est le risque de sanction le plus élevé de tout le produit.

Un modèle à qui on demande un schema `Product` produira un prix, une note moyenne et une disponibilité. Ils seront plausibles et faux. Google traite un balisage qui ne correspond pas au contenu visible comme du spam structuré.

La règle est mécanique : **chaque champ de schema est extrait du DOM avec son sélecteur source**. Si le prix n'est pas dans la page, il n'entre pas dans le schema.

leenq ne produit pas des données structurées. Il produit la traduction en JSON-LD de ce qui est déjà affiché. C'est la doctrine « jamais de chiffre inventé », transposée dans du code.

Même logique pour le H1 : il se dérive du title, du slug, du premier paragraphe. Il n'affirme rien de nouveau.

## Ce qu'on ne construit pas

**Conversion WebP et AVIF, lazy loading, suppression de scripts.** Ce n'est pas du SEO, c'est de l'ingénierie front et de la chaîne de build. Le lazy loading appliqué sans discernement dégrade les Core Web Vitals dès qu'il touche l'image LCP, c'est un anti-pattern documenté. « Supprimer les scripts inutiles » est l'action qui détruira un client : inutile du point de vue d'un crawler, ça désigne la balise d'analytics, la bannière de consentement, le test A/B, le panier. Rayon catastrophique, effet immédiat sur le chiffre d'affaires. Ces trois lignes sont déjà résolues par `next/image`, par le CDN, par la plateforme.

**Envoi automatique du sitemap à Google.** L'endpoint de ping des sitemaps a été retiré, et l'Indexing API reste réservée aux offres d'emploi et aux événements diffusés. Le sitemap est lu au crawl. À revérifier avant toute promesse produit, mais ça ne rentre pas dans la roadmap.

**Les sites sans dépôt ni API d'écriture.** Un agent est aussi autonome que sa surface d'écriture. Sur un site legacy en FTP, c'est zéro. On refuse, et on l'assume.

## Le périmètre s'étend par la preuve

Les sept classes oranges ne le restent pas.

Chaque action appliquée est un pari daté, résolu en GSC contre des pages témoins. Le jour où mille cibles de 301 proposées par l'agent ont été validées par des humains sans qu'aucune régression soit mesurée, la classe passe au vert.

Ce n'est pas un réglage, c'est un résultat.

C'est là qu'est le seul actif non copiable. Un moteur de règles se réécrit en trois mois. Trois ans de journal d'actions résolues en GSC sur cent sites, non. Même logique que les benchmarks GSC agrégés dans `qadence/Corpus-Qadence.md` : la valeur dépend du nombre de sites connectés.

Le produit affiche ce compteur. Combien d'actions appliquées seules ce mois-ci, combien de régressions mesurées. Zéro régression sur mille actions est l'argument de vente, et c'est la seule preuve qui vaille.

## Les pièges connus

**Le constructeur de pages WordPress.** Si le client utilise un page builder, le `post_content` qu'on édite n'est pas ce qui s'affiche. La correction est écrasée au premier enregistrement. Détecter le builder au moment de la connexion et refuser le site, ou n'y appliquer que ce qui passe par l'API des métadonnées.

**Idempotence et conflits.** Que se passe-t-il quand la PR de l'agent entre en conflit avec un commit humain. Quand le CMS régénère la page et efface le correctif. Quand l'agent recorrige ce qu'un humain a délibérément défait. Il faut une mémoire des corrections révoquées : ce qu'un humain annule ne se réapplique pas.

**Le gel.** Pendant une migration, un lancement, une période commerciale forte, l'agent ne touche à rien. Un interrupteur, visible, par site.

**Le rollback n'est pas gratuit.** Sur Git, c'est un revert. Sur WordPress, c'est une révision restaurée, et si l'état des extensions a changé entre-temps, non. Et surtout : un rollback après que Google a vu le changement ouvre un second cycle de réindexation. D'où le module 5.

## Ce que leenq a déjà

Le crawl et le graphe interne. Les connecteurs `git`, `github`, `wordpress`, `nextdata` dans `lib/connectors/`. Le write-back gated en pull request et en révision, validé en réel (PR #9 sur organikk-next, chaîne WordPress complète). L'auth GSC. La boucle d'impact `lenkrr-impact` avec les paris `link_bets` et les verdicts J+30 et J+90.

Autrement dit : les modules 0 (partiellement), 1, 4 et 6 existent.

Manquent le moteur de règles généralisé (module 2), la table des classes d'action (module 3), et surtout la vérification de préversion (module 5).

Tant que le module 5 n'existe pas, leenq propose. Le jour où il existe, leenq agit.

## Le pain point, chiffré, sur un client réel

Leexi : SEO hors-marque à moins 43 % en six mois, cause racine une refonte sans 301 ni canonical, découverte des mois plus tard dans la GSC. Réparation faite à la main, 178 URLs testées une par une (`wiki/log.md`, 2026-06-09 et `prestation/clients/leexi.md`, 2026-07-02).

Le consultant SEO est jugé sur des résultats qu'il n'a pas les mains pour produire. Il recommande, un autre exécute, mal ou jamais, et il découvre les dégâts un trimestre plus tard.

C'est le produit.

## Le modèle commercial

**Le mode aigu vend.** Une refonte arrive, le consultant a peur, il branche le connecteur pour l'occasion. C'est la porte d'entrée, pas le produit.

**Le mode chronique facture.** Le connecteur reste, l'agent tourne chaque nuit, la facturation suit le portefeuille du consultant. Il ajoute un client, il ajoute un site, il paie plus.

Le consultant achète du levier, pas son remplacement. Il garde le jugement, qui est ce qu'il facture. L'agent prend les mains. La frontière entre les deux bouge dans le sens que la data autorise.

Le plan unique à 39 € par mois du squelette Stripe actuel ne correspond plus à ce produit. La tarification est à refaire, par site.

## Décisions ouvertes

Absorption de leenq maillage dans le moteur général, ou coexistence le temps de la transition.

Stacks supportées à la V1. Next.js sur dépôt Git d'abord, WordPress ensuite, rien d'autre.

Tarification par site, et seuil de pages.

Nom du produit : leenq reste, ou l'agent technique prend un nom propre.

Où vit le module 5 : un déploiement de préversion Netlify ou Vercel côté client, ou un build en bac à sable côté leenq.

## Ce qui n'est pas tranché

Le décompte « douze classes en zone verte, sept en orange » vient de notre propre liste, pas d'un audit de marché. Il donne un ordre de grandeur, pas une mesure.

Le retrait de l'endpoint de ping des sitemaps et la restriction de l'Indexing API sont à revérifier dans la documentation Google avant toute mention publique.

Le positionnement des acteurs qui appliquent des correctifs à l'edge est à vérifier de première main avant d'écrire quoi que ce soit qui les compare.

Pages liées : [[concepts/maillage-systeme]] · [[moc/moc-maillage]]
