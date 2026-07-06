---
type: source
source_type: doctrine
title: "Modèle corpus 5 : distances réelles par profil"
aliases: [modele-corpus-5-golfiller, distances-par-profil]
tags: [golfiller, pseo, product-led, data-proprietaire, corpus, modele, haute-surprise]
created: 2026-07-06
updated: 2026-07-06
sources: 1
confidence: medium
status: draft
---

# Modèle corpus 5 : distances réelles par profil

Le corpus 5 du [[corpus-golfiller|Corpus Golfiller]]. C'est le seul actif non copiable : les distances viennent de l'instrumentation client de Golfiller, pas d'une source publique. Ce fichier est le modèle, pas la page finale. Tous les chiffres sont notés `‹…›` : ce sont des marqueurs de format, aucune donnée n'est inventée.

## Couche 1 : la base (le corpus)

Une ligne = un profil croisé à un club. La donnée agrégée, jamais la donnée individuelle.

| Champ | Type | Exemple de format | Rôle |
|---|---|---|---|
| `profil_index` | tranche | `36+`, `28-36`, `18-28`, `10-18`, `<10` | variable pSEO principale (le golfeur connaît son index) |
| `sexe` | segment | `homme`, `femme` | sous-filtre |
| `club` | catégorie | `Driver`, `Bois 3`, `Hybride`, `Fer 5`, `Fer 7`, `Fer 9`, `PW`, `SW` | ligne du tableau |
| `carry_m` | mesure | `‹carry moyen, m›` | distance de vol moyenne |
| `total_m` | mesure | `‹distance totale moyenne, m›` | vol + roule |
| `n` | entier | `‹taille de l'échantillon›` | garde-fou de fiabilité |
| `ecart_type_m` | mesure | `‹dispersion, m›` | honnêteté statistique |
| `maj` | date | `2026-07-06` | fraîcheur de l'agrégat |

Clé d'unicité : `profil_index × sexe × club`.

### Comment la donnée entre

Trois sources possibles, par ordre de propreté :
1. Le quiz profileur (« Quelle balle pour vous ? ») qui demande index, sexe et distances ressenties par club.
2. Les données déclarées à la commande (index renseigné, balle achetée).
3. À terme, un carnet de distances que le client tient sur le site.

Anonymisation dès la réception, DPA, agrégation seule. Aucune ligne individuelle ne sort de la base.

### Garde-fou anti-invention

Une cellule ne se publie que si `n ≥ ‹seuil, ex. 30›`. Sous le seuil, la cellule affiche « donnée en cours de collecte », jamais une estimation. C'est la règle absolue de production du corpus : pas de donnée, pas de chiffre.

## Couche 2 : la page publique (le modèle)

Variable pSEO = `profil_index`. Une URL par tranche d'index, chacune sur une requête réelle (« distance moyenne golf index ‹X› », « distance driver handicap ‹X› »). Le squelette est en HTML sémantique brut, answer-first, réhabillable ensuite au template maison.

```html
<h1>Distances moyennes par club pour un index ‹18-28›</h1>

<p>Un golfeur d'index ‹18-28› porte son driver à ‹carry› m en moyenne
(‹total› m avec la roule), et son fer 7 à ‹carry› m. Chiffres mesurés
sur ‹n› golfeurs de ce profil, mis à jour le ‹date›.</p>

<table>
  <caption>Distances moyennes, index ‹18-28›, hommes</caption>
  <thead>
    <tr><th>Club</th><th>Carry (m)</th><th>Total (m)</th><th>Échantillon</th></tr>
  </thead>
  <tbody>
    <tr><td>Driver</td><td>‹carry›</td><td>‹total›</td><td>‹n›</td></tr>
    <tr><td>Bois 3</td><td>‹carry›</td><td>‹total›</td><td>‹n›</td></tr>
    <tr><td>Fer 7</td><td>‹carry›</td><td>‹total›</td><td>‹n›</td></tr>
    <!-- une ligne par club de la base -->
  </tbody>
</table>

<h2>Ce que ces distances changent pour le choix de balle</h2>
<p>À ce profil, la vitesse de swing tourne autour de ‹mph› mph, ce qui
oriente vers une balle de compression ‹basse/moyenne›. La collection
filtrée sur ce profil : <a href="/balles?index=18-28">voir les balles</a>.</p>

<h2>Calculer votre index exact</h2>
<p>Ces tranches partent de l'index. Si vous ne connaissez pas le vôtre :
<a href="/calcul-index-golf">le calculateur</a>.</p>
```

## La Haute Surprise (ce qui rend la page non copiable)

Le net regorge de tableaux de distances « théoriques » (PGA Tour, moyennes de tour). Personne n'a les distances **réelles des golfeurs amateurs par index**, avec la dispersion. L'angle contrarien vient de là : montrer l'écart entre la distance qu'un golfeur croit faire et celle qu'il fait vraiment à son index. Un acteur ne peut pas recopier ce chiffre, il faudrait ses propres clients.

C'est ce que le [[golfiller-strat-source|cas Golfiller]] appelle la data propriétaire agrégée : elle monte le Confidence Score de l'IA et force la citation.

## Maillage sortant (obligatoire, 2 minimum)

- Vers le calculateur d'index (corpus 1) : « calculez votre index exact ».
- Vers la collection filtrée par profil (le point de conversion).
- Vers le tableau de compression (corpus 2) quand la balle recommandée est nommée.

Liens : [[corpus-golfiller]], [[golfiller-strat-source]], [[pseo-data-driven-models]]
