---
type: source
source_type: note
title: "Guide de 0 à 1 : les skills SEO d'Organikk et ce qu'on peut faire avec"
created: 2026-06-10
updated: 2026-06-10
tags: [guide, skills, seo, geo, pseo, content-brain, onboarding, methode]
sources: 0
confidence: high
status: draft
---

# De 0 à 1 : le système SEO d'Organikk

> Le guide complet de nos skills et de ce qu'on peut faire en SEO avec. On part d'un site qui n'a rien, on arrive à un système qui produit du lead en autonomie. Chaque étape liste les skills à dégainer et comment ils s'enchaînent.

## En résumé

Un projet SEO chez nous suit un parcours en 7 phases : cadrage → mots-clés → architecture → production → technique → maillage → suivi, avec une couche GEO qui traverse tout. À chaque phase correspondent des skills précis. La règle au-dessus de tout : on ne fait pas de la visibilité, on fait de la conversion. On vise le lead, pas le trafic. Et chaque page se construit sur la data propriétaire du client, jamais sur un prompt générique.

## La philosophie avant les outils

Quatre principes qui décident de tout ce qui suit :

1. **Conversion, pas visibilité.** 90 à 95 % des visites n'achètent pas tout de suite. L'objectif d'une page, c'est de récupérer un e-mail qualifié, pas de monter dans une position moyenne.
2. **Décisionnel et transactionnel.** L'informationnel se fait manger par les LLM. On va chercher les requêtes Do, celles qu'on tape en situation de décision.
3. **Originalité, pas copie.** On donne l'information que les autres ne donnent pas. C'est ce que Google et les moteurs IA veulent servir.
4. **80/20.** L'IA fait 80 % du travail. On facture les 20 % qui font ranker : la stratégie, la data propriétaire, le jugement.

Tout le reste, ce sont des skills qui exécutent cette doctrine.

---

# Le parcours de 0 à 1

## Phase 0 : cadrage

Avant tout skill, on cadre. La money page, le point de conversion, la data disponible (calls commerciaux, tickets SAV, CRM, avis), le secteur. Sans data exploitable en entrée, le système ne tourne pas : c'est le pré-requis non négociable.

## Phase 1 : les mots-clés business

L'objectif : passer d'une thématique floue à une liste de requêtes qualifiées, triées par potentiel de conversion.

- **`seo-recherche-mots-cles`** : from scratch, d'une thématique à une liste exhaustive (intention, volume, difficulté). La première brique.
- **`seo-clustering-mots-cles`** : regroupe la liste brute en clusters par partage de SERP. 1 cluster = 1 page. Évite la cannibalisation dès la conception.
- **`seo-mots-cles-decisionnels`** : isole les requêtes qui convertissent (bas de funnel, transactionnel) et écarte l'informationnel qui ne fait que du trafic.

Ce que tu peux faire : sortir, pour un nouveau client, une carte complète de ses requêtes business priorisées en une session.

## Phase 2 : l'architecture de contenu

On passe des mots-clés à une structure de pages qui tient debout.

- **`seo-cluster-aeo`** : construit le cocon sémantique optimisé pour les moteurs de réponse (framework Know-Simple / Know / Do). Pilier + satellites.
- **`seo-modeles-pseo`** : conçoit les modèles de pages décisionnelles autour d'une money page (scoring Proximité × Intention × Faisabilité).
- **`seo-programmatique-pseo`** : 1 template + 1 variable = des centaines de pages longue traîne, sans thin content.
- **`seo-roadmap-pseo`** : séquence tout ça en plan d'exécution.

Ce que tu peux faire : transformer un catalogue ou une offre en architecture de plusieurs centaines de pages, chacune calée sur une requête réelle.

## Phase 3 : le brief et la sémantique

Avant de rédiger, on prépare le terrain sémantique pour ranker mathématiquement.

