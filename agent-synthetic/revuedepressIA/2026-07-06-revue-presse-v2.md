---
type: revue-presse
title: "Algorithme du 6 juillet 2026 (v2) : Salesforce fixe la GA de son connecteur ChatGPT à juillet, l'objet à optimiser sort du site"
date: 2026-07-06
edition: 2026-07-06-revue-presse-v2
author: SyntheticBrain
status: draft
pilier_info_jour: Recherche agentique
tags: [algorithme, revue-presse, recherche-agentique, salesforce, agentforce, chatgpt, business-seo]
---

# Algorithme, édition du 6 juillet 2026 (v2)

## L'essentiel en 4 points

- Salesforce a fait passer Agentforce Commerce en disponibilité générale le 29 juin 2026 sur les trois agents Shopper, Buyer et Merchant, et annonce l'intégration native à ChatGPT en GA pour juillet, à Google AI Mode et Gemini plus tard dans l'été.
- Pour un vendeur qui passe par ce canal, l'unité de découverte n'est plus la page produit publique, c'est le flux catalogue synchronisé depuis Salesforce Business Manager ; la mesure de visibilité doit se séparer entre canal search organique et canal agent commerce.
- Fabrice Canel, responsable de l'indexation et créateur d'IndexNow chez Bing, a annoncé sa retraite de Microsoft effective le 1er juillet 2026 après près de trente ans ; Microsoft n'a pas publié de successeur.
- Microsoft Threat Intelligence a publié le 29 juin 2026 l'analyse d'une extension Chrome usurpant Perplexity, qui interceptait chaque caractère saisi dans la barre d'adresse via `declarativeNetRequest` avant de rediriger vers un moteur légitime ; Google a retiré l'extension après signalement.

## Info du jour : Salesforce Agentforce Commerce passe GA et fixe la GA de son intégration ChatGPT à juillet 2026

Salesforce a publié [le 24 juin 2026 le communiqué qui annonce la disponibilité générale d'Agentforce Commerce](https://www.salesforce.com/news/stories/agentforce-commerce-announcement/), consolidé le 29 juin lors de la mise en ligne effective des trois agents commerciaux Shopper, Buyer et Merchant. La couverture indépendante de [Digital Commerce 360, 24 juin](https://www.digitalcommerce360.com/2026/06/24/salesforce-releases-ai-agents-b2b-ecommerce-updates/), [Martech Notes, 29 juin](https://www.martechnotes.com/salesforces-agentforce-commerce-ga-lands-ahead-of-peak-season-with-shopper-buyer-and-merchant-agents/) et [CX Today, 29 juin](https://www.cxtoday.com/crm/salesforce-agentforce-commerce-generally-available/) confirme la date de GA et la portée du produit. L'annonce nomme Nitin Mangtani, EVP et GM d'Agentforce Commerce, Shirley Gao, Chief Digital & Information Officer de PacSun, et Luke Barber, Head of Ecommerce Technology chez Iceland Foods. Les intégrations natives sont programmées à des dates distinctes : ChatGPT en GA en juillet 2026, Google AI Mode et Gemini plus tard dans l'été.

Le fait neuf n'est pas l'existence des agents. Salesforce avait déjà annoncé Agentforce Sales dans ChatGPT en décembre 2025 et un pilote Agentforce Commerce le 13 avril 2026. Le fait neuf est l'atteinte simultanée du stade GA sur les trois périmètres (Shopper pour le B2C conversationnel, Buyer pour la commande B2B via WhatsApp et SMS, Merchant pour l'orchestration back-office), et le calendrier fixé de mise à disposition sur des surfaces d'IA générative externes. Le connecteur ChatGPT synchronise le catalogue produit directement depuis Salesforce Business Manager, sans logiciel supplémentaire.

Pour la doctrine, l'annonce touche trois concepts existants.

Sur [[concepts/agentic-search]], la fiche pose que "être sélectionné par l'agent pour accomplir une tâche" remplace "être affiché dans une liste de liens". Le déploiement Agentforce en donne une instrumentation opérable côté vendeur : l'agent Shopper est un composant Salesforce qui a accès à l'inventaire et au checkout du client Salesforce, pas un module autonome qui parcourt le web. Un vendeur qui passe par ce canal ne cherche plus à faire ranker sa page produit dans une réponse générative ; il cherche à ce que son catalogue Business Manager soit correctement synchronisé, que ses attributs conversationnels soient renseignés, et que ses règles d'inventaire soient à jour.

Sur [[concepts/data-proprietaire]], la fiche identifie la data propriétaire comme le moat SEO/GEO. Le connecteur Agentforce Commerce déplace l'unité qui compte du "contenu publié sur une page produit" vers "le flux catalogue synchronisé avec des attributs marchand structurés". La condition d'entrée pour un vendeur Salesforce n'est plus la qualité rédactionnelle de la page produit, c'est la complétude et la fraîcheur du flux catalogue en amont. Ligne à ajouter à la fiche : le pipeline catalogue temps réel entre PIM/OMS et le connecteur d'agent devient un moat opérationnel autant qu'informationnel, distinct de la data propriétaire textuelle.

