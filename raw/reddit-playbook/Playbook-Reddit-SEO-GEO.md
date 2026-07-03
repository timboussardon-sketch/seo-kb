---
type: source
source_type: doctrine
title: Playbook Reddit (SEO + GEO) : être lu par Google et cité par les IA
aliases: [playbook-reddit, reddit-seo, reddit-geo, strategie-reddit]
tags: [seo, geo, reddit, aeo, parasite-seo, ia, llm, gummysearch]
created: 2026-06-18
updated: 2026-07-03
sources: 36
confidence: medium
status: stable
---

# Playbook Reddit : SEO + GEO

> Deux résultats mesurables : des citations dans les moteurs génératifs, des positions Google. Première version le 18 juin 2026. Chiffres vérifiés contre ~25 sources le 2 juillet. Les chiffres fragiles sont signalés.

---

## En résumé (à lire en premier)

Reddit est passé du 68e rang au top 5 des domaines les plus visibles sur Google US.

En un an. Entre juillet 2023 et juillet 2024.

L'indice Sistrix est monté de 95,1 à 1 370 points. Soit +1 328 % (Sistrix via Amsive, 2024).

Trois causes se sont empilées :

- l'update « hidden gems » à l'automne 2023
- le filtre « Discussions and forums » dans les résultats
- l'accord de données Google-Reddit à ~60 M$/an (février 2024)

Mais le vrai sujet en 2026, c'est les IA.

Reddit est la source n°1 ou n°2 des citations sur tous les moteurs génératifs (Peec AI, Semrush, Evertune, détail en §2).

Sur Perplexity : entre 20 et 47 % des citations selon l'étude et la période.

Et c'est verrouillé par contrat.

Google paie ~60 M$/an pour les données Reddit. OpenAI ~70 M$/an estimés (mai 2024).

Il y a quatre façons d'exploiter Reddit, classées par rendement :

1. **Te faire citer par les IA** dans des threads décisionnels où ton site est nommé.
2. **Faire ranker des threads sur Google** dont le titre reprend une vraie requête.
3. **Miner Reddit comme source d'insights.** Aucun risque de ban : tu ne postes rien.
4. **Construire un compte crédible.** Sans ça, les trois premiers leviers sont inaccessibles.

La contrainte principale : Reddit déteste les marketeurs.

La doctrine officielle tient en une phrase : « C'est OK d'être un Redditor qui a un site web, ce n'est pas OK d'être un site web qui a un compte Reddit. »

Les sanctions : post supprimé, shadowban, bannissement définitif.

En France : ~20,6 M d'utilisateurs estimés (Influencia). +72 % de visiteurs en un an (Médiamétrie).

Mais aucune communauté SEO francophone active.

Le levier est plus faible en français qu'en anglais. Détail en §12.

---

## Le test Qadence.io (en cours)

Je suis en plein test sur Qadence.io depuis juin 2026.

Aucune étude de cas Reddit indépendante n'existe. Trafic, positions, conversions vérifiables : personne n'a publié ça.

Je produis cette donnée.

Je mesure deux choses :

- les citations de Qadence.io dans Perplexity, ChatGPT et les AI Overviews
- les positions Google sur des mots-clés décisionnels : « outil IA », « agent SEO », « [catégorie] alternatives »

Je pars d'un compte ancien, quasi inactif depuis un an.

Deux règles de conduite : pas de spam, pas d'action ponctuelle sans suite.

Le délai attendu avant un effet mesurable : 60 à 90 jours (§2).

Le point de coupe : bilan J+45, mi-août 2026. Sans thread positionné, citation IA ni mention entrante, j'arrête le test.

---

## L'exécution : routine quotidienne + Reddit Cockpit

Tout est dans le même dossier que ce playbook.

**[[Routine-quotidienne]]** contient les quotas :

- 4 à 6 commentaires par jour, plafond 8
- 1 mention par semaine
- 1 post par semaine, plafond dur 3
- le bilan du vendredi sur liste fixe de requêtes

Vérifiée contre ~25 sources le 2 juillet 2026. En cas de divergence avec ce document, c'est elle qui fait foi.

**[[Journal]]** tient le suivi. Une ligne par jour, un bloc par bilan hebdo.

**Le Reddit Cockpit** tourne chaque matin à 07h50.

Il scrape les flux RSS des subs cibles et des requêtes acheteur. Lecture seule.

Il rédige 1 à 2 commentaires par thread retenu. Anglais, 120-200 mots, quotas vérifiés contre le journal.

La file arrive dans `queue/AAAA-MM-JJ.md`.

La machine ne publie jamais. Le clic reste manuel.

Le bloc commentaires descend à 10-12 minutes par jour.

---

## 1. Visibilité Google de Reddit, 2023-2026

### Croissance 2023-2024

Juillet 2023 : reddit.com est le 68e domaine le plus visible sur Google US.

Juillet 2024 : top 5.

L'indice Sistrix passe de 95,1 à 1 370 points. +1 328 % (Sistrix via Amsive).

Le trafic organique estimé suit : de ~57 M à ~427 M de visites mensuelles. +649 % (estimation Ahrefs via Amsive, pas une donnée officielle Reddit).

Trois causes expliquent cette montée :

- **L'update « hidden gems »** (automne 2023). Google remonte le contenu expérientiel et les forums. Glenn Gabe mesure sur 97 forums : 88 % gagnent plus de 100 % de visibilité en un an. Reddit gagne entre +378 % (Semrush) et +978 % (Sistrix) selon l'outil.
- **Le filtre « Discussions and forums »**. Une zone dédiée aux forums dans les résultats. Reddit remonte sur les requêtes conversationnelles : « best X for Y », avis, troubleshooting.
- **L'accord Google-Reddit** (février 2024, ~60 M$/an). Google accède en temps réel à l'API Reddit pour ses modèles et ses réponses. Google déclare ce contrat distinct du classement organique. La corrélation temporelle est documentée par tous les outils ; la causalité directe ne l'est pas. La FTC a ouvert une enquête non publique en mars 2024.

