# leenq IA AUTO : agent autonome de SEO technique

> Cadrage produit, 2026-07-09. Statut : spec, rien n'est codé. Évolution de leenq du module « maillage interne » vers l'agent qui tient la technique du site.

## En résumé

leenq ne détecte pas des problèmes, il les corrige, il vérifie que la correction tient, et il recommence chaque nuit.

Aucun humain ne valide. Il n'y a pas de file d'attente d'approbation, il y a un dashboard de contrôle. La sécurité ne vient pas d'un clic, elle vient de quatre mécanismes : la vérification avant fusion, un budget d'actions par nuit, un déploiement progressif par classe, et un retour arrière automatique.

Ce qui rend l'autonomie possible n'est pas la puissance du modèle. C'est le fait qu'on peut vérifier qu'une correction est juste **avant** que Google la voie.

Acheteur : le consultant SEO, qui tient six à dix sites clients depuis un écran. Tarif par site. Il garde le jugement, l'agent prend les mains.

Le maillage interne, déjà construit, devient une règle parmi les autres dans le même moteur. Il n'est plus le produit.

## Le paysage, vérifié le 2026-07-09

**Okara** (`okara.ai/agent/seo`, ~66 $/mois) audite le site chaque jour et livre « 2 high-impact recommendations daily with step-by-step guides and copy-ready snippets ». Title, meta, Open Graph, ALT, H1, canonicals, liens cassés. Plus un suivi des citations dans ChatGPT, Perplexity, Gemini. **Il n'écrit pas sur le site.** Le livrable final est un extrait à coller à la main.

**Polsia** (`polsia.com`) n'est pas un produit SEO. C'est une plateforme d'agents autonomes : identité persistante, mémoire, outils, exécution planifiée, boucle précâblée, cycles quotidiens sur données réelles. Le « RankPilot » qui remonte en recherche vit sur `rankpilot-7.polsia.app` et semble être une app construite **sur** Polsia par un tiers, pas un produit de Polsia. À vérifier.

Screaming Frog, Sitebulb, Semrush, Ahrefs : détection seule.

Sur WordPress, les plugins SEO écrivent déjà seuls les canonicals, les Open Graph et le sitemap. Ce n'est pas de la détection. leenq ne peut pas se vendre là-dessus à un utilisateur WordPress.

Dans le haut de marché, des acteurs appliquent réellement, en injectant les correctifs **à l'edge**. Vérifier leur positionnement de première main avant d'écrire une page qui les compare.

**Conclusion : personne n'écrit dans la source du client.** C'est la ligne de démarcation, et c'est la partie difficile.

## Le pari

Deux positions techniques, et elles sont liées.

**On écrit dans la source, jamais à l'edge.** L'injection entre le serveur et Google crée une divergence permanente entre ce que le dépôt contient et ce que le moteur voit. Les équipes techniques la refusent, elle se perd au changement d'hébergeur, elle ne survit pas au fournisseur qui la vend. Un correctif posé en pull request est relu, versionné, et il reste au client le jour où il part.

**On vérifie avant de fusionner, pas après avoir cassé.** Toute la sécurité du produit tient dans cette inversion.

## Les deux questions à ne jamais confondre

*Ma correction est-elle juste ?* Ça se vérifie en quelques minutes. On reconstruit le site, on crawle le déploiement de préversion, on rejoue les règles. Google n'intervient pas.

*Ma correction a-t-elle rapporté ?* Ça prend trente à quatre-vingt-dix jours dans la GSC, avec du bruit et une mise à jour d'algorithme qu'on ne contrôle pas.

Un agent qui agit seul n'a pas besoin de la seconde réponse. Il a besoin de la première, plus une garantie que la classe d'action qu'il exécute a une espérance positive par construction. Aplatir une chaîne de redirections n'est jamais négatif. Ça ne se mesure pas, ça se vérifie.

C'est ce découplage qui rend l'autonomie atteignable aujourd'hui.

## Pourquoi il n'y a pas de validation humaine

Parce qu'elle est du théâtre.

Un consultant qui reçoit quarante pull requests par nuit ne les lit pas. Il clique. Le bouton « approuver » ne produit pas de sécurité, il produit une signature. Il transfère la responsabilité sans réduire le risque.

