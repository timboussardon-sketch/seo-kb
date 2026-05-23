---
type: proposition
title: Modèle — Proposition commerciale PDF (design organikk.co)
aliases: [modele-proposition-pdf, template-proposition-design, proposition-pdf]
tags: [proposition, commercial, template, modele, pdf, design, organikk]
created: 2026-05-21
updated: 2026-05-21
confidence: high
status: stable
---

# Modèle — Proposition commerciale PDF

Gabarit de proposition commerciale au format PDF, design organikk.co. À utiliser après un call de vente : on garde le design et la structure, on remplace le contenu.

La source est un fichier HTML + CSS, rendu en PDF par Chrome headless. Pas de Word, pas de Canva. Le fichier se modifie au texte, se versionne, se régénère en une commande.

## Fichiers du modèle

- `modele-proposition-pdf.html` — le gabarit. Le CSS (design) est dans le `<style>` du `<head>`. Le contenu est dans le `<body>`, rempli avec un exemple réel (client Leexi).
- `exemple-proposition-leexi.pdf` — le rendu de référence, 8 pages. À quoi une proposition finie doit ressembler.

## Design (ne se touche pas d'un client à l'autre)

- Format A4. Couverture pleine page bleu nuit, puis 11 sections sur pages blanches.
- Couleurs : bleu profond `#1B3E8F`, bleu `#2559DD`, bleu clair `#4685F0`, accent rouge `#FF371C`, encre `#0A0F1E`.
- Typographies : Inter (texte), Instrument Serif italic (accent sur un mot clé), JetBrains Mono (labels, numéros, chiffres).
- Tout le design vit dans le `<style>` du `<head>`. On n'y touche pas.

## Structure de contenu (11 sections)

| # | Section | Rôle | Composant visuel |
|---|---------|------|------------------|
| 1 | Synthèse | Le constat et l'objectif unique de la mission | Prose, 3 paragraphes |
| 2 | Analyse de l'existant | Le diagnostic | Tableau + duo forces / faiblesses + encadré opportunité |
| 3 | Stratégie proposée | L'approche | Prose + tableau de modèles + 2 cartes + carte « pièce centrale » |
| 4 | Méthodologie | Qui fait quoi | Prose + duo (demandé au client / rythme) |
| 5 | Livrables | Ce que le client garde | Liste numérotée |
| 6 | Planning | Le déroulé | 3 cartes (une par mois ou par phase) |
| 7 | Tarification | Le prix | Carte prix : périmètre à gauche, montant à droite |
| 8 | Résultats attendus | La projection chiffrée | 4 stats + mention « estimation » + prose |
| 9 | Hors périmètre | Ce qui n'est pas inclus | 4 cartes |
| 10 | Pourquoi ce setup | L'argument de fond | 4 cartes numérotées |
| 11 | Prochaine étape | Le closing | Encadré + signature |

La structure ne change pas. Si une section est inutile pour un client, on la vide ou on l'enlève, on ne réorganise pas.

## Ce qui change à chaque client

- Nom du client : chercher/remplacer dans tout le fichier.
- Couverture : titre, sous-titre, pitch d'une ligne sur le client, les 4 métriques clés.
- Sections 1 à 11 : tout le contenu rédactionnel.
- Section 7 : le prix et les modalités.
- Date (couverture et pied de signature).

## Règles non négociables

- Zéro em-dash « — ». Deux-points, virgules ou parenthèses à la place.
- « organikk.co » toujours en entier. Jamais « Organikk » seul.
- Pas de mention « Confidentiel ».
- Titres en couleur unie. Pas de dégradé appliqué sur du texte : ça casse au rendu PDF selon le lecteur.
- Icônes en SVG inline, jamais de glyphes type ✓ ✕ : selon la police ils sortent en carrés.
- Toute projection chiffrée porte la mention « ceci est une estimation ». Rester prudent sur les chiffres, sous-promettre.
- Voix Tim : factuel, phrases courtes, données plutôt qu'opinions, zéro bullshit.

## Produire une nouvelle proposition

1. Dupliquer `modele-proposition-pdf.html` en `proposition-[client].html`.
2. Remplacer le contenu entre `<body>` et `</body>`. Ne pas toucher au `<style>`.
3. Générer le PDF avec Chrome headless :

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=12000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="Proposition-[client].pdf" \
  "file:///chemin/absolu/proposition-[client].html"
```

4. Vérifier le rendu page par page (8 pages environ). Contrôler em-dashes, glyphes, titres.

## Lié

- [[template-retainer-2h-500]] — l'autre modèle de proposition, format rétainer léger, texte markdown simple. Celui-ci est le format « gros dossier » designé.
