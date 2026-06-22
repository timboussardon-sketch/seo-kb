---
type: audit
title: "Audit indexation Organikk - 2026-06-22"
date: 2026-06-22
perimetre: "https://organikk.co/wiki/* + index /wiki/"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical"]
indexation_google_estimee: "non testable (rate-limit Google sur site:organikk.co, pas d'API GSC dans ce run)"
pages_testees: 40
anomalies_critiques: 0
anomalies_mineures: 2
loop: indexation-check
---

# Audit indexation Organikk - 2026-06-22

## Synthese

40 pages wiki testees (39 fiches + racine `/wiki`). Toutes repondent en HTTP 200 final, aucune `noindex`, toutes presentes dans `sitemap.xml`, aucune bloquee par `robots.txt`. Aucune anomalie critique.

Les deux anomalies mineures du run precedent ([[reports/indexation-organikk-2026-06-15]]) sont **toujours presentes**, a l'identique :

1. Sitemap declare les URLs sans trailing slash, le serveur redirige systematiquement vers la version avec slash (40/40 wiki). M1 inchangee. P1 du run du 15 juin n'a pas ete suivie.
2. `lastmod` uniforme sur toutes les URLs du sitemap, fixe a la date de build (`2026-06-22T06:57:30.027Z` aujourd'hui, vs `2026-06-13T09:25:23.405Z` la semaine derniere). M2 inchangee. P2 du run du 15 juin n'a pas ete suivie.

Un changement notable hors perimetre wiki : le sitemap est passe de **169 a 136 URLs en 7 jours** (-33 URLs). Le scope wiki reste inchange (40 URLs), donc ce delta concerne d'autres sections (blog, pages services, etc.). Pas une anomalie en soi, mais a noter pour comprehension globale.

Indexation Google estimee : **non testable** (idem run precedent). Le fetch sur `site:organikk.co/wiki/` retourne une page d'assistance Google generique, pas de SERP. Sans GSC API, on ne peut pas distinguer "non indexee" de "non testable".

Robots.txt : inchange. `Allow: /`, deux paths privatifs disallowed, sitemap declare.

## Anomalies critiques

Aucune.

## Anomalies mineures

### M1. Sitemap declare des URLs non canoniques (40/40 wiki) — recurrence

**Constat** : identique au run du 15 juin. Le sitemap pointe vers `https://organikk.co/wiki/<slug>`, le serveur renvoie un `301` vers `https://organikk.co/wiki/<slug>/`. 40/40 wiki touchees, vraisemblablement les 136 URLs du sitemap entier.

**Preuve** : tests d'aujourd'hui — `redirects=1` sur 40/40, `final_url = input_url + "/"` sur 40/40, canonical du DOM = version trailing-slash sur 40/40.

**Impact** : crawl budget gaspille (deux requetes par URL au lieu d'une).

**Statut vs run precedent** : aucune amelioration. La recommandation P1 du 15 juin (corriger le generateur de sitemap pour emettre les URLs avec trailing slash) n'a pas eu d'effet observable.

### M2. lastmod uniforme sur 136 URLs — recurrence

**Constat** : toutes les entrees portent `lastmod=2026-06-22T06:57:30.027Z`. La date a change depuis le 15 juin (nouveau build entretemps), mais le pattern "lastmod = date de build, pas date de modif par page" persiste.

**Impact** : Google deprend le champ pour prioriser le re-crawl. Le `lastmod` reste decoratif.

**Statut vs run precedent** : aucune amelioration. La recommandation P2 du 15 juin (alimenter `lastmod` depuis la vraie date de modif par page) n'a pas eu d'effet.

## Recommandations priorisees

**P1 (reconduite) - Reecrire le sitemap avec trailing slash.** Toujours valable. Cible : 0 redirection au prochain audit.

**P2 (reconduite) - Alimenter `lastmod` depuis la vraie date de modif par page.** Toujours valable. Toujours sans effet pour l'instant.

**P3 (reconduite) - Brancher GSC API pour mesurer l'indexation reelle.** Toujours non fait. Tant que ce point n'est pas resolu, "indexation Google estimee" restera "non testable" semaine apres semaine.

**P4 (nouveau) - Comprendre le delta -33 URLs au sitemap entre le 15 et le 22 juin.** Le scope wiki est stable, mais le sitemap global a perdu 19,5% de ses URLs en une semaine. A clarifier : suppressions deliberees (clean up de pages periphériques) ou regression du generateur ? A verifier au prochain run.

## Non testable

- Indexation Google reelle par URL. Non testable sans GSC API. Statut a re-evaluer au prochain run avec un pull GSC, comme recommande depuis le 15 juin.

## Methode

- Sitemap parsing : `curl` sur `https://organikk.co/sitemap.xml`, 136 URLs au total dont 40 sous `/wiki(/*)`.
- HTTP status : `curl -sL -A "Mozilla/5.0 (compatible; OrganikkIndexCheck/1.0)" --max-time 25` sur les 40 URLs, code final + nb redirects + URL finale.
- Noindex / canonical : grep regex sur le HTML rendu de chaque page.
- Robots.txt : lecture directe.
- Indexation Google : tentative `WebFetch` sur `site:organikk.co/wiki/`, page d'assistance generique retournee, non testable.

Aucun forcage d'indexation declenche. Lecture seule.
