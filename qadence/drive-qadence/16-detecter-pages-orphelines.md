---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: comment détecter les pages orphelines de mon site
intention: Do
capacite_qadence: maillage-interne-gsc
schema: HowTo + Article
created: 2026-07-13
sources_vault: [[maillage-interne]], [[maillage-systeme]]
---

# Comment détecter les pages orphelines de votre site

Une page orpheline est une page qui ne reçoit aucun lien interne entrant ; on la repère en croisant l'architecture éditoriale (piliers, hubs, satellites) avec les impressions et positions réelles de la Search Console.

## Ce qu'est une page orpheline

- Une page orpheline ne reçoit aucun lien interne entrant [[maillage-systeme]]
- Le maillage interne hiérarchise les pages (mère, fille, petite-fille) et guide l'exploration [[maillage-interne]]
- Sans lien entrant, une page reste hors du réseau qui distribue l'autorité [[maillage-interne]]
- La page dead-end est le cas miroir : elle ne renvoie vers rien [[maillage-systeme]]

## Détecter par l'architecture éditoriale

- Classer les articles en piliers (3 à 5), chaque pilier avec un hub et ses satellites [[maillage-systeme]]
- Un satellite sans lien depuis son hub ni ses voisins de pilier est orphelin [[maillage-systeme]]
- La détection est possible dès le cadrage, avant toute donnée comportementale [[maillage-systeme]]
- Repère : chaque page devrait viser au moins trois liens entrants depuis trois articles existants [[maillage-systeme]]

## Détecter par la donnée Search Console

- Croiser impressions et positions réelles repère les pages sous-maillées et orphelines [[maillage-interne]]
- Une page qui a des impressions mais aucun lien entrant est une orpheline qui performe déjà [[maillage-interne]]
- Un maillage corrigé fait remonter ces pages sans créer de contenu [[maillage-interne]]
- La donnée GSC vient après l'architecture, pour prioriser les corrections [[maillage-systeme]]

## Lancer le diagnostic avec Qadence

- Qadence lit votre Search Console et repère les pages qui ont des impressions sans maillage entrant [[maillage-interne]]
- La sortie distingue orphelines réelles et pages simplement sous-maillées, chacune avec son action [[maillage-systeme]]
- Le tri suit l'ordre architecture d'abord, donnée comportementale ensuite [[maillage-systeme]]

→ **Détecter mes pages orphelines** sur qadence.io/app
