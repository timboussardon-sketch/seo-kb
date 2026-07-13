---
type: audit
title: "Audit indexation Organikk - 2026-07-13 (site complet)"
date: 2026-07-13
perimetre: "https://organikk.co - 146 URLs du sitemap (site entier, 2e run hors /wiki)"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical / h1", "wordcount HTML body"]
indexation_google_estimee: "non mesuree ce run (pas d'acces GSC dans cet environnement, cf. Limites)"
pages_testees: 146
anomalies_critiques: 2
anomalies_mineures: 4
loop: indexation-check
---

# Audit indexation Organikk - 2026-07-13

## Synthese

2e run sur le site complet (146 URLs). Meme perimetre, meme taille de sitemap qu'au run du 10 juillet, mais **aucune des deux anomalies critiques ouvertes n'est corrigee** : `/manifeste/` renvoie toujours `HTTP 404`, `/accompagnement-seo-geo/` reste orpheline. En parallele, un vrai progres editorial : **10 fiches wiki qui pesaient moins de 300 mots au dernier run sont toutes passees au-dessus de 340 mots**. La reco P5 du 10 juillet a ete appliquee. Les fiches denses ne remontent pas encore en impression, mais le corpus n'est plus mince.

Verifications validees sur 146/146 :
- `HTTP 200` final apres redirections
- Absence de `noindex` en `meta` HTML
- `<link rel=canonical>` present et strictement egal a l'URL finale
- `<title>` present et non vide
- Non bloque par `robots.txt`

Verifications avec anomalies :
- Sitemap declare des URLs non canoniques : **145 / 146** (301 vers le slash final ; seule la racine echappe car elle n'a pas de chemin)
- `lastmod` uniforme sur tout le sitemap : **146 / 146** (`2026-07-13T05:24:33.210Z`)
- Pages orphelines (0 lien interne entrant) : **2 / 146** — identiques au run precedent
- Pages sous-maillees (1 seul lien entrant) : **30 / 146** — nombre identique au run precedent
- Pages sans `<h1>` : **1 / 146** (`/accompagnement-1-1-30-jours/`)
- Contenu sous 300 mots : **3 / 146** (contre 14 au run precedent)
- Page servie par Google en 404 selon la mesure du 10/07 : **1** (`/manifeste/`, toujours 404 ce run)

Statut d'indexation Google : **non teste ce run**. Le pull GSC (`admin-gsc-export`) n'est pas accessible depuis cet environnement d'execution. Il ne s'agit pas d'une regression du site : la mesure du 10/07 (49/146 confirmees, 97 indeterminees) est le dernier signal fiable. Rappel doctrinal : « non indexee » et « non testable » restent deux etats distincts.

Sitemap : 146 URLs, delta 0 vs run precedent. Trajectoire 35 jours : 169 -> 136 -> 143 -> 143 -> 146 -> 146.

Robots.txt inchange (`Allow: /`, deux `Disallow` privatifs, sitemap declare).

## Anomalies critiques

### C1. `/manifeste/` renvoie toujours 404 — 2e recurrence

**Constat.** `curl -sIL https://organikk.co/manifeste/` renvoie `HTTP/2 404`. Meme reponse sur `/manifeste` sans slash. Ni ajoute au sitemap, ni redirige en 301.

**Lecture.** La reco P1 du 10 juillet demandait une redirection 301 vers `/methode/` ou `/systeme/`. Elle n'a pas ete appliquee, et la GSC continuera de servir la page en 404 sur la requete `manifeste seo` tant que Google n'a pas recrawle et vu la redirection. Chaque impression envoie un utilisateur sur une page d'erreur. Le co&ucirc;t est le meme qu'a l'ouverture de l'anomalie : la 2e URL du site en impressions est morte.

Aucun `<a href>` vers `/manifeste` sur les 146 pages du site : **0 backlink interne**. Rien pour signaler a Google que la page a change de nom.

**Action.** Ajouter une regle de redirection `301 /manifeste{,/} -> /methode/`. Une ligne dans la config Netlify (`_redirects` ou `netlify.toml`). Jamais de 410.

### C2. `/accompagnement-seo-geo/` reste orpheline — 2e recurrence

**Constat.** Verifie par crawl des 146 pages du sitemap : la chaine `accompagnement-seo-geo` n'apparait que sur sa propre page (1 fichier sur 146, l'auto-reference).

