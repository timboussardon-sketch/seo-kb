---
type: query
title: "Mots-clés que les IA ne peuvent pas manger (matière newsletter)"
aliases: [mots-cles-que-l-ia-ne-mange-pas, kw-non-cannibalisables, newsletter-ia-ne-mange-pas]
tags: [newsletter, geo, aeo, mots-cles-actionnels, product-led, data-proprietaire, ai-overview, cannibalisation]
created: 2026-06-24
updated: 2026-06-24
sources: 6
confidence: high
status: draft
---

# Mots-clés que les IA ne peuvent pas manger

Note de matière pour une édition de newsletter. Tout ce que le vault dit sur le sujet, recoupé et sourcé. Voix de travail, pas encore la voix d'édition.

## Le point de départ : ta propre phrase

L'expression vient de toi, en clair, dans le call Leexi du 21 mai 2026 :

> "Il faut qu'on trouve tous les mots-clés que ChatGPT ne peut pas vous manger. Parce que demain, si tu tapes « meilleur logiciel de prise de notes », il va te lister les logiciels, mais est-ce que tu fais un clic derrière ? Pas forcément. (...) Tous les mots-clés informationnels qui vont être mangés par les IA, on ne récupérera aucun clic." [[sources/leexi-call-2026-05-21]]

C'est la thèse centrale. Un mot-clé est "mangé" quand le moteur génératif répond à la place du site, dans son interface, sans renvoyer de clic. La question n'est pas d'être visible, c'est de savoir si la requête laisse encore une raison de cliquer. [[concepts/tabou-visibilite]]

## Le mécanisme : ce que l'IA mange, ce qu'elle laisse

L'IA répond bien aux requêtes où l'utilisateur veut **lire** ("qu'est-ce que X", "top 10 des Y"). Elle ne répond pas à la place du site quand l'utilisateur veut **faire** : calculer, simuler, comparer sur ses propres chiffres, décider, demander un devis, tester un outil. [[concepts/mots-cles-actionnels]]

D'où le terme signature : le **mot-clé actionnel**, à la fois décisionnel et transactionnel. L'utilisateur attend une action à la fin (contact, démo, téléchargement, devis, achat), pas juste une information. Ce sont les requêtes qui survivent à l'IA parce que la réponse n'est pas un paragraphe, c'est un geste. [[concepts/mots-cles-actionnels]]

## La donnée qui tranche : la prévalence des AI Overviews dépend du type d'intention

C'est le chiffre qui rend la newsletter solide, et il est contre-intuitif. L'étude Seer Interactive (24 avril 2026, 53 marques, 5,47 millions de requêtes) mesure la fréquence d'apparition de l'AI Overview par type de requête :

| Type de requête | Prévalence AI Overview |
|---|---|
| Informationnelle | 36 % |
| Commerciale | 8 % |
| Transactionnelle | 5 % |
| Comparaison ("meilleur X", "X vs Y") | 95,4 % |
| Question ("comment faire X") | 85,9 % |

Source : [[concepts/metriques-visibilite-geo]] via l'édition [[revues-presse/2026-06-16]]. Lecture directe : une requête transactionnelle a 5 % de chances de croiser un AIO, une requête de comparaison en a 95 %. Le terrain transactionnel est presque vierge d'IA. Le terrain de la comparaison générique est saturé.

Deuxième couche de la même étude : sur les requêtes **sans** AI Overview, le CTR organique monte (de 2,93 % à 3,97 % en douze mois). Ce segment ne disparaît pas, il se concentre sur les gens qui ont déjà décidé de cliquer. Les mots-clés que l'IA ne mange pas valent donc mécaniquement plus cher au clic. [[revues-presse/2026-06-16]]

## Le piège à désamorcer : "comparatif" n'est pas un bloc homogène

Tension à traiter franchement dans l'édition, sinon un lecteur attentif la verra. Toi tu recommandes les pages de bascule ("passer de Fathom à Leexi", "passer de Whisper à Leexi") [[sources/leexi-call-2026-05-21]]. Or Seer dit que les requêtes de comparaison sont mangées à 95 %. Et l'étude Averi (8 juin 2026, 12 mois de GSC) montre une page "AirOps alternatives" à 0,02 % de CTR, 77 967 impressions pour 17 clics. [[revues-presse/2026-06-08]]

