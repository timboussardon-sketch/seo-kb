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

> Dérivée du [[Playbook-Reddit-SEO-GEO]]. Chiffres vérifiés contre ~25 sources le 2026-07-02 (3 audits web parallèles, détail en bas de page). Budget : 25 à 30 min/jour, 6 jours sur 7, plus deux rendez-vous hebdo. Terrain : Qadence.io, subs anglophones search/IA en priorité.

## En résumé

Par jour : réponses à tout ce qui est arrivé (100 % sous 48 h, sous 2 h après un post), 4 à 6 commentaires de 120-200 mots, en priorité dans des threads déjà positionnés sur Google. Par semaine : 1 mention maximum de Qadence ou d'un site à soi, 1 post (plafond dur : 3, data interne Reddit). Le vendredi : mesure sur liste fixe de requêtes. Le 1er du mois : fraîcheur des vieux threads investis, par commentaire, pas par réécriture.

---

## Quotas

| Action | Quota | Ancrage |
|---|---|---|
| Commentaires utiles | 4 à 6/jour, plafond 8 | bande 2-8/jour, consensus des guides 2025-2026 : 4-7 (Backlinko), 5-8 (SubredditSignals) pour un compte rodé ; aucun guide ne recommande plus de 8 |
| Rythme | actions espacées, jamais en rafale ; 20 commentaires/heure = pattern spam | KarmaGuy 2026 ; limite technique ~1 action/10-15 min quand le karma est bas dans un sub |
| Mention de Qadence / sites à soi | 1/semaine max | ratio 95/5 ; le 90/10 formel a été retiré par Reddit, enforcement par Contributor Quality Score (comportemental) + règles de chaque sub |
| Même lien | 2 fois/jour max, jamais 5 subs d'affilée | KarmaGuy + ReddiReach 2026 |
| Même commentaire | jamais répété, même reformulé a minima | déclencheur n°1 des filtres spam (RedShip 2026) |
| Post à valeur | 1/semaine, plafond dur 3/semaine | data interne Reddit (Rob Gaige, Adweek 2026) : au-delà de 3/semaine le sentiment chute ; 3 commentaires communautaires = +2,2 % de mentions vs +0,5 % pour 1 post |
| Cross-post d'un même contenu | 3-4 subs pertinents max, espacés de 6 h, jours différents | postpone.app et recoupements 2025-2026 ; le « 1 toutes les 2-3 semaines » antérieur n'avait aucune source |
| Réponses aux commentaires et DM | 100 % sous 48 h ; sous 2 h après un post | §7bis du playbook + guides Reddit-SEO 2025-2026 |

Sub avec seuil de karma ou d'âge non atteint : commentaires seuls, pas de post.

---

## Déroulé quotidien (25-30 min)

**1. Veille (5 min).**
Alertes F5Bot (Qadence, organikk, fusionn, nom). Deux sorties : threads où intervenir aujourd'hui, threads négatifs à traiter. Les IA citent le négatif au même taux que le positif (~6,1 % vs ~5 %, AuthorityTech 2026, source à intérêt commercial). Thread négatif : réponse factuelle sous 48 h. Cadence documentée par les guides GEO : hebdomadaire ; le quotidien via F5Bot est au-dessus de la pratique, à coût nul (alertes email).

**2. Réponses (5 min).**
100 % des commentaires et DM reçus depuis la veille. Les commentaires actifs soutiennent le ranking du thread et le karma (§1 et §8 du playbook).

**3. Commentaires (15 min ; ~8-10 min avec le cockpit).**
Le Reddit Cockpit (`~/Code/reddit-cockpit/`, launchd 07h50) dépose chaque matin une file de drafts dans `queue/AAAA-MM-JJ.md` : threads scorés, 1-2 commentaires pré-rédigés, quotas en tête. Relecture, ajustement, collage manuel. La machine ne publie jamais. Sans le cockpit, sélection manuelle selon les mêmes règles.

4 à 6 commentaires. Sélection par priorité :

- **Priorité 1 : threads déjà positionnés sur Google** sur les requêtes acheteur (`site:reddit.com "best ai seo tool"`, etc.). Perplexity source Reddit via les SERP Google (procès Reddit v. Perplexity, oct. 2025) ; un commentaire dans un thread positionné apparaît dans Perplexity en quelques jours.
- **Priorité 2 : threads de moins de 48 h**, via New/Rising et les mots-clés de douleur (« best X for Y », « [catégorie] alternatives », troubleshooting). Heuristique de sélection : 30 à 100 réponses (source unique, à valider sur le terrain).

Format : 120 à 200 mots, 2-3 données précises (outil, chiffre daté, étapes), registre documentation, sans « je pense ». Longueur médiane des commentaires cités par les IA : ~80 mots (Semrush, 248 000 URLs) ; 120-200 vise la marge haute. Seuil d'upvotes : inexistant, 80 % des posts cités en ont moins de 20 (médiane 5-8, Semrush). La répétition d'une même recommandation dans des threads différents pèse plus qu'un score élevé dans un seul thread.

Mention « une option que j'utilise moi-même est X » : uniquement si légitime dans le thread, quota hebdo non consommé, disclosure incluse.

**4. Log (2 min).**
Une ligne dans [[Journal]] : date, commentaires, subs, mention oui/non, threads repérés, insights.

---

## Rendez-vous hebdo

