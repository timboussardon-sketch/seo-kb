# Bing supprime 90 000 URL d'un site YMYL cité 90 000 fois par ChatGPT et publie sa doctrine anti-spam : détecteur de motif, jamais one-off

*Édition du 18 juillet 2026. Pilier Niche SEO.*

## L'essentiel en 5 points

- Bing a retiré la totalité des URL d'un site YMYL le 10 juillet 2026, environ 48 heures après un signalement public de Lily Ray et Barry Schwartz à Krishna Madhavan, principal product manager Bing.
- Le site cumulait environ 90 000 URL indexées côté Bing et plus de 90 000 citations dans des réponses ChatGPT, alors qu'il affichait une visibilité organique quasi-nulle sur Google et aucun signal éditorial standard (auteur, contact, société).
- Krishna Madhavan a publié en clair la doctrine d'application Microsoft : pas de sanction site par site, l'équipe entraîne un détecteur qui applique la règle à tout site présentant le même motif.
- L'événement documente par les faits que la disponibilité d'un site dans les réponses ChatGPT en mode Search dépend directement de sa présence dans l'index Bing, et qu'un retrait d'index entraîne un recul des citations en aval.
- Le cas ouvre une question opérationnelle pour les consultants SEO/GEO : jusqu'où l'exposition à un seul moteur, Bing pour ChatGPT et Google pour AI Overviews et AI Mode, constitue un risque de perte de citation mesurable et documentable dans un audit.

---

## Info du jour. Un site YMYL retiré de Bing en 48 heures, une doctrine d'application publiée

### Ce qui s'est passé, dans l'ordre

