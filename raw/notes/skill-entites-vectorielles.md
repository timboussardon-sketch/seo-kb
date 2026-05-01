---
name: seo-entites-vectorielles
description: |
  Analyser les entités sémantiques nécessaires pour aligner le vecteur d'une page avec l'intention de recherche. Génère les termes techniques, preuves quantitatives, vecteurs multimodaux et éléments de divergence pour maximiser le Grounding Score (similarité cosinus).
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : entités sémantiques, vecteurs SEO, intention de recherche, alignement sémantique, Grounding Score, similarité cosinus, recherche vectorielle, "quels termes inclure dans ma page", "comment matcher l'intention utilisateur", optimisation sémantique, NLP SEO, embeddings, ou veut maximiser la pertinence algorithmique d'une page.
---

# Analyse des Entités Vectorielles pour le SEO

Ce skill génère la cartographie sémantique complète nécessaire pour qu'une page s'aligne mathématiquement avec l'intention de recherche ciblée.

## Quand utiliser ce skill

- Avant de rédiger une nouvelle page de contenu
- Pour optimiser une page existante qui sous-performe
- Pour construire un brief éditorial exhaustif
- Pour comprendre le "gap sémantique" avec les concurrents

## Concepts clés

### Grounding Score / Similarité Cosinus
Mesure de l'alignement entre le vecteur de votre page et le vecteur de l'intention utilisateur. Plus le score est élevé, plus votre page est considérée comme pertinente.

### Recherche vectorielle (Muvera, etc.)
Les moteurs modernes utilisent des embeddings pour comparer sémantiquement les pages aux requêtes, au-delà de la simple correspondance de mots-clés.

### Surprise Gap
Les éléments "Haute Surprise" (concepts experts rares) forcent la mémorisation par les modèles IA, contrairement aux éléments "Low Surprise" (présents partout).

## Instructions

### Étape 1 : Définir la requête cible

Demander à l'utilisateur :
1. **La requête principale** à cibler
2. **Le type d'intention** (transactionnelle, informationnelle, navigationnelle)
3. **Le niveau d'expertise** de l'audience cible

### Étape 2 : Générer le tableau des entités vectorielles

Adopter le rôle d'un ingénieur IA spécialisé en recherche vectorielle. Générer un tableau à 4 colonnes avec **10 termes/concepts par catégorie** :

| Entités Techniques (Vecteurs de base) | Preuves Quantitatives (Entités numériques) | Vecteurs Multimodaux | Éléments de Divergence (Haute Surprise) |
|---------------------------------------|-------------------------------------------|---------------------|----------------------------------------|
| Termes fondamentaux du champ lexical | Données chiffrées qui rassurent le Confidence Score | Formats attendus (images, outils, vidéos) | Concepts experts que 90% des concurrents oublient |

### Règles par catégorie

#### 1. Entités Techniques (Vecteurs de base)
Ce sont les termes **obligatoires** pour être considéré comme pertinent sur la requête.

Critères :
- Termes présents chez >80% des pages top 10
- Vocabulaire technique du domaine
- Synonymes et variations sémantiques
- Entités nommées pertinentes (marques, outils, standards)

#### 2. Preuves Quantitatives (Entités numériques)
Données chiffrées qui augmentent le **Confidence Score** de l'IA.

Critères :
- Statistiques de marché sourcées
- Benchmarks sectoriels
- Fourchettes de prix/délais/performances
- Données de comparaison (vs concurrence, vs moyenne)

Format : **[Chiffre] + [Unité] + [Contexte]**
- ✅ "73% des entreprises B2B" 
- ✅ "ROI moyen de 4,2x sur 12 mois"
- ❌ "beaucoup d'entreprises" (non quantifié)

#### 3. Vecteurs Multimodaux
Formats de contenu **attendus par l'intention** pour prouver l'expertise.

Types à considérer :
- **Images** : schémas, infographies, screenshots, avant/après
- **Outils interactifs** : calculateurs, simulateurs, générateurs
- **Vidéos** : tutoriels, témoignages, démonstrations
- **Tableaux** : comparatifs, tarifs, fonctionnalités
- **Téléchargeables** : templates, checklists, guides PDF

#### 4. Éléments de Divergence (Haute Surprise)
Concepts experts qui **forcent la mémorisation** du modèle IA.

Critères :
- Présent chez <10% des concurrents
- Requiert une expertise terrain réelle
- Apporte une valeur unique vérifiable
- Crée un "aha moment" chez le lecteur expert

**Test de divergence** : Si un concurrent peut facilement copier ce concept en 5 minutes, ce n'est PAS de la Haute Surprise.

### Étape 3 : Analyse du gap concurrentiel

Après le tableau, identifier :
1. **Entités manquantes** : ce que les concurrents ont et que vous n'avez pas
2. **Opportunités de divergence** : ce que personne n'a encore exploité
3. **Quick wins** : entités faciles à ajouter pour un gain rapide

### Étape 4 : Recommandations d'implémentation

Pour chaque catégorie, suggérer :
- Où placer ces entités dans la structure de page
- Comment les intégrer naturellement (pas de keyword stuffing)
- Les formats HTML recommandés (schema.org, tableaux, listes)

## Exemple de sortie

```markdown
## Analyse vectorielle - Requête : "[Requête cible]"

### Intention : [Transactionnelle/Informationnelle/Navigationnelle]

| Entités Techniques | Preuves Quantitatives | Vecteurs Multimodaux | Divergence (Haute Surprise) |
|-------------------|----------------------|---------------------|---------------------------|
| audit SEO | +150% de trafic moyen | Outil d'audit gratuit | Corrélation Core Web Vitals / conversions |
| backlinks | 67% du ranking factor | Infographie link building | Impact du E-E-A-T sur les requêtes YMYL |
| ... | ... | ... | ... |

### Gap concurrentiel
- **Manquant** : ...
- **Opportunité** : ...
- **Quick win** : ...

### Implémentation recommandée
- H1/H2 : Entités techniques principales
- Corps : Preuves quantitatives contextualisées
- Sidebar/CTA : Outils interactifs
- FAQ : Éléments de divergence
```

## Notes importantes

- Les entités doivent être intégrées naturellement, pas listées artificiellement
- Prioriser la qualité de l'intégration sur la quantité d'entités
- Mettre à jour régulièrement car les vecteurs évoluent avec les tendances