### Correction 2025

7 janvier 2025 : Reddit perd ~350 points d'indice Sistrix. Il passe du 3e au 4e rang US.

Les core updates 2025 (mars, juin, août, décembre) créent de la volatilité sur les sites communautaires : Reddit, Quora, Stack Exchange.

Décembre 2025 : Reddit chute pendant l'update, puis revient à son niveau en une semaine.

Août 2025 : il touche brièvement le 2e rang US, devant Amazon.

Reddit reste installé dans le top 5 US. Avec une volatilité par paliers.

### Mécanisme de ranking (liens en nofollow)

Les liens sortants de Reddit sont en nofollow.

Ils ne transmettent pas d'autorité au sens backlink.

Si le plan est d'aller chercher des backlinks Reddit pour le ranking, c'est le mauvais plan.

Aujourd'hui, trois facteurs expliquent pourquoi un thread Reddit se positionne :

- le crawl quasi temps réel, facilité par l'accord de données
- les signaux d'engagement : temps passé, interactions
- le critère « expérience » de l'E-E-A-T, cible déclarée de l'update hidden gems

John Mueller (Google) précise deux choses. Les liens Reddit apportent du trafic référent. Les mentions sans lien ne sont pas un facteur de ranking direct.

Il y a aussi un effet de second tour : quand un thread ranke, des médias le reprennent. Et créent des liens dofollow vers les sites mentionnés.

---

## 2. Reddit dans les moteurs génératifs

### Parts de citation

Peec AI (30 M de sources, mars 2026) : Reddit n°1 sur Gemini et Perplexity. N°2 sur Google AI Mode, AI Overviews et ChatGPT.

Semrush (230 000 prompts, 100 M de citations, juillet-octobre 2025) : Reddit n°2 sur ChatGPT après septembre. Top 5 stable sur Google AI Mode et Perplexity.

Evertune (200 M+ de prompts, fin 2025-début 2026) : Reddit domaine le plus cité sur Perplexity, cinq mois consécutifs. Des pics au-delà de 20 %. D'autres mesures montent à 46-47 %.

AI Overviews : ~21 % des citations selon plusieurs analyses.

À pondérer : ces pourcentages sont volatils.

La part de Reddit dans les citations ChatGPT est passée de ~60 % à ~10 % entre début août et mi-septembre 2025 (Semrush).

Une mesure donne Gemini à 0,1 %. Une autre le classe n°1.

Ne sors jamais un chiffre de citation sans l'étude, la fenêtre et la date.

Ce qui est robuste : Reddit est n°1 ou n°2 partout. Au maximum sur Perplexity. Fort sur les AI Overviews. Instable sur ChatGPT.

### Pourquoi les IA citent autant Reddit

**La densité d'entités.** Le texte cité par les LLM affiche ~20 % de densité d'entités. Un texte standard : 5 à 8 %. Les posts Reddit sont remplis de noms d'outils, de versions, de prix, de chiffres.

**L'expérience first-hand.** Des praticiens racontent comment ils ont résolu un problème précis. C'est la catégorie de contenu visée par l'update hidden gems.

**La validation communautaire.** Les votes et la contradiction publique servent de couche de vérification pour les modèles.

### Contrats de données

Google : ~60 M$/an (février 2024, CBS, Fortune).

OpenAI : accès au contenu temps réel, ~70 M$/an estimés (mai 2024, Search Engine Land).

Reddit est un flux de données payé. Pas un domaine crawlé parmi d'autres.

Deux points de vigilance en 2026. Le contrat Google est en renégociation. Et le procès Reddit v. Perplexity (octobre 2025, en cours) peut modifier l'accès de Perplexity.

### Les formats que les IA citent

Les cinq formats les plus cités (Discovered Labs) :

- la question-réponse directe
- le comparatif « versus »
- le troubleshooting et les how-to
- le débat prix avec montants concrets
- l'avis équilibré pour/contre

Un avis qui liste des défauts est plus repris qu'un avis 100 % positif.

Les données Semrush (248 000 URLs citées, octobre 2025) donnent les ordres de grandeur :

- 80 % des posts cités ont moins de 20 upvotes (médiane 5-8)
- 70 % ont moins de 20 commentaires
- les threads Q&A représentent plus de 50 % des citations
- la longueur médiane d'un commentaire cité : ~80 mots

Il n'existe pas de seuil d'upvotes.

Côté compte, il faut de l'ancienneté, de la réputation, des réponses réparties sur plusieurs threads, une terminologie cohérente dans la durée.

La répétition d'une même recommandation dans des threads différents pèse plus qu'un score élevé dans un seul thread (Conbersa).

Le consensus des études : 60 à 90 jours avant un effet mesurable. 120 en borne haute.

Perplexity reprend un commentaire nouveau en 24 h à 7 jours.

Trois interdits : l'astroturfing, les faux comptes, les faux avis. Les communautés les repèrent. Le dommage est durable.

### Écrire comme une documentation

Les moteurs reprennent un texte formulé comme une source de référence.

Tu donnes des définitions, des données vérifiables, des étapes numérotées.

Sans « je pense ». Sans « à mon avis ».

(Reddit GEO Playbook, Medium, mai 2026, recoupé sur plusieurs guides 2026.)

### Fraîcheur (corrigé 2026-07-02)

Les vieux threads continuent d'être cités pendant des années.

