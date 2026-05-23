---
type: modele-strategie
slug: modele-strategie
title: Modèle · Stratégie SEO par secteur
auteur: Timothée Boussardon
sources:
  - "[[strategie-seo-serrurier-lyon]]"
  - "[[strategie-seo-agence-immobiliere-lyon]]"
  - "[[strategie-seo-paysagiste-paris]]"
  - "[[strategie-seo-avocat-paris]]"
  - "[[strategie-seo-hotel-paris]]"
date: 2026-05-15
pattern: "[[modele-mots-clés]]"
tags:
  - modele
  - strategie
  - seo-local
  - reproduction
  - anti-hallucination
related:
  - "[[modele-strategie-b2b]]"
  - "[[modele-mots-clés]]"
  - "[[strategie-seo-serrurier-lyon]]"
  - "[[strategie-seo-agence-immobiliere-lyon]]"
  - "[[strategie-seo-paysagiste-paris]]"
  - "[[strategie-seo-avocat-paris]]"
  - "[[strategie-seo-hotel-paris]]"
  - "[[skill-programmatique-pseo]]"
  - "[[skill-entites-vectorielles]]"
  - "[[skill-product-led-seo]]"
---

# Stratégie SEO pour [SECTEUR] à [VILLE]

Modèle fusionné depuis cinq applications publiées (serrurier Lyon, agence immobilière Lyon, paysagiste Paris, avocat Paris, hôtel Paris). Mêmes os, mêmes phrases-clés, contenus adaptables par secteur. À dupliquer puis à calibrer. Mise à jour 2026-05-15 : ajout de la méta-section discipline data anti-hallucination, du 4ème pattern de thèse (captation directe vs dépendance plateforme), de la variable marché atypique géographique, et de la variable contraintes réglementaires sectorielles.

