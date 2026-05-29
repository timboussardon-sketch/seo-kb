---
type: prompt
source_type: doc-interne
title: "Prompt pSEO — Sites Non-Produit (Média, Éditorial, Communautaire)"
aliases: ["prompt pSEO média", "prompt pSEO éditorial", "prompt programmatique non-produit"]
tags: ["prompt", "pseo", "programmatique-seo", "product-led-seo", "template", "scalable", "media", "editorial"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["doctrine-tim"]
confidence: haute
status: actif
usage: "Sites média, blogs, annuaires, communautés, comparateurs — sans offre produit/service directe"
---

# Prompt pSEO — Sites Non-Produit (Média, Éditorial, Communautaire)

## Quand utiliser ce prompt

Sites **sans offre produit/service directe** : médias, blogs d'autorité, annuaires, comparateurs indépendants, communautés, bases de données publiques. Le modèle de revenu est publicitaire, affiliation, ou notoriété.

Différence clé avec [[prompt-pseo-produit-service]] : ce prompt intègre l'**Étape 0 — Test de Substitution LLM** obligatoire avant tout développement de modèle. Chaque page doit justifier son existence face à ChatGPT.

## Le prompt complet

```
<role>
Tu es un stratège en Programmatic SEO et Growth Engineering.
Tu conçois des systèmes de contenu scalables qui transforment des bases de données en machines à trafic organique.
Tu raisonnes comme un ingénieur produit (data → template → pages) ET comme un SEO senior (intent → SERP → conversion).
</role>

<context>
- URL : [URL DU SITE]
- Description : [DESCRIPTION EN 3-5 PHRASES : ce que fait l'entreprise, pour qui, quelle offre principale, quel positionnement, quelle preuve sociale (avis, certifications, résultats)]

## DONNÉES DISPONIBLES EN BASE
Liste ici TOUTES les données structurées que le site possède déjà ou peut générer. C'est le carburant du programmatique — sans données, pas de pages scalables.
  • [DATASET 1 — ex: base de 50 articles de blog couvrant X, Y, Z]
  • [DATASET 2 — ex: liste de 200 produits avec caractéristiques]
  • [DATASET 3 — ex: base de clients/cas d'étude par secteur]
  • [DATASET 4 — ex: FAQ exhaustive sur le sujet principal]
  • [DATASET 5 — ex: données réglementaires, listes officielles, annuaires]
  • [DATASET 6 — ex: données sectorielles, statistiques marché]
  • [DATASET 7 — ex: clusters sémantiques déjà identifiés]
  • [...]

## URL / PAGES EXISTANTES
  • [URL PAGE PILIER 1] — [description courte]
  • [URL PAGE PILIER 2] — [description courte]
  • [URL PAGE SERVICE 1] — [description courte]
  • [URL HUB CONTENU / BLOG] — [description courte]
  • [...]
  • Structure blog : [PATTERN D'URL DU BLOG — ex: site.com/blog/[categorie]/[article]]

## CONCURRENTS DIRECTS
  • [CONCURRENT 1 — nom + positionnement en 1 phrase]
  • [CONCURRENT 2]
  • [CONCURRENT 3]
  • [CONCURRENT 4]
  • [...]

## OBJECTIF BUSINESS
- Objectif primaire : [CE QUE LE SITE VEUT GÉNÉRER — ex: leads qualifiés, ventes e-commerce, inscriptions, demandes de devis]
- Objectif secondaire : [OBJECTIF SECONDAIRE — ex: notoriété, vente d'un produit complémentaire]
- Cible principale : [PERSONA #1 — qui est-il, quel est son problème, où en est-il dans son parcours]
- Cible secondaire : [PERSONA #2 — si pertinent]
</context>

<task>
Conçois une stratégie de contenu programmatique SEO complète pour [URL DU SITE].

Le principe : identifier des modèles de pages où UN SEUL TEMPLATE + UNE VARIABLE QUI CHANGE = des centaines/milliers de pages uniques qui rankent chacune sur un mot-clé longue traîne.

Pour chaque modèle de contenu, tu dois :

### ÉTAPE 0 — TEST DE SUBSTITUTION LLM (OBLIGATOIRE, À FAIRE EN PREMIER)

Avant de valider UN SEUL modèle, applique ce test à chaque idée :

**Le Test ChatGPT en 3 questions :**

1. "Est-ce qu'un utilisateur peut obtenir un résultat ÉQUIVALENT en tapant un prompt sur ChatGPT/Claude/Gemini ?" → Si OUI → ÉLIMINÉ.
2. "Est-ce que la page propose un OUTIL INTERACTIF, une DATA VISUALISATION, un COMPARATIF STRUCTURÉ ou une FONCTIONNALITÉ EMBARQUÉE qu'un LLM textuel ne peut pas reproduire ?" → Si NON → ÉLIMINÉ.
3. "Est-ce que la page a une raison d'EXISTER dans un navigateur plutôt que dans un chat IA ?" → Si NON → ÉLIMINÉ.

**Ce qui PASSE le test (exemples) :**
- Calculateurs interactifs avec inputs personnalisés
- Comparateurs côte à côte avec données temps réel
- Data visualisations (graphes, timelines, cartes, tableaux croisés)
- Outils fonctionnels embarqués (le produit LUI-MÊME dans la page)
- Agrégateurs de données multi-sources avec filtres
- Templates/générateurs téléchargeables
- Simulateurs avec variables ajustables

**Ce qui NE PASSE PAS le test (exemples) :**
- Listes "Top X de [catégorie]" → ChatGPT fait mieux
- Résumés / Explications de concepts → ChatGPT fait mieux
- Questions/Réponses textuelles → ChatGPT fait mieux
- "Que dit [source] sur [thème]" → ChatGPT fait mieux
- Guides étape par étape en texte pur → ChatGPT fait mieux
- Biographies / Fiches descriptives → ChatGPT fait mieux
- Définitions / Glossaires textuels → ChatGPT fait mieux

Présente les résultats du test dans un tableau AVANT de développer les modèles :

| Idée de modèle | Test ChatGPT Q1 | Test Q2 (interactif ?) | Test Q3 (raison navigateur ?) | Verdict |

### ÉTAPE 1 — IDENTIFIER LES MODÈLES SCALABLES (minimum 5)

Ne retenir QUE les modèles qui ont passé l'Étape 0.

Pour chaque modèle, détaille :

**A) Architecture**
- Nom du modèle
- Pattern d'URL : [site.com]/[prefixe]/[variable]
- Head term (partie fixe) + Modificateur (variable qui change)
- Nombre de pages possibles (estimation réaliste)
- Source de données : quelle table/API/dataset alimente la variable

**B) Template de page (structure exacte)**
- H1 : formule avec variable
- OUTIL/COMPOSANT INTERACTIF CENTRAL : description précise de l'élément interactif qui justifie l'existence de la page (tableau comparatif, calculateur, graphe, widget, générateur, etc.)
- Section par section : ce que contient chaque bloc (avec nombre de mots indicatif)
- Données affichées vs données cachées (teaser → conversion)
- CTA spécifique et sa position
- Schema.org recommandé (Article, FAQPage, Product, HowTo, Course, LocalBusiness, SoftwareApplication, Dataset, etc.)

**C) SEO & Intent**
- Phase du funnel : TOFU / MOFU / BOFU
- Type d'intention : Informationnelle / Commerciale / Transactionnelle / Navigationnelle
- 10 exemples de requêtes exactes que ces pages cibleront
- Compétition estimée (faible/moyenne/forte) avec justification
- Potentiel de Featured Snippet ou AI Overview : oui/non et pourquoi
- Score de substitution LLM : pourquoi cette page résiste à ChatGPT (1-2 phrases)

**D) Avantage compétitif**
- Pourquoi ces pages sont IMPOSSIBLES à reproduire par un LLM généraliste
- Pourquoi ces pages sont IMPOSSIBLES à copier par un concurrent
- Quelle donnée propriétaire ou composant interactif rend chaque page unique

### ÉTAPE 2 — MATRICE DE PRIORISATION

Classe les modèles dans un tableau avec ces critères :

| Modèle | Pages possibles | Effort par page | Impact SEO | Potentiel conversion | Données déjà dispo ? | Moat vs LLM | PRIORITÉ |

### ÉTAPE 3 — MOTS-CLÉS PAR MODÈLE

Pour chaque modèle, génère un tableau de 10-15 mots-clés longue traîne :

| Requête | Intention | Phase funnel | Compétition estimée |

### ÉTAPE 4 — PLAN D'EXÉCUTION 90 JOURS

- Semaine par semaine : quel modèle lancer, combien de pages, quelles actions techniques.
- Prérequis techniques pour chaque modèle (SSR, sitemap dynamique, schema markup, composants interactifs, imports de données, etc.)

### ÉTAPE 5 — RÉSUMÉ EXÉCUTIF

- En 5 phrases : pourquoi cette stratégie va fonctionner pour [URL DU SITE]
- Le modèle #1 à lancer en premier et pourquoi.
</task>

<rules>
## RÈGLES NON-NÉGOCIABLES — À respecter pour CHAQUE page produite

### RÈGLE 0 — Anti-substitution LLM (LA PLUS IMPORTANTE)
Chaque page pSEO DOIT contenir au moins UN élément interactif ou data-driven qu'un utilisateur ne peut PAS obtenir en tapant un prompt sur ChatGPT, Claude, Gemini ou tout autre LLM généraliste. Si la valeur de la page peut être intégralement reproduite par un prompt textuel → la page n'a pas de raison d'exister et ne doit PAS être produite.

Les formes acceptables de moat anti-LLM sont :
- Outil interactif : calculateur, simulateur, générateur avec inputs utilisateur
- Data visualisation : graphes, timelines, cartes, tableaux croisés dynamiques
- Comparatif structuré : tableaux multi-colonnes avec données vérifiées et mises à jour
- Produit embarqué : le service/outil du site fonctionnel directement dans la page
- Données propriétaires agrégées : données que le LLM n'a pas (logs utilisateurs, données terrain, stats d'usage)
- Fonctionnalité de persistance : sauvegarde, tracking, progression, personnalisation
- Contenu multimodal non-textuel : images interactives, vidéos, audio, 3D

### RÈGLE 1 — Contenu unique obligatoire (anti-thin content)
Chaque variable change non seulement le H1 mais aussi le CONTENU RÉEL de chaque section. Le template définit la STRUCTURE, jamais le texte. Si deux pages d'un même modèle partagent plus de 30% de texte identique, c'est un échec. Chaque section doit être rédigée spécifiquement pour la variable concernée.

### RÈGLE 2 — Données terrain, zéro hallucination
Chaque page est enrichie par les données propriétaires et retours terrain du client (cas réels, erreurs fréquentes, astuces concrètes). Ce n'est PAS du texte généré automatiquement à partir d'une base de données. Aucun chiffre, aucune statistique, aucun pourcentage ne doit être inventé ou "halluciné". Si une donnée n'est pas vérifiable, elle n'apparaît pas.

### RÈGLE 3 — Sourcing obligatoire des données marché et chiffres
Toute donnée chiffrée (taille de marché, taux de croissance, statistiques sectorielles, etc.) DOIT provenir d'une source d'autorité vérifiable et datée de moins de 3 ans.

Protocole à respecter pour chaque chiffre publié :
1. Citer la source entre parenthèses : (Source : [Organisme], [Rapport/Étude], [Année])
2. Indiquer l'année de la donnée
3. Si aucune source fiable n'existe → NE PAS inventer de chiffre. Remplacer par une formulation qualitative ("marché en croissance", "forte demande") ou par le placeholder [DONNÉE À SOURCER — vérifier sur [source recommandée]] pour signaler qu'un chiffre doit être recherché manuellement avant publication.

INTERDIT : arrondir "à la louche", extrapoler un chiffre national vers un sous-segment, ou citer une source sans l'avoir vérifiée.

### RÈGLE 4 — Canonical propre et zéro doublon technique
Chaque page a sa balise canonical qui pointe vers elle-même. Aucun paramètre d'URL, aucune variation (filtres, tri, pagination) ne doit créer de pages dupliquées. Une URL = un contenu = une canonical.

### RÈGLE 5 — Maillage interne différenciant
Chaque page pointe vers un ensemble DIFFÉRENT de pages internes. Le graphe de liens est unique par page. Aucune page ne doit avoir exactement le même bloc de liens internes qu'une autre. Détaille pour chaque modèle la logique de maillage spécifique.

### RÈGLE 6 — Surprise Score : chaque passage doit apporter de l'information inédite
Les architectures LLM (Titans/MIRAS) utilisent un "gradient de surprise" pour décider quoi mémoriser. Un contenu prévisible = oublié. Un contenu avec données nouvelles, angle contrarien, expertise unique = mémorisé.

Application :
- Chaque section DOIT contenir au moins 1 élément "High Surprise" : donnée propriétaire, angle contrarien, insight absent du web.
- Informations High Surprise placées au DÉBUT et à la FIN de chaque section (effet primauté/récence).
- Si une section n'apporte rien de nouveau vs les 10 premiers résultats Google → la réécrire ou la supprimer.
- Structure de mémoire associative : chaque paragraphe rappelle le précédent (faible surprise contextuelle) mais ajoute une info nouvelle (haute surprise informationnelle).

### RÈGLE 7 — Grounding Score : structurer pour le Passage Ranking et l'AI Overview
Google fonctionne en Triade SERP : Document Ranking → Passage Ranking → Passage Generation. Si aucun passage n'est assez dense pour être extrait, tu es classé mais invisible dans les réponses IA.

Application :
- Chaque page DOIT contenir 1 "passage ancré" de 150-200 mots : densité sémantique maximale, réponse directe extractible en Featured Snippet ou AI Overview.
- Réponse directe en 2-3 phrases AVANT de développer. Format : [Réponse] → [Développement] → [Preuve/Source].
- Chaque page doit inclure 1 "bloc d'authorship algorithmique" (~50 mots) répondant à 100% de la micro-intention cible, conçu pour extraction en Position 0.
- Couvrir la requête principale + 2-3 micro-intentions proches dans des passages distincts pour maximiser le score RRF sur le cluster sémantique.
</rules>

<constraints>
- EXCLUSIONS : [LISTE DES AXES À NE PAS TRAITER — ex: "Ne propose AUCUN modèle basé sur la localisation géographique" ou "Ne propose aucun modèle basé sur X, déjà couvert"]
- ANTI-CANNIBALISATION : Ne propose JAMAIS deux modèles qui ciblent la même personne avec des variables similaires. Si deux modèles se recoupent, fusionne-les en un seul modèle complet. Un modèle = un angle unique.
- ANTI-SUBSTITUTION LLM : Ne propose JAMAIS un modèle dont la valeur peut être intégralement reproduite par un prompt ChatGPT/Claude/Gemini. Chaque modèle DOIT avoir un composant interactif ou data-driven non-reproductible par un LLM textuel.
- CIBLE : [DESCRIPTION PRÉCISE DE LA CIBLE — qui elle est, qui elle n'est PAS. Ex: "La cible est le dirigeant de PME, PAS le particulier"]
- Chaque modèle DOIT être alimenté par des données que le site possède déjà ou peut générer automatiquement.
- Priorise les modèles où la compétition est FAIBLE et les données sont PROPRIÉTAIRES.
- Chaque page doit avoir un CTA clair vers l'une des offres du site.
- Pense mobile-first et maillage interne vers les pages piliers existantes.
- Le ton doit être [DESCRIPTION DU TON — ex: "expert mais accessible", "technique et précis", "chaleureux et rassurant"].
</constraints>

<output_format>
Structure ta réponse exactement comme suit :

# [URL DU SITE] — Stratégie Programmatique SEO

## Test de Substitution LLM (Étape 0)
[Tableau de validation de chaque idée AVANT développement]

## Le Principe (3 lignes max)

## Modèle 1 : [Nom]
### Architecture / Composant Interactif Central / Template / SEO & Intent / Avantage compétitif vs LLM
[...jusqu'à Modèle 5 minimum]

## Matrice de Priorisation (avec colonne "Moat vs LLM")
## Mots-clés Prioritaires par Modèle
## Plan d'Exécution 90 Jours
## Métriques de Succès
## Résumé Exécutif
</output_format>
```

## Différences avec le prompt Produit/Service

| Aspect | [[prompt-pseo-produit-service]] | Ce prompt (Non-Produit) |
|---|---|---|
| Étape 0 — Test LLM | Absente | **Obligatoire** avant tout modèle |
| Règle 0 — Anti-substitution | Absente | **Règle #1** non-négociable |
| Composant interactif | Recommandé | **Obligatoire** pour chaque modèle |
| Colonne "Moat vs LLM" | Non | Oui dans la matrice de priorisation |
| Score de substitution | Non | Oui dans la section SEO & Intent |
| Exemples pass/fail | Non | Oui (7 exemples qui passent, 7 qui échouent) |

## Pourquoi 2 prompts séparés

Un site produit/service a un **moat naturel** : ses données propriétaires (prix, stock, clients). Le test LLM est moins critique car le produit lui-même est la valeur.

Un site non-produit n'a **aucun moat naturel** : tout son contenu textuel est reproductible par un LLM. Le test de substitution est donc **vital** — sans composant interactif ou données temps réel, la page n'a aucune raison d'exister face à ChatGPT.

## Concepts liés

[[programmatique-pseo]] · [[product-led-seo]] · [[fully-meets]] · [[grounding-score]] · [[surprise-gap]] · [[agentic-search]] · [[entites-vectorielles]] · [[skill-maillage-interne]] · [[skill-cannibalisation]]

## Skills mobilisés

[[skill-programmatique-pseo]] · [[skill-product-led-seo]] · [[skill-entites-vectorielles]] · [[skill-cluster-aeo]]

## Stratégies liées

[[strat-victoria-garden-pseo]] · [[prompt-pseo-produit-service]]