La résolution n'est pas que "le comparatif est mort". Elle est qu'il y a deux objets différents derrière le même mot :

- **Le comparatif éditorial generique** ("meilleur logiciel de X", "X alternatives" en listicle) : un LLM produit 80 % de la page tout seul, il connaît les acteurs et génère la liste dans l'AIO. Page substituable, donc mangée. C'est exactement le cas Averi.
- **La page de bascule décisionnelle** ("passer de X à Y") portée par de la data propriétaire (preuves clients réelles, captures, chiffres internes) et un point de conversion (récupérer un email) : l'intention est d'agir, pas de lire un classement. Ce n'est pas le même mot-clé même si le mot "comparatif" traîne autour.

Le test qui sépare les deux est le test de substitution. [[concepts/test-substitution-llm]]

## Les deux filtres pour décider d'attaquer un mot-clé ou pas

**Test de substitution LLM (filtre 80 %).** Pour chaque idée de page, demander à un LLM de produire la réponse. S'il produit 80 % de la page, ne pas la créer : elle n'a aucun avantage défensif. [[concepts/test-substitution-llm]]

**Test ChatGPT en 2 questions.** Q1 : est-ce que ChatGPT peut répondre à cette requête ? Q2 : si oui, peut-il faire mieux que toi ? Oui aux deux : la page est morte avant d'exister. Sinon : opportunité, surtout si l'intention est une action. [[concepts/mots-cles-actionnels]]

Les deux disent la même chose sous deux angles : un mot-clé survit à l'IA quand sa réponse exige quelque chose que le modèle n'a pas, soit une donnée propriétaire, soit un outil qui s'exécute.

## Où ils se trouvent : pas dans Semrush, dans ta data

Les mots-clés actionnels ne sont pas dans les outils SEO classiques, parce que tout le monde y a accès et qu'un LLM peut les ressortir aussi. Ils sont dans ta data propriétaire : calls clients, tickets SAV, chat support, avis G2/Trustpilot, champ "raison du deal perdu" du CRM, commentaires LinkedIn, GSC croisée avec les deals closed. [[concepts/data-proprietaire]] [[concepts/mots-cles-actionnels]]

Ta formulation dans le call : "La data propriétaire que tu as, toi, moi je ne l'ai pas. On se battra sur les mêmes mots-clés, sauf les mots-clés propriétaires que tu as, toi." [[sources/leexi-call-2026-05-21]] C'est le moat. Un nouvel entrant copie ton outil en dix minutes sur Claude Code, il ne copie pas dix ans de calls clients.

## Le format qui défend pour de bon : la page est l'outil

L'extrême du test de substitution, c'est le Product-Led SEO : la page embarque le composant fonctionnel (calculateur, simulateur, configurateur, comparateur sur données réelles). L'AI Overview peut résumer un texte, il ne peut pas exécuter ton calculateur dans la SERP. [[concepts/product-led-seo]]

Et l'outil ne sert pas qu'à défendre le mot-clé. Il récupère un email et il envoie à Google un signal d'engagement (l'utilisateur uploade, joue avec l'outil). [[sources/leexi-call-2026-05-21]] La requête "outil gratuit de X" force d'ailleurs ChatGPT à renvoyer vers une vraie page outil, là où "meilleur logiciel de X" ne renvoie qu'une liste.

## Le cadrage business à garder en tête

Sur 100 personnes qui cherchent, 90 veulent comprendre, 10 sont prêtes à agir. [[raw/bootcamp4/exercices/exercice-skill-seo-mots-cles-decisionnels]] Le travail consiste à isoler les 10, et à transformer une partie des 90 en emails via un outil ou une page-problématique. Chaque page a un intérêt mesurable (un email, un lead), pas un score de visibilité. [[concepts/tabou-visibilite]]

Ordre d'attaque des mots-clés : décisionnel d'abord (meilleur, comparatif de bascule, avis), actionnel (la page attend un geste), transactionnel (achat), informationnel en dernier. [[raw/bootcamp4/session-3-audit-resume-participants]]

## Angles d'édition possibles

- Angle "le chiffre qui retourne l'intuition" : 5 % d'AIO sur le transactionnel contre 95 % sur la comparaison. Ouvrir là-dessus, dérouler le reste.
- Angle "le test que tu peux faire en 30 secondes" : le test ChatGPT 2 questions, appliqué en direct sur trois mots-clés du lecteur.
- Angle "pourquoi ta page comparatif est à 0,02 % de CTR" : partir du cas Averi, expliquer substituable vs défendable.
- Angle "la seule liste de mots-clés que personne ne peut te copier" : la data propriétaire comme moat.

