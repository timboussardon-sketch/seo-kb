---
type: audit
title: "Audit indexation Organikk - 2026-07-20 (site complet, sitemap x2 en 7 jours)"
date: 2026-07-20
perimetre: "https://organikk.co - 330 URLs du sitemap (site entier, 3e run hors /wiki)"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1", "wordcount HTML body via strip regex", "graphe interne calcule sur les 330 pages"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 330
anomalies_critiques: 2
anomalies_mineures: 5
loop: indexation-check
---

# Audit indexation Organikk - 2026-07-20

## Synthese

Evenement structurant de la semaine : **le sitemap passe de 146 a 330 URLs, +184 en 7 jours**. Trajectoire 42 jours : 169 -> 136 -> 143 -> 143 -> 146 -> 146 -> 330. C'est le premier vrai mouvement scale-up depuis l'ouverture de la boucle. Trois sections nouvelles portent l'essentiel : `/guide-evaluateurs-google/` (103 pages, decoupage du QRG), `/mises-a-jour-google/` (27 pages, historique des updates), `/statuts-indexation-google/` (17 pages, un statut par cas). Deux plus petites : `/robots-ia/` (14 pages, une par bot) et `/glossaire/` (7 pages). Le wiki gagne aussi 16 fiches (40 -> 56).

Les fondamentaux tiennent sur ce nouveau volume : **330/330 en HTTP 200 final, 330/330 avec canonical strictement egal a l'URL finale, aucun `noindex` (`meta robots` + `X-Robots-Tag` verifie sur echantillon de 30), aucune page bloquee par `robots.txt`**. Aucun soft-404 detecte au parcours. Aucune page servie a moins de 170 mots.

