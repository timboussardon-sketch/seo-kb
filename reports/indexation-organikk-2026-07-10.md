---
type: audit
title: "Audit indexation Organikk - 2026-07-10 (site complet)"
date: 2026-07-10
perimetre: "https://organikk.co - 146 URLs du sitemap (site entier, 1er run hors /wiki)"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical", "GSC searchAnalytics API (edge admin-gsc-export, 28j)"]
indexation_google_estimee: "49/146 confirmees indexees (impressions GSC reelles) - 97 indeterminees"
pages_testees: 146
anomalies_critiques: 2
anomalies_mineures: 4
loop: indexation-check
---

# Audit indexation Organikk - 2026-07-10

## Synthese

Premier run sur le **site entier** (146 URLs) et non sur le seul perimetre `/wiki` des 4 runs precedents. Premier run aussi avec de la **vraie donnee GSC** : la reco P3 du 15 juin (brancher la Search Console) est levee via l'edge `admin-gsc-export` de Fusionn, propriete `https://organikk.co/` connectee.

Verifications validees :
- HTTP 200 final : 146 / 146
- Absence de `noindex` (meta + `X-Robots-Tag`) : 146 / 146
- Canonical present et egal a l'URL finale : 146 / 146
- Non bloque par `robots.txt` : 146 / 146
- Balise `<title>` presente et unique : 146 / 146

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **146 / 146** (301 vers le slash final)
- `lastmod` uniforme : **146 / 146** (`2026-07-09T10:33:40.070Z`)
- Pages orphelines (0 lien interne entrant) : **2 / 146**
- Pages sous-maillees (1 seul lien entrant) : **30 / 146**
- Contenu sous 300 mots : **14 / 146**
- Page servie par Google en 404 : **1**

Statut d'indexation, pour la premiere fois mesure et non estime : **49 des 146 URLs du sitemap ont genere au moins une impression** sur les 28 derniers jours (2026-06-12 au 2026-07-10). Ces 49 sont indexees, sans ambiguite. Les **97 autres sont indeterminees** : une page indexee peut rester a zero impression. L'API `searchAnalytics` ne dit pas si une page est dans l'index, elle dit si elle a ete servie. La distinction est maintenue.

Volume total sur la periode : 437 impressions, 17 clics.

Le scraping `site:` reste inexploitable, **5e run consecutif** : Google renvoie une coquille avec redirection JS, aucune SERP dans le HTML. Cette methode est a abandonner (voir Recommandations, P4).

Sitemap : 146 URLs, contre 143 au run du 6 juillet (delta +3). Trajectoire sur 28 jours : 169 -> 136 -> 143 -> 143 -> 146.

Robots.txt inchange : `Allow: /`, deux paths privatifs en `Disallow` (dashboard bootcamp, espace Leexi), sitemap declare.

## Anomalies critiques

### C1. `/manifeste/` renvoie 404 alors que Google la sert toujours

**Constat.** `https://organikk.co/manifeste/` et `https://organikk.co/manifeste` renvoient tous deux `HTTP 404`. La GSC rapporte pourtant sur cette URL **30 impressions en 28 jours, position moyenne 28,6**, ce qui en fait la **2e page du site en impressions**, juste derriere la racine (75 impressions). La requete porteuse est `manifeste seo` (28 impressions, position 30,5).

**Lecture.** La page a ete retiree du site sans redirection. Google la conserve dans son index et continue de l'afficher sur une requete qui la positionne page 3. Chaque impression envoie un utilisateur sur une page d'erreur. Zero clic constate, ce qui est coherent avec la position, mais le signal envoye a Google est mauvais et la requete `manifeste seo` est une requete d'autorite qu'on abandonne.

L'URL est absente du sitemap, donc les 4 audits precedents ne pouvaient pas la voir. C'est exactement le trou que le passage au perimetre complet devait ouvrir.

**Action.** Rediriger `/manifeste/` en `301` vers la page vivante la plus proche. Candidates : `/methode/` (18 impressions, position 5,9) ou `/systeme/` (14 impressions, position 5,4). Jamais de 410.

### C2. `/accompagnement-seo-geo` est orpheline

**Constat.** Page d'offre, 1 272 mots, `HTTP 200`, indexee (1 impression sur 28 jours). **Zero lien interne entrant** sur les 146 pages du site. Verifie : la chaine `accompagnement-seo-geo` n'apparait dans le HTML d'aucune autre page que la sienne.

**Lecture.** Une page commerciale de 1 272 mots que rien ne pointe. Elle vit uniquement par le sitemap. C'est le profil type de la page qui n'accumule aucun signal et reste bloquee en fond d'index.

**Action.** La lier depuis les hubs qui portent deja du maillage : `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours`. Trois liens entrants suffisent a sortir du statut orphelin.

## Anomalies mineures

### M1. Sitemap declare 146 URLs non canoniques - 5e recurrence

Le sitemap pointe vers `https://organikk.co/<path>` sans slash final. Le serveur renvoie un `301` vers `<path>/`. Mesure sur les 146 URLs : **146 sur 146** redirigent, et la redirection est exclusivement l'ajout du slash. Aucune autre transformation.

Les 4 runs precedents ecrivaient « vraisemblablement 143/143 ». C'est maintenant verifie sur la totalite du site, plus une hypothese.

Le canonical du DOM pointe, lui, correctement vers la version avec slash sur 146/146. Le site n'est donc pas en danger, mais chaque URL du sitemap coute un aller-retour de crawl inutile.

P1 du 15 juin, sans effet observable apres 25 jours.

### M2. `lastmod` uniforme sur 146/146 - 5e recurrence

