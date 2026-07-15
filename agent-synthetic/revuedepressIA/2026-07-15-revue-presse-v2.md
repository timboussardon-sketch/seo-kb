# Algorithme, édition du 15 juillet 2026 (v2)

**Les agents IA se cassent sur la page tarifs des sites B2B, 1 500 essais mesurés**

## Résumé en 5 points

- Étude Kevin Indig et David Kaufman (Siteline), publiée sur Growth Memo le 13 juillet 2026 et reprise par Search Engine Land le 15 juillet 2026 : 100 produits B2B testés sur 3 tâches acheteur (tarifs et fonctions, intégrations, sécurité et conformité), 5 exécutions chacune, 1 500 essais au total avec agents sans URL de départ.
- Tarifs et fonctions atteignent 79 pct de réponses première-partie et 84 pct de citations première-partie, contre 92 à 93 pct pour la sécurité et 93 pct pour les intégrations : le tarif est le seul point de rupture systématique du site B2B face à un agent.
- Trois modes d'échec chiffrés : opacité tarifaire (45 pct de citations tierces quand le prix n'est pas publié, 55 pct restent première-partie sur du « contact sales »), non-lisibilité machine (prix en JavaScript, calculateurs, tableaux ambigus, 18 pct de citations tierces même avec un prix affiché), friction d'accès (blocage crawlers, présente sur 7 pct des essais mais qui fait passer la citation tierce de 17 à 77 pct sur les tarifs).
- Les 580 citations tierces recensées se répartissent en 52 pct sources éditoriales (blogs, guides), 46 pct annuaires (G2, Capterra, Vendr, Tekpon), 2 pct pages écosystème.
- Trois brèves : Google introduit la génération d'images IA dans AI Overviews avec Nano Banana (14 juillet), étude Fractl et SparkToro sur les publications de niche à forte affinité audience (358 placements, 1,7x supérieurs aux médias grand public), projection eMarketer plafonnant le marché US des chatbots publicitaires à 5,41 Md$ en 2030 face à l'objectif OpenAI de 100 Md$.

## Info du jour . Pilier Product-Led SEO

**Là où les agents IA calent sur les sites B2B, c'est le tarif.**

