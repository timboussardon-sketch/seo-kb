---
type: audit
title: "Audit indexation Organikk - 2026-08-03 (site complet, sitemap 332 URLs, M4 applique)"
date: 2026-08-03
perimetre: "https://organikk.co - 332 URLs du sitemap (site entier)"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1", "wordcount HTML body via strip regex", "graphe interne calcule sur les 331 pages telechargees"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 332
anomalies_critiques: 2
anomalies_mineures: 5
loop: indexation-check
---

# Audit indexation Organikk - 2026-08-03

## Synthese

Sitemap a **332 URLs (+2 vs 2026-07-27)**. Trajectoire 56 jours : 169 -> 136 -> 143 -> 143 -> 146 -> 146 -> 330 -> 330 -> 332. Semaine de mouvements internes plutot que de scale : le total est quasi stable, mais la composition a change (wiki 56 -> 55, un fichier retire ; +2 URLs recuperees ailleurs). Les fondamentaux tiennent : **332/332 en HTTP 200 final, 331/331 avec canonical strictement egal a l'URL finale, aucun `noindex` (`meta robots` + echantillon `X-Robots-Tag` sur 30 URLs), aucune page bloquee par `robots.txt`, `<title>` present sur 331/331, `<h1>` present sur 331/331**.

**Une reco a ete appliquee cette semaine (premiere fois depuis le 13/07)** : la M4 sur `/accompagnement-1-1-30-jours/` est fermee. La page a maintenant un `<h1>` (`Votre systeme SEO proprietaire pour ranker sur Google et les LLM, sans repartir de zero`) et pese **1313 mots** (vs 165 au 27/07, +1148). C'est plus qu'un correctif : la page a ete entierement refondue. Detail plus bas.