Toutes les URLs portent `2026-07-09T10:33:40.070Z`, la date du dernier build. Un `lastmod` qui bouge a chaque deploiement sur toutes les pages ne transporte aucune information de fraicheur. Google apprend a l'ignorer.

P2 du 15 juin, sans effet observable apres 25 jours.

### M3. Le wiki ne genere quasiment aucune visibilite

Sur les 40 pages `/wiki`, **2 seulement ont genere une impression** en 28 jours : la racine `/wiki/` (15 impressions) et `/wiki/surprise-score` (2 impressions). Les 38 fiches restantes sont a zero.

A rapprocher de M4 : 10 des 14 pages sous 300 mots sont des fiches wiki. Le corpus est mince et il ne remonte pas.

Statut d'indexation de ces 38 fiches : **indetermine**, pas « non indexe ». Trancher demande l'API URL Inspection (voir P4).

### M4. 14 pages sous 300 mots

Dont 10 fiches wiki (`core-web-vitals` 206 mots, `titans-architecture` 240, `muvera` 243, `clustering-semantique` 256, `pillar-page` 269, `silo-seo` 274, `embedding-seo` 277, `eeat` 284, `featured-snippet` 289, `similarite-cosinus` 289).

Trois cas sont normaux et n'appellent aucune action : `/contact` (42 mots), `/accompagnement-1-1-30-jours` (36 mots, tunnel de quiz en 5 etapes) et `/resultats` (196 mots).

A noter : `/accompagnement-1-1-30-jours` est la **seule page du site sans `<h1>`**. Page de conversion, 145 liens entrants, zero impression.

Reste `/secteurs` : 109 mots, hub de section, **zero lien entrant**, zero impression, alors qu'elle porte 2 pages enfants (`/secteurs/avocat`, `/secteurs/hotellerie`).

## Autres observations

**30 pages sous-maillees** (1 seul lien entrant) : 14 pages `/newsletter`, 5 `/strategies`, 3 `/actualites`, plus `/resultats`, `/freelance-geo-lyon`, `/bootcamp-quiz`, `/bootcamp/programme`. Le maillage de ces sections repose sur une seule page de listing.

**`/services`** renvoie un `301` vers `/systeme/` et recolte 14 impressions en position 9,1, sur la requete de site `organikk.co`. Comportement normal pour une URL historique redirigee. Aucune action.

**`/guides/de-0-a-1-seo-claude.pdf`** est servi par Google (6 impressions, position 23,0) et n'est pas dans le sitemap. Un PDF indexe est un actif, pas une anomalie. A ajouter au sitemap si on veut le pousser.

**66 % du sitemap est a zero impression** (97 pages sur 146). Repartition : 38 `/wiki`, 18 `/blog`, 13 `/newsletter`, 9 `/strategies`, 4 `/actualites`, 15 pages diverses. C'est une mesure de visibilite, pas d'indexation.

## Recommandations priorisees

1. **Rediriger `/manifeste/` en 301** vers `/methode/`. Effort : une ligne de config. Impact : recupere 30 impressions par mois aujourd'hui envoyees sur une 404, et arrete le signal d'erreur. **Le seul point urgent de ce rapport.**

2. **Mailler `/accompagnement-seo-geo`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours`. Effort : trois liens. Impact : sort une page d'offre de 1 272 mots du statut orphelin.

3. **Corriger le sitemap** pour qu'il declare les URLs avec le slash final, et rendre le `lastmod` reel (date de derniere modification du contenu, pas date de build). Effort : le generateur de sitemap. Impact : supprime 146 redirections de crawl et rend le `lastmod` exploitable. Ouvert depuis 25 jours.

4. **Remplacer le check `site:` par l'API URL Inspection.** Le scraping Google est mort, 5 runs sur 5. La connexion GSC existe deja (`google_connections`, propriete `https://organikk.co/`). Il manque un endpoint `urlInspection/index:inspect` a cote de `admin-gsc-export`. Effort : ~30 min. Impact : passe les 97 pages « indeterminees » a un statut officiel (`INDEXED`, `CRAWLED_NOT_INDEXED`, `DISCOVERED_NOT_INDEXED`, `URL_IS_UNKNOWN_TO_GOOGLE`). C'est la seule facon de savoir si les 38 fiches wiki sont indexees ou non.

5. **Densifier ou fusionner les 10 fiches wiki sous 300 mots**, et donner un `<h1>` a `/accompagnement-1-1-30-jours`. Effort : editorial. Impact : indirect, a traiter apres avoir su (P4) si ces fiches sont indexees.

## Limites de ce rapport

- **Indexation reelle non mesuree.** `searchAnalytics` dit qu'une page a ete servie, pas qu'elle est indexee. Les 49 pages a impressions sont indexees avec certitude. Les 97 autres sont indeterminees : aucune ne peut etre declaree « non indexee » sur cette base.
- **Fenetre de 28 jours.** Une page publiee recemment, ou saisonniere, peut etre indexee et a zero impression sur la periode.
- **Scraping `site:` inexploitable** : Google sert une coquille a redirection JS, sans SERP. Marque « non testable », jamais « non indexee ».
- **Perimetre = sitemap.** Une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. `/manifeste/` n'a ete trouvee que parce que la GSC la remontait.
- **Maillage interne calcule sur les 146 pages du sitemap uniquement.** Un lien depuis une page hors sitemap ne serait pas compte. Les 2 orphelines ont ete reverifiees par grep sur le HTML des 146 pages.
- Un premier passage HTTP en parallele (8 requetes simultanees) a perdu 29 reponses. Elles ont ete rejouees en sequentiel : les 146 repondent bien `200`. Aucun echec reel.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]].
Methode : [[gsc-export]], [[maillage-interne]].
