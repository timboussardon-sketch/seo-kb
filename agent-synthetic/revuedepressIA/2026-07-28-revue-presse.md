---
type: revue-presse
title: MCP 2026-07-28 passe stateless aujourd'hui, la barrière de mise en production d'un serveur baisse
date: 2026-07-28
pilier: Recherche agentique
edition: 2026-07-28
author: SyntheticBrain
status: draft
---

# MCP 2026-07-28 passe stateless aujourd'hui, la barrière de mise en production d'un serveur baisse

## Résumé

- Le texte normatif de la spec Model Context Protocol 2026-07-28 est publié ce jour, avec suppression du handshake `initialize`/`initialized` et de l'en-tête `Mcp-Session-Id` ; un serveur MCP peut désormais être routé derrière un load balancer round-robin sans stockage de session partagé.
- La période officielle de dépréciation démarre : les fonctionnalités marquées `deprecated` restent utilisables pendant au moins 12 mois avant tout retrait, ce qui laisse le temps aux implémentations de migrer sans coupure.
- Reddit publie ses résultats du deuxième trimestre 2026 jeudi 30 juillet ; les tensions autour du renouvellement du contrat de licence de données avec Google, chiffré à environ 60 millions USD par an, ont fait chuter l'action de 9 % le 22 juillet.
- L'agent d'achat Buy Now de Perplexity aurait franchi le seuil de 2 millions d'acheteurs actifs mensuels début juillet, avec une couche shopping annualisée à 2 milliards USD de GMV et une commission de 8 à 12 %, selon deux sources coordonnées et sans historique consolidé dans notre registre, à traiter comme direction, pas comme mesure de référence.

## Info du jour — Recherche agentique

La spécification 2026-07-28 du Model Context Protocol devient normative ce jour. Les mainteneurs du protocole l'avaient annoncée le 21 mai 2026 comme la révision la plus large depuis le lancement, avec une période de dix semaines de validation ouverte aux implémenteurs de SDK ([Model Context Protocol Blog, 2026-05-21](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)). Cette période se termine aujourd'hui.

Le changement de fond, contrairement à ce que suggère la formule « la plus large depuis le lancement », n'est pas un ajout de fonctionnalités mais un retrait. Le nouveau texte supprime le handshake `initialize`/`initialized` et l'en-tête `Mcp-Session-Id` ([Model Context Protocol Blog, 2026-05-21](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)). Les informations de client, la version de protocole et les capacités transitent maintenant via des champs `_meta` sur chaque requête, au lieu d'un handshake initial partagé sur la durée de la session ([WorkOS, 2026-05-30](https://workos.com/blog/mcp-2026-spec-agent-authentication)).

Ce qui change concrètement pour un serveur MCP en production : un serveur qui exigeait auparavant des sessions collantes, un stockage de session partagé et de l'inspection profonde de paquets au gateway peut désormais fonctionner derrière un load balancer round-robin ordinaire, en routant le trafic sur un en-tête `Mcp-Method`, avec les réponses `tools/list` mises en cache par le client aussi longtemps que le `ttlMs` du serveur l'autorise ([The Register, 2026-07-23](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)). L'infrastructure HTTP standard suffit.

Pour un consultant SEO/GEO qui suit l'agentique, l'implication opérationnelle est double. D'une part, un éditeur de contenu ou un vendor SEO qui voulait exposer un serveur MCP à un client Claude, ChatGPT, Copilot ou Cursor n'a plus besoin d'une couche middleware de gestion de session. Le coût de déploiement d'un connecteur baisse. D'autre part, le calendrier officiel de dépréciation démarre aujourd'hui : les fonctionnalités marquées `deprecated` restent fonctionnelles pendant au moins 12 mois avant tout retrait ([Model Context Protocol Blog, 2026-05-21](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)). Les serveurs existants ne cassent pas ce jour, comme le confirment les mainteneurs.

