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

> Deux résultats visés, mesurables : des citations dans les moteurs génératifs (GEO) et des positions Google via des threads qui rankent. Cadrage : 2026-06-18. Chiffres d'exécution vérifiés contre ~25 sources le 2026-07-02. Les chiffres fragiles sont signalés comme tels.

---

## En résumé (à lire en premier)

Reddit est passé du 68e rang au top 5 des domaines les plus visibles sur Google US entre juillet 2023 et juillet 2024. Indice Sistrix : de 95,1 à 1 370 points, +1 328 % (Sistrix via Amsive, 2024). Trois causes documentées, cumulées : l'update « hidden gems » déployée à l'automne 2023, le filtre « Discussions and forums » dans les résultats, l'accord de licence de données Google-Reddit à ~60 M$/an signé en février 2024.

Sur les moteurs génératifs, Reddit est la source n°1 ou n°2 des citations selon toutes les études 2025-2026 (Peec AI, Semrush, Evertune, détail §2). Sur Perplexity : 20 à 47 % des citations selon l'étude et la période. Ces accès sont contractuels : Google ~60 M$/an, OpenAI ~70 M$/an estimés (mai 2024).

Quatre usages, dans l'ordre de rendement documenté :

1. **Citations IA** via des threads décisionnels où le site est nommé de façon authentique.
2. **Positions Google** via des threads dont le titre correspond à une requête réelle.
3. **Extraction d'insights** : pain points, verbatims, vocabulaire réel. Aucun risque de ban, rien n'est posté.
4. **Compte crédible** (âge, karma, historique de contributions). Prérequis des trois usages précédents.

Contrainte structurante : la politique anti-spam de Reddit. Doctrine officielle de la plateforme : « C'est OK d'être un Redditor qui a un site web, ce n'est pas OK d'être un site web qui a un compte Reddit. » Sanctions constatées : post supprimé, shadowban, bannissement.

France : ~20,6 M d'utilisateurs estimés (Influencia), +72 % de visiteurs mensuels sur un an (Médiamétrie), aucune communauté SEO francophone active. Le levier est plus faible en français qu'en anglais. Détail et conséquences en §12.

---

## Le test Qadence.io (terrain first-party)

Test lancé en juin 2026 sur Qadence.io. Aucune étude de cas Reddit indépendante avec trafic, positions et conversions vérifiables n'existe (voir note de fiabilité). Ce test produit cette donnée.

Objectifs mesurés : 1. citations de Qadence.io dans Perplexity, ChatGPT et AI Overviews ; 2. positions Google sur des mots-clés décisionnels (« outil IA », « agent SEO », « [catégorie] alternatives »).

État initial : compte ancien (premier post il y a un an), activité quasi nulle depuis. Deux règles de conduite : pas de spam, pas d'action ponctuelle sans suite. Délai attendu avant effet mesurable : 60 à 90 jours (§2). Point de coupe : bilan à J+45 (mi-août 2026) ; sans thread positionné, citation IA ni mention entrante, le test s'arrête.

---

## L'exécution : routine quotidienne + Reddit Cockpit (depuis 2026-07-02)

La couche d'exécution est dans le même dossier :

- **[[Routine-quotidienne]]** : les quotas (4-6 commentaires/jour plafond 8, 1 mention/semaine, 1 post/semaine plafond dur 3, bilan hebdo sur liste fixe de requêtes). Vérifiée contre ~25 sources le 2026-07-02. En cas de divergence avec ce document, la routine fait foi sur les chiffres d'exécution.
- **[[Journal]]** : suivi append-only. Une ligne par jour, un bloc par bilan hebdo.
- **Reddit Cockpit** (`~/Code/reddit-cockpit/`) : scrape RSS en lecture seule des subs cibles et des requêtes acheteur, chaque jour à 07h50, puis drafting automatique de 1-2 commentaires par thread retenu (anglais, 120-200 mots, quotas vérifiés contre le journal). Sortie : `queue/AAAA-MM-JJ.md`. La machine ne publie jamais, le clic reste manuel. Temps du bloc commentaires : ~10-12 min/jour.

---

## 1. Visibilité Google de Reddit, 2023-2026

### Croissance 2023-2024

