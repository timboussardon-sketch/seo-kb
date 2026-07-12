---
type: revue-presse
title: "Algorithme du 6 juillet 2026 : Cloudflare expose le ratio crawl / renvoi par opérateur"
date: 2026-07-06
edition: 2026-07-06-revue-presse
author: SyntheticBrain
status: draft
pilier_info_jour: GEO
tags: [algorithme, revue-presse, geo, agentic-search, cloudflare, mesure]
---

# Algorithme, édition du 6 juillet 2026

## L'essentiel en 3 points

- Cloudflare met à disposition, le 1er juillet 2026, deux tableaux de bord (BotBase et Attribution Business Insights) qui exposent pour la première fois aux éditeurs, opérateur par opérateur, le rapport entre le nombre de requêtes des robots IA et le trafic effectivement renvoyé, avec une taxonomie des robots en sept catégories.
- Les ratios crawl / renvoi publiés dans le rapport d'anniversaire du même jour s'étalent de 14 pour 1 (Google) à 73 000 pour 1 (Anthropic), un ordre de grandeur qui reste vendeur mais que la disponibilité du tableau de bord rend désormais mesurable au niveau du site.
- La mise à jour de spam Google de juin 2026 est close depuis 10 jours ; aucun tracker large échantillon n'a encore publié de ventilation verticale des gagnants et perdants au 6 juillet 06h UTC.

## Info du jour : Cloudflare rend visible aux éditeurs le rapport crawl / renvoi par opérateur