**Lecture.** Page d'offre, `HTTP 200`, 1 272 mots au dernier comptage, canonical propre. Elle est indexable et decouvrable seulement par le sitemap. La reco C2 du 10 juillet (mailler depuis `/systeme/`, `/methode/`, `/accompagnement-1-1-30-jours/`) n'a pas ete appliquee non plus. Grep confirme : aucun de ces trois hubs ne contient le slug ce run.

**Action.** Poser trois liens ancre naturels depuis les trois hubs. Trois lignes de HTML.

## Anomalies mineures

### M1. Sitemap declare 145 URLs non canoniques — 6e recurrence

145 des 146 `<loc>` du sitemap sont declares sans slash final. Le serveur renvoie un `301` vers `<path>/` sur les 145. La seule exception est la racine `https://organikk.co`, sans chemin, qui repond 200 directement.

Le canonical du DOM pointe correctement vers la version avec slash sur 146/146. Aucun risque d'indexation duale, mais chaque URL du sitemap coute un aller-retour de crawl inutile.

P1 ouverte depuis le 15 juin, sans effet observable apres 28 jours.

### M2. `lastmod` uniforme sur 146/146 — 6e recurrence

Toutes les URLs portent `2026-07-13T05:24:33.210Z`, la date du dernier build. `uniq -c` sur les `<lastmod>` renvoie une seule ligne : 146 occurrences. `lastmod` = date de build, pas date de modification par page. Google apprend a l'ignorer.

P2 ouverte depuis le 15 juin, sans effet observable apres 28 jours.

### M3. `/secteurs/` est orpheline et mince — 2e recurrence

Hub de section pour deux pages enfants (`/secteurs/avocat/`, `/secteurs/hotellerie/`), 270 mots, zero lien interne entrant. Meme profil qu'au 10/07 (109 mots a l'epoque : la page a ete un peu etoffee, mais reste mince pour un hub et toujours orpheline).

**Action.** Soit densifier et mailler comme un vrai hub sectoriel, soit renoncer et enlever du sitemap. La demi-mesure actuelle ne rend service ni au maillage ni au corpus.

### M4. `/accompagnement-1-1-30-jours/` : 163 mots, pas de `<h1>`

Seule page du site sans `<h1>`. 163 mots (tunnel de quiz en 5 etapes). Page de conversion, sous-maillee (1 lien entrant depuis `/plan-du-site/` selon la carte de ce run — au 10/07 elle etait mieux maillee, verifier une regression eventuelle du template plan-du-site).

**Action.** Ajouter un `<h1>` au premier ecran du quiz. Une balise, aucun impact UX.

## Observation positive

**P5 du 10 juillet appliquee : les 10 fiches wiki sous 300 mots ont ete densifiees.**

| Fiche | 10/07 | 13/07 |
|---|---:|---:|
| core-web-vitals | 206 | 353 |
| titans-architecture | 240 | 388 |
| muvera | 243 | 394 |
| clustering-semantique | 256 | 399 |
| pillar-page | 269 | 413 |
| silo-seo | 274 | 415 |
| embedding-seo | 277 | 428 |
| eeat | 284 | 423 |
| featured-snippet | 289 | 444 |
| similarite-cosinus | 289 | 442 |
| resultats | 196 | 346 |