Les deux anomalies critiques ouvertes depuis le 10/07 sont toujours la, pour la 5e fois consecutive : **`/manifeste{,/}` reste en `HTTP 404` (24 jours d'ouverture)** et **`/accompagnement-seo-geo/` reste orpheline sur les 331 pages crawlees (24 jours)**. Aucun signe d'action cote site pour ces deux points.

Cote sitemap, les deux recurrences structurelles atteignent leur **9e occurrence** : `sitemap_canonical_mismatch` (331/332 URLs redirigent en 301 vers leur variante slash final) et `lastmod_uniforme` (332/332 a `2026-08-03T05:17:36.121Z`, date du dernier build). Les P1 et P2 sont ouvertes depuis le 15/06, soit **49 jours** sans effet observable.

Statut d'indexation Google : **non teste ce run** (pas d'acces a l'edge `admin-gsc-export` depuis cet environnement). Derniere mesure fiable : 10/07 (49/146 confirmees, 97 indeterminees). Sur les 332 URLs actuelles, aucune ne peut etre declaree "non indexee" (`non testable` != `non indexee`, cf. Limites). Le diff `urlInspection API` reste en attente dans `memory/questions.md` depuis le 10/07 : **24 jours d'ouverture pour ce debloqueur systeme**.

Robots.txt inchange (3 sections Disallow : `/dashboard-bootcamp-organikk-private-2026/`, `/espace-leexi/`, `/espace-fgformation/`).

Verifications validees sur 331/331 pages telechargees :
- `HTTP 200` final apres redirections (mesure sur 332/332 URLs via curl)
- Absence de `noindex` en `meta` HTML
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- `<h1>` present (versus 330/331 au 27/07 : la seule page sans h1 a ete corrigee)
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **331 / 332** (301 vers le slash final ; seule la racine echappe)
- `lastmod` uniforme sur tout le sitemap : **332 / 332** (`2026-08-03T05:17:36.121Z`)
- Pages orphelines (0 lien interne entrant) : **2 / 331** (identiques aux 4 runs precedents)
- Pages sous-maillees (1 seul lien entrant) : **62 / 331** (18.7 %, meme repartition que 20/07 et 27/07)
- Contenu sous 300 mots : **18 / 331** (identique au 27/07, sans le repli du corpus `/contact/` deja au comptage precedent)
- Page critique en 404 : **1** (`/manifeste/`)

## Anomalies critiques

### C1. `/manifeste{,/}` toujours 404 - 5e recurrence

`curl -sIL https://organikk.co/manifeste/` renvoie `HTTP/2 404`. Meme reponse sans slash. La page n'est pas dans le sitemap. Aucun `<a href>` vers `/manifeste` sur les 331 pages crawlees : 0 backlink interne confirme par grep sur `pages/*.html`.

Reco P1 du 10/07 (redirection 301 `/manifeste{,/} -> /methode/`) : non appliquee. **24 jours d'ouverture**. Au 10/07, la GSC comptait 30 impressions sur 28 jours sur cette URL (2e page du site en impressions). Sans reprise de la mesure GSC ce run, on ne sait pas si Google la sert encore ou l'a fait tomber, mais tant que la 404 est en place chaque impression eventuelle est perdue.

Action inchangee : `301 /manifeste{,/} -> /methode/`. Une ligne dans `_redirects` / `netlify.toml`. Jamais de 410.

### C2. `/accompagnement-seo-geo/` toujours orpheline - 5e recurrence

Verifie par crawl des 331 pages : la chaine `accompagnement-seo-geo` n'apparait que sur sa propre page (1 fichier sur 331, auto-reference).

Page d'offre solide (`HTTP 200`, canonical propre, `1533 mots`, `h1` : *Remonter sur Google et etre cite par les IA*, `title` : *Accompagnement SEO + GEO pour PME*). Elle reste decouvrable uniquement par le sitemap.

Reco C2 du 10/07 (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) : non appliquee. Verification : la refonte de `/accompagnement-1-1-30-jours/` cette semaine (nouvelle version a 1313 mots) aurait ete la meilleure occasion d'ajouter le lien vers `/accompagnement-seo-geo/`. Aucun lien n'a ete pose. Grep sur la page refondue = 0 occurrence de `accompagnement-seo-geo`.

Action inchangee : trois liens ancre naturels depuis les trois hubs. **Le contexte de refonte de `/accompagnement-1-1-30-jours/` renforce l'urgence : les deux pages parlent du meme sujet, l'une pointe deja vers l'autre en logique produit.**

## Anomalies mineures

### M1. Sitemap declare 331 URLs non canoniques - 9e recurrence

331 des 332 `<loc>` du sitemap sont declares sans slash final. Le serveur renvoie `301` vers `<path>/` sur les 331. Seule exception : la racine `https://organikk.co`, sans chemin. La `num_redirects=0` cote curl est trompeuse (curl affiche `url_effective` avec slash mais ne compte pas la redirection cote racine), mais c'est bien un cas trivial : la racine repond directement.

Le canonical du DOM pointe correctement vers la version avec slash sur 331/331. Aucun risque d'indexation duale, mais chaque URL du sitemap coute un aller-retour de crawl inutile. Le probleme est stable au niveau du 27/07 (331 requetes inutiles par crawl, +2 vs 329 la semaine derniere du fait des 2 URLs ajoutees).

P1 ouverte depuis le 15/06, sans effet observable apres **49 jours**.

### M2. `lastmod` uniforme sur 332/332 - 9e recurrence

Toutes les URLs portent `2026-08-03T05:17:36.121Z`, date du dernier build. `uniq -c` sur les `<lastmod>` renvoie une seule ligne : 332 occurrences. Meme pattern qu'aux 8 runs precedents. Google apprend a ignorer ce champ.

Sans granularite par page, la priorisation du re-crawl repose entierement sur les signaux Google (backlinks, popularite, engagement) sans aucun signal serveur. Particulierement penalisant sur `/guide-evaluateurs-google/*` (103 pages) et `/statuts-indexation-google/*` (17 pages) : contenu de reference qui devrait etre marque *stable / mis a jour rarement*, envoye sans distinction avec des mises a jour reelles.

P2 ouverte depuis le 15/06, sans effet observable apres **49 jours**.

### M3. `/secteurs/` reste orpheline et mince - 5e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`), **283 mots** (vs 287 au 27/07, vs 293 au 20/07, vs 270 au 13/07, vs 109 au 10/07). Le comptage brut baisse encore legerement (-4 mots), toujours zero lien interne entrant.

Action inchangee : soit vraie densification et maillage depuis 2 pages amont minimum, soit retrait du sitemap.

### M4 FERMEE. `/accompagnement-1-1-30-jours/` : h1 present, 1313 mots

**Reco appliquee.** La page a un `<h1>` (`Votre systeme SEO proprietaire pour ranker sur Google et les LLM, sans repartir de zero`), unique. Wordcount **1313** (vs 165 au 27/07, 170 au 20/07, 163 au 13/07). C'est +1148 mots en une semaine, la page est manifestement refondue.

L'anomalie initiale (une balise `<h1>` manquante sur 1 page sur 330) est corrigee, et le probleme adjacent (page trop mince : 165 mots) l'est aussi par la meme occasion.

Reste ouvert cote texte : le `<title>` de la page est `Coaching SEO` alors que le `<h1>` parle de "systeme SEO proprietaire pour ranker sur Google et les LLM". Divergence title / h1 a signaler comme observation (pas une anomalie technique bloquante), a arbitrer par Tim ; probablement un vestige de l'ancienne version.

**M4 sortie du registre a partir du prochain run.**

### M5. Section `/robots-ia/` : 13/13 pages sous 300 mots - 3e occurrence, avec regression apparente

Deux mouvements depuis le 27/07 :
1. Une des 14 pages a ete retiree du sitemap (13 URLs vs 14).
2. Les 13 restantes sont **toutes** sous 300 mots au comptage brut (vs 12/14 au 27/07). Fourchette 245-295, moyenne 265.

C'est desormais 100 % de la section qui reste mince, sur un format `pSEO template + variable bot`. La reco du 20/07 (soit assumer format Know-Simple court, soit densifier a >=400 mots avec doctrine Organikk) reste ouverte. Point a trancher par Tim au vendredi.

## Observations positives

**M4 appliquee - premiere reco cloturee depuis le 13/07.** `/accompagnement-1-1-30-jours/` a ete refondue : `<h1>` ajoute, +1148 mots. Bonne nouvelle sur le rythme, meme si les deux critiques et les deux mineures de sitemap restent ouvertes.

**Le corpus wiki reste stable au-dessus de 400 mots**, malgre le retrait d'une fiche (55 vs 56 au 27/07). Moyenne 550 mots, min 411 (`core-web-vitals`), max 698. Aucune fiche sous 400 mots. Echantillon verifie : `core-web-vitals` 411, `titans-architecture` 511, `muvera` 440, `pillar-page` 492, `silo-seo` 446.

**Aucune anomalie technique nouvelle detectee.** HTTP 200 sur 332/332, canonical == URL finale sur 331/331 pages crawlees, echantillon `X-Robots-Tag` sur 30 URLs sans en-tete, `<h1>` present sur 331/331. La sante technique globale tient sur le corpus stabilise.

**Pas de nouvelle orpheline apparue.** Les 2 orphelines identifiees (`/accompagnement-seo-geo/`, `/secteurs/`) sont les memes que les 4 runs precedents. Aucune des 62 pages sous-maillees n'est passee a zero lien entrant.

## Autres observations

**Section `/statuts-indexation-google/` : 3 pages sur 16 sous 300 mots** (`erreur-de-redirection` 282, `soft-404` 284, `erreur-de-serveur-5xx` 298 ; les 13 autres entre 304 et 352). C'est un signal mineur, mais coherent avec le pattern `pSEO template court` observe sur `/robots-ia/`. Point a garder en tete si Tim doit trancher la question format court vs densifie.

**62 pages sous-maillees (1 seul lien entrant), meme repartition que les deux runs precedents** :
- `/guide-evaluateurs-google/*` : 32 sur 103 (le hub distribue vers 103 enfants, mais 32 enfants n'ont *que* ce lien, aucune reference croisee entre chapitres freres)
- `/newsletter/*` : 18 sur 29
- `/strategies/*` : 5 sur 15
- `/actualites/*` : 3 sur 4
- 4 pages isolees (`/bootcamp-quiz/`, `/bootcamp/programme/`, `/freelance-geo-lyon/`, `/resultats/`)

Aucun mouvement sur le maillage transverse en une semaine. Reco 4 (chapitre precedent / suivant sur `/guide-evaluateurs-google/*`) reconduite.

**Divergence title/h1 sur la page refondue `/accompagnement-1-1-30-jours/`** : title = `Coaching SEO`, h1 = `Votre systeme SEO proprietaire pour ranker sur Google et les LLM, sans repartir de zero`. A verifier : est-ce voulu (deux angles differents pour deux publics) ou vestige de la version precedente ? Pas une anomalie technique, mais Google et les LLM utilisent les deux comme signaux d'intention et une divergence forte peut brouiller.

**Aucune section nouvelle detectee cette semaine.** Pas de nouvelle matiere premiere pour la boucle apprentissage sur ce cote-la.

**Delta sitemap +2 sans changement de sections observable** : les sections principales gardent leurs volumes (guide 103, wiki 56 hub inclus, newsletter 29, mises-a-jour 27, statuts 17, robots-ia 14, glossaire 7, outils 5). Le +2 se joue sur des pages annexes ou du bruit de comptage. Pas d'action.

**Scraping `site:` sur Google : toujours retire de l'audit.** Le check #8 du skill reste desactive tant que Tim n'a pas tranche le diff propose (`loops/indexation-check/memory/questions.md`, en attente depuis le 10/07).

## Recommandations priorisees

1. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. **5e reconduite consecutive.** Une ligne dans `_redirects`. Toujours le seul point urgent : la page morte est servie a chaque impression Google (mesuree a 30 imp / 28j au 10/07, non re-mesuree ce run).

2. **Mailler `/accompagnement-seo-geo/`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. **5e reconduite consecutive.** Trois liens ancre. **Contexte renforce** : la refonte cette semaine de `/accompagnement-1-1-30-jours/` (1313 mots) etait l'occasion la plus naturelle d'ajouter le lien, aucun n'a ete pose. Les deux pages parlent du meme service, il faut les relier.

3. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (**49 jours d'ouverture**). Le generateur de sitemap est le seul livrable.

4. **Ajouter du maillage transverse dans `/guide-evaluateurs-google/`.** Reconduite du 20/07. Priorite : liens "chapitre precedent / chapitre suivant" (ordre du QRG) sur les 103 pages, plus quelques references croisees explicites entre concepts lies (une dizaine). Ratio inchange en 14 jours.

5. **Trancher sur `/robots-ia/`.** 13 pages, **13/13 sous 300 mots** apres retrait d'une page. Reconduite du 20/07. Reponse a demander a Tim au vendredi. Meme question qui pourrait se poser pour `/statuts-indexation-google/` (3 pages sur 16 dans la meme zone), a garder en tete.

6. **Trancher sur `/secteurs/`** : soit hub reel (>=600 mots, maille depuis 2 pages amont minimum, avec `<h2>` par secteur), soit retrait du sitemap. **5e reconduite.**

7. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). **24 jours d'ouverture pour ce debloqueur systeme.** Sans ca, l'audit reste aveugle sur la couverture d'indexation.

8. **Aligner title et h1 sur `/accompagnement-1-1-30-jours/`** (title = `Coaching SEO`, h1 = `Votre systeme SEO proprietaire...`). Observation post-refonte, priorite basse. Une ligne HTML.

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Sur les 332 URLs actuelles, aucune ne peut etre declaree "non indexee". Aucune estimation n'a ete inventee (§10 regle 4). L'ecart `non indexee` / `non testable` est explicite.
- **X-Robots-Tag verifie sur echantillon de 30 URLs**, pas sur les 332. Aucun `noindex` server-side dans l'echantillon (aucun en-tete X-Robots-Tag detecte, meme benin).
- **331 pages telechargees sur 332 URLs** (une collision de slug entre deux URLs). Le manquant est probablement une page de bootcamp ou d'un sous-chemin similaire. Ecart negligeable pour le calcul de backlinks (< 0.3 %), mais signale.
- **Fenetre de decouverte = sitemap.** Comme aux 4 runs precedents, une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. C'est exactement ce qui s'est passe pour `/manifeste` au 10/07 (rattrapee uniquement par la mesure GSC). Sans reprise de la mesure GSC, cette classe de bug redevient invisible.
- **Maillage calcule sur les 331 pages telechargees uniquement.** Un lien depuis une page hors sitemap ne serait pas compte.
- **Sections pSEO recentes non evaluees qualitativement.** Ce run mesure la sante technique (HTTP, canonical, robots, wordcount, backlinks) mais pas la qualite editoriale ni la differentiation vecteurs des 103 pages `/guide-evaluateurs-google/*` ni des 14 pages `/robots-ia/*` ni des 17 pages `/statuts-indexation-google/*`. C'est le boulot du skill `seo-cluster-aeo` ou d'un vrai audit editorial, pas de celui-ci.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]], [[reports/indexation-organikk-2026-07-13]], [[reports/indexation-organikk-2026-07-20]], [[reports/indexation-organikk-2026-07-27]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator).