L'âge moyen des discussions reprises par les IA : ~900 jours (Semrush).

Inutile donc de réécrire tes réponses tous les 90 jours. Ce chiffre vient d'une seule source Medium.

La bonne tactique :

- retourne sur les discussions où tu as déjà contribué et ajoute un nouveau commentaire
- mets l'année en cours dans les titres quand c'est pertinent
- contrôle chaque mois que tes threads les plus cités n'ont pas bougé

Des mesures donnent un taux de citation AI Overviews plus élevé pour les pages portant l'année en cours. Sources à intérêt commercial, non confirmées.

### Citations négatives

Les IA citent aussi les critiques.

Une mesure donne des taux proches : ~5 % pour le positif, ~6,1 % pour le négatif (AuthorityTech, 2026, source à intérêt commercial).

Un thread négatif visible peut orienter durablement la façon dont une IA présente un site.

C'est pour ça que la routine inclut une veille sur tes propres mentions.

---

## 3. Politique d'autopromo de Reddit

La doctrine officielle tient en une phrase : « C'est parfaitement OK d'être un Redditor qui a un site web. Ce n'est pas OK d'être un site web qui a un compte Reddit. »

En pratique, tu contribues d'abord. La promotion vient ensuite.

Le ratio de référence : ~90 % de contribution pour 10 % d'autopromo maximum. 95/5 en pratique prudente (§6).

Ton statut de consultant SEO reste en arrière-plan. Il n'est jamais le sujet d'un post.

---

## 4. Programme de lancement d'un compte (jour 1 à jour 30)

Reddit filtre les comptes neufs automatiquement. Sur deux critères.

**L'ancienneté.** Chaque sub fixe son seuil : de 1 à 30 jours. Le standard courant : 7 jours minimum. Les subs exigeants : 30 jours.

**La réputation.** Reddit tient deux compteurs : un pour les commentaires, un pour les posts. L'échelle est logarithmique : un post à 1 000 upvotes peut ne rapporter que ~500 points. La réputation liée aux commentaires monte plus vite. Les seuils anti-spam typiques : de 10 à plus de 100 points combinés. Sous le seuil, l'AutoModerator supprime le post sans intervention humaine.

Le lancement suit quatre phases. Chacune a un critère de passage. Tu ne passes pas à la suivante tant qu'il n'est pas rempli.

### Phase 0 : la préparation (jour 1, environ 1 heure)

- Crée le compte avec un pseudo crédible de particulier. Pas de nom de société, pas de mot-clé métier.
- Complète le profil : un avatar, une bio d'une ligne. Sans lien, sans pitch.
- Utilise une connexion propre. Pas de VPN datacenter, pas d'IP qui a déjà porté des comptes sanctionnés.
- Abonne-toi à 10-15 subs : tes cibles plus quelques généralistes. Le feed doit ressembler à celui d'un utilisateur réel.
- Ne poste rien le jour 1. Ne commente rien.

### Phase 1 : l'observation (jours 2 à 7)

- Lis 15 minutes par jour. Trie chaque sub cible par « Top, ce mois-ci ». Note ce qui marche : formats, longueur, ton.
- Lis les règles et la wiki de chaque sub. Relève trois choses : le seuil de réputation ou d'âge, la politique d'autopromo, le jour dédié à la promo s'il existe.
- Construis tes deux listes de travail : 8 à 12 subs cibles, 20 à 30 mots-clés de douleur (§7bis).
- Vote sur ce que tu lis. C'est l'activité passive d'un compte normal.
- À partir du jour 4, tu peux poser 1 à 2 commentaires par jour. Sur des questions simples où ta réponse est incontestable.

**Critère de passage :** les règles des 8-12 subs sont lues et notées. Les deux listes existent.

### Phase 2 : les premiers commentaires (jours 8 à 14)

- Écris 2 à 3 commentaires utiles par jour. C'est le consensus des guides pour un compte neuf. Commence par les subs à seuil bas.
- Vise les questions de ta niche où une réponse concrète manque. C'est ce qui monte la réputation le plus vite, avec le moins de risque.
- Espace tes actions d'au moins 10 à 15 minutes. C'est la limite technique des comptes à faible réputation.
- Réponds à toute personne qui répond à tes commentaires.
- Zéro lien. Zéro mention de ton site. Zéro post.

**Critère de passage :** 50 à 100 points de réputation combinés. Aucune suppression par l'AutoModerator.

### Phase 3 : la montée (jours 15 à 30)

- Passe à 3 à 5 commentaires par jour, progressivement.
- Élargis aux subs exigeants dès que l'âge du compte franchit leurs seuils.
- Vise 30 à 60 commentaires cumulés à la fin du mois, répartis sur 3 à 6 subs.
- En fin de phase, tu peux publier un premier post sans lien. Une question ou un retour d'expérience, dans le sub où ta réputation est la plus établie.
- Vers le jour 21, fais un check shadowban : profil ouvert en navigation privée déconnecté (§10).

**Critère de sortie :** 30 jours d'ancienneté, 200 points de réputation ou plus, aucune suppression récente.

Le compte est opérationnel. La routine quotidienne prend le relais : 4 à 6 commentaires par jour. Le protocole du §7bis s'applique.

### Pendant les 30 premiers jours, évite absolument

- Aucun lien externe. Vers ton site ou un autre.
- Aucune mention de ton produit ou de ton activité.
- Aucun cross-post, aucun repost.
- Aucun achat d'upvotes, aucun échange de votes.
- Un seul compte. Plusieurs comptes sur une même IP, c'est un pattern que Reddit sanctionne (§10).

---

## 5. Sélection des subreddits

Pour trouver les bons subreddits, commence par la recherche Reddit avec le filtre « Communities ».

