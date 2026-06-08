# Google teste Web Bot Auth : autoriser un agent IA par signature plutôt que par adresse IP

_Édition du 2026-06-06. Pilier de l'info du jour : recherche agentique. Draft SyntheticBrain, non envoyé._

## En résumé

- Google teste **Web Bot Auth**, un mécanisme qui fait signer aux robots leurs requêtes avec une clé numérique. Le but : vérifier l'identité d'un crawler ou d'un agent IA de façon fiable, là où le nom du robot et son adresse IP se falsifient facilement.
- Précision qui change le sens de l'annonce : Google ne crée pas ce mécanisme seul. C'est un projet de norme ouvert, écrit d'abord par Cloudflare, avec un co-auteur Google. Google le teste, statut expérimental.
- **Ask.com** a fermé son activité de recherche le 1er mai 2026. IAC sort du search après presque trente ans.
- Google a déployé des **Search profiles** pour les éditeurs et créateurs (4 juin 2026), un profil suivable qui augmente la probabilité de réapparaître dans Discover.
- Les installations de **DuckDuckGo** ont bondi après l'annonce d'une recherche Google plus centrée sur l'IA. En parallèle, un responsable produit Microsoft a écrit sur une diapositive que l'IA qui résume les résultats réduit les clics et les visites.

## L'info du jour : la vérification des agents IA passe de l'adresse IP à la signature

*Doctrine : [[concepts/agentic-search]].*

