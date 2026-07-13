---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: quels mots-clés ajouter à ma page pour ranker
intention: Do
capacite_qadence: seo-entites-vectorielles
schema: HowTo
created: 2026-07-13
sources_vault: [[entites-vectorielles]], [[information-gain]], [[purete-vectorielle]], [[ingenierie-semantique-inversee]], [[methode-organikk-4-piliers]]
---

# Quels mots-clés ajouter à ma page pour ranker

Ajouter des mots-clés ne fait pas ranker. Ce qui aligne une page, c'est compléter le nuage d'entités attendu par l'intention, apporter ce que le corpus n'a pas encore, et ne pas diluer la page sur plusieurs intentions.

## Sortir de la logique de densité de mots-clés

- On ne vise plus une densité de mots-clés mais un nuage d'entités qui rapproche le vecteur de la page du barycentre attendu [[entites-vectorielles]]
- Les moteurs modernes comparent les pages aux requêtes par embeddings, pas par correspondance lexicale [[entites-vectorielles]]
- Le keyword stuffing dégrade la performance : moins 8 % sur GEO-Bench, moins 9 % sur Perplexity en production [[information-gain]]

## Compléter les quatre catégories d'entités

- Entités techniques : le vocabulaire obligatoire présent chez plus de 80 % du top 10, socle de pertinence [[entites-vectorielles]]
- Preuves quantitatives : chiffres sourcés au format chiffre plus unité plus contexte, jamais « beaucoup » [[entites-vectorielles]]
- Vecteurs multimodaux : schémas, tableaux, outils, formats attendus par l'intention [[entites-vectorielles]]
- Éléments de divergence : concepts experts présents chez moins de 10 % des concurrents [[entites-vectorielles]]

## Ajouter ce que le corpus n'a pas déjà dit

- Une page gagne de l'information gain quand elle ajoute ce que le corpus existant n'a pas : un chiffre, un fait vérifié, un angle, une donnée terrain [[information-gain]]
- Reprendre mécaniquement l'existant produit un contenu « sans effort », noté au plus bas par les Quality Raters [[information-gain]]
- L'ajout de citations verbatim (Quotation Addition) donne le gain le plus fort mesuré : plus 41 % sur PAWC [[information-gain]]
- L'ajout de statistiques donne plus 34 %, l'ajout de sources plus 29 % [[information-gain]]
- Depuis l'architecture Titans, apporter l'information manquante prime sur répéter la réponse déjà connue [[ingenierie-semantique-inversee]]

## Écrire chaque affirmation sous forme atomique

- L'IA vérifie les claims par atomisation : chaque affirmation est découpée en fait isolé, vérifié indépendamment [[information-gain]]
- « La Tesla est une voiture chère avec une bonne autonomie » n'est pas cité, faute d'atomes vérifiables [[information-gain]]
- Un claim exploitable est un fait chiffré et sourçable, isolé [[information-gain]]

## Ne pas casser la pureté vectorielle de la page

- Une page traite une seule intention, sinon son vecteur devient le barycentre de plusieurs zones et s'éloigne de chaque requête [[purete-vectorielle]]
- Plus le contenu s'étale hors intention, moins il est cité par les moteurs génératifs [[purete-vectorielle]]
- Les micro-intentions adjacentes se rangent en FAQ, le corps reste pur [[purete-vectorielle]]
- La longueur sans pureté est un handicap, pas un signal d'autorité [[purete-vectorielle]]

## Lancer le diagnostic avec Qadence

Qadence part de l'intention de ta page telle qu'elle ressort dans ta Search Console, génère les entités attendues par catégorie, puis liste celles que ta page ne contient pas encore. Tu récupères une liste d'entités à intégrer, pas une liste de mots-clés à bourrer. Aucun chiffre inventé : donnée absente, donnée signalée.

→ **Lancer mon diagnostic** sur qadence.io/app
