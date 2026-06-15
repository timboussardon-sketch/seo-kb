---
type: audit
title: "Audit indexation Organikk - 2026-06-15"
date: 2026-06-15
perimetre: "https://organikk.co/wiki/* + index /wiki/"
sources_de_verite: ["HTTP status (curl)", "https://organikk.co/sitemap.xml", "https://organikk.co/robots.txt", "DOM meta robots / canonical"]
indexation_google_estimee: "non testable (rate-limit Google sur site:organikk.co, pas d'API GSC dans ce run)"
pages_testees: 40
anomalies_critiques: 0
anomalies_mineures: 2
loop: indexation-check
---

# Audit indexation Organikk - 2026-06-15

## Synthese

40 pages testees : 39 fiches wiki listees dans `/wiki/` + la racine `/wiki`. Toutes repondent en HTTP 200 final, aucune ne porte `noindex`, toutes sont declarees dans `sitemap.xml`, aucune n'est bloquee par `robots.txt`. Aucune anomalie critique.

Deux anomalies mineures, systemiques, repliquees sur les 40 URLs :
1. Le sitemap declare les URLs **sans trailing slash** (`/wiki/agent-seo`) alors que la version canonique est **avec trailing slash** (`/wiki/agent-seo/`). Resultat : 40/40 pages renvoient un `301` vers la canonique. Google finit par crawler la bonne URL, mais chaque URL consomme deux requetes au lieu d'une.
2. `lastmod` identique (`2026-06-13T09:25:23.405Z`) sur les 169 URLs du sitemap. Quand un sitemap horodate tout son contenu a la milliseconde pres a la meme date, Google deprend le champ. Pas un blocage, mais le signal de fraicheur ne joue pas.

Indexation Google estimee : **non testable** dans ce run. La requete `site:organikk.co/wiki/` via fetch web a renvoye un blocage Google (rate-limit / consent). Sans acces GSC API, on ne peut pas distinguer "non indexee" de "non testable". Pour ce run, on s'en tient aux signaux verifiables localement (HTTP + sitemap + meta). A re-faire avec GSC API pour quantifier l'indexation reelle.

Robots.txt sain : `Allow: /`, deux paths privatifs explicitement disallowed (`/dashboard-bootcamp-organikk-private-2026/`, `/espace-leexi/`), sitemap declare.

## Anomalies critiques

Aucune.

## Anomalies mineures

### M1. Sitemap declare des URLs non canoniques (40/40 wiki, vraisemblablement 169/169 site)

**Constat** : toutes les URLs `wiki/*` du sitemap pointent vers la forme sans slash final.

```
sitemap        : https://organikk.co/wiki/agent-seo
serveur 301 -> : https://organikk.co/wiki/agent-seo/
canonical      : https://organikk.co/wiki/agent-seo/
```

**Preuve** : 40/40 lignes du test du jour ont `redirects=1` et `final_url` differente de l'URL sitemap. Code final 200, mais via un saut de redirection systematique. Pattern verifie sur tout l'echantillon teste.

**Impact** : crawl budget gaspille. Sur un site de cette taille (169 URLs) ce n'est pas critique, mais a chaque cycle de re-crawl, chaque URL est servie deux fois.

**Cause probable** : Next.js avec `trailingSlash: true` cote app, mais le generateur de sitemap emit les URLs sans slash.

### M2. lastmod uniforme sur 169 URLs

**Constat** : toutes les entrees du sitemap.xml portent le meme `lastmod` : `2026-06-13T09:25:23.405Z`. Date du dernier build, pas date de derniere modif du contenu.

**Impact** : Google detecte le pattern et ignore le champ pour prioriser le re-crawl. C'est une perte de signal, pas un blocage. Tant que ca reste comme ca, le `lastmod` ne sert a rien.

## Recommandations priorisees

**P1 - Reecrire le sitemap avec trailing slash.** Faible effort, gain crawl budget. Le `next-sitemap` ou la logique custom qui genere `sitemap.xml` doit emettre `https://organikk.co/wiki/agent-seo/` au lieu de `https://organikk.co/wiki/agent-seo`. Cible : 0 redirection au prochain audit (vs 40/40 aujourd'hui).

**P2 - Alimenter lastmod a partir de la vraie date de modif par page.** Si le contenu wiki vit dans un CMS / dans le repo, prendre la date du fichier (frontmatter `updated:` ou `git log`) plutot que la date de build. Sans ca, le champ reste decoratif.

**P3 - Brancher GSC API pour mesurer l'indexation reelle au prochain run.** Le rate-limit Google sur les requetes `site:` rend l'estimation non fiable. Le pull GSC (deja en place pour `gsc-watcher`, cf. [[preuves/SETUP-GSC]]) doit aussi servir cette boucle : exporter `index_coverage` par URL au lieu de chercher via Google search.

## Non testable

- Indexation Google reelle par URL. Non testable sans GSC API. Statut a re-evaluer au prochain run avec un pull GSC.

## Methode

- Sitemap parsing : `WebFetch` sur `https://organikk.co/sitemap.xml`, 169 URLs, dont 39 sous `/wiki/*` + 1 index `/wiki`.
- HTTP status : `curl -sL -A "Mozilla/5.0 (compatible; OrganikkIndexCheck/1.0)" --max-time 25` sur les 40 URLs, code final + nb redirects + URL finale.
- Noindex / canonical : grep regex sur le HTML rendu de chaque page.
- Robots.txt : lecture directe.
- Indexation Google : tentative `WebFetch` sur `site:organikk.co/wiki/`, rate-limite (blocage Google), donc non testable.

Aucun forcage d'indexation (`Submit URL`, IndexNow, etc.) n'a ete declenche. Lecture seule.
