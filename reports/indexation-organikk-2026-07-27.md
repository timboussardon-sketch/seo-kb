---
type: audit
title: "Audit indexation Organikk - 2026-07-27 (site complet, sitemap stable 330 URLs)"
date: 2026-07-27
perimetre: "https://organikk.co - 330 URLs du sitemap (site entier)"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1", "wordcount HTML body via strip regex", "graphe interne calcule sur les 330 pages"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 330
anomalies_critiques: 2
anomalies_mineures: 5
loop: indexation-check
---

# Audit indexation Organikk - 2026-07-27

## Synthese

Semaine de digestion apres le scale-up de la semaine derniere. **Sitemap stable a 330 URLs (delta 0 vs 2026-07-20)**. Trajectoire 49 jours : 169 -> 136 -> 143 -> 143 -> 146 -> 146 -> 330 -> 330. Rien n'a bouge cote structure : ni ajout de section, ni suppression. Les fondamentaux tiennent : **330/330 en HTTP 200 final, 330/330 avec canonical strictement egal a l'URL finale, aucun `noindex` (`meta robots` + echantillon `X-Robots-Tag` sur 30 URLs), aucune page bloquee par `robots.txt`, `<title>` present sur 330/330**.

Les deux anomalies critiques ouvertes depuis le 10/07 sont toujours la, pour la 4e fois consecutive : **`/manifeste{,/}` reste en `HTTP 404` (17 jours d'ouverture)** et **`/accompagnement-seo-geo/` reste orpheline sur les 330 pages du sitemap (17 jours)**. Aucun signe d'action cote site.

Cote sitemap, les deux recurrences structurelles atteignent leur 8e occurrence : `sitemap_canonical_mismatch` (329/330 URLs redirigent en 301 vers leur variante slash final) et `lastmod_uniforme` (330/330 a `2026-07-27T04:49:02.855Z`, date du dernier build). Les P1 et P2 sont ouvertes depuis le 15/06, soit 42 jours sans effet observable.

Statut d'indexation Google : **non teste ce run** (pas d'acces a l'edge `admin-gsc-export` depuis cet environnement). Derniere mesure fiable : 10/07 (49/146 confirmees, 97 indeterminees). Sur les 330 URLs actuelles, aucune ne peut etre declaree "non indexee" (`non testable` != `non indexee`, cf. Limites). Le diff `urlInspection API` reste en attente dans `memory/questions.md` depuis le 10/07.

Robots.txt inchange.

Verifications validees sur 330/330 :
- `HTTP 200` final apres redirections
- Absence de `noindex` en `meta` HTML
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **329 / 330** (301 vers le slash final ; seule la racine echappe)
- `lastmod` uniforme sur tout le sitemap : **330 / 330** (`2026-07-27T04:49:02.855Z`)
- Pages orphelines (0 lien interne entrant) : **2 / 330** (identiques aux 3 runs precedents)
- Pages sous-maillees (1 seul lien entrant) : **62 / 330** (18.8 %, identique au 20/07)
- Pages sans `<h1>` : **1 / 330** (`/accompagnement-1-1-30-jours/`)
- Contenu sous 300 mots : **18 / 330** (+1 vs 20/07 : `/contact/` apparait au comptage brut)
- Page critique en 404 : **1** (`/manifeste/`)

## Anomalies critiques

### C1. `/manifeste{,/}` toujours 404 - 4e recurrence

`curl -sIL https://organikk.co/manifeste/` renvoie `HTTP/2 404`. Meme reponse sans slash. La page n'est pas dans le sitemap. Aucun `<a href>` vers `/manifeste` sur les 330 pages du site : 0 backlink interne apres crawl du sitemap complet.

Reco P1 du 10/07 (redirection 301 `/manifeste{,/} -> /methode/`) : non appliquee. **17 jours d'ouverture**. Au 10/07, la GSC comptait 30 impressions sur 28 jours sur cette URL (2e page du site en impressions). Sans reprise de la mesure GSC ce run, on ne sait pas si Google la sert encore ou l'a fait tomber, mais tant que la 404 est en place chaque impression eventuelle est perdue.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne dans `_redirects` / `netlify.toml`. Jamais de 410.

### C2. `/accompagnement-seo-geo/` toujours orpheline - 4e recurrence

Verifie par crawl des 330 pages du sitemap : la chaine `accompagnement-seo-geo` n'apparait que sur sa propre page (1 fichier sur 330, auto-reference).

Page d'offre, `HTTP 200`, canonical propre. Le corpus n'a pas bouge cette semaine et le maillage entrant non plus. Elle reste decouvrable uniquement par le sitemap.

Reco C2 du 10/07 (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) : non appliquee. Grep confirme sur les trois hubs cibles.

Action inchangee : trois liens ancre naturels depuis les trois hubs.

## Anomalies mineures

### M1. Sitemap declare 329 URLs non canoniques - 8e recurrence

329 des 330 `<loc>` du sitemap sont declares sans slash final. Le serveur renvoie `301` vers `<path>/` sur les 329. Seule exception : la racine `https://organikk.co`, sans chemin, qui repond 200 directement.

Le canonical du DOM pointe correctement vers la version avec slash sur 330/330. Aucun risque d'indexation duale, mais chaque URL du sitemap coute un aller-retour de crawl inutile. Le probleme reste au meme niveau que le 20/07 (329 requetes inutiles par crawl), stable depuis le scale-up.

P1 ouverte depuis le 15/06, sans effet observable apres **42 jours**.

### M2. `lastmod` uniforme sur 330/330 - 8e recurrence

Toutes les URLs portent `2026-07-27T04:49:02.855Z`, date du dernier build. `uniq -c` sur les `<lastmod>` renvoie une seule ligne : 330 occurrences. Meme pattern qu'aux 7 runs precedents. Google apprend a ignorer ce champ.

Sans granularite par page, la priorisation du re-crawl repose entierement sur les signaux Google (backlinks, popularite, engagement) sans aucun signal serveur. C'est particulierement penalisant pour les sections recentes (`guide-evaluateurs-google`, `mises-a-jour-google`, `statuts-indexation-google`, `robots-ia`) qui doivent se faire une place dans l'index sans indice de fraicheur.

P2 ouverte depuis le 15/06, sans effet observable apres **42 jours**.

### M3. `/secteurs/` reste orpheline et mince - 4e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`), **287 mots** (vs 293 au 20/07, vs 270 au 13/07, vs 109 au 10/07). Le contenu a legerement baisse cette semaine (-6 mots au comptage brut), toujours zero lien interne entrant.

Action inchangee : soit vraie densification et maillage depuis 2 pages amont minimum, soit retrait du sitemap.

### M4. `/accompagnement-1-1-30-jours/` : 165 mots, pas de `<h1>` - 4e recurrence

Seule page du site sans `<h1>` sur 330. **165 mots** (vs 170 au 20/07, 163 au 13/07). Tunnel de quiz.

Action inchangee : ajouter un `<h1>` au premier ecran du quiz. Une balise.

### M5. Section `/robots-ia/` : 12/14 pages sous 300 mots - toujours en attente d'arbitrage

Meme etat que le 20/07 : 12 des 14 pages entre 248 et 298 mots au comptage brut, 2 tout juste au-dessus. Aucune modification observable en une semaine. Rappel : c'est un choix editorial recent (14 pages ajoutees la semaine du 13->20/07), format probablement pSEO "un template + une variable bot".

La reco reste ouverte : soit assumer le format court comme reponse Know-Simple et le documenter en interne, soit densifier chaque fiche a >=400 mots avec du terrain (user-agent exact, comportement observe, doctrine Organikk sur chaque bot). Point a trancher par Tim au vendredi.

## Observations positives

**Le corpus wiki reste stable au-dessus de 400 mots.** 56 fiches, moyenne 577 mots, min 411, max 1893. **Aucune fiche wiki n'est desormais sous 400 mots** (vs 55/56 au 20/07). Echantillon verifie : `core-web-vitals` 411, `titans-architecture` 511, `muvera` 443, `pillar-page` 492, `silo-seo` 449. Aucune regression detectee sur le corpus wiki.

**Aucune anomalie technique nouvelle detectee.** HTTP 200 sur 330/330, canonical == URL finale sur 330/330, echantillon X-Robots-Tag sur 30 URLs sans en-tete. La sante technique globale tient sur un corpus qui a double en un mois puis s'est stabilise.

**Pas de nouvelle orpheline apparue.** Les 2 orphelines identifiees (`/accompagnement-seo-geo/`, `/secteurs/`) sont les memes que les 3 runs precedents. Aucune des 62 pages sous-maillees n'est passee a zero lien entrant cette semaine.

## Autres observations

**62 pages sous-maillees (1 seul lien entrant), meme repartition que le 20/07** :
- `/guide-evaluateurs-google/*` : 32 sur 103 (le hub distribue vers 103 enfants, mais 32 enfants n'ont *que* ce lien, aucune reference croisee entre chapitres freres)
- `/newsletter/*` : 18 sur 29
- `/strategies/*` : 5 sur 15
- `/actualites/*` : 3 sur 4
- 4 pages isolees (`/bootcamp-quiz/`, `/bootcamp/programme/`, `/freelance-geo-lyon/`, `/resultats/`)

La distribution des liens entrants dans `/guide-evaluateurs-google/*` fait apparaitre un pattern regulier : 32 pages a 1 lien, 6 a 2, 3 a 3, puis des paliers (8 a 4, 8 a 8, 13 a 9, 8 a 11, 8 a 12, 8 a 15, 8 a 19). Le pattern par groupes de 8 suggere que le maillage transverse existe mais sur des sous-ensembles specifiques (probablement les sections thematiques du QRG), pas de facon uniforme. Les 32 pages isolees semblent etre les feuilles les plus profondes.

Aucune section nouvelle detectee cette semaine. **Pas de nouvelle matiere premiere pour la boucle apprentissage sur ce cote-la.**

**Scraping `site:` sur Google : toujours retire de l'audit.** Le check #8 du skill reste desactive tant que Tim n'a pas tranche le diff propose (`loops/indexation-check/memory/questions.md`, en attente depuis le 10/07).

## Recommandations priorisees

1. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. **4e reconduite consecutive.** Une ligne dans `_redirects`. C'est toujours le seul point urgent : la page morte est servie a chaque impression Google (mesuree a 30 imp / 28j au 10/07, non re-mesuree ce run).

2. **Mailler `/accompagnement-seo-geo/`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. **4e reconduite consecutive.** Trois liens ancre.

3. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (**42 jours d'ouverture**). Le generateur de sitemap est le seul livrable. Le cout du non-fait double sur les sections pSEO recentes qui perdent leur signal de fraicheur.

4. **Ajouter du maillage transverse dans `/guide-evaluateurs-google/`.** Le hub distribue bien vers 103 enfants, mais 32 enfants n'ont *que* ce lien. Priorite : liens "chapitre precedent / chapitre suivant" (ordre du QRG) sur les 103 pages, plus quelques references croisees explicites entre concepts lies (une dizaine). Reconduite du 20/07.

5. **Trancher sur `/robots-ia/`.** 14 pages, 12 sous 300 mots. Reconduite du 20/07. Reponse a demander a Tim au vendredi.

6. **Ajouter un `<h1>` a `/accompagnement-1-1-30-jours/`.** Une balise. **4e reconduite.** La reco ne coute rien.

7. **Trancher sur `/secteurs/`** : soit hub reel (>=600 mots, maille depuis 2 pages amont minimum, avec `<h2>` par secteur), soit retrait du sitemap. **4e reconduite.**

8. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). Sans ca, l'audit reste aveugle sur la couverture d'indexation d'un corpus qui a double en un mois. **17 jours d'ouverture pour ce debloqueur systeme.**

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Sur les 330 URLs actuelles, aucune ne peut etre declaree "non indexee". Aucune estimation n'a ete inventee (§10 regle 4). L'ecart `non indexee` / `non testable` est explicite.
- **X-Robots-Tag verifie sur echantillon de 30 URLs**, pas sur les 330. Aucun `noindex` server-side dans l'echantillon (aucun en-tete X-Robots-Tag detecte, meme benin).
- **Fenetre de decouverte = sitemap.** Comme au 20/07, une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. C'est exactement ce qui s'est passe pour `/manifeste` au 10/07 (rattrapee uniquement par la mesure GSC). Sans reprise de la mesure GSC, cette classe de bug redevient invisible.
- **Maillage calcule sur les 330 pages du sitemap uniquement.** Un lien depuis une page hors sitemap ne serait pas compte.
- **Sections pSEO recentes non evaluees qualitativement.** Ce run mesure la sante technique (HTTP, canonical, robots, wordcount, backlinks) mais pas la qualite editoriale ni la differentiation vecteurs des 103 pages `/guide-evaluateurs-google/*` ni des 14 pages `/robots-ia/*`. C'est le boulot du skill `seo-cluster-aeo` ou d'un vrai audit editorial, pas de celui-ci.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]], [[reports/indexation-organikk-2026-07-13]], [[reports/indexation-organikk-2026-07-20]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator).
