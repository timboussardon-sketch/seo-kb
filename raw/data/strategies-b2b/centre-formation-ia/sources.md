---
secteur: centre-formation-ia
scope: national
date_creation: 2026-05-15
auteur: Timothée Boussardon (Organikk)
statut: collecte en cours
modele_applique: modele-strategie-b2b
regle: aucun chiffre injecté dans la stratégie sans ligne sourcée ici
---

# Sources canoniques · centre de formation spécialisé IA (national)

Aucune donnée chiffrée n'apparaît dans la stratégie tant qu'elle n'est pas rattachée à une ligne de ce fichier avec URL, date d'extraction, et fichier brut local.

## Codes NAF concernés

- 85.59A · Formation continue d'adultes (cœur de cible)
- 85.59B · Autres enseignements (formations courtes non diplômantes)
- 62.02A · Conseil en systèmes et logiciels informatiques (volet conseil IA opérationnel pour entreprises)

## Sources institutionnelles formation professionnelle

| Source | URL canonique | Donnée recherchée | Statut |
|---|---|---|---|
| France Compétences (autorité publique) | https://www.francecompetences.fr | RNCP, RS, Qualiopi, financement par certification | Référence permanente |
| Mon Compte Formation (CPF) | https://www.moncompteformation.gouv.fr | Solde CPF moyen, top formations financées, volumes annuels | À extraire |
| DARES (statistiques publiques) | https://dares.travail-emploi.gouv.fr | Statistiques formation professionnelle continue France | À extraire |
| INSEE base SIRENE | https://avis-situation-sirene.insee.fr | Nombre d'organismes NAF 85.59A en activité | À extraire |
| France Travail (ex-Pôle Emploi) | https://www.francetravail.fr | Volume formation demandeurs d'emploi, AIF | À consulter |
| Centre Inffo | https://www.centre-inffo.fr | Observatoire et veille de la formation professionnelle | À consulter publications |
| Carif-Oref (réseau régional) | https://www.reseau-carif-oref.org | Données régionales offre de formation et financement | À consulter |
| Qualiopi (certification) | https://travail-emploi.gouv.fr/qualiopi | Critères de certification qualité des organismes | Référence permanente |

## Sources spécifiques marché IA

| Source | URL | Donnée | Statut |
|---|---|---|---|
| Numeum (ex-Syntec Numérique) | https://numeum.fr | Panorama secteur tech France, emploi IA | À consulter |
| LaborIA (Institut Pasteur + INRIA + Ministère du Travail) | https://www.laboria.ai | Étude impact IA sur le travail et la formation | À consulter |
| Pix (compétences numériques) | https://pix.fr | Baromètre compétences numériques France | À consulter |
| BPI France études tech | https://www.bpifrance.fr | Études adoption IA dans les PME et ETI | À consulter |
| Conseil national du numérique | https://cnnumerique.fr | Rapports adoption numérique entreprises | À consulter |
| Anthropic / OpenAI rapports usage | https://www.anthropic.com | Statistiques usage ChatGPT et Claude entreprise | À consulter |

## OPCO et financement (pour cocon transparence financement)

| Source | URL | Donnée | Statut |
|---|---|---|---|
| OPCO Atlas (services financiers) | https://www.opco-atlas.fr | Financements formations tech secteur tertiaire | À consulter |
| OPCO Akto (services intellectuels) | https://www.akto.fr | Financements formations conseil ingénierie | À consulter |
| OPCO 2i (industrie) | https://www.opco2i.fr | Financements formations PME industrielles | À consulter |
| OPCO Mobilités (transport logistique) | https://www.opcomobilites.fr | Financements formations logistique | À consulter |

## Comparateurs et plateformes (à ne pas linker, juste connaître)

| Source | URL | Usage |
|---|---|---|
| Moncompteformation.gouv.fr (référence officielle) | https://www.moncompteformation.gouv.fr | Plateforme de référence CPF, OBLIGATOIRE pour fiche organisme |
| Topformation | https://www.topformation.fr | Comparateur privé (à éviter en backlink mais à monitorer) |
| Diplomeo | https://diplomeo.com | Idem |
| Maformation | https://maformation.fr | Idem |
| Comparis Formation | https://comparis.fr | Idem |

## Data terrain à collecter côté centre client

Aucune publication sans au moins une de ces sources renseignées :

- Nombre de préinscriptions et d'inscrits sur 24 mois glissants
- Taux de complétion par programme
- Taux d'insertion ou de mise en application post-formation
- Témoignages apprenants vidéo et écrits (avec accord daté)
- Études de cas clients entreprises (DRH, manager, CEO) avec ROI mesuré
- Mix B2C / B2B / financement CPF / financement OPCO / financement entreprise
- Certifications obtenues (Qualiopi, RNCP, RS, ISO si applicable)
- Logos clients entreprises (avec autorisation écrite)
- Avis Google et Trustpilot agrégés

## Sources à exclure formellement

- Aucun scraping de site concurrent organisme de formation IA
- Aucune donnée reprise depuis blog SEO formation sans remontée à la source primaire
- Aucun chiffre repris d'une étude payante sans accès au rapport intégral
- Aucune mention nominative d'un concurrent organisme de formation dans le contenu publié (on parle "le marché", "les acteurs du secteur")

## Variables à renseigner dans la stratégie

- `[NB-ORGANISMES-NAF-8559A-FRANCE]` · source INSEE SIRENE
- `[VOLUME-CPF-ANNUEL]` · source Mon Compte Formation
- `[NB-CERTIFICATIONS-IA-RNCP]` · source France Compétences
- `[SOLDE-CPF-MOYEN]` · source Mon Compte Formation ou DARES
- `[CROISSANCE-FORMATION-IA-MARCHE]` · source Numeum ou BPI France
- `[NB-INSCRITS-CENTRE]` · data terrain client
- `[TAUX-COMPLETION-MOYEN]` · data terrain client
- `[TAUX-INSERTION-POST-FORMATION]` · data terrain client
- `[ROI-MOYEN-MESURE-CLIENT]` · data terrain client études de cas
