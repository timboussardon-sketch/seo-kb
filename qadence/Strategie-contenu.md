---
type: strategie
title: "Qadence — Stratégie de contenu (index)"
projet: qadence
created: 2026-06-18
updated: 2026-06-18
statut: en cours
---

# Qadence — Stratégie de contenu

Cluster de contenu « Comment faire X » : chaque page démontre, sur un problème réel, que Qadence le résout, puis renvoie vers l'agent (la page business). Le contenu se positionne ET se fait citer par les moteurs génératifs.

**Un doc par contenu** dans `strategie-contenu/`. Ce fichier est l'index.

## Règles de production (non négociables)

- **Uniquement nos skills et nos process.** Zéro invention.
- **Lire le vault Obsidian à chaque page** avant de produire : skill concerné + concepts liés. On cite la doctrine, jamais du SEO générique.
- **Aucun chiffre ni date inventé** (règle GEO Sentinel). Si une donnée manque : `[À SOURCER]`.
- **Voix Tim** : tutoiement, direct, anti-IA writing, positions tranchées. Pas de tiret cadratin. Pas de rhétorique IA (« ce n'est pas X, c'est Y »). On ne met jamais les sites en compétition (pas de « concurrent ») : on parle des pages déjà classées et des intentions à couvrir.
- **GEO** = Generative Engine Optimization (jamais SEO géographique).
- **Un contenu à la fois.**

## Forme de chaque page (doctrine Organikk appliquée à elle-même)

- **Answer-first** : réponse à la requête dans les 2-3 premières phrases, bloc dans les 300 premiers mots ([[answer-first-pattern]]).
- **Passages ancrés** : chaque H2 = un vecteur sémantique autonome de 150-200 mots ([[triade-serp]] phase 2).
- **Grounding** : au moins 2 preuves atomiques / 100 mots, data de la méthode ([[grounding-score]]).
- **Surprise** : un angle que la SERP ne dit pas ([[surprise-gap]]).
- **Action Engine** : chaque page Know pointe vers le Do (l'agent Qadence).

## Pilier et maillage

- **Pilier (Do, page business)** : l'agent SEO/GEO branché Search Console → `qadence.io/app`.
- Chaque sous-cluster a un **hub** (page Know chapeau) ; les satellites Know pointent vers le hub + le Do.
- Maillage intentionnel : **Know → Do prioritaire** sur Know → Know ([[know-simple-know-do]], [[maillage-systeme]]).

## Périmètre & avancement (clusters 1, 2, 3, 4, 5, 6, 9)

### Cluster 1 — Search Console & diagnostic
*Jade · audit_gsc · analyse_gsc_complete · cohortes_gsc · quick_win*
- [x] [[strategie-contenu/01-analyser-sa-search-console|01 — Comment analyser sa Search Console]]
- [ ] 02 — Comment auditer son site sur les 28 derniers jours (Jade)
- [ ] 03 — Comment savoir pourquoi une page perd des positions
- [ ] 04 — Comment trouver ses pages en position 3 à 12 (gains rapides)
- [ ] 05 — Comment améliorer son CTR sur une page bien positionnée
- [ ] 06 — Comment prioriser ses actions SEO (plan RICE)
- [ ] 07 — Comment segmenter ses pages en cohortes de performance
- [ ] 08 — Comment repérer ses impressions sous-exploitées

### Cluster 2 — Maillage interne
*Indigo · maillage_interne · maillage_systeme · maillage_interne_gsc*
- [ ] Comment faire un maillage interne efficace · trouver ses pages orphelines · choisir ses ancres · structurer un cocon · relier mères/filles · repérer les liens manquants (GSC)

### Cluster 3 — Cannibalisation
*cannibalisation*
- [ ] Détecter une cannibalisation · résoudre deux pages sur la même requête · fusion vs 301 · vérifier dans la GSC

### Cluster 4 — Recherche & clustering mots-clés
*Ambre · recherche_mots_cles · clustering_mots_cles · mots_cles_decisionnels*
- [ ] Trouver des mots-clés sur une thématique · regrouper par intention · 1 cluster = 1 page · mots-clés qui convertissent · longue traîne · opportunités business

### Cluster 5 — Intention & sémantique
*intention_recherche · query_requete · preparation_semantique · entites_vectorielles · score_semantique*
- [ ] Intention d'un mot-clé · décoder une requête (cluster RRF) · préparer le champ sémantique · couvrir les entités · mesurer le grounding · couvrir toute l'intention

### Cluster 6 — Brief & rédaction
*Carmin · brief_contenu · structure_hn · structure_hn_editoriale · workflow_article*
- [ ] Faire un brief SEO · structurer les Hn · plan d'article qui se positionne · rédiger de A à Z · hiérarchiser H1/H2/H3 · auditer une structure Hn

### Cluster 9 — Technique
*Azur · core_web_vitals · donnees_structurees · Onyx (indexation)*
- [ ] Améliorer ses Core Web Vitals · audit Lighthouse · données structurées Schema.org · vérifier l'indexation · pourquoi une page n'est pas indexée · résoudre noindex/sitemap

(Exclus : 7 GEO · 8 pSEO · 10 Stratégie.)
