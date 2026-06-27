# Brèves — modèle de newsletter

Deuxième modèle de newsletter, à côté de l'édition Algorithme (`revuedepressIA/{date}-revue-presse.md`). Même boucle de production et d'apprentissage que l'édition Algorithme : [[methodes/cadrage-boucle-edition-algorithme]].

## Le principe

Ce n'est pas un digest, c'est une **revue d'actualité SEO intéressante**. On garde **les 3 informations les plus pertinentes du jour (3 max)** et on développe chacune succinctement. Une brève existe parce qu'elle est intéressante et qu'elle compte pour quelqu'un dans le search, pas parce qu'elle s'est produite. On ne liste pas les infos du jour, on garde les 3 qui méritent qu'on en parle.

**Le seul juge à l'entrée :** « est-ce une actu intéressante qui compte pour quelqu'un dans le SEO / GEO / IA-search / business du search, ou de l'info pour de l'info ? »

Passe si : ça raconte quelque chose (angle, tension, conséquence), ça touche le terrain search/business, tu aurais envie d'en parler à un confrère.

Dégage (« info pour info ») si : changelog ou spec granulaire, stat isolée sans histoire, tracking ultra-spécialiste, annonce produit brute sans conséquence.

**3 infos max, les meilleures.** Si une journée n'en sort que 2 vraiment intéressantes, on publie 2. Jamais une 3e tiède pour faire le compte.

## Le format

Une seule section : `## Les dernières infos 🍿`, puis **3 brèves numérotées maximum**. Pas d'info du jour approfondie type Algorithme, mais chaque brève est **développée succinctement** : un paragraphe court (3 à 5 phrases), le titre porte l'angle, le corps donne le fait daté + le contexte utile + ce qui le rend intéressant pour le search. On développe assez pour comprendre pourquoi ça compte, sans délayer.

Différence avec Algorithme : Algorithme creuse une info du jour + 3-4 brèves. Brèves choisit les 3 actus les plus pertinentes et les explique.

## La veille = scrape des conversations (méthode réelle)

La matière intéressante est dans ce que les gens du search se DISENT, pas dans les blogs d'agences qui rabâchent. WebSearch générique remonte ces blogs : c'est le piège, on ne part pas de là. Deux temps : découvrir les sujets chauds sur les réseaux, puis sourcer/vérifier chacun (un titre de thread n'est pas une source).

- **Reddit = canal principal**, scrapeable en `curl` via le flux `.rss` (le JSON et WebFetch sont bloqués). `curl -s -A "brevesbot/1.0" "https://www.reddit.com/r/SEO/top/.rss?t=week&limit=15"` sur les subs r/SEO, r/bigseo, r/TechSEO, r/juststart, r/GoogleAnalytics. Parse en grep/sed (pas de python, sandbox). On garde les threads à vrai sujet (débat, donnée, cas, chute de trafic), pas les « New to SEO ».
- **X = secondaire** : WebSearch `site:x.com <sujet/compte>` remonte le contenu des tweets mais les dates sont mélangées, vérifier chaque date.
- **LinkedIn = faible** (login, pas de RSS) : au mieux WebSearch `site:linkedin.com/posts`, ne pas compter dessus.
- **Presse search** : seulement pour sourcer un sujet déjà repéré, jamais comme point de départ.

Reddit/X donnent le SUJET, ensuite on remonte à la source réelle (doc Google, étude, data de l'auteur) et on vérifie. Source primaire introuvable = pas de brève.

## Périmètre

Tout tourne autour du **search** : SEO, GEO (Generative Engine Optimization / AEO, jamais SEO géographique), IA-search (LLM, moteurs génératifs, AI Overviews / AI Mode / SGE en tant qu'ils touchent la recherche), business du search (acquisition organique, monétisation, niches, mouvements de marché). Hors search = hors périmètre. Le périmètre est nécessaire mais pas suffisant : une info dans le périmètre mais pas intéressante dégage quand même.

## Règles (héritées de l'agent-synthetic)

- **Liens de sources TOUJOURS** : chaque brève finit par `*Sources : [nom](url) / [nom](url)*`. Pas de lien sourçable, pas de brève.
- **Anti-hallucination** : aucun chiffre, %, date ou citation hors d'une source réellement consultée. Donnée d'agence agrégée = signalée comme telle dans la note de fin.
- **Fraîcheur 4 mois** : rien de plus vieux que J−4 mois.
- **Recoupement** : viser 2 sources indépendantes par brève quand c'est possible.
- **Anti-redite** : ne pas répéter les brèves de l'édition Algorithme du jour ou de la veille.
- **Voix SyntheticBrain** : analyste search, vouvoiement, factuel, direct, avec un angle quand l'info en a un. Pas de métaphore, pas de tiret cadratin, aucun personnage, aucune injonction « fais ça lundi ».
- **Rien n'est envoyé** : draft uniquement.

## Rythme quotidien

Chaque jour : **1 édition Brèves + 2 éditions revue de presse (Algorithme)**.

- Brèves : 1 fois par jour, ce fichier (`breves-IA/{date}-breves.md`).
- Algorithme : 2 fois par jour (`revuedepressIA/{date}-revue-presse.md`, puis `-v2`).

L'édition Brèves et les deux éditions Algorithme du même jour ne se répètent pas : anti-redite croisée entre les trois.

## Sélection (filtre d'intérêt)

Pas de grille notée : un seul juge, le filtre d'intérêt du *Principe* ci-dessus. On classe les candidats par pertinence et on garde **les 3 meilleurs, 3 max**. Une info devient une brève si elle est intéressante et qu'elle compte pour le search ; sinon elle dégage, même dans le périmètre. Cas des **études et stats** : admises seulement si elles racontent quelque chose (une stat brute dégage, la même avec un angle peut passer). Si tu ne sais pas dire pourquoi c'est intéressant, c'est que ça ne l'est pas. On ne met jamais une 3e brève tiède pour faire le compte.

## Convention de fichier

`breves-IA/{YYYY-MM-DD}-breves.md`. Suffixer `-v2`, `-v3` si le fichier du jour existe déjà.

## Structure type

```markdown
# Brèves IA — {YYYY-MM-DD}

## Les dernières infos 🍿

**1. Titre qui porte l'angle intéressant**

Paragraphe court (3 à 5 phrases) : le fait daté, le contexte utile, puis ce qui le rend intéressant pour le search.

*Sources : [nom](url) / [nom](url)*

---

(2 et 3 — 3 brèves maximum, ou moins)

*Note de fiabilité : 2-3 lignes honnêtes. Rien n'a été envoyé.*
```
