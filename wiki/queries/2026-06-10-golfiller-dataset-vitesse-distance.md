---
type: query
title: Golfiller, dataset sourcé vitesse de swing et distance par club
aliases: [golfiller-dataset-vitesse-distance]
tags: [golfiller, pseo, product-led, data, client]
created: 2026-06-10
updated: 2026-06-10
sources: 12
confidence: high
status: stable
---

# Dataset vitesse de swing et distance par club (sourcé)

> **En résumé.** Matière première du modèle « vitesse/distance par club » de [[modeles-pseo-2026-06-10-golfiller]]. Toutes les données viennent de sources ouvertes et vérifiées une à une (TrackMan, Shot Scope, Arccos, USGA/R&A) : data mesurée par launch monitor ou shot tracking uniquement. Règle absolue appliquée : chaque chiffre porte sa source, et la page publiée listera ces sources en fin de page. Une table déclarative (vitesses par âge) a été écartée du contenu publiable, conservée ici en confidence low.

## Données retenues pour la page (mesurées)

### PGA Tour par club (TrackMan 2024)

Vitesse de club, vitesse de balle et carry pour les 12 clubs. Driver : 115 mph / 171 mph / 282 yards. Fer 7 : 92 mph / 123 mph / 176 yards. PW : 84 mph / 104 mph / 142 yards. Table complète dans la source 1. Recoupement officiel USGA/R&A 2024 : club speed moyen PGA Tour 115,9 mph, drive moyen mesuré 300,2 yards (source 5).

| Club | Club speed (mph) | Ball speed (mph) | Carry (yd) |
|---|---|---|---|
| Driver | 115 | 171 | 282 |
| Bois 3 | 110 | 162 | 249 |
| Bois 5 | 106 | 156 | 236 |
| Hybride | 102 | 149 | 231 |
| Fer 3 | 100 | 145 | 218 |
| Fer 4 | 98 | 140 | 209 |
| Fer 5 | 96 | 135 | 199 |
| Fer 6 | 94 | 130 | 188 |
| Fer 7 | 92 | 123 | 176 |
| Fer 8 | 89 | 118 | 164 |
| Fer 9 | 87 | 112 | 152 |
| PW | 84 | 104 | 142 |

### LPGA Tour par club (TrackMan 2023)

Driver : 96 mph / 143 mph / 223 yards. Fer 7 : 78 mph / 106 mph / 143 yards. PW : 72 mph / 88 mph / 111 yards. Table complète : source 2. L'angle d'attaque driver LPGA est positif (+3,0° dans la table TrackMan 2019, source 8) là où le PGA est négatif (-1,3°) : angle d'analyse pour la page.

| Club | Club speed (mph) | Ball speed (mph) | Carry (yd) |
|---|---|---|---|
| Driver | 96 | 143 | 223 |
| Bois 3 | 92 | 135 | 200 |
| Bois 5 | 90 | 130 | 189 |
| Hybride | 87 | 125 | 178 |
| Fer 4 | 82 | 118 | 175 |
| Fer 5 | 81 | 114 | 166 |
| Fer 6 | 80 | 111 | 155 |
| Fer 7 | 78 | 106 | 143 |
| Fer 8 | 76 | 102 | 133 |
| Fer 9 | 74 | 95 | 123 |
| PW | 72 | 88 | 111 |

### Vitesse de swing driver des amateurs, par handicap (TrackMan 2024, mesuré)

| Profil | Hommes (mph) | Femmes (mph) |
|---|---|---|
| Tour pro | 115 (PGA) | 96 (LPGA) |
| Scratch ou mieux | 110 | 90 |
| Handicap 5 | 101 | 87 |
| Handicap 10 | 95 | 83 |
| Handicap 15 | (golfeur moyen hcp 14,5 : 94) | 79 |
| Bogey golfer | 92 | non publié |

Source 3. La table TrackMan s'arrête là : pas de tranche 20+ publiée, ne pas extrapoler. Moyenne générale homme amateur : 93,4 mph, plus de 40 % des golfeurs mesurés entre 91 et 100 mph (source 4).

### Distance totale par club et par handicap, hommes (Shot Scope, P-Avg)

| Club | Scratch | Hcp 5 | Hcp 10 | Hcp 15 | Hcp 20 | Hcp 25 |
|---|---|---|---|---|---|---|
| Driver | 285 | 261 | 259 | 236 | 225 | 204 |
| Bois 3 | 261 | 234 | 227 | 215 | 195 | 178 |
| Hybride | 237 | 216 | 214 | 197 | 180 | 162 |
| Fer 4 | 223 | 201 | 199 | 186 | 169 | 151 |
| Fer 5 | 200 | 183 | 187 | 169 | 162 | 143 |
| Fer 6 | 185 | 172 | 171 | 162 | 151 | 137 |
| Fer 7 | 178 | 164 | 161 | 154 | 146 | 132 |
| Fer 8 | 166 | 153 | 150 | 146 | 138 | 122 |
| Fer 9 | 155 | 139 | 140 | 136 | 129 | 108 |
| PW | 141 | 126 | 127 | 121 | 108 | 90 |
| Gap wedge | 126 | 109 | 110 | 104 | 94 | 79 |
| Sand wedge | 105 | 86 | 98 | 84 | 85 | 80 |
| Lob wedge | 86 | 71 | 79 | 75 | 78 | 49 |

