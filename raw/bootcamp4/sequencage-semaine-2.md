---
title: Séquençage Semaine 2 — Création de contenu + scoring
bootcamp: 4
semaine: 2
theme: création de contenu (brief → workflow → scoring → call)
---

# Séquençage Semaine 2 — Bootcamp 4

**Logique de la semaine** : input → run → évaluation → call.
Chacun arrive au call avec un article + un diagnostic, pas juste un article brut.

| Jour | Thème | Skill / Action | Livrable |
|------|-------|----------------|----------|
| 1 | Brief éditorial | `seo-brief-contenu` | 1 brief structuré stocké dans le dossier Claude |
| 2 | Rédaction bout en bout | `article-engine-pipeline` | 1 article produit (brut) |
| 3 | Fact-checking | Grok + prompt d'intégration sources | Article enrichi de chiffres + URL sourcées |
| 4 | Scoring qualité | Surprise Score + Grounding Score | Article scoré + 2 axes d'amélioration |
| 5 | Call collectif (10h00) | Revue en live de 2-3 cas | Patterns d'erreur identifiés |

---

## Jour 1 — Brief éditorial

Salut à tous, j'espère que vous avez passé un bon WE prolongé,

On démarre la semaine 2 🎉

L'objectif de cette semaine : que vous sortiez avec un workflow qui vous aide à rédiger le meilleur article possible, un article que l'on va venir scorer (notamment pour les LLMs) pour pouvoir l'améliorer plus facilement.

Aujourd'hui, on s'attaque à l'étape 1, la plus importante du process : le brief.

La qualité de votre rédaction dépend de la qualité du brief qu'on lui donne.

On va utiliser le skill `seo-brief-contenu` que vous retrouverez ici en deux formats :

https://drive.google.com/drive/folders/1WocuOXI4NkOzQMYTIHElX-MbLuKDD0Zk?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto

1 en MD pour ceux qui ne veulent pas le personnaliser, et en format Word pour ceux qui souhaitent ajouter ou retirer des choses (ensuite, une fois modifié, vous le donnez en MD à Claude).

Ensuite :
1. Choisir 1 mot-clé sur lequel vous voulez ranker
2. Lancer le skill `seo-brief-contenu` sur ce sujet

Petit rappel : continuez à stocker tout ce que vous produisez. Plus votre Claude a de contexte, plus il devient pertinent.

Venez en MP si vous bloquez 🙏

---

## Jour 2 — Rédaction bout en bout

Salut à tous,

Jour 2. Aujourd'hui on lance le moteur.

On va utiliser le skill `article-engine-pipeline`, qui enchaîne automatiquement les 5 phases : décodage sémantique RRF → FAQ stratégique FM → workflow de rédaction 8 étapes → checklist fact-check.

C'est le skill "bout en bout". Vous lui donnez votre brief du jour 1, il vous sort un article complet.

Votre mission aujourd'hui :
1. Reprendre le brief du jour 1
2. Lancer `article-engine-pipeline` dessus
3. Stocker l'article brut dans votre dossier Claude (sous-dossier `articles/`)

⚠️ Ne touchez pas encore à l'article. On veut la sortie brute du pipeline. C'est cette version qu'on va fact-checker demain.

Si le pipeline déraille sur une étape (Surprise Gap pas assez fort, données manquantes, etc.), notez-le. Ce sera utile pour le call.

À demain pour le fact-checking 💪

---

## Jour 3 — Fact-checking avec Grok

Salut à tous,

Jour 3. Votre article est sorti du pipeline. Avant de le scorer, on lui ajoute la couche qui change tout pour l'autorité : **les sources et les chiffres vérifiés**.

Le pipeline produit un article structurellement solide. Mais sur les affirmations fortes, il manque souvent la preuve atomique — le chiffre précis, l'URL primaire qui valide. C'est exactement ce qu'on va combler aujourd'hui, et pour ça on utilise **Grok** (qui a accès à X et au web en temps réel, donc des sources fraîches et primaires).

Votre mission aujourd'hui :
1. Reprendre l'article brut du jour 2
2. Ouvrir Grok et lui coller le prompt ci-dessous (en remplaçant `[Insérer ici le texte complet d'origine]` par votre article)
3. Récupérer la version enrichie (chiffres + URL encadrés par des guillemets français `« »`)
4. Relire chaque ajout : Grok peut halluciner une URL ou un chiffre — **vérifier manuellement chaque source** avant de l'accepter
5. Stocker la version fact-checkée dans votre dossier Claude (sous-dossier `articles/` avec suffixe `-factchecked`)

