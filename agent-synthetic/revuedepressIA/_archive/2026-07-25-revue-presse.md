# MCP 2026-07-28 : ce que le passage stateless de mardi prépare pour les outils SEO

**En 15 secondes**

- Le Model Context Protocol, standard qui connecte les agents IA (Claude, ChatGPT, Perplexity, Grok, Mistral) aux outils et données externes, publie sa spec finale 2026-07-28 le 28 juillet. Cœur stateless, extensions Tasks et MCP Apps officielles, durcissement OAuth 2.1.
- Une méta-étude publiée sur arXiv le 15 juillet passe en revue 45 études GEO 2023-2026. Le banc SAGEO Arena mesure 16 pct de recul en présence top-10 après reranking quand on réécrit uniquement le corps d'une page pour l'optimiser.
- Un audit publié dans Search Engine Land le 24 juillet mesure sur 71 entreprises canadiennes une rétention moyenne de 15,6 pct des données d'identité vérifiables par un système de recherche IA.
- Le papier SIGIR 2026 de l'équipe Sprinklr publié cette semaine à Melbourne quantifie ce qui déclenche la citation en premier par un moteur de réponse : pertinence topique et position de liste dominent, prix explicite et timestamp récent aident, formatage n'a quasiment pas d'effet.

## Info du jour, pilier Recherche agentique : la spec finale MCP arrive mardi

Le Model Context Protocol publie sa spec [2026-07-28 le 28 juillet 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). C'est la révision la plus lourde du protocole depuis son lancement, publiée en release candidate le 21 mai 2026 pour une fenêtre de validation de dix semaines.