Kevin Indig et David Kaufman (fondateur de [Siteline](https://siteline.ai/blog/ai-agent-software-benchmark/)) ont publié le 13 juillet 2026 sur [Growth Memo](https://www.growth-memo.com/p/where-ai-agents-get-stuck-on-your) un test empirique de la lisibilité des sites B2B par les agents IA. Search Engine Land a repris l'étude le 15 juillet 2026 (Kevin Indig, republication éditoriale à 11h ET). [AIVO Journal](https://www.aivojournal.org/the-price-is-not-right/) publie une couverture indépendante le même jour.

**Protocole.** 100 produits logiciels B2B, 3 tâches acheteur par produit (tarifs et fonctions, intégrations, sécurité et conformité), 5 exécutions par tâche pour absorber la variabilité probabiliste des LLM. Les agents ne reçoivent pas d'URL de départ : ils doivent trouver le site officiel eux-mêmes. Soit 1 500 essais au total.

**Résultat central.** L'écart entre la tâche « tarifs et fonctions » et les deux autres est net et mesuré.

| Tâche | Réponse première-partie | Citation première-partie |
| --- | --- | --- |
| Tarifs et fonctions | 79 pct | 84 pct |
| Intégrations | 93 pct | 99 pct |
| Sécurité et conformité | 92 pct | 99 pct |

Autrement dit, un agent qui vient chercher les tarifs cite une source extérieure au vendeur dans 16 pct des cas, contre 1 pct pour les intégrations. Le tarif à lui seul concentre 77 pct de toutes les citations tierces observées dans l'étude.

**Trois modes d'échec distincts.** Growth Memo décompose la rupture en trois causes chiffrées.

Opacité tarifaire : quand le vendeur ne publie pas de prix, 45 pct des essais partent chercher un tiers. Les 55 pct restants restent première-partie sur du « contact sales », c'est-à-dire une réponse qui ne renseigne pas le prix. Même sur un site qui affiche un prix numérique lisible, 18 pct des essais citent quand même un tiers.

Non-lisibilité machine : prix rendu uniquement en JavaScript, prix dans un calculateur interactif, tableau ambigu, capture d'écran, PDF. Le site montre le prix à un humain mais l'agent ne parvient pas à extraire une valeur exploitable. Growth Memo rappelle un point technique : les agents Anthropic et OpenAI n'exécutent pas le JavaScript, contrairement à Google.

Friction d'accès : erreur de fetch, rate limit, blocage explicite. Cette friction n'apparaît que sur 7 pct des essais toutes tâches confondues, mais elle a un effet démesuré sur les tarifs. Sur les essais tarifs sans erreur d'accès, la citation tierce reste autour de 17 pct. Sur ceux avec erreur d'accès, elle passe à 77 pct.

**Qui prend la place du vendeur.** 580 citations tierces recensées, réparties comme suit : 52 pct sources éditoriales (blogs, guides, articles), 46 pct annuaires (G2, Capterra, Vendr, Tekpon), 2 pct écosystème (app stores, pages partenaires). Ce sont les annuaires spécialisés qui absorbent la moitié du trafic d'agents qu'un site B2B laisse échapper sur ses propres tarifs.

**Une recommandation avec mesure d'effet.** Ajouter un balisage `schema.org Product` et `Offer` avec prix et devise sur la page tarifs fait passer un score interne de préparation agent de 73 à 93 points sur l'échantillon Growth Memo. C'est la seule intervention testée par l'étude qui produit un delta mesuré, et elle valide côté terrain la thèse de [[concepts/structural-information-geo]] : le balisage structurel domine la lecture par les agents, pas le body text.

**Ce que cela change pour le SEO B2B.** L'étude opère un déplacement de l'objet à optimiser. On ne parle plus d'apparaître dans un top 10 générique, on parle de rester la source première quand un agent vient répondre à une intention transactionnelle nommée (« combien coûte tel outil »). Trois articulations doctrinales tiennent.

D'abord [[concepts/product-led-seo]]. La page tarifs est la page produit par excellence pour l'agent : elle contient un fait vérifiable (le prix) qu'aucune reformulation LLM ne peut inventer sans risque. Rendre cette page lisible machine, c'est la conserver comme unité d'analyse pour l'agent, au lieu de la voir remplacée par une reprise éditoriale ou un annuaire.

Ensuite [[concepts/agentic-search]]. L'objectif de sélection par l'agent se joue à un endroit précis et opérationnel : la page tarifs. C'est là que Growth Memo mesure une variance de 60 points entre les vendeurs les mieux préparés et les moins préparés.

Enfin [[concepts/data-proprietaire]] et [[concepts/tabou-visibilite]]. Quand un annuaire cite votre prix à la place de votre site, votre donnée tarifaire n'appartient plus à votre canal. La métrique opérationnelle à suivre n'est pas la « visibilité » du vendeur dans les réponses IA, c'est le taux de citation première-partie sur ses propres pages tarifs et fonctions. Cette dimension complète [[concepts/metriques-visibilite-geo]] avec une 8e mesure : le taux de citation première-partie par tâche acheteur, décliné par catégorie (tarifs, intégrations, sécurité).

**Trois limites documentaires.**

1. L'étude porte sur des produits logiciels B2B. Rien ne dit que le motif se reproduit sur des sites e-commerce grand public, où le prix est presque toujours publié en HTML statique, ni sur des sites de service à devis (agence, cabinet), où le prix n'existe pas comme entité fixe.
2. Growth Memo et Siteline sont partie prenante d'un outil vendu (« AI agent readiness tool » proposé par Siteline). La démonstration est légitime mais la barre de reproduction externe reste à passer par un tiers non-vendeur.
3. La table des vendeurs testés n'est pas publiée en intégralité (10 exemples cités dans l'article, 90 non listés). Reproduire le protocole demandera l'accès à la liste complète des 100 produits.

**Prédictions.**

- P-2026-07-15-v2-1 : d'ici le 31 mars 2027, un vendor de mesure de visibilité IA (Ahrefs, Semrush, Profound, Previsible, CiteLens, Kasper, mybrandi) ajoute au tableau de bord une colonne dédiée au taux de citation première-partie par catégorie de tâche acheteur (tarifs, fonctions, intégrations, sécurité). Résolution positive : billet blog ou changelog produit nommant la métrique. Résolution négative : aucun vendor n'a exposé cette dimension d'ici fin mars 2027.
- P-2026-07-15-v2-2 : d'ici le 31 décembre 2026, un annuaire B2B parmi G2, Capterra, Vendr, Tekpon publie un rapport interne mesurant sa part de citations agent sur les requêtes tarifaires par catégorie de produit. Résolution positive : rapport publié avec pourcentages et méthodologie. Résolution négative : silence prolongé.

## Brèves

### B1 . Actualité SEO . Google introduit la génération d'images IA dans AI Overviews (Nano Banana)

Le 14 juillet 2026, Google a annoncé l'intégration de la génération d'images IA dans les AI Overviews, ainsi qu'une refonte de la page d'accueil de Google Images pour ses 25 ans. Sources primaire et reprises : [Search Engine Land, Barry Schwartz](https://searchengineland.com/google-ai-overviews-now-lets-you-create-image-482163), [Search Engine Journal, Matt Southern](https://www.searchenginejournal.com/google-adds-image-generation-to-ai-overviews-revamps-images/582242/), [Android Authority](https://www.androidauthority.com/google-images-celebrates-25-years-with-new-ai-upgrades-3687349/).

Fait : depuis un prompt texte, l'utilisateur obtient une image générée directement dans l'AI Overview, sans quitter la page de résultats. Le modèle utilisé est Nano Banana, système Google déployé progressivement dans Search et Chrome depuis le début d'année. Le déploiement s'étale « sur les prochaines semaines » en anglais, sur les régions qui supportent déjà la création d'images dans AI Mode. La page d'accueil de Google Images ajoute une galerie navigable avec mise à jour en temps réel, plus des onglets de collections personnalisées pour les utilisateurs connectés (déploiement desktop, US, anglais d'abord).

Ce que cela change côté SEO : les sites de stock d'images (banques d'images gratuites et payantes) perdent une part de la requête image « visualise moi un salon de style nautique », qui reçoit désormais une image générée à la volée dans le résultat même. Search Engine Journal note explicitement que l'intégration renforce le pattern « réponse complète sur la page de résultats sans besoin de clic ». Pas de mécanisme d'attribution ni de citation communiqué pour les images générées, contrairement aux réponses textuelles d'AI Overviews. Fiche doctrine adjacente : [[concepts/agentic-search]] et le déplacement continu de l'unité citée du domaine vers le fragment produit sur place.

### B2 . Niche SEO . Étude Fractl et SparkToro : les publications de niche à forte affinité battent les grands médias sur l'audience professionnelle

Fractl a publié le 18 juin 2026 avec SparkToro l'étude « Hidden PR Goldmine » (Kelsey Libert et Aditya Sachdeva), reprise et commentée sur Search Engine Land le 14 juillet 2026. Sources : [SparkToro, billet primaire de synthèse](https://sparktoro.com/blog/audience-affinity-vs-traffic-why-high-affinity-media-belongs-in-your-earned-media-strategy/), [PPC.land](https://ppc.land/the-high-traffic-trap-fractl-data-shows-smbs-are-pitching-the-wrong-media/), [Contentgrip](https://www.contentgrip.com/audience-affinity-earned-media/).

Fait chiffré : 358 placements médias (sites web, chaînes YouTube, podcasts, subreddits) mesurés sur 8 industries, notés par un score d'affinité audience calculé sur les cohortes SparkToro de décideurs professionnels. Les publications de niche affichent une affinité audience 1,7x supérieure aux grands médias, malgré un écart de trafic pouvant atteindre 130x. Exemples cités : RecruitingDaily.com (10 K visiteurs mensuels, score d'affinité SaaS 93) rivalise avec GetApp.com (418 K visiteurs, score 90). InsureTechInsights.com (8 K visiteurs, score 80) domine Investopedia.com (834 K visiteurs, score 19) sur la verticale assurance. Fractl définit la fourchette « hidden gem » comme 5 K à 10 K visiteurs mensuels et un domain rating mid-60 à low-70.

Ce que cela change côté GEO : les études précédentes sur les citations d'AI Overviews privilégient les grands médias par domain authority. L'étude Fractl inverse la lecture côté cohorte lecteur (décideur B2B nommé) et suggère qu'un placement sur un site niche à 5 000 visiteurs peut valoir plus qu'une reprise sur un média à 500 000 visiteurs, sur ces cohortes précises. Fiche doctrine adjacente : [[concepts/data-proprietaire]] (un placement niche à forte densité de décideurs vaut mieux qu'une reprise diluée) et angle « niche SEO » du périmètre qui n'avait pas été tenu comme brève depuis plusieurs éditions.

### B3 . Business SEO . eMarketer plafonne le marché US des publicités chatbot à 5,41 Md$ en 2030

Le 14 juillet 2026, Search Engine Land relaie une projection eMarketer qui contredit frontalement la cible interne d'OpenAI. Sources : [PPC.land](https://ppc.land/emarketer-says-us-ai-ad-spend-hits-68bn-by-2030-and-chatgpt-misses-most-of-it/), [Search Engine Land, Danny Goodwin](https://searchengineland.com/openai-chatgpt-ads-100-billion-revenue-target-482365), [AdWeek](https://www.adweek.com/media/openais-ad-business-is-on-pace-to-miss-its-own-forecast-by-90-analyst-says/).

Fait chiffré : eMarketer projette 5,41 Md$ pour l'ensemble du marché US des publicités sur chatbots autonomes en 2030. OpenAI a communiqué en interne un objectif de 2,5 Md$ de revenus publicitaires en 2026 et de 100 Md$ en 2030. Écart entre la cible OpenAI 2030 et la projection eMarketer 2030 : un facteur 18, soit 94 pct sous la cible interne. La projection eMarketer 2026 se situe sous 1 Md$, soit 90 pct sous les 2,5 Md$ d'OpenAI. Cause avancée par l'analyste : la densité publicitaire d'un chatbot ne peut pas atteindre celle d'un moteur de recherche classique. Pour tenir la projection eMarketer, chaque réponse commerciale devrait déjà comporter un placement payant. Le CPM initial du pilote ChatGPT Ads (60 $) est projeté par eMarketer à environ 15 $ en 2030.

Ce que cela change côté Business SEO : la projection eMarketer pose une limite empirique à la thèse « les chatbots vont capter la valeur publicitaire du search ». Deux implications opérationnelles. Un, l'arbitrage entre optimiser pour AI Overviews (moteur Google, densité publicitaire supportée) et pour ChatGPT (chatbot autonome, densité publicitaire projetée basse) ne se joue pas symétriquement côté monétisation. Deux, si eMarketer a raison, la couche gratuite d'AI Answers reste dominée par la citation organique, pas par la publicité payante, ce qui renforce la valeur de la citation première-partie mesurée par l'étude info du jour. Fiche doctrine adjacente : [[concepts/tabou-visibilite]] (mesurer la conversion et le lead, pas la « visibilité »).

---

*Draft SyntheticBrain. Rien n'a été envoyé. Trois sources indépendantes par claim principal, verdict au niveau du claim, prédictions datées.*