Sur [[concepts/metriques-visibilite-geo]], les trois métriques posées (Imp_wc, Imp_pos, Subjective Impression) mesurent la citation dans une réponse générative textuelle. Elles ne couvrent pas la sélection produit par un agent commerce, qui produit une action d'achat plutôt qu'une phrase citante. La ligne à ajouter est la suivante : le canal agent commerce demande une seconde grille de mesure, distincte de la citation, structurée autour du taux de sélection produit par requête, du volume de commandes déclenchées via connecteur agent, et du rapport entre catalogue synchronisé complet et catalogue partiel.

L'angle propriétaire pour un consultant SEO ou GEO qui suit un vendeur Salesforce.

Un. Séparer explicitement la mesure de la présence dans la réponse générative (canal search organique via AI Overviews, ChatGPT, Perplexity) de la mesure de la sélection produit par un agent commerce (canal ChatGPT via Agentforce). Ne pas agréger les deux dans un score unique de visibilité IA, ce sont deux mécaniques distinctes.

Deux. Auditer le flux catalogue en amont du connecteur avant d'auditer la page produit publique. Si le flux Business Manager n'est pas correctement peuplé (attributs conversationnels manquants, inventaire décalé), l'agent ne sélectionnera pas le produit, indépendamment de la qualité SEO du site public.

Trois. Documenter la condition d'entrée effective. Le connecteur ChatGPT est en GA prévue en juillet mais pas encore effective au 6 juillet. Aucune adoption chiffrée n'est publiée par Salesforce à date. Ne pas présenter à un client des projections de commandes via canal agent tant qu'un cohort d'usage réel n'est pas mesuré.

Quatre. Ne pas confondre annonces multi-moteurs et disponibilité simultanée. ChatGPT est daté en juillet, Google AI Mode et Gemini sont datés "plus tard dans l'été", sans engagement de calendrier public. Les deux canaux doivent être suivis séparément.

Prédiction P-2026-07-06-v2-1 : d'ici le 31 décembre 2026, Salesforce ou un cabinet indépendant publie une mesure du taux de sélection produit par l'agent Shopper Agentforce sur un cohort d'au moins dix clients Salesforce, avec ventilation par catégorie de produits. Si aucune mesure n'est publiée, le connecteur reste au stade "GA annoncée sans cohorte de mesure", et le fait franchement neuf reste la disponibilité technique, pas la performance mesurée.

Prédiction P-2026-07-06-v2-2 : d'ici le 31 décembre 2026, au moins un connecteur d'agent commerce concurrent sur Shopify, BigCommerce ou Adobe Commerce atteint la GA sur ChatGPT sur un périmètre équivalent aux trois agents Salesforce. Si aucun n'atteint la GA, l'avance de Salesforce sur le canal ChatGPT enterprise reste au stade opérationnel.

## Brèves

### B1. Actualité SEO : Fabrice Canel se retire de Microsoft Bing, aucun successeur nommé