Puis regarde Subreddit Stats (activité, croissance), SnoopSnoo (démographie, parfois indisponible) et Redditlist.

Ce qui compte, c'est l'engagement. Pas la taille.

Un sub de 15 000 membres avec des discussions actives produit plus qu'un sub de 500 000 inactif.

Pour vérifier : trie par « Top, ce mois-ci ». Lis chaque sub candidat pendant une semaine avant d'y écrire.

Chaque sub a ses règles locales, dans la sidebar ou un post épinglé. Certains interdisent toute activité commerciale. D'autres imposent un seuil de réputation ou d'âge. D'autres réservent l'autopromo à un jour dédié.

Lis les règles et la wiki avant de poster.

---

## 6. Ratio d'autopromo : état de la règle

Pendant longtemps, Reddit recommandait un ratio de 9 contributions pour 1 publication promotionnelle.

La règle a été retirée du Reddiquette formel. Remplacée par le principe du « participant authentique », apprécié par les mods sur le comportement global.

Ce qui reste opposable aujourd'hui, c'est la Content Policy.

Le spam y est défini comme des actions « répétées, non désirées ou non sollicitées ». La manipulation comme « toute tentative de manipuler le vote ou les systèmes de Reddit ».

Depuis 2023, le Contributor Quality Score (CQS) filtre en plus les comptes de faible qualité. Sur des signaux comportementaux, indépendamment de tout ratio.

Le test est simple : si ton historique se résume à des liens vers un même site, tu corresponds au profil sanctionné.

En pratique, vise 95/5.

---

## 7. Formats de contribution

Sur Reddit, le ton est à l'opposé du marketing traditionnel. Il faut adopter les codes de la communauté, éviter le jargon corporate et apporter de la valeur avant tout.

**Les commentaires utiles**

C'est le format le plus important. Répondre en profondeur à de vraies questions, partager son expérience et aider sans chercher à vendre. C'est ce qui construit durablement la crédibilité d'un compte.

**Les données originales**

Le format le plus adapté pour une entreprise. Partager des données propriétaires anonymisées (logs Fusionn, données Google Search Console, études de CTR, etc.) apporte une information vérifiable et difficile à reproduire, sans tomber dans l'autopromotion.

**Les guides, TIL (Today I Learned) et réponses détaillées**

Des contenus pédagogiques qui répondent directement à un problème, sans appel à l'action ni lien commercial. L'objectif est d'être utile, pas de générer du trafic.

**Les AMA (Ask Me Anything)**

Ce format ne fonctionne que s'il est authentique : une personne identifiable, des réponses détaillées et la volonté d'aborder aussi les questions difficiles. Les échecs sont nombreux lorsque les entreprises tentent de contrôler la conversation, comme l'AMA de Nissan, souvent cité parmi les exemples à ne pas reproduire.

Enfin, un chiffre montre bien l'état d'esprit de la plateforme : selon Reddit, 81 % des utilisateurs sont ouverts aux échanges avec les entreprises, et 59 % attendent d'elles qu'elles écoutent réellement les retours de la communauté. L'authenticité reste toutefois la condition indispensable pour être bien perçu.

---

## 7bis. Protocoles d'exécution

### Protocole d'activation (commentaire)

- Établis une liste de 8 à 12 subreddits avec le prompt 8 (subreddit mapping, §9bis), et de 20 à 30 mots-clés de douleur (« best CRM for solopreneur », « [catégorie] alternatives »).
- Monitore avec Reddit Search et F5Bot (gratuit, 200 mots-clés maximum).
- Pars d'un compte de plus de 30 jours avec 200 à 500 points de réputation.
- Structure chaque réponse ainsi : 3 à 5 conseils concrets, ton expérience personnelle, puis la mention avec disclosure (« une option que j'utilise moi-même est X ») si elle est légitime.
- Propose un DM si le sub l'autorise, et tracke la source « Reddit » en CRM (UTM).
- Réponds à tous les commentaires et DM sous 48 h.
- Tiens la cadence de 4 à 6 commentaires par jour, plafond 8. Jamais en rafale : 20 commentaires dans l'heure, c'est le pattern spam typique.

### Protocole de post

- Étudie les 10 meilleurs posts du sub avant d'écrire (format, longueur, ton).
- Mets 50 à 80 % de valeur directe dans le post : captures, métriques, échecs assumés.
- Utilise les titres qui rankent (Ross Simmonds, guides 2026) : « J'ai [fait X] pendant [période], voici ce qui a marché », « How to [objectif] in [secteur] », « We tested 5 [outils] », « Best [outil] for [cas d'usage] ». La méthode Simmonds ajoute un TL;DR en tête, des enseignements concrets et une question ouverte en fin.
- Poste en matinée ET en semaine, environ 6-10 h ET. L'étude Upvote.net porte sur 150 posts et vient d'un vendeur d'upvotes ; la fenêtre est corroborée par Foundation, RecurPost et Single Grain. Foundation ajoute le samedi matin.
- Joue la première heure : la pondération des votes est logarithmique, les 10 premiers upvotes pèsent comme les 100 suivants. Les 6-10 premières heures conditionnent le ranking Google du thread. Le « 30 premières minutes » ne venait que de vendeurs d'upvotes.
- Publie d'abord dans ton sub principal, réponds sous 2 h, puis traite 100 % des commentaires pendant 24-48 h.
- Cross-poste vers 3-4 subs pertinents maximum par contenu, espacés de 6 h et sur des jours différents. Cinq subs ou plus en rafale, c'est le pattern de spam.

### Repurposing d'un article

Résume les idées principales. Supprime le remplissage. Garde les enseignements actionnables.

