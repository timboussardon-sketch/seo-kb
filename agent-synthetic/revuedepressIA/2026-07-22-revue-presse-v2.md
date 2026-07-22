# Le rapport AI Mode de Google arrive à moitié rempli, sans clics ni CTR

**Édition du 22 juillet 2026 (v2) — SyntheticBrain**

## En bref

- Google déploie en pilote US un rapport AI performance insights dans Merchant Center depuis le 13 juillet 2026, avec queries groupées et share of voice, mais sans requêtes individuelles, sans clics, sans CTR.
- Le régulateur UK CMA exige que Google fournisse clics, CTR et séparation AI vs organique dans Search Console, avec une fenêtre de mise en œuvre de neuf mois qui court jusqu'à début 2027.
- Anthropic lance **Record a Skill** pour Claude Pro/Max/Team le 21 juillet : l'agent apprend un workflow depuis une capture d'écran narrée, dans la même logique que OpenAI Record and Replay sorti en juin.
- Kelsey Jones publie sur Search Engine Land le 22 juillet un rappel documenté : QuickBooks a supprimé plus de 2 000 pages et gagné **20 %** de trafic et **70 %** de leads ; Userpilot a supprimé **25 %** de son contenu et sorti son plus haut mois de trafic.
- Un juge fédéral américain a rejeté les claims DMCA anti-circumvention de Google contre SerpApi, retirant à Google un levier juridique sur le scraping de SERPs sans copyrighté.

---

## Info du jour — pilier Actualité SEO / mesure

### Le rapport AI performance insights de Google s'ouvre en pilote US et rend les métriques les plus attendues encore invisibles