En revanche, **les deux anomalies critiques ouvertes depuis le 10/07 ne sont toujours pas corrigees, pour la 3e fois consecutive** : `/manifeste/` reste en `HTTP 404` (10 jours d'ouverture), `/accompagnement-seo-geo/` reste orpheline (10 jours). Le scale-up editorial ne s'est pas accompagne de l'action minimale sur ces deux points.

Recurrences structurelles sur le sitemap : `sitemap_canonical_mismatch` (7e recurrence, 329/330), `lastmod_uniforme` (7e recurrence, 330/330 a la date de build), P1 et P2 ouvertes depuis le 15/06, sans effet observable apres 35 jours.

Statut d'indexation Google : **non teste ce run** (pas d'acces a l'edge `admin-gsc-export` depuis cet environnement). Derniere mesure fiable : 10/07, 49/146 confirmees. Le corpus vient de doubler : la question de la couverture d'indexation devient plus urgente, elle sera aveugle tant que la variante GSC / `urlInspection` du skill n'est pas ecrite (diff en attente dans `memory/questions.md`).

Robots.txt inchange.

Verifications validees sur 330/330 :
- `HTTP 200` final apres redirections
- Absence de `noindex` en `meta` HTML
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **329 / 330** (301 vers le slash final ; seule la racine echappe)
- `lastmod` uniforme sur tout le sitemap : **330 / 330** (`2026-07-18T04:37:53.988Z`)
- Pages orphelines (0 lien interne entrant) : **2 / 330** (identiques au run precedent)
- Pages sous-maillees (1 seul lien entrant) : **62 / 330** (18.8 %)
- Pages sans `<h1>` : **1 / 330** (`/accompagnement-1-1-30-jours/`)
- Contenu sous 300 mots : **17 / 330**
- Page critique en 404 : **1** (`/manifeste/`)

## Anomalies critiques

### C1. `/manifeste{,/}` toujours 404 - 3e recurrence

`curl -sIL https://organikk.co/manifeste/` renvoie `HTTP/2 404`. Meme reponse sans slash. La page n'est pas dans le sitemap. Aucun `<a href>` vers `/manifeste` sur les 330 pages du site : 0 backlink interne apres crawl du sitemap complet.

Reco P1 du 10/07 (redirection 301 `/manifeste{,/} -> /methode/`) : non appliquee. 10 jours d'ouverture, alors qu'au 10/07 la GSC comptait 30 impressions sur 28 jours sur cette URL (2e page du site en impressions a l'epoque). Chaque impression sert une page d'erreur. La ligne de redirection n'est toujours pas dans `_redirects` / `netlify.toml`.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne. Jamais de 410.

### C2. `/accompagnement-seo-geo/` toujours orpheline - 3e recurrence

Verifie par crawl des 330 pages du sitemap : la chaine `accompagnement-seo-geo` n'apparait que sur sa propre page (1 fichier sur 330, auto-reference).

Page d'offre, `HTTP 200`, canonical propre. Le doublement du sitemap n'a rien change ici : aucune des 184 pages ajoutees ne pointe vers cette URL. Elle reste decouvrable uniquement par le sitemap.

Reco C2 du 10/07 (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) : non appliquee. Grep confirme sur les trois hubs cibles.

Action inchangee : trois liens ancre naturels depuis les trois hubs.

## Anomalies mineures

### M1. Sitemap declare 329 URLs non canoniques - 7e recurrence

329 des 330 `<loc>` du sitemap sont declares sans slash final. Le serveur renvoie `301` vers `<path>/` sur les 329. Seule exception : la racine `https://organikk.co`, sans chemin, qui repond 200 directement.

Le canonical du DOM pointe correctement vers la version avec slash sur 330/330. Aucun risque d'indexation duale, mais chaque URL du sitemap coute un aller-retour de crawl inutile. Le probleme s'aggrave mecaniquement avec le scale-up : 329 requetes inutiles par crawl complet au lieu de 145 au run precedent.

P1 ouverte depuis le 15/06, sans effet observable apres 35 jours.

### M2. `lastmod` uniforme sur 330/330 - 7e recurrence

Toutes les URLs portent `2026-07-18T04:37:53.988Z`, date du dernier build. `uniq -c` sur les `<lastmod>` renvoie une seule ligne : 330 occurrences. Meme pattern qu'aux 6 runs precedents. Google apprend a ignorer ce champ.

Cette anomalie devient plus couteuse avec le scale-up : sur 330 pages dont une bonne partie sont fraiches, Google n'a aucun moyen de trier ce qui vient de bouger. La priorisation du re-crawl repose desormais entierement sur ses propres signaux (backlinks, popularite, engagement) sans aucun signal serveur.

P2 ouverte depuis le 15/06, sans effet observable apres 35 jours.

### M3. `/secteurs/` reste orpheline et mince - 3e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`), 293 mots (vs 270 au 13/07, vs 109 au 10/07), toujours zero lien interne entrant. Le contenu monte lentement mais le maillage entrant ne bouge pas.

Action : soit vraie densification et maillage depuis 2 pages amont minimum, soit retrait du sitemap. Meme reco qu'au 13/07.

### M4. `/accompagnement-1-1-30-jours/` : 170 mots, pas de `<h1>` - 3e recurrence

Seule page du site sans `<h1>` sur 330. 170 mots (vs 163 au 13/07). Tunnel de quiz.

Action inchangee : ajouter un `<h1>` au premier ecran du quiz. Une balise.

### M5. Nouvelle section `/robots-ia/` : 14 pages, toutes entre 255 et 305 mots

Section ajoutee cette semaine. 14 pages format "une par bot" (`claude-user`, `chatgpt-user`, `amazonbot`, `perplexitybot`, `meta-externalagent`, `oai-searchbot`, `claudebot`, `perplexity-user`, `applebot-extended`, `ccbot`, `gptbot`, `bytespider`, `google-extended`, une 14e). 12 sur 14 sont sous 300 mots au comptage brut. Format probablement pSEO : un template + une variable bot.

Ce n'est pas une erreur d'audit, c'est un choix editorial recent qu'il faut trancher. Deux voies : soit assumer le format court comme reponse a une intention Know-Simple ("est-ce que le bot X respecte robots.txt ?", "quelles directives lui appliquer ?") et le documenter en interne, soit densifier chaque fiche a >=400 mots avec des elements distinctifs par bot (user-agent exact, comportement observe, gestion de la freshness, cas d'usage IA associe).

Rappel doctrinal : le seuil de 300 mots n'est pas magique, mais 12 pages sous 300 mots ajoutees en une semaine merite un statut explicite dans la doctrine du site.

## Observations positives

**Le progres editorial du 13/07 tient.** Les 11 fiches densifiees au dernier run sont toutes restees au-dessus de 400 mots (echantillon verifie : `core-web-vitals` 424, `titans-architecture` 520, `muvera` 451, `pillar-page` 501, `silo-seo` 458). Aucune regression, aucune reduction. Le corpus wiki est desormais stable au-dessus du seuil sur 55 des 56 fiches. Moyenne wiki : 563 mots.

**Aucune anomalie technique majeure sur les 184 pages ajoutees.** HTTP 200 final, canonical propre, absence de noindex, presence de `<h1>` et `<title>`. Le pipeline de generation a tenu la charge sur la marche editoriale la plus importante depuis l'ouverture de la boucle.

**Wiki : +16 fiches en 10 jours (40 -> 56).** Croissance du corpus doctrinal sans casser le maillage entrant : les nouvelles fiches wiki ne creent pas d'orphelines, ni de pages a 1 lien entrant. A verifier si elles sortent en impressions au prochain run avec GSC.

## Autres observations

**62 pages sous-maillees (1 seul lien entrant), soit 18.8 % du sitemap.** Repartition :
- `/guide-evaluateurs-google/*` : 32 sur 103 (le hub `/guide-evaluateurs-google/` recoit 105 liens entrants et distribue vers ses enfants, mais 32 enfants n'ont *que* ce lien du hub, aucune reference croisee entre chapitres frères)
- `/newsletter/*` : 18 sur 29 (meme pattern, une seule page de listing distribue)
- `/strategies/*` : 5 sur 15
- `/actualites/*` : 3 sur 4
- 4 pages isolees (`/bootcamp-quiz/`, `/bootcamp/programme/`, `/freelance-geo-lyon/`, `/resultats/`)

C'est une trajectoire attendue pour les sections `guide-evaluateurs-google` et `newsletter` en debut de vie : elles fonctionnent en etoile a partir du listing. Mais si le pari editorial est le pSEO (guide QRG decoupe en 103 pages), il faudra au minimum du maillage transverse "chapitre precedent / chapitre suivant" et des references entre concepts lies (ex : `experience-expertise-authoritativeness-trust` <-> `ymyl-experience-ou-expertise`) sinon Google traitera ces pages comme du contenu duplique en cluster.

**Nouvelles sections a documenter dans le vault :** `/guide-evaluateurs-google/*` (103), `/mises-a-jour-google/*` (27), `/statuts-indexation-google/*` (17), `/robots-ia/*` (14), `/glossaire/*` (7), `/outils/*` (5). C'est une matiere premiere neuve pour la boucle apprentissage, et une couverture nouvelle a suivre en indexation.

**Scraping `site:` sur Google : toujours retire de l'audit.** Le check #8 du skill reste desactive tant que Tim n'a pas tranche le diff propose (voir `memory/questions.md`, en attente depuis le 10/07).

## Recommandations priorisees

1. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. **3e reconduite consecutive.** Une ligne dans `_redirects`. C'est toujours le seul point urgent : la page morte est servie a chaque impression Google.

2. **Mailler `/accompagnement-seo-geo/`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. **3e reconduite consecutive.** Trois liens ancre.

3. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (35 jours d'ouverture). Le probleme se paie maintenant au double : 329 requetes de crawl inutiles au lieu de 145. Le generateur de sitemap est le seul livrable.

4. **Ajouter du maillage transverse dans `/guide-evaluateurs-google/`.** Le hub distribue bien vers 103 enfants, mais 32 enfants n'ont *que* ce lien. Priorite : liens "chapitre precedent / chapitre suivant" (ordre du QRG) sur les 103 pages, plus quelques references croisees explicites entre concepts lies (une dizaine). Sinon la section est structurellement en danger de traitement "boilerplate".

5. **Trancher sur `/robots-ia/`.** 14 pages ajoutees cette semaine, 12 sous 300 mots. Soit assumer le format court comme reponse Know-Simple, soit densifier a >=400 mots avec du terrain (user-agent exact, comportement observe, doctrine Organikk sur chaque bot). Reponse a demander a Tim au vendredi.

6. **Ajouter un `<h1>` a `/accompagnement-1-1-30-jours/`.** Une balise. 3e reconduite. La reco ne coute rien.

7. **Trancher sur `/secteurs/`** : soit hub reel (>=600 mots, maille depuis 2 pages amont minimum, avec `<h2>` par secteur), soit retrait du sitemap. 3e reconduite.

8. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). Sans ca, l'audit est aveugle sur la couverture d'indexation d'un corpus qui vient de doubler. C'est le seul debloqueur qui manque au systeme.

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Sur les 330 URLs actuelles, aucune ne peut etre declaree "non indexee". Aucune estimation n'a ete inventee (§10 regle 4). L'ecart "non indexee" / "non testable" est explicite.
- **X-Robots-Tag verifie sur echantillon de 30 URLs**, pas sur les 330. Aucun `noindex` server-side dans l'echantillon (aucun en-tete X-Robots-Tag detecte, meme benin).
- **Fenetre de decouverte = sitemap.** Comme au 13/07, une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. C'est exactement ce qui s'est passe pour `/manifeste` au 10/07 (rattrapee uniquement par la mesure GSC). Sans reprise de la mesure GSC, cette classe de bug redevient invisible.
- **Maillage calcule sur les 330 pages du sitemap uniquement.** Un lien depuis une page hors sitemap ne serait pas compte.
- **Sections pSEO recentes non evaluees qualitativement.** Ce run mesure la sante technique (HTTP, canonical, robots, wordcount, backlinks) mais pas la qualite editoriale ni la differentiation vecteurs des 103 pages `/guide-evaluateurs-google/*`. C'est le boulot du skill `seo-cluster-aeo` ou d'un vrai audit editorial, pas de celui-ci.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]], [[reports/indexation-organikk-2026-07-13]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator).