**Variables à substituer dans tout le doc** : `[SECTEUR]` (métier ou produit), `[VILLE]` (zone géographique), `[INTENTION-DOMINANTE]` (urgence transactionnelle, décision long cycle, etc.), `[OUTIL-PRINCIPAL]` (simulateur de coût, estimateur de prix, calculateur, comparateur), `[DURÉE-ROADMAP]` (9 à 12 mois selon cycle d'achat), `[CONTRAINTES-REGLEMENTAIRES]` (déontologie ordre professionnel, RGPD santé, AMF finance, RIN avocat, à vérifier en amont et valider avant publication si applicable).

---

## Discipline data et anti-hallucination (méta-section obligatoire)

Aucune stratégie n'est publiée tant que la discipline suivante n'a pas été respectée. C'est ce qui sépare un modèle scalable d'un modèle qui hallucine et plante un Core Update.

### Étape 1 · Créer le sources.md avant la rédaction

Pour chaque application `[SECTEUR] + [VILLE]`, créer un fichier `raw/data/strategies-[VILLE]/[secteur]/sources.md` qui liste :

- Codes NAF concernés (vérifiables INSEE, stables et publics)
- URLs canoniques des sources institutionnelles (INSEE, fédérations sectorielles, observatoires publics, organismes ville-spécifiques)
- Liste des variables `[NOM-VARIABLE]` à remplir, avec source attendue pour chaque
- Liste des sources à exclure formellement (aucun scraping concurrent, aucune statistique reprise sans remontée à la source primaire)

### Étape 2 · Règle absolue de rédaction

Aucun chiffre n'apparaît dans la stratégie tant qu'il n'est pas rattaché à une ligne du sources.md avec URL canonique, date d'extraction, et contexte exact (année de référence, périmètre géographique, source citée). Si la donnée n'est pas disponible ou pas accessible, le placeholder reste explicite (`[NOM-VARIABLE]`) avec mention de la source à consulter, et la stratégie n'est pas publiée tant que le placeholder n'est pas levé ou explicitement annoté.

### Étape 3 · Pipeline de collecte hiérarchisé

Niveau 1, sources publiques structurées avec endpoint stable (INSEE SIRENE, INSEE ESANE, data.gouv.fr, observatoires publics, COG, base DVF). Téléchargement CSV ou API officielle, jamais de scraping HTML qui peut changer.

Niveau 2, sources publiques semi-structurées (rapports PDF de fédérations sectorielles, communiqués INSEE). Extraction manuelle avec citation URL + page.

Niveau 3, data terrain du client (volumes traités, paniers moyens, délais réels observés, photos datées, témoignages vérifiés). C'est ce qui fait la différence entre une page générique et une page qui ranke. C'est le client qui la fournit.

### Étape 4 · Fact-check avant publication

Chaque chiffre a une URL source consultable au jour de publication. Chaque nom propre cité existe vraiment (vérification WebFetch). Chaque prix moyen est daté à moins de 12 mois. Aucune affirmation "selon une étude" sans étude nommée. Si un point passe pas, on retire la phrase, on ne brode pas pour combler.

### Étape 5 · Sources à exclure formellement

Pas de Semrush, pas d'Ahrefs, pas de crawl des sites concurrents pour piquer des chiffres. La data sectorielle vient des sources officielles, la data terrain vient du client. Quand on cite "les concurrents pratiquent l'opacité tarifaire", c'est une thèse stratégique, pas un chiffre vérifiable, donc pas de risque d'hallucination chiffrée.

---

## Thèse centrale (à adapter selon le secteur)

**À l'ère du GEO, les stratégies SEO génériques ne suffisent plus pour se différencier et amener un trafic qualifié sur ses pages. Seules les pages ultra-spécialisées par expertise rankent et se font citer par les moteurs génératifs** (ChatGPT, Perplexity, Google AI Overviews).

Pour un acteur du `[SECTEUR]` à `[VILLE]`, ça veut dire arrêter d'attaquer le mot-clé générique `[SECTEUR] [VILLE]` (inattaquable, dilué, sans signal de spécialité) et assumer un angle ultra-spécifique formulé en une phrase qui structure toute la page.

Quatre patterns observés sur les applications publiées (cas Lyon serrurier et immo, cas Paris paysagiste, avocat, hôtel) :

- Transparence comme avantage compétitif principal (secteurs où les concurrents cachent les prix)
- Transition du volume vers les micro-intentions sémantiques plus autorité ultra-niche plus outils interactifs (secteurs saturés de contenu générique)
- Média expert local plutôt que prestataire générique (secteurs où la donnée marché manque)
- Captation directe contre dépendance plateforme (secteurs intermédiés par une plateforme dominante sur la page de résultats organiques : OTA pour l'hôtellerie, annuaires sponsorisés et comparateurs juridiques pour les avocats, portails immobiliers pour l'immo, marketplaces pour la restauration et les services). Le pattern : assumer la réservation ou la prise de contact directe comme proposition de valeur explicite, avec garantie tarifaire transparente et signaux de proof qui surpassent la plateforme sur la longue traîne ultra-spécialisée que la plateforme ne ranke pas.

La stratégie priorise la génération de leads plutôt que le trafic, en visant les requêtes décisionnelles à forte intention commerciale.

Implémentation en roadmap trois phases ciblant **30 mots-clés prioritaires sur [DURÉE-ROADMAP] mois**.

---

## 01 · Vue d'ensemble de la stratégie

[Décrire en 1 paragraphe le profil de l'utilisateur cible et son intention dominante. Identifier le trou de marché concret : ce que les concurrents font mal ou ne font pas.]

Principe central : **la seule métrique qui compte est le nombre de leads collectés** (appels et emails), pas le trafic ou les impressions.

---

## 02 · Diagnostic marché et opportunités SEO

### Contexte national

[Statistiques nationales du secteur : chiffre d'affaires global, nombre d'entreprises, taille moyenne, marge sectorielle, EBITDA moyen. Sources publiques INSEE, fédérations professionnelles, études sectorielles.]

### Opportunité locale

[Spécificités de [VILLE] : position dans la hiérarchie urbaine française, contribution PIB régional, densité de la demande, état de la concurrence locale, manques observés sur les sites concurrents.]

### Proposition d'angle différenciant

[En une phrase, le positionnement différenciant. Exemple sur le cas serrurier : « transparence tarifaire publique ». Exemple sur le cas immo : « seule agence Lyon traitant le marché local comme un média expert ».]

---

## 03 · Trois facteurs de ranking Google pour 2026

Section invariante. Ces 3 facteurs s'appliquent à tous les secteurs.

### 1. Surprise · Apporter une information que les autres ne donnent pas

Google récompense les pages qui ajoutent une information neuve à la requête, pas celles qui répètent ce qu'on lit déjà partout.

Pour chaque requête cible, lister ce que les pages classées 1-10 disent et identifier ce qu'elles ne disent pas. La donnée terrain propriétaire (taux d'occupation, montants moyens observés, délais réels, fourchettes au m²) que personne ne publie est exactement ce qui ranke.

Le moat n'est ni le branding ni le territoire : c'est l'information que vous seul pouvez publier.

### 2. Densité d'information · Ne pas blablater pour rien dire

Chaque ligne apporte une information ou un chiffre. Pas de phrase de transition, pas de paraphrase, pas de "comme nous l'avons dit", pas de mise en bouche marketing.

Une bonne page tient en 1200-1500 mots avec 30-40 informations utiles, pas en 3000-4000 mots avec les mêmes informations diluées dans du remplissage. Google sait mesurer la concentration informationnelle d'un passage.

Test simple : si on retire une phrase, est-ce que la valeur informationnelle de la page baisse ? Si non, c'est du blabla. À retirer.

### 3. Utilité concrète pour le visiteur

Google fait évaluer ses résultats par des évaluateurs humains. Pour une requête transactionnelle, la page qui mérite la note maximale délivre tout de suite : `[OUTIL-PRINCIPAL]` ou fourchette de prix visible sans scroller, photos ou cas comparables, mention claire des contraintes, bouton d'appel ou de prise de rendez-vous accessible.

Les outils interactifs et les CTA transparents font mieux que les formulaires de contact cachés sans contexte.

Commun aux 3 facteurs : aucun ne récompense le volume. Tous récompensent l'information neuve, la concentration informationnelle, et l'utilité pour le visiteur.

---

## 04 · Cocon sémantique et architecture de pages

L'architecture du site suit une hiérarchie en trois niveaux. Une page mère par grand sujet (intention primaire du secteur), des pages filles qui traitent les sous-sujets précis, et des pages petites-filles pour les requêtes ultra-spécifiques (longue traîne décisionnelle).

Le maillage entre toutes ces pages se fait à la main, lien par lien, sans plugin automatique. C'est ce qui distingue un site qui ranke d'un site qui empile du contenu sans cohérence.

Concrètement, on commence par identifier 30 mots-clés cœur, on construit le cocon sémantique autour, et on publie environ 10 pages par mois.

### Cocon 1 · [INTENTION PRIMAIRE]
[Le cocon le plus transactionnel du secteur. Exemple serrurier : urgences. Exemple immo : estimation immobilière. 5 à 8 mots-clés.]

### Cocon 2 · [PROBLÈMES SPÉCIFIQUES OU DATA MARCHÉ]
[Sous-intentions concrètes : situations problème côté service, prix au m² par arrondissement côté immo. 4 à 6 mots-clés.]

### Cocon 3 · [POST-ACTE ou PRE-VENTE]
[Étapes adjacentes : post-effraction côté serrurier, vendre son bien côté immo. 4 à 6 mots-clés.]

### Cocon 4 · [TRANSPARENCE TARIFAIRE ou ACHAT PAR QUARTIER]
[Le cocon « rassurance » : prix transparents, comparatifs, alternatives. 4 à 6 mots-clés.]

### Cocon 5 · [GÉOGRAPHIE PRÉCISE ou LONGUE TRAÎNE BUDGET]
[Granularité géographique (arrondissements, quartiers) ou longue traîne IA très qualifiée (budget précis). 4 à 6 mots-clés.]

### Cocon 6 · [GUIDES ET CONFIANCE]
[Confiance, choix, comparaison agences ou prestataires, anti-arnaque, mandat exclusif. 3 à 5 mots-clés.]

---

## 05 · Ancrage local et crédibilité terrain

Un article « [SECTEUR] [VILLE arrondissement ou quartier] » ne doit pas être un « [SECTEUR] France » avec l'arrondissement rajouté. La localisation authentique exige : data terrain précise, acteurs locaux nommés, langage reflétant une expertise de quartier établie. Photos d'intervention ou de bien, témoignages avec date et zone précise, partenariats locaux affichés.

---

## 06 · Roadmap opérationnelle en trois phases

### Phase 1 (mois 0 à 3) · Bottom-funnel transactionnel + [OUTIL-PRINCIPAL]

- Déployer 10 pages par mois sur les requêtes transactionnelles et décisionnelles (cocons 1, 2, 3 prioritairement)
- Intégrer [OUTIL-PRINCIPAL] (simulateur de coût, estimateur de prix, calculateur, comparateur) sur chaque page ciblée, signal Highly Meets
- Optimiser Google Business Profile (chaque antenne avec photos, horaires, avis récents)
- Implémenter la structure H1 H2 pour le Passage Ranking : chaque H2 égale 150 à 200 mots autonomes
- Poser le maillage interne dès la semaine 1, pas après production
- Intégrer avis Google et Trustpilot directement sur la page
- Vérifier l'indexation Search Console sous 48 heures

### Phase 2 (mois 3 à 6) · Middle-funnel + transparence + longue traîne

- Analyser Search Console : pages avec forte impression et peu de clics, renforcer title et meta
- Déployer les pages tarifs ou prix avec data réelle et datée
- Créer les pages longue traîne IA très qualifiées (budget précis, situation précise)
- Exécuter le premier refresh obligatoire sur les pages data (prix, statistiques, marché)
- Ajouter des éléments E-E-A-T : cas concrets avec chiffres, délai, zone
- Lancer le cocon de granularité géographique fine (arrondissements ou quartiers)

### Phase 3 (mois 6 à [DURÉE-ROADMAP]) · Ultra-niche + autorité + backlinks naturels

- Mots-clés à très faible concurrence et intention hautement qualifiée (post-acte, longue traîne business)
- Lancer une newsletter ou un guide ressource à fort potentiel de backlinks naturels (presse locale, partenaires, médias spécialisés)
- Format : data terrain réelle + tendance + analyse expert + conseil actionnable
- Publier chaque édition de newsletter comme article du site : signal de récence + backlink potentiel
- Fidéliser le segment à plus forte valeur (vendeurs côté immo, contrats annuels côté service)
- Mesurer les recherches de marque (la hausse de « [nom marque] [VILLE] » égale signal qualité pour les LLMs)
- A/B tester les lead magnets et CTAs

---

## 07 · [OUTIL-PRINCIPAL] · Le différenciateur principal

[Décrire la mécanique du calculateur, simulateur, estimateur ou comparateur central à la stratégie.]

Mécanique type : **[VARIABLE 1] + [VARIABLE 2] = [VALEUR FOURNIE IMMÉDIATEMENT] + capture email + téléphone**.

Exemples de combinaisons à implémenter (à adapter au secteur) :
- [Cas d'usage 1] + [contexte] → estimation + capture email
- [Cas d'usage 2] + [contexte] → estimation + capture email
- [Cas d'usage 3] + [contexte] → estimation + capture email
- [Cas d'usage 4] + [contexte] → estimation + capture email
- [Cas d'usage 5] + [contexte] → estimation + capture email

Pourquoi ça fonctionne : la plupart des acteurs cachent l'information ou demandent un contact avant de fournir la valeur. L'outil casse le pattern. Il répond à la première question universelle du visiteur (combien ça coûte, combien ça vaut, lequel choisir) avant d'exiger un contact. Page « Do » classée Fully Meets par Google, lead qualifié à la sortie.

---

## 08 · Idées de mots-clés décisionnels

Un mot-clé décisionnel est une requête tapée par un visiteur prêt à passer à l'acte : il sait ce qu'il veut, il compare les options, il cherche le bon prestataire ou le bon produit. À l'opposé des requêtes d'exploration qui veulent juste comprendre un sujet.

Format de la matrice (à remplir avec les 30 mots-clés du secteur) :

```
mot-clé, intention, cocon associé, mois de production, format ou outil
```

Exemple de ligne : `serrurier urgence lyon, urgent, cocon 1, M1, simulateur`

Légende des mois :
- **M1** : impact business immédiat, à lancer Phase 1
- **M2** : mois 2 à 3 de production, Phase 1 fin et début Phase 2
- **M3** : mois 4 à 6, Phase 2 et début Phase 3

Distribution typique observée :
- 7 à 10 mots-clés en M1 (les plus transactionnels, urgents ou rentables)
- 10 à 12 mots-clés en M2 (le cœur de la matrice, intentions claires)
- 8 à 12 mots-clés en M3 (longue traîne, ultra-niche, requêtes IA)

---

## 09 · Erreurs critiques à éviter

- Cacher les chiffres (prix, data marché) pour garder les prospects : inverse l'effet Fully Meets
- Acheter des backlinks : créer du contenu si utile qu'il génère des liens naturels
- Générique « [SECTEUR] [VILLE] » sans granularité : segmenter par arrondissement, quartier, type, problème
- Audit 6 mois avant publication : publier 30 mots-clés rapidement, indexer, observer Search Console
- Zéro preuve d'expertise visible : afficher SIRET, certifications, assurance, photos terrain sur chaque page
- Formulaire contact sans contexte tarifaire : [OUTIL-PRINCIPAL] interactif avant la prise de contact
- Contenu IA générique non supervisé : filtré au Core Update, demande data terrain et angle local identifiable
- Multiplier les pages de quartier ou de catégorie génériques sans data locale
- Page speed avant contenu : 80 % contenu, 20 % technique, l'indexation bat la vitesse
- Négliger la newsletter ou le guide ressource Phase 3 : c'est le meilleur générateur de backlinks naturels

---

## 10 · Checklist de lancement semaine 1

1. Valider les 30 mots-clés prioritaires avec connaissance terrain [VILLE]
2. Construire le cocon sémantique (mère, filles, petites-filles) sur spreadsheet avant production
3. Créer ou vérifier le Google Business Profile : SIRET, certifications, photos réelles
4. Publier la première landing page sur la requête principale avec [OUTIL-PRINCIPAL] intégré
5. Intégrer avis Google et Trustpilot directement sur la page (pas en liens externes)
6. Vérifier l'indexation en Search Console sous 48 heures après publication
7. Définir le planning de publication : 10 pages par mois avec assignations de mots-clés
8. Écrire la page mère cocon avec structure Passage Ranking : chaque H2 égale réponse autonome 150 à 200 mots
9. [Élément de conversion principal mobile : numéro de téléphone épinglé en header, ou CTA outil interactif visible above the fold]
10. Configurer le tracking des conversions réelles (clics CTA, durée d'engagement, sortie email)

---

## 11 · FAQ stratégique

Cinq questions canoniques observées sur les deux applications publiées. À adapter au secteur tout en gardant la structure.

### Pourquoi [OUTIL-PRINCIPAL] sur ce type de site ?

[Réponse type : c'est une page « Do » actionnelle, format que Google classe Fully Meets dans ses Quality Rater Guidelines. L'utilisateur ne veut pas lire un article, il veut [LA VALEUR FOURNIE] immédiate. L'outil capte l'intention, donne une réponse utile, déclenche l'appel ou l'email. C'est aussi la meilleure défense contre les concurrents qui pratiquent l'opacité.]

### Combien de temps avant les premiers appels ou leads entrants ?

[Réponse type : 2 à 3 mois sur le local pack si Google Business Profile complet. 4 à 6 mois sur le SEO classique pour accrocher les premières positions. La fiche locale ramène avant le site. L'engagement total se mesure sur 6 à 12 mois.]

### Faut-il vraiment des backlinks locaux pour ranker à [VILLE] ?

[Réponse type : oui mais pas n'importe lesquels. Pas les annuaires DA80 génériques. Ce qui compte : la presse locale, les sites des mairies, les partenaires métiers, les associations. Un backlink local pertinent vaut dix backlinks génériques sur des annuaires obsolètes.]

### 30 mots-clés c'est suffisant pour couvrir [VILLE] ?

[Réponse type : largement suffisant. La matrice de combinaisons (intention, granularité géographique, situation) couvre les vrais cas d'usage qui génèrent des appels. Au-delà, on dilue l'autorité sur des requêtes à très faible volume. Mieux vaut 30 pages qui rankent que 200 qui plafonnent.]

### Comment se différencier des [acteurs dominants ou problématiques de la page de résultats organiques] ?

[Réponse type : trois leviers concrets. Transparence sur la donnée que les concurrents cachent (prix, méthode, équipe). [OUTIL-PRINCIPAL] qui donne la valeur avant la prise de contact. Témoignages vérifiés avec preuves (date, zone, type de prestation). Les pages « prix » et « avis vérifiés » rassurent. C'est ce qui transforme une page de résultats organiques polluée en avantage.]

---

## 12 · À retenir

La stratégie priorise la précision sur le volume, les micro-intentions sémantiques sur les mots-clés génériques, et l'utilité réelle sur la chasse aux liens. Implémentation sur [DURÉE-ROADMAP] mois en 3 phases, avec insistance sur signaux de fraîcheur, optimisation Passage Ranking et marqueurs E-E-A-T spécifiques au marché de [SECTEUR] à [VILLE].

---

## Notes pour adapter le template à un nouveau secteur

Cinq éléments varient systématiquement d'une application à l'autre. Le reste est invariant.

**Variable 1 · La durée de roadmap.** 9 mois pour les secteurs à cycle d'achat court et intention transactionnelle dominante (urgence, dépannage, services réactifs). 12 mois pour les secteurs à cycle long et décision réfléchie (immobilier, conseil B2B, formation, équipement durable, aménagement haute valeur, contentieux civil).

**Variable 2 · L'outil Product-Led principal.** Toujours présent, mais sa nature change. Simulateur de coût pour les services avec variables de tarification (urgence, type de prestation, week-end). Estimateur de prix ou d'indemnisation pour les actifs ou dossiers à valeur unitaire variable (immobilier, véhicules, préjudice corporel). Calculateur de capacité, de rendement ou de cotisation pour les produits financiers, investissements et recours (AT-MP côté employeur). Moteur de devis direct pour les services intermédiés par plateforme (hôtellerie, restauration, services à domicile). Comparateur ou quiz pour les choix multi-critères.

**Variable 3 · Les 6 cocons sémantiques.** La structure en 6 cocons est invariante, mais le contenu de chaque cocon dépend du secteur. Globalement : un cocon « intention primaire transactionnelle », un cocon « problèmes ou situations spécifiques », un cocon « adjacent à l'acte principal », un cocon « transparence tarifaire ou data marché », un cocon « granularité géographique ou longue traîne business », un cocon « confiance et choix éclairé ».

**Variable 4 · Le marché atypique géographique.** Question préalable à toute application : est-ce que `[SECTEUR]` dans `[VILLE]` correspond au marché national ou crée un sous-marché atypique qu'il faut redéfinir avant de rédiger ? Exemples observés. Paysagiste France égale jardins privés ; paysagiste Paris égale terrasses, balcons, copropriétés, toitures bureaux (pas de jardins privés en intra-muros). Hôtel France égale tourisme de loisir dominant ; hôtel Paris égale marché ultra-saturé OTA avec basculement massif vers le milieu de gamme et le luxe depuis 2009. Si la combinaison crée un sous-marché atypique, la thèse centrale, les cocons sémantiques et la matrice 30 mots-clés doivent refléter ce sous-marché et non pas le secteur national.

**Variable 5 · Les contraintes réglementaires sectorielles.** Question préalable à investiguer : `[SECTEUR]` est-il encadré par une déontologie d'ordre professionnel, une réglementation publicitaire stricte, ou un cadre de protection des données sensibles ? Exemples observés. Avocat : RIN articles 6 information, 10 publicité, 11 confraternité, validation cabinet obligatoire avant publication. Santé : RGPD données de santé, encadrement publicité médicale, ordre des médecins. Finance : AMF démarchage, conseil en investissement. Architecte : ordre des architectes. Si applicable, ajouter un volet "validation réglementaire obligatoire avant publication" en checklist semaine 1, et adapter le ton du contenu (pas de promesse de résultat pour les professions encadrées). Si non applicable, ignorer cette variable.

Tout le reste (les 3 facteurs de ranking, l'ancrage local, la roadmap 3 phases, le format de matrice 30 mots-clés, la checklist semaine 1, la structure FAQ, et surtout la discipline data anti-hallucination en méta-section) est repris pixel-perfect d'une application à l'autre.

---

## Sources et liens

- Application 1 : [[strategie-seo-serrurier-lyon]] (publié 2026-01-12, pattern transparence tarifaire)
- Application 2 : [[strategie-seo-agence-immobiliere-lyon]] (publié 2026-01-08, pattern média expert local)
- Application 3 : [[strategie-seo-paysagiste-paris]] (publié 2026-05-15, pattern marché atypique géographique sous-marché terrasse-balcon-copropriété)
- Application 4 : [[strategie-seo-avocat-paris]] (publié 2026-05-15, pattern autorité ultra-niche par spécialité, contraintes RIN)
- Application 5 : [[strategie-seo-hotel-paris]] (publié 2026-05-15, pattern captation directe vs dépendance plateforme OTA)
- Pattern global : [[modele-mots-clés]]
- Skills mobilisés : [[skill-programmatique-pseo]], [[skill-entites-vectorielles]], [[skill-product-led-seo]], [[skill-cluster-aeo]], [[ton-de-voix-tim]]
- Concepts liés : [[e-e-a-t]], [[fully-meets]], [[passage-ranking]], [[product-led-seo]], [[anti-ai-writing]], [[data-proprietaire]]