Fabrice Canel, Principal Product Manager en charge de l'indexation chez Bing, [a annoncé sur son compte X @facan sa retraite de Microsoft effective le 1er juillet 2026](https://x.com/facan/status/2072214413827002384). L'information est reprise par [Search Engine Land, article de 5h39](https://searchengineland.com/fabrice-canel-retires-from-microsoft-bing-after-legendary-career-481397), [Search Engine Journal](https://www.searchenginejournal.com/fabrice-canel-longtime-bing-search-leader-retires-from-microsoft/581247/), [Search Engine Roundtable](https://www.seroundtable.com/fabrice-canel-retires-41602.html) et [Optimixed](https://www.optimixed.com/fabrice-canel-retires-from-microsoft-after-almost-30-years/). Canel invoque la Voluntary Retirement Program de Microsoft après près de trente ans dans l'entreprise. Il a dirigé l'équipe crawling et indexing de Bing, a été à l'origine du protocole IndexNow, et a contribué à la construction de Bing Webmaster Tools.

Aucun successeur n'est nommé au 6 juillet 2026. La question de la continuité de la voix publique de Bing sur les sujets d'indexation et d'IndexNow reste ouverte : le rôle a été personnifié par Canel pendant plus d'une décennie et concentrait la relation avec la communauté SEO et webmasters. La prédiction P-2026-07-02-4 (nomination d'un successeur Canel documentée) reste ouverte, avec une contrainte de date supplémentaire : le départ est acté, la succession non annoncée.

### B2. Actualité SEO : Microsoft détecte une extension Chrome qui usurpe Perplexity et intercepte chaque touche saisie dans la barre d'adresse

Microsoft Threat Intelligence a publié [le 29 juin 2026 l'analyse d'une extension Chromium malveillante nommée "Search for perplexity ai"](https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/), signée par Asutosha Panigrahi, Ashwani Kumar et Mohd Sadique. L'extension, identifiant `flkebkiofojicogddingbdmcmkpbplcd`, utilise un domaine typosquattant (perplexity-ai[.]online) pour imiter le domaine légitime perplexity.ai. La couverture indépendante confirme la découverte : [The Hacker News](https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html), [Malwarebytes](https://www.malwarebytes.com/blog/privacy/2026/07/fake-perplexity-chrome-extension-spies-on-your-searches), [TechRepublic](https://www.techrepublic.com/article/news-fake-perplexity-chrome-extension-searches/), [Windows Report](https://windowsreport.com/malicious-perplexity-ai-chrome-extension-removed-after-microsoft-warning/) et [Tech Times](https://www.techtimes.com/articles/319360/20260630/fake-perplexity-chrome-extension-how-one-permission-combo-logged-every-keystroke.htm).

L'extension abuse trois capacités techniques déclarées dans le manifest MV3. La permission `chrome_settings_overrides` remplace le moteur de recherche par défaut du navigateur. Les permissions `declarativeNetRequest`, `declarativeNetRequestFeedback` et `declarativeNetRequestWithHostAccess` permettent d'intercepter et de réécrire les requêtes réseau vers un serveur contrôlé par l'attaquant. Chaque caractère saisi dans la barre d'adresse (y compris les recherches partielles ou abandonnées) est transmis au serveur attaquant avant validation utilisateur, avec l'IP, les en-têtes et le user-agent, avant redirection vers un moteur légitime (Perplexity, Google ou Bing). Microsoft précise que Google a retiré l'extension après signalement responsable, sans publier de chiffre d'installations touchées.

Pour un consultant SEO ou GEO, le fait a deux portées. Sur l'axe mesure de trafic, une extension qui intercepte les requêtes utilisateur avant émission vers un moteur crée un canal de captation invisible pour l'éditeur ciblé et pour les outils d'analytics standards. Sur l'axe surface de citation, l'usurpation d'identité d'un moteur d'IA générative dans une extension d'installation grand public élargit le périmètre d'exposition à protéger au-delà du site : recommander à un client de vérifier la présence de son moteur préféré comme extension officielle vérifiée, et non comme extension tierce marketée par une image similaire.

### B3. Business SEO : Anthropic étend Claude Enterprise via Microsoft Foundry en GA et ajoute des contrôles administrateurs à Claude Enterprise

Anthropic a annoncé [le 29 juin 2026 la disponibilité générale de Claude dans Microsoft Foundry](https://www.anthropic.com/news/claude-in-microsoft-foundry), reprise sur [le blog Claude d'Anthropic](https://claude.com/blog/claude-in-microsoft-foundry), avec Claude Opus 4.8 et Claude Haiku 4.5 accessibles via la Messages API, en environnement Azure, avec zone de données US et infrastructure NVIDIA GB300 Blackwell Ultra. La couverture indépendante inclut [Windows News](https://windowsnews.ai/article/anthropics-claude-models-hit-general-availability-in-microsoft-foundry-bringing-enterprise-ai-govern.432199), [EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/anthropic-brings-claude-to-microsoft-foundry-with-azure-hosting-and-governance-controls) et [AI Business](https://aibusiness.com/agentic-ai/anthropic-s-claude-models-available-microsoft-foundry). Le 3 juillet 2026, Anthropic a documenté dans ses [notes de version Claude Enterprise](https://releasebot.io/updates/anthropic/claude) l'ajout de contrôles administrateurs (analytique d'usage, entitlements au niveau modèle, alertes de dépense) via un tableau de bord et une Analytics API.

Le fait relatif à la doctrine SEO/GEO n'est pas la disponibilité du modèle. Il est la structure de marché qui s'installe. Le connecteur d'agents commerce Salesforce est GA sur ChatGPT en juillet (OpenAI-Salesforce-Azure OpenAI Service). Claude est GA sur Microsoft Foundry en juin (Anthropic-Microsoft-Azure). Les deux canaux enterprise coexistent sur Azure, sur des grilles de gouvernance et de tarification distinctes. Pour un vendeur qui prépare son adressage IA en entreprise, la conséquence pratique est qu'il ne suffit plus de "brancher son catalogue à ChatGPT". Il faut préparer, à horizon 2026-2027, un accès parallèle aux surfaces Claude Enterprise (Microsoft Foundry, Claude.ai Enterprise, Microsoft 365 Copilot) sous des règles d'accès distinctes de celles d'OpenAI.

L'angle pour un consultant : l'écosystème enterprise IA se structure autour de deux points d'accès distincts (le connecteur commerce côté OpenAI-Salesforce, l'accès Foundry côté Anthropic-Microsoft) et non plus autour d'un unique moteur par entreprise. La condition d'entrée pour être sélectionné par les agents de chaque écosystème diffère, et il n'existe pas de standard commun public au 6 juillet.

Prédiction P-2026-07-06-v2-3 : d'ici le 31 décembre 2026, Anthropic publie une mesure d'adoption Claude Enterprise via Microsoft Foundry (nombre de clients enterprise actifs ou requêtes par mois) sur un périmètre chiffré. Si aucune mesure n'est publiée, le passage GA reste un signal de disponibilité technique et pas une mesure d'usage enterprise consolidée.

---

*Draft SyntheticBrain, 2026-07-06 v2. Rien n'a été envoyé.*