On ne supprime pas le garde-fou, on le déplace de l'humain vers la machine et vers une politique. Quatre mécanismes le remplacent, et ils font le travail mieux qu'un clic.

**La vérification de préversion.** Build, crawl, invariants, fusion. Elle valide la correction mieux qu'un humain qui survole un diff.

**Le budget de rayon.** Un plafond d'actions par nuit, par classe, par site. Si l'agent se trompe, les dégâts sont bornés par construction.

**Le déploiement progressif.** Une classe commence sur cinq pages. On attend, on mesure, on passe à cinquante, puis au site.

**Le retour arrière automatique.** L'agent surveille ses propres résultats et révoque une classe d'action dès qu'une régression apparaît. Pas l'humain. L'agent.

## L'espace d'action remplace la validation

Une action dangereuse ne doit pas être « soumise à approbation ». Elle doit **ne pas exister**.

Un agent qui ne sait pas exprimer « supprimer une page », « écrire dans `robots.txt` », « poser un `noindex` », ne peut pas les faire, et il n'a besoin de personne pour l'en empêcher. Il n'y a pas de bouton, il n'y a pas de verbe dans son vocabulaire.

Autonomie totale sur un espace restreint. Pas autonomie partielle sur un espace total. La première est un produit, la seconde est une posture.

## Règle dure : l'autonomie n'est pas décidée par le modèle

Un modèle ne dit jamais « je suis sûr, je peux appliquer ».

La confiance auto-déclarée d'un LLM n'est pas un signal de sécurité, elle est mal calibrée par construction. Le modèle dira « sûr » sur un H1 faux et « incertain » sur un canonical trivialement correct.

Le droit d'agir est une propriété **de la classe d'action**, pas de l'inférence. Il est inscrit dans une table, hors ligne, et il se met à jour à partir du journal des actions passées et de leurs résultats mesurés.

Le modèle formule. La table autorise.

## Le critère qui classe les actions

Trois axes, aucun ne s'appelle « difficulté ».

**Rayon d'explosion.** Combien de pages une erreur touche.

**Réversibilité.** Un revert de commit suffit, ou l'index met des mois à revenir.

**Latence de détection.** L'erreur se voit en lisant la page, ou seulement dans la GSC au trimestre suivant.

Un H1 médiocre : une page, réversible en un commit, visible immédiatement. Trois voyants au vert, l'agent y va seul, alors même que le H1 demande un jugement sémantique.

Un 301 vers la mauvaise cible : signal consolidé au mauvais endroit, index lent à revenir, découverte à J+90. Trois voyants au rouge.

La ligne ne passe pas entre déterministe et sémantique. Elle passe entre le coût de se tromper.

## La table des classes d'action

Le cœur du produit. Chaque ligne porte son niveau d'autonomie, et ce niveau se gagne, il ne se décrète pas.

| Zone | Classes d'action |
|---|---|
| **Autonome** : l'agent applique, budget plein | H1 manquant ou multiple, hiérarchie Hn désordonnée, meta description absente, ALT manquant, Open Graph, sitemap incohérent, chaîne de redirections aplatie, canonical pointant vers un 404, `nofollow` interne accidentel, directives contradictoires, lien interne mort, dimensions d'images |
| **Canari** : l'agent applique, budget serré, retour arrière automatique | ajout d'un self-canonical absent, liens internes ajoutés, ancres de maillage |
| **Hors espace V1** : l'agent ne sait pas les exprimer | cible d'un 301, modification d'un canonical existant, fusion de pages cannibales, pagination et facettes, contenu dupliqué, élagage, `robots.txt`, toute action qui retire une page de l'index |
| **Hors périmètre produit** | Core Web Vitals, rendu JavaScript, configuration serveur et CDN |

Deux nuances qui coûtent cher si on les rate.

**Ajouter un canonical n'est pas modifier un canonical.** Poser un self-canonical là où il n'y en a pas est bénin. Changer un canonical existant peut désindexer la page. Deux classes distinctes, deux zones différentes.

**Poser un 301 n'est pas choisir sa cible.** La pose est mécanique. Le choix de la cible est un jugement à rayon large et à retour lent, et le déploiement progressif ne le sauve pas : à cinq pages on ne mesure rien, à quatre-vingt-dix jours il est trop tard. Hors espace V1.

