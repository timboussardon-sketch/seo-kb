---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: mon site perd des positions sur Google
intention: Do
capacite_qadence: rank-tracker + audit_gsc
schema: HowTo
created: 2026-07-13
sources_vault: [[passage-ranking]], [[entites-vectorielles]], [[intention-recherche]], [[fraicheur-contenu]]
---

# Mon site perd des positions sur Google

Une page qui glisse sur une requête décroche sur trois plans : son contenu n'est plus aligné avec l'intention, son vecteur sémantique est devenu générique, ou ses passages ne sont plus extractibles. On corrige l'alignement, on renforce le vecteur, on optimise passage par passage, puis on remet à jour.

## Vérifier l'alignement de la page avec l'intention
- L'intention de recherche est le besoin réel derrière la requête, pas les mots tapés : un décalage fait glisser la page [[intention-recherche]]
- Deux requêtes qui partagent le même top 10 relèvent de la même intention et d'une seule page ; un contenu qui s'en écarte perd sa place [[intention-recherche]]
- Situer la page sur la grille Know Simple / Know / Do pour vérifier qu'elle répond au bon niveau de maturité [[intention-recherche]]

## Renforcer le vecteur sémantique de la page
- Une page au vecteur générique a le même vecteur que tout le monde et devient invisible dans la SERP [[entites-vectorielles]]
- Reconstituer les 4 catégories d'entités : techniques, preuves quantitatives, vecteurs multimodaux et éléments de divergence à haute surprise [[entites-vectorielles]]
- Les moteurs comparent la page à la requête par embeddings, pas par correspondance lexicale : la densité de mots-clés ne suffit plus [[entites-vectorielles]]

## Optimiser les passages, pas seulement la page
- Google classe un passage spécifique plutôt que la page entière, ce qui déplace l'unité d'optimisation vers le bloc [[passage-ranking]]
- Placer un passage ancré de 150 à 200 mots dans les 300 premiers mots pour rester extractible en Featured Snippet et AI Overview [[passage-ranking]]
- Traiter chaque H2 comme un vecteur évalué séparément et y répartir les entités attendues [[entites-vectorielles]]

## Remettre la page à jour
- Une page récente est citée environ 3 fois plus sous 3 mois : la fraîcheur soutient la reconquête de position [[fraicheur-contenu]]

## Lancer le diagnostic avec Qadence
- Le rank-tracker suit l'évolution des positions par requête sur ta propriété et isole les URL qui décrochent, sans chiffre inventé : donnée absente = signalée
- L'audit_gsc relie chaque perte de position à l'intention de la requête pour trancher entre réalignement du contenu et renforcement du vecteur
→ CTA : qadence.io/app
