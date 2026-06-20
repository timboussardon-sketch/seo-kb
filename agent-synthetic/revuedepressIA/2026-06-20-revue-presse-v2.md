---
date: 2026-06-20
edition: 2026-06-20-v2
agent: SyntheticBrain
pilier_info_jour: GEO
contexte: cloud
capture_mode: native
---

# Algorithme — édition du 20 juin 2026 (v2)

> Confiance dans la recherche IA : 54 pct des consommateurs américains la jugent plus utile que la recherche classique, contre 82 pct il y a un an. Et 70 pct l'utilisent plus.

## En 4 points

- La confiance déclarative dans la recherche IA chute de 28 points en 12 mois (82 → 54 pct), pendant que l'usage progresse (70 pct des consommateurs américains l'utilisent davantage). [Source : étude Fractl × Search Engine Land, 1 008 consommateurs + 150 marketeurs, Q2 2026.]
- 27 pct des marques disent avoir été déformées dans une réponse IA, 14 pct attribuent à cette déformation un impact mesurable sur la relation client ou les ventes. La part des marketeurs qui suivent activement la présence de leur marque dans les LLM passe de 22 à 49 pct sur un an.
- OpenAI ouvre l'Ads Manager ChatGPT en libre-service aux entreprises britanniques le 19 juin 2026, six semaines après l'ouverture US et deux semaines après l'allumage du pilote publicitaire UK côté utilisateurs. Pas de structure multi-comptes type MCC pour le moment.
- Stagwell met en service The Media Machine le 19 juin, un système d'achat média à plus de 20 agents IA branché directement sur Google Marketing Platform, Meta, Microsoft, LinkedIn, TikTok et The Trade Desk. La couche conversationnelle est posée par-dessus l'outillage existant, sans bascule.

## Info du jour — pilier **GEO** : la recherche IA perd 28 points de confiance déclarative en 12 mois pendant que son usage progresse

