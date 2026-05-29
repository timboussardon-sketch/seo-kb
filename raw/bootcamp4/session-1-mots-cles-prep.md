---
type: bootcamp-session-resume
bootcamp: 4
session: 1
topic: mots-clés
date: 2026-05-07
duration: 70 min
status: resume
tags:
  - bootcamp4
  - session-1
  - mots-cles
  - micro-intentions
  - vecteur-semantique
  - workflow-mot-cle
related:
  - "[[bootcamp-seo-ia]]"
  - "[[skill-entites-vectorielles]]"
  - "[[skill-cluster-aeo]]"
  - "[[skill-quick-win]]"
  - "[[skill-brief-contenu]]"
---

# Session 1 · Mots-clés · Résumé

Idée directrice : un mot-clé seul ne suffit plus à positionner une page. Ce qui ranke, c'est un nuage de micro-intentions assemblé en vecteur sémantique.

---

## 1 · Micro-intentions et leur importance

Une requête business cache toujours plusieurs intentions. « Freelance GEO » : définition, comparatif vs SEO classique, fourchette de prix, mode de facturation, profil type, cas clients, outils utilisés, délai de résultats. Chacune = une micro-intention. La page qui ranke est celle qui les couvre toutes, pas celle qui répète le mot-clé principal.

KW Planner sur « freelance GEO » : 1 mot-clé. Fusionn : 50 micro-intentions. On ne cherche plus le bon mot-clé, on cherche la bonne couverture.

Deux cas concrets. Golfiller : page existante, H1 et meta intacts, on injecte les micro-intentions dans le contenu, top 1. La page n'était pas mal optimisée, elle était mal entourée. Appart hotel Bordeaux 9000 vol/mo : aucun GMB, tout misé sur les micro-intentions de la page, top SERP locale et leads.

Les micro-intentions, c'est la matière première du SEO 2026. Google les note via la similarité cosinus, les moteurs de réponse les extraient pour citer une source.

---

## 2 · La bascule

| Avant | Maintenant |
|---|---|
| Mot-clé | Vecteur d'intention |
| Match exact | Similarité cosinus |
| Densité de mots-clés | Couverture de micro-intentions |
| Choisir LE mot-clé | Construire LE nuage |

À retenir : avant on matchait, maintenant on construit. Optimiser, c'était chercher le bon paramètre à régler. Construire, c'est assembler un nuage qui couvre toutes les micro-intentions de la requête.

---

## 3 · Comment je choisis mes mots-clés · 4 piliers doctrine

Avant d'attaquer un mot-clé, je le passe au filtre de quatre questions. Si la requête échoue à l'une, je ne la prends pas.

**Pilier 1 · Surprise Gap.** Test ChatGPT en deux questions. ChatGPT peut-il répondre à la requête ? Peut-il faire mieux que ce qu'on produira ? Si oui aux deux, la page sera générique et n'apportera rien à la SERP. On jette. Si non à au moins une, il y a un gap exploitable. On prend.

Le vrai levier du Surprise Score, c'est la data originale. Ce que les autres n'ont pas ou ne disent pas. Un benchmark interne sur 200 clients, un chiffre tiré du CRM, une donnée extraite des calls jamais publiée nulle part, un retour contre-intuitif que les concurrents évitent. C'est ça qui fait diverger ton vecteur du corpus moyen, et c'est ça que Google et les moteurs de réponse préfèrent citer. Donnée existante ailleurs = commodité. Donnée chez toi seulement = Surprise Score. Avant de prendre une requête, je vérifie qu'on a au moins une donnée propriétaire à injecter dedans. Sinon, on ne sort pas du lot.

**Pilier 2 · Grounding Score.** Le client a-t-il la matière pour ancrer la page ? Data propriétaire, calls enregistrés, tickets support, CRM, études internes. Sans matière, le vecteur reste générique et le contenu plat. Sans grounding, on ne prend pas.