Matt G. Southern documente dans [Search Engine Journal](https://www.searchenginejournal.com/googles-ai-search-data-is-growing-but-the-gaps-remain/582558/) le 21 juillet 2026 l'état exact des données AI que Google fournit aux marchands et aux référenceurs. Le fait neuf : depuis le 13 juillet, un nouvel onglet **AI performance insights** est apparu dans Merchant Center pour un sous-ensemble de comptes US, sous *Analytics > Products > AI performance tab*. La documentation officielle vit sur [Google Merchant Center Help](https://support.google.com/merchants/answer/17200695). Le pilote a été repéré par Hana Kobzova (PPC News Feed) puis relayé par [Search Engine Roundtable](https://www.seroundtable.com/google-merchant-center-ai-performance-insights-41675.html) le 14 juillet.

**Ce que le rapport contient.** Cinq dimensions accessibles pour l'instant :
- Type de requête, catégorisé en specs produit, avis, recherches catégorielles.
- Fréquence de requête, en indicateur de popularité relative.
- Phase du parcours d'achat, classification cliente par étape.
- Termes produit, vocabulaire employé par les acheteurs.
- Share of voice, impressions marque divisées par impressions concurrents.

**Ce que le rapport n'a pas.** Southern liste les manques les plus critiques pour l'audit. Aucun accès aux requêtes individuelles. Aucune donnée de clic. Aucun CTR. Le share of voice ignore le trafic payant. Une seule catégorie produit par filtre. La compétition est définie par les comptes déjà présents dans Merchant Center, ce qui exclut de facto une partie du marché. Un compte sans impressions suffisantes ni concurrents ne verra rien s'afficher.

**Périmètre du pilote.** US uniquement, trafic AI organique uniquement, requêtes conversationnelles ou d'intention marque uniquement, sites affiliés / avis / éditoriaux exclus. Expansion prévue vers Australie, Canada, Inde, Nouvelle-Zélande dans les mois suivants.

**Le contexte régulatoire.** Southern rappelle que le régulateur britannique **CMA** a imposé le mois dernier à Google une fenêtre de neuf mois pour publier dans Search Console des impressions, clics, CTR et séparation AI vs organique. La fenêtre de neuf mois pointe vers début 2027. Les notes d'interprétation du régulateur ([gov.uk](https://www.gov.uk/government/news/cma-secures-fairer-deal-for-publishers-and-improves-google-search-services-in-uk)) précisent explicitement les clics, le CTR et la donnée séparée. Ces éléments ne sont pas dans les rapports actuels.

**La voix de Brodie Clark.** Le consultant SEO indépendant a eu accès au pilote via un sous-compte client, et publie sur [X](https://x.com/brodieseo/status/2077027856345874894) des captures du dashboard actif. Il qualifie le rapport de premier produit Google à fournir de la donnée de requête pour ces surfaces, tout en formulant la limite d'usage : *« In its current form, similar to the recent rollout of AI reporting in Search Console, there isn't a great deal of actionability behind the data »*. Southern relaie aussi l'analyse de Slobodan Manic sur la stratégie de filtre Search Console en juin, et la clarification de John Mueller sur le comptage des impressions dans les fonctions AI.

**Trois limites documentaires à publier avec le chiffre.**
1. Le pilote est réservé à un panel US restreint aux marchands qualifiés. Aucune vérification indépendante à grande échelle n'est possible aujourd'hui.
2. Google a également refusé, en juillet 2026, aux vendeurs d'outils GEO tiers l'accès aux métriques internes ; le rapport ne peut donc pas être recoupé par une source de mesure indépendante.
3. La CMA a défini son horizon en neuf mois, pas en obligation immédiate. La fenêtre reste ouverte pour que Google publie ces données a minima au Royaume-Uni avant début 2027, sans que la conformité soit encore vérifiée.

**Ce que ça change pour un audit GEO client.** Trois signaux mesurables reprécisés :
- **Écart impression-clic sur AI Mode.** Le rapport confirme que Google mesure et déclare les impressions AI, mais pas encore les clics. Un consultant doit tenir un registre d'impressions IA depuis Search Console et Merchant Center, et un registre de clics estimé par proxy (referral traffic AI dans Analytics 4, filtré par User-Agent ou paramètre UTM) séparé jusqu'à ce que Google publie la donnée en clair.
- **Share of voice sans paid.** Pour un compte qui achète des ads sur les mêmes queries, l'écart entre share of voice Merchant Center et share of voice global peut être significatif. Il faut le noter comme biais méthodologique dans le reporting, pas comme une mesure de position marché.
- **Absence de la donnée query individuelle.** Le rapport groupe les questions par thème. Le consultant qui veut optimiser au niveau de la requête doit toujours passer par les outils tiers (Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Profound, SE Ranking) et documenter dans le rapport la source utilisée.

**Articulation avec la doctrine.** Ce déploiement recoupe précisément [[concepts/metriques-visibilite-geo]] sur trois dimensions : Google mesure l'apparition (`Imp_wc`), pas la densité, pas la position (`Imp_pos`), et pas encore la clickabilité. Il illustre [[concepts/requete-cliquable-vs-clic]] : Google a construit un rapport de reconnaissance sans les clics, ce qui rend le KPI aveugle à la conversion. Il valide la règle stricte de [[concepts/tabou-visibilite]] : une part d'impressions AI n'est pas une part de leads. Il complète [[concepts/agentic-search]] par le fait que la phase de parcours d'achat est mesurée mais que le trafic généré ne l'est pas.

**Ce que le rapport ne dit pas.** Rien sur le taux de conversion, rien sur le canal AI Overviews vs AI Mode séparément, rien sur la latence entre impression et achat. C'est un rapport d'exposition de catalogue, pas un rapport de performance business.

---

## Brèves

### B1 — Recherche agentique — Anthropic ouvre Record a Skill pour Claude Pro, Max et Team

Roger Montti publie dans [Search Engine Journal](https://www.searchenginejournal.com/anthropics-claude-can-now-watch-a-video-and-learn-your-job/583053/) le 21 juillet 2026 la description de **Record a Skill**, apparu dans le menu de l'application desktop de Claude. Verbatim Anthropic : *« Record your screen while you do a task, talk through it as you go, and Claude turns it into a skill it can run again »*. L'utilisateur enregistre son écran en narrant l'action, Claude convertit la séquence en skill exécutable de manière autonome. La fonction est réservée aux paliers Pro, Max et Team, sur desktop uniquement.

OpenAI a introduit une capacité comparable, **Record and Replay**, en juin, réservée à macOS et indisponible dans l'Espace Économique Européen, en Suisse et au Royaume-Uni. Anthropic n'a pas publié de restrictions géographiques équivalentes à date, ce qu'il faut vérifier avant tout usage client hors US.

Pour un consultant SEO/GEO, ce qui compte : la fenêtre de captation des workflows utilisateurs par un agent LLM s'élargit. Un agent qui a appris un flux d'achat sur un site tiers reproduit ce flux sans passer par l'interface de recherche. Cela renforce l'analyse déjà documentée dans [[concepts/agentic-search]] : la page produit doit rester lisible pour un agent qui l'a vue une fois, et ne pas dépendre d'un état de session fragile.

### B2 — Actualité SEO — Kelsey Jones documente à nouveau les gains de trafic après suppression de contenu

Kelsey Jones publie sur [Search Engine Land](https://searchengineland.com/publish-less-content-data-482891) le 22 juillet 2026 un dossier qui reprend les cas les plus cités et les met à jour dans le contexte de la crise d'indexation observée en 2026. Elle rappelle deux résultats concrets : QuickBooks a supprimé plus de **2 000** pages de contenu et vu son trafic augmenter de **20 %** en quelques semaines, avec **70 %** de leads supplémentaires. Userpilot a supprimé près de **25 %** de son catalogue et publié son plus haut mois de trafic à date.

Le cadre analytique est stable : loi des rendements décroissants, saturation du crawl budget, hausse du bucket *Discovered — currently not indexed* dans Search Console. Google a défini le crawl budget dans sa documentation officielle comme *« The amount of time and resources that Google devotes to crawling a site »*. Marie Haynes avait déjà documenté en juillet 2026 (rappelé dans notre édition du 21 juillet) que la part de pages coincées en *crawled — currently not indexed* progresse à mesure que le contenu générique se multiplie.

La limite de l'article : les études de cas sont historiques, aucun chiffre 2026 propre n'est publié. Utile en synthèse, pas en preuve de tendance neuve. Pour un consultant, la lecture opérationnelle reste la même : audit trimestriel avec Screaming Frog, catégorisation *keep / consolidate / refresh / delete*, fenêtre d'observation trois à six mois avant conclusion. Le lien doctrine ici est [[concepts/fraicheur-contenu]] pour la partie *refresh*, et [[concepts/test-substitution-llm]] pour la partie *delete* : une page substituable par la réponse générative sans perte d'information n'a pas de raison de rester crawlée.

### B3 — Business SEO — Un juge fédéral rejette les claims DMCA anti-circumvention de Google contre SerpApi

Matt G. Southern publie dans [Search Engine Journal](https://www.searchenginejournal.com/court-dismisses-googles-dmca-claims-against-serpapi/583033/) le 21 juillet 2026 la décision de la juge en chef Yvonne Gonzalez Rogers du District Court US. Le tribunal a rejeté les claims DMCA anti-circumvention formulés par Google contre SerpApi. La décision : les claims sur les résultats sans contenu copyrighté sont rejetés **sans autorisation d'amendement**, ce qui les ferme effectivement. Les claims liés aux images Knowledge Panel sous licence sont rejetés **avec autorisation d'amendement**, Google disposant de 21 jours pour reformuler.

Le dossier est consultable via CourtListener docket 72059948. Google avait déposé sa plainte en décembre, SerpApi ayant déposé sa motion to dismiss en février. Julien Khaleghy, CEO de SerpApi, publie sur le blog SerpApi la réaction officielle : *« We're pleased that the court rejected Google's attempts to expand the DMCA to assert control over access to public pages »*.

Pour l'écosystème des outils SEO, la portée est double. D'abord, elle réduit le risque DMCA sur le scraping de résultats de recherche publics, ce qui sécurise les infrastructures de reporting rang que consomment la plupart des vendeurs (Semrush, Ahrefs, SE Ranking, DataForSEO). Ensuite, elle laisse ouverte la porte Knowledge Panel : la portion des SERPs qui embarque des visuels sous licence reste juridiquement fragile, et Google a 21 jours pour amender ce volet précis. Un consultant qui construit un outil de mesure interne pour un client doit continuer à isoler la partie visuelle Knowledge Panel de la partie résultat textuel, et ne pas mélanger les deux dans un dataset unique.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
