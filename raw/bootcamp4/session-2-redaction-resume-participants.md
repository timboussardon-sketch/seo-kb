---
type: bootcamp-session-resume
bootcamp: 4
session: 2
date: 2026-05-15
audience: participants
related:
  - "[[session-2-redaction-transcript]]"
  - "[[session-2-redaction-debrief]]"
  - "[[session-2-redaction-prep]]"
  - "[[sequencage-semaine-2]]"
  - "[[session-3-audit-resume-participants]]"
---

# Résumé du Call 2 · Mieux rédiger avec l'IA

Salut à tous,

Voici le résumé complet du call de ce matin. Pour ceux qui n'ont pas pu assister, vous avez tout ce qu'il faut ici pour rattraper. Pour les autres, c'est une base à relire à tête reposée et à garder sous la main quand vous attaquez vos rédactions cette semaine.

L'idée du call n'était pas de vous présenter le workflow rédaction (vous l'avez reçu mercredi en skill). L'idée c'était de vous donner ma réflexion derrière, pour que vous puissiez l'adapter à votre manière de travailler. Claude ne rédige pas à votre place, il rédige avec vous. C'est ça qu'on construit.

---

## Pourquoi on attaque la rédaction avant l'audit

Semaine 1 : mots-clés. Semaine 2 : rédaction. Semaine 3 : audit. Pourquoi l'audit n'est pas en premier ? Parce que je ne veux pas que ma stratégie soit biaisée par ce que le client (ou l'agence précédente) a déjà fait. Si une boîte vient vous voir et qu'elle a déjà eu une agence avant, c'est que ça s'est probablement mal passé. Partir de leur travail pour construire le vôtre, ça n'a pas grand intérêt.

On part de ce qu'on pense être bon, via nos skills, nos compétences, notre data propriétaire. Et on compare avec l'audit en semaine 3. Si vous préférez faire l'audit en S1, ça marche aussi, il n'y a pas de problème.

## Les 2 problématiques avec la rédaction IA aujourd'hui

1. **Indexation difficile.** Avec la multiplication des contenus IA, c'est très difficile d'indexer vos pages aujourd'hui, même quand la page est bonne. Si en plus la page est rédigée à l'IA sans cadre, ça devient très compliqué.
2. **Rédiger pour les robots, pas seulement pour l'humain.** Pendant longtemps on vous a dit "rédigez pour l'humain, pas pour Google". Ce n'est plus tout à fait vrai. Demain, ce sont des agents qui viendront scraper vos pages pour réserver un call, une chambre d'hôtel. Il faut penser au robot dès aujourd'hui.

Votre manière de réfléchir la création de contenu change.

## Règle absolue · un mot-clé à la fois

Comme pour les mots-clés en S1, moins le scope est large, meilleur sera le résultat. Si vous demandez à Claude de rédiger 10 articles d'un coup, le résultat sera horrible. Pareil si vous lui demandez tous vos posts LinkedIn du mois en une seule fois.

C'est un par un. Il n'y a pas de bouton magique. Et il faut bien intégrer ce point : **si vous n'êtes pas bon en SEO, Claude ne sera pas bon**. Si vous ne maîtrisez pas votre workflow, votre process, le résultat sera moyen. Il va vous produire des choses qui semblent géniales au premier abord. Plus vous gratterez, plus vous verrez les patterns, les données hallucinées, les tournures recyclées. Le contenu n'est pas si bon que ça au départ. C'est vous qui le rendez bon.

## Skill vs workflow · quand utiliser quoi

Vous avez deux types de compétences dans Claude :

- Les **skills** : des automatisations focales (trouver les mots-clés business, scorer un article, etc.).
- Les **workflows** : la manière dont Claude doit utiliser plusieurs skills en cascade pour un livrable complet (la stratégie SEO d'un client, la rédaction d'un article).

Si vous avez juste besoin d'une brique, n'utilisez pas le workflow complet, appelez juste le skill. Si votre client vous dit qu'il manque des mots-clés décisionnels, vous ne relancez pas tout le workflow mots-clés, vous appelez le skill `seo-quick-win` ou similaire.

Personnellement, j'utilise plus souvent les skills que les workflows. Une fois qu'un workflow a tourné, on itère via les skills. Adaptez à vos besoins.

## Les 5 étapes du workflow rédaction

Cinq étapes dans l'ordre. Si vous sautez une étape, la suivante s'effondre.

### Étape 1 · Le brief

Le brief c'est ce qu'on a vu en S1. Il se fait en amont, pas en même temps que la rédaction. Vous lancez `seo-brief-contenu` sur la requête cible et vous lui demandez la structure Hn complète dans la même demande. Hn dans le brief, pas après.

Brief sans structure Hn validée = brief incomplet. Sans elle, Claude structure à sa façon par défaut, vous retombez dans le format LLM moyen (intro mou, trois sous-titres décoratifs, conclusion qui résume).

Une structure Hn valide doit contenir : couverture exhaustive des micro-intentions de la requête, hiérarchie d'intention respectée (Know-Simple en début, Know au milieu, Do en fin), un H2 dédié au passage ancré (extractible Featured Snippet), une FAQ à la fin, au moins un H2 qui couvre l'angle absent de la SERP.

Vous validez la structure Hn avant tout. Si elle ne vous plaît pas, vous corrigez à la main et vous réinjectez.

### Étape 2 · Nourrir le brief avec ta data propriétaire

La structure Hn est validée. Avant la rédaction, vous nourrissez chaque H2 avec votre matière objective. C'est ça qui transforme un brief générique en brief client.

Pour chaque H2, vous cherchez dans vos archives et vous collez dans le brief : donnée chiffrée propriétaire (CRM, dashboard, étude commandée), verbatim client (calls, emails, témoignages), cas client (projets passés, dataset accumulé), entité technique précise, donnée terrain Reddit ou Grok.

Règle simple : un H2 sans matière propriétaire = un H2 sur lequel vous allez écrire de la commodité. Vous revenez à vos archives, vous trouvez la matière, vous collez sous le H2 concerné. Si rien ne sort, vous remettez le H2 lui-même en question.

À la fin de cette étape, votre brief ressemble plus à un dossier de presse qu'à un sommaire. C'est le signe que c'est bien fait.

### Étape 3 · Ajouter tes idées perso dans le brief

La data objective est en place. Vous ajoutez maintenant votre couche subjective : vos inversions, vos positions tranchées, votre point de vue éditorial. Personne ne peut le faire à votre place.

Pour chaque H2, vous vous posez 3 questions : quelle position tranchée j'ai que les autres n'osent pas formuler, quelle inversion experte je peux poser (le consensus dit X, ma data dit Y), quel exemple concret je peux raconter ici (un client, un cas vécu, un chiffre interne).

Vous collez les réponses dans le brief, sous le H2 concerné. Pas en bloc séparé. Au bon endroit, pour que Claude les voie au moment où il rédige cette section précise.

Garde-fou : si vous n'avez pas d'opinion tranchée sur un H2, c'est probablement que ce H2 ne devrait pas exister sur cette page. Vous le retirez, ou vous le déléguez à un article satellite pour plus tard. Mieux vaut une page courte avec une voix qu'une page longue qui dilue.

### Étape 4 · Lancer le workflow rédaction, ne pas dépasser 50%

Le brief est complet. Vous lancez le skill rédaction reçu mercredi, en joignant le doc complémentaire fourni avec et votre worksheet ton de voix rempli, dans la même conversation Claude que le brief.

Vous lancez. Mais vous ne laissez pas Claude finir l'article d'un coup. **Vous arrêtez à 40-50%** sur les pages piliers. Sur un article cible 2000-2500 mots, vous arrêtez à 1000-1200 mots.

Pourquoi cette règle des 50% sur les piliers : le LLM dérive après ~1000 mots. Il retombe dans son corpus moyen, recycle ses tournures, perd votre ton de voix. Plus vous le laissez écrire d'un coup, plus la dérive s'accumule. Vous voulez vérifier que les fondations tiennent avant de bâtir le reste, et fact-checker la matière déjà produite avant que d'éventuelles hallucinations contaminent les 50% suivants.

Nuance importante : la règle des 50% c'est pour les **pages piliers / fondamentales**. Pour les **modèles de page** (pSEO), on peut le laisser rédiger 90-100% parce qu'on a déjà cadré le template ailleurs (on en reparle plus bas).

Sur les 1000-1200 premiers mots, vous relisez avec 4 questions :
1. Le ton de voix tient-il ? (comparez avec votre worksheet)
2. Le Surprise Gap est-il visible dans les 300 premiers mots ?
3. Y a-t-il un tic LLM qui s'est glissé (jargon creux, méta-intro, faux enthousiasme) ?
4. La data propriétaire et les idées perso injectées aux étapes 2 et 3 sont-elles effectivement présentes ?

Si non à l'un des quatre, vous reprenez ici, avant d'aller plus loin. Pas après.

### Étape 5 · Fact-check Perplexity, puis finir l'article

Vous prenez le morceau de 1000-1200 mots produit à l'étape 4 et vous le donnez à Perplexity en Deep Search.

**Changement important par rapport à mercredi** : on faisait avant le fact-check avec Grok en mode expert. Grok mode expert n'est plus accessible gratuitement (300€/mois). On bascule sur **Perplexity Deep Search** (20€/mois, partiellement gratuit). On continue à utiliser Grok pour les signaux sociaux sur les mots-clés (scraping Twitter), mais pour le fact-check c'est Perplexity.

Le prompt à coller (je vous le remets propre dans le drive cette semaine) :

```
Rôle : Spécialiste du Fact-Checking et de la consolidation de l'autorité du contenu.

Objectif : Intégrer des sources précises (URL) ou des chiffres vérifiés directement dans le texte d'origine, là où l'affirmation est la plus forte et nécessite une preuve factuelle immédiate.

Ressources fournies :
Le Texte à Modifier : ([Insérer ici le texte complet d'origine])

Raisonnement : Pensez étape par étape à l'endroit optimal de chaque ajout de source/chiffre dans le texte.

Consignes d'intégration :
Placement : Placez chaque source (URL) ou chaque chiffre là où il apporte le plus de crédibilité ou de précision à l'affirmation la plus proche.
Formatage Strict : Vous devez encadrer uniquement l'ajout (le chiffre ou l'URL) par des guillemets doubles français : « [Chiffre ou URL] ».
Priorité : Donnez la priorité aux chiffres précis ou aux URL des sources primaires qui valident des faits spécifiques.
```

Garde-fou absolu : vous vérifiez manuellement chaque source. Une URL morte ou un chiffre inventé tue plus de crédibilité qu'il n'en apporte. Vous ouvrez, vous vérifiez, si le doute persiste vous retirez.

Sur les contenus longs, Perplexity fact-checke moins bien. Donc **fact-checkez à l'étape 5 (sur le morceau de 1000-1200 mots), pas seulement à la fin**. À cette étape 5, ce n'est pas qu'un plan, Claude met aussi des idées et des données à valider, donc il y a déjà de la matière à fact-checker. Vous pouvez même fact-checker deux fois : à l'étape 5 et à la sortie finale.

**Finir l'article.** Vous revenez à Claude (toujours la même conversation). Vous lui donnez le morceau fact-checké avec ses sources « », et la consigne : "termine l'article en respectant la structure Hn, en gardant le même ton, en utilisant les sources fact-checkées comme matière, et sans répéter ce qui a déjà été dit". Vous laissez produire les 50% restants.

Vérifications finales avant de considérer l'article livré : passage ancré dans les 300 premiers mots (150-200 mots auto-suffisants, extractible Featured Snippet), bloc d'authorship ~50 mots à la fin (extractible Position 0 / AI Overview), FAQ stratégique en bas de page, ton de voix tenu sur l'ensemble, mots interdits absents.

Et un dernier point sur le temps : **45 min en moyenne pour un article standard, mais 1h30 à 2h pour un contenu vraiment fondamental**. C'est normal. C'est pas parce que c'est rédigé par une IA qu'il faut bâcler. Demain tout le monde aura du contenu, ce qui fera la différence c'est la qualité difficile à copier.

---

## Le scoring · `opendecoder-seo-scoring-system`

Une fois l'article rédigé, vous le scorez. Pas tous, mais au minimum vos pages fondamentales. Le scoring vous donne le pourcentage de chances de ranker dans les IA. Ce n'est pas 100% fiable, mais ça donne une direction et surtout, ça reste en mémoire dans votre Claude.

Le système calque le paper OpenDecoder (Mo et al., 2026). Quatre scores qui s'agrègent :

```
S_final = S_Pertinence + 0.5 × (S_Qualite + S_Potentiel + S_AEO)
S_100 = (S_final / 2.5) × 100
```

S_Pertinence porte la base (coefficient 1). Les 3 autres sont des bonus à coefficient 0.5. C'est la règle des 3 bonus qui s'ajoutent à la pertinence dominante.

**S_Pertinence** : alignement sémantique entre la page et l'intention. Couverture des entités (primaires, secondaires, tertiaires), alignement intention (Know-Simple / Know / Do / Commercial), couverture du champ sémantique (clusters attendus), signaux on-page.

**S_Qualite** : qualité éditoriale jugée par LLM en mode Quality Rater. E-E-A-T, profondeur, structure Hn, lisibilité.

**S_Potentiel** : capacité à performer face à la SERP estimée et à l'effort engagé. Paysage concurrentiel, complétude des formats attendus, signaux d'opportunité, position GSC actuelle si dispo.

**S_AEO** : survie face aux moteurs IA (SGE, SearchGPT, Perplexity, AI Overview). Surprise (éléments Haute Surprise), Grounding Density (preuves atomiques par 100 mots), RAG Structurer (extractibilité), Freshness Guard (signaux temporels).

À la fin vous obtenez une note sur 100. Sous 65 sur l'une des dimensions, vous reprenez la dimension la plus faible. Au-dessus de 85, le contenu est prêt.

Ce qui est intéressant : Claude garde tous vos scores en mémoire. Plus vous scorez, plus il apprend ce qui marche chez vous. Si l'article A a fait 88 et qu'il est cité par ChatGPT, Claude sait que 88 est la note moyenne sur cette thématique. Le prochain contenu, il visera plus haut. **Le standard d'exigence monte avec le temps**.

À la sortie du scoring, vous devez pouvoir énoncer 2 axes d'amélioration concrets, formulés au niveau du sous-score :
- "S_ent à 0.55 : ajouter les entités secondaires sur la garantie et l'autonomie dans le H2 pricing"
- "S_surprise à 0.25 : injecter le verbatim client du cas Lyon dans le H2 sur l'intégration"
- "S_format à 0.40 : ajouter le tableau comparatif neuf / reconditionné absent aujourd'hui"

Pour le suivi des citations LLM, je vous le redis : pas d'outil dédié bidon (la plupart des "AI rank tracker" sont nuls). Soit suivi à la main avec votre client, soit via votre Analytique. La data peut être redonnée à Claude pour qu'il calibre son standard de note.

---

## Les modèles de page · scaler le système

Une fois que vous savez produire UN bon article, la question suivante : comment passer à 100 pages, 500 pages, sans tomber dans la moulinette à thin content que Google sanctionne et que les LLMs ignorent.

La réponse, c'est le modèle de page. Pas un template creux où on change juste le nom de la ville, mais une architecture éditoriale qui branche une base de données propriétaire.

Le principe en une ligne :

```
Template (fixe) + Variable (base de données) = N pages organiques uniques
```

### Les 3 couches d'un bon modèle de page

1. **Base de données propriétaire structurée.** Une source de vérité avec champs typés. Pas un Excel bâclé. Si vos données viennent d'un scrap public, votre modèle est copiable, donc commodité.
2. **Logique conditionnelle.** Le contenu change selon les variables, pas seulement leur affichage. Un paragraphe si le prospect est PME, un autre si c'est ETI. Un bloc technique si le cas d'usage demande de l'API, un autre si c'est no-code.
3. **Couche éditoriale humaine ou IA supervisée.** Exemples nommés, anecdotes datées, cas client, captures, témoignages. C'est ce qui empêche la page d'être une copie lexicale de sa voisine.

### La stratégie anti-ChatGPT

Aujourd'hui je travaille sur des stratégies **anti-ChatGPT**. Concrètement, je ne fais plus aucun mot-clé sur lequel ChatGPT peut se mettre à la place du site.

Le filtre pour trier vos mots-clés et vos modèles de page :
- **Informationnel** : mangé par GPT.
- **Comparatif** : grande chance d'être mangé.
- **Simulateur** : demain, mangé.
- **Outil basé sur votre data propriétaire** : safe.
- **Transactionnel / décisionnel ultra-niché** : safe.
- **Expérience interactive sur la page** (calculateur, configurateur, devis instantané) : safe.

Il faut être spécialisé, niché, **proposer une expérience sur la page** que ChatGPT ne peut pas reproduire dans sa fenêtre de conversation.

### Les hubs et les directories

Aujourd'hui je fais quasiment plus d'articles de blog pour mes clients. Je fais des **hubs** qui contiennent des **directories** (annuaires denses de pages spécifiques).

Exemple côté organikk.co : hub "Stratégies SEO par typologie" (la page mère expose la méthode, les pages filles sont des stratégies par typologie de business), hub "Actualité SEO" (une étude par page, un mot-clé par page). Le hub c'est la page catégorie qui regroupe vos pages spécifiques.

Pour un hôtel : hub "Où manger", hub "Quoi visiter", hub "Séjours personnalisés". Sur la page mère "Séjours personnalisés", vous expliquez pourquoi vos séjours sont conçus comme ça, et vous listez vos séjours comme une page catégorie e-commerce avec filtres (nombre de personnes, budget, type de festival). Un utilisateur arrive, filtre selon ses critères, et trouve une page séjour qui ne ressemble à rien de ce qu'il aurait obtenu dans ChatGPT.

L'angle clé : ChatGPT connaît déjà l'historique de vos utilisateurs (fiche d'impôts, situation pro, famille). Quand l'utilisateur tape "séjour Bordeaux pas trop cher", ChatGPT personnalise selon son contexte. Donc demain on aura une page par persona ultra-spécifique. Et vous, vous pouvez créer ces pages avec votre data propriétaire (cas clients, calls commerciaux, SAV). Vos vrais mots-clés du futur ne sont plus dans SEMRush ou les PAA, ils sont dans vos archives.

Mieux : sur ces pages, vous proposez un outil interactif (configurateur de séjour, devis instantané). L'utilisateur remplit ses critères, à la fin "donne ton e-mail pour recevoir l'itinéraire détaillé". Vous récupérez l'e-mail, votre client le passe en marketing. Si la personne devient cliente, vous avez sa data complète, vous créez des partenariats locaux ("ce soir vous savez pas où manger, allez là"). **Vous n'êtes plus des SEO qui créent des pages, vous êtes des SEO qui récupèrent la data pour augmenter le panier moyen.**

C'est ce qu'on prépare pour demain. Vous n'aurez pas besoin de tout déployer aujourd'hui, mais c'est dans cette direction que ça va.

### Les 3 garde-fous avant de scaler un modèle

Avant de lancer la production massive d'un modèle :

1. **5 pages manuelles avant de scaler.** Vous produisez 5 pages à la main, intégralement. Vous vérifiez qu'elles tiennent debout, qu'elles s'indexent dans les 3 semaines.
2. **Indexation gate.** Avant de pousser les 100 pages suivantes, vous vérifiez l'indexation des 5 premières via GSC. Si seulement 2 sur 5 sont indexées sous 3 semaines, vous reprenez le template.
3. **Scoring sur les 5 premières.** Chaque page passe par `opendecoder-seo-scoring-system`. Si une page tombe sous 65 sur S_100, le template est faiblard, on reprend.

Si vous pouvez générer la page automatiquement sans donnée propriétaire ni couche éditoriale, ne la faites pas. Le pSEO de mauvaise qualité a tué des sites entiers depuis 2022.

---

## Points soulevés en Q&R

### Une conversation par client (Julien, Romain)

Un projet Claude par client, et dans ce projet **une seule conversation**, qu'on garde ouverte. Vous pouvez épingler les conversations importantes. Si une tâche est terminée, vous demandez à Claude de l'enregistrer dans le dossier client, vous ouvrez une nouvelle conv, et si besoin vous réinjectez la précédente comme contexte. Mais le mieux reste de tout garder dans la même conversation. La fenêtre Claude est à 1 million de tokens. Sur le terminal (qu'on verra plus tard), la limite saute encore plus loin.

### README par client pour les règles d'itération (Jamel)

Pour chaque client, vous créez un fichier README qui agrège toutes vos remarques d'itération : "pour ce client, jamais de chiffre en intro", "pas de jargon", "ne cite jamais la loi X", "ne crée pas de pages en dessous de 100€ de budget si c'est un hôtel". Claude lit ce README à chaque conversation sur ce client. C'est votre mémoire des règles spécifiques. Plus vous le nourrissez, moins vous répétez les mêmes corrections.

Ça demande de la discipline (une review précise de chaque contenu), donc ne le faites pas pour tous les types de pages au début. Commencez par vos pages principales. Jamel, on en reparle en 1V1.

### Documents en local pas pris en compte

Question récurrente. Le fichier est dans votre dossier Cowork, mais Claude ne le voit pas spontanément. Solution : en début de conversation, vous attachez explicitement les fichiers importants (ton de voix, brief du client, dossier client). Une fois qu'il les a vus dans la conv courante, il les oublie moins. S'il oublie au milieu, vous réattachez le fichier concerné.

Encore une fois : restez dans la même conversation, sinon vous recommencez à zéro à chaque ouverture.

### Itération sur un article rédigé (Christophe)

Une fois que Claude vous a sorti un article, vous itérez. Vous lui dites "change l'introduction", "ajuste cette section comme ça". Il ne relance pas le workflow, il part du contenu existant. Vous itérez tant que ça ne vous va pas. C'est ce qui peut faire passer un article de 45 min à 1h30 voire 2h sur du contenu fondamental. C'est normal, c'est même ce qu'il faut faire.

### Pureté vectorielle

Concept central qu'on a creusé en live. Sur une page, vous ne parlez pas de toutes vos entités sémantiques, vous noieriez l'intention de recherche. Sur "agence SEO", vous ne donnez pas en même temps un outil audit + un cas client BTP + 10 sujets connexes. Vous restez sur la **pureté vectorielle de la requête**.

Les ouvertures vers des sujets connexes (ex : backlinks vs contenu sur une page agence SEO), vous les mettez dans la FAQ. La FAQ sert pour les micro-intentions long-tail et les angles connexes sans casser la pureté du corps de page.

Études récentes : plus le contenu est long, plus vous risquez de ne pas être cité par les LLMs. Faites dense, pas long.

### Intention utilisateur vs intention LLM

Dans le brief `seo-brief-contenu`, vous avez deux intentions de recherche distinctes : l'intention utilisateur (ce que l'humain veut savoir) et l'intention LLM (ce que les LLMs attendent pour pouvoir citer la page). Les deux ne sont pas identiques. Sur "agence SEO", l'utilisateur veut savoir comment choisir la meilleure agence. Le LLM veut en plus un comparatif freelance vs agence. Vous traitez les deux.

---

## Devoirs pour cette semaine

1. **Choisir 1 page pilier** (un mot-clé business sur un client) et faire tourner les 5 étapes du workflow rédaction de bout en bout : brief → data propriétaire dans le brief → idées perso dans le brief → workflow rédaction à 50% → fact-check Perplexity Deep Search → finir l'article.
2. **Scorer la page produite** via `opendecoder-seo-scoring-system` (le skill vous arrive cette semaine si vous ne l'avez pas encore). Notez vos 4 scores et votre S_100 agrégé.
3. **Identifier les 2 axes d'amélioration concrets** à partir des sous-scores les plus faibles. Formulez-les au niveau du sous-score, pas du score global.
4. **Réfléchir à 1 ou 2 modèles de page** anti-ChatGPT que vous pourriez lancer chez un client, en testant le filtre "qu'est-ce que ChatGPT ne peut pas faire à ma place".
5. **Créer le README de votre client principal** avec les 3-5 règles d'itération qui reviennent le plus souvent quand vous rédigez pour lui.

Venez me voir en MP si vous bloquez.

## Ce qui arrive en semaine 3

L'audit avec Claude. On va connecter votre Search Console, scorer la santé sémantique du site existant, identifier les quick wins (positions 3-12 avec impressions hautes et CTR pourri), détecter les cannibalisations entre pages, et construire le cocon depuis la vraie data GSC. Vous repartirez avec un rapport d'audit prêt à présenter à votre client.

Bravo à tous, on a tenu deux semaines, plus qu'une à passer sur la production et après on bascule sur les automatisations et la prospection en S4.

À jeudi prochain.

Tim