## 1. Les preuves : ce que le vault contient comme news et stats

Réponse directe à la question "est-ce qu'il y a de la donnée qui justifie de viser des mots-clés non mangés ?" : oui, et elle se range en quatre couches.

### a. Le clic s'effondre, mais seulement sur certaines requêtes

| Donnée | Chiffre | Source |
|---|---|---|
| Clic vers un résultat classique quand un AIO s'affiche | 8 % contre 15 % sans AIO | Pew Research, 2025 |
| CTR organique sur requêtes avec AIO | -61 % (1,76 % à 0,61 %) | Seer Interactive, 3 119 termes, 42 organisations |
| CTR position 1 avec AIO présent | -58 % | Ahrefs, 300 000 mots-clés |
| Taux de zéro-clic US | 68 % début 2026 contre 58,5 % en 2024 | SparkToro / Similarweb |
| CTR position 1 sur requêtes informationnelles, en un an | -44,6 %, même sans résumé IA | Ahrefs, 150 000 mots-clés |

Réf vault : [[etudes-IA/2026-06-18-stats-ai-overviews-ctr]], [[etudes-IA/2026-06-19-stats-zero-clic-intent-informationnel-transactionnel]].

### b. La preuve qui parle directement aux sites non produit : l'étude Wikipédia

C'est la donnée la plus importante pour ton angle, parce que Wikipédia est le site éditorial pur par excellence, sans produit ni service à vendre. Étude sur 161 382 articles : -15 % de trafic en moyenne avec l'AI Overview, mais la perte n'est pas uniforme.

- Culture, lifestyle, société : perte élevée. La requête est simple, l'IA répond entièrement, zéro raison de cliquer.
- Sciences, technologie, médecine : perte faible. La requête est complexe, l'IA répond partiellement, l'utilisateur clique pour aller plus loin.

Tu l'avais déjà formulé dans ton édition Algorithme de mars 2026 : *« le contenu généraliste n'est plus la priorité. Il faut de l'expertise, du contenu de niche, du contenu actionnel. »* La règle pour un site sans produit : ce qui survit n'est pas le format outil (tu n'en as pas forcément), c'est la profondeur et la complexité que l'IA ne peut traiter qu'à moitié. Réf : [[sources/algorithme-etude-citation-ia]].

### c. Le contenu générique mis à l'échelle s'effondre, la data propriétaire tient

- Lily Ray, 13 mai 2026, 220+ sites se déclarant clients de plateformes de contenu IA : 54 % ont perdu au moins 30 % de leur pic de trafic, 39 % au moins 50 %, 22 % au moins 75 %. Réf : [[revues-presse/2026-06-01]].
- Étude académique (10 000 requêtes, 25 domaines) sur ce qui augmente la citation par les LLM : ajouter des citations +41 %, ajouter des statistiques +30 %, ajouter des sources d'autorité +30 %. Ce qui se fait manger, c'est le texte nu. Ce qui se fait citer, c'est la donnée sourcée. Réf : [[sources/algorithme-etude-citation-ia]].

### d. La nuance pro à garder : le clic se déplace, il ne disparaît pas

68 % de zéro-clic d'un côté, mais le trafic issu des moteurs IA monte (x3 sur certains panels) et convertit mieux (7,1 % sur un panel, deux fois mieux que l'organique selon Conductor). Réf : [[etudes-IA/2026-06-18-stats-recherche-ia-geo]], [[revues-presse/2026-06-16]]. Pour un site non produit, l'implication est que se faire citer (GEO) devient un objectif au même titre que se faire cliquer.

## 2. Le process pour les trouver : X et Reddit

Le principe de fond vient de ton workflow mots-clés en six sources : le consensus web est le bruit, le terrain X est le signal, Reddit donne le langage non filtré, le croisement donne les angles exclusifs. Réf : [[raw/bootcamp4/session-1-mots-cles-prep]]. Pour la chasse aux mots-clés non mangés, deux sources font le gros du travail parce qu'elles remontent des intentions que l'IA n'a pas digérées et des formulations absentes des outils SEO.

### X via Grok DeepSearch

