---
type: source
source_type: doctrine
title: Routine quotidienne Reddit (SEO + GEO)
aliases: [routine-reddit, reddit-quotidien, reddit-daily]
tags: [reddit, geo, seo, routine, qadence]
created: 2026-07-02
updated: 2026-07-03
sources: 25
confidence: high
status: stable
---

# Routine quotidienne Reddit

> Cette routine est dérivée du [[Playbook-Reddit-SEO-GEO]]. Ses chiffres ont été vérifiés contre ~25 sources le 2026-07-02 : chaque quota repose sur la convergence de 4 à 6 sources indépendantes, aucun sur une source unique. Le budget est de 25 à 30 minutes par jour, 6 jours sur 7, plus deux rendez-vous hebdomadaires. Le terrain est Qadence.io, sur les subs anglophones search/IA en priorité.

## En résumé

Chaque jour, tu réponds d'abord à tout ce qui est arrivé (100 % sous 48 h, sous 2 h après un post), puis tu écris 4 à 6 commentaires de 120 à 200 mots, en priorité dans des threads déjà positionnés sur Google.

Chaque semaine, tu t'autorises au maximum une mention de Qadence ou d'un site à toi, et tu publies un post (le plafond dur est de 3, d'après la recherche interne de Reddit). Le vendredi, tu mesures sur une liste fixe de requêtes.

Le 1er de chaque mois, retourne dans les discussions où tu as déjà répondu et ajoute un nouveau commentaire. Ne modifie jamais tes anciens messages.

---

## Quotas

| Action | Quota |
|---|---|
| Commentaires utiles | 4 à 6 par jour, plafond 8 |
| Rythme | actions espacées dans la journée, jamais en rafale |
| Mention de Qadence ou d'un site à toi | 1 par semaine maximum |
| Même lien | 2 fois par jour maximum, jamais plusieurs subs d'affilée |
| Même commentaire | jamais répété, même reformulé |
| Post à valeur | 1 par semaine, plafond dur de 3 par semaine |
| Cross-post d'un même contenu | 3 à 4 subs maximum, espacés de 6 h, sur des jours différents |
| Réponses aux commentaires et DM reçus | 100 % sous 48 h, sous 2 h après un post |

Si un sub impose un seuil de réputation ou d'âge que le compte ne franchit pas encore, tu t'y limites aux commentaires, sans poster.

---

## Déroulé quotidien (25-30 min)

**1. Veille (5 min).**
Tu ouvres les alertes de mentions. Tu en sors deux choses : les threads où intervenir aujourd'hui, et les threads négatifs à traiter. Les IA citent le négatif au même taux que le positif (environ 6,1 % contre 5 %, AuthorityTech 2026, source à intérêt commercial). Un thread négatif reçoit une réponse factuelle sous 48 h.

**2. Réponses (5 min).**
Tu réponds à 100 % des commentaires et DM reçus depuis la veille. Les commentaires actifs soutiennent le ranking du thread et la réputation du compte.

**3. Commentaires (15 min ; 8 à 10 min avec le cockpit).**
Le Reddit Cockpit dépose chaque matin à 07h50 une file de drafts dans `queue/AAAA-MM-JJ.md` : des threads scorés, 1 à 2 commentaires pré-rédigés par thread, et les quotas rappelés en tête. Tu relis, tu ajustes, tu colles à la main. La machine ne publie jamais.

Tu écris 4 à 6 commentaires, sélectionnés dans cet ordre :

- **Priorité 1 : les threads déjà positionnés sur Google** sur tes requêtes acheteur (`site:reddit.com "best ai seo tool"`, etc.). Perplexity source Reddit via les SERP Google (procès Reddit v. Perplexity, octobre 2025) : un commentaire dans un thread positionné apparaît dans Perplexity en quelques jours.
- **Priorité 2 : les threads de moins de 48 h**, repérés via New/Rising et les mots-clés de douleur (« best X for Y », « [catégorie] alternatives », troubleshooting). L'heuristique de sélection est un thread de 30 à 100 réponses (source unique, à valider sur le terrain).

Le format : 120 à 200 mots, 2 à 3 données précises (un outil nommé, un chiffre daté, des étapes), en registre documentation, sans « je pense ». La longueur médiane des commentaires cités par les IA est d'environ 80 mots (Semrush, 248 000 URLs) ; 120-200 vise la marge haute.

Il n'existe pas de seuil d'upvotes : 80 % des posts cités en ont moins de 20 (médiane 5-8, Semrush). La répétition d'une même recommandation dans des threads différents pèse plus qu'un score élevé dans un seul thread.

La mention « une option que j'utilise moi-même est X » ne part que si elle est légitime dans le thread, que le quota hebdomadaire n'est pas consommé, et qu'elle inclut la disclosure.

**4. Log (2 min).**
Tu ajoutes une ligne dans [[Journal]] : date, commentaires, subs, mention oui/non, threads repérés, insights.

---

## Rendez-vous hebdomadaires

**Mardi, mercredi ou jeudi matin ET : le post.**
La fenêtre est 6-10 h ET, soit 18-22 h à Manille. Elle est corroborée par quatre sources indépendantes ; le samedi matin ET ressort comme fenêtre secondaire.

Le titre reprend une requête réelle, en format question de préférence : les threads Q&A représentent plus de 50 % des citations IA (Semrush). Le corps contient 50 à 80 % de valeur directe : captures, métriques, échecs assumés. Le format le plus compatible avec ton activité reste la donnée originale anonymisée (logs, données de recherche, tests).

Après publication, la première heure est décisive pour la distribution Reddit : la pondération des votes est logarithmique, les 10 premiers upvotes pèsent comme les 100 suivants. Les 6 à 10 premières heures conditionnent le ranking Google du thread. Tu réponds sous 2 h, puis tu suis les commentaires pendant 24 à 48 h.

**Vendredi : la mesure (15 min).**
Tu relèves six chiffres dans le [[Journal]] :

1. La réputation du compte (commentaires + posts)
2. Les positions des threads via `site:reddit.com`
3. Les citations de Qadence.io et de tes sites sur une **liste fixe de 15 à 20 requêtes acheteur** passées dans Perplexity, ChatGPT et les AI Overviews. La liste fixe rend la mesure comparable d'une semaine à l'autre.
4. Les mentions de la semaine (volume, tonalité)
5. Les insights redescendus dans le process besoin → mot-clé → cluster
6. Le trafic référent Reddit (faible attendu)

Tu conclus par un verdict en une phrase : ce qu'on reconduit, ce qu'on ajuste.

---

## Cycle mensuel

Le 1er du mois, 20 minutes. La donnée de cadrage : l'âge moyen des threads Reddit cités par les IA est d'environ 900 jours (Semrush), les vieux threads forts restent cités. Trois actions :

- tu retournes dans les discussions où tu as déjà répondu et tu ajoutes un nouveau commentaire (un chiffre à jour, un retour récent) ; Perplexity reprend un commentaire nouveau en 24 h à 7 jours ;
- tu mets l'année courante dans les titres quand c'est pertinent ;
- tu contrôles tes 3 à 5 threads les plus cités : une nouvelle réponse passée au-dessus de la tienne, un thread verrouillé.

Le délai avant un effet GEO mesurable est de 60 à 90 jours (consensus multi-sources), 120 en borne haute. Il n'y aura pas de verdict sur le test Qadence avant fin août 2026. L'évolution attendue se fait par paliers : la part de Reddit dans les citations ChatGPT est passée d'environ 60 % à environ 10 % en deux semaines en septembre 2025 (Semrush).

---

## Spécifique 2026

- **Tes réponses en anglais couvrent aussi les requêtes en français.** Les pages Reddit auto-traduites (`?tl=`) représentent 40 à 73 % des citations Reddit sur les surfaces IA de Google dans les marchés non anglophones d'Europe (Peec AI, 64,77 M de citations, mars-juin 2026). ChatGPT a quasi cessé de citer les pages traduites (de 6,14 % à 0,30 % entre avril et juin 2026).
- **Reddit Answers** est passé de 1 M à 15 M d'utilisateurs hebdomadaires en 2025. C'est une surface supplémentaire, alimentée par les mêmes réponses, sans action dédiée.
- **Le procès Reddit v. Perplexity** (octobre 2025, en cours) peut changer l'accès de Perplexity à Reddit. On n'optimise pas pour un seul moteur.

---

## Garde-fous

- Le même commentaire ne se répète jamais, même reformulé : c'est le déclencheur n°1 des filtres.
- Le même lien ne part pas plus de 2 fois par jour, ni dans plusieurs subs d'affilée.
- Les raccourcisseurs de liens (bit.ly, t.co) sont flaggés automatiquement.
- La manipulation de vote est sanctionnée sous toutes ses formes.
- Un changement brutal de comportement d'un compte ancien (des liens en volume) déclenche un flag.
- Un post lié à l'activité commerciale suppose les règles du sub lues avant, et un message aux mods en cas de doute.
- Le contrôle final reste le profil : un historique réduit à des liens vers un même site correspond au pattern sanctionné.

**Check shadowban mensuel** : tu ouvres ton profil en navigation privée déconnecté. Une page introuvable ou des posts invisibles signalent un shadowban probable. Tu gèles toute activité jusqu'au diagnostic.