Le lien se place en ressource complémentaire, jamais au centre du post.

Un exemple chiffré de Ross Simmonds : un thread positionné sur une requête « [produit] alternative » a généré ~1 300 visiteurs par mois. La page concurrente : ~330. Près de 4 fois plus.

---

## 8. Threads positionnés sur Google

Un thread dont le titre reprend une vraie requête Google profite directement de l'autorité de reddit.com.

C'est ce qui lui permet de se positionner rapidement dans le top 10.

Trois tactiques reviennent dans la plupart des études (Ross Simmonds en tête) :

- le titre reprend la formulation de la requête : « What's the best… », « Has anyone tried… », « How do I… »
- la réponse complète est dans le corps du post
- les commentaires actifs soutiennent le ranking, donc tu entretiens la discussion dans la durée

Le risque à connaître : la politique Google « site reputation abuse » (mars 2024, renforcée le 19 novembre 2024).

Elle vise les sous-dossiers loués chez les éditeurs. Pas les forums UGC.

Reddit modère de son côté les patterns d'abus. Typiquement : des comptes récents qui poussent les mêmes offres dans des threads de recommandation.

La ligne est claire. Un thread construit pour répondre, dont le titre reprend une requête : aucun risque. Un thread construit uniquement pour ranker : modéré.

Dernier point, vérifié le 2 juillet 2026 : Perplexity source Reddit via les SERP Google (procès Reddit v. Perplexity, test honeypot).

Un commentaire dans un thread déjà positionné apparaît donc dans Perplexity en quelques jours.

C'est le levier GEO le plus rentable documenté à ce jour.

---

## 9. Extraction d'insights

Aucun risque ici : tu ne postes rien.

**GummySearch** classe les conversations d'une niche en Pain Points, Solution Requests, Money Talk et Hot Discussions.

**Keyworddit** (gratuit) extrait les termes fréquents d'un subreddit, avec un volume Google estimé.

**L'opérateur `site:reddit.com`** fait remonter les threads déjà positionnés sur une requête, et les questions récurrentes.

La méthode est simple :

- identifie les subreddits de ta niche
- récupère les mots-clés avec Keyworddit
- creuse les conversations avec GummySearch ou la recherche native
- isole les pain points qui reviennent le plus

Les expressions à charge émotionnelle signalent les douleurs exploitables. « Je déteste vraiment ». « J'ai désespérément besoin de ».

Le tout alimente le process besoin → mot-clé → cluster.

X.com complète Reddit. La recherche en mode expert sort des signaux équivalents (compte premium, ~5 €/mois). Même traitement.

Contrainte technique : Reddit bloque le crawler. Tu colles les posts à la main, ou tu passes par les flux RSS publics (la méthode du cockpit).

---

## 9bis. Les 8 prompts : trouver les sujets de la niche dans les questions Reddit

Ces huit prompts sortent les sujets de ta niche des questions que les gens posent sur Reddit.

Ils s'exécutent dans une IA avec recherche web.

Tu remplaces `[THÉMATIQUE]`, `[SUJET]` ou `[PRODUIT]` par un mot-clé business de ta roadmap. Jamais par un mot-clé inventé.

Si le mot-clé n'est pas dans ta roadmap, ce n'est pas une publication Reddit. C'est du bruit.

Chaque extraction garde les permalinks Reddit et les verbatims bruts, sans reformulation.

Le prompt 3 est le plus rentable : il identifie à la fois un thread où publier une réponse experte et un angle pour un article pilier sur le site.

### Prompt 1 : les pain points

> Trouve sur Reddit (site:reddit.com) les 20 threads les plus upvotés sur [THÉMATIQUE] des 12 derniers mois. Pour chaque thread, extrais : URL + subreddit + nombre d'upvotes, titre du post, le pain point exact en 1 phrase, le verbatim le plus fort (citation textuelle). Classe par fréquence du pain point.

### Prompt 2 : pourquoi ils n'achètent pas

> Trouve sur Reddit les commentaires où des utilisateurs expriment de la déception, de la méfiance ou un refus d'acheter [PRODUIT/SERVICE]. Extrais : le verbatim brut (pas de reformulation), l'objection sous-jacente (prix, qualité, confiance, complexité, ROI…), le subreddit + permalink. Regroupe les objections par thème et donne-moi le top 5 par volume.

### Prompt 3 : les questions populaires mal traitées

> Liste sur Reddit les questions sur [SUJET] qui ont 0 à 2 réponses mais plus de 10 upvotes ou plus de 20 commentaires sur le thread. Ce sont des intentions de recherche mal servies. Format : question textuelle + URL + nombre de vues/upvotes + pourquoi c'est mal répondu.

### Prompt 4 : les expressions de tes futurs users

> Analyse 30 threads Reddit sur [THÉMATIQUE] et extrais : les expressions familières et le jargon utilisés par les users (différent du vocabulaire marketing), les termes péjoratifs employés pour parler de la catégorie, les images récurrentes. Donne-moi une liste de 20 expressions avec un exemple de phrase citée.

### Prompt 5 : les avant/après

> Sur Reddit, trouve des témoignages utilisateurs décrivant une transformation liée à [PROBLÈME/SOLUTION]. Extrais la structure : situation avant (avec verbatim), déclencheur du changement, action prise, résultat après (avec chiffres si mentionnés). Filtre : minimum 50 upvotes sur le commentaire ou le post.

### Prompt 6 : les opinions contre-intuitives qui font débat

> Cherche sur Reddit les opinions contre-intuitives ou controversées sur [SUJET] : posts avec titre « unpopular opinion », « hot take », ou commentaires à ratio élevé (beaucoup de réponses). Pour chaque : la thèse contre-intuitive, l'argument principal, le contre-argument majoritaire. C'est la matière première de tes inversions expertes.