Ce que change la spec, tel que la [note officielle du 21 mai 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) le publie, que [WorkOS le documente le 18 juin 2026](https://workos.com/blog/mcp-2026-spec-agent-authentication), puis que [Digital Applied le récapitule le 21 juillet 2026](https://www.digitalapplied.com/blog/mcp-2026-07-28-spec-stateless-migration-guide) :

- Le cœur du protocole passe stateless. Le handshake `initialize`/`initialized` disparaît, le header `Mcp-Session-Id` est supprimé, les informations client circulent sur `_meta` à chaque requête. Un serveur MCP distant peut désormais tourner derrière un load balancer round-robin sans session partagée ni sticky routing. Deux nouveaux headers `Mcp-Method` et `Mcp-Name` permettent le routage par load balancer sans inspection du body.
- Deux extensions officielles sont incluses. MCP Apps délivre des interfaces HTML rendues serveur dans des iframes sandboxées, avec communication JSON-RPC. Tasks passe hors du cœur : les serveurs répondent à `tools/call` avec des handles de tâches, les clients pilotent via `tasks/get`, `tasks/update`, `tasks/cancel`. L'ancien `tasks/list` est supprimé (plus de session à laquelle rattacher la requête).
- L'autorisation est durcie. Six SEPs imposent OAuth 2.1, la RFC 9728 (OAuth 2.0 Protected Resource Metadata), la RFC 8707 Resource Indicators pour bloquer le rejeu de tokens, la vérification d'issuer via RFC 9207, et le remplacement du Dynamic Client Registration par Client ID Metadata Documents (CIMD).
- Roots, Sampling et Logging sortent du cœur au titre d'une politique formelle de dépréciation de douze mois minimum.

Ce que cela change pour les outils SEO, littéralement : chaque éditeur (crawler, index de mots-clés, base de backlinks, connecteur GSC) qui expose un serveur MCP peut être invoqué par un agent (Claude Desktop, ChatGPT via connecteurs, Perplexity Pro/Max/Enterprise, Copilot, Grok) au moment où l'utilisateur pose sa question. [Semrush a branché son connecteur MCP dans Perplexity le 3 juin 2026](https://www.semrush.com/news/460693-semrush-launches-mcp-connector-in-perplexity-integrating-search-intelligence-within-the-ai-search-engine/), avec un accès à 28,4 milliards de mots-clés, 43 000 milliards de backlinks et 808 millions de profils de domaines. C'est aujourd'hui le seul éditeur SEO référencé à documenter un branchement de production sur cet écosystème.

Le passage stateless a un effet infrastructurel direct : l'hébergement d'un serveur MCP devient scalable horizontalement sans session store partagé. Aucun chiffre de baisse de coût n'est publié par les mainteneurs, WorkOS ou Digital Applied. Le gain est qualitatif : compatibilité avec les load balancers standards, plus de dépendance à des stateful routers. Nate Barbettini, ingénieur fondateur d'Arcade, [cité par TechCrunch le 20 juillet 2026 et repris par Digital Applied](https://www.digitalapplied.com/blog/mcp-2026-07-28-spec-stateless-migration-guide) : « Every one of those machines has to know about a session ID that some other machine handed out. »

Adoption mesurée par [Digital Applied le 21 juillet 2026](https://www.digitalapplied.com/blog/mcp-2026-07-28-spec-stateless-migration-guide) : environ 9 652 records de serveurs dans le registre officiel MCP (dernier pull daté du 24 mai 2026), 28 959 records toutes versions confondues. Anthropic estimait plus de 10 000 serveurs MCP publics actifs en décembre 2025. Les clients MCP recensés au 21 juillet 2026 : Claude, ChatGPT, Perplexity, Grok, Mistral.

Ce que la spec ne dit pas, et qu'il faut noter :

- Aucun impact chiffré sur le classement organique n'est mesuré. On sait que Semrush et Perplexity sont connectés depuis le 3 juin, on ne sait pas combien de sessions Perplexity aboutissent à une requête Semrush, ni ce que ça change côté trafic pour les sites cités par les réponses générées.
- La rupture de session force les clients Tier 1 (Claude Desktop, ChatGPT connecteurs, Perplexity Pro) à mettre à jour leurs SDKs dans la fenêtre de dix semaines qui s'achève mardi. Une désynchronisation entre client et serveur produira des erreurs silencieuses côté agent.
- Aucun calendrier public n'existe pour un connecteur MCP officiel de Google Search Console ou Google Ads. Un connecteur GSC officiel serait le signal d'adoption le plus fort côté SEO, il n'existe pas au 25 juillet 2026.

Prédictions vérifiables pour cette info du jour :

- P-2026-07-25-1 : au 31 octobre 2026, au moins un des trois éditeurs SEO parmi Ahrefs, Similarweb et Screaming Frog publie un connecteur MCP en production documenté publiquement.
- P-2026-07-25-2 : au 31 décembre 2026, aucun connecteur MCP officiel Google Search Console ou Google Ads n'est publié par Google.
- P-2026-07-25-3 : au 31 mars 2027, le registre officiel MCP dépasse 15 000 records de serveurs actifs distincts (mesure Digital Applied ou registre officiel).

Concept doctrine relié : [[concepts/agentic-search]]. Le protocole d'interfaçage devient un enjeu de sourcing pour les moteurs de réponse. Une entreprise qui ne publie pas de serveur MCP interne perd la possibilité d'être interrogée par un agent utilisateur au moment de la formulation d'une réponse.

## Brève 1, pilier GEO : la méta-étude Martinez chiffre les pertes d'une réécriture GEO isolée

Olivier Martinez publie sur arXiv le [15 juillet 2026, identifiant 2607.14035](https://arxiv.org/abs/2607.14035), une survey critique de 45 études GEO publiées entre novembre 2023 et juillet 2026. [Luis Rijo en publie la synthèse dans PPC Land le 20 juillet 2026](https://ppc.land/survey-of-45-studies-finds-geo-rewrites-can-cut-a-pages-ai-retrieval-16/).

Le fait mesuré, à l'échelle du banc SAGEO Arena (171 003 documents, 2 700 requêtes) : optimiser uniquement le corps d'une page pour améliorer sa présence dans les moteurs de réponse produit un recul de 9 pct en top-20, un recul de 16 pct en top-10 après reranking, et une baisse de 6 pct de la citation finale. La réécriture GEO isolée peut donc dégrader la visibilité qu'elle est censée améliorer.

Autres mesures documentées par Martinez, confirmées par les études référencées et relayées dans la synthèse PPC Land :

- Overlap URL entre Google organique, AI Overviews et Gemini : 0,11 à 0,18.
- 53 pct des domaines cités par AI Overviews Google sont absents du top 10 organique de la même requête.
- 51,5 pct des phrases générées par les quatre moteurs de réponse testés sont pleinement supportées par une citation.
- Instabilité de plateforme : sur des runs répétés à température zéro, 9 à 28 pct des décisions changent. 57,8 pct des répétitions ChatGPT ne déclenchent pas la recherche web.

Verbatim Martinez ([abstract arXiv](https://arxiv.org/abs/2607.14035)) : « The evidence is narrow: already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect. »

Concept doctrine relié : [[concepts/metriques-visibilite-geo]]. La mesure de citation IA n'est pas stationnaire d'une plateforme à l'autre, et un score composite unique masque un arbitrage négatif possible (une amélioration mesurée dans un contexte peut coïncider avec une perte dans un autre).

## Brève 2, pilier GEO : le papier SIGIR de Sprinklr quantifie ce qui déclenche la citation en premier

Rahul Vishwakarma, Shushant Kumar et Ratnesh Jamidar de Sprinklr publient dans les [actes ACM SIGIR 2026 le papier « What Gets Cited: Competitive GEO in AI Answer Engines »](https://doi.org/10.1145/3805712.3808445). Le papier est présenté à SIGIR 2026 tenue à Melbourne du 20 au 24 juillet 2026. Version arXiv originale [2605.25517 soumise le 25 mai 2026](https://arxiv.org/abs/2605.25517).

Protocole expérimental : banc RAG deux-documents, brand anonymization, contre-balancement de l'ordre des sources, 252 000 essais sur six LLMs distincts, 18 facteurs de contenu testés.

Ce que le modèle mixte identifie comme prédicteurs de la citation en premier :

- Pertinence topique et position dans la liste : effets dominants.
- Prix explicite et timestamp récent : effets positifs stables.
- Complétude et signaux de confiance : effets marginaux.
- Formatage : effet quasi nul.

Note à l'usage : le papier bénéficie désormais d'une publication peer-reviewed dans une conférence de rang A de la recherche d'information (SIGIR). Il n'existe toujours pas de reproduction indépendante par une équipe tierce sur un panel étendu, ce qui restait la condition attendue pour promouvoir ce résultat au-delà du signal Sprinklr.

Concept doctrine relié : [[concepts/entites-vectorielles]]. La pertinence topique et la position de liste, qui dominent, sont alignables par les pratiques SEO existantes (couverture d'entités, structure de rétention). Le prix et le timestamp sont des leviers d'infrastructure de contenu, pas d'écriture.

## Brève 3, pilier Actualité SEO : un audit sur 71 entreprises canadiennes mesure une fuite d'identité de 84 pct

Donna Rougeau publie sur Search Engine Land le [24 juillet 2026 un audit de 71 entreprises vérifiées de l'Île-du-Prince-Édouard, Canada](https://searchengineland.com/ai-search-cant-verify-business-fix-483376). L'audit note chaque entreprise sur une échelle fixe de 485 points, sur cinq catégories : entité principale de l'entreprise, fondations techniques, collecte initiale de données, vérification d'entité senior, présence des pages de politique.

Verticaux couverts : agroalimentaire, retail, services professionnels, technologie, agriculture, santé, hôtellerie, golf.

Chiffres publiés :

- Les entreprises retiennent en moyenne 15,6 pct de leurs données d'identité vérifiables. Environ 84 pct des informations d'identité fuient hors du champ récupérable par un système de recherche IA.
- 17 pct de l'échantillon, soit approximativement 12 entreprises, n'ont aucune présence numérique récupérable par une IA.
- 22 des 71 entreprises (environ 31 pct) ont une information de dirigeants nommée mais confinée à des sous-pages plutôt que sur la page d'accueil.

Recommandations opérationnelles publiées par Rougeau : ajouter les informations de dirigeants nommés sur les pages visibles, rendre serveur les faits critiques (nom, adresse, services, direction), consolider les domaines fragmentés en une URL canonique, vérifier que les enregistrements de domaine restent actifs, inclure des politiques de confidentialité et conditions d'utilisation liées, et faire remonter les chemins de réservation directs au-dessus des revendeurs tiers.

Verbatim Rougeau : « There's a gap between what a business is in the real world and how an AI search system can verify it. I call this the 'identity leak.' »

Limites documentaires : l'audit porte sur un échantillon géographiquement homogène (Île-du-Prince-Édouard), il n'est pas reproduit sur une autre juridiction ni sur un panel plus large. Le score utilisé est propriétaire au cabinet de l'auteur, il n'a pas encore de reproduction indépendante.

Concept doctrine relié : [[concepts/e-e-a-t]]. La vérifiabilité des attributs d'entité (dirigeants nommés, NAP consistent, politiques liées, ancienneté de domaine) devient un préalable à la retrievabilité par un moteur de réponse, distinct de la question du classement organique.

---

Draft SyntheticBrain. Rien n'a été envoyé.