## La cadence est le produit

Okara applique une limite : deux corrections par jour. Ça se lit comme une contrainte, c'est une décision de produit, et elle est excellente.

Une cadence bornée crée une habitude, rend le travail digestible, et donne un récit. Elle est aussi, exactement, le budget de rayon d'explosion. La contrainte de sécurité **est** l'argument commercial.

Donc l'agent n'applique pas quarante-trois correctifs par nuit. Il en applique un petit nombre, il les vérifie, il les mesure.

« Trois corrections appliquées cette nuit, trois vérifiées, zéro régression depuis quatre mois » est une meilleure phrase qu'un compteur qui s'emballe, et un meilleur produit.

## Les modules

**0. Correspondance URL vers source.** Le module le plus dur, absent de toutes les specs naïves. Le crawl donne le HTML servi, la correction s'écrit dans le source. Il faut savoir que `/blog/balle-de-golf` est produite par tel objet, tel fichier, telle ligne. Parsing d'arbre syntaxique sur un dépôt, ou correspondance vers un `post_id` sur WordPress. Ce module décide quels sites leenq accepte, donc quel marché il adresse. C'est la barrière à l'entrée.

**1. Observation.** Crawl brut et crawl rendu, sitemap, robots, hreflang, canonicals, graphe de liens, profondeur, orphelines, GSC. Diff avec le crawl de la veille : c'est le signal. Commodity.

**2. Détection.** Moteur de règles déterministe. Pas de modèle, pas d'hallucination, coût nul.

**3. Décision.** Gabarit déterministe quand la cible est calculable. Modèle quand il faut formuler. La table des classes tranche le mode d'application.

**4. Application.** Dans la source. Pull request sur Git, révision sur WordPress. Jamais d'écriture directe en production sans passage par le module 5.

**5. Vérification avant fusion.** Build, crawl du déploiement de préversion, rejeu de toutes les règles, contrôle des invariants. Si un invariant saute, la PR se ferme d'elle-même. Quelques minutes.

**6. Mesure après fusion.** Chaque action est un pari daté, résolu à J+30 et J+90 en différence de différences contre des pages témoins. Cette mesure ne conditionne pas l'action. Elle conditionne l'élargissement du périmètre et déclenche le retour arrière automatique.

Le module 5 est la pièce qui manque à leenq aujourd'hui, et c'est celle qui autorise l'agent à se passer de l'humain.

## Le runtime

Repris de la forme Polsia : identité persistante, mémoire, outils, exécution planifiée, boucle qui tourne sans que personne l'ouvre.

**Le signal déclenche, pas l'utilisateur.** Personne ne se lève le matin pour lancer un scan. Le déploiement du client est le signal. Le produit existe sans qu'on l'ouvre.

**Zéro rapport à lire.** On ne livre pas un document, on livre des pull requests fusionnées et vérifiées. C'est le refus du livrable intermédiaire, et c'est ce qui sépare leenq de Semrush, d'Ahrefs et d'Okara.

**L'apprentissage cumulé est vendu, pas caché.** Le journal des actions résolues en GSC est visible dans le produit, pas dans une note d'architecture.

**« Ton agent », pas « notre plateforme ».** Vocabulaire personnifié, singulier, possessif. Un consultant qui tient six clients a six agents qui travaillent la nuit.

## Le moteur de règles : ne pas courir après le nombre

Cinq cents règles est un piège. C'est le terrain de Screaming Frog et de Sitebulb, et sur un site de cinquante mille pages ça produit deux cent mille constats sur lesquels personne n'agit. C'est pour ça que les audits meurent dans un tableur.

leenq ne sort pas des constats. Il sort **une file de diffs applicables**.

Le nombre qui compte est le nombre de correcteurs vérifiés. Une règle sans correcteur est du bruit qu'on paie à crawler.

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

C'est le risque de sanction le plus élevé du produit.

Un modèle à qui on demande un schema `Product` produira un prix, une note moyenne et une disponibilité. Ils seront plausibles et faux. Google traite un balisage qui ne correspond pas au contenu visible comme du spam structuré.