- **`seo-brief-contenu`** : brief éditorial avec structure Hn optimisée Passage Ranking, basé sur ce que les concurrents n'ont pas dit.
- **`seo-entites-vectorielles`** : la cartographie des entités à inclure pour aligner la page sur l'intention (Grounding Score, gap concurrentiel).
- **`seo-preparation-semantique`** : la préparation amont du terrain sémantique.
- **`seo-peurs-objections`** : les freins psychologiques de l'audience, pour le contenu à haute conversion et les verbatims Haute Surprise.

Ce que tu peux faire : donner à la rédaction une cible précise, pas un sujet vague. Tu sais exactement quels termes, quelles objections, quels angles mettre.

## Phase 4 : la production

On rédige, dans la voix du client, avec un contrôle qualité dur.

- **`ton-de-voix-tim`** : applique une voix anti-IA-writing stricte (paramétrable par client via le corpus de voix).
- **`seo-workflow-article`** : les 8 étapes de rédaction (Surprise Gap, Ancrage, Données, Inversions, Architecture, Rédaction, FAQ, Compilation).
- **`article-engine-pipeline`** : le bout en bout, avec décodage RRF en amont et checklist de fact-check en aval.
- **`content-brain`** : enveloppe le pipeline dans une boucle qui apprend d'une page à l'autre, logge les claims, pose des prédictions J+30/J+90, et bloque la publi si la quality gate n'est pas passée.
- **`seo-product-led-seo`** : conçoit les outils interactifs (calculateurs, simulateurs) qui décrochent la note Fully Meets sur les requêtes Do.

Ce que tu peux faire : produire du contenu qui parle comme les acheteurs du client, sort des faits que personne d'autre n'a, et s'améliore à chaque page.

## Phase 5 : la technique

Pour que tout ce contenu soit indexable et citable.

