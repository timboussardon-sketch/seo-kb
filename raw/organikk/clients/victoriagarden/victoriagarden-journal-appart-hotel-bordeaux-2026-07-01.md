---
type: audit
title: "Journal Victoria Garden : chantier hub « appart hotel bordeaux » (analyse + home + activités + météo + hub)"
aliases: [victoriagarden-journal-appart-hotel-bordeaux]
tags: [seo, client, victoriagarden, journal, hub, cannibalisation, maillage, appart-hotel]
created: 2026-07-01
updated: 2026-07-01
sources: 3
confidence: high
status: stable
---

# Journal : chantier « appart hotel bordeaux » (2026-07-01)

Session de travail sur la requête « appart hotel bordeaux » où Victoria Garden avait perdu des positions. Élucide et prolonge [[victoriagarden-audit-gsc-2026-06-11]]. Analyse amont : [[victoriagarden-analyse-semantique-appart-hotel-bordeaux-2026-07-01]] ; brief : [[victoriagarden-brief-hub-appart-hotel-bordeaux-2026-07-01]].

## En résumé

Le contenu n'était pas le problème, l'architecture l'était. Trois causes cumulées sur « appart hotel bordeaux » (3 348 impressions/90 j, position moyenne 8,8) :
1. Chute d'impressions (10 546 → 5 606 → 3 348 sur un an) : contraction de couverture / demande / AI Overview.
2. Cannibalisation : 8 URL du site se disputent la même requête, aucune ne passe le top 8.
3. Pack local : Victoria est 3e, ce qui rabote le CTR organique.

Décision validée par Tim : transformer la page pilier `/destination/appart-hotel-bordeaux-centre/` en vrai hub comparatif, et bâtir autour un maillage home → hub → activités/météo → séjour au mois. Data terrain fournie par Tim : `base-activites-bordeaux.xlsx` (155 activités, distances depuis la résidence) et `donnees-meteo-bordeaux-pau.xlsx` (normales Météo-France 1991-2020).

## Ce qui a été produit (dossier client)

Tout est en blocs WordPress Gutenberg, calé sur le CSS du thème victoria-garden (fonts sofia-pro / bely-display, vert de marque #2c7373, tableaux `wp-block-table` à en-tête vert, espacement 24-32 px, boutons affinés radius 6 px). Registre vouvoiement pro.

| Livrable | Fichier code | Aperçu rendu |
|---|---|---|
| Contenu home (4 blocs : au mois, comparatif, destinations, FAQ) | Google Doc « Home page : contenu prêt à coller (v2) » | — |
| Page activités (155 activités, 14 catégories) | `vg-activites-CODE-A-COLLER.txt` | `vg-page-activites-bordeaux.html` |
| Page météo (climat 12 mois + saisonnalité) | `vg-meteo-CODE-A-COLLER.txt` | `vg-page-meteo-bordeaux.html` |
| Hub (quartiers + comparatif + selon votre séjour + FAQ schema) | `vg-hub-CODE-A-COLLER.txt` | `vg-page-hub-bordeaux.html` |

Accès GSC via l'export Fusionn (`admin-gsc-export`, propriété `https://www.victoriagarden.com/`), lecture seule. Cf. [[reference_gsc_export_fusionn]] côté mémoire.

## Plan de maillage (étape 3)

- Home → hub `/destination/appart-hotel-bordeaux-centre/` (blocs destinations) + → `/appart-hotel-au-mois/` (bloc au mois).
- Hub → `/appart-hotel-au-mois/`, → page comparatif Airbnb, → page activités, → page météo.
- Pages activités et météo → hub (bouton Réserver) + → au mois.
- Pages événements (`/evenements-bordeaux-2026/`, fort trafic Know) → hub, pour convertir le trafic éditorial en réservation.
- Les liens « quand venir » et « que faire » sont en `href="#"` tant que les pages activités/météo ne sont pas publiées : à mettre à jour avec leurs URL réelles.

## Résolution de la cannibalisation (à faire)

Un seul pilier sur le head term. Les autres URL gardent leur longue traîne et maillent vers le pilier, elles ne concourent plus sur « appart hotel bordeaux » :
- `/destination/appart-hotel-bordeaux-centre/` : pilier unique (garder).
- `/appart-hotel-au-mois/` : reste sur le cluster au mois (garder, à protéger, positions 1,9-7).
- `/appart-hotel-place-de-la-victoire-bordeaux/`, `/trouvez-votre-appart-hotel-a-bordeaux-avec-parking/`, `/apparthotel-pour-4-personnes-a-bordeaux/` : satellites longue traîne, requalifier le title/H1 sur leur intention propre (parking, 4 personnes, place de la Victoire) et lier vers le pilier.
- Accueil et versions `/en/` `/es/` : les sortir de la course sur le head term (hreflang + maillage), ne pas cibler « appart hotel bordeaux » en title.
- Formaliser via le skill `seo-cannibalisation` au prochain passage.

## Points ouverts

- Vérifier 6 adresses marquées « ⚠ à vérifier » dans la base avant publication : Aux 4 Coins du Vin, Bordeaux Tower segway, Cromagnon, Origine (restaurant), Origine Café, Yarn Coffee.
- Baliser sur le hub et la home : Product/Offer (prix), AggregateRating/Review (avis), FAQPage (fait sur le hub via bloc HTML JSON-LD).
- Relevé SERP FR manuel pour confirmer positions + présence AI Overview.
- Mesure de contrôle J+30 / J+90 en GSC sur « appart hotel bordeaux » et le cluster au mois une fois les pages en ligne.
