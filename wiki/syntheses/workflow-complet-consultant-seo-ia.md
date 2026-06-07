---
type: synthesis
title: Workflow complet du consultant SEO IA — De la prospection à la livraison
aliases: [workflow-consultant-seo-ia, pipeline-consultant]
tags: [synthese, workflow, consultant, freelance, claude-cowork, prospection, livraison]
created: 2026-04-12
updated: 2026-04-12
sources: 6
confidence: high
status: stable
---

# Workflow complet du consultant SEO IA

**Troisième synthèse** de cette KB. Pipeline intégral du consultant SEO IA, de la prospection à la livraison récurrente. Croise le workflow de rédaction de Tim (raw/notes/tim-workflow-redaction.md), les 10 skills propriétaires, les insights des calls prospects, et la doctrine post-SGE. `confidence: high` — appliqué par Tim avec résultats documentés.

---

## Pipeline en 9 étapes

### 1. Prospection

**Outil :** Claude Cowork + scraping
**Process :**
- Scraper des sites par secteur/critères (ex : sites de jouets, artisans Paris)
- Évaluer automatiquement la qualité SEO (H1, meta, vitesse, contenu)
- Scorer le potentiel (note Claude) → filtrer les prospects pertinents
- Générer un email de prospection personnalisé basé sur les faiblesses identifiées

**Résultat :** Liste qualifiée de prospects avec email prêt à envoyer. Cf. call 9 (Julien) : Tim décrit un participant avancé qui automatise ce process.

### 2. Call découverte

**Outil :** Claude Cowork (préparation) + enregistrement du call
**Process :**
- Avant le call : mini-audit du site prospect (scraping HTML, positions estimées)
- Pendant le call : montrer les mots-clés business identifiés (volume, CPC, roadmap)
- Ne PAS dire "visibilité". Dire "mots-clés business", "conversion", "leads qualifiés"
- Donner la transparence : voici exactement ce que je vais faire

**Résultat :** Closing 10% → 50%. Le prospect comprend la valeur concrète. Cf. [[syntheses/vendre-seo-ia-2026]].

### 3. Audit SEO

**Outil :** Claude Cowork + MCP (Search Console si accès client) + scraping
**Process :**
- Scraper les URLs du site (HTML, H1, H2, meta, vitesse)
- Analyser la Search Console (positions, clics, impressions, CTR)
- Identifier les quick-wins (positions 4-15, CTR faible) → cf. skill-quick-win
- Détecter la cannibalisation → cf. skill-cannibalisation
- Évaluer le maillage interne → cf. skill-maillage-interne
- Produire un rapport structuré avec priorités

**Résultat :** Audit actionnable en 10-15 minutes (vs. plusieurs heures avant). Cf. call 5 (Dev web).

### 4. Recherche mots-clés

**Outil :** Claude Cowork + Fusionn + Grok (fact-checking)
**Process :**
- Identifier les mots-clés transactionnels / actionnels (pas informationnels)
- Trouver les mots-clés **non cités sur les LLM mais cliqués** par les utilisateurs
- Mapper les entités vectorielles (relations sémantiques Roi-Reine) → cf. skill-entites-vectorielles
- Créer les clusters AEO (MECE, 3 types d'intention) → cf. skill-cluster-aeo

**Résultat :** Liste de 30-40 mots-clés business priorisés, avec mapping sémantique.

### 5. Brief de contenu

**Outil :** Claude Cowork
**Process :**
- Structurer les H2 comme vecteurs sémantiques distincts (Passage Ranking)
- Au moins un H2 doit créer un Surprise Gap
- Intégrer les sources de data propriétaire identifiées
- Définir le format (article, page service, landing, outil interactif)

Cf. skill-brief-contenu, [[concepts/passage-ranking]], [[concepts/surprise-gap]].

### 6. Rédaction

**Outil :** Claude Cowork + Grok (fact-checking) + data client
**Process :**
- 80% consensus IA (ce que tout le monde dit sur le sujet)
- 20% data propriétaire unique :
  - Calls clients enregistrés → ton de voix, jargon
  - Avis clients → formulations, pain points
  - Données internes → chiffres, résultats, cas d'usage
  - Études/sources exclusives
- Relecture humaine obligatoire (pas de contenu "effort-less")

**Temps :** 1h30 → 45 minutes par article (gain documenté).
Cf. skill-workflow-article, [[concepts/anti-ai-writing]], [[concepts/data-proprietaire]].

### 7. Suivi positions

**Outil :** Claude Cowork + Search Console + tracking LLM
**Process :**
- Suivi automatisé des positions Google (GSC)
- Suivi des citations LLM (ChatGPT, Perplexity, Gemini)
- Tracking des clics CTA
- Alertes sur les mouvements significatifs

### 8. Rapports clients

**Outil :** Claude Cowork (génération automatique)
**Process :**
- Claude résume tout ce qui a été fait dans la semaine
- Génère un rapport structuré avec liens vers les livrables
- Envoi par email → remplace les calls de suivi hebdomadaires
- Le client reçoit de la valeur sans que le consultant perde du temps

**Résultat :** Tim ne fait plus de calls de suivi → temps réinvesti ailleurs.

### 9. Itération & capitalisation

**Outil :** Claude Cowork (système transversal)
**Process :**
- Claude analyse les patterns cross-clients (ce qui fonctionne / ne fonctionne pas)
- Création de skills personnalisés basés sur les résultats
- Chaque projet nourrit le suivant (capitalisation)
- Mise à jour du workflow : garder les 80% qui fonctionnent, faire évoluer les 20%

**Résultat :** Fin du "redémarrage perpétuel". Le consultant a un système qui s'améliore avec le temps.

---

## Métriques de performance du pipeline

| Étape | Avant workflow IA | Après workflow IA |
|-------|------------------|-------------------|
| Audit | Plusieurs heures | 10-15 minutes |
| Rédaction article | 1h30 | 45 minutes |
| Rapport client | Call 30min + rédaction | Automatique |
| Closing | 10% | 50% |
| Charge mentale | "Je recommence à chaque fois" | "Je sais exactement quoi faire de A à Z" |

---

## Pages liées

[[syntheses/doctrine-seo-post-sge]] · [[syntheses/vendre-seo-ia-2026]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/passage-ranking]] · [[concepts/aeo]] · [[concepts/workflow-redaction-8-etapes]]