- **`seo-donnees-structurees`** : JSON-LD automatique (graphe d'entité site-wide + schémas par page) sur Next.js App Router.
- **`seo-core-web-vitals`** : audit LCP / CLS / TBT mobile-first, plan de correction priorisé.
- **`indexation-check`** : audit d'indexation sans outil payant (statut HTTP, blocages, sitemap, maillage entrant, statut Google estimé).

Ce que tu peux faire : t'assurer que les pages produites sont vues, comprises et servies, pas perdues.

## Phase 6 : le maillage et la cannibalisation

On relie les pages entre elles et on règle les conflits.

- **`maillage-systeme`** : architecture en piliers, hub / satellite, choix d'ancres, détection des pages orphelines et dead-end, sans dépendre de la GSC.
- **`maillage-interne-gsc`** : le maillage piloté par la data Search Console (hiérarchie mère / fille / petite-fille, règles Know→Do).
- **`seo-cannibalisation`** : repère les pages qui se battent sur la même intention et tranche (301, fusion, différenciation, ou rien si Triade SERP).

Ce que tu peux faire : faire circuler le jus de lien et empêcher tes propres pages de se plomber entre elles, à l'échelle de milliers d'URLs.

## Phase 7 : le suivi et l'apprentissage

Le contenu publié revient mesuré, sinon « data propriétaire » reste un argument et pas un fait.

- **`seo-quick-win`** : repère les opportunités GSC (pages position 3-12, CTR faible) qui rapportent vite.
- **Les boucles GSC** : traitement des exports Search Console et fiches preuves reliant chaque contenu à l'hypothèse qu'il teste, mesurées à J+30 et J+90.

Ce que tu peux faire : savoir ce qui convertit vraiment, réécrire les CTA qui sous-performent, et nourrir le système avec du réel.

---

# La couche GEO (traverse tout)

Le moteur n'est plus Google seul. ChatGPT, Perplexity, les AI Overviews. Une bonne stratégie travaille tous ces moteurs avec la même base de contenu.

- **`seo-geo-audit`** : note un texte sur 7 scores algorithmiques (Surprise, Grounding, Content Effort, Alignement RRF, RAG Structurer, Freshness Guard, Action Engine) pour garantir la citation par les moteurs génératifs.
- **`seo-cluster-aeo`** : l'architecture pensée pour les moteurs de réponse, pas seulement pour les liens bleus.

Ce que tu peux faire : vérifier qu'un contenu survivra aux filtres IA et sera cité, pas juste indexé.

---

# La mémoire du système

- **`kb-semantic-search`** : recherche sémantique sur toute la base de connaissances (doctrine, cas, concepts). C'est ce qui rend le système cumulatif : chaque mission enrichit ce qu'on installe à la suivante.

## Et la confidentialité de la data ?

Le système se nourrit de data client (calls, mails, tickets SAV), donc la question est légitime. Trois points qui la règlent :

1. **Sur un compte pro (API, Team, Enterprise), Anthropic n'entraîne jamais ses modèles sur vos données.** C'est le défaut des conditions commerciales, rien à configurer. Sur un compte perso (Free, Pro, Max), il faut désactiver le réglage « Help improve Claude » dans claude.ai → Settings → Privacy, sinon les sessions servent à l'entraînement et sont conservées 5 ans (30 jours une fois désactivé).
2. **Le RGPD est un sujet distinct de l'entraînement.** Pour la data client : informer les participants quand un call est enregistré, et passer par un compte pro, qui ouvre droit au contrat de sous-traitance d'Anthropic (le DPA).
3. **Le brut reste en local.** La base de connaissances vit dans des fichiers sur votre machine, pas dans un outil cloud. On n'envoie à l'API que ce qui sert au traitement en cours, anonymisé quand c'est possible.

---

# Les workflows types (comment on enchaîne)

**Nouveau client, de zéro :**
`seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-decisionnels` → `seo-cluster-aeo` / `seo-modeles-pseo` → `seo-brief-contenu` → `article-engine-pipeline` (dans `content-brain`) → `seo-donnees-structurees` → `maillage-systeme` → suivi GSC.

**Money page + pages satellites (décisionnel) :**
`seo-modeles-pseo` → `seo-mots-cles-decisionnels` → `seo-brief-contenu` + `seo-peurs-objections` → production → `seo-product-led-seo` pour l'outil de capture.

**Site existant qui stagne :**
`indexation-check` → `seo-cannibalisation` → `maillage-interne-gsc` → `seo-quick-win` → réécriture ciblée.

**Vérifier qu'un contenu sera cité par l'IA :**
`seo-geo-audit` → corrections → `seo-entites-vectorielles` pour combler le gap.

---

# Le tableau récap

| Phase | Skills | Ce que tu fais |
|---|---|---|
| Mots-clés | recherche, clustering, decisionnels | Carte des requêtes business priorisées |
| Architecture | cluster-aeo, modeles-pseo, programmatique-pseo, roadmap-pseo | Structure de pages à l'échelle |
| Brief | brief-contenu, entites-vectorielles, preparation-semantique, peurs-objections | Cible sémantique précise |
| Production | workflow-article, article-engine-pipeline, content-brain, ton-de-voix, product-led-seo | Contenu original dans la voix du client |
| Technique | donnees-structurees, core-web-vitals, indexation-check | Pages vues et comprises |
| Maillage | maillage-systeme, maillage-interne-gsc, cannibalisation | Jus de lien qui circule, zéro conflit |
| Suivi | quick-win, boucles GSC | Mesure réelle, apprentissage |
| GEO | geo-audit, cluster-aeo | Citation par les moteurs IA |
| Mémoire | kb-semantic-search | Système cumulatif |

---

# Le passage à 1 : l'autonomie

Le but n'est pas de rester indispensable. À la fin, le client (ou le freelance qu'on équipe) pilote le système lui-même : les skills tournent dans sa voix, sur sa data, avec ses boucles de suivi. On a installé une machine, pas livré un bouquet de Google Docs. C'est ça, le 1.