Côté SDK, les versions bêta compatibles avec la spec 2026-07-28 étaient disponibles depuis fin juin : Python `v2.0.0b1`, TypeScript `v2` bêta, Go `v1.7.0-pre.1`, C# `v2.0.0-preview.1` ([Model Context Protocol Blog, 2026-06-29](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)). L'adoption de ces SDK par les gestionnaires de paquets standard (Python, Go) reste opt-in : les versions stables restent servies par défaut, sauf demande explicite de pré-release. Le changement de version principale du SDK TypeScript passe par un nouveau nom de paquet, ce qui rend l'adoption intentionnelle.

Ce que ce jour ne change pas : aucun chiffre indépendant d'adoption post-28 juillet n'est disponible. Le parc de serveurs MCP en production, dernièrement estimé à environ 10 000 par les mainteneurs et les fournisseurs partenaires ([Model Context Protocol Blog, 2026-05-21](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)), pourrait être vérifié par audit tiers dans les prochaines semaines. Aucun tel audit indépendant n'est publié à ce jour.

**Lien doctrine** — [[concepts/agentic-search]] : le protocole d'accès aux données et outils par les agents devient un objet à cartographier au même titre que les moteurs de recherche eux-mêmes. Un serveur MCP qui expose une base de connaissances propriétaire à des agents constitue un point d'accès agent distinct de la page web indexée par les crawlers classiques. Ce type de point d'accès n'est pas encore mesuré par les outils GEO courants.

## Brèves

### B1 — Business SEO. Résultats Reddit du 2ᵉ trimestre attendus jeudi, la question du renouvellement du contrat Google reste ouverte

