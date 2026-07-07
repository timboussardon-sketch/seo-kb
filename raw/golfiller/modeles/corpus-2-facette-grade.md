---
type: source
source_type: doctrine
title: "Modèle corpus 2 : facette grade (qualité d'occasion)"
aliases: [modele-corpus-2-grade-golfiller, facette-grade-golfiller]
tags: [golfiller, pseo, product-led, corpus, modele, occasion, conversion]
created: 2026-07-07
updated: 2026-07-07
sources: 1
confidence: high
status: draft
---

# Modèle corpus 2 : facette grade (qualité d'occasion)

Le modèle #3 du [[modeles-corpus-golfiller|tableau des modèles]]. C'est un champ du corpus 2 (specs des balles) : l'état de reconditionnement. Money Page = la collection filtrable. Données réelles relevées sur golfiller.fr le 2026-07-07 (page guide de gradation), aucun chiffre inventé.

Golfiller a déjà une page guide de gradation statique. Ce modèle la transforme en page décisionnelle qui route chaque visiteur vers la bonne collection.

## Couche 1 : la base (le champ)

Un champ `grade` sur chaque balle du corpus 2. Quatre tiers, libellés maison Golfiller (à reprendre tels quels) :

| Grade | État (verbatim Golfiller) | Perf. annoncée | Remise annoncée |
|---|---|---|---|
| `4A` | Parfait état, très légères traces de jeu ou jaunissements possibles | 100 % | −50 % |
| `3A` | Bon état, effacements d'impressions, traces de clubs, éraflures, feutres ou jaunissement possibles | 98 % | −60 % |
| `2A` | État correct, effacements importants, impacts de jeu, éraflures ou jaunissements possibles | 96 % | −70 % |
| `1A` | Usure prononcée, impacts répétés, décolorations et imperfections | 95 % | −70 % |

Les chiffres de performance et de remise sont ceux annoncés par Golfiller sur sa page, à traiter comme argument commercial maison, pas comme mesure indépendante.

## Couche 2 : la page (le modèle)

### Honnêteté SEO d'abord

Personne ne tape « balle 4A » ou « grade 3A » : ce sont des noms internes Golfiller, pas des requêtes. La page ne rank donc pas sur les noms de grade. Elle rank sur la vraie intention : « quelle qualité de balle d'occasion choisir », « balle reconditionnée fiable », « différence balle occasion et neuve », « perte de performance balle d'occasion ». Le grade est la réponse, pas la requête.

Le modèle a donc deux couches d'URL :

1. **Une page décisionnelle unique** (celle qui rank), qui compare les 4 grades et envoie vers la bonne collection.
2. **Une facette de collection par grade** (celle qui convertit) : `/collections/balles-occasion-4a`, `-3a`, `-2a`, `-1a`. Elle ne vise pas le SEO, elle capte le clic sortant de la page décisionnelle.

### Squelette de la page décisionnelle (HTML brut, réhabillable au template maison)

```html
<h1>Quelle qualité de balle de golf d'occasion choisir ?</h1>

<p>Golfiller trie ses balles en quatre grades, du plus proche du neuf
(4A) au plus marqué (1A). La performance de frappe bouge peu d'un grade
à l'autre : ce qui change, c'est l'aspect et le prix. Un joueur qui perd
des balles prend du 1A ou 2A ; un joueur qui veut du quasi-neuf prend du 4A.</p>

<table>
  <caption>Les 4 grades Golfiller</caption>
  <thead>
    <tr><th>Grade</th><th>État</th><th>Pour qui</th><th>Voir</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>4A</td>
      <td>Parfait état, traces très légères possibles</td>
      <td>Compétition, veut du quasi-neuf à moindre prix</td>
      <td><a href="/collections/balles-occasion-4a">balles 4A</a></td>
    </tr>
    <tr>
      <td>3A</td>
      <td>Bon état, légères marques d'usage</td>
      <td>Parcours régulier, bon compromis prix/aspect</td>
      <td><a href="/collections/balles-occasion-3a">balles 3A</a></td>
    </tr>
    <tr>
      <td>2A</td>
      <td>Correct, marques et effacements visibles</td>
      <td>Joue souvent, perd des balles, veut du volume</td>
      <td><a href="/collections/balles-occasion-2a">balles 2A</a></td>
    </tr>
    <tr>
      <td>1A</td>
      <td>Usure prononcée</td>
      <td>Entraînement, practice, débutant qui perd beaucoup</td>
      <td><a href="/collections/balles-occasion-1a">balles 1A</a></td>
    </tr>
  </tbody>
</table>

<h2>La performance baisse-t-elle avec le grade ?</h2>
<p>Peu. Un impact cosmétique n'est pas un impact de vol. La différence de
grade se voit surtout à l'œil et au portefeuille, pas sur la trajectoire.
Le vrai levier de performance reste le modèle de balle, pas son état :
<a href="/comparer">comparer deux modèles</a>.</p>

<h2>Occasion 4A ou neuf ?</h2>
<p>Une 4A annoncée à performance équivalente coûte moitié moins qu'une
neuve. Pour le même modèle, l'écart d'aspect est faible et l'écart de prix
est net. <a href="/collections/balles-occasion-4a">Voir les 4A par modèle.</a></p>
```

## Variable pSEO secondaire (croisement)

Le grade se croise avec le modèle (corpus 2) pour multiplier les pages de collection utiles à la conversion : `[modèle] en 4A`, `[modèle] en 3A`. Ces facettes captent le clic de qui cherche déjà « Pro V1 occasion » et veut choisir son état. Elles maillent vers la fiche modèle (modèle #4) et vers la page décisionnelle ci-dessus.

## Maillage (2 minimum)

- Vers les 4 collections par grade : le point de conversion.
- Vers le comparateur de modèles (corpus 2, modèle #1) : « la performance dépend du modèle, pas du grade ».
- Vers la fiche modèle d'occasion (modèle #4) quand un modèle précis est nommé.

Liens : [[corpus-golfiller]], [[modeles-corpus-golfiller]], [[golfiller-strat-source]]
