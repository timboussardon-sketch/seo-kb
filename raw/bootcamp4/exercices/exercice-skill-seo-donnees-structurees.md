---
title: "seo-donnees-structurees : le balisage JSON-LD"
bootcamp: 4
type: exercice
session: 3
skill: seo-donnees-structurees
cowork: oui
created: 2026-06-09
---

# seo-donnees-structurees : le balisage JSON-LD

**Pré-requis** : le skill seo-donnees-structurees installé. Une page (HTML ou contenu) + son intention.

## Le cas

Le balisage Schema.org aide les moteurs à comprendre ta page et décroche les rich results. Cet exercice génère le JSON-LD adapté au contenu (Article, FAQPage, Product...), sans saisie manuelle.

## Ce que tu dois faire

**1. Donne la page + son type**
Le contenu et l'intention (article, produit, FAQ...).

**2. Lance le skill**

```text
Lance seo-donnees-structurees sur cette page. Génère le JSON-LD adapté
au contenu (Article, FAQPage, Product, BreadcrumbList) avec un @id graph
cohérent. Suis les 3 principes universels si je ne suis pas sur Next.js.
```

**3. Intègre**
Le JSON-LD dans la page, ou les principes universels selon ton CMS.

## Ce que tu dois obtenir — le « screen »

```
JSON-LD — page "logiciel de facturation"

{ "@type": "Product", "name": "...", "offers": {...} }
{ "@type": "FAQPage", "mainEntity": [ ...3 questions... ] }
{ "@type": "BreadcrumbList", ... }

Dérivé du contenu réel, @id graph site-wide cohérent.
```

## Vérifier que tu as réussi

- [ ] Le bon type de schéma selon le contenu.
- [ ] Dérivé du contenu réel (rien d'inventé).
- [ ] @id graph cohérent site-wide.
- [ ] Valide au Rich Results Test.

## Le piège

Baliser des infos absentes de la page. Le JSON-LD doit refléter le contenu visible, sinon Google l'ignore ou pénalise.

## Comment ça marche

Le skill lit le contenu et génère le graphe d'entité + les schémas par page dérivés du contenu. 3 règles universelles valables sur tout CMS, code Next.js en bonus.