Cloudflare a publié le 1er juillet 2026, deuxième anniversaire de son [Content Independence Day](https://blog.cloudflare.com/agentic-internet-bot-report/), deux nouveaux tableaux de bord destinés à ses clients Bot Management : [BotBase](https://developers.cloudflare.com/changelog/post/2026-07-01-botbase-attribution-business-insights/) et [Attribution Business Insights](https://blog.cloudflare.com/attribution-business-insights/), écrits par Jin-Hee Lee et Oliver Payne. BotBase est un annuaire consultable des robots que Cloudflare identifie, classés en sept catégories : Search, Agent, Training, Transact, Data Collection, SEO, Ads Verification. Attribution Business Insights compare, opérateur par opérateur, l'activité de crawl et le volume de trafic renvoyé au site, sur des fenêtres de 24 heures, 7 jours ou 30 jours.

L'information neuve est la mise à disposition du ratio par opérateur au niveau du site individuel. Jusqu'ici, les ratios crawl / renvoi étaient publiés au niveau agrégé par les rapports Cloudflare Radar et évoqués dans la presse comme des chiffres externes. Le rapport d'anniversaire du 1er juillet 2026 réaffirme trois ratios repères, mesurés en 2025 sur le réseau Cloudflare : [Google à 14 pour 1, OpenAI à 1 700 pour 1, Anthropic à 73 000 pour 1](https://blog.cloudflare.com/agentic-internet-bot-report/). Ces chiffres sont ceux du fournisseur d'infrastructure lui-même et n'ont pas été reproduits par une mesure tierce publiée. Ce qui change avec Attribution Business Insights, c'est qu'un éditeur enterprise peut désormais voir son propre ratio pour chaque opérateur qui le crawle, avec un statut Allowed, Blocked ou Partially blocked, plutôt que de raisonner sur une moyenne globale du réseau.

Le même rapport publie deux autres mesures : plus de 50 pour cent du trafic sur le réseau Cloudflare est désormais non humain, et le crawl à visée d'entraînement représente 52 pour cent des requêtes de robots en juin 2026, contre 22 pour cent au printemps 2025. Cloudflare mentionne également un déclin de 40 pour cent du trafic humain dans les catégories de sites les plus crawlées sur les douze derniers mois. Ces trois chiffres, produits par une seule source vendeur, portent une direction attribuée à Cloudflare et pas une valeur de référence indépendante.

Pour la doctrine, l'annonce touche trois concepts existants et en teste un quatrième.

Sur [[concepts/metriques-visibilite-geo]], Attribution Business Insights ajoute une métrique inédite : le ratio crawl / renvoi par opérateur, disponible au site plutôt qu'au réseau. La fiche doctrinale distingue déjà l'apparition, la densité et la position de citation. Elle n'inclut pas la mesure des flux entrants par crawler ni le rapport entre ces flux et le trafic sortant vers l'éditeur. La ligne à ajouter est la suivante : la mesure crawl / renvoi par opérateur devient le premier indicateur direct de l'asymétrie économique entre l'accès au contenu et le renvoi de trafic, disponible dans un tableau de bord d'éditeur.

Sur [[concepts/tabou-visibilite]], la publication réaffirme l'obligation d'attribuer les chiffres à leur pipeline de mesure et à leur période. Le ratio 73 000 pour 1 mesuré sur le réseau Cloudflare 2025 pour Anthropic n'est pas transposable tel quel à un site donné. La fiche impose que le mot ratio, comme le mot visibilité, ne soit jamais employé sans son numérateur, son dénominateur et sa fenêtre temporelle. Un consultant qui présente un chiffre du dashboard Attribution Business Insights à un client doit indiquer, à la ligne près, quel opérateur, quelle catégorie, quelle fenêtre et quel statut Allowed ou Blocked.

Sur [[concepts/data-proprietaire]], la mesure des ratios crawl / renvoi produit un nouvel actif de première main pour l'éditeur qui l'active. Ces données ne sont pas publiques ni reproductibles par un tiers sans accès au réseau du site. La fiche définit le moat propriétaire comme un pipeline de collecte que le concurrent ne peut pas répliquer. Le tableau de bord Attribution Business Insights entre dans cette définition : il produit, par site, une série temporelle non substituable qui devient un argument de vente pour la fonction commerciale d'un éditeur qui négocie avec un opérateur de moteur IA.

Sur [[concepts/agentic-search]], la taxonomie BotBase à sept catégories propose un vocabulaire de classification que la fiche n'exigeait pas jusqu'ici. La séparation entre Search (crawl pour rafraîchir une base de connaissance ancrée RAG), Agent (crawl à la demande pour un utilisateur final), et Training (crawl pour l'entraînement de modèle) est une distinction technique que la fiche va devoir intégrer si les autres fournisseurs d'infrastructure (Akamai Bot Manager, Cloudflare concurrents) reprennent la même segmentation.

Portée et limites. Le tableau de bord Attribution Business Insights est réservé aux clients enterprise Cloudflare Bot Management, ce qui limite l'accès aux éditeurs qui disposent de ce niveau de contrat. Aucun montant de rémunération versé à un éditeur n'est publié dans le rapport. Aucun engagement de mainstream operator IA (Google, OpenAI, Anthropic, Perplexity, Microsoft, Meta) sur la reprise des sept catégories BotBase n'est documenté. La mesure du ratio crawl / renvoi par opérateur n'est pas reproduite à ce jour par un tableau de bord équivalent chez un fournisseur d'infrastructure indépendant.

Trois recommandations pour un consultant GEO ou SEO technique qui intervient chez un éditeur Cloudflare enterprise. Un, sur un audit trimestriel, extraire du dashboard Attribution Business Insights la série des ratios crawl / renvoi par opérateur sur les fenêtres 7 jours et 30 jours, en indiquant à chaque ligne le statut Allowed ou Blocked. Deux, ne pas présenter une moyenne agrégée du ratio sans la ventilation par opérateur ; un ratio réseau élevé masque des opérateurs à ratio faible qui rapportent effectivement du trafic. Trois, joindre au reporting la note explicite que le ratio est une mesure fournisseur d'infrastructure, pas une mesure indépendante ; si l'éditeur veut une contre-mesure, il faut installer une deuxième solution d'observabilité côté serveur qui recompte les user-agents identifiés.

Prédiction P-2026-07-06-1 : d'ici le 31 décembre 2026, au moins un fournisseur d'infrastructure indépendant de Cloudflare (Akamai, Fastly, Amazon CloudFront, Google Cloud Armor) publie un tableau de bord éditeur exposant le ratio crawl / renvoi par opérateur sur une taxonomie de robots à plus de 3 catégories. Si aucun ne le fait, le vocabulaire de segmentation BotBase à sept catégories reste une classification propriétaire Cloudflare et pas un standard sectoriel.

Prédiction P-2026-07-06-2 : d'ici le 31 décembre 2026, au moins une étude tierce publie une comparaison des ratios crawl / renvoi mesurés par Cloudflare Attribution Business Insights avec une source externe indépendante (Bot Management concurrent ou observabilité côté serveur), sur un échantillon documenté d'au moins dix sites. Si aucune reproduction n'est publiée, les chiffres 14 / 1 700 / 73 000 pour 1 restent des références vendeur.

## Brèves

### B1. Recherche agentique : Meta publie un serveur MCP pour son platform développeur

Meta a annoncé le 30 juin 2026, via [le blog Meta for Developers](https://developers.meta.com/blog/) et repris par [PPC Land le 5 juillet](https://ppc.land/meta-launches-developer-tools-mcp-cutting-dashboard-logins-to-zero/), un serveur MCP en bêta à l'adresse mcp.facebook.com/devtools. Auteure de l'annonce : Zoë Lieberman. La bêta expose dix outils dans un espace de noms devtools_ pour permettre aux assistants de code IA (Claude Code, Claude Desktop, OpenAI Codex, ChatGPT, Cursor) d'accéder aux données de compte développeur sans passage par le tableau de bord. Deux outils ne demandent aucune permission scope app, huit demandent un scope Read ou Manage, une seule capacité en écriture est proposée : la gestion des abonnements webhook.

Cette annonce prolonge le premier MCP de Meta déjà publié le 29 avril 2026 pour la [Marketing API](https://www.facebook.com/business/news/meta-ads-ai-connectors), qui exposait 29 outils. Le serveur du 30 juin étend le principe au périmètre Developer Platform, séparé de l'ads platform. La distinction touche la recherche agentique : les serveurs MCP publiés par les grandes plateformes exposent une interface de contrôle standardisée que les agents IA peuvent appeler directement. La taxonomie des serveurs MCP publiés en 2026 sur les plateformes majeures s'étoffe (Meta Ads avril, Meta Developer Tools juin, TikTok Ads via Digiday reporté juin, Google Ads via Ads Data Hub non publié à ce jour).

Portée réelle. Le périmètre reste strictement développeur et non search. L'écosystème MCP côté publicité est plus mature que côté search classique : aucun grand moteur de recherche organique ne propose à ce jour un serveur MCP pour ses outils webmaster.

### B2. Actualité SEO : mise à jour de spam Google de juin 2026, aucun bilan grand échantillon à J+10

Le déploiement de la mise à jour de spam Google de juin 2026 est [clos depuis le 26 juin 2026 à 14h00 heure du Pacifique](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ) selon Google Status Dashboard. La fenêtre de lecture fiable des données, définie par Google comme sept jours après clôture, est ouverte depuis le 3 juillet. Au 6 juillet 06h UTC, aucun bilan gagnants / perdants par vertical n'a été publié à échantillon supérieur à 10 000 domaines par un tracker de mesure de visibilité indépendant. [Tech2Geek publie une analyse](https://www.tech2geek.net/google-june-2026-spam-update-winners-losers-and-what-it-means-for-seo-ai-search-and-your-website/) descriptive sans donnée quantifiée. [Digital Applied publie une lecture qualitative sur la volatilité observée](https://www.digitalapplied.com/blog/google-june-2026-ranking-update-volatility-seo-analysis) sans échantillon détaillé. [Search Engine Journal confirme la clôture](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/) sans analyse post-clôture. Lily Ray n'a pas publié d'analyse Amsive sur cette mise à jour au 6 juillet, 22e édition consécutive où la directive n'est pas tenue.

L'absence de bilan tracker large échantillon 10 jours après clôture est une donnée en soi : elle contredit la lecture pressée d'un impact large et différentiable. La prédiction P-2026-07-03-4 (bilan de deux trackers indépendants avant le 17 juillet) reste ouverte à 11 jours. La prédiction P-2026-07-02-v2-5 (bilan avant le 10 juillet) reste ouverte à 4 jours.

### B3. Business SEO : OpenAI recrute pour des formats publicitaires natifs et conversationnels

OpenAI a ouvert début juillet 2026 des offres d'emploi Engineering sur son équipe Monetization, reprises par [Search Engine Journal](https://www.searchenginejournal.com/openai-hiring-points-to-image-video-ads-coming-to-chatgpt/581289/) et [Digiday](https://digiday.com/marketing/openai-looks-beyond-a-single-ad-format-with-image-video-and-conversational-ads-in-the-works/), et mentionnées dans [le rapport PPC Land du 4 juillet](https://ppc.land/ai-overviews-cut-publisher-clicks-39-8-in-first-randomized-study/) sur l'étude Agarwal-Sen. Trois annonces publiées sur la page carrières d'OpenAI décrivent la construction d'une infrastructure pour des formats publicitaires : texte, image, vidéo, natif, conversationnel, interactif. Le poste Ad Formats engineer senior demande sept ans d'expérience minimum et affiche une rémunération de 230 000 à 385 000 dollars annuels plus equity. Deux postes iOS et Android, quatre ans d'expérience minimum, portent sur la validation de format et le pattern UX policy-aware.

Cette information est un signal d'intention de moyen terme, pas un déploiement. Elle indique que la structure interne d'OpenAI ouvre un axe d'ingénierie produit dédié aux formats publicitaires, alors qu'aucun format n'est encore documenté publiquement au 6 juillet. La séparation formats organiques / formats payants dans les réponses de ChatGPT reste, à date, non annoncée publiquement. La prédiction ouverte P-2026-05-30-5 (format publicitaire dans la réponse générative sortant du stade annonce) reste ouverte côté ChatGPT ; côté Google, elle a été partiellement résolue le 6 juin 2026 par l'ouverture santé AI Mode.

---

*Draft SyntheticBrain, 2026-07-06. Rien n'a été envoyé.*
