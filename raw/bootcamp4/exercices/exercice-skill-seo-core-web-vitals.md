---
title: "seo-core-web-vitals : la perf qui freine ton SEO"
bootcamp: 4
type: exercice
session: 3
skill: seo-core-web-vitals
cowork: terminal
created: 2026-06-09
---

# seo-core-web-vitals : la perf qui freine ton SEO

**Pré-requis** : le skill seo-core-web-vitals + Lighthouse CLI + jq (terminal uniquement). Le sitemap.xml. Sur Cowork pur : prends PageSpeed Insights public à la place.

## Le cas

Un site lent rank moins bien. Cet exercice audite la perf (LCP, CLS, TBT) en mobile sur un échantillon de ton sitemap, via Lighthouse local, et sort les 5 pires pages à corriger.

## Ce que tu dois faire

**1. Vérifie les pré-requis (terminal)**
Lighthouse et jq installés.

**2. Lance le skill**

```text
Lance seo-core-web-vitals sur ce sitemap (échantillon 50 URLs).
Tableau LCP/CLS/TBT par URL, verdicts, top 5 pages à corriger,
et détecte un éventuel pattern de redirection sitemap.
```

**3. Corrige**
Les 5 pires pages d'abord.

## Ce que tu dois obtenir — le « screen »

```
CORE WEB VITALS — mobile (échantillon)

URL              | LCP   | CLS  | TBT   | Verdict
/                | 2,1s  | 0,02 | 120ms | OK
/blog/article-x  | 4,8s  | 0,31 | 540ms | A corriger

Top 5 à corriger en tête. Pattern redirect sitemap détecté : quick win.
```

## Vérifier que tu as réussi

- [ ] Tableau LCP/CLS/TBT par URL.
- [ ] Verdicts par page.
- [ ] Top 5 pages à corriger.
- [ ] Détection d'un pattern de redirection sitemap (quick win).

## Le piège

Auditer une page à la main une par une. Le skill échantillonne le sitemap d'un coup. Et sur Cowork il ne tourne pas : PageSpeed public à la place.

## Comment ça marche

Le skill lance Lighthouse en local sur un échantillon mobile, agrège les métriques et repère les problèmes structurels récurrents, pas juste page par page.
