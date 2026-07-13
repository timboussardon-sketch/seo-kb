---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: pourquoi Google affiche la mauvaise page de mon site
intention: Do
capacite_qadence: seo-cannibalisation
schema: HowTo + Article
created: 2026-07-13
sources_vault: [[cannibalisation]], [[intention-recherche]]
---

# Pourquoi Google affiche la mauvaise page de mon site

Google sert la page qu'il juge la plus alignée avec l'intention de la requête ; quand ce n'est pas celle que tu veux, c'est que deux pages se disputent le mot-clé et que Google hésite, ce qui se voit dans la Search Console à la position moyenne qui saute selon l'URL servie.

## Google sert l'URL qu'il juge la plus proche de l'intention

- L'intention de recherche est le besoin réel derrière la requête, pas les mots tapés ; Google sert la page qui y répond le mieux [[intention-recherche]]
- Si la page affichée n'est pas la bonne, l'alignement entre la page et l'intention est en cause [[intention-recherche]]

## Une URL qui change au fil des jours signale une hésitation

- Quand Google alterne entre deux URL sur la même requête, la position moyenne saute dans la Search Console [[cannibalisation]]
- Deux pages se disputent le mot-clé, aucune ne consolide l'autorité, Google tranche différemment selon les jours [[cannibalisation]]

## Le bon diagnostic croise la requête et la page

- On ne conclut jamais à l'œil : croiser requête × page dans la Search Console montre quelle URL sort sur quoi [[cannibalisation]]
- Vérifier si les deux pages visent la même intention ou deux besoins distincts [[intention-recherche]]
- Deux requêtes qui partagent le même top 10 relèvent d'une seule intention, donc d'une seule page à servir [[intention-recherche]]

## Diriger Google vers la bonne page

- Re-spécialiser chaque page sur sa micro-intention avec des ancres distinctes pour lever l'ambiguïté [[cannibalisation]]
- Fusionner quand les deux pages servent le même besoin, l'une absorbe l'autre [[cannibalisation]]
- 301 de l'URL faible vers la page à faire ranker, obligatoire sur les doublons post-refonte [[cannibalisation]]
- Aucune action si Google affiche volontairement plusieurs URL du même site sur la requête [[cannibalisation]]

## Lancer le diagnostic avec Qadence

- La capacité seo-cannibalisation repère les requêtes où l'URL servie change et désigne la page à consolider [[cannibalisation]]
- Le rapport distingue le vrai conflit du faux positif triade SERP [[cannibalisation]]
- Le choix de la page canonique reste à toi

→ **Voir quelle page Google sert sur chaque requête** sur qadence.io/app