Grok est le seul LLM branché en temps réel sur X. Il sort des intentions fraîches que ni le Keyword Planner ni la GSC ne voient. Deux prompts suffisent pour la découverte de mots-clés non mangés.

Prompt terrain (ce que les praticiens demandent et que l'IA ne traite pas bien) :

```
Active DeepSearch. Sujet : [THÉMATIQUE]
Cherche uniquement sur X, 30 derniers jours :
1. Les questions concrètes posées par des praticiens qui n'obtiennent
   pas de bonne réponse (ni dans les commentaires, ni quand on tape
   la question dans ChatGPT)
2. Les calculs, comparaisons et arbitrages personnels que les gens
   font à la main (chiffres, configs, cas particuliers)
3. Les débats où les experts ne sont pas d'accord
Pour chaque trouvaille : la formulation exacte, @handle, date, lien.
Format tableau.
```

Prompt gap (ce que X discute et que Google ne couvre pas) :

```
À partir des données X ci-dessus, isole :
1. Les sujets activement discutés sur X mais absents des 10 premiers
   résultats Google
2. Les questions où la réponse exige une donnée chiffrée, un calcul
   personnalisé ou un cas précis (donc non résolvable par un paragraphe
   générique d'IA)
3. Les formulations récurrentes que personne n'a transformées en page
Format : [Intention | Pourquoi l'IA ne la mange pas | Format de page]
```

### Reddit

Reddit donne le vocabulaire réel, les objections nues, les questions mal servies. Garde-fou opérationnel : le crawler est souvent bloqué, donc on colle les threads à la main et on les décompose en besoin puis mot-clé puis cluster. Les prompts utiles pour la chasse aux non mangés sont ceux qui remontent une intention que l'IA ne sait pas clore.

Prompt questions mal servies (le filon principal) :

```
Liste sur Reddit (site:reddit.com) les questions sur [SUJET] qui ont :
- 0 à 2 réponses satisfaisantes
- mais >10 upvotes ou >20 commentaires
Ce sont des intentions de recherche mal servies.
Pour chacune : question textuelle exacte, URL, subreddit, et pourquoi
aucune réponse (web ou IA) ne la satisfait.
```

Prompt vocabulaire et arbitrages personnels :

```
Analyse 30 threads Reddit sur [THÉMATIQUE] et extrais :
- Les expressions exactes que les gens emploient (≠ vocabulaire marketing)
- Les moments où ils décrivent un calcul, une comparaison ou un choix
  qu'ils ont dû faire eux-mêmes faute de réponse toute faite
Donne 20 formulations avec la phrase citée.
```

Prompt inversions (matière à Surprise Gap) :

```
Cherche sur Reddit les opinions contre-intuitives sur [SUJET]
(titres "unpopular opinion", "hot take", threads à fort ratio de réponses).
Pour chaque : la thèse, l'argument, le contre-argument majoritaire.
```

Le tri ensuite : chaque formulation remontée passe le test de substitution ci-dessous. Ce qui reste alimente le Google Sheet noté sur Mot-clé / Intention / Difficulté / Funnel / Note.

## 3. Le tableau d'analyse : mangé contre non mangé, pour un site non produit

Pour un site sans produit ni service (média, blog d'expertise, site de contenu, éditeur), le moat ne peut pas être "j'embarque mon produit dans la page". Il devient l'un de ces quatre : une donnée first-party que toi seul publies (étude, baromètre, mesure), un outil interactif qui est la valeur en lui-même (calculateur, comparateur filtrable), une profondeur de niche que l'IA ne traite qu'à moitié (la leçon Wikipédia sciences/tech/médecine), ou une agrégation de signaux frais ou communautaires que le modèle n'a pas structurés. La conversion n'est plus un email vers un SaaS, c'est la citation par l'IA, l'autorité, l'audience récurrente, l'affiliation ou la publicité.

### Étape 0 du skill pSEO appliquée (test de substitution LLM)

Exemple sur un site de contenu running (aucun produit vendu).

| Idée de page | Q1 ChatGPT répond aussi bien ? | Q2 composant interactif ou data non reproductible ? | Q3 raison d'exister dans un navigateur ? | Verdict |
|---|---|---|---|---|
| « meilleur plan d'entraînement marathon » | Oui, liste générique | Non | Non | Mangé |
| « qu'est-ce que le mur du marathon » | Oui, réponse complète | Non | Non | Mangé |
| « calculateur d'allure selon mon chrono cible » | Non, calcul personnalisé | Oui, calculateur | Oui | Non mangé |
| « comparateur de 30 montres GPS, prix et autonomie à jour » | Non | Oui, comparateur filtrable + data fraîche | Oui | Non mangé |
| « temps moyen au marathon de Paris par tranche d'âge, 50 000 finishers » | Non, donnée propriétaire | Oui, dataviz + étude originale | Oui | Non mangé |

### Tableau étendu : 14 mots-clés notés (site non produit)

Mélange volontaire de niches (running, finance perso, immobilier, nutrition, voyage, culture) pour montrer que la logique se transpose. Le verdict ne dépend pas du sujet, il dépend de ce que l'IA peut clore seule.

| # | Mot-clé | Intention | Verdict | Pourquoi | Moat / format sur un site non produit |
|---|---|---|---|---|---|
| 1 | « qu'est-ce que le VO2max » | Know-Simple | Mangé | Définition close en deux phrases dans l'AIO | Aucun, texte substituable |
| 2 | « combien de calories dans une banane » | Factuel | Mangé | Réponse directe, zéro raison de cliquer | Aucun |
| 3 | « définition de l'inflation » | Know-Simple | Mangé | L'IA répond mieux et plus court | Aucun |
| 4 | « symptômes de la grippe » | Know | Mangé | Requête simple, réponse complète en AIO | Aucun |
| 5 | « meilleurs films de 2026 » | Commercial/liste | Mangé | ChatGPT génère la liste directement | Aucun, listicle reproductible |
| 6 | « recette de pâte à crêpes » | Know | Mangé | Recette servie dans la SERP | Aucun |
| 7 | « comment calculer son IMC » (explication) | Know | Mangé | L'IA explique la formule, pas besoin de page | Aucun si c'est du texte |
| 8 | « calculateur d'allure marathon selon mon chrono cible » | Do | Non mangé | Calcul personnalisé que l'AIO ne fait pas tourner | Outil interactif (le calculateur est la valeur) |
| 9 | « simulateur de capacité d'emprunt selon apport et revenus » | Do | Non mangé | Entrées perso + calcul, l'IA ne le restitue pas dans la SERP | Outil interactif |
| 10 | « convertisseur d'allure min/km vers temps sur 5/10/21/42 km » | Do | Non mangé | Conversion à inputs multiples | Outil interactif |
| 11 | « comparateur de 30 montres GPS, prix et autonomie à jour » | Commercial | Non mangé | Données fraîches et filtrables que le modèle n'a pas à jour | Comparateur filtrable + data live |
| 12 | « baromètre des loyers par quartier à Lyon, données 2026 » | Know/data | Non mangé | Donnée chiffrée datée et localisée que l'IA n'a pas | Étude first-party + dataviz |
| 13 | « âge du record perso en course, analyse de 200 000 finishers » | Know/data | Non mangé | Donnée originale, jamais publiée ailleurs | Étude propriétaire citable |
| 14 | « comparatif fiscal SCI à l'IR vs IS sur 10 ans avec mes chiffres » | Do/complexe | Non mangé | Arbitrage complexe et personnalisé, l'IA ne le tranche qu'à moitié | Simulateur + profondeur de niche (leçon Wikipédia) |

Quatre familles de non mangés ressortent : les outils interactifs (8, 9, 10), les comparateurs à données fraîches (11), les études first-party citables (12, 13) et les arbitrages complexes personnalisés (14). Les mangés (1 à 7) ont un point commun : l'IA referme la requête sans que l'utilisateur ait à agir ni à voir une donnée qu'elle n'a pas.

### Deux réflexes de production pour sites non produit

Au-delà du choix du mot-clé, il y a deux façons de fabriquer la page non mangeable que l'édition gagnerait à montrer.

**Le réflexe annuaire (directory sémantique dense).** Quand une thématique se croise sur deux ou trois axes (profil par besoin par format, type par usage par niveau), chaque croisement devient une page. Une matrice de combinaisons produit des centaines de pages, chacune dense et structurée, qui répond à une micro-requête ultra-précise. L'IA ne la mange pas parce que ce n'est pas une réponse en paragraphe, c'est une ressource navigable et filtrable qui agrège et croise plusieurs sources, avec une densité sémantique qu'un chat ne restitue pas. Sur un site sans produit, la conversion ne passe pas par un email vers un SaaS mais par un lead magnet attaché à la page (un PDF, un guide, un export téléchargeable). Le piège à tenir : le thin content. Chaque page de la matrice doit changer de contenu réel, pas seulement de titre, sinon Google la traite comme dupliquée.

**Le réflexe création de data (pas seulement agrégation).** L'étage au-dessus de "viser un mot-clé non mangé", c'est construire soi-même la donnée qui n'existe pas encore sous forme structurée : compiler des specs depuis les sources primaires, relever un terrain, agréger une base métier à la main, et en faire un tableau comparable ou une étude. Cette donnée devient citable par les IA précisément parce qu'elle n'était nulle part avant. Ensuite on lit ses pages winners dans la GSC, on isole le pattern commun de celles qui sur-performent, et on transforme les pages "Do" gagnantes en outils interactifs (calculateur, comparateur, tableau filtrable). L'autorité se bâtit par la densité thématique de la verticale et le maillage interne, pas par l'achat de liens. C'est le levier qui permet à un petit site de passer devant des acteurs majeurs sur sa niche, sans budget de netlinking.

### La paire à montrer dans l'édition

| Critère | Mot-clé mangé | Mot-clé non mangé |
|---|---|---|
| Requête | « qu'est-ce que la VMA » | « calculer ma VMA à partir de mon dernier 10 km » |
| Intention | Informationnelle simple (Know-Simple) | Actionnelle (Do) |
| Ce que fait l'IA | Répond entièrement dans l'AIO, zéro clic | Ne fait pas tourner le calcul personnalisé dans la SERP |
| Prévalence AIO | Élevée (36 % sur l'informationnel) | Faible, l'intention exige une action |
| Moat sur un site non produit | Aucun, texte substituable | Le calculateur est la valeur, plus une donnée de référence sourcée |
| Format | Article (à éviter) | Outil interactif + passage ancré citable |

Lecture pour l'édition : sur un site sans produit, le mot-clé non mangé n'est pas forcément transactionnel, c'est celui dont la réponse complète exige soit un calcul personnalisé, soit une donnée que tu es seul à avoir, soit une profondeur que l'IA ne couvre qu'à moitié. Les deux filtres restent le test de substitution 80 % et le test ChatGPT en deux questions. Réf : [[concepts/test-substitution-llm]], [[concepts/product-led-seo]], [[concepts/mots-cles-actionnels]].

## Sources mobilisées

```
[[sources/leexi-call-2026-05-21]] — la phrase fondatrice + cadrage email/outil/data propriétaire (verbatim Tim)
[[concepts/mots-cles-actionnels]] — terme signature, test ChatGPT 2 questions, où trouver les kw
[[concepts/test-substitution-llm]] — filtre 80 %, cas Victoria Garden (5 validées / 2 rejetées)
[[concepts/product-led-seo]] — la page EST l'outil, défense la plus solide face aux LLM
[[concepts/data-proprietaire]] — le moat, 5 types de data propriétaire
[[concepts/tabou-visibilite]] — bannir "visibilité", vendre des leads
[[revues-presse/2026-06-16]] — étude Seer : prévalence AIO par type d'intention (le tableau)
[[revues-presse/2026-06-08]] — étude Averi : cas page "alternatives" à 0,02 % de CTR
```

## Gaps identifiés

- Pas de chiffre first-party à toi sur la prévalence AIO par intention (tout vient de Seer/Averi, panels externes). Un relevé maison sur une propriété GSC réelle rendrait l'édition imparable. À croiser avec [[project_etudes_originales]] (étude CTR x AI Overviews GSC déjà prévue).
- Le seuil 80 % du test de substitution est qualitatif, jamais mesuré. L'édition peut l'assumer comme heuristique, pas comme métrique.
- Manque un exemple chiffré de page-outil qui a tenu (CTR maintenu) pour équilibrer le cas Averi négatif. Golfiller pourrait servir si data dispo. [[project_golfiller]]

## Queries dérivées

- "Quels mots-clés de bascule (passer de X à Y) survivent réellement à l'AIO selon la GSC ?"
- "Liste des formats de page qui passent le test de substitution, classés par coût de production"
- "Comment mesurer en GSC la part de mes impressions qui partent sur des requêtes mangées par l'AIO"
