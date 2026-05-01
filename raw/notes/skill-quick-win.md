---
name: seo-quick-win
description: >
  Identifier les opportunités SEO à impact rapide depuis les données GSC. 
  Pages en position 3-12 avec impressions élevées et CTR sous-performant.
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : quick win, gains rapides, 
  opportunités immédiates, pages à optimiser vite, "qu'est-ce que je peux améliorer sans rédiger",
  "quelles pages sont proches du top 3", "résultats court terme", "on est en position 4-10",
  optimisation rapide, pages sous-performantes, CTR faible, ou uploade un export GSC 
  et veut des actions immédiates.
---

# Skill 01 — Quick Win SEO

## Rôle

Identifier dans les données GSC les pages positionnées entre la position 3 et 12, avec un volume d'impressions élevé et peu de clics. Prioriser les optimisations à impact rapide sans créer de nouveau contenu.

**Logique de priorité :**
1. Optimiser les pages existantes d'abord
2. Ensuite seulement, proposer de créer les pages pour les mots-clés qui font des impressions sans page dédiée

---

## Réflexion appliquée (méthode Boussardon)

- Le volume n'est pas un signal. Le **delta entre impressions et clics** est le vrai signal d'opportunité.
- Être top 3 est l'objectif — pas "être visible". **Position 4 = invisible commercialement.**
- On ne rédige pas pour ranker. On optimise ce qui existe d'abord. La création vient ensuite.
- Un quick win SEO n'est pas un hack : c'est corriger un décalage entre l'intention de la requête et ce que la page délivre réellement.
- Avant de proposer du nouveau contenu, **vider le backlog d'opportunités GSC.**
- Un quick win GEO inclut la **densification des "Preuves Atomiques"** : remplacer les phrases littéraires ou le bruit marketing par le schéma `[Sujet + Relation + Entité/Valeur]` dans les premiers paragraphes.

---

## Données requises

| Source | Description | Obligatoire |
|--------|-------------|-------------|
| Export GSC Pages | URL, Clics, Impressions, CTR, Position moyenne (90 jours) | ✅ Oui |
| Contexte secteur | Secteur d'activité, offre du client | Recommandé |

**Minimum viable :** Export GSC avec au moins 30 jours de données, filtre position 4–15, tri impressions décroissant.

---

## Raisonnement de l'agent (étapes obligatoires)

L'agent DOIT suivre ces étapes **dans l'ordre** avant de répondre :

### Étape 1 — Filtrer
Filtrer les pages entre position 3.0 et 15.0. Exclure :
- Pages branded (contenant le nom de marque)
- Homepage

### Étape 2 — Trier
Trier par impressions décroissantes → identifier les 10 pages avec le plus fort potentiel manqué.

### Étape 3 — Calculer le gap CTR
Pour chaque page, calculer le gap CTR :

| Position | CTR attendu |
|----------|-------------|
| 4 | ~7% |
| 5 | ~5% |
| 6-10 | ~2-3% |
| 11-15 | ~1-2% |

**Gap = CTR attendu - CTR réel**

### Étape 4 — Croiser avec l'intention
Identifier l'intention de chaque requête principale :
- **Décisionnelle** (prix, comparatif, meilleur, avis) → priorité maximale
- **Transactionnelle** (achat, urgence, devis) → priorité haute
- **Informationnelle** (comment, pourquoi, guide) → priorité basse

### Étape 5 — Prioriser
Critères de priorité maximale :
- Pages décisionnelles
- Impressions élevées (>500/mois)
- CTR < 3%
- Gap CTR > 1.5%

### Étape 6 — Lister les leviers
Pour chaque page retenue, identifier les leviers d'optimisation :
- Balise title (inclure chiffres, bénéfice, différenciateur)
- Méta-description (CTA, preuve sociale)
- Structure Hn (H1 avec data, H2 alignés sur intentions)
- FAQ en haut de page (question = requête principale)
- Contenu du premier écran (densification atomique)
- Preuves atomiques : `[Sujet + Relation + Entité/Valeur]`

**NE PAS répondre avant d'avoir complété chaque étape.**

---

## Format de sortie OBLIGATOIRE

### Tableau de 5 à 10 pages quick win priorisées

```
QUICK WIN — Top [N] Opportunités GSC

| # | URL | Position | Impressions | CTR réel | CTR attendu | Delta | Intent |
|---|-----|----------|-------------|----------|-------------|-------|--------|
| 1 | /exemple-page | 6.2 | 12 400 | 1.8% | 3.5% | -1.7% | Déc. |
```

### Fiche action par page (minimum 2 actions dont 1 preuve atomique)

```
→ Page /exemple-page

Action 1 : [Type d'action] — [Description concrète]
Action 2 : [Type d'action] — [Description concrète]  
Action 3 : Densification atomique — [Exemple avant/après]
```

---

## Exemple de sortie attendue

```
QUICK WIN — Top 5 Opportunités GSC

| # | URL | Position | Impressions | CTR réel | CTR attendu | Delta | Intent |
|---|-----|----------|-------------|----------|-------------|-------|--------|
| 1 | /service/serrurier-lyon | 6.2 | 12 400 | 1.8% | 3.5% | -1.7% | Déc. |
| 2 | /prix-remplacement-batterie | 7.8 | 8 900 | 2.1% | 3.0% | -0.9% | Déc. |
| 3 | /urgence-plombier-paris | 5.1 | 6 200 | 3.2% | 5.0% | -1.8% | Trans. |

→ Page /service/serrurier-lyon

Action 1 : Réécrire le title — inclure prix indicatif + délai
         Avant : "Serrurier Lyon - Intervention rapide"
         Après : "Serrurier Lyon : 89€ - Intervention en 30 min 24h/24"

Action 2 : Ajouter bloc Q&A en top de page (question = requête principale)
         "Combien coûte un serrurier à Lyon ?" → réponse directe chiffrée

Action 3 : Densification atomique du premier paragraphe
         Avant : "Notre équipe intervient rapidement pour tous vos problèmes de serrurerie"
         Après : "Intervention serrurier Lyon en 30 minutes. Tarif : 89€ jour, 129€ nuit. 
                  Agréé assurance. 4.8/5 sur 847 avis Google."
```

---

## Ce que l'agent NE DOIT PAS faire

❌ Proposer de créer de nouvelles pages avant d'avoir épuisé les quick wins existants

❌ Recommander des optimisations sans s'appuyer sur les données GSC réelles

❌ Confondre volume de recherche et impressions GSC — ce sont deux métriques différentes

❌ Donner des conseils génériques ("améliorez votre CTR") sans action concrète sur l'URL concernée

❌ Ignorer l'intention business de la page — une page informationnelle en position 8 n'est pas forcément une priorité

❌ Oublier la densification atomique — c'est le levier GEO le plus rapide

---

## Critère de qualité

La sortie est **bonne** si :

1. Chaque page retenue a un **delta CTR chiffré**
2. Chaque page a une **intention identifiée** (Déc./Trans./Info.)
3. Chaque page a **au moins 2 actions concrètes**
4. Au moins **1 action de preuve atomique** avec exemple avant/après
5. **Aucune recommandation générique** dans la sortie