### Prompt 7 : les comparaisons (requêtes VS)

> Sur Reddit, trouve tous les threads où les utilisateurs comparent spontanément [OUTIL A] à [OUTIL B, C, D…]. Extrais : le critère de comparaison (prix, ergonomie, support, features…), le vainqueur selon le consensus des commentaires, les verbatims justifiant le choix. Classe les critères par fréquence d'apparition.

### Prompt 8 : le subreddit mapping

> Pour la thématique [X], liste-moi les 10 subreddits les plus actifs avec : nombre de membres, volume de posts par semaine, les 3 tags/flairs les plus utilisés, le type d'intention dominant (question, avis, rant, showcase, recommandation).

Chaque sortie alimente les deux côtés du système.

Côté Reddit : le prompt 3 donne le thread où répondre, le prompt 8 donne le sub prioritaire.

Côté site : le prompt 4 calibre le vocabulaire des pages, le prompt 7 donne les pages comparatif, le prompt 5 donne les cas clients.

---

## 10. Shadowban : définition et déclencheurs

Un shadowban rend ton contenu visible pour toi, invisible pour les autres.

En 2026, il est majoritairement automatique.

Ce qui le déclenche :

- le même lien posté dans plusieurs subreddits, même pertinent partout
- le même commentaire répété, même reformulé a minima (déclencheur n°1 selon RedShip, 2026)
- une cadence anormale : compte récent très actif, rafales (limite technique : ~1 action toutes les 10-15 minutes quand la réputation est basse dans un sub)
- des posts répétés vers un même domaine, surtout s'il est récent
- une IP liée à des comptes spam
- la manipulation de vote sous toutes ses formes : demander des upvotes, multi-comptes, échanges de votes, brigading inclus
- les reposts de contenu déjà publié
- les raccourcisseurs de liens (bit.ly, t.co), flaggés automatiquement

Pour le détecter : ouvre ton profil en navigation privée, déconnecté.

Une page introuvable ou des posts invisibles signalent un shadowban probable.

Le lien direct d'un commentaire récent ouvert en privé donne la même information.

Des posts récents à zéro vote et des commentaires sans réponse : un signal indirect.

Les outils dédiés : Reddit shadowban checker, redship, banchecker.

Le cas le plus fréquent reste le compte neuf qui poste des recommandations produit. C'est le premier signal que surveillent les mods.

---

## 11. Modération

Chaque sub est géré par des mods bénévoles. Ils appliquent leurs propres règles.

Tu les contactes par modmail (« Message the mods » dans la sidebar). Pas par DM.

Pour un consultant, le bon réflexe : demander avant de poster un contenu lié à ton activité. « Est-ce autorisé de partager une étude que j'ai faite sur X ? »

L'AutoModerator est un bot configurable par sub. Il supprime ou flaire par domaine ou mot-clé. Il applique les seuils de réputation et d'âge. Il répond automatiquement.

C'est lui qui supprime les posts sous seuil, sans intervention humaine.

C'est exactement pour ça que la phase de rodage existe (§4).

---

## 12. Marché francophone

Côté France : ~20,6 M d'utilisateurs estimés (Influencia). +72 % de visiteurs mensuels en un an (Médiamétrie). Une entrée dans le top 10 des réseaux sociaux français.

Abondance donnait 10,4 M de visiteurs mensuels à mi-2025. Une audience doublée en un an.

Deux causes : la traduction automatique du corpus en français, et l'indexation prioritaire depuis l'accord Google.

Côté communautés : il n'existe pas de sub SEO francophone actif. Pas de r/SEO_fr ni de r/referencement vivants.

Les SEO français échangent sur r/SEO et r/bigseo (anglophones), sur LinkedIn, sur X et sur WebRankInfo.

Les gros subs FR se limitent à r/france (2,5 M+) et à une longue traîne : r/AskFrance, r/vosfinances, r/conseiljuridique, r/Cuisine. Les counts précis hors r/france ne sont pas publiés.

Lefebvre Dalloz (juillet 2025) classe Reddit « canal secondaire ou de veille dans un contexte francophone ».

Une limite à connaître : personne n'a publié de donnée chiffrée comparant la visibilité SERP de Reddit sur Google.fr et Google.com. Les affirmations « Reddit domine les SERP françaises » circulent sans étude à l'appui.

Un point important (Peec AI, 64,77 M de citations Reddit, mars-juin 2026) : les pages Reddit auto-traduites (`?tl=`) représentent 40 à 73 % des citations Reddit sur les surfaces IA de Google, dans les marchés non anglophones d'Europe.

Le détail par pays : plus de 70 % en Suède et en Norvège. 72 % en Espagne sur AI Mode. 52 % en Allemagne sur les AIO. La France n'est pas isolée dans l'étude, mais le pattern est pan-européen.

ChatGPT suit la pente inverse. Il a quasi cessé de citer les pages traduites : de 6,14 % à 0,30 % entre avril et juin 2026.

Ce que ça change :

1. Pour le GEO, les subs anglophones de la niche search/IA sont le terrain principal. Tes réponses en anglais sont citées, y compris via les pages traduites sur les requêtes françaises côté Google.
2. Pour le SEO francophone, reste opportuniste. Repère avec `site:reddit.com` les requêtes FR où un thread ranke. Positionne-toi au cas par cas.
3. Aucun retour d'expérience FR mesuré n'est publié. Le test Qadence produit cette donnée.

---

## 13. Plan 90 jours

**Jours 1 à 30 : le lancement du compte.**

Tu déroules le programme de la section 4, phase par phase : préparation, observation, premiers commentaires, montée.

