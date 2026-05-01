---
source: "https://organikk.co/blog/agent-seo-ia-simple"
slug: agent-seo-ia-simple
title: "Premier agent SEO IA : configuration et prompting, Organikk"
author: "Timothée Boussardon"
date_published: 2026-01-28
date_scraped: 2026-04-30
description: "Configurer Claude en agent SEO spécialisé plutôt qu'en outil généraliste. Une fois en place, ce setup est réplicable sur tous tes clients."
type: article-blog-organikk
---

# Premier agent SEO IA : configuration et prompting, Organikk

Remarque : Ça peut paraître complexe, mais une fois configuré, c'est **duplicable sur tous vos clients**. C'est le niveau 0 de ce qu'on pourra faire demain. Bienvenue dans la nouvelle ère du consulting SEO.

En 3 étapes :

- Configurer une fois → Project SEO + Custom Instructions
- Ajouter le contexte → Client + Data + Stratégie
- Exécuter → Prompt rapide ou complet selon le besoin

Le résultat : une liste de mots-clés pour le SEO et le GEO (Generative Engine Optimization).

## 01 ·1/ Configuration (10 minutes chrono)

### Étape 1, Créer le projet

- Aller sur claude.ai/new
- Cliquer sur "Projets" → "Créer un projet"
- Nom : Process SEO

### Étape 2, Instructions personnalisées

Dans "Connaissances du projet" → "Instructions personnalisées", coller le prompt ci-dessous.

# RÔLE Expert SEO avec 15 ans d'expérience. Spécialité : **transformer 1 mot-clé en stratégie SEO complète**. # MÉTHODOLOGIE (4 ÉTAPES) ## 1. Génération (2-3 min) 50 mots-clés : head terms, moyenne traîne, longue traîne Scoring : intention, difficulté, conversion Format : tableau Markdown ## 2. Analyse intentions (3-5 min) Catégorisation (info/nav/trans/commercial) Maturité utilisateur Format contenu optimal ## 3. Clustering (4-6 min) 3-5 pages piliers + satellites Hiérarchie sémantique, Priorisation ROI, Maillage interne ## 4. Longue traîne (3-4 min) 30 variations ultra-spécifiques Quick wins vs long terme # PRINCIPES Transactionnel > Informationnel Spécificité > Volume Micro-niches (3+ contraintes) ROI d'abord # WORKFLOW 1. Demander contexte (URL, secteur, zone, cibles) 2. Demander mots-clés déjà traités 3. Demander mot-clé principal 4. Exécuter les 4 étapes 5. Livrer plan 6 mois # RÈGLES Jamais de mots-clés génériques Jamais de doublons Toujours identifier Quick Wins (score 9-10)

## 02 ·2/ Contexte client

### Étape 3, Template contexte client

Créer ce fichier Markdown pour chaque client et l'ajouter au projet.

## CONTEXTE CLIENT **Business :**

- URL :
- Secteur :
- Zone géo :
- Cibles :
- Objectif :
**Mots-clés traités :**[liste ou "Aucun"]**Mot-clé principal :**[votre mot-clé]

### Étape 4, Documents à ajouter dans le projet

- Contexte client rempli
- Votre ton de voix
- Stratégie SEO (dataset)
- Instructions personnalisées (étape 2)
- Fichier avec tous vos contenus SEO existants
- Export Google Search Console (fichier Excel)
- Briefs des meilleurs mots-clés

Pour scraper le contenu de votre site : scraper.bolt.host (outil gratuit).

## 03 ·3/ Prompting

### Audit SEO & GEO sous 48h.

30 min en visio. Je reviens avec une analyse de vos opportunités réelles.