Aujourd'hui, quand un site veut autoriser ou bloquer un robot, il se fie à deux signaux : le nom que le robot déclare (son User-Agent) et son adresse IP. Les deux se falsifient. N'importe quel script peut se présenter comme « Googlebot » ou « GPTBot ». La vérification sérieuse demande des recoupements manuels (plages d'IP officielles, requêtes DNS inverses), que peu de sites tiennent à jour.

**Web Bot Auth** change la méthode. Le robot signe chacune de ses requêtes avec une clé privée. Il publie la clé publique correspondante à une adresse connue de son domaine. Le serveur qui reçoit la requête vérifie la signature avec cette clé publique. Si elle correspond, l'identité du robot est prouvée par un calcul, pas par une déclaration. Le mécanisme s'appuie sur la norme de signature des requêtes HTTP ([RFC 9421](https://www.rfc-editor.org/rfc/rfc9421.html)).

Google documente son test sur sa page développeurs, mise à jour le 4 mai 2026, avec un statut clairement expérimental : « Google ne signe pas encore toutes ses requêtes », tous les agents Google n'utilisent pas Web Bot Auth ([Google for Developers](https://developers.google.com/crawling/docs/crawlers-fetchers/web-bot-auth)). Couverture indépendante côté presse spécialisée le 5 mai 2026 ([Search Engine Journal](https://www.searchenginejournal.com/google-is-testing-new-bot-authorization-standard/573957/)).

Le point à ne pas déformer : Google ne « lance » pas un protocole maison. Web Bot Auth est un projet de norme déposé à l'IETF, l'organisme qui standardise les protocoles d'internet. L'auteur principal est Thibault Meunier, chez Cloudflare ; un ingénieur Google, Sandor Major, est co-auteur ([draft IETF, version du 2 mars 2026](https://datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/)). Cloudflare a publié sa proposition le 15 mai 2025, environ un an avant le test public de Google, et vérifie déjà ces signatures à son niveau dans son programme de robots vérifiés ([Cloudflare, 15 mai 2025](https://blog.cloudflare.com/web-bot-auth/)). La nouveauté de 2026, c'est l'entrée de Google, pas le mécanisme lui-même.

Pourquoi cela compte pour le référencement et la recherche agentique. La gestion des crawlers IA repose aujourd'hui sur des fichiers `robots.txt` qui nomment des robots, et sur des blocages par adresse IP. Ces deux leviers supposent qu'on sait à qui on a affaire, ce qui n'est pas vraiment le cas. Une identité signée rend la décision d'autorisation fiable : un site peut accorder l'accès à un agent identifié de façon certaine, ou le refuser, sans dépendre d'une liste d'adresses tenue à la main. Pour la conformité d'un crawler maison, le principe rejoint une règle déjà appliquée côté production : un robot doit être identifiable et respecter les règles d'accès du site ([[concepts/pseo-data-driven-models]]). La distinction entre un robot qui exécute une commande et un agent qui enchaîne des actions devient ici concrète : c'est l'agent autonome qu'on cherche à authentifier avant de le laisser lire ou agir ([[concepts/agentic-search]]).

Ce qui reste incertain. Le mécanisme est expérimental côté Google, qui ne signe pas toutes ses requêtes. Le texte est un projet de norme, pas une norme figée. Son adoption au-delà de Cloudflare et Google reste à confirmer. Le signal est solide sur la direction technique, pas sur un déploiement généralisé à court terme.

## Brèves

### Actualité search : Ask.com a fermé son moteur de recherche

IAC a arrêté l'activité de recherche d'Ask.com le 1er mai 2026, annoncé le 2 mai. Le message publié sur le site cite la décision « d'arrêter notre activité de recherche, qui inclut Ask.com ». Lancé sous le nom Ask Jeeves en 1996 comme pionnier de la recherche en langage naturel, racheté par IAC en 2005, le service avait abandonné sa propre technologie de recherche vers 2010. Il s'arrête après presque trente ans, dans un contexte où les réponses générées par IA réduisent les clics vers les sites. Sources : [TechCrunch, 2 mai 2026](https://techcrunch.com/2026/05/02/farewell-jeeves-ask-com-shuts-down/) et [Search Engine Land](https://searchengineland.com/ask-com-shuts-down-after-over-25-years-476304). (À noter : une vidéo de veille datait cette fermeture au 5 mai, c'est inexact.)

### Éditeurs : Google déploie des Search profiles

Google a annoncé le 4 juin 2026 un profil dédié pour les éditeurs et les créateurs. Ce profil regroupe les derniers articles, vidéos et publications d'une source, et permet aux internautes de la suivre, ce qui augmente la probabilité de revoir son contenu dans Discover. On y accède depuis le contenu de la source dans Discover, depuis un bouton sur le panneau de connaissances mobile, ou par une adresse directe. L'accès demande une audience conséquente sur au moins une plateforme (seuils rapportés : 100 000 abonnés sur YouTube, Instagram ou X, 300 000 sur TikTok). Lancement aux États-Unis d'abord. Google le présente comme un outil de visibilité ; plusieurs reprises le relient au recul du trafic envoyé aux éditeurs depuis l'arrivée des réponses IA. Sources : [blog.google, 4 juin 2026](https://blog.google/products-and-platforms/products/search/a-new-profile-to-help-publishers-and-creators-highlight-their-work-on-search/), [Variety](https://variety.com/2026/digital/news/google-search-profiles-creators-publishers-ai-results-1236766526/), [Search Engine Land](https://searchengineland.com/google-introduces-search-profiles-within-google-discover-479475).

### Signal utilisateurs : DuckDuckGo grimpe, Microsoft reconnaît la baisse de clics

Après l'annonce, à Google I/O 2026, d'une recherche plus centrée sur l'IA et sans désactivation simple, les installations de DuckDuckGo ont augmenté. DuckDuckGo communique un pic à environ +30 % sur une journée (25 mai) et une moyenne de +18 % sur la semaine du 20 au 25 mai ; les visites de sa page sans IA montent de +22,7 % en moyenne sur la même semaine. Une mesure tierce, Apptopia, confirme l'ordre de grandeur sur les installations : +29 % aux États-Unis, mais seulement +12 % au niveau mondial, ce qui situe l'effet surtout aux États-Unis ([TechCrunch, 26 mai 2026](https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/)). En parallèle, un responsable produit marketing de Microsoft, James Murray, a écrit sur une diapositive que « l'IA résume les résultats, ce qui réduit les clics et les visites », repéré dans un webinaire ([Search Engine Roundtable](https://www.seroundtable.com/microsoft-ai-reducing-clicks-website-visits-41429.html)). Deux signaux qui pointent la même chose : la recherche centrée IA déplace une partie de la demande et réduit le trafic sortant. À garder en proportion : DuckDuckGo reste autour de 2 % du marché américain, et le pic est lié au moment de l'annonce I/O.

---

_Prédictions ouvertes ajoutées cette édition : voir `ledgers/predictions.jsonl` (P-2026-06-06-1, P-2026-06-06-2). Source de découverte du jour : veille vidéo YouTube élargie, chaque piste recoupée en source primaire avant publication. Piste écartée : le montage « Princeton a testé 5 tactiques, Google en a tué 4 le 15 mai » (étude réelle mais de novembre 2023, faux lien causal avec la guidance Google du 15 mai 2026)._
