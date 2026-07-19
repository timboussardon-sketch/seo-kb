# Algorithme, édition du 14 juillet 2026 · La citation IA a une durée de vie mesurable, la moitié des mentions disparaît en un jour

*Draft SyntheticBrain, non publié.*

## À retenir

- Deux études indépendantes publiées entre le 25 juin et le 9 juillet 2026 mesurent la durée de vie des citations dans ChatGPT, Google AI Mode, Gemini et Perplexity : 44 à 52 % des sources citées ne réapparaissent jamais après leur première apparition.
- La durabilité d'une citation dépend d'abord du domaine hôte : le contenu propriétaire tient en médiane 41 jours quand un article Forbes tient 10 jours et un fil Reddit 11 jours, selon [Brandi AI](https://mybrandi.ai/ai-citation-strategy/) (15 661 URL sur 60 jours).
- Cette mesure ajoute une dimension aux [[concepts/metriques-visibilite-geo|métriques de visibilité GEO]] déjà formalisées, `Imp_wc` et `Imp_pos`, qui traitent la citation comme un état stable à un instant t sans mesurer sa persistance.
- Brève 1 · Google a ajouté le 13 juillet 2026 dans sa doc de canonicalisation la recommandation d'inclure `rel="canonical"` sur la page canonique elle-même, et a mis à disposition dans Google Ads la prévisualisation des personnalisations texte et de l'extension d'URL finale ([Search Engine Roundtable](https://www.seroundtable.com/google-self-referential-canonical-41669.html)).
- Brève 2 · Sam Richardson publie sur [Search Engine Land](https://searchengineland.com/seo-priorities-ai-shopping-482062) six priorités pour rendre un catalogue produit lisible aux moteurs de recommandation IA, sur la base de Google Merchant Center AI performance insights.
- Brève 3 · Dale Bertrand propose sur [Search Engine Land](https://searchengineland.com/geo-investment-attribution-482108) une méthode pour justifier un investissement GEO sans attribution parfaite, appuyée sur une mesure Loamly qui range 70,6 % du trafic IA en trafic Direct dans GA4.

---

## Info du jour · La durée de vie d'une citation IA devient mesurable

**Pilier : GEO / search IA.** Deux publications indépendantes documentent en juin et juillet 2026 un fait que les tableaux de bord GEO existants ne mesuraient pas : la citation dans une réponse IA n'est pas un état stable, c'est un flux à durée de vie courte, et cette durée dépend du domaine hôte.

**Étude 1. Brandi AI, 9 juillet 2026.** Seth Maloney publie sur [mybrandi.ai](https://mybrandi.ai/ai-citation-strategy/) les résultats d'un suivi de 15 661 URL uniques qui ont cité Brandi AI dans les réponses de moteurs génératifs sur une fenêtre de 60 jours. Résultats principaux :

- 52 % des URL citées ne sont apparues qu'un seul jour puis n'ont plus été observées.
- Le contenu détenu par Brandi AI (`mybrandi.ai`) tient en médiane 41 jours, avec 70 % encore actif à J+60.
- PR Newswire tient 27 jours, avec 56 % encore actif à J+60.
- Les sources académiques tiennent 19 jours, 44 % encore actif à J+60.
- Reddit tient 11 jours, 48 % des URL en one-day.
- Forbes tient 10 jours, 54 % des URL en one-day.

L'auteur associe la durabilité à cinq caractéristiques de contenu : recherche originale, cadres nommés, lancements produits, analyses de tendance, distinctions ou classements.

**Étude 2. Writesonic, 25 juin 2026, présentée par Ethan Crump (Foundation Marketing).** [Foundation Inc.](https://foundationinc.co/lab/vol-298/) publie les données Writesonic de Samanyou Garg sur 23 millions de sources citées suivies d'avril à juin 2026 dans ChatGPT, Gemini, Perplexity et Google AI Overviews. Résultats principaux :

- 44 % des pages citées ont disparu après une seule apparition, sans réapparition dans les réponses suivies.
- La durée de vie médiane des citations qui persistent est de 11 à 15 jours.
- Perplexity retient les sources environ deux fois plus longtemps que ChatGPT.
- ChatGPT affiche la plus forte volatilité de citations parmi les quatre moteurs mesurés.

Verbatim de la synthèse Writesonic : « Citation share is fluid. Citation durability is the asset. »

**Recoupement.** Les deux échantillons sont indépendants (Brandi AI compte 15 661 URL sur son propre corpus de citations entrantes ; Writesonic compte 23 millions de sources sur un corpus multi-marques). Les deux périodes se chevauchent (avril–juin 2026 côté Writesonic, mai–juillet 2026 côté Brandi AI). Les ordres de grandeur convergent : environ la moitié des citations observées à un moment t ne durent pas au-delà d'une observation, et la durée de vie médiane utile se situe en semaines, pas en mois. Une troisième synthèse indépendante ([Authority Tech, « Your AI Citations Expire in 4.5 Weeks »](https://authoritytech.io/curated/ai-citation-half-life-platform-refresh-playbook-2026)) et une quatrième mesure ([Stacker Research, « Most AI Citations Fade in Weeks »](https://stacker.com/blog/source-decay-research-the-stacker-network-effect-on-ai-citation-persistence)) corroborent l'ordre de grandeur de la demi-vie.

**Lecture par rapport à la doctrine.** [[concepts/metriques-visibilite-geo]] formalise trois métriques ancrées dans [[sources/2026-04-13-geo-aggarwal-2024]] : `Imp_wc` (part de phrases citant la source), `Imp_pos` (idem, pondéré par la position dans la réponse), Subjective Impression (jugement LLM sur pertinence, unicité, diversité). Ces trois métriques sont calculées à un instant t. Les études Brandi AI et Writesonic ouvrent une dimension distincte : la persistance temporelle. Si `Imp_wc` d'une source vaut 0,3 aujourd'hui mais que cette source disparaît demain, la lecture opérationnelle change. La citation qui apparaît un jour puis disparaît n'a pas la même valeur commerciale que celle qui tient 40 jours et couvre plusieurs cycles de requêtes successives.

Ce constat conforte [[concepts/data-proprietaire]] par un mécanisme précis : les sources qui portent des chiffres uniques, des cadres nommés, des lancements documentés (donc de la data que seul l'auteur détient) ont une durée de vie deux à quatre fois plus longue selon Brandi AI. Le moat compétitif ne se joue pas seulement sur la probabilité d'être cité, mais sur la durée pendant laquelle la citation tient.

Le vocabulaire respecte [[concepts/tabou-visibilite]] : le mot mesuré ici n'est pas « visibilité » mais durée de vie d'une citation nommée dans une réponse IA, ce qui est vérifiable par l'observation directe des sorties des moteurs.

**Implication opérationnelle.** Deux points concrets pour un audit GEO d'ici la fin du trimestre :

1. Séparer sur le tableau de bord la mesure ponctuelle (citation actuelle) de la mesure de persistance (nombre de jours consécutifs d'apparition sur une même famille de requêtes). Aucun outil couche vendeur (Ahrefs Brand Radar, Semrush AI Visibility Toolkit, Profound, Previsible, CiteLens) n'expose aujourd'hui cette persistance sous forme de colonne dédiée, d'après la revue des pages produit publiques.
2. Prioriser sur la roadmap de contenu ce qui produit une donnée que personne d'autre ne détient (chiffre client mesuré, cadre nommé, étude propre, lancement) plutôt que la reprise d'informations déjà en circulation. Une reprise finit dans Reddit ou Forbes côté distribution, avec une durée de vie médiane sous les deux semaines.

**Limites documentaires.**

- Le corpus Brandi AI est le corpus de citations entrantes de Brandi AI, biaisé côté domaine par la surface du vendeur ; les 41 jours de durée de vie du contenu propriétaire tiennent sur `mybrandi.ai` et non sur un contenu propriétaire moyen d'une marque tierce.
- Le corpus Writesonic n'a pas été publié en méthodologie détaillée (segmentation marque par marque, protocole d'échantillonnage des requêtes, définition d'une citation comptée) au moment de cette édition.
- Aucun des deux corpus ne segmente les résultats par intention de requête (informationnelle, commerciale, transactionnelle), ni par industrie.
- Aucune mesure n'a été publiée à ce jour par un moteur (Google, OpenAI, Anthropic, Perplexity) sur la durée de vie interne d'une citation dans ses propres réponses ; les mesures viennent toutes de tiers.

**Prédictions ouvertes (nouvelles).**

- P-2026-07-14-1 · D'ici le 31 décembre 2026, un fournisseur d'outil de mesure de visibilité IA parmi Ahrefs Brand Radar, Semrush AI Visibility Toolkit, Profound, Previsible, CiteLens ou Evertune ajoute une colonne de durée de vie ou de persistance de citation à son rapport, distincte de la métrique de citation instantanée. Résolution positive : release note ou billet produit nommé. Résolution négative : silence.
- P-2026-07-14-2 · D'ici le 30 juin 2027, une reproduction indépendante du protocole Brandi AI sur un corpus tiers de citations entrantes (marque nommée non-vendeur d'outils GEO) publie une distribution de durée de vie par domaine hôte comparable, avec sensibilité aux intentions de requête. Résolution positive : billet ou papier nommé. Résolution négative : absence de réplication publique.

---

## Brèves

### 1 · Actualité SEO. Google formalise le canonique auto-référentiel et enrichit les prévisualisations d'annonces

**Fait.** Le 13 juillet 2026, Barry Schwartz relève sur [Search Engine Roundtable](https://www.seroundtable.com/google-self-referential-canonical-41669.html) que Google a ajouté à la documentation officielle de canonicalisation la ligne suivante : « Do include a rel="canonical" link on the canonical page itself (also known as a self-referential canonical). » Cette recommandation était présente dans des interventions de John Mueller depuis 2011 mais absente du texte normatif. La mise à jour la fait passer du folklore de forum à la doc primaire.

Le même jour, Google Ads a introduit la prévisualisation des personnalisations texte et de l'extension d'URL finale directement dans la console annonceur, avec en complément un filtrage des prévisualisations par asset, relayé par [Search Engine Land](https://searchengineland.com/) via la couverture du 13 juillet.

**Doctrine.** Deux clarifications procédurales sans changement d'algorithme. La première réduit la marge d'ambiguïté sur le signal canonique dans un contexte où Google indique par ailleurs pouvoir tenir jusqu'à deux semaines une page dans un cluster de doublons ([[sources/2026-07-13-google-canonicalization-2-weeks-hold]], couvert en édition v2 du 13 juillet). La seconde touche la vérification à l'aveugle de campagnes Google Ads mais n'a pas d'impact SEO direct.

**Limites.** La recommandation canonique auto-référentielle n'est pas nouvelle sur le fond ; ce qui est neuf, c'est son inscription dans la doc. Aucun changement de comportement de crawler n'est associé.

**Corroboration.** [Search Engine Roundtable](https://www.seroundtable.com/google-self-referential-canonical-41669.html) primaire, [Search Engine Land, daily recap 13 juillet](https://searchengineland.com/latest-posts) via les articles de la journée.

### 2 · Product-Led SEO. Sam Richardson publie six priorités SEO pour l'AI shopping

**Fait.** Le 13 juillet 2026, [Sam Richardson signe sur Search Engine Land](https://searchengineland.com/seo-priorities-ai-shopping-482062) un article intitulé « 6 SEO priorities for AI shopping ». Il pose la question opérationnelle sous forme d'un verbatim court : « AI can't recommend what it can't understand. » Le cœur du texte est une liste d'exigences appliquées au catalogue produit destinées à rendre la fiche produit lisible pour un moteur de recommandation IA : titres précis, description structurée, attributs machine-lisibles, schéma `Product` et `Offer`, données de compatibilité et de taille, signaux d'avis. L'article cite les rapports Google Merchant Center AI performance insights comme outil de suivi côté opérateur.

**Doctrine.** Le point s'articule directement à [[concepts/product-led-seo]] et à [[concepts/data-proprietaire]]. La lecture Tim de Product-Led SEO au sens strict repose sur un composant embarqué non substituable par un LLM (calculateur, simulateur, configurateur). L'article de Richardson ne traite pas ce cas mais son extension e-commerce : rendre le catalogue produit lui-même l'artefact SEO principal, dont la qualité de structuration devient la variable optimisable. On rejoint la lecture posée dans l'édition v2 du 13 juillet à partir de Rémi Kerhoas sur `agentic-search` : le point d'optimisation stratégique n'est plus la page marketing, c'est le flux de données produit.

Article de « how to » plus que fait franchement neuf. Retenu ici parce qu'il consolide la lecture doctrine dans le pilier Product-Led SEO qui n'a pas été info du jour depuis le 16 juin v2, et parce qu'il ancre la mesure côté outil primaire Google (Merchant Center AI performance insights) plutôt que côté vendeur d'outil.

**Limites.** L'article ne publie pas de mesure comparative de rappel d'agent sur catalogue structuré vs standard. C'est un cadre de bonnes pratiques, pas une expérimentation contrôlée. La mesure de l'effet reste à faire.

**Corroboration.** L'article Richardson est isolé côté fait éditorial du jour, mais son cadre est cohérent avec les priorités énoncées en édition v2 du 13 juillet à partir de [Jason Tabeling (SEL 481923)](https://searchengineland.com/how-google-ucp-native-commerce-affects-your-seo-strategy-481923) sur l'attribut `native_commerce` du UCP et l'exigence de données structurées `Product/Offer/Review` avec inventaire temps réel.

### 3 · GEO. Dale Bertrand propose une méthode pour justifier un investissement GEO sans attribution parfaite

**Fait.** Le 13 juillet 2026, [Dale Bertrand publie sur Search Engine Land](https://searchengineland.com/geo-investment-attribution-482108) un texte qui propose de mesurer l'impact business d'un investissement GEO à partir d'estimations pipeline plutôt que d'attribution session par session. Le cadre s'appuie sur trois éléments.

D'abord une mesure : 70,6 % du trafic généré par des plateformes IA est agrégé dans le canal Direct de GA4 selon [Loamly](https://www.loamly.ai/blog/ai-traffic-attribution-crisis), à partir de 446 405 visites suivies dans leur base. Les visites IA sont ensuite mesurées comme convertissant à 10,21 % contre 2,46 % pour le trafic non IA. Deux corroborations existent sur ce point : [Similarweb](https://ppc.land/your-analytics-are-lying-similarweb-traces-ai-recommendations-to-real-traffic/) sur la sous-attribution, et [Adobe Analytics](https://business.adobe.com/blog/the-latest/adobe-report-shows-shift-to-agentic-ai-shopping) pour la conversion supérieure du trafic IA (couverte en édition 0606 v3 pour Adobe Q1 2026).

Ensuite un cadre nommé, « The Dollar Rule » : si un chiffre ne se traduit pas en dollars, ce n'est pas une métrique business, c'est une métrique de canal.

Enfin une formule : Revenue Influenced = Taux de mention × Interactions annuelles × Valeur de deal × Taux de conversion. Bertrand donne un exemple : un concurrent apparaissant dans 10 % des appels de découverte d'une entreprise de santé, sur 1 200 appels qualifiés annuels, à 500 000 dollars de valeur moyenne de deal, avec 20 % de conversion, donne 12 millions de dollars de pipeline influencé annuellement.

**Doctrine.** Le cadre articule [[concepts/tabou-visibilite]] : substituer un mot ambigu (visibilité) par un chiffre en dollars. Il complète l'info du jour : la mesure ponctuelle de citation ne suffit pas, ni la mesure ponctuelle d'attribution ; le raisonnement bascule sur une lecture pipeline, avec des hypothèses explicites et vérifiables. Cette lecture rejoint le point posé dans l'info du jour sur la durabilité : mieux vaut une citation qui tient 40 jours sur un contenu propriétaire qu'une citation instantanée non traçable.

**Limites.** Le cadre est méthodologique et non empirique : Bertrand ne publie pas de comparaison mesurée entre une équipe qui applique la Dollar Rule et une équipe qui applique l'attribution classique. Le chiffre 70,6 % de Loamly repose sur un unique fournisseur, non répliqué à ce jour sur un panel indépendant. La formule Fuzzy Math postule que le taux de conversion des deals influencés est équivalent au taux de conversion moyen, hypothèse non testée.

**Corroboration.** [Loamly](https://www.loamly.ai/blog/ai-traffic-attribution-crisis) primaire vendeur pour le 70,6 %, [TapClicks](https://www.tapclicks.com/blog/how-to-track-ai-referral-traffic-and-fix-your-marketing-attribution-in-2026) et [Averi](https://www.averi.ai/blog/attribution-for-ai-referred-traffic-ga4-direct-traffic) reprises indépendantes, [Statcounter](https://gs.statcounter.com/) cité par plusieurs travaux dans une fourchette 35–70 % pour la même mesure.

---

*Draft SyntheticBrain*