Le 17 juin 2026, Search Engine Land et Fractl publient une étude conjointe sur 1 008 consommateurs américains adultes et 150 marketeurs interrogés au cours du deuxième trimestre 2026 ([Search Engine Land, Kelsey Libert, 17 juin 2026](https://searchengineland.com/ai-search-adoption-rises-consumer-trust-declines-study-480338) ; [Fractl, AI Statistics 2026](https://www.frac.tl/ai-statistics/) ; [Yext, 7 Data-Backed Stats on AI Search Trust](https://www.yext.com/blog/7-data-backed-facts-on-ai-trust-and-consumer-decision-making-in-2026)). L'échantillon consommateur est représentatif au niveau national pour l'âge, le genre et la région. L'échantillon marketeur va de moins de 10 à plus de 5 000 salariés, et couvre les rôles SEO, contenu, social, analytics, paid media, PR et direction marketing.

Trois mesures structurent le résultat.

La première est un effondrement de la confiance déclarative. À la question « la recherche par IA vous paraît-elle plus utile que la recherche classique ? », 82 pct répondaient oui en 2025. En 2026, 54 pct répondent oui. La part des sceptiques explicites passe de 3 à 17 pct sur la même période. La part de répondants qui disent perdre confiance dans une marque si elle utilise fortement l'IA pour produire son contenu passe de 20 pct (2025) à 40 pct (2026).

La deuxième mesure est paradoxale : 70 pct des consommateurs disent utiliser plus de recherche IA qu'il y a un an. Autrement dit, la confiance déclarative décroche alors que l'usage réel s'accroît. L'étude ne donne pas de mesure d'usage objective tierce, c'est une mesure auto-déclarative à mettre en regard de Cloudflare Radar (trafic bot dépassant trafic humain, mai-juin 2026) et de SparkToro/Datos (68 pct des recherches Google américaines sans clic au premier trimestre 2026). L'étude renforce un motif déjà documenté : l'usage augmente, la confiance déclarative dans la qualité de la réponse diminue.

La troisième mesure concerne directement les marques. 27 pct des organisations interrogées disent avoir été représentées de façon erronée dans une réponse générée par IA. 14 pct attribuent à cette déformation un impact mesurable sur la relation client ou les ventes. La part des marketeurs qui surveillent activement la présence de leur marque dans les LLM passe de 22 pct (2025) à 49 pct (2026), pendant que la part des organisations qui déclarent constamment leur usage de l'IA reste à 20 pct.

Sur la demande de transparence, les chiffres sont nets : 84 pct des consommateurs veulent un label sur les contenus écrits générés ou assistés par IA, 91 pct sur la vidéo, 90 pct sur l'image, 87 pct sur l'audio. Côté marketeur, 53 pct du travail comporte désormais une part d'IA, contre 38 pct en 2025. 50 pct des marketeurs interrogés disent observer une baisse de trafic organique depuis l'apparition d'AI Overviews, 11 pct une hausse, le reste un effet neutre ou indéterminé. Sur la stratégie GEO, 61 pct expriment un degré de confiance, mais seulement 12 pct se déclarent très confiants avec des résultats mesurables.

Lecture doctrine. L'étude touche trois fiches.

Sur [[concepts/metriques-visibilite-geo]], elle ajoute une dimension qui n'était pas mesurée : la confiance déclarative côté consommateur comme variable indépendante de la part de citation côté marque. Une part de citation stable peut s'accompagner d'une chute de la confiance dans la réponse qui contient cette citation, donc d'une chute de la valeur économique de la citation. Le couple part-de-citation × confiance-dans-la-réponse devient une métrique à deux dimensions, pas une seule.

Sur [[concepts/structural-information-geo]], la demande de label par 84 à 91 pct des consommateurs selon le format renforce la lecture que les marqueurs explicites (date, source, auteur, qualification) ont un poids structurel dans la perception de la réponse. La mesure ne dit pas que les marques qui labelisent gagnent en confiance ; elle dit que l'absence de label est explicitement signalée comme une raison de méfiance.

Sur [[concepts/data-proprietaire]] et [[concepts/test-substitution-llm]], le chiffre des 27 pct de marques disant avoir été déformées par une réponse IA est la première mesure publique du risque de représentation erronée, à comparer avec la mesure Lily Ray 18 juin (69 pct des listicles cite la marque mais recommande un concurrent). Les deux mesures décrivent des mécanismes différents : Lily Ray mesure l'écart entre citation et recommandation sur des listicles B2B SaaS auto-promo, Fractl mesure un taux d'erreur factuel auto-déclaré côté marque toutes verticales. Elles ne sont pas substituables, elles documentent deux faces d'un même problème de fiabilité de la couche d'agrégation IA.

Limites à signaler. C'est une enquête déclarative, donc soumise au biais de sélection (qui répond à un sondage marketing) et au biais de mémoire (qui se souvient correctement de son comportement de recherche). L'étude est commanditée par Fractl et publiée par Search Engine Land, deux acteurs avec un intérêt direct au sujet ; ce n'est pas une mesure indépendante d'un cabinet d'études neutre. Les comparaisons année par année reposent sur des panels distincts en 2025 et 2026, pas un suivi longitudinal des mêmes répondants. Le taux d'erreur factuel sur réponses IA est auto-déclaré côté marque, il n'y a pas de validation tierce des incidents listés.

Prédiction. P-2026-06-20-v2-1 : une étude indépendante d'un cabinet d'études neutre (Pew, YouGov, Ipsos, Edelman) reproduira le sens de la mesure consommateur (baisse de confiance déclarative dans la recherche IA en 2026 versus 2025) avec un panel longitudinal sur les mêmes répondants, avant le 31 mars 2027.

## Brèves

### Brève 1 — pilier **Actualité SEO** : OpenAI ouvre l'Ads Manager ChatGPT en libre-service aux entreprises britanniques

Le 19 juin 2026, OpenAI ouvre l'Ads Manager de ChatGPT en bêta libre-service aux entreprises basées au Royaume-Uni ([Search Engine Land, Anu Adegbola, 19 juin 2026](https://searchengineland.com/openai-opens-chatgpt-ads-manager-beta-to-uk-advertisers-480679) ; [PPC Land, Luis Rijo](https://ppc.land/chatgpt-ads-go-live-in-the-uk-as-openai-expands-pilot-beyond-us/)). La rollout passe par un courriel envoyé aux annonceurs. L'interface se découpe en quatre sections : campagnes, outils, facturation, paramètres. La création de compte est ouverte, l'invitation d'un partenaire agence se fait via Settings → Users → Invites.

Trois précisions opérationnelles. Première limite documentée : il n'y a pas de structure multi-comptes type Manager Account (MCC) côté Google Ads. Chaque compte doit être accédé individuellement. Deuxième précision : OpenAI demande explicitement aux agences et aux freelances de ne pas créer le compte à la place du client, mais d'inviter le client à le créer puis à les rattacher en partenaire. Troisième précision : l'ouverture de l'Ads Manager est distincte de l'allumage du pilote publicitaire britannique côté utilisateurs (annoncé le 6 juin 2026 par Benji Shomair, VP Monetization), lui-même distinct de l'annonce d'extension géographique à cinq marchés (UK, Japon, Corée du Sud, Brésil, Mexique) du 7 mai 2026.

Calendrier opérationnel pour les annonceurs SEO/SEA : l'Ads Manager américain est ouvert depuis le 5 mai 2026 et OpenAI revendique 100 M USD de revenu publicitaire annualisé six semaines après l'ouverture US. Les annonces ne servent qu'aux abonnés Free et Go, pas aux Plus, Pro ou Enterprise. La verticale concernée la première année est la recherche produit et la comparaison, pas la conversation longue.

Lecture. Pour un éditeur ou une marque SEO, l'ouverture côté annonceur change le calcul d'arbitrage entre présence organique dans une réponse ChatGPT et présence payante adjacente. Tant que la part d'utilisateurs Free + Go reste très majoritaire sur ChatGPT (proportion non publiée par OpenAI au 20 juin), la couche payante adjacente à la réponse devient une variable nouvelle de la mesure de visibilité, distincte de la part de citation organique mesurée par les outils GEO.

### Brève 2 — pilier **Recherche agentique** : Stagwell met en service un système d'achat média à plus de 20 agents IA branché sur Google Marketing Platform, Meta et The Trade Desk

Le 19 juin 2026, Stagwell (NASDAQ: STGW) met en service The Media Machine ([communiqué Stagwell via PressRelease](https://www.pressrelease.com/news/stagwell-stgw-launches-the-media-machine-full-lifecycle-agentic-media-operating) ; [Stocktitan, STGW Stock News](https://www.stocktitan.net/news/STGW/stagwell-stgw-launches-the-media-machine-full-lifecycle-agentic-4wof5b0zikom.html) ; [Digiday, Media Buying](https://digiday.com/media-buying/stagwell-enhances-its-ai-powered-tools-on-the-media-side/)). Le système est développé par l'agence média GALE en collaboration avec Assembly et Stagwell Media Platform. Il étend une couche agentique précédemment limitée au marketing (« The Machine », lancée plus tôt) à l'ensemble du cycle d'achat média.

Architecture documentée. Plus de 20 agents IA opèrent sur quatre étapes : planification, achat, optimisation, reporting. Le système est branché directement sur les API de Google Marketing Platform, Meta, Microsoft, LinkedIn, TikTok et The Trade Desk. La couche d'identité repose sur un ID graph unifié alimenté côté Stagwell. Les agents s'intègrent dans l'outillage déjà utilisé par les équipes média (Figma, Slack, Teams, Adobe, dashboards de performance), sans bascule de pile.

Quote verbatim de Brad Nunn, Managing Director Media chez GALE : « Built by our media practitioners with deep activation expertise, The Media Machine was designed to solve the fundamental limitations that arise when conversational layers are bolted onto legacy tools » ([communiqué via stocktitan](https://www.stocktitan.net/news/STGW/stagwell-stgw-launches-the-media-machine-full-lifecycle-agentic-4wof5b0zikom.html)). La revendication est que les couches conversationnelles ajoutées par-dessus des outils anciens ne capturent pas la profondeur d'activation nécessaire à un achat média de production.

Lien doctrine. La mise en service de The Media Machine confirme que la couche d'orchestration entre acheteur (marque/holdco) et fournisseur (Google, Meta, TikTok, The Trade Desk) devient agentique côté holdco, en parallèle de l'agentique côté commerce vu chez Adyen le 16 juin ([2026-06-19](2026-06-19-revue-presse.md)) et de la couche découverte agentique vue avec ARD le 17 juin ([2026-06-20](2026-06-20-revue-presse.md)). Trois couches distinctes (découverte, paiement, achat média) basculent en agentique en moins d'un mois, chacune avec son standard concurrent ou ses partenaires d'intégration distincts. Pour [[concepts/agentic-search]], la fiche couvre les deux premières (découverte, paiement) mais pas la troisième (achat média côté holdco), à signaler comme limite explicite.

Prédiction. P-2026-06-20-v2-2 : au moins un autre holdco majeur (Publicis Groupe, WPP, IPG, Omnicom, Havas, Dentsu) annoncera avant le 31 décembre 2026 un système d'achat média agentique connecté à au moins 3 des 6 plateformes intégrées par Stagwell (Google Marketing Platform, Meta, Microsoft, LinkedIn, TikTok, The Trade Desk), avec une revendication d'orchestration end-to-end planification→reporting.

---

*SyntheticBrain — édition close. Aucun envoi.*
