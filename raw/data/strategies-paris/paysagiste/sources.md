---
secteur: paysagiste
ville: Paris
date_creation: 2026-05-15
auteur: Timothée Boussardon (Organikk)
statut: collecte en cours
regle: aucun chiffre injecté dans strategie-seo-paysagiste-paris.md sans ligne sourcée ici
---

# Sources canoniques · paysagiste Paris

Aucune donnée chiffrée n'apparaît dans la stratégie tant qu'elle n'est pas rattachée à une ligne de ce fichier avec URL, date d'extraction, et fichier brut local.

## Codes NAF concernés

- 81.30Z · Services d'aménagement paysager (cœur de cible : conception, création, entretien d'espaces verts)
- 71.11Z · Activités d'architecture (architectes-paysagistes diplômés ENSP / ESAJ)
- 01.30Z · Reproduction de plantes (pour les volets pépinière interne et fourniture végétale)

## INSEE et data publique

| Source | URL canonique | Donnée recherchée | Statut |
|---|---|---|---|
| INSEE base SIRENE | https://avis-situation-sirene.insee.fr | Nombre d'entreprises NAF 81.30Z sur Paris (75) et Île-de-France (11) | À extraire |
| INSEE ESANE | https://www.insee.fr/fr/statistiques/serie/010565692 | Chiffre d'affaires sectoriel NAF 81.30Z | À extraire |
| INSEE démographie entreprises | https://www.insee.fr/fr/statistiques | Créations / défaillances annuelles secteur paysage | À extraire |
| data.gouv.fr | https://www.data.gouv.fr | Base SIRENE complète téléchargeable au format CSV | À télécharger |
| Apur Atelier Parisien d'Urbanisme | https://www.apur.org | Surface d'espaces verts Paris, plan biodiversité Ville de Paris | À consulter |
| Paris Open Data | https://opendata.paris.fr | Inventaire arbres remarquables, espaces verts publics par arrondissement | À télécharger CSV |

## Fédérations et observatoires sectoriels

| Organisme | URL | Donnée | Statut |
|---|---|---|---|
| UNEP Union Nationale des Entreprises du Paysage | https://www.unep.fr | Chiffres clés annuels filière paysage (CA, effectifs, marges, croissance) | À consulter rapport annuel |
| VAL'HOR interprofession horticole | https://www.valhor.fr | Observatoire des données économiques de la filière | À consulter publications |
| FNTP Fédération Nationale des Travaux Publics | https://www.fntp.fr | Index BT, indices conjoncturels | À consulter |
| Plante & Cité | https://www.plante-et-cite.fr | Études techniques végétalisation urbaine | À consulter |

## Sources Paris-spécifiques

| Source | URL | Donnée | Statut |
|---|---|---|---|
| Ville de Paris Direction des Espaces Verts | https://www.paris.fr/pages/des-espaces-verts-toujours-plus-nombreux-3681 | Politique végétalisation, permis de végétaliser | À consulter |
| Plan Biodiversité Paris 2030 | https://www.paris.fr | Objectifs chiffrés végétalisation, toitures, façades | À extraire |
| Préfecture de Paris registre copropriétés | Registre national copropriétés ANAH | Volume copropriétés avec espaces communs par arrondissement | À consulter |

## Data terrain à collecter côté client

Aucune publication sans au moins une de ces sources renseignées :

- Volume de devis terrasse / balcon / copropriété traités sur 12 mois glissants
- Panier moyen par typologie (terrasse 20 m², balcon 8 m², copropriété 200 m², bureau 500 m²)
- Délais de réalisation moyens par typologie
- Photos avant/après datées et géolocalisées (arrondissement précis)
- Témoignages clients vérifiés avec consentement écrit
- Liste des partenaires locaux nommés (syndics, architectes, paysagistes pépiniéristes Île-de-France)

## Sources à exclure formellement

- Aucun scraping de site concurrent paysagiste Paris
- Aucune statistique reprise depuis blogs sectoriels sans remontée à la source primaire
- Aucun chiffre repris d'une étude payante sans accès au rapport intégral

## Chiffres extraits le 2026-05-15

### UNEP · Chiffres clés filière paysage 2024

Source : https://www.lesentreprisesdupaysage.fr/etudes-chiffres-cles/chiffres-cles-du-paysage/
Extraction : 2026-05-15

- Chiffre d'affaires sectoriel France 2024 : 8,5 milliards d'euros (croissance +60 % depuis 2014)
- Nombre d'entreprises France : 33 550
- Effectifs : 140 300 actifs dont 112 400 salariés
- Structure : 61,5 % d'entreprises sans salariés, 23,5 % de 1 à 5 salariés, 15 % de plus de 5 salariés (ces 15 % réalisent 76 % du chiffre d'affaires)
- Répartition clientèle : particuliers 49 %, entreprises privées 25,5 %, marchés publics 24,5 %
- Investissement 2024 : 640 millions d'euros (70 % des entreprises ont investi, soit 7,5 % du chiffre d'affaires)

## Variables encore à renseigner

- `[NB-ENTREPRISES-NAF-8130Z-PARIS]` · source INSEE SIRENE, requête NAF 81.30Z + département 75 à faire
- `[PART-PARIS-ESPACES-VERTS]` · source Apur ou Paris Open Data, fichier CSV à télécharger
- `[NB-COPROPRIETES-PARIS-AVEC-ESPACES-COMMUNS]` · source registre national copropriétés ANAH
- `[PRIX-MOYEN-AMENAGEMENT-TERRASSE-M2]` · data terrain client, non extractible publiquement
- `[DUREE-MOYENNE-CHANTIER-TERRASSE]` · data terrain client, non extractible publiquement

## Variables remplies

- `[CA-FILIERE-PAYSAGE-FRANCE]` égale 8,5 milliards d'euros 2024 source UNEP
- `[NB-ENTREPRISES-NAF-8130Z-FRANCE]` égale 33 550 entreprises source UNEP
