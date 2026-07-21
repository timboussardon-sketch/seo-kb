---
type: note
title: Extensions Chrome — journal
date: 2026-07-21
tags: [extension, chrome, search-console, qadence, journal]
status: manuel
---

# Extensions Chrome — journal

Journal des extensions Chrome maison. Une entrée par chantier.

---

## 2026-07-21 — Clone Google Search Console dans l'extension `gsc-keyword-tracker`

### Ce que c'est
Recréation de la Google Search Console, à l'identique (pixel perfect), directement dans une extension Chrome. Il n'existe aucune extension GSC officielle, d'où l'intérêt.

Greffé sur l'extension existante **`~/Code/gsc-keyword-tracker/`** (« Qadence — Performances Search Console », v1.0.1). PAS l'extension « Qadence IA » (`~/Code/organikk-extension/`, maillage interne) ni `qadence-semantique`.

L'OAuth était déjà en place (scope `webmasters.readonly`, `key.pem` fige l'ID), donc rien à recréer côté Google Cloud.

### Ce que l'app fait (strictement, factuel)
Depuis Chrome, sans ouvrir Search Console :

Vue portefeuille (tous les sites d'un coup) :
- classement des sites par clics
- par site : impressions, CTR, position moyenne
- variation vs période précédente (hausse/baisse)
- courbe de tendance par site (sparkline)
- totaux consolidés du parc (clics, impressions, CTR global, position)
- vue Heatmap (chaque site dimensionné par ses clics)

Vue par site (clone GSC dans l'extension) :
- Vue d'ensemble : synthèse Performances + requêtes principales
- Performances : clics, impressions, CTR, position moyenne ; graphe d'évolution à bascule + tooltip ; détail par requête, page, pays, appareil, apparence, date
- volet Date déroulant : 24 h / 7 j / 28 j / 3 mois
- export CSV de n'importe quel tableau (reste dans l'extension)

Toutes les données viennent de l'API officielle Google Search Console. Ce sont les vrais chiffres du compte, pas une estimation.

### Ce que l'app NE fait PAS (à ne pas confondre avec l'extension maillage)
- pas d'envoi automatique dans ChatGPT (elle exporte un CSV, point)
- pas de connexion WordPress
- pas de maillage interne (orphelines, PageRank, ancres) : ça, c'est l'extension Qadence IA

### Faisabilité (rappel technique)
- Affichable via API : Performances (searchAnalytics), Inspection d'URL, Sitemaps.
- Jamais d'API (impossible dans l'extension) : Pages/indexation, Liens, Signaux Web essentiels (CrUX), Actions manuelles, Sécurité.
- Publier l'extension avec le scope `webmasters.readonly` sur le Chrome Web Store exige une validation Google (scope sensible). En usage perso / test users, mode « Testing » suffit, zéro validation.

### Décisions produit (Tim, 2026-07-21)
- **Popup uniquement, jamais de fenêtre pleine.** Le clone vit dans le popup. Bouton plein écran et barre « Inspecter une URL » retirés. Aucun lien vers la GSC web.
- **Seulement 2 sections** dans la barre latérale : Vue d'ensemble + Performances. Tout le reste retiré (car soit sans API, soit pas encore construit).
- **Échelle réduite** pour la lisibilité en popup (polices/paddings compacts, popup 760×600).
- « + Nouveau » retiré, pill Date transformée en volet déroulant.
- **Mode démo vidéo** : touche « b » floute les noms de domaine sauf golfiller et qadence (classe `.blurable`, non persisté). Pour filmer sans exposer les sites clients.

### Gotcha
Popup Chrome : un contenu en `position:fixed` + le chrome Qadence masqué → le `<body>` du popup se réduit à 0 et « l'app se coupe ». Fix : `body.gsc-on:not(.full) { width:760px; height:600px }`.

### Fichiers
`tracker.html`, `tracker.css` (bloc `.gsc-*`), `tracker.js`. `preview.html` = maquette autonome jetable (stubs `chrome.*` + `fetch`, données factices, sert au rendu headless de contrôle).

### Roadmap possible (si validé)
- Sitemaps réels dans l'extension (API `sitemaps.list`)
- Inspection d'URL réelle (API `urlInspection.index.inspect`, quota 2 000/jour)
- Connexion Search Console → filtres par requête/pays/appareil comme dans GSC

### Test
`chrome://extensions` → recharger l'extension → clic sur l'icône → Connecter → clic sur un site.