Juillet 2023 : reddit.com est le 68e domaine le plus visible sur Google US. Juillet 2024 : top 5. Indice Sistrix : 95,1 → 1 370 points entre juillet 2023 et avril 2024, +1 328 % (Sistrix via Amsive). Trafic organique estimé : ~57 M → ~427 M de visites mensuelles sur la même période, +649 % (estimation Ahrefs via Amsive, pas une donnée Reddit).

Trois causes documentées :

- **Update « hidden gems »** (annoncée mai 2023, déployée dans les core updates d'octobre-novembre 2023) : remontée du contenu expérientiel et des forums. Mesure de Glenn Gabe sur 97 forums : 88 % ont gagné plus de 100 % de visibilité sur un an. Gain Reddit selon l'outil : +378 % (Semrush) à +978 % (Sistrix).
- **Filtre « Discussions and forums »** : zone dédiée aux forums dans les résultats, qui remonte Reddit sur les requêtes conversationnelles (« best X for Y », avis, troubleshooting).
- **Accord Google-Reddit** (février 2024, ~60 M$/an) : accès temps réel à l'API Reddit pour l'entraînement des modèles et les réponses. Google déclare le contrat distinct du classement organique. La corrélation temporelle avec l'explosion de visibilité est documentée par tous les outils ; la causalité directe ne l'est pas. La FTC a ouvert une enquête non publique sur ces licences en mars 2024.

### Correction 2025

À partir du 7 janvier 2025 : perte d'environ 350 points d'indice Sistrix, passage du 3e au 4e rang US. Les core updates 2025 (mars, juin, août, décembre) créent de la volatilité sur les sites communautaires (Reddit, Quora, Stack Exchange). Décembre 2025 : chute pendant le déploiement, retour au niveau antérieur dans la semaine suivante. Août 2025 : 2e rang US atteint brièvement, devant Amazon. Position structurelle : top 5 US, avec volatilité par paliers.

### Mécanisme de ranking (liens en nofollow)

Les liens sortants de Reddit sont en nofollow. Ils ne transmettent pas d'autorité au sens backlink. Une stratégie « backlinks Reddit » n'a pas de base technique.

Facteurs de ranking d'une page Reddit documentés : crawl quasi temps réel (facilité par l'accord de données), signaux d'engagement (temps passé, interactions), critère « expérience » de l'E-E-A-T (cible déclarée de l'update hidden gems). John Mueller (Google) : les liens Reddit apportent du trafic référent ; les mentions sans lien ne sont pas un facteur de ranking direct. Effet de second ordre constaté : un thread qui ranke est repris par des médias, qui créent des liens dofollow vers les sites mentionnés.

---

## 2. Reddit dans les moteurs génératifs

### Parts de citation

- Peec AI (30 M de sources, mars 2026) : Reddit n°1 des domaines cités sur Gemini et Perplexity, n°2 sur Google AI Mode, AI Overviews et ChatGPT.
- Semrush (230 000 prompts, 100 M de citations, juillet-octobre 2025) : Reddit n°2 sur ChatGPT après septembre, top 5 stable sur Google AI Mode et Perplexity.
- Evertune (200 M+ de prompts, fin 2025-début 2026) : Reddit domaine le plus cité sur Perplexity sur cinq mois consécutifs, pics au-delà de 20 %. D'autres mesures donnent 46-47 % des citations Perplexity.
- AI Overviews : ~21 % des citations selon plusieurs analyses.

À pondérer : ces pourcentages sont volatils. Part de Reddit dans les citations ChatGPT : ~60 % → ~10 % entre début août et mi-septembre 2025 (Semrush). Une mesure donne Gemini à 0,1 % quand une autre le donne n°1. Tout chiffre de citation se donne avec l'étude, la fenêtre et la date. Ordres de grandeur robustes : Reddit n°1 ou n°2 partout, maximum sur Perplexity, fort sur AI Overviews, instable sur ChatGPT.

### Facteurs explicatifs documentés

- **Densité d'entités.** Le texte cité par les LLM affiche ~20 % de densité d'entités, contre 5-8 % pour un texte standard. Les posts Reddit contiennent des noms d'outils, versions, prix, chiffres.
- **Expérience first-hand.** Récits de résolution de problèmes par des praticiens, catégorie de contenu visée par l'update hidden gems.
- **Validation communautaire.** Votes et contradiction publique servent de couche de vérification pour les modèles.

### Contrats de données

Google : ~60 M$/an (février 2024, CBS, Fortune). OpenAI : accès au contenu temps réel, ~70 M$/an estimés (mai 2024, Search Engine Land). Reddit est un flux de données payé, pas un domaine crawlé parmi d'autres. Point de vigilance 2026 : le contrat Google est en renégociation, et le procès Reddit v. Perplexity (octobre 2025, en cours) peut modifier l'accès de Perplexity.

### Formats cités et conditions

Les cinq formats de threads les plus cités par les IA (Discovered Labs) : question-réponse directe, comparatif « versus », troubleshooting/how-to, débat prix avec montants, avis équilibré pour/contre. Un avis qui liste des défauts est plus repris qu'un avis uniquement positif.

Données Semrush (248 000 URLs Reddit citées, octobre 2025) : 80 % des posts cités ont moins de 20 upvotes, médiane 5-8. 70 % ont moins de 20 commentaires. Les threads Q&A représentent plus de 50 % des citations. Longueur médiane d'un commentaire cité : ~80 mots. Il n'existe pas de seuil d'upvotes.

Conditions côté compte : ancienneté et karma, réponses réparties sur plusieurs threads plutôt qu'un post unique, terminologie cohérente dans la durée. La répétition d'une même recommandation dans des threads différents pèse plus qu'un score élevé dans un seul thread (Conbersa). Délai avant effet mesurable : 60 à 90 jours, consensus multi-sources ; 120 jours en borne haute. Perplexity reprend un commentaire Reddit nouveau en 24 h à 7 jours.

Interdits : astroturfing, faux comptes, faux avis. Détection communautaire documentée, dommage durable.

### Rédaction : format documentation

Les moteurs reprennent davantage un texte formulé comme une source de référence : définitions, données vérifiables, étapes numérotées. Sans « je pense », « à mon avis » (Reddit GEO Playbook, Medium, mai 2026, recoupé sur plusieurs guides 2026).

### Fraîcheur (corrigé 2026-07-02)

Âge moyen des threads Reddit cités par les IA : ~900 jours (Semrush). Les vieux threads forts restent cités. La tactique n'est pas de réécrire ses réponses tous les 90 jours (chiffre issu d'une seule source Medium) : elle consiste à ajouter un commentaire récent dans les vieux threads forts déjà investis, à indiquer l'année courante dans les titres pertinents, et à contrôler chaque mois la dérive des threads les plus cités. Des mesures donnent un taux de citation AI Overviews plus élevé pour les pages portant un signal d'année courante ; sources à intérêt commercial, non confirmées.