La règle est mécanique : **chaque champ de schema est extrait du DOM avec son sélecteur source**. Si le prix n'est pas dans la page, il n'entre pas dans le schema.

leenq ne produit pas des données structurées. Il produit la traduction en JSON-LD de ce qui est déjà affiché. C'est la doctrine « jamais de chiffre inventé », transposée dans du code.

Même logique pour le H1 : il se dérive du title, du slug, du premier paragraphe. Il n'affirme rien de nouveau.

## Ce qu'on ne construit pas

**Conversion WebP et AVIF, lazy loading, suppression de scripts.** Ce n'est pas du SEO, c'est de l'ingénierie front et de la chaîne de build. Le lazy loading appliqué sans discernement dégrade les Core Web Vitals dès qu'il touche l'image LCP. « Supprimer les scripts inutiles » est l'action qui détruira un client : inutile du point de vue d'un crawler, ça désigne la balise d'analytics, la bannière de consentement, le test A/B, le panier. Déjà résolu par `next/image`, par le CDN, par la plateforme.

**Le link building.** Le RankPilot de Polsia l'annonce en autonome. Un agent qui acquiert des liens seul, c'est de l'achat de liens automatisé. Interdit partout dans la doctrine.

**Envoi automatique du sitemap à Google.** L'endpoint de ping a été retiré, et l'Indexing API reste réservée aux offres d'emploi et aux événements diffusés. Le sitemap est lu au crawl. À revérifier avant toute promesse produit.

**Les sites sans dépôt ni API d'écriture.** Un agent est aussi autonome que sa surface d'écriture. Sur un site legacy en FTP, c'est zéro. On refuse, et on l'assume.

## Les trois modes

Personne ne donnera à un agent le droit d'écrire sur la production de son client au premier jour. Pas parce que ce n'est pas sûr, mais parce que le client du consultant ne l'autorisera pas.

**Mode ombre.** L'agent tourne chaque nuit, produit les diffs, passe les invariants sur la préversion, et n'applique rien. Le dashboard montre ce qu'il aurait fait et que tout est vert. Trente nuits comme ça, et deux choses arrivent : le client fait confiance, et le journal se remplit.

**Mode canari.** L'agent applique, borné. Quelques pages, une classe, un budget. Retour arrière automatique.

**Mode autonome.** Le budget s'ouvre classe par classe, à mesure que le journal le prouve.

Le mode ombre n'est pas un compromis sur la promesse. C'est ce qui la finance, parce que c'est lui qui produit la donnée qui permet de la tenir ensuite.

## Le dashboard de contrôle

Pas des cases à cocher. Pas de file d'attente d'approbation.

Le journal de ce qui a été fait cette nuit. Le compteur d'actions appliquées et de régressions mesurées, par classe. Les budgets, réglables. Un gel par site, pour les migrations et les périodes commerciales. Un retour arrière global. La liste des actions que l'agent n'a pas le droit d'exprimer, avec le motif.

Un poste de pilotage, pas une file d'attente.

## Le périmètre s'étend par la preuve

Chaque action appliquée est un pari daté, résolu en GSC contre des pages témoins. Le jour où mille actions d'une classe ont tourné sans qu'aucune régression soit mesurée, la classe passe du canari à l'autonome, et le budget s'ouvre.

Ce n'est pas un réglage, c'est un résultat.

C'est là qu'est le seul actif non copiable. Un moteur de règles se réécrit en trois mois. Trois ans de journal d'actions résolues en GSC sur cent sites, non. Même logique que les benchmarks GSC agrégés dans `qadence/Corpus-Qadence.md` : la valeur dépend du nombre de sites connectés.

Le produit affiche ce compteur. Zéro régression sur mille actions est l'argument de vente, et c'est la seule preuve qui vaille.

## Les pièges connus

**Le constructeur de pages WordPress.** Si le client utilise un page builder, le `post_content` qu'on édite n'est pas ce qui s'affiche. La correction est écrasée au premier enregistrement. Détecter le builder à la connexion et refuser le site, ou n'appliquer que ce qui passe par l'API des métadonnées.