**Pilier 3 · pSEO.** Le mot-clé scale-t-il en template ? 1 template + N variables (ville, métier, secteur, taille d'entreprise) = des centaines de pages avec une longue traîne propre. Si oui, priorité haute, ça débloque un système entier.

**Pilier 4 · AEO.** Quelle intention derrière la requête ? Hiérarchie : Do (transactionnel, l'utilisateur veut agir) > Know (l'utilisateur veut comprendre) > Know-Simple (l'utilisateur veut une définition courte). On privilégie Do. Toujours. C'est là que la conversion existe et que les Quality Raters notent Fully Meets.

Les quatre piliers fonctionnent en série, pas en parallèle. Une requête doit valider les quatre pour entrer dans la roadmap.

---

## 4 · L'importance du contexte et ce que je mets dedans

Sans contexte client réel, ton vecteur reste générique. Même vecteur que tout le monde = nulle part dans la SERP. Le contexte fait diverger le vecteur, la divergence crée le Surprise Gap.

Quatre sources alimentent le contexte que j'injecte dans Claude :

**Calls clients.** Verbatims, objections réelles, vocabulaire des prospects. Tout ce qui ne remonte ni dans la SERP ni dans les outils SEO. Source numéro un : c'est la seule qui donne le langage non filtré du marché.

**Études de marché.** Chiffres, tendances, segments, parts de marché, taux de pénétration. Le grounding factuel qui ancre la page dans des données vérifiables. Un avis devient une assertion citable.

**Reddit.** Les vraies questions des utilisateurs, leurs problèmes concrets, leurs retours d'expérience. Une couche de langage que Google n'indexe pas en profondeur et que ChatGPT a peu vue. Source de micro-intentions invisibles dans la SERP.

**Grok mode expert.** Data fraîche non sourcée, signaux X, Reddit et forums spécialisés en temps réel. Le complément que ChatGPT n'a pas, parce que sa fenêtre de connaissance est coupée. Sert à attraper les sujets émergents avant qu'ils saturent.

Sans ces quatre sources, le vecteur reste générique. Avec, il diverge. Le Surprise Gap, c'est ça : l'écart mesuré entre ta page et la moyenne du corpus sur la requête.

---

## 5 · Le workflow mot-clé · 6 sources dans l'ordre

Six sources, dans l'ordre. Chaque étape donne une matière différente. À la fin, on assemble dans un seul Google Sheet noté sur 5 critères.

---

### Étape 1 · Google Keyword Planner · Volume marché et idées de mots-clés

**Pourquoi cette source.** Seul outil qui donne les volumes de recherche réels de Google. Sert à découvrir des mots-clés et à valider le potentiel volume d'un sujet. Accès via API ou export Google Sheet.

**Mode 1 · Recherche par mots-clés.**
- Accès : Google Ads, Outils, Keyword Planner, Trouver de nouveaux mots-clés
- Saisir 3 à 5 mots-clés seeds : les termes que le client utilise naturellement pour décrire son activité
- Filtrer par pays et langue pour éliminer le bruit
- Télécharger le CSV avec toutes les suggestions

**Mode 2 · Recherche par site.**
- Saisir l'URL du site du client
- Google analyse le contenu et suggère les mots-clés associés
- Astuce : entrer l'URL d'une page spécifique (pas le domaine) pour des résultats plus ciblés
- Tester 2 à 3 concurrents pour découvrir des angles qu'ils couvrent et que le client ne couvre pas

**Ce qu'on récupère.**

| Colonne | Utilité | Action |
|---|---|---|
| Mot-clé | Idées brutes | Garder ceux à intention business |
| Volume mensuel | Taille du marché | Indicatif, pas un critère de choix |
| Concurrence | Difficulté Ads, pas SEO | Concurrence haute = sujet monétisable |
| Tendance 3 mois | Saisonnalité | Repérer les sujets en hausse |

> Le Keyword Planner donne le volume, pas l'intention. Un mot-clé à 10 000 recherches/mois sans intention business = 0 lead. On filtrera avec la GSC.

---

### Étape 2 · Google Search Console · Données réelles et quick wins

**Pourquoi cette source.** La GSC est la seule source de vérité. Elle montre ce que Google pense déjà du site : les requêtes, les pages associées, et le delta entre visibilité et résultat. Accès via MCP (un peu technique) ou export Google Sheet.

**Export des données.**
- Période : 3 derniers mois
- Métriques : clics, impressions, CTR, position moyenne
- Export 1 · Requêtes : toutes les requêtes par impressions décroissantes
- Export 2 · Pages : toutes les pages indexées
- Export 3 · Requêtes par pages : le croisement requête / URL

**Analyse · le delta impressions vs clics.** Le signal clé n'est pas le volume mais le delta entre impressions et clics.

| Signal observé | Ce que ça veut dire | Action |
|---|---|---|
| Impressions élevées + clics faibles | Google te montre, personne ne clique | Optimiser title + meta |
| Position 3-12 + impressions élevées | Proche du top 3, quick win | Optimiser la page existante |
| CTR élevé + impressions faibles | Niche où tu es pertinent | Créer plus de contenu |
| Requête sans page dédiée | Google t'associe sans page | Créer la page = content gap |

> Règle d'or : on optimise l'existant AVANT de créer du nouveau. Les quick wins sont toujours la première action.

---

### Étape 3 · Grok et Perplexity · Data fraîche X et web que personne n'a compilée

**Pourquoi cette source.** Grok est le seul LLM branché en temps réel sur X. Il récupère les données terrain, retours pratiques et débats que ni le Keyword Planner ni la GSC ne voient. C'est un guide de sourcing, pas de rédaction. Perplexity complète sur les études de marché data poussées.

Cinq prompts en chaîne. Chaque prompt dépend du précédent. À la fin, on a un dataset fact-checké prêt à injecter dans la rédaction.

**Prompt 1 · Cartographier ce que tout le monde dit déjà.** Objectif : poser la baseline. Savoir ce que ChatGPT et Gemini répondent déjà sur le sujet, c'est ce que l'article ne doit PAS répéter.

```
Sujet : [TON SUJET]

Donne-moi le consensus actuel sur ce sujet :
- Ce que les 10 premiers résultats Google disent
- Ce que ChatGPT et Gemini répondent quand on leur pose la question
- Les chiffres et stats qui reviennent partout

Format : liste des 5-7 affirmations les plus répétées + les stats
les plus citées avec leur source d'origine.
```

Output : la réponse moyenne du web. Tout ce qui sort = le bruit. Le prompt 2 va chercher le signal.

**Prompt 2 · Scanner X pour les données terrain (DeepSearch).** Objectif : trouver ce que les praticiens partagent sur X et que personne n'a encore compilé dans un article.

```
Active DeepSearch. Sujet : [TON SUJET]

Cherche uniquement sur X, 30 derniers jours :

1. Les chiffres concrets partagés par des praticiens (résultats A/B, % de réussite, métriques, cas clients)
2. Les retours terrain négatifs ou les échecs documentés
3. Les débats entre experts : qui dit quoi et pourquoi ils ne sont pas d'accord
4. Les questions posées qui n'obtiennent pas de bonne réponse

Pour chaque trouvaille, donne :
- La donnée exacte
- L'auteur du post (nom ou @handle)
- La date du post
- Le lien

Format tableau.
```

Output : micro-données fraîches, retours réels, controverses en cours. Matière première exclusive : l'info que les autres LLMs n'ont pas dans leur corpus.

**Prompt 3 · Trouver les stats récentes sur le web (DeepSearch).** Objectif : compléter les données X avec des études, rapports et stats vérifiables publiés récemment.

```
Sujet : [TON SUJET]

Cherche sur le web les données les plus récentes (moins de 60 jours) :

1. Études ou rapports publiés en 2025-2026 avec des chiffres précis
2. Stats qui CONTREDISENT les idées reçues listées au prompt 1
3. Données provenant de sources primaires (pas des articles qui citent d'autres articles)

Pour chaque stat :
- Le chiffre exact
- La source primaire (nom de l'étude/rapport + organisme)
- La date de publication
- Le lien direct

Exclure toute donnée de plus de 60 jours.
Format tableau.
```

Output : preuves chiffrées et vérifiables. Croisé avec les données X du prompt 2 = mix terrain + académique que personne n'a.

**Prompt 4 · Identifier les angles que personne ne couvre.** Objectif : croiser les prompts 2 et 3 pour faire émerger les vrais content gaps.

```
À partir des données terrain (prompt 2) et des stats web (prompt 3), identifie :

1. Les 3 informations les plus surprenantes : celles qui contredisent le consensus du prompt 1
2. Les sujets discutés activement sur X mais absents des 10 premiers résultats Google
3. Les questions fréquentes sur X qui n'ont aucune réponse satisfaisante sur le web
4. Les données chiffrées que personne n'a encore croisées ensemble

Pour chaque trouvaille, indique :
- Ce que le web dit (ou ne dit pas)
- Ce que X révèle de différent
- Pourquoi c'est un angle intéressant

Format : tableau avec colonnes [Angle | Source X | Source Web | Pourquoi c'est un gap]
```

Output : liste d'angles exclusifs. L'info existe, mais personne ne l'a structurée. C'est là que tu apportes la valeur.

**Prompt 5 · Vérifier et sécuriser chaque donnée.** Objectif : aucune donnée ne sort sans vérification. Fact-check de tout ce qu'on a récolté.

```
Voici les données que j'ai récoltées pour mon article :

[COLLER LE TABLEAU DES DONNÉES DES PROMPTS 2 + 3]

Pour chaque donnée :

1. Vérifie que la source existe vraiment et que le chiffre est exact
2. Vérifie si des experts sur X ont contesté ou nuancé cette donnée récemment
3. Classe chaque donnée :
   ✅ Vérifiée : source confirmée, chiffre exact
   ⚠️ À nuancer : approximatif ou contesté, propose une reformulation prudente
   ❌ Non fiable : source introuvable ou chiffre faux, à retirer

Format tableau avec colonnes [Donnée | Verdict | Justification | Reformulation si nécessaire | Nuance X si existante]
```

Output : dataset nettoyé et sécurisé. Chaque chiffre utilisé est soit vérifié, soit reformulé avec prudence. Zéro risque de publier une stat fausse.

> Consensus (1) = le bruit. Terrain X (2) = le signal. Stats web (3) = la preuve. Croisement (4) = les angles exclusifs. Fact-check (5) = la sécurité. Chaque prompt dépend du précédent.

---

### Étape 4 · Reddit · Verbatims, pain points et angles contre-intuitifs

**Pourquoi cette source.** Reddit, c'est où les utilisateurs parlent sans filtre marketing. Vocabulaire réel, objections nues, retours négatifs, métaphores. Aucune étude ne capture ça.

Double usage. (1) Identifier les sujets sur lesquels publier sur Reddit en réponse à un mot-clé business. (2) Nourrir tes rédactions SEO sur ton site avec les verbatims, objections, vocabulaire réel et angles contre-intuitifs remontés. Une exécution = deux livrables alignés : un plan de publications Reddit ciblées + un brief d'enrichissement pour la page mot-clé correspondante sur le site.

Huit prompts thématiques. À choisir selon ce qu'on cherche à creuser.

**Prompt 1 · Pain points.**

```
Trouve sur Reddit (site:reddit.com) les 20 threads les plus upvotés sur [THÉMATIQUE] des 12 derniers mois.

Pour chaque thread, extrais :
- URL + subreddit + nb upvotes
- Titre du post
- Le pain point exact en 1 phrase
- Le verbatim le plus fort (citation textuelle)

→ Classe par fréquence du pain point.
```

**Prompt 2 · Pourquoi ils n'achètent pas ton produit ou service.**

```
Trouve sur Reddit les commentaires où des utilisateurs expriment de la déception, de la méfiance ou un refus d'acheter [PRODUIT/SERVICE].

Extrais :
- Le verbatim brut (pas de reformulation)
- L'objection sous-jacente (prix, qualité, confiance, complexité, ROI…)
- Le subreddit + permalink

→ Regroupe les objections par thème et donne-moi le top 5 par volume.
```

**Prompt 3 · Questions populaires que personne n'a traitées correctement.**

```
Liste sur Reddit les questions sur [SUJET] qui ont :
- 0 à 2 réponses
- Mais >10 upvotes ou >20 commentaires sur le thread

→ Ce sont des intentions de recherche mal servies.

Format : question textuelle + URL + nombre de vues/upvotes + pourquoi c'est mal répondu.
```

**Prompt 4 · Expressions utilisées par tes futurs users.**

```
Analyse 30 threads Reddit sur [THÉMATIQUE] et extrais :
- Les expressions familières / jargon utilisé par les users (≠ vocabulaire marketing)
- Les termes péjoratifs employés pour parler des concurrents ou de la catégorie
- Les métaphores récurrentes

→ Donne-moi une liste de 20 expressions avec exemple de phrase citée.
```

**Prompt 5 · Avant / Après.**

```
Sur Reddit, trouve des témoignages utilisateurs décrivant une transformation liée à [PROBLÈME/SOLUTION].

Extrais la structure :
- Situation AVANT (avec verbatim)
- Déclencheur du changement
- Action prise
- Résultat APRÈS (avec chiffres si mentionnés)

Filtre : minimum 50 upvotes sur le commentaire ou le post.
```

**Prompt 6 · Opinions contre-intuitives qui font débat.**

```
Cherche sur Reddit les opinions contre-intuitives ou controversées sur [SUJET], posts avec titre "unpopular opinion", "hot take", ou commentaires à ratio élevé (beaucoup de réponses).

Pour chaque :
- La thèse contre-intuitive
- L'argument principal
- Le contre-argument majoritaire

→ Matière première pour tes inversions expertes.
```

**Prompt 7 · Comparaisons (requêtes VS).**

```
Sur Reddit, trouve tous les threads où les utilisateurs comparent spontanément [MARQUE/OUTIL A] à [MARQUE/OUTIL B, C, D…].

Extrais :
- Le critère de comparaison (prix, ergonomie, support, features…)
- Le vainqueur selon le consensus des commentaires
- Les verbatims justifiant le choix

→ Classe les critères par fréquence d'apparition.
```

**Prompt 8 · Subreddit mapping (vue d'ensemble).**

```
Pour la thématique [X], liste-moi les 10 subreddits les plus actifs avec :
- Nombre de membres
- Volume de posts/semaine
- Les 3 tags/flairs les plus utilisés
- Le type d'intention dominant (question, avis, rant, showcase, recommandation)

Objectif : savoir où aller pêcher mes signaux selon le format de contenu que tu prépares.
```

> Pain points (1) = la douleur. Objections (2) = le frein. Questions mal servies (3) = la niche éditoriale. Vocabulaire (4) = le langage authentique. Avant/Après (5) = la preuve transformation. Inversions (6) = le Surprise Gap. Comparaisons (7) = la requête VS. Subreddit mapping (8) = la cartographie.

---

### Étape 5 · Données propriétaires · L'avantage compétitif que personne ne peut copier

**Pourquoi cette source.** Les données propriétaires révèlent des mots-clés qu'aucun outil ne connaît. Elles viennent du langage réel des clients, pas des algorithmes.

**Source A · Contenu existant du client.**
- Articles de blog, pages services, études de cas : quels sujets génèrent de l'engagement ?
- Emails envoyés aux prospects : quels arguments reviennent le plus ?
- Posts LinkedIn et réseaux sociaux : lesquels ont le plus d'interactions ?

**Source B · Interviews et verbatims clients.**
- Calls de découverte : noter les mots exacts utilisés par les prospects
- « Comment tu décrirais ton problème à un collègue ? » → mots-clés naturels
- Témoignages clients : les phrases avant / après révèlent les pain points
- Questions fréquentes en call ou email : chaque question récurrente = un article potentiel

**Source C · Données métier exclusives.**
- Chiffres internes : taux de conversion, benchmarks, stats sectorielles
- Process propriétaires : méthodologies, frameworks, grilles
- Cas clients anonymisés : résultats concrets = preuve

**Comment extraire les mots-clés.**
1. Collecter 10 à 20 verbatims (calls, emails, témoignages)
2. Repérer les formulations récurrentes : ce sont les mots-clés longue traîne
3. Croiser avec la GSC : est-ce que ces formulations apparaissent déjà ?
4. Si non, créer du contenu pour créer la demande

> Un concurrent peut copier tes mots-clés Keyword Planner. Il ne peut pas copier les verbatims de TES clients. C'est ça, l'information gain.

---

### Étape 6 · SEO Programmatique (pSEO) · Template + variable = des centaines de pages qui rankent

**Pourquoi cette source.** Le pSEO transforme les mots-clés identifiés aux étapes 1 à 5 en un système scalable. 1 template multiplié par une variable = des centaines de pages longue traîne qui captent du trafic là où personne ne se positionne.

**Le principe.**
- Formule : 1 template + 1 variable qui change = des centaines de pages uniques
- Chaque page cible une requête ultra-spécifique (longue traîne)
- Source de données : les bases de données propriétaires du client (secteurs, localisations, indicateurs, catégories)

**Identifier les modèles scalables.** Pour chaque modèle, définir :

| Élément | Description | Exemple |
|---|---|---|
| Pattern d'URL | [site]/[prefixe]/[variable] | site.com/formation/[secteur] |
| Head term (fixe) | La partie qui ne change pas | Créer un OF en |
| Modificateur (variable) | Ce qui rend chaque page unique | langues, coaching, BTP |
| Nombre de pages | Estimation réaliste | 25-35 pages par modèle |
| Source de données | Base qui alimente la variable | Liste secteurs, OPCO, régions |

**Matrice de priorisation des modèles.** Chaque modèle est évalué sur 4 critères :
1. Volume total estimé : somme des volumes de toutes les pages du modèle
2. Effort de création : combien de données uniques faut-il par page ?
3. Compétition SERP : qui est déjà positionné sur ces requêtes ?
4. Potentiel conversion : est-ce que la page mène à une action business ?

**Exécution.**
- Phase 1 (J1 à J30) : lancer le modèle prioritaire, celui avec le meilleur ratio impact/effort
- Phase 2 (J30 à J60) : mesurer, itérer, lancer le 2e modèle
- Phase 3 (J60 à J90) : scale, les modèles restants + optimisation des existants

> Chaque page générée doit apporter de la valeur unique. La variable doit créer du contenu réellement différent d'une page à l'autre (OPCO différents, réglementations différentes, marchés différents).

---

### Livrable · Google Sheet final

Tous les mots-clés extraits aux étapes 1 à 5 atterrissent dans un seul Google Sheet. Une ligne = un mot-clé. Cinq critères de notation :

| # | Critère |
|---|---|
| 1 | Volume |
| 2 | CPC |
| 3 | Intérêt business |
| 4 | Difficulté |
| 5 | YoY (Year over Year) |

Le tri se fait sur la combinaison Intérêt business + Difficulté inversée. Fort intérêt business + faible difficulté = priorité 1. Le volume sert d'arbitrage entre deux mots-clés équivalents, pas de critère principal.

Exemple de sortie : [[matrice-priorisation-mots-cles]]