### Citations négatives

Les IA citent aussi les critiques et comparatifs défavorables. Une mesure donne des taux de citation proches entre sentiment positif (~5 %) et négatif (~6,1 %) (AuthorityTech, 2026, source à intérêt commercial). Un thread négatif visible peut orienter durablement la présentation d'un site par une IA. La veille sur ses propres mentions fait partie du dispositif (routine, bloc veille).

---

## 3. Politique d'autopromo de Reddit

Doctrine officielle : « C'est parfaitement OK d'être un Redditor qui a un site web. Ce n'est pas OK d'être un site web qui a un compte Reddit. »

Conséquence opérationnelle : la contribution précède la promotion. Ratio de référence : ~90 % de contribution pour 10 % d'autopromo maximum ; 95/5 en pratique prudente (§6). Le statut de consultant SEO reste en arrière-plan, jamais le sujet d'un post.

---

## 4. Montée d'un compte

Reddit filtre les comptes neufs automatiquement.

1. **Création et profil.** Avatar, bio sobre, sans mention commerciale.
2. **Ancienneté.** Seuils fixés par chaque subreddit : 1 à 30 jours. Standard courant : 7 jours minimum, 30 jours sur les subs exigeants. Un compte créé le jour même qui poste un lien est filtré.
3. **Karma.** Deux types : comment karma et post karma. Échelle logarithmique (un post à 1 000 upvotes peut rapporter ~500 de karma). Le comment karma se construit plus vite. Seuils anti-spam typiques des subs : 10 à 100+ de karma combiné. Sous le seuil, l'AutoModerator supprime le post sans intervention humaine.
4. **Rodage : 2 à 4 semaines.** Commentaires utiles uniquement dans les subs cibles, zéro lien. Lecture des posts triés par « Top, ce mois-ci » pour cartographier ce qui fonctionne. Cette phase conditionne l'accès à tout le reste.