Passage moyen +155 mots. Aucune de ces 11 pages n'est plus sous 300 mots. Le corpus wiki reste mince en visibilite (38 des 40 fiches a zero impression au 10/07), mais le prealable editorial est acquis. Le prochain vrai signal viendra du run avec GSC : si les 10 fiches densifiees restent a zero impression 30 jours apres reindexation, c'est que le probleme n'est pas la longueur, c'est le maillage entrant et la requete cible.

## Autres observations

**30 pages sous-maillees** (1 seul lien entrant), meme scope qu'au 10/07 : 15 pages `/newsletter/*` (toutes maillees uniquement depuis `/newsletter/`), 5 `/strategies/*`, 3 `/actualites/*`, 3 `/bootcamp*` et `/freelance-geo-lyon`, `/resultats`. Le maillage de ces sections repose sur une seule page de listing.

**Scraping `site:` sur Google : non teste ce run** (retire de l'audit). Le check #8 du skill est mort depuis 5 runs consecutifs (voir `memory/questions.md`, diff en attente du 10/07 pour remplacement par l'API URL Inspection).

## Recommandations priorisees

1. **Rediriger `/manifeste{,/}` en 301** vers `/methode/`. Reconduite du 10/07. Une ligne dans `_redirects`. C'est le seul point urgent.

2. **Mailler `/accompagnement-seo-geo`** depuis `/systeme/`, `/methode/` et `/accompagnement-1-1-30-jours/`. Reconduite du 10/07. Trois liens.

3. **Corriger le sitemap** : declarer les URLs avec le slash final, alimenter `lastmod` depuis la vraie date de derniere modification de contenu par page. Reconduite du 15/06 (28 jours d'ouverture). Le generateur de sitemap est le seul livrable.

4. **Trancher sur `/secteurs/`** : soit hub reel (>=600 mots, maille depuis 2 pages amont minimum, avec `<h2>` par secteur), soit retrait du sitemap. La version actuelle (270 mots, orpheline) ne sert personne.

5. **Ajouter un `<h1>` a `/accompagnement-1-1-30-jours/`**. Une balise. Deja demande implicitement au 10/07.

6. **Brancher `urlInspection/index:inspect`** a cote de `admin-gsc-export` (diff en attente du 10/07 dans `memory/questions.md`). Sans ca, l'audit reste aveugle sur les 97 URLs indeterminees. C'est le seul debloqueur qui manque au systeme.

## Limites de ce rapport

- **Statut d'indexation Google non teste.** Pas d'acces a l'edge `admin-gsc-export` depuis cet environnement d'execution. La derniere mesure fiable est celle du 10/07 (49/146 confirmees, 97 indeterminees). Aucune page ne peut etre declaree « non indexee » sur cette base, et aucune estimation n'a ete inventee ici (§10 regle 4).
- **Scraping `site:` officiellement retire de l'audit** apres 5 runs a « non testable ». Le check #8 reste dans le skill tant que Tim n'a pas tranche le diff propose (voir `memory/questions.md`).
- **Fenetre de decouverte = sitemap.** Comme au 10/07, une page vivante absente du sitemap et sans lien entrant echapperait a cet audit. `/manifeste` reste connue ici uniquement parce que le run precedent l'a documentee — sans la mesure GSC croisee, cette classe de bug ne se detecterait pas ce run.
- **Maillage calcule sur les 146 pages du sitemap uniquement.** Un lien depuis une page hors sitemap ne serait pas compte.
- **Progres editorial constate mais pas encore mesurable en impressions.** Il faudra la fenetre 28j du prochain run avec GSC pour dire si les 10 fiches densifiees remontent.

## Liens

Runs precedents : [[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]], [[reports/indexation-organikk-2026-07-06]], [[reports/indexation-organikk-2026-07-10]].
Methode : [[gsc-export]], [[maillage-interne]].
Skills en attente de decision : [[loops/indexation-check/memory/questions]] (remplacement check #8 par urlInspection API, correction chemin validator).