[Réserver 30 min →](https://cal.com/tim-boussardon-yzrrb1/30min)

Avant de lancer : bien ajouter tous les documents de contexte et personnaliser le prompt avec votre requête cible.

Le prompt ci-dessous est conçu pour du **reverse engineering sémantique**, générer des micro-intentions pour **maximiser le Score [[rrf]]** et **atteindre le niveau [[fully-meets]]** sur des requêtes commerciales et procédurales.

### Sous-thème 1, Choix / Comparaison (MOFU)

L'objectif est d'aider à la décision, positionner l'offre et générer des leads qualifiés. Ce sous-thème couvre les intentions de recherche secondaires à dimension commerciale : prix, critères de sélection, comparaisons, garanties, preuves sociales.

Micro-intention, Type, Rôle HM/FM, Hook SEO

prix freelance seo selon expérience, Commercial, FM → Budget transparent, Grille Tarifaire 2026

freelance vs agence avantages, Commercial, FM → Aide décision, Matrice Complète

garantie résultats seo possible, Transactionnel, FM → Réduction risque, Paiement Performance ?

### Le prompt complet

<role> Expert en reverse engineering sémantique. Vous générez des micro-intentions pour maximiser le score RRF et atteindre Fully Meets (FM) sur les requêtes commerciales et procédurales. </role> <context> Requête : {{VOTRE_REQUÊTE}} Phase : MOFU/BOFU (Commercial + Procédural) Objectif : Aide décision, génération leads, conversion </context> <task> Génère 2 sous-thèmes avec 8-10 micro-intentions chacun : SOUS-THÈME 2 : CHOIX/COMPARAISON (Commercial

- MOFU) Pour chacune : 1. Requête exacte (4-10 mots) 2. Type : Commercial / Transactionnel / Informationnel 3. Rôle HM/FM 4. Hook SEO (4-6 mots) </task> <constraints>
- Requêtes naturelles utilisateur (pas académiques)
- Longue traîne 4-10 mots
- 8-10 micro-intentions minimum par sous-thème
- Formats multimodaux (pas que texte) </constraints> Lance pour : {{VOTRE_REQUÊTE}}

Ce système s'appuie sur la **logique du cocon vectoriel** : chaque micro-intention est un satellite qui renforce l'autorité sémantique de la page pilier. Un bon [[grounding-score]] sur chaque segment permet d'être recruté comme source par les moteurs génératifs.

Une fois configuré, cet agent est duplicable sur tous les clients. La logique reste la même : contexte → clustering → micro-intentions → contenu avec **topical authority maximale**.

### Ma stratégie SEO du moment

### Ma roadmap SEO 2026 en 6 étapes

### Mon process complet pour trouver les meilleurs mots-clés SEO en 2026

## FAQ

Un bot répond à une instruction, une à la fois. Un agent enchaîne des actions : il lit ton brief, va chercher de la data, structure le clustering, produit les micro-intentions, sort un livrable. L'agent décide d'un parcours, le bot exécute une commande. Concrètement, l'agent demande des skills configurés et des permissions outils (lecture de fichiers, navigation, écriture). Le bot se contente d'un prompt.

Un brief court mais dense : ton de marque (3 lignes), mots-clés piliers (3 à 5), sources autorisées, format de sortie attendu (markdown, longueur, structure des H2). Pas plus de 500 tokens pour le système initial, sinon l'agent perd de la liberté de raisonnement. Le reste, c'est dans les skills qui se chargent à la demande.

Un par client. Chaque client a sa data, sa voix, ses contraintes sectorielles, ses interdits. Un agent générique produit du contenu générique. C'est précisément ce qu'on veut éviter en 2026. Une fois le premier agent cadré, dupliquer prend 30 minutes : tu copies le dossier de skills, tu remplaces les fichiers de contexte spécifiques. Le coût de duplication est marginal.

3 à 4 pour démarrer : recherche (collecte de data), brief (structuration), rédaction (premier jet), fact-check (vérification des claims). Avec ça, l'agent boucle la production d'un article complet. Tu enrichis ensuite au besoin : skills d'audit, de génération de méta-data, de maillage interne, de relecture éditoriale. Mais 4 skills bien faits valent mieux que 12 skills bricolés.

Oui, c'est tout l'intérêt. La logique de l'agent reste la même : contexte, clustering, micro-intentions, contenu avec topical authority. Seuls changent la data ingérée et les contraintes éditoriales. Une fois ton template d'agent stabilisé après 2 ou 3 clients, tu déploies en moins d'une heure. C'est ce qui rend le système scalable sans embaucher.

---

**Connecté avec :** [[rrf]] · [[fully-meets]] · [[grounding-score]]
