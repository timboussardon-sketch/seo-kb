# Brèves IA — modèle de newsletter

Deuxième modèle de newsletter, à côté de l'édition Algorithme (`revuedepressIA/{date}-revue-presse.md`). Même boucle de production et d'apprentissage que l'édition Algorithme : [[methodes/cadrage-boucle-edition-algorithme]].

## Le format

Une seule section : `## Les dernières infos 🍿`, puis **10 brèves numérotées** par jour. Pas d'info du jour approfondie, pas de tableau, pas d'analyse longue. Chaque brève fait 2 à 4 phrases.

Différence avec Algorithme : Algorithme creuse une info du jour + 3-4 brèves. Brèves IA ne fait que du court, mais en plus grand nombre (10), pour couvrir large.

## Règles (héritées de l'agent-synthetic)

- **Périmètre strict** : SEO, IA, LLM, Google, moteurs de recherche, search marketing. Rien d'autre. Test : « est-ce que ça change la façon dont on est trouvé, lu ou cité dans un moteur ? ».
- **Liens de sources TOUJOURS** : chaque brève finit par `*Sources : [nom](url) / [nom](url)*`. Pas de lien sourçable, pas de brève.
- **Anti-hallucination** : aucun chiffre, %, date ou citation hors d'une source réellement consultée. Donnée d'agence agrégée = signalée comme telle dans la note de fin.
- **Recoupement** : viser 2 sources indépendantes par brève quand c'est possible.
- **Anti-redite** : ne pas répéter les brèves de l'édition Algorithme du jour ou de la veille.
- **Voix SyntheticBrain** : analyste search/IA, vouvoiement, factuel, direct. Pas de métaphore, pas de tiret cadratin, aucun personnage.
- **Rien n'est envoyé** : draft uniquement.

## Rythme quotidien

Chaque jour : **1 édition Brèves + 2 éditions revue de presse (Algorithme)**.

- Brèves : 1 fois par jour, ce fichier (`breves-IA/{date}-breves.md`).
- Algorithme : 2 fois par jour (`revuedepressIA/{date}-revue-presse.md`, puis `-v2`).

L'édition Brèves et les deux éditions Algorithme du même jour ne se répètent pas : anti-redite croisée entre les trois.

## Grille de sélection (seuil minimum 4,5/5)

Grille commune avec Algorithme, détaillée dans [[notation]]. Une info ne devient une brève que si elle passe la grille. Chaque candidat est noté de 0 à 5 sur les 5 critères, on fait la moyenne, et **on ne retient que les moyennes ≥ 4,5**. Seuil exigeant et assumé : si moins de 10 candidats atteignent 4,5, on élargit la veille pour remonter à 10, jamais on ne descend le seuil.

| Critère | Note 0-5 sur quoi |
|---|---|
| **Pertinent** | L'info change quelque chose pour un consultant SEO/IA ou ses clients. Pas une curiosité tech sans conséquence search. |
| **Original** | Pas déjà rabâchée partout ni reprise des éditions récentes. Apporte un fait, un chiffre ou une nuance qu'on ne lit pas dans tous les résumés. |
| **Angle intéressant** | Il y a un angle, une implication, une tension, pas juste une annonce brute recopiée. |
| **Basé sur ma doctrine** | Se relie à la doctrine de Tim (4 piliers, anti-volume, données propriétaires / ce qui ne se copie pas, SEO post-SGE, GEO/AEO). Lien réel, pas décoratif. |
| **Orienté IA SEO** | Au cœur du search/IA, pas en périphérie. Touche la façon dont on est trouvé, lu ou cité par un moteur. |

## Convention de fichier

`breves-IA/{YYYY-MM-DD}-breves.md`. Suffixer `-v2`, `-v3` si le fichier du jour existe déjà.

## Structure type

```markdown
# Brèves IA — {YYYY-MM-DD}

## Les dernières infos 🍿

**1. Titre de la brève**

2 à 4 phrases factuelles.

*Sources : [nom](url) / [nom](url)*

---

(… jusqu'à 10)

*Notes de fiabilité : … Rien n'a été envoyé.*
```