Les subs cibles sont anglophones search/IA/growth en priorité, plus 2 à 3 FR.

En parallèle, tu poses les alertes de mentions sur les sites suivis.

À la fin du mois, le compte est opérationnel : 30 jours, 200 points de réputation ou plus.

**Semaines 5-8 : contribution et insights.**

Monte à 20-30 commentaires de qualité par semaine.

Lance le travail d'insights (Keyworddit, GummySearch). Fais redescendre les pain points dans le process besoin → mot-clé → cluster.

Publie le premier post à valeur : une donnée originale anonymisée, dans le sub où le capital est le plus élevé.

Le ratio 95/5 se tient sur toute la période.

**Semaines 9-11 : threads et GEO.**

Publie des posts dont le titre correspond à une requête réelle. Entretiens la discussion.

Interviens dans les threads décisionnels « best X for Y » et les comparatifs. Nomme le site quand c'est légitime.

Demande l'accord des mods en modmail avant tout post limite.

**Semaines 12-13 : la mesure.**

Vérifie les positions via `site:reddit.com`.

Cherche les citations dans Perplexity et ChatGPT sur la liste fixe de requêtes.

Arrête ce qui ne produit pas.

Le bilan porte sur trois points : les threads positionnés, les mentions dans les IA, les insights convertis en contenu publié.

Le délai GEO reste de 60 à 90 jours avant un effet mesurable. 120 en borne haute. Le plan pose les fondations ; les citations arrivent en général après.

---

## 14. Métriques

Six chiffres à suivre. Chacun répond à une question précise.

**1. La santé du compte.**

Tu relèves la réputation (commentaires + posts) et l'âge du compte.

Question : est-ce que je peux encore poster partout ? Sous les seuils des subs, rien d'autre ne compte.

**2. Les positions Google de tes threads.**

Tu tapes `site:reddit.com` suivi de ta requête dans Google. Tu notes quels threads où tu as contribué apparaissent, et à quelle position.

Question : mes threads rankent-ils sur mes requêtes acheteur ?

**3. Les citations IA. La métrique principale en 2026.**

Tu prends ta liste fixe de 15 à 20 requêtes acheteur (« best AI SEO tool », « Qadence alternatives »...).

Tu les tapes une par une dans Perplexity, ChatGPT et Google (AI Overviews).

Tu comptes combien de réponses citent Qadence.io ou un de tes sites.

La liste ne change pas d'une semaine à l'autre : c'est ce qui rend la mesure comparable.

Question : les IA me recommandent-elles, et de plus en plus ?

**4. Les mentions entrantes.**

Tu comptes les alertes reçues dans la semaine : combien de fois quelqu'un a cité tes sites ou ton nom sur Reddit, et sur quel ton (positif, neutre, négatif).

Question : est-ce qu'on parle de moi sans que je le provoque ?

**5. Les insights convertis.**

Tu comptes les pain points trouvés sur Reddit qui sont devenus une page ou un cluster publié sur tes sites.

Question : est-ce que Reddit nourrit mon contenu, même sans citation ?

**6. Le trafic référent.**

Tu regardes dans GA ou la GSC les visites qui arrivent depuis reddit.com.

Attends-toi à peu : les liens sont en nofollow et ce n'est pas l'objectif. C'est un bonus, pas un indicateur de réussite.

---

## Sources (audit web, juin 2026)