**Mardi, mercredi ou jeudi matin ET : le post.**
Fenêtre : 6-10 h ET, soit 18-22 h à Manille. Corroborée par 4 sources (Foundation, RecurPost, Single Grain, Upvote.net) ; l'étude Upvote.net porte sur 150 posts et vient d'un vendeur d'upvotes, la convergence des sources fait foi, pas cette étude. Foundation ajoute le samedi matin ET. Pics réels par sub : outil per-sub type Delay for Reddit ou Postpone.

Titre = requête réelle, format Q&A de préférence : les threads Q&A représentent plus de 50 % des citations IA (Semrush). Corps : 50 à 80 % de valeur directe (captures, métriques, échecs assumés). Format le plus compatible avec l'activité : donnée originale anonymisée (logs Fusionn, GSC, tests).

Après publication : première heure décisive pour la distribution Reddit (pondération logarithmique des votes, les 10 premiers upvotes pèsent comme les 100 suivants), 6-10 premières heures pour le ranking Google. Réponses sous 2 h, suivi 24-48 h. Le « 30 premières minutes » antérieur ne venait que de vendeurs d'upvotes.

**Vendredi : mesure (15 min).**
Dans le [[Journal]] :

1. Karma (comment + post)
2. Positions des threads via `site:reddit.com`
3. Citations de Qadence.io et des sites sur **liste fixe de 15-20 requêtes acheteur** passées dans Perplexity, ChatGPT, AI Overviews. Liste fixe = mesure comparable d'une semaine à l'autre (cadence documentée par les guides GEO 2026)
4. Mentions F5Bot (volume, tonalité)
5. Insights redescendus dans le process besoin → mot-clé → cluster
6. Trafic référent Reddit (GA/GSC, faible attendu)

Verdict en une phrase : reconduire ou ajuster, quoi.

---

## Cycle mensuel (fraîcheur)

Le 1er du mois, 20 min. Donnée de cadrage : âge moyen des threads Reddit cités par les IA ~900 jours (Semrush) ; les vieux threads forts restent cités. Le « refresh tous les 90 jours » vient d'une seule source Medium. Actions :

- commentaire récent dans les vieux threads forts déjà investis (chiffre à jour, retour récent) ; Perplexity reprend un commentaire nouveau en 24 h à 7 jours ;
- année courante dans les titres quand pertinent ;
- contrôle des 3-5 threads les plus cités : nouvelle réponse au-dessus, thread verrouillé.

Délai avant effet GEO mesurable : 60 à 90 jours (consensus multi-sources), 120 en borne haute. Pas de verdict sur le test Qadence avant fin août 2026. Évolution attendue par paliers : la part de Reddit dans les citations ChatGPT est passée d'environ 60 % à environ 10 % en deux semaines en septembre 2025 (Semrush).

---

## Spécifique 2026

- **Les réponses en anglais couvrent aussi les requêtes en français.** Pages Reddit auto-traduites (`?tl=`) : 40 à 73 % des citations Reddit sur les surfaces IA de Google dans les marchés non anglophones d'Europe (Peec AI, 64,77 M de citations, mars-juin 2026). ChatGPT a quasi cessé de citer les pages traduites (6,14 % → 0,30 %, avril-juin 2026).
- **Reddit Answers** : 1 M → 15 M d'utilisateurs hebdo en 2025. Surface supplémentaire alimentée par les mêmes réponses, sans action dédiée.
- **Procès Reddit v. Perplexity** (oct. 2025, en cours) : l'accès de Perplexity à Reddit peut changer. Ne pas optimiser pour un seul moteur.

---

## Garde-fous

- Même commentaire jamais répété, même reformulé : déclencheur n°1 des filtres (RedShip 2026)
- Même lien : 2 fois/jour max, jamais plusieurs subs d'affilée
- Raccourcisseurs de liens (bit.ly, t.co) : flag automatique
- Manipulation de vote : sanctionnée sous toutes ses formes
- Changement brutal de comportement d'un compte ancien (liens en volume) : flag
- Post lié à l'activité commerciale : règles du sub lues avant, modmail en cas de doute
- Contrôle du profil : un historique réduit à des liens vers un même site correspond au pattern sanctionné

**Check shadowban mensuel** : profil ouvert en navigation privée déconnecté. Page introuvable ou posts invisibles = shadowban probable. Gel de toute activité jusqu'au diagnostic.

---

## Note de vérification (2026-07-02)

Routine confrontée au web via 3 audits parallèles (~25 sources, 2025-2026). Corrections issues de la vérification : plafond de commentaires 10 → 8 ; plafond dur 3 posts/semaine ajouté (data interne Reddit) ; « 30 premières minutes » remplacé par 1 h + 6-10 h ; cross-post « toutes les 2-3 semaines » remplacé par espacement 6 h+ / 3-4 subs ; refresh 90 jours remplacé par cycle mensuel (source unique, contredite par l'âge moyen ~900 jours des threads cités). Ajouts : ciblage prioritaire des threads positionnés sur Google, format 120-200 mots, liste fixe de requêtes pour la mesure, section 2026.

Biais des sources : la quasi-totalité des sources donnant un chiffre précis vend un outil ou service Reddit (KarmaGuy, SubredditSignals, ReddiReach, RedShip, Upvote.net). Sources les moins biaisées : Semrush (248 000 URLs citées, oct. 2025), Peec AI, Adweek/eMarketer (recherche interne Reddit), Search Engine Land, formule de ranking logarithmique (Salihefendic). Chaque quota repose sur la convergence de 4-6 sources indépendantes, aucun sur une source unique.