Le 22 juin, Glenn Gabe (GSQI) publie une étude de cas intitulée *Surging in ChatGPT, Dead in Google* décrivant un site YMYL dans le domaine santé. Le site publie du contenu massivement généré par IA, sans byline auteur, sans mentions légales, sans page de contact. Côté Google, il est indexé sur environ 45 000 URL et se classe autour des positions 7 à 8. Côté Bing, il a environ 88 000 URL indexées et de bons classements. Et il apparaît dans plus de 90 000 réponses ChatGPT ([Glenn Gabe, GSQI, 22 juin 2026](https://www.gsqi.com/marketing-blog/surging-in-chatgpt-dead-in-google/)).

Le 8 juillet, Lily Ray et Barry Schwartz signalent publiquement le site à Krishna Madhavan, principal product manager Microsoft Bing, sur X. Madhavan répond qu'il va regarder.

Le 10 juillet, environ 48 heures plus tard, Bing supprime l'intégralité des URL du site de son index, soit près de 90 000 URL selon l'analyse publiée par Digital Applied le 14 juillet ([Digital Applied, 14 juillet 2026](https://www.digitalapplied.com/blog/bing-algorithmic-deindexing-chatgpt-visibility-spam-2026)). Le même jour, Madhavan publie sur X la formule qui sera reprise dans la couverture SEO : *« we do not do one offs....not scalable.... »*, verbatim rapporté par Barry Schwartz sur Search Engine Roundtable le 13 juillet ([Search Engine Roundtable, 41670, Barry Schwartz, 13 juillet 2026](https://www.seroundtable.com/bing-indexing-penalties-41670.html)) et repris par Optimixed le même jour ([Optimixed, 13 juillet 2026](https://www.optimixed.com/microsoft-bing-does-not-do-one-off-indexing-penalties-not-scalable/)).

### Ce que dit précisément Madhavan

Madhavan clarifie deux choses. D'abord, il refuse la logique d'une sanction ciblée site par site : *« not scalable »* signifie que Microsoft Bing ne construit pas une exception pour un site donné. Ensuite, il décrit la mécanique effectivement employée : l'équipe identifie un motif de spam, entraîne un détecteur sur ce motif, et applique le résultat à tous les sites qui présentent ce motif simultanément. Le site retiré le 10 juillet est présenté comme un cas particulier d'une classe plus large qui a été retirée en même temps.

Cette formulation constitue le premier énoncé public d'une politique d'application anti-spam par Bing depuis le déploiement du rapport AI Performance dans Bing Webmaster Tools en février 2026 et son extension par intents, topics et citation share le 16 juin 2026 (déjà couverts).

### Ce que le fait démontre pour ChatGPT en mode Search

Le lien entre présence Bing et citation ChatGPT n'était jusqu'ici documenté que par des études de corrélation. Le cas fournit un signal quasi-causal : le site alimentait ChatGPT via son grounding sur l'index Bing, et sa disparition de l'index a été publiquement flaguée par Lily Ray et Schwartz comme l'événement précédant, et permettant, le retrait des citations qui suivait. Digital Applied documente le retrait des URL mais ne publie pas de vérification chiffrée du recul des citations ChatGPT post-10 juillet. Aucune analyse indépendante n'a été publiée à ce jour sur cet effet aval mesuré.

### Trois limites documentaires à publier avec l'analyse

D'abord, le site reste anonymisé dans toutes les publications, y compris celle de Gabe. Aucune vérification indépendante du nom, du domaine ou du profil de contenu n'est possible depuis les publications actuelles. Ensuite, Digital Applied est à ce jour la seule publication à documenter le chiffre de 90 000 URL retirées côté Bing. Les autres sources rapportent qualitativement « removed from index » sans reprendre le chiffre. Enfin, aucune source ne documente un chiffre post-10 juillet sur l'évolution des 90 000+ citations ChatGPT. Le retrait aval est plausible mais reste à mesurer.

### Ce que ça change pour un audit SEO/GEO client

Cette édition articule quatre concepts de doctrine, chacun avec un rôle distinct :

- [[concepts/e-e-a-t]]. Les trois signaux absents du site (byline auteur, page de contact, société) sont ceux qui apparaissent en priorité dans le Search Quality Rater Guidelines pour qualifier Experience et Trustworthiness sur un site YMYL santé. Le cas confirme que leur absence conjuguée à la génération massive IA constitue un motif industriellement détectable, pas seulement une lecture manuelle.
- [[concepts/metriques-visibilite-geo]]. La dépendance à un seul moteur pour l'alimentation d'un autre moteur (ici Bing pour ChatGPT) constitue une dimension de risque non couverte par les métriques de citation en usage. La mesure à ajouter dans un audit : part de citations dans un moteur cible A qui dépendent structurellement de l'indexation dans un moteur B.
- [[concepts/tabou-visibilite]]. La métrique proposée ci-dessus n'est pas de la visibilité, c'est un risque. La documenter dans un rapport client sous l'étiquette « visibilité » diluerait le message. Le terme opérationnel est *dépendance de grounding* ou *exposition mono-moteur*.
- [[concepts/parasite-seo]]. Le site retiré n'exploitait pas l'autorité de Bing au sens réglementaire de site reputation abuse Google, mais l'affaire éclaire une adjacence : ChatGPT parasite l'index Bing pour son grounding, et un site parasite l'index Bing pour son exposition ChatGPT. Le motif de risque est symétrique.

Pour un audit client sur une verticale YMYL (santé, finance, juridique), la démarche opérationnelle qui découle du cas comporte trois étapes distinctes. Vérifier que le site est indexé côté Bing avec un volume cohérent avec Google, en utilisant Bing Webmaster Tools. Documenter la présence dans le rapport AI Performance de Bing (Copilot) et croiser avec un outil de mesure côté ChatGPT (Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Profound) pour établir la dépendance de grounding. Publier explicitement le risque de dépendance mono-moteur dans le rapport client, distinct des KPI de citation.

### Prédictions vérifiables

- **P-2026-07-18-1** : dans les 90 jours (31 octobre 2026), un deuxième site YMYL nommé publiquement sera identifié comme retiré par le même détecteur de motif Bing, avec une chronologie signalement → retrait similaire.
- **P-2026-07-18-2** : avant le 31 décembre 2026, Microsoft publiera dans un billet blog.bing.com, un support doc ou une intervention publique de Krishna Madhavan une clarification écrite de la doctrine *« pattern detector, no one-offs »* nommant au moins un motif identifié.
- **P-2026-07-18-3** : avant le 31 mars 2027, une étude tierce (Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Profound ou équivalent) publiera une mesure de corrélation entre présence Bing et taux de citation ChatGPT sur un panel > 1000 sites.

---

## Brèves

### B1. Actualité SEO / GEO : les Top Stories arrivent dans les AI Overviews de Google, en direct US mobile

Barry Schwartz a publié le 17 juillet sur Search Engine Land la confirmation par un porte-parole Google que le carrousel Top Stories est désormais pleinement déployé dans les AI Overviews, aux États-Unis, sur mobile ([Barry Schwartz, Search Engine Land, 482615, 17 juillet 2026](https://searchengineland.com/top-stories-roll-out-in-google-ai-overviews-482615)). Cette étape formalise l'annonce faite à Google I/O en mai 2026 (« fresh perspectives, new updates and prominent links ») et documentée en amont par Search Engine Roundtable ([Barry Schwartz, Search Engine Roundtable, 41583, 29 juin 2026](https://www.seroundtable.com/google-top-stories-ai-overviews-41583.html)).

Le carrousel affiche des articles éditoriaux d'actualité (New York Times, Yahoo cités par la documentation Search Engine Roundtable) et intègre les Preferred Sources sélectionnées par l'utilisateur en priorité, lorsqu'un article de ces sources est disponible sur le sujet. Preferred Sources a franchi le seuil de 345 000 sources uniques sélectionnées au 27 mai 2026 selon Google (aucune donnée d'adoption US publiée depuis) et son extension aux AI Overviews et AI Mode a démarré en juin 2026 ([Search Engine Journal, 576032, 30 mai 2026](https://www.searchenginejournal.com/google-preferred-sources-hit-345k-expand-into-ai-search/576032/)).

Pour un éditeur presse, deux conséquences distinctes se dégagent. La surface AI Overviews expose désormais un slot éditorial prioritaire, avec un mécanisme de sélection utilisateur (Preferred Sources) qui ne dépend pas des seuls signaux algorithmiques. Aucune donnée n'est publiée sur la part des AI Overviews américains sur mobile qui affichent ce carrousel, ni sur le taux de clic effectif vers les articles listés. Attendre ces deux mesures avant de traiter Top Stories AIO comme un canal de trafic mesurable.

### B2. GEO : Nick Fox chiffre le trafic AI Search en milliards de clics hebdomadaires, sans publier de méthode ni de dénominateur

Nick Fox, SVP Knowledge and Information chez Google, a publié le 17 juillet une prise de parole sur LinkedIn et X déclarant que Google envoie des milliards de clics par jour vers le web, et *« billions of clicks to websites every week through AI features in Search alone – and we're just getting started »*, verbatim ([Matt G. Southern, Search Engine Journal, 582755, 17 juillet 2026](https://www.searchenginejournal.com/google-puts-a-number-on-ai-search-clicks-without-the-data/582755/)).

Matt Southern souligne dans son cadrage l'absence de trois éléments dans la publication de Fox : aucune comparaison entre le chiffre hebdomadaire AI Search et le chiffre quotidien Search agrégé, aucun dénominateur (part des sessions AI Search qui produisent un clic), et aucun accès à la mesure au niveau site (le rapport AI Performance dans Google Search Console reste limité aux impressions, sans clics ni CTR ni requêtes détaillées).

Le fait s'articule frontalement avec [[concepts/tabou-visibilite]] : la formulation *« billions of clicks weekly »* est un chiffre sans unité de comparaison ni protocole de mesure vérifiable côté éditeur. Un consultant SEO/GEO ne peut ni le corroborer sur ses propres logs, ni le décomposer par vertical. La publication renforce le motif observé sur les autres publications d'agrégats côté Google (par exemple les 32 millions d'instances Google SearchViewer citées par Profound le 14 juillet dans AI Mode, déjà couvertes) : le chiffrage vient d'une couche opaque et n'est pas rapprochable des mesures internes. Documenter dans un rapport client la distinction entre chiffre agrégé Google et mesure au niveau site propre.

### B3. Recherche agentique : le navigateur Perplexity Comet passe l'agent en Opus 4.6 par défaut pour les utilisateurs Max et étend l'accès iOS

Perplexity a publié en juillet 2026 une mise à jour du navigateur Comet dans laquelle l'agent Comet Browser Agent est désormais servi par Claude Opus 4.6 par défaut pour les abonnés Max et Claude Sonnet 4.6 pour les abonnés Pro ([Perplexity Changelog, juillet 2026](https://www.perplexity.ai/changelog)). L'utilisateur Max peut sélectionner entre plusieurs modèles : Sonar (moteur propriétaire Perplexity), Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4, Gemini 3.1 Pro et Kimi K2.5. Comet a également étendu son accès iOS à l'ensemble des utilisateurs sur cette période et introduit un mode voix par GPT Realtime 1.5 permettant les interactions vocales continues avec l'onglet actif.

Cette mise à jour vient s'ajouter à l'annonce Perplexity Space du 15 juillet 2026 déjà couverte (édition du 16 juillet v2, angle runtime agent). Deux niveaux distincts se dégagent pour le pilier Recherche agentique : la couche runtime (Space, microVM Firecracker) et la couche modèle piloté par l'utilisateur (Comet Agent, choix Opus 4.6). Un consultant SEO/GEO chargé d'un audit d'exposition agent doit désormais tenir compte de deux dimensions supplémentaires : la fenêtre de raisonnement du modèle choisi côté navigateur agentique (Opus 4.6 vs modèles moins profonds pouvant modifier la sélection des sources) et la persistance de la session sandbox (déjà documentée pour Space).

Limite documentaire : Perplexity Changelog est la seule source primaire. Aucun analyste tiers (SEL, SEJ, Search Engine Roundtable) n'a publié une couverture éditoriale indépendante de cette bascule modèle par défaut à date. Traiter comme fact vendeur unique jusqu'à corroboration.

---

*Édition produite par SyntheticBrain (agent revue de presse SEO/IA). Rien n'a été envoyé. Draft.*
