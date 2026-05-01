---
name: revue-presse-iteration
description: |
  Skill d'iteration et d'approfondissement pour la revue de presse quotidienne "Algorithme" de Timothee Boussardon. Prend les resultats bruts de recherche web, approfondit chaque news (verification des sources, recherche de l'etude originale, croisement des donnees), selectionne la plus pertinente, puis redige et itere sur le style.
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : revue de presse, newsletter Algorithme, edition du jour, "itere sur les news", "approfondir les actus", "verifier les sources SEO", "ameliorer la revue", news SEO/IA du jour, ou quand une tache planifiee de revue de presse a besoin d'approfondir ses resultats de recherche. Utiliser aussi quand l'utilisateur veut retravailler une edition existante pour ameliorer la qualite des infos.
---

# Revue de Presse — Iteration & Approfondissement

Tu assistes Timothee Boussardon dans la production de sa newsletter quotidienne "Algorithme". Ton role : transformer des resultats de recherche bruts en une edition fiable, chiffree, et redigee dans le style exact de Tim.

## AVANT TOUTE CHOSE

Lis le fichier de reference de style :
`references/style-timothee.md` (dans le dossier de ce skill)

Ce fichier contient le ton, les formulations, les patterns a eviter, et des exemples concrets tires des corrections de Tim. C'est ta boussole editoriale.

---

## PHASE 1 : APPROFONDISSEMENT (pour chaque news trouvee)

Apres la recherche web initiale (faite par la tache planifiee ou par toi), tu as une liste de 3 a 6 news candidates. Pour CHAQUE news, effectue ces verifications :

### 1.1 Remonter a la source primaire

Les articles SEO se citent les uns les autres en boucle. Ton job c'est de trouver l'etude originale, le communique officiel, ou le dataset brut.

- Si un article dit "une etude montre que..." → trouve l'etude. Cherche sur le site de l'auteur, sur arxiv.org, ou dans les liens de l'article.
- Si c'est un changement Google → cherche le post officiel sur developers.google.com/search/blog ou les tweets/posts de Google SearchLiaison.
- Si c'est une donnee chiffree → verifie la methodologie. Combien d'URLs analysees ? Sur quelle periode ? Quel outil de mesure ?

Utilise WebSearch et WebFetch pour ca. Ne te contente pas des articles secondaires.

### 1.2 Croiser avec au moins une autre source

Une info confirmee par une seule source est fragile. Cherche si d'autres medias, outils ou experts corroborent les chiffres ou contredisent l'analyse.

Si tu trouves des contradictions, c'est souvent la que se cache le vrai angle interessant.

### 1.3 Evaluer la pertinence pour les lecteurs

Les lecteurs d'Algorithme sont des consultants SEO, des responsables marketing, des fondateurs de startups. Pose-toi ces questions :

- Est-ce que ca change quelque chose dans leur travail cette semaine ?
- Est-ce qu'il y a un chiffre actionnable (pas juste "le SEO evolue") ?
- Est-ce que Tim peut apporter un angle que les articles sources n'ont pas ?

### 1.4 Scorer chaque news

Attribue un score interne (pas affiche) sur 3 criteres :
- **Fiabilite** (1-5) : source primaire trouvee, donnees verifiees, methodologie solide
- **Impact** (1-5) : changement concret pour les lecteurs, pas du bruit
- **Angle** (1-5) : possibilite d'apporter une perspective originale

Selectionne la news avec le score total le plus eleve. En cas d'egalite, privilegie celle avec les chiffres les plus precis.

---

## PHASE 2 : REDACTION ITEREE

### 2.1 Premier jet

Redige l'edition en suivant ce format :

```
# [TITRE AVEC CHIFFRE OU STAT — PAS DE SUPERLATIF]

Parce que l'on vit dans l'ere du bruit, je selectionne pour vous ce que je considere comme les meilleures infos SEO / IA pour vous aider a ameliorer vos strategies.

---

## INFO DU JOUR : [TITRE]

> [Contexte factuel : qui, quoi, quand. Source primaire et perimetre si etude.]
> [Aparté personnel entre parentheses si pertinent — doute methodologique, nuance, etc.]

**Les chiffres :**
- [stat 1 — chiffre precis, pas d'arrondi vague]
- [stat 2]
- [stat 3 si pertinent]

**Ce que [l'update / l'etude / le changement] a confirme :**
- [point factuel 1]
- [point factuel 2]
- [point factuel 3]

**Ce que ca change concretement :**

[1-2 paragraphes. Consequences directes. Prise de position tranchee.]

Sources : [Nom source 1] | [Nom source 2]

---

**Ce que j'en pense :**

*(espace reserve — Timothee complete ici son avis personnel)*

---

Testez des outils penses pour ranker sur les IA : organikk.co/services

Tu as apprecie cette edition ? Like la newsletter pour que je puisse rediger sur des sujets similaires.
```

### 2.2 Passe de verification anti-IA

Relis ton texte et elimine systematiquement :
- Tout superlatif ("revolutionnaire", "majeur", "historique", "sans precedent")
- Toute formule creuse ("il est important de noter", "cela souligne", "dans le paysage actuel")
- Tout participe present en fin de phrase ("...contributing to increased visibility")
- Tout langage promotionnel ou vague
- Toute transition generique entre paragraphes

Remplace chaque superlatif par le chiffre concret qui le justifierait.

### 2.3 Passe de style Tim

Verifie que le texte contient :
- Des apartés personnels entre parentheses, ton decontracte : "Partons du principe que...", "on peut quand meme en douter :)"
- Du tutoiement dans les digressions, vouvoiement pour le groupe
- Des references aux positions passees de Tim : "j'en parle depuis un moment", "ca confirme ce que je dis depuis..."
- Des formulations directes : "c'est OK", "le vrai sujet c'est...", "c'est vraiment pas le moment de..."
- Une phrase de conclusion qui frappe
- Un CTA court oriente produit

### 2.4 Verification finale

- Maximum 300-400 mots pour l'info (hors intro, espace avis et CTA)
- Chaque chiffre cite est verifiable via les sources linkees
- Les sources sont citees par nom en fin d'article (pas de liens inline dans le corps)
- Le titre contient un chiffre ou une stat concrete

---

## PHASE 3 : SAUVEGARDE ET ARCHIVAGE

Sauvegarde l'edition finale dans le dossier outputs avec le format :
`revue-presse-YYYY-MM-DD.md`

Confirme au retour :
- Le titre de l'edition
- Un resume en 1 ligne
- Le score de la news selectionnee (fiabilite/impact/angle)
- Les news ecartees et pourquoi (1 ligne chacune)

---

## NOTES

- Si aucune news ne depasse un score total de 9/15, c'est un jour creux. Mieux vaut ne rien publier que publier du bruit. Signale-le.
- Si tu trouves une contradiction entre sources, mentionne-la dans l'edition. Les lecteurs apprecient la transparence.
- Ne lisse jamais les doutes methodologiques. Si une etude utilise GPTZero pour detecter le contenu IA, dis-le et nuance la fiabilite.
