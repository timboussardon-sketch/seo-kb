---
title: "Algorithme — édition du 14 juin 2026 (v2)"
date: 2026-06-14
pillar: recherche-agentique
sources_count: 13
author: SyntheticBrain
---

# Google publie l'Open Knowledge Format, une spécification ouverte pour la mémoire des agents IA

> Édition du samedi 14 juin 2026, v2. Pilier : **Recherche agentique**.

## Résumé

- Le 12 juin, Google Cloud a publié l'Open Knowledge Format (OKF) v0.1, une spécification ouverte construite sur des fichiers markdown et un YAML frontmatter, qui formalise la manière dont les agents IA stockent, partagent et consomment les connaissances d'une organisation. La spec reprend explicitement le pattern public proposé par Andrej Karpathy en avril 2025.
- Données Similarweb publiées le 11 juin pour mai 2026 : ChatGPT passe de 76,4 % à 52,7 % du trafic web mondial vers les plateformes IA en douze mois, Claude passe de 1,6 % à 8,9 % et Gemini de 8,9 % à 27,3 %.
- PPC Land documente le 14 juin la fermeture du site overfishing.org après vingt et un ans d'exploitation, son propriétaire mesurant un trafic ramené de 750 visiteurs uniques par jour à 50 lors des fenêtres où AI Overviews est actif dans la région testée. Le cas s'ajoute à All About Berlin (-70 % de trafic de recherche) et à la fermeture de Bauer Xcel Media Deutschland (160 emplois, fermeture 30 septembre 2026 annoncée le 14 avril 2026).
- Le rapport Gracenote « Plot Holes in AI » publié le 10 juin teste un modèle IA non ancré (Claude Sonnet 4.0) sur 2 600 films et séries dans 13 pays : pour 506 titres, soit 19,5 % de l'échantillon, l'ensemble des six attributs métadonnées testés (titre, description, acteurs, genres, année de sortie, durée) est entièrement halluciné.

## Info du jour — Google formalise un format ouvert pour la mémoire des agents IA

Pilier : **Recherche agentique**.

Sam McVeety, Tech Lead Data Analytics chez Google Cloud, et Amir Hormati, Tech Lead BigQuery chez Google Cloud, ont publié le 12 juin 2026 l'Open Knowledge Format (OKF) v0.1, sur le [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/). Le code, la spécification et trois bundles d'exemple sont disponibles dans le dépôt [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) sur GitHub.

La spécification est volontairement minimale. Un dépôt OKF est un dossier de fichiers markdown avec un YAML frontmatter. Le seul champ obligatoire est `type` ; les champs `title`, `description`, `resource`, `tags`, `timestamp` sont recommandés. Deux noms de fichiers sont réservés : `index.md` pour l'énumération du contenu, `log.md` pour l'historique chronologique. Il n'y a ni registre de schéma centralisé, ni autorité de gouvernance, ni SDK obligatoire. Un dépôt OKF est lisible par `cat`, transportable par `git clone`, consommable par un serveur de fichiers statiques, une UI de knowledge management (Obsidian, Notion, MkDocs), un LLM qui charge les fichiers dans son contexte, un index de recherche ou un viewer de graphe.

Google fournit deux implémentations de référence : un agent d'enrichissement qui parcourt les datasets BigQuery, rédige les fiches concept des tables et des vues, puis les enrichit avec citations, schémas et chemins de jointure via une passe LLM ; et un visualiseur HTML statique qui transforme n'importe quel bundle OKF en graphe interactif autocontenu. Trois bundles prêts à parcourir sont fournis : un bundle GA4 e-commerce, un bundle Stack Overflow, un bundle Bitcoin sur datasets publics.

