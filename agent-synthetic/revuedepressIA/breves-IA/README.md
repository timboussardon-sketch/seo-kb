# Brèves IA — modèle de newsletter

Deuxième modèle de newsletter, à côté de l'édition Algorithme (`revuedepressIA/{date}-revue-presse.md`).

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