**Prompt à coller dans Grok :**

```
Rôle : Spécialiste du Fact-Checking et de la consolidation de l'autorité du contenu.

Objectif : Intégrer des sources précises (URL) ou des chiffres vérifiés directement dans le texte d'origine, là où l'affirmation est la plus forte et nécessite une preuve factuelle immédiate.

Ressources fournies :
Le Texte à Modifier : ([Insérer ici le texte complet d'origine])

Raisonnement : Pensez étape par étape à l'endroit optimal de chaque ajout de source/chiffre dans le texte.

Consignes d'intégration :
Placement : Placez chaque source (URL) ou chaque chiffre là où il apporte le plus de crédibilité ou de précision à l'affirmation la plus proche.
Formatage Strict : Vous devez encadrer uniquement l'ajout (le chiffre ou l'URL) par des guillemets doubles français : « [Chiffre ou URL] ».
Priorité : Donnez la priorité aux chiffres précis ou aux URL des sources primaires qui valident des faits spécifiques.
```

⚠️ **Règle d'or** : on ne fait pas confiance aveuglément à Grok. Chaque chiffre, chaque URL doit être ouvert et vérifié. Une source qui n'existe pas ou un chiffre inventé tue plus de crédibilité qu'il n'en ajoute. Si le doute persiste, on retire.

À demain pour le scoring 💪

---

## Jour 4 — Scoring de l'article

Salut à tous,

Jour 4. Aujourd'hui, on évalue.

Produire un article, c'est bien. Le sourcer, c'était hier. Savoir s'il est bon avant qu'il aille en SERP, c'est aujourd'hui. On le fait avec **2 scores** :

**Surprise Score** — Est-ce que votre article dit quelque chose que les concurrents n'ont PAS dit ? Si oui, Google a une raison de le remonter. Si non, il est noyé.

**Grounding Score** — Est-ce que votre article est aligné sémantiquement avec l'intention de recherche ciblée ? Les bons termes, les bonnes entités, les bons vecteurs.

Votre mission aujourd'hui :
1. Reprendre l'article **fact-checké du jour 3** (avec les sources et chiffres validés)
2. Scorer manuellement chaque dimension (Surprise + Grounding)
3. Identifier **2 axes d'amélioration concrets** (pas "améliorer l'intro" — du précis : "ajouter données chiffrées dans le H2 sur X")
4. Stocker le scoring dans votre dossier Claude (sous-dossier `scoring/` ou directement à côté de l'article)

Le scoring, c'est aussi ce qui va alimenter votre Claude au fil du temps. Plus vous scorez, plus il apprend ce qui marche chez vous.

On se voit demain au call à 10h00 — venez avec votre article + vos scores + vos 2 axes. On regarde 2-3 cas en live.

---

## Jour 5 — Call collectif

Salut à tous,

Jour 5 🎉 on a notre call à 10h00.

Ce que vous amenez :
- Votre article produit jour 2, fact-checké jour 3
- Vos scores Surprise + Grounding (jour 4)
- Vos 2 axes d'amélioration identifiés
- **1 question concrète** sur laquelle vous bloquez

Format du call :
- Tour de table express (1 min / personne) : sujet + score global
- Deep dive sur 2-3 cas représentatifs
- Identification des patterns d'erreur communs
- Q&R libre

L'objectif n'est pas que je vous dise si votre article est bon. L'objectif est que **vous repartiez avec une méthode d'évaluation que vous pouvez reproduire** sur les 50 prochains articles.

À tout à l'heure 🙌

---

## Notes pour Tim (interne)

- **Point d'attention** : le jour 1 (brief) est le plus stratégique. Si le brief est faible, tout le reste s'effondre. Insister là-dessus dans le message de jour 1.
- **Lien avec S1** : la semaine 1 a installé les skills et stocké le contexte. La S2 active concrètement la chaîne brief → article → fact-check → scoring.
- **Charge cognitive** : plus light que S1 d'après l'engagement initial ("les autres seront cool cool"). Tenir cette promesse — chaque jour = 1 action claire, 1 livrable.
- **Risque jour 3 (fact-check Grok)** : hallucinations d'URL ou de chiffres. Marteler la vérification manuelle. Penser à montrer en call un cas concret de source inventée pour ancrer le réflexe.
- **Préparation call** : récupérer en amont 2-3 articles + scoring des participants les plus avancés pour la revue en live.