Le blog de Google Cloud cite explicitement le pattern public proposé par Andrej Karpathy dans son [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (avril 2025), en reprenant cette phrase de Karpathy : « LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass ». Les auteurs Google écrivent que la prise en charge LLM corrige exactement ce qui fait abandonner les wikis personnels par les humains : le coût de maintenance des références croisées et de la mise à jour incrémentale.

Trois sources indépendantes confirment l'annonce et les détails techniques en plus du blog Google Cloud : la couverture [PPC Land](https://ppc.land/googles-okf-wants-to-be-the-lingua-franca-for-ai-agent-knowledge/) (Luis Rijo, 12 juin), la fiche [Welcome.AI](https://www.welcome.ai/content/google-clouds-open-knowledge-format-enhances-ai-interoperability-and-efficiency) et l'article [Shashi.co](https://www.shashi.co/2026/06/google-publishes-plain-text-format-for.html) datés du 12 juin. Le fichier de spécification est consultable directement à [`okf/SPEC.md`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) dans le dépôt GitHub officiel.

OKF se positionne explicitement sous les autres standards émergents pour les agents IA. PPC Land identifie trois initiatives parallèles citées par Google : l'Ad Context Protocol (ACP, lancé fin 2025), l'AAMP de l'IAB Tech Lab (formalisé le 26 février 2026), et la structure hiérarchique de dossiers d'accès aux entrepôts de données via LLM proposée par Meta en août 2025. Le blog Google Cloud écrit qu'OKF « opère à une couche plus générale et inférieure, pas spécifiquement liée au domaine publicitaire ». Le format est aussi explicitement indépendant du Model Context Protocol (MCP) : MCP définit comment un agent appelle des outils, OKF définit ce que l'agent sait avant d'agir.

Pour la doctrine SEO de cette base : OKF apporte une réponse structurelle à une question que la fiche [[concepts/persistent-wiki-vs-rag]] laissait ouverte, celle de la portée du pattern Karpathy. La fiche notait que la proposition de Karpathy était « structurelle et qualitative, pas empirique » et qu'il faudrait la vérifier avec d'autres sources avant d'en faire une doctrine. La réponse n'est pas empirique mais institutionnelle : Google Cloud publie une spécification ouverte du même pattern, avec deux implémentations de référence et trois bundles, et la positionne comme couche d'interopérabilité pour les agents IA. La fiche [[concepts/agentic-search]] gagne par là une couche supplémentaire dans son inventaire : la couche connaissance interopérable, distincte des couches d'identité éditeur (Web Bot Auth, Applebot-Extended), de paiement machine-à-machine (Mastercard AP4M, Visa-OpenAI), d'exécution outillée (MCP, A2A), de gouvernance entreprise (Microsoft Agent 365 Defender, Agent Registry) et de notification événementielle (Google Information Agents AI Mode).

L'implication pour le SEO et le GEO est directe sur un point précis. Pour une marque qui veut être correctement représentée par un agent IA d'entreprise interne (Salesforce, ServiceNow, Microsoft Foundry, Google ADK), structurer son knowledge produit, ses descriptifs, ses politiques et ses datasets en bundles OKF devient un canal direct d'alimentation de la mémoire de l'agent, distinct du SEO sur l'index web public. Le canal SEO classique alimente ce que l'agent voit du monde extérieur ; un bundle OKF alimente ce que l'agent sait de l'organisation qui le déploie. Les deux ne se substituent pas, ils s'additionnent.

Trois limites doivent être nommées explicitement. La v0.1 n'a pas encore de connecteur natif annoncé chez les autres plateformes d'agents : à ce jour, seul Google Cloud Knowledge Catalog l'ingère. L'effet de réseau dépendra de l'adoption par les autres éditeurs enterprise. Le format est vendor-neutral sur le papier mais sous gouvernance Google Cloud sur le dépôt principal ; aucune fondation ou consortium externe n'a encore pris la main. Enfin, OKF ne dit rien des mécanismes de retraitement et de signature : un consommateur OKF doit faire confiance à la source du bundle, comme un consommateur de site web doit faire confiance au domaine éditeur.

Deux prédictions découlent de ce constat :

- P-2026-06-14-v2-1 : au moins un autre acteur enterprise majeur (Microsoft Foundry, AWS Bedrock, Anthropic, Salesforce, ServiceNow ou Databricks) annoncera un connecteur natif OKF, ou un format directement aligné sur la spec, dans une de ses plateformes d'agents IA, d'ici le 31 décembre 2026.
- P-2026-06-14-v2-2 : au moins un éditeur SEO/AEO public (Profound, Otterly, AthenaHQ, Brand Radar, Peec) publiera avant le 31 décembre 2026 un rapport mesurant la corrélation entre adoption d'un format markdown structuré pour la connaissance interne d'une entreprise et taux de citation de cette entreprise dans les réponses LLM.

## Brèves

### Marché des chatbots IA : ChatGPT à 52,7 % du trafic web, Claude à 8,9 %, Gemini à 27,3 %

Pilier : **GEO / search IA**.

Les données Similarweb pour mai 2026, publiées sur LinkedIn le 11 juin et reprises par Luis Rijo sur [PPC Land](https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/) le même jour, mesurent les visites web mondiales tous appareils vers les domaines des plateformes IA génératives. ChatGPT passe de 76,4 % en juin 2025 à 52,7 % en mai 2026, soit une perte de 23,7 points de pourcentage en douze mois. Claude passe de 1,6 % à 8,9 % et enregistre son plus gros gain mensuel à 2,9 points sur la période avril-mai 2026. Gemini passe de 8,9 % à 27,3 %, soit un gain de 18,4 points. DeepSeek mesure 4,0 %, Grok 2,8 %, Copilot 2,0 %, Perplexity 1,3 %.

La reprise [Sedestral](https://sedestral.com/en/blog/ai-search-market-share-2026) confirme la même tendance directionnelle. La mesure Similarweb porte sur les visites web vers les domaines des plateformes, pas sur l'usage applicatif ni sur les surfaces IA insérées dans les moteurs (AI Mode, AI Overviews). Les commentateurs ont souligné une zone d'incertitude méthodologique : la part Gemini mesurée par Similarweb sépare-t-elle les visites vers `gemini.google.com` des surfaces AI Mode et AI Overviews de Google Search ? La réponse n'est pas explicitée par la donnée publiée. Pour cette raison, la mesure se prend comme directionnelle, pas comme part absolue.

L'enseignement pour la pratique GEO est qu'optimiser uniquement pour ChatGPT n'est plus suffisant. La part de Claude est multipliée par cinq et demi en un an, celle de Gemini est multipliée par trois. La rubrique « plateformes prioritaires » d'un outil GEO en septembre 2025 et en juin 2026 n'a pas la même hiérarchie. Cette mesure converge directionnellement avec les rapports First Page Sage juin 2026 (54,7 / 27,4 / 8,2 %) déjà traités dans l'édition du 13 juin, mais l'apport propre est la série longitudinale sur douze mois, qui n'existait pas dans les autres données publiques. Elle teste la prédiction P-2026-06-13-2 qui suit le ratio global trafic AI vs trafic search.

### Le dossier des fermetures éditoriales attribuées à AI Overviews continue de s'épaissir

Pilier : **Actualité SEO**.

Le site overfishing.org, exploité par un opérateur néerlandais nommé Pepijn depuis 2003, a annoncé sa fermeture le 25 février 2024 et sa documentation est analysée par [PPC Land](https://ppc.land/ai-overviews-killed-overfishing-org-and-its-not-alone/) (Luis Rijo, 14 juin). Pepijn documente un pattern oscillatoire pendant les tests régionaux d'AI Overviews fin 2023 : environ 750 visiteurs uniques par jour sur les jours normaux, environ 50 sur les jours où Google active la fonctionnalité dans la région testée. Pepijn cite directement la mécanique : « Whenever Google enabled this in a region the traffic to overfishing.org just disappeared » (post du 22 mai 2026). Le déploiement global d'AI Overviews dans plus de 100 pays en octobre 2024 a produit selon Pepijn une « sharp inflection in publisher traffic data ».

PPC Land croise ce cas avec deux autres dossiers déjà publics. All About Berlin, guide d'expatriés berlinois exploité depuis 2017 par Nicolas Bouliane et documenté par son auteur sur [nicolasbouliane.com](https://nicolasbouliane.com/blog/death-by-ai), mesure une perte de 70 % du trafic de recherche entre octobre 2024 et mai 2026. Bauer Xcel Media Deutschland, branche numérique allemande de Bauer Media Group, a annoncé le 14 avril 2026 sa fermeture quasi complète au 30 septembre 2026, avec suppression de 160 emplois. La couverture [Press Gazette](https://pressgazette.co.uk/publishers/digital-journalism/bauer-unveils-major-digital-restructure-hitting-jobs-in-germany-and-uk/) attribue la décision à la disruption causée par l'IA dans le revenu éditeur, et la couverture [Digiday](https://digiday.com/media/bauer-media-group-slashes-publishing-headcount-in-company-wide-restructure/) précise le périmètre du plan de restructuration.

La trame technique est documentée. Une étude Ahrefs sur 300 000 mots-clés (mars 2024 - mars 2025) mesurait que le premier résultat organique perd en moyenne 34,5 % de ses clics quand un AI Overview est présent. Une étude Pew Research de juillet 2025 mesurait que les utilisateurs ne cliquent sur les sources d'un AI Overview que dans 1 % des cas. Pour la fiche [[concepts/ai-overviews-impact]] (si elle existe, sinon pour la prochaine version doctrine), le cas overfishing.org apporte la précision temporelle utile : la perte se produit dès les tests régionaux, avant le déploiement global. Pour la boucle preuve interne, le pattern « jours actifs / jours non actifs » est une méthode de mesure directe que les éditeurs peuvent reproduire si AI Overviews est actif sur une partie seulement de leurs requêtes.

### Gracenote mesure 19,5 % de titres entièrement hallucinés par un LLM non ancré sur 2 600 films et séries

Pilier : **GEO / search IA**.

Le rapport [Plot Holes in AI](https://gracenote.com/insights/plot-holes-in-ai/) publié le 10 juin par Gracenote, business unit de Nielsen, teste un modèle IA non ancré sur 2 600 films et séries dans 13 pays, et compare ses réponses à un second modèle ancré via un serveur MCP connecté à la base de données vidéo de Gracenote. Le communiqué officiel est publié sur le [centre de presse Nielsen](https://www.nielsen.com/news-center/2026/ungrounded-llm-fabricates-every-detail-for-nearly-1-in-5-movie-and-tv-titles-tested-new-gracenote-report-finds/) le 10 juin. La couverture [Streaming Media](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=175221) et la reprise [PPC Land](https://ppc.land/gracenote-data-shows-ai-hallucinates-1-in-5-streaming-titles-completely/) (Luis Rijo, 10 juin) en confirment les chiffres.

Six attributs métadonnées sont testés par titre : titre, description, acteurs, genres, année de sortie, durée. Pour 506 titres, soit 19,5 % de l'échantillon, l'ensemble des six attributs est entièrement halluciné par l'instance non ancrée. La précision des noms d'acteurs cités sur le top 100 des films américains est de 53 %. Moins d'un tiers des réponses globales sont classées « haute qualité » par le protocole de notation. Le taux d'hallucination complète par pays varie fortement : 28,3 % aux Pays-Bas, 26,5 % en Australie, 21,5 % aux États-Unis, 9,7 % en Allemagne. PPC Land précise que le modèle testé est Claude Sonnet 4.0 dans deux configurations distinctes (ancrée vs non ancrée), avec la même prompt template.

L'enseignement pour la pratique GEO est double. Premièrement, le grounding d'un LLM sur une base de données externe par MCP ne réduit pas l'hallucination à zéro mais la déplace : il y a moins de fabrications complètes et plus de réponses correctes ou partiellement correctes. Deuxièmement, la mesure est faite sur les attributs métadonnées factuels d'une entité connue (titre, acteurs, année). Pour une marque, le risque GEO de représentation par un LLM non ancré est proportionnel à la spécificité de ses entités et à leur représentation dans le corpus d'entraînement. L'angle complète la prédiction P-2026-06-13-v2-1 qui suit la mesurabilité des notifications d'agents IA : ici, c'est la mesurabilité de la précision de représentation des entités qui est ouverte. Le rapport Gracenote établit qu'elle est mesurable, à l'échelle de plusieurs milliers de titres et de plusieurs pays, et qu'un protocole de grounding via MCP fait une différence quantifiable.

## Stratégie et prédictions

L'angle de cette édition est que la course aux standards d'interopérabilité des agents IA passe maintenant par la couche connaissance, après être déjà passée par les couches identité (Web Bot Auth, Applebot-Extended), paiement (AP4M, Visa-OpenAI), exécution (MCP, A2A) et gouvernance (Microsoft Agent 365 Defender). OKF est la première proposition publique d'un standard ouvert pour la mémoire d'un agent, soutenue par un éditeur cloud majeur. Les trois enjeux à surveiller dans les six prochains mois sont l'adoption par un deuxième éditeur cloud, la disponibilité de connecteurs depuis les catalogues existants (Dataplex, Unity Catalog, Collibra) qui figurent déjà comme cas d'usage dans la documentation Google, et l'apparition d'une couche d'audit ou de signature qui manque à la v0.1.

Pour la boucle preuve interne, OKF rapproche aussi la pratique de cette KB d'une convention publique : les conventions `index.md` énumération, `log.md` chronologique append-only, `type` obligatoire dans le frontmatter, sont exactement celles documentées dans `AGENTS.md` de ce dépôt. Le rapprochement est intéressant à observer dans le temps, sans rien en conclure prématurément.

Prédictions ouvertes ajoutées ce run :

- P-2026-06-14-v2-1 : un autre acteur enterprise majeur (Microsoft Foundry, AWS Bedrock, Anthropic, Salesforce, ServiceNow ou Databricks) annonce un connecteur natif OKF ou un format directement aligné, d'ici 2026-12-31.
- P-2026-06-14-v2-2 : un éditeur SEO/AEO public (Profound, Otterly, AthenaHQ, Brand Radar, Peec) publie un rapport mesurant la corrélation entre adoption d'un format markdown structuré pour la connaissance interne d'une entreprise et taux de citation de cette entreprise dans les réponses LLM, d'ici 2026-12-31.

## Sources consultées

Info du jour : [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) (12 juin) ; [GitHub GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) ; [PPC Land](https://ppc.land/googles-okf-wants-to-be-the-lingua-franca-for-ai-agent-knowledge/) ; [Welcome.AI](https://www.welcome.ai/content/google-clouds-open-knowledge-format-enhances-ai-interoperability-and-efficiency) ; [Shashi.co](https://www.shashi.co/2026/06/google-publishes-plain-text-format-for.html) ; [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Brève 1 : [PPC Land](https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/) ; [Sedestral](https://sedestral.com/en/blog/ai-search-market-share-2026).

Brève 2 : [PPC Land overfishing.org](https://ppc.land/ai-overviews-killed-overfishing-org-and-its-not-alone/) ; [nicolasbouliane.com](https://nicolasbouliane.com/blog/death-by-ai) ; [Press Gazette](https://pressgazette.co.uk/publishers/digital-journalism/bauer-unveils-major-digital-restructure-hitting-jobs-in-germany-and-uk/) ; [Digiday](https://digiday.com/media/bauer-media-group-slashes-publishing-headcount-in-company-wide-restructure/).

Brève 3 : [Gracenote](https://gracenote.com/insights/plot-holes-in-ai/) ; [Nielsen news center](https://www.nielsen.com/news-center/2026/ungrounded-llm-fabricates-every-detail-for-nearly-1-in-5-movie-and-tv-titles-tested-new-gracenote-report-finds/) ; [Streaming Media](https://www.streamingmedia.com/Articles/ReadArticle.aspx?ArticleID=175221) ; [PPC Land](https://ppc.land/gracenote-data-shows-ai-hallucinates-1-in-5-streaming-titles-completely/).
