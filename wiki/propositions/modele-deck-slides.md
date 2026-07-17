---
type: proposition
title: Modèle — Deck de proposition en slides (16:9)
aliases: [modele-deck-slides, deck-proposition, propale-slides]
tags: [proposition, commercial, template, modele, deck, slides, pdf, design, organikk]
created: 2026-07-17
updated: 2026-07-17
sources: 2
confidence: high
status: stable
---

# Modèle — Deck de proposition en slides

Format de proposition commerciale en slides 16:9, validé le 2026-07-17 sur la propale [[entities/yalp]]. **C'est le format par défaut pour les prochaines propales.**

L'autre modèle, [[modele-proposition-pdf]], reste le dossier A4 dense en 11 sections. Le deck le remplace quand le prospect doit comprendre vite, ou quand il compare plusieurs agences.

## Fichiers du modèle

- `modele-deck-slides.html` — le gabarit, rempli avec l'exemple réel Yalp.
- `exemple-deck-yalp.pdf` — le rendu de référence, 10 slides paysage.

## Design (ne se touche pas d'un client à l'autre)

Repris de la présentation d'approche `organikk.co/presentation-seo`, pas du modèle A4.

- Slides 16:9, impression en 297mm × 167mm.
- Geist et Geist Mono. Jamais Inter. Cf. [[feedback_typo_geist_regle_fondamentale]].
- Fond `#f5f5f7`, encre `#1d1d1f`, dégradé bleu `#1B3E8F → #2559DD → #5b86f5` sur les titres.
- Couverture et slide finale sur le dégradé bleu plein.
- Tout le CSS vit dans le `<style>` du `<head>`. On n'y touche pas.
- Navigation clavier et points de pagination sur la version écran, masqués à l'impression.

## Structure (10 slides)

| # | Slide | Contenu |
|---|-------|---------|
| 00 | Couverture | Logo client inline dans le titre, objectif chiffré, préparé par |
| 01 | Le constat | Le vrai problème, puis 4 chiffres du prospect |
| 02 | Vos problématiques actuelles | 3 problématiques, jamais plus |
| 03 | Notre approche | Les 3 partis pris doctrinaux |
| 04 | Exemple de requêtes business | 6 pistes, aucun volume affiché |
| 05 | L'agent SEO client | Ce qu'on met dedans / ce qu'il fait ensuite |
| 06 | La roadmap | Les 4 phases doctrinales + rythme de production |
| 07 | Budget | Prix, ce que couvre la mission, sans engagement |
| 08 | Nos KPIs durant la mission | La métrique, la cible, l'équation |
| 09 | Logo | Le logo client en grand, centré |

## Règles non négociables

**Les titres sont des phrases.** Sujet + verbe, jamais de fragment nominal. « Le plus gros problème que je vois n'est pas votre trafic », pas « Le constat ». Cf. [[feedback_factuel_phrases_completes]]. Trois exceptions validées par Tim, parce que ce sont des intertitres de section : « Vos problématiques actuelles », « La roadmap », « Nos KPIs durant la mission ».

**Pas de label mono au-dessus des titres.** Le titre attaque directement. Les labels ne survivent qu'à l'intérieur des colonnes.

**L'approche et la roadmap se reprennent de la doctrine, jamais réinventées.** La source de vérité est `organikk-next/scripts/build-presentation-seo.py`. Les 3 partis pris : décisionnel uniquement, data propriétaire, liens gagnés jamais achetés. Les 4 phases : Stratégie / Mise en production et agent SEO / Mise en production et optimisation / Optimisation, production et CRO. Le rythme de production (10 à 15 pages par mois, 45 à 50 à trois mois) fait partie de la doctrine : ne pas le retirer.

**Zéro chiffre inventé.** Tant que la Search Console n'est pas lue, aucune projection de trafic ou de position. La slide KPI porte la mention de prudence. Les chiffres du prospect sont attribués au prospect. Cf. [[feedback_jamais_mentir_prospection]] et §5.4 de l'AGENTS.

**Pas de slide de closing.** Ni étapes, ni relance, ni signature : c'est l'e-mail d'accompagnement qui porte le closing. Le deck se ferme sur le logo client.

**Pas de colonne Volume** sur les requêtes. Cf. [[feedback_pas_colonne_volume]].

**Zéro tiret cadratin.** Deux-points, virgules ou parenthèses. Cf. [[feedback_pas_de_tiret_cadratin]].

## Le logo du client

Sur la couverture, le logo **remplace le nom du client dans le titre**, en inline. Sur la slide finale, il est en grand au centre.

Récupération : chercher le logo sur le site du prospect, le télécharger, le **rendre en image et le regarder avant de l'intégrer**. Sur Yalp, le fichier au nom le plus évident (`/hubfs/logo.svg`) était le logo d'une autre marque hébergée sur le même portail HubSpot. Vérifier, toujours.

Intégration en data URI base64 pour que le PDF reste autonome, sans appel réseau.

Alignement inline : mesurer la baseline du fichier plutôt que de caler à l'œil. Sur un logo dont la hauteur de capitale vaut `c` et la hauteur totale `H`, avec Geist dont la hauteur de capitale vaut ~0,72em :

```
height: (0.72 × H / c) em          → sur Yalp : .87em
vertical-align: -(jambage / H × height) → sur Yalp : -.15em
```

Recolorisation : si le logo fourni n'est pas à la couleur de la charte du client, recolorer en préservant le canal alpha, pour garder l'antialiasing des courbes.

## Produire un nouveau deck

1. Dupliquer `modele-deck-slides.html` en `deck-[client]-organikk.html`.
2. Remplacer le contenu entre `<body>` et `</body>`. Ne pas toucher au `<style>`.
3. Remplacer les deux logos (couverture inline + slide finale).
4. Générer le PDF :

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=9000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="Deck-SEO-[Client]-organikk.co.pdf" \
  "file:///chemin/absolu/deck-[client]-organikk.html"
```

5. Contrôler le rendu slide par slide. Vérifier les tirets cadratins, les coupures de mots dans les titres (`.nb` pour rendre insécable), et que le nombre de slides est bon.
6. Montrer le rendu en local à Tim avant tout envoi. Cf. [[feedback_montrer_en_local]].

## Document d'accompagnement

Le deck traite le client : son diagnostic, sa stratégie, son prix. La présentation générique `organikk.co/presentation-seo` porte ce qui ne change pas : les chiffres du marché, les outils Qadence et Fusionn, la data Organikk. Ne pas les redire dans le deck.

## Lié

- [[modele-proposition-pdf]] — le dossier A4 en 11 sections, l'autre format
- [[template-retainer-2h-500]] — le format rétainer léger
- [[sources/2026-07-16-call-15-baptiste-yalp]] — le call dont sort l'exemple
- [[concepts/methode-organikk-4-piliers]] · [[concepts/data-proprietaire]] · [[concepts/mots-cles-actionnels]]
