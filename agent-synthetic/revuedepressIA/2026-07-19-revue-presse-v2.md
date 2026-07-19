# Algorithme. 2026-07-19 (v2)

## Résumé

- Apple publie une politique publicitaire pour Apple Maps qui exclut d'entrée tout le bloc home services (plomberie, électricité, serrurerie, HVAC, dératisation, couverture, entreprise générale), les bail bonds et les cryptocurrency ATMs. Politique effective 14 juillet 2026, lancement produit annoncé « cet été » aux États-Unis et au Canada.
- Cette exclusion sépare nettement les deux offres de search local publicitaire : Google Local Services Ads garde tout un pan de verticales rentables auquel Apple refuse l'accès dès le premier jour.
- John Mueller précise via Search Engine Journal le fonctionnement du bouton « Validate Fix » de Search Console : il n'accélère pas le retraitement en soi, il attache un échantillon d'URL à un suivi et prévient une fois le passage constaté. À utiliser après une correction complète, pas URL par URL.
- Perplexity fait entrer son système de mémoire agentique Brain en accès entreprise (lancement Max preview le 18 juin 2026, généralisation entreprise notée dans les release notes du 13 juillet), et rend Perplexity Computer capable de publier un site web à l'adresse `pplx.app` ou via connecteur Vercel.
- Le budget SEO/GEO d'une agence qui travaille pour un plombier américain doit être revu avant la saison publicitaire d'automne : Apple Maps ne sera pas un canal d'acquisition payante pour cette entité.

## Info du jour. Actualité SEO. Apple ferme la porte d'Apple Maps Ads à plusieurs verticales entières avant même le lancement du produit

Pilier de l'édition : **Actualité SEO**, avec une lecture business SEO en corollaire.

