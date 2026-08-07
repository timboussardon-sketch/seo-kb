---
title: Modèle pSEO — Corpus & directories Ideelab autour de "idée business"
date: 2026-08-07
type: pseo-strategy
site: ideelab.co
---

# Corpus & directories — Ideelab

Suite à [[recherche-2026-08-07-ideelab-idee-business]]. Doctrine appliquée : [[feedback_corpus_avant_pages]] (le corpus sert d'abord le produit, la page est le sous-produit) et [[feedback_directories_data_ia]] (combler un manque de matière, pas empiler des mots-clés).

Décidé par Tim le 2026-08-07 : construire les deux axes groundés en parallèle (digital + secteur), abandonner l'axe budget (aucune donnée réelle derrière), jamais de vocabulaire « concurrent »/« concurrence » ([[feedback_pas_de_mot_concurrent]]).

## Axe 1 — Digital (App Store + GitHub)

**Statut produit** : corpus live aujourd'hui sur `ideelab.co` (home = `searchQuickSources`, score de saturation log-scale LIBRE/À CREUSER/SATURÉ). Double emploi déjà vérifié : le corpus sert le produit ET peut servir la page sans travail supplémentaire.

**Dataset (variable), proposition de curation à valider par Tim** :
productivité, finance personnelle, santé et fitness, éducation/e-learning, réseaux sociaux, e-commerce, IA/outils IA, jeux mobiles, outils développeur, no-code/low-code, RH/recrutement, immobilier, voyage, livraison/logistique, rencontre, musique, podcast, cuisine/recettes, bien-être/méditation, gestion de projet, CRM/vente, marketing digital, comptabilité/facturation, legaltech, assurance/insurtech, sport, animaux de compagnie, parentalité/enfants, mode/beauté, gestion locative, freelance/indépendants, prise de rendez-vous, prise de notes, traduction/langues, mobilité/covoiturage.

**Template de page** : « Idée d'application [catégorie] : [N] apps déjà sur l'App Store, [N] projets sur GitHub — [statut LIBRE/À CREUSER/SATURÉ] ». Donnée = même calcul que le produit (`src/lib/score.ts`), jamais un chiffre réinventé pour la page.

Requêtes :
- idée d'application [catégorie]
- idée d'app [catégorie] pas encore faite
- application [catégorie] qui n'existe pas encore
- projet open source [catégorie] idée
- idée de SaaS [catégorie]
- outil [catégorie] qui manque
- application [catégorie] originale à créer
- idée d'app mobile [catégorie] 2026
- comment savoir si une application [catégorie] existe déjà
- combien d'applications [catégorie] sont déjà publiées
- combien de projets [catégorie] existent déjà sur GitHub
- idée de produit digital [catégorie]

## Axe 2 — Secteur (registre France, NAF + CA)

**Statut produit** : corpus réel et fonctionnel (`recherche-entreprises.api.gouv.fr`, zéro clé, testé), mais plus affiché sur la home depuis la refonte UI du 2026-08-07 (réaffichage encore à décider par Tim). Construit en parallèle sur décision de Tim — le double emploi produit sera complet une fois le réaffichage tranché, pas bloquant pour sortir les pages.

**Dataset (variable), proposition de curation à valider par Tim** :
restauration, boulangerie-pâtisserie, coiffure, esthétique/institut de beauté, bâtiment/travaux, plomberie, électricité, e-commerce, conciergerie, coaching sportif, coaching professionnel/formation, services à la personne, garde d'enfants, garde d'animaux/toilettage, agence immobilière, VTC/transport de personnes, livraison/coursier, événementiel, réparation (auto, électroménager, informatique), nettoyage/pressing, fleuriste, photographe, traiteur, salle de sport, crèche privée, auto-école, déménagement, jardinage/paysagisme, location de matériel, food truck. Pas les ~732 codes NAF bruts — une sélection mappée sur des idées business réellement tapées, chaque libellé à faire correspondre à son/ses codes NAF avant industrialisation.

**Template de page** : « Idée business dans [secteur] : [N] entreprises actives en France, CA moyen [X]€ » — donnée directe de l'API (`activite_principale` + `etat_administratif=A` + `finances.ca`), plafonnée "10 000+" au-delà de la limite Elasticsearch, jamais arrondie au hasard.

Requêtes :
- idée business [secteur]
- ouvrir un/une [secteur]
- créer une entreprise de [secteur]
- combien d'entreprises de [secteur] en France
- [secteur] : combien d'entreprises actives
- CA moyen d'une entreprise de [secteur]
- taille du marché [secteur] France
- idée business [secteur] rentable
- code NAF [secteur]
- statistiques entreprises [secteur] France
- idée business [secteur] à [ville]
- ouvrir un/une [secteur] à [ville]

**Croisement secteur × ville** : possible techniquement (`siege.libelle_commune` dans l'API), mais pas de génération combinatoire aveugle. À tester sur un échantillon restreint (grandes villes × secteurs à fort volume déclaratif) avant industrialisation, pour éviter des pages vides ou à trafic nul.

## Axe Product Hunt — écarté

Pas seulement une question de corpus pour cette liste : l'API v2 Product Hunt n'a aucun champ de recherche texte libre (vérifié par introspection GraphQL, filtre uniquement featured/topic/date/url). Impossible de chercher une idée dessus, donc écarté aussi bien côté produit que côté pages. À réévaluer si l'API change.

## Axe budget — abandonné

Décidé le 2026-08-07 : pas de champ capital/investissement dans l'API registre, pas de donnée réelle pour grounder cet axe. Pas de page dessus.

## Étape suivante

- `seo-clustering-mots-cles` sur les deux listes de requêtes pour figer le découpage 1 page = 1 template.
- Décider avec Tim de la sélection finale des catégories (axe 1) et secteurs (axe 2) — curation humaine, pas de liste exhaustive automatique.
- Réafficher le corpus secteur côté produit (tab « entreprises » ou « Statistique idée » évoqué dans [[project_ideelab]]) pour fermer la boucle double emploi.
