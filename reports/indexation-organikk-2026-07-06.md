---
type: audit
title: "Audit indexation Organikk - 2026-07-06"
date: 2026-07-06
perimetre: "https://organikk.co/wiki/* + index /wiki/"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical"]
indexation_google_estimee: "non testable (page Google requiert JS, pas d'API GSC dans ce run)"
pages_testees: 40
anomalies_critiques: 0
anomalies_mineures: 2
loop: indexation-check
---

# Audit indexation Organikk - 2026-07-06

## Synthese

40 pages wiki testees (39 fiches + racine `/wiki`). 40/40 repondent en HTTP 200 final, 0 `noindex`, 40/40 presentes dans `sitemap.xml`, 0 bloquee par `robots.txt`. Canonical du DOM = URL finale sur 40/40. Aucune anomalie critique.

Les deux anomalies mineures identifiees le 15 juin sont **toujours presentes a l'identique** : **4e occurrence consecutive** ([[reports/indexation-organikk-2026-06-15]], [[reports/indexation-organikk-2026-06-22]], [[reports/indexation-organikk-2026-06-29]]). Les recos P1 et P2 du 15 juin restent sans effet observable.

1. Sitemap declare les URLs sans trailing slash, le serveur redirige en `301` vers la version avec slash (40/40 wiki, vraisemblablement 143/143 site entier).
2. `lastmod` uniforme sur 143/143 URLs du sitemap, fixe a la date du dernier build (`2026-07-06T04:54:49.560Z`).

Hors perimetre wiki, le sitemap se stabilise cette semaine : 143 URLs comme au run precedent (delta 0 vs 2026-06-29). Sur 21 jours : 169 -> 136 -> 143 -> 143. Le mouvement bidirectionnel des deux semaines precedentes ne se reproduit pas. La P4 du 22 juin ("documenter la rotation editoriale") reste ouverte, sans nouveau signal cette semaine.

Indexation Google estimee : **non testable**, 4e run consecutif. Le fetch sur `site:organikk.co/wiki/` retourne toujours une page Google `noscript`, aucune SERP exploitable sans JS. Sans GSC API (P3 du 15 juin), on ne peut pas distinguer "non indexee" de "non testable".

Robots.txt : inchange vs runs precedents. `Allow: /`, deux paths privatifs `Disallow`, sitemap declare.

## Anomalies critiques

Aucune.

## Anomalies mineures

### M1. Sitemap declare des URLs non canoniques (40/40 wiki) - 4e recurrence

**Constat** : identique aux runs des 15 juin, 22 juin, 29 juin. Le sitemap pointe vers `https://organikk.co/wiki/<slug>`, le serveur renvoie un `301` vers `https://organikk.co/wiki/<slug>/`. 40/40 wiki touchees, vraisemblablement les 143 URLs du sitemap entier.

**Preuve** : tests d'aujourd'hui - `num_redirects=1` sur 40/40 URLs wiki testees, `final_url = url_sitemap + "/"` sur 40/40, canonical DOM = version trailing-slash sur 40/40.

**Impact** : crawl budget gaspille (deux requetes par URL au lieu d'une).

**Statut vs runs precedents** : aucune amelioration en 21 jours. La recommandation P1 du 15 juin (corriger le generateur de sitemap pour emettre les URLs avec trailing slash) n'a toujours pas eu d'effet observable.

### M2. lastmod uniforme sur 143 URLs - 4e recurrence

**Constat** : toutes les entrees portent `lastmod=2026-07-06T04:54:49.560Z`. La date change a chaque build (`2026-06-13` -> `2026-06-22` -> `2026-06-27` -> `2026-07-06`), mais le pattern "lastmod = date du dernier build, pas date de modif par page" persiste.

**Impact** : Google deprend le champ pour prioriser le re-crawl. Le `lastmod` reste decoratif.

**Statut vs runs precedents** : aucune amelioration en 21 jours. La recommandation P2 du 15 juin (alimenter `lastmod` depuis la vraie date de modif par page) n'a toujours pas eu d'effet.

## Observations hors anomalie

### O1. Sitemap stable a 143 URLs, wiki stable a 40

143 URLs au sitemap cette semaine, identique a la semaine derniere. Le wiki reste a 40 URLs sur quatre runs consecutifs. Sections hors wiki : 29 newsletter, 23 blog, 15 strategies, 4 outils, 4 actualites, 3 secteurs, plus 24 pages transverses.

Trajectoire sur 21 jours : 169 -> 136 -> 143 -> 143. Le mouvement bidirectionnel signale la semaine derniere ne se reproduit pas ce run. La P4 du 22 juin ("comprendre le solde -33 puis +7") reste sans donnee nouvelle : ni ajout, ni suppression cette semaine.

## Recommandations priorisees

**P1 (reconduite, 4e fois) - Reecrire le sitemap avec trailing slash.** Toujours valable. Sans cette correction, l'anomalie M1 sera reconduite chaque semaine. Cible : 0 redirection au prochain audit.

**P2 (reconduite, 4e fois) - Alimenter `lastmod` depuis la vraie date de modif par page.** Toujours valable, toujours sans effet. Tant que `lastmod` reste decoratif, Google ne s'en sert pas pour prioriser le re-crawl.

**P3 (reconduite, 4e fois) - Brancher GSC API pour mesurer l'indexation reelle.** Toujours non fait. Sans cela, "indexation Google estimee" restera "non testable" semaine apres semaine, et la boucle ne mesure que des signaux structurels. C'est la seule reco qui debloque un vrai signal terrain, les deux autres portent sur le crawl.

**P4 (reconduite) - Documenter la politique editoriale qui fait varier le sitemap hors wiki.** Aucun mouvement cette semaine, mais la trajectoire 169 -> 136 -> 143 -> 143 sur 21 jours reste non documentee cote site.

## Non testable

- Indexation Google reelle par URL. Page Google requiert JS, page `noscript` retournee. Statut a re-evaluer au prochain run si la P3 (GSC API) est branchee d'ici la.

## Methode

- Sitemap parsing : `curl` sur `https://organikk.co/sitemap.xml`, 143 URLs au total dont 40 sous `/wiki(/*)`.
- HTTP status : `curl -sL -A "Mozilla/5.0 (compatible; OrganikkIndexCheck/1.0)" --max-time 25` sur les 40 URLs wiki, recuperation `http_code`, `num_redirects`, `url_effective`.
- Noindex / canonical : extraction regex sur le HTML rendu de chaque page (40/40 fetched).
- Robots.txt : lecture directe.
- Indexation Google : tentative HTTP sur `https://www.google.com/search?q=site:organikk.co/wiki/`, page `noscript` (redirection JS), non testable.

Aucun forcage d'indexation declenche. Lecture seule.
