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

## Document d'accompagnement : la présentation de l'approche

Toute proposition part avec la présentation générique d'organikk.co. Les deux se répartissent le travail : la proposition traite le client (son diagnostic, sa stratégie, son prix), la présentation porte ce qui ne change pas d'un client à l'autre (l'approche, les chiffres du marché, les outils, la roadmap). Ça évite de re-justifier la doctrine dans chaque dossier.

- **En ligne** : `organikk.co/presentation-seo` (7 slides, navigation au clavier, `noindex`)
- **PDF à joindre** : `organikk.co/presentation-seo/organikk-presentation-seo.pdf` (7 pages paysage)
- **Source de vérité** : `organikk-next/scripts/build-presentation-seo.py`. Le script régénère l'HTML et écrase la sortie : ne jamais éditer `public/presentation-seo/index.html` à la main. Le gabarit est recopié dans le vault à `raw/organikk/_MODELE-presentation-approche.html` pour lecture.
- Le PDF se régénère avec la commande Chrome headless documentée en tête du script.

Quand la mettre dans le fil : en pièce jointe du mail de proposition, ou envoyée seule après un premier call quand le prospect demande « c'est quoi votre approche ». Elle ne contient aucun prix et aucun nom de client, donc elle circule sans risque.

**Contrainte de contenu** : les chiffres affichés portent tous leur source, leur date et leur échantillon. Ils se périment. Avant un envoi important, vérifier que les quatre chiffres de la slide marché tiennent toujours (voir les limites notées dans [[hypotheses]] et le registre [[contradictions]]).

## Lié

- [[modele-deck-slides]] — le deck en slides 16:9, **format par défaut depuis le 2026-07-17**. Celui-ci reste le dossier A4 dense, quand le prospect veut du détail écrit.
- [[template-retainer-2h-500]] — l'autre modèle de proposition, format rétainer léger, texte markdown simple. Celui-ci est le format « gros dossier » designé.