---

## 5. Sélection des subreddits

Découverte : recherche Reddit filtre « Communities », Subreddit Stats (activité, croissance), SnoopSnoo (démographie, parfois indisponible), Redditlist.

Critère principal : l'engagement, pas la taille. Un sub de 15 000 membres avec des discussions actives produit plus qu'un sub de 500 000 inactif. Vérification : tri « Top, ce mois-ci », une semaine de lecture par sub candidat avant d'y écrire.

Règles locales : chaque sub a les siennes (sidebar ou post épinglé). Certains interdisent toute activité commerciale, d'autres imposent un seuil de karma ou d'âge, d'autres réservent l'autopromo à un jour dédié. Lecture obligatoire avant tout post, wiki du sub comprise.

---

## 6. Ratio d'autopromo : état de la règle

La règle 9:1 (9 contributions pour 1 contenu promotionnel) a été publiée par Reddit puis retirée du Reddiquette formel. Remplacement : « participant authentique », apprécié par les mods sur le comportement global.

Texte opposable aujourd'hui, Content Policy : spam = actions « répétées, non désirées ou non sollicitées » ; manipulation = « toute tentative de manipuler le vote ou les systèmes de Reddit ». Depuis 2023, le Contributor Quality Score (CQS) filtre les comptes de faible qualité par signaux comportementaux, indépendamment de tout ratio.

Test de contrôle : un profil dont l'historique se résume à des liens vers un même site correspond au pattern sanctionné. Ratio de travail : 95/5.

---

## 7. Formats de contribution

Ton constaté : anti-marketing, vocabulaire de la communauté, sans jargon corporate.

- **Commentaires utiles.** Le volume principal. Réponses en profondeur à de vraies questions, sans pitch. Construit karma et crédibilité.
- **Données originales.** Format le plus compatible avec une activité commerciale : data first-party anonymisée (logs Fusionn, GSC, études CTR). Apport vérifiable, pas de format publicitaire.
- **Réponses gratuites, TIL, guides.** Sans CTA, sans lien commercial.
- **AMA.** Conditions de réussite documentées : personne réelle, réponses longues, questions gênantes traitées. Échecs documentés : Nissan (questions plantées), cas archivés sur r/AMADisasters.

Donnée de contexte : selon Reddit, 81 % des utilisateurs acceptent les conversations avec les acteurs commerciaux, 59 % attendent qu'ils écoutent le feedback. Condition : authenticité.

---

## 7bis. Protocoles d'exécution

### Protocole d'activation (commentaire)