Reddit publie ses résultats du deuxième trimestre 2026 le jeudi 30 juillet. Le consensus des analystes attend un bénéfice par action de 0,97 USD et un chiffre d'affaires de 732,82 millions USD, avec une croissance annuelle d'environ 47 % ([The Motley Fool, 2026-07-27](https://www.fool.com/investing/2026/07/27/reddit-incs-next-earnings-report-on-july-30-could-send-the-stock-soaring-heres-why/)).

L'attention des investisseurs porte moins sur ces chiffres que sur le contexte publié 8 jours plus tôt. Le 22 juillet, le Wall Street Journal a rapporté que Reddit remet en question le renouvellement de son contrat de licence de données d'intelligence artificielle avec Google, signé en février 2024 et valorisé environ 60 millions USD par an ([CNBC, 2026-07-22](https://www.cnbc.com/2026/07/22/reddit-stock-google-ai-content-deal.html)). L'action a chuté d'environ 9 % dans la séance qui a suivi la publication ([TradingKey, 2026-07-22](https://www.tradingkey.com/analysis/stocks/us-stocks/262049360-why-is-reddit-rddt-stock-down-today-google-ai-deal-tradingkey)). Reddit conserve par ailleurs un contrat séparé avec OpenAI, estimé à environ 70 millions USD par an.

L'argument documenté côté Reddit : les réponses génératives de Google réduisent le trafic renvoyé vers Reddit, ce qui rend le tarif forfaitaire d'origine moins favorable. La direction cherche un modèle qui rapproche la rémunération de la valeur effectivement extraite par le moteur, soit du pricing par usage, soit du pricing dynamique ([TradingKey, 2026-07-22](https://www.tradingkey.com/analysis/stocks/us-stocks/262049360-why-is-reddit-rddt-stock-down-today-google-ai-deal-tradingkey)).

Ce qui manque pour trancher : la publication effective des résultats jeudi, avec le chiffre de licence de données isolé (39 millions USD au T1), et toute prise de parole du management sur la position de renouvellement. Les deux éléments ne seront lisibles qu'à partir du 30 juillet, après clôture.

### B2 — Business SEO. Perplexity revendique 2 millions d'acheteurs actifs mensuels et 2 milliards USD de GMV annualisé sur son agent d'achat

Perplexity revendique que son agent Buy Now aurait franchi le seuil de 2 millions d'acheteurs actifs mensuels, la couche shopping tournant à un run rate annualisé de 2 milliards USD de GMV, selon deux sources coordonnées ([Novadata, 2026-07-03](https://novadata.io/resources/news/perplexity-buy-now-agent-2m-shoppers-july-2026)) citant Ecommerce Times daté du 2 juillet 2026. Le modèle documenté : une commission de 8 à 12 % du GMV sur les transactions Buy Now, variable par catégorie, en plus du traitement Stripe ([Novadata, 2026-07-03](https://novadata.io/resources/news/perplexity-buy-now-agent-2m-shoppers-july-2026)).

Le contexte : en avril 2026, Amazon a restreint l'accès de Perplexity aux prix et à l'inventaire en temps réel. Le GMV attribué à Amazon aurait chuté d'environ 30 % dans les 60 jours suivants, ce qui a accéléré la construction d'un catalogue direct auprès des marchands. Les marques direct-to-consumer sur Shopify auraient été priorisées dans le moteur de recommandation ([Novadata, 2026-07-03](https://novadata.io/resources/news/perplexity-buy-now-agent-2m-shoppers-july-2026)).

Réserves méthodologiques explicites. Le chiffrage repose sur deux sources reprises l'une l'autre (Ecommerce Times comme source première, Novadata comme reprise). Aucune ne figure dans notre registre de sources avec un historique consolidé. Perplexity n'a pas publié de chiffre officiel documentant ces seuils, aucun rapport d'analyste tiers n'est disponible, et aucune donnée d'audit indépendant ne confirme le run rate. À traiter comme direction attribuée à Perplexity, pas comme mesure de référence.

Ce qui rendrait le chiffre exploitable : une communication officielle Perplexity, un rapport d'analyste tiers isolant les commissions perçues, ou une confirmation d'un merchant Shopify sur le volume attribué à Perplexity dans son propre reporting.

**Lien doctrine** — [[concepts/tabou-visibilite]] : si les chiffres se confirment, le point utile pour un consultant n'est pas la « visibilité » sur Perplexity mais le taux de commission effectif (8-12 %) sur des transactions finalisées, comparable à ce que prend une plateforme marketplace, distinct d'un modèle publicitaire ou d'affiliation classique.

### B3 — Business SEO. Meta revendique 1 million d'entreprises actives sur Business Agent WhatsApp et Messenger

Meta communique qu'au moins 1 million d'entreprises utilisent son Business Agent sur WhatsApp et Messenger, chiffre repris dans le tour d'horizon publicitaire de juillet 2026 ([Boot Camp Digital, 2026-07-22](https://bootcampdigital.com/blog/july-2026-digital-news-updates/)). Le communiqué mentionne également plus de 8 millions d'annonceurs utilisant les outils créatifs génératifs, sans détailler la fréquence d'usage ni la répartition par région.

Trois nouvelles métriques sont mises à disposition pour mesurer la performance des chatbots de marque : `AI conversations` (nombre de conversations gérées par l'agent), `Contact with intent to buy` (contacts sortants avec intention d'achat détectée) et `Containment rate` (part des conversations résolues sans transfert humain) ([Boot Camp Digital, 2026-07-22](https://bootcampdigital.com/blog/july-2026-digital-news-updates/)).

Réserves. Les chiffres sont revendiqués par Meta, sans audit tiers ni ventilation par vertical, taille d'entreprise ou géographie. La métrique `Containment rate` en particulier reste sensible à la définition de « conversation résolue », qui n'est pas documentée publiquement au niveau de la spécification. À traiter comme direction d'usage, avec pondération vendeur explicite.

Le point utile : ces trois métriques sont proches, dans leur conception, de ce que des vendors GEO commencent à instrumenter côté agents IA (Nudge, Kasper, Loftie). Meta les rend natives dans son propre ads manager, ce qui pourrait modifier la référence de mesure côté annonceurs travaillant en direct sur ces canaux.

---

Draft SyntheticBrain. Rien n'a été envoyé.
