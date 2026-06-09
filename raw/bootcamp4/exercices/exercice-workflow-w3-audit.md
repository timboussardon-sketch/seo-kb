---
title: "Exercice capstone — Workflow 3 : auditer un site"
bootcamp: 4
type: exercice-capstone
session: 3
workflow: audit-8-phases
cowork: partiel
duree: "3h30 à 5h"
created: 2026-06-09
related:
  - "[[workflow-audit-bootcamp4]]"
---

# Exercice capstone — Workflow 3 : auditer un site

**Niveau** : intermédiaire · **Durée** : 3h30 à 5h (étalable) · **Pré-requis** : skills `indexation-check`, `seo-quick-win`, `seo-cannibalisation`, `maillage-systeme`, `maillage-interne-gsc`, `audit-engine-pipeline` installés. Un accès GSC + le sitemap.xml de ton client. (`seo-core-web-vitals` en plus si tu es sur terminal.)

## Le cas

Ton client te demande « pourquoi mon SEO stagne ? ». Tu vas répondre avec un audit complet, 100% data Google, sans aucun outil payant. Le but n'est pas un PDF de 40 pages : c'est un plan d'action priorisé en 3 horizons que le client peut suivre.

## Ce que tu dois faire

**1. Réunis tes 3 entrées.**
- Export GSC (Requêtes + Pages, 6 mois, CSV).
- L'URL du `sitemap.xml` de ton client.
- L'adresse du site (pour le crawl des liens et la structure Hn).

**2. Lance l'orchestrateur.**
Dans Claude, dépose tes fichiers et colle :

```text
Lance audit-engine-pipeline sur ce site. Voici l'export GSC et le sitemap.
Déroule les phases dans l'ordre et arrête-toi après chaque phase pour me montrer
le livrable avant de passer à la suivante.
```

**3. Déroule les 8 phases** (détail dans [[workflow-audit-bootcamp4]]) : positionnement → indexation → Core Web Vitals → quick wins → structure Hn → cannibalisation → maillage → synthèse. Chaque phase nourrit la suivante. Si tu es sur Cowork sans terminal, la phase Core Web Vitals sera sautée : prends un PageSpeed Insights public en complément.

**4. Produis le rapport final** (phase 6) : la synthèse en 3 horizons, anomalies critiques en tête.

## Ce que tu dois obtenir   ← le « screen »

Le rapport final ressemble à ça (exemple sur un site fictif) :

```
AUDIT SEO — exemple-saas.fr — synthèse

Anomalies critiques (à traiter d'abord)
- 3 pages business en noindex accidentel (depuis la refonte de mars)
- /tarifs/ absente du sitemap

Horizon 1 — Semaines 1-2 (quick wins)
- Réécrire les title des 5 pages position 3-12 sous-cliquées → +1 800 clics estimés
- Corriger les 3 noindex → réindexation

Horizon 2 — Mois 1 (fondations)
- Résoudre 4 cannibalisations (2 fusions, 2 différenciations)
- Reconstruire le maillage : 6 pages orphelines à relier

Horizon 3 — Mois 2-3 (croissance)
- Cluster décisionnel sur [thème business]
- Modèle pSEO sur [variable]
```

## Vérifier que tu as réussi

- [ ] Les anomalies critiques sont en tête, pas noyées en ligne 47.
- [ ] Chaque reco quick win a un impact chiffré en clics (pas « améliorer le SEO »).
- [ ] Le plan est en 3 horizons, priorisé par impact, pas une liste à plat.
- [ ] Tu distingues « non indexée » et « non testable » (rate-limit Google), tu ne confonds pas les deux.
- [ ] Le rapport tient en une synthèse lisible par un dirigeant, pas un dump technique.

## Le piège

Vouloir tout corriger en même temps. Un audit qui sort 60 actions sans ordre est inutilisable. La valeur est dans la **priorisation** : ce qui rapporte vite (horizon 1) avant ce qui demande du fond (horizon 3). Et on ne verse pas d'eau dans un seau percé : les anomalies critiques (noindex, pages business non indexées) passent avant tout le reste.

## Comment ça marche

L'orchestrateur enchaîne des skills spécialisés, chacun sur une dimension (indexation, quick wins, cannibalisation, maillage), tous nourris par la même data Google. La dernière phase ne fait pas un nouveau diagnostic : elle synthétise les précédentes en un plan que le client peut exécuter. C'est ça que tu vends, pas le diagnostic : le plan priorisé.

## Version WhatsApp

> Capstone audit : réunis ton export GSC (6 mois) + le sitemap.xml de ton client. Dans Claude : « lance audit-engine-pipeline, déroule les 8 phases en t'arrêtant après chacune ». Tu sors un rapport en 3 horizons (quick wins → fondations → croissance), anomalies critiques en tête. Piège : prioriser, pas tout corriger d'un coup. Cowork sans terminal = phase Core Web Vitals sautée, prends un PageSpeed public à la place. 💪