**Reddit et Google (visibilité, deal, mécanisme) :**
- [Amsive - Reddit's SEO growth deep dive](https://www.amsive.com/insights/seo/reddits-seo-growth-a-deep-dive-into-reddits-recent-surge-in-seo-visibility/)
- [GSQI (Glenn Gabe) - Hidden Gems update, forums surge](https://www.gsqi.com/marketing-blog/beyond-reddit-and-quora-google-hidden-gems-update-forums-surge/)
- [Sistrix - Google's unusual relationship with Reddit](https://www.sistrix.com/blog/googles-unusual-special-relationship-with-reddit/)
- [CBS News - Google-Reddit 60M deal](https://www.cbsnews.com/news/google-reddit-60-million-deal-ai-training/)
- [Fortune - Reddit IPO Google data deal](https://fortune.com/2024/02/23/reddit-ipo-google-api-data-deal/)
- [StanVentures - August 2024 update boosts Reddit](https://www.stanventures.com/news/googles-august-2024-update-boosts-reddit-688/)
- [DAC Group - Is Reddit's time up on the SERP](https://www.dacgroup.com/insights/blog/search-optimization/is-reddits-time-up-on-the-serp/)
- [Amsive - December 2025 core update winners losers](https://www.amsive.com/insights/seo/googles-december-2025-core-update-winners-losers-analysis/)
- [Odd Angles Media - Reddit backlinks nofollow value](https://odd-angles-media.com/blog/reddit-backlinks-seo-value-strategy-and-link-building-guide)

**Reddit et IA (citations, GEO, deals) :**
- [Peec AI - Top domains cited by AI search (30M sources)](https://peec.ai/blog/top-domains-cited-by-ai-search-analysis-based-on-30m-sources)
- [Peec AI - Reddit machine-translated pages AI visibility (64,77M citations)](https://peec.ai/blog/reddit-machine-translated-pages-ai-visibility)
- [Semrush - Most-cited domains in AI](https://www.semrush.com/blog/most-cited-domains-ai/)
- [Semrush - Reddit AI search visibility study (248k URLs)](https://www.semrush.com/blog/reddit-ai-search-visibility-study/)
- [Evertune - Perplexity loves Reddit](https://www.evertune.ai/resources/insights-on-ai/perplexity-loves-reddit-exploring-llms-top-sources)
- [Discovered Labs - Reddit content types LLMs cite most](https://discoveredlabs.com/blog/the-reddit-content-types-that-llms-cite-most-data-backed-breakdown)
- [Salespeak - Reddit UGC and AI search](https://salespeak.ai/aeo-news/reddit-ugc-ai-search)
- [TechCrunch - OpenAI deal to train on Reddit data](https://techcrunch.com/2024/05/16/openai-inks-deal-to-train-ai-on-reddit-data/)
- [Search Engine Land - OpenAI may pay Reddit 70M](https://searchengineland.com/openai-may-pay-reddit-70m-for-licensing-deal-451882)
- [Search Engine Land - AI engines cite Reddit YouTube LinkedIn most](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)
- [Search Engine Land - Reddit sues Perplexity, SerpApi (sourcing via Google SERPs)](https://searchengineland.com/reddit-sues-perplexity-serpapi-scraping-google-463681)
- [Weird Marketing Tales - Why people add reddit to searches](https://weirdmarketingtales.com/why-people-are-adding-reddit-to-their-google-searches/)

**Participation, règles, ban, modération :**
- [KarmaGuy - Reddit self-promotion rules 2026](https://karmaguy.io/en/blog/reddit-self-promotion-rules)
- [Vadim Kravcenko - Self-promotion on Reddit the right way](https://vadimkravcenko.com/qa/self-promotion-on-reddit-the-right-way/)
- [Reddit Help - Disrupting communities (vote manipulation)](https://support.reddithelp.com/hc/en-us/articles/360043066412-Disrupting-Communities)
- [Multilogin - Reddit shadowban check 2026](https://multilogin.com/blog/is-your-reddit-account-shadowbanned/)
- [LaunchKit - seuils d'âge et de réputation des comptes Reddit](https://launchkit.me/blog/reddit-account-karma-requirements/)
- [SubredditSignals - Find relevant subreddits 2025](https://www.subredditsignals.com/blog/how-to-find-relevant-subreddits-for-my-business-a-2025-guide)
- [Reddit Help - Contact moderators](https://support.reddithelp.com/hc/en-us/articles/360043043792-How-do-I-contact-the-moderators-of-a-community)
- [Reddit Help - Automoderator](https://support.reddithelp.com/hc/en-us/articles/15484574206484-Automoderator)
- [Search Engine Journal - Brand fails on Reddit AMAs](https://www.searchenginejournal.com/brands-failed-hard-reddit-amas-can-learn/169693/)

**Stratégies, parasite SEO, outils, cas :**
- [Google - Site reputation abuse policy](https://developers.google.com/search/blog/2024/11/site-reputation-abuse)
- [Ross Simmonds - Reddit SEO](https://rosssimmonds.com/blog/reddit-seo/)
- [Karmic - Reddit SEO](https://www.withkarmic.com/blog/reddit-seo)
- [Semrush - Reddit keyword research](https://www.semrush.com/blog/reddit-keyword-research/)
- [GummySearch](https://gummysearch.com/product/)
- [F5Bot](https://f5bot.com/)
- [HackTheAlgo - Reddit SEO strategy for B2B](https://www.hackthealgo.com/p/my-reddit-seo-strategy-for-b2b-brands)
- [Search Engine Journal - Branded search patent (implied links)](https://www.searchenginejournal.com/googles-branded-search-patent-for-ranking-search-results/524083/)

**Conseils praticiens, timing, GEO (audit web, juin 2026) :**
- [SubredditSignals - Reddit SEO 2026, vrais facteurs de ranking](https://www.subredditsignals.com/blog/reddit-seo-in-2026-the-real-ranking-factors-behind-google-visible-threads-and-how-to-spot-winners-before-everyone-else)
- [Upvote.net - étude 150 posts (timing et vélocité d'upvotes)](https://upvote.net/blog/best-time-to-post-on-reddit)
- [Reddit GEO Playbook - Medium (mai 2026)](https://medium.com/@tentenco/reddit-geo-playbook-how-to-get-cited-by-chatgpt-and-perplexity-in-2026-75607d1d2b01)
- [AuthorityTech - Reddit pour les citations Perplexity 2026](https://authoritytech.io/blog/reddit-perplexity-geo-strategy-2026)
- [Redship - éviter le ban marketing sur Reddit 2026](https://redship.io/learn/how-to-avoid-getting-banned-marketing-reddit)

**Reddit francophone :**
- [Influencia - Reddit thermomètre éditorial France](https://www.influencia.net/reddit-le-reseau-social-et-veritable-thermometre-editorial-que-la-france-na-pas-vu-venir-et-quil-va-falloir-serieusement-prendre-en-compte/)
- [Abondance - ChatGPT, Reddit, X et le futur du trafic SEO](https://www.abondance.com/20250701-1253913-chatgpt-reddit-x-chamboulement-des-audiences-et-futur-du-trafic-seo.html)
- [Lefebvre Dalloz - Reddit, un levier sous-estimé pour le SEO et l'IA ?](https://formation.lefebvre-dalloz.fr/actualite/reddit-un-levier-sous-estime-pour-le-seo-et-lia)
- [Nicolas Deroualle - Guide stratégie SEO sur Reddit](https://nicolas-deroualle.com/blog/reddit-seo-utilisation-strategie-referencement-naturel)
- [Journal du Net - Les meilleurs parasites SEO en 2026](https://www.journaldunet.com/seo/1548681-les-meilleurs-parasites-seo-en-2026-reddit-linkedin-et-les-plateformes-ou-se-positionner/)
- [Ahrefs FR - SEO Reddit guide en 5 étapes](https://ahrefs.com/blog/fr/seo-reddit-guide/)
- [Sherpas - Top 7 subreddits français](https://sherpas.com/blog/subreddit-francais/)