**Le fait, daté.** Le 14 juillet 2026, Apple met à jour ses [Apple Advertising Services policies](https://ads.apple.com/). La rubrique consacrée à Apple Maps liste une série de catégories qui ne sont pas autorisées à acheter des annonces à l'intérieur du produit Maps. Le communiqué est repris le 15 juillet par [TechCrunch](https://techcrunch.com/2026/07/15/apple-quietly-reveals-how-its-maps-ads-will-differ-from-googles/), [MacRumors](https://www.macrumors.com/2026/07/15/apple-maps-ad-prohibitied-categories/) et [Cult of Mac](https://www.cultofmac.com/news/apple-maps-ads-ban-home-services-and-more), puis analysé le 17 juillet par [Brooke Osmundson sur Search Engine Journal (SEJ 582542)](https://www.searchenginejournal.com/apple-maps-ads-ban-home-services/582542/) et par [Barry Schwartz sur Search Engine Roundtable (41696)](https://www.seroundtable.com/apple-maps-ads-bans-home-services-41696.html).

**La liste exacte des catégories exclues.** Home services : plomberie, électricité, serrurerie, HVAC, contrôle des nuisibles, couverture, entreprise générale (general contractors). S'ajoutent les services de bail bonds et les criminal pretrial surety bond services, ainsi que les opérateurs de cryptocurrency ATMs. Les services médicaux sont traités « au cas par cas » plutôt qu'automatiquement approuvés. La date d'entrée en vigueur de la politique est le 14 juillet 2026. La date de lancement du produit publicitaire n'est pas fixée précisément : Apple indique « this summer » aux États-Unis et au Canada, sans jour ni semaine.

**La citation Apple. Sur la donnée utilisateur**, la doctrine publiée est courte et sans ambiguïté : *« Ad interactions and location activity will not connect to a user's Apple account. Personal data remains on the device and is not collected, stored, or shared by Apple Ads »* (Apple Advertising Services, cité par SEJ le 17 juillet). Ce paragraphe est le socle politique de tout le reste : Apple construit une couche pub qui refuse de reproduire la logique de matching à l'identité utilisateur telle que Google Local Services Ads la pratique aujourd'hui.

**Ce que la comparaison Google Local Services Ads donne à voir.** Sur Google, les verticales home services passent aujourd'hui par un dispositif de vérification qui inclut enregistrement d'entreprise, contrôle de licence professionnelle, vérification d'assurance et background check. C'est un canal payant significatif pour ces métiers, avec une porte d'entrée qualifiée. Apple choisit de ne pas ouvrir cette porte du tout : la vérification n'est pas remplacée par un autre dispositif, la catégorie est fermée. TechCrunch note que cette décision inverse la logique dominante du search local publicitaire, où la home services est justement le segment le plus rentable pour l'éditeur du moteur.

**Angle SEO/GEO opérationnel.** Pour un consultant SEO qui travaille avec un plombier, un serrurier, un installateur de chauffage ou un couvreur aux États-Unis, plusieurs choses changent dans les prochains mois.

Sur la partie payante, Apple Maps ne sera pas un canal d'acquisition, indépendamment de la qualité de la fiche ou du volume de citations organiques éventuelles. Le budget prévu au titre du search local publicitaire retombe entièrement sur Google Local Services Ads, avec accessoirement Bing Local Ads et la couche Meta.

Sur la partie organique, l'enjeu se déplace : la fiche Apple Maps reste indexable et affichable, mais elle n'a pas de renfort payant possible. La priorité passe donc à la complétude de la fiche Apple Business Connect (nom, catégorie, adresse, téléphone, horaires, photos), à la présence dans les annuaires régionaux qu'Apple utilise pour recouper la véracité de la fiche, et à la cohérence entre la donnée Apple et la donnée Google Business Profile.

Sur la partie AEO/GEO, la question à se poser est différente : Apple Maps n'est pas cité par les surfaces génératives Google (AI Overviews, AI Mode) ni par ChatGPT ou Perplexity dans leurs réponses de recherche locale. Un plombier absent d'Apple Maps ne perd pas de citations dans un moteur de réponse IA aujourd'hui. Le risque à surveiller vit ailleurs : quand un assistant embarqué dans iOS 27 déclenchera une recommandation locale sans passer par la case « ouvre-moi Google Maps », c'est la fiche Apple qui portera la conversion, avec ou sans annonces.

**Ce qui reste incertain.**

1. La date exacte de lancement du produit Apple Maps Ads. Apple ne s'engage que sur « this summer » aux US/Canada. Aucun média n'obtient de calendrier ferme au 19 juillet.
2. Le tarif et le mécanisme d'enchère. Aucun élément public à ce stade sur le CPM, le CPC ou le format d'enchère (mots-clés, catégories, requêtes de proximité).
3. Le volume d'audience qu'un annonceur peut espérer atteindre sur Apple Maps aux États-Unis en 2026. Aucun chiffre public d'utilisateurs mensuels ou de requêtes de recherche locale sur Apple Maps n'est communiqué par Apple.
4. La possibilité pour les catégories exclues de contourner la politique via un service adjacent. Un plombier ne peut pas acheter, mais un site marketplace regroupant plusieurs plombiers pourrait techniquement acheter des annonces sur des requêtes locales génériques. Apple ne s'est pas prononcé sur ce point.

**Lien avec la doctrine du wiki.**

- [[concepts/tabou-visibilite]] : Apple Maps devient une surface de discovery locale qui n'entre dans aucun outil de mesure de « visibilité » globale existant. Ni Semrush ni Ahrefs ni Sistrix ne tracent Apple Maps à date. Une visibilité captée sur cette surface est aujourd'hui invisible aux rapports d'agence habituels. Le refus d'une métrique globale unique se confirme, et l'obligation de piloter surface par surface se confirme aussi.
- [[concepts/metriques-visibilite-geo]] : la grille se doit d'ajouter deux lignes lisibles côté client. Une ligne « présence organique Apple Maps » (fiche complète, catégorie correcte, photos, horaires), et une ligne « éligibilité publicité Apple Maps » (oui / non selon la politique Apple). Pour les verticales exclues, la seconde ligne est un « non » définitif à date.
- [[concepts/agentic-search]] : la carte des surfaces embarquées dans Siri et l'app Maps devient déterminante. Un agent embarqué iOS qui répond à « find a plumber near me » n'a pas de couche pub à traverser sur Apple Maps ; il traverse la fiche organique. La qualité de la fiche pèse plus fort sur ce parcours.
- [[concepts/e-e-a-t]] : Apple pousse implicitement les verticales exclues à démontrer davantage leur autorité et leur fiabilité par les canaux qu'Apple ne mesure pas directement (avis Google Business Profile, presse locale, agrégateurs de licence pro), pour compenser l'absence de canal pub. C'est un cas concret de report d'E-E-A-T d'un moteur vers ses voisins.

**Prédictions ouvertes ce run.**

- P-2026-07-19-v2-1 : d'ici le 30 septembre 2026, Apple publie ou communique à ses partenaires une date de lancement ferme d'Apple Maps Ads aux États-Unis (semaine précise ou date). Résolution positive : date annoncée publiquement. Résolution négative : silence à cette date.
- P-2026-07-19-v2-2 : d'ici le 31 mars 2027, un éditeur d'outil SEO/GEO de référence (Semrush, Ahrefs, Sistrix, Whitespark, BrightLocal) ajoute Apple Maps comme surface trackée à son offre. Résolution positive : release notes ou blog produit daté. Résolution négative : pas d'ajout au tableau de bord.
- P-2026-07-19-v2-3 : d'ici le 31 décembre 2026, une plainte ou une contestation formelle est déposée par une association professionnelle d'un des verticaux exclus (par exemple National Association of Home Builders, Cryptocurrency ATM operators trade group) contre la politique publicitaire Apple Maps. Résolution positive : dépôt de plainte publique. Résolution négative : silence.

---

## Brèves

### Brève 1. Actualité SEO. Le bouton Validate Fix de Search Console : ce qu'il fait vraiment, selon John Mueller

John Mueller précise dans un article publié le 17 juillet 2026 sur Search Engine Journal ([When To Use Search Console's 'Validate Fix,' According To Google, SEJ 582791](https://www.searchenginejournal.com/when-to-use-search-consoles-validate-fix-according-to-google/582791/)) ce que fait exactement le bouton Validate Fix quand un site owner clique dessus après avoir corrigé un problème d'indexation ou de couverture.

Le mécanisme est le suivant. Le bouton n'accélère pas le recrawl en soi. Il attache un suivi à un échantillon des URL affectées par le type d'erreur signalé, puis relance Google sur cet échantillon pour vérifier que la correction est effective. Si l'échantillon passe le test, Search Console notifie que le lot est validé. La validation est liée à un type d'erreur entier, pas à une URL isolée : cliquer Validate Fix suppose que toutes les instances du problème sont corrigées, sinon la vérification échouera. Google précise que ne pas cliquer sur le bouton n'empêche pas Google de détecter la correction lors de son crawl régulier.

**Angle SEO.** Le bouton est utile après une correction complète, pas URL par URL. L'usage optimal est de laisser passer un délai de propagation de la correction (par exemple 48 à 72 heures après un déploiement) avant de lancer la validation, pour éviter que l'échantillon tombe sur des pages encore en cache erroné. Le rapport SEJ ne fournit pas de chiffre sur la durée moyenne de validation ; sur ce point, la doctrine reste qu'un crawl régulier fait le travail sans intervention. Le bouton reste utile essentiellement pour marquer une date de reprise de suivi côté agence.

### Brève 2. Recherche agentique. Perplexity Brain passe en entreprise et Perplexity Computer peut publier un site

Perplexity a annoncé le 13 juillet 2026 une série de mises à jour de Computer, son produit agent. Les release notes de [releasebot.io/updates/perplexity-ai](https://releasebot.io/updates/perplexity-ai) datent la publication au 13 juillet. Perplexity elle-même documente la mémoire agentique Brain sur son blog produit ([Self-improving Memory for Agents](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents)) et la couverture initiale par [MarkTechPost du 18 juin 2026](https://www.marktechpost.com/2026/06/18/perplexity-launches-brain/) situe le premier accès en preview côté Max.

Ce qui change au 13 juillet. Brain (mémoire auto-améliorante, qui construit un graphe de contexte privé à partir des sessions, connecteurs, fichiers et décisions passées, puis se re-entraîne pendant la nuit) devient disponible aux clients Enterprise. Les tests internes de Perplexity indiquent une amélioration de 25 pct de la justesse des réponses et de 16 pct du recall, à un coût réduit de 13 pct sur les tâches à contexte antérieur. Le mode orchestration Opus 4.8 Fast Mode arrive pour accélérer les workflows complexes sans dégrader la qualité. Un orchestrateur Claude Fable 5 est ajouté pour la recherche profonde et la synthèse multi-sources. Le switch de modèle en cours de tâche (mid-task model switching) autorise à changer d'orchestrateur entre deux tours d'un même workflow sans redémarrer. Computer peut publier un site web à une adresse `pplx.app` ou via connecteur Vercel, avec des permissions granulaires public / privé.

**Angle GEO / agent.** La mémoire agentique persistante change la lecture des consommations. Un agent qui apprend d'une tâche à l'autre chez le même client convient mieux à une prestation d'audit continu qu'à un audit ponctuel. Pour un consultant SEO/GEO, la conséquence est double. Côté offre : un audit Perplexity Computer d'une propriété client s'exécute désormais plus vite et moins cher si le graphe de contexte a déjà été alimenté. Côté mesure : la capacité de Computer à publier un site à `pplx.app` ouvre un nouveau surface d'observation. Un site publié via Perplexity peut hériter d'un référencement organique via l'index Bing (Perplexity interroge Bing sur les requêtes commerciales) sans passer par un hébergement classique. À suivre : un vrai chiffre d'usage post-généralisation Enterprise, non publié à ce stade.

### Brève 3. GEO. Le rapport Generative AI de Search Console continue son extension, sans métrique de clic

Google Search Console rend le rapport « Generative AI features » accessible à un nombre croissant de sites depuis son lancement en bêta le 3 juin 2026, avec une extension notable autour du 9 juillet 2026 documentée par [Search Engine Roundtable (41549)](https://www.seroundtable.com/google-ai-performance-report-expands-41549.html). L'annonce initiale est [documentée par Google Search Central](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) et le rapport est décrit sur [Search Engine Land (article 457076)](https://searchengineland.com/google-ai-mode-traffic-data-search-console-457076).

Le rapport publie des impressions pour deux surfaces : AI Overviews et AI Mode, plus une vue Discover séparée. Il fournit un découpage par pages, pays, appareils (Search only), et dates (hourly, daily, weekly, monthly). Il ne fournit pas de clicks, pas de CTR, pas de position moyenne, et pas de queries au niveau de la ligne. Google précise que les impressions AI étaient déjà comptabilisées dans le rapport Performance général : il ne s'agit pas d'un nouveau canal de mesure, mais d'une découpe séparée du même canal.

**Angle GEO.** Le rapport reste, à ce stade, plus utile pour compter l'exposition que pour piloter la conversion. Un opérateur qui gère une agence GEO doit continuer de coupler cette donnée impressions Google à une mesure externe (Profound, Peec AI, Semrush AI Visibility Index, Ahrefs Brand Radar) pour obtenir la part de citations et la ventilation par surface, données que Google ne publie pas. Le rapport Generative AI de GSC devient une brique nécessaire mais pas suffisante d'un tableau de bord AI Search, pas un remplaçant des outils tiers de mesure GEO. Rappel de doctrine : les impressions AI sans les clicks ne se lisent pas seules. Elles ne comptent qu'en écart par rapport aux impressions organiques hors AI, sur la même requête ou le même cluster.

---

Draft SyntheticBrain. Rien n'a été envoyé.