- Liste : 8 à 12 subreddits, 20 à 30 mots-clés de douleur (« best CRM for solopreneur », « [catégorie] alternatives »).
- Monitoring : Reddit Search + F5Bot (gratuit, 200 mots-clés max).
- Compte : plus de 30 jours, karma 200-500.
- Structure de réponse : 3 à 5 conseils concrets, expérience personnelle, puis mention avec disclosure (« une option que j'utilise moi-même est X ») si légitime.
- DM proposé si le sub l'autorise. Source « Reddit » trackée en CRM (UTM).
- Réponse à tous les commentaires et DM sous 48 h.
- Cadence : 4 à 6 commentaires par jour, plafond 8 (aligné 2026-07-02 sur le consensus des guides, bande 2-8/jour). Jamais en rafale : 20 commentaires dans l'heure correspond au pattern spam détecté.

### Protocole de post

- Étude préalable des 10 meilleurs posts du sub (format, longueur, ton).
- 50 à 80 % de valeur directe dans le post : captures, métriques, échecs assumés.
- Titres qui rankent (Ross Simmonds, guides 2026) : « J'ai [fait X] pendant [période], voici ce qui a marché », « How to [objectif] in [secteur] », « We tested 5 [outils] », « Best [outil] for [cas d'usage] ». Méthode Simmonds : TL;DR en tête, enseignements concrets, question ouverte en fin.
- Timing : matinée ET en semaine, environ 6-10 h ET (corrigé 2026-07-02 : l'étude Upvote.net porte sur 150 posts, pas 1 000, vendeur d'upvotes ; fenêtre corroborée par Foundation, RecurPost, Single Grain ; Foundation ajoute le samedi matin).
- Première heure décisive : pondération logarithmique des votes, les 10 premiers upvotes pèsent comme les 100 suivants. Les 6-10 premières heures conditionnent le ranking Google du thread (corrigé 2026-07-02 : le « 30 premières minutes » ne venait que de vendeurs d'upvotes).
- Publication d'abord dans le sub principal. Réponses sous 2 h, puis 100 % des commentaires pendant 24-48 h.
- Cross-post : 3-4 subs pertinents maximum par contenu, espacés de 6 h et sur des jours différents. 5 subs ou plus en rafale = pattern de spam (corrigé 2026-07-02 : l'ancien « 1 toutes les 2-3 semaines » n'avait aucune source).

### Repurposing d'un article

Résumé des idées principales, suppression du remplissage, enseignements actionnables, lien en ressource complémentaire, jamais au centre du post. Donnée Ross Simmonds : un thread positionné sur une requête « [produit] alternative » a généré ~1 300 visiteurs/mois contre ~330 pour la page concurrente, soit ~4x.

---

## 8. Threads positionnés sur Google

Mécanique : un thread dont le titre correspond à une requête réelle bénéficie de l'autorité du domaine reddit.com dans le top 10.

Tactiques documentées (Ross Simmonds) : le titre reprend la formulation de la requête (« What's the best… », « Has anyone tried… », « How do I… ») ; la réponse complète est dans le corps ; les commentaires actifs soutiennent le ranking, donc la discussion s'entretient.

Cadre de risque : politique Google « site reputation abuse » (mars 2024, renforcée le 19 novembre 2024). Elle vise les sous-dossiers loués chez les éditeurs, pas les forums UGC. Reddit modère de son côté les patterns d'abus : comptes récents poussant les mêmes offres dans des threads de recommandation. Critère de décision : un thread construit pour répondre, dont le titre correspond à une requête, reste dans le cadre ; un thread construit uniquement pour ranker correspond au pattern modéré.

Croisement GEO (vérifié 2026-07-02) : Perplexity source Reddit via les SERP Google (procès Reddit v. Perplexity, test honeypot). Un commentaire dans un thread déjà positionné apparaît dans Perplexity en quelques jours. C'est le levier GEO au meilleur rendement documenté.

---

## 9. Extraction d'insights

Usage sans risque : rien n'est posté.

- **GummySearch** : classement automatique des conversations d'une niche en Pain Points, Solution Requests, Money Talk, Hot Discussions.
- **Keyworddit** (gratuit) : extraction des termes fréquents d'un subreddit avec volume Google estimé.
- **`site:reddit.com`** sur Google : threads déjà positionnés sur une requête, questions récurrentes.

Méthode : subs cibles → mots-clés bruts (Keyworddit) → conversations (GummySearch ou recherche native) → pain points. Les expressions à charge émotionnelle (« je déteste vraiment », « j'ai désespérément besoin de ») signalent les douleurs exploitables. Alimente le process besoin → mot-clé → cluster.

X.com en complément : la recherche en mode expert sort des signaux équivalents (compte premium, ~5 €/mois). Même traitement.

Contrainte technique : Reddit bloque le crawler. Les posts se collent à la main pour décomposition, ou passent par les flux RSS publics (méthode du cockpit).

---

## 10. Shadowban : définition et déclencheurs

Shadowban : contenu visible pour l'auteur, invisible pour les autres. Majoritairement automatique en 2026.

Déclencheurs documentés :

- même lien posté dans plusieurs subreddits, même pertinent ;
- même commentaire répété, même reformulé a minima (déclencheur n°1 selon RedShip, 2026) ;
- cadence anormale : compte récent très actif, rafales (limite technique ~1 action/10-15 min quand le karma est bas dans un sub) ;
- posts répétés vers un même domaine, surtout récent ;
- IP liée à des comptes spam ;
- manipulation de vote sous toutes ses formes (demander des upvotes, multi-comptes, échanges de votes), brigading inclus ;
- reposts de contenu déjà publié ;
- raccourcisseurs de liens (bit.ly, t.co), flaggés automatiquement.

Détection : profil ouvert en navigation privée déconnecté (« page not found » ou posts invisibles = shadowban probable) ; lien direct d'un commentaire récent ouvert en privé ; posts récents à zéro vote et commentaires sans réponse. Outils : Reddit shadowban checker, redship, banchecker.

Pattern le plus fréquent : compte neuf qui poste des recommandations produit. C'est le premier signal surveillé par les mods.

---

## 11. Modération

Chaque sub est géré par des mods bénévoles qui appliquent leurs propres règles. Contact : modmail (« Message the mods » dans la sidebar), pas les DM. Usage utile pour un consultant : demander avant de poster un contenu lié à son activité (« est-ce autorisé de partager une étude que j'ai faite sur X ? »).

AutoModerator : bot configurable par sub. Supprime ou flaire par domaine ou mot-clé, applique les seuils de karma et d'âge, répond automatiquement. C'est lui qui supprime les posts sous seuil, sans intervention humaine. D'où la phase de rodage (§4).

---

## 12. Marché francophone

Données France : ~20,6 M d'utilisateurs estimés (Influencia), +72 % de visiteurs mensuels sur un an (Médiamétrie), top 10 des réseaux sociaux en France. Abondance : 10,4 M de visiteurs mensuels à mi-2025, audience doublée en un an. Causes : traduction automatique du corpus en français, indexation prioritaire depuis l'accord Google.

Communautés : pas de sub SEO francophone actif (pas de r/SEO_fr ni r/referencement vivants). Les SEO français échangent sur r/SEO et r/bigseo (anglophones), sur LinkedIn, X et WebRankInfo. Gros subs FR : r/france (2,5 M+), puis longue traîne (r/AskFrance, r/vosfinances, r/conseiljuridique, r/Cuisine). Counts précis non publiés hors r/france.

Évaluation du levier FR : Lefebvre Dalloz (juillet 2025) classe Reddit « canal secondaire ou de veille dans un contexte francophone ». Limite de preuve : aucune donnée chiffrée comparant la visibilité SERP de Reddit sur Google.fr et Google.com n'est publiée. Les affirmations « Reddit domine les SERP françaises » circulent sans étude à l'appui.

Donnée 2026 déterminante (Peec AI, 64,77 M de citations Reddit, mars-juin 2026) : les pages Reddit auto-traduites (`?tl=`) représentent 40 à 73 % des citations Reddit sur les surfaces IA de Google dans les marchés non anglophones d'Europe (Suède/Norvège 70 %+, Espagne 72 % sur AI Mode, Allemagne 52 % sur AIO ; France non isolée, pattern pan-européen). ChatGPT a quasi cessé de citer les pages traduites (6,14 % → 0,30 %, avril-juin 2026).

Conséquences :

1. GEO : les subs anglophones de la niche search/IA sont le terrain principal. Les réponses en anglais sont citées, y compris via les pages traduites sur les requêtes françaises côté Google.
2. SEO francophone : opportuniste. Repérage `site:reddit.com` des requêtes FR où un thread ranke, positionnement au cas par cas.
3. Aucun retour d'expérience FR mesuré n'est publié. Le test Qadence produit cette donnée.

---

## 13. Outils

| Outil | Fonction | Coût |
|---|---|---|
| GummySearch | Pain points, classement auto des conversations | Payant (essai gratuit) |
| Keyworddit | Mots-clés d'un subreddit avec volume Google estimé | Gratuit |
| F5Bot | Alertes email sur mots-clés, 200 max. Pas de dashboard ni sentiment | Gratuit |
| Brand24 | Social listening multi-plateformes, sentiment, part de voix | ~199 $/mois |
| Subreddit Stats | Statistiques et croissance des subreddits | Gratuit |
| SnoopSnoo | Analyse de profil et d'activité (parfois indisponible) | Gratuit |
| Redditlist | Découverte et classement de subreddits | Gratuit |
| Shadowban checker | Vérification de shadowban | Gratuit |

Stack retenu : Keyworddit + GummySearch pour les insights, F5Bot pour les mentions. Brand24 seulement si un compte client exige sentiment et part de voix.

---

## 14. Plan 90 jours

**Jours 1-14 : socle.** Compte complété, vieillissement. 8 à 10 subs identifiés (anglophones search/IA/growth en priorité, 2-3 FR). Une semaine de lecture par sub, règles et wiki lues. Commentaires utiles uniquement, zéro lien. Objectif : franchir les seuils de karma et d'âge. F5Bot posé sur les sites suivis.

**Semaines 3-6 : contribution et insights.** 20-30 commentaires de qualité par semaine. Travail d'insights lancé (Keyworddit, GummySearch), pain points redescendus dans le process besoin → mot-clé → cluster. Premier post à valeur, donnée originale anonymisée, dans le sub au capital le plus élevé. Ratio 95/5 tenu.

**Semaines 7-10 : threads et GEO.** Posts dont le titre correspond à une requête réelle, discussion entretenue. Interventions dans les threads décisionnels « best X for Y » et comparatifs, mention du site quand elle est légitime. Accord des mods demandé en modmail avant tout post limite.

**Semaines 11-13 : mesure.** Positions vérifiées via `site:reddit.com`. Citations recherchées dans Perplexity et ChatGPT sur la liste fixe de requêtes. Arrêt de ce qui ne produit pas. Bilan : threads positionnés, mentions dans les IA, insights convertis en contenu publié.

Délai GEO : 60 à 90 jours avant effet mesurable, 120 en borne haute. Le plan pose les fondations ; les citations arrivent en général après.

---

## 15. Métriques

- Karma et âge du compte (condition d'accès).
- Threads positionnés sur Google et positions (`site:reddit.com`).
- Citations des sites et du nom dans Perplexity, ChatGPT, AI Overviews, sur liste fixe de 15-20 requêtes acheteur (métrique principale 2026).
- Mentions F5Bot (volume, tonalité).
- Insights Reddit convertis en pages ou clusters publiés.
- Trafic référent Reddit (faible attendu).

---

## Note de fiabilité (à lire avant de citer ces chiffres ailleurs)

Mise à jour 2026-07-02 : les chiffres d'exécution (cadences, timing, cross-post, fraîcheur) ont été vérifiés contre ~25 sources via 3 audits web parallèles et corrigés dans le corps, marqués « corrigé 2026-07-02 ». Détail des corrections dans [[Routine-quotidienne]], qui fait foi sur l'exécution. Apports de cette vérification : 80 % des posts cités par les IA ont moins de 20 upvotes (Semrush, 248 000 URLs) ; threads Q&A > 50 % des citations ; Perplexity source Reddit via les SERP Google (procès Reddit v. Perplexity) ; pages auto-traduites `?tl=` = 40-73 % des citations Reddit sur les surfaces IA de Google en Europe non anglophone (Peec AI).

Chiffres les mieux ancrés sur source primaire : update hidden gems (Glenn Gabe), visibilité +1 328 % (Sistrix via Amsive, 2024), accords Google 60 M$ (CBS, Fortune) et OpenAI 70 M$ estimé (Search Engine Land), citations IA (Semrush juillet-octobre 2025, Peec AI mars 2026).

Limites : les pourcentages de citation IA sont volatils, à toujours dater et fenêtrer. Les chiffres de trafic en visites sont des estimations Ahrefs. Aucune étude de cas Reddit indépendante avec méthodo vérifiable n'existe ; le test Qadence.io est en cours, résultats non disponibles. Les données sur l'effet du signal d'année et la parité positif/négatif viennent de sources à intérêt commercial, non confirmées. Les stats « +15-40 % de visibilité » et « +11 % de lift publicitaire » viennent de sources à intérêt commercial. Mentions sans lien : pas un facteur de ranking direct (consensus Mueller) ; effets réels = demande de marque et citation IA. « Mention Reddit = backlink » est faux.

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
- [LaunchKit - Reddit account age and karma requirements](https://launchkit.me/blog/reddit-account-karma-requirements/)
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