**Idempotence et conflits.** Que se passe-t-il quand la PR de l'agent entre en conflit avec un commit humain. Quand le CMS régénère la page et efface le correctif. Quand l'agent recorrige ce qu'un humain a délibérément défait. Il faut une mémoire des corrections révoquées : ce qu'un humain annule ne se réapplique pas.

**Le gel.** Pendant une migration, un lancement, une période commerciale forte, l'agent ne touche à rien.

**Le rollback n'est pas gratuit.** Sur Git, c'est un revert. Sur WordPress, une révision restaurée, et si l'état des extensions a changé, non. Et surtout : un rollback après que Google a vu le changement ouvre un second cycle de réindexation. D'où le module 5.

## Ce que leenq a déjà

Le crawl et le graphe interne. Les connecteurs `git`, `github`, `wordpress`, `nextdata` dans `lib/connectors/`. Le write-back gated en pull request et en révision, validé en réel (PR #9 sur organikk-next, chaîne WordPress complète). L'auth GSC. La boucle d'impact `lenkrr-impact` avec les paris `link_bets` et les verdicts J+30 et J+90.

Modules 0 (partiellement), 1, 4 et 6 : existent.

Manquent le moteur de règles généralisé (module 2), la table des classes d'action (module 3), et la vérification de préversion (module 5).

Tant que le module 5 n'existe pas, leenq propose. Le jour où il existe, leenq agit.

## Le pain point, chiffré, sur un client réel

Leexi : SEO hors-marque à moins 43 % en six mois, cause racine une refonte sans 301 ni canonical, découverte des mois plus tard dans la GSC. Réparation faite à la main, 178 URLs testées une par une (`wiki/log.md`, 2026-06-09 et `prestation/clients/leexi.md`, 2026-07-02).

Le consultant SEO est jugé sur des résultats qu'il n'a pas les mains pour produire. Il recommande, un autre exécute, mal ou jamais, et il découvre les dégâts un trimestre plus tard.

C'est le produit.

## Le modèle commercial

**Acheteur : le consultant SEO.** Décision Tim, 2026-07-09. Pas le fondateur sans SEO, qui est la cible d'Okara et de Polsia. Le consultant achète du levier, pas son remplacement. Il garde le jugement, qui est ce qu'il facture.

**Tarif par site.** Il ajoute un client, il ajoute un site, il paie plus. Un consultant qui grossit paie plus sans qu'on lui vende quoi que ce soit. Le plan unique à 39 € par mois du squelette Stripe ne correspond plus à ce produit.

**Le mode aigu vend, le mode chronique facture.** Une refonte arrive, le consultant a peur, il branche le connecteur pour l'occasion. Le connecteur reste, l'agent tourne chaque nuit.

**Le dashboard multi-sites est la surface.** Le consultant ouvre un écran le matin, voit ses dix sites, voit ce qui a été corrigé cette nuit et ce qui a cassé chez le client. Ce n'est plus un outil, c'est son poste de travail.

## Décisions ouvertes

Absorption de leenq maillage dans le moteur général, ou coexistence le temps de la transition.

Stacks supportées à la V1. Next.js sur dépôt Git d'abord, WordPress ensuite, rien d'autre.

Tarification par site, et seuil de pages.

Nom du produit : leenq reste, ou l'agent technique prend un nom propre.

Où vit le module 5 : un déploiement de préversion Netlify ou Vercel côté client, ou un build en bac à sable côté leenq.

Suivi des citations IA (ChatGPT, Perplexity, Gemini) en option, comme Okara, ou hors périmètre.

## Ce qui n'est pas tranché

Le décompte des classes par zone vient de notre propre liste, pas d'un audit de marché. Ordre de grandeur, pas mesure.

Le retrait de l'endpoint de ping des sitemaps et la restriction de l'Indexing API sont à revérifier dans la documentation Google avant toute mention publique.

Le statut de `rankpilot-7.polsia.app` (app tierce construite sur Polsia, ou produit de Polsia) n'est pas confirmé. `polsia.com/live` n'a renvoyé que son titre.

Le positionnement des acteurs qui appliquent des correctifs à l'edge est à vérifier de première main avant d'écrire quoi que ce soit qui les compare.

Pages liées : [[concepts/maillage-systeme]] · [[moc/moc-maillage]]