Yards, distance totale, métrique Shot Scope P-Avg (moyenne après retrait de 10 % d'outliers). Sources 6 et 7. Écart scratch vs hcp 25 au driver : 81 yards.

### Drive moyen hommes/femmes (Arccos 2024, shot tracking)

Hommes tous handicaps : 224,7 yards. Femmes : 176,2 yards (source 9).

### Référence officielle USGA/R&A (2024 Distance Report)

Drives mesurés sur parcours. Hommes amateurs (2019, dernière collecte) : 215,6 yards en moyenne, de 239,2 (hcp <6) à 176,6 (hcp 21+). Femmes amateurs : 147,9 yards en moyenne, de 196,7 (hcp <6) à 119,8 (hcp 29+). Tours 2024 : PGA 300,2 / LPGA 259,2 / Champions (50+) 279,2 yards. 48 % des drives PGA Tour 2024 dépassent 300 yards (source 5).

### Ratios pour le calculateur

- TrackMan : +1 mph de club speed = jusqu'à +3 yards au driver (source 3).
- Golf.com/TrackMan : ~2,5 yards par mph (source 4).
- Efficience réelle PGA Tour 2025 : 302,8 yds / 116,46 mph = 2,60 yards par mph (source 10).
- Conversions : 1 mph = 1,609 km/h ; 1 yard = 0,9144 m (définitions, pas de source métier).

## Écarté du publiable

- **Vitesses par âge (HackMotion, source 11)** : aucune méthodologie de mesure citée, fourchettes déclaratives. Confidence low, ne pas publier. Alternative mesurée pour parler des seniors : PGA Tour Champions (pros 50+) à 279,2 yards (source 5). La vraie table par âge existe chez Par4Success/TPI (source 12) mais n'est pas affichée publiquement : à acheter ou à remplacer par la data clients Golfiller.
- Données introuvables en mesuré : vitesse hommes hcp 20+, carry (et non distance totale) par club amateur, découpage Arccos par handicap.

## Sources (à reprendre en fin de page publiée)

1. Golf Monthly, « How Far Do PGA Tour Players Hit Every Club In The Bag? », données TrackMan 2024, 26/02/2025 : https://www.golfmonthly.com/tour/how-far-pga-tour-players-hit-every-club-in-the-bag
2. Golf Monthly, « How Far Do LPGA Tour Players Hit Every Club In the Bag? », données TrackMan 2023, 03/05/2024 : https://www.golfmonthly.com/features/the-game/how-far-lpga-tour-players-hit-every-club-in-the-bag
3. TrackMan, « What is Club Speed? », 23/09/2024 : https://www.trackman.com/blog/golf/what-is-club-speed
4. Golf.com, « Here's how fast golfers swing their driver, based on handicap », données TrackMan, 03/02/2021 : https://golf.com/instruction/how-fast-swing-driver-based-handicap/
5. USGA / R&A, « 2024 Distance Report », PDF officiel : https://assets.randa.org/c42c7bf4-dca7-00ea-4f2e-373223f80f76/138e4fb6-ef49-4d22-bc26-d759fc07e3f2/Distance%20Report%202024%20Annual%20Driving%20Distance%20Report.pdf
6. Golf Monthly, « How Far Do Amateur Golfers Drive The Ball In 2026? », données Shot Scope, 29/05/2026 : https://www.golfmonthly.com/features/how-far-does-the-average-amateur-golfer-drive-the-golf-ball-in-2026
7. GolfMagic, « The latest average total distance yardages by golf handicap category », données Shot Scope, 10/07/2025 : https://www.golfmagic.com/equipment/news/latest-total-distance-yardages-golf-handicap-category-are-out-where-do-you-stand
8. TrackMan, tables officielles PGA/LPGA 2019 (PDF) : https://teeituprva.com/wp-content/uploads/2019/03/PGA-AVERAGES-INTERACTIVE.pdf et https://teeituprva.com/wp-content/uploads/2019/03/LPGA-AVERAGES-INTERACTIVE.pdf
9. Golf.com, « How far golfers actually hit their drives, according to data », données Arccos 2023-2024, 09/05/2025 : https://golf.com/instruction/driving/how-far-golfers-actually-hit-their-drives-arccos/
10. Swing Man Golf, « Average Golf Swing Speed Chart », stats PGA Tour 2025 : https://swingmangolf.com/average-golf-swing-speed-chart-2/
11. HackMotion, « Average Golf Swing Speed by Age », 16/12/2025 (déclaratif, écarté) : https://hackmotion.com/average-golf-swing-speed-by-age/
12. TPI / Par4Success, « Club Head Speed by Age Group » : https://www.mytpi.com/articles/swing/club-head-speed-by-age-group-what-percentile-are-you-in

Pages liées : [[modeles-pseo-2026-06-10-golfiller]] · [[2026-06-10-golfiller-gsc-90j]] · [[entities/golfiller]] · [[concepts/data-proprietaire]]
