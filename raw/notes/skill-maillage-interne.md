---
name: maillage-interne-gsc
description: >
  Analyse et optimisation du maillage interne SEO à partir des données Google Search Console (GSC).
  Utilise la méthode Timothée Boussardon : cocon sémantique, hiérarchie page mère/fille/petite-fille,
  et signaux GSC pour identifier les opportunités de liens internes à fort ROI.
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : maillage interne, liens internes, cocon SEO,
  pages orphelines, GSC + SEO, Search Console + stratégie de contenu, analyse de structure de site,
  hiérarchie sémantique, pages mères/filles, ou demande d'optimiser la circulation du PageRank interne.
  Utiliser aussi quand l'utilisateur uploade un fichier GSC (CSV, Excel) et veut analyser son SEO.
---

# Skill : Analyse du Maillage Interne depuis la GSC

## Philosophie (méthode Boussardon)

Le maillage interne est **ultra important** — c'est la puissance SEO. Pas de backlinks achetés, mais un cocon sémantique solide construit autour de mots-clés business choisis avec soin.

Principes fondamentaux :
- **Page mère = au moins 10 citations** depuis des pages filles/petites-filles
- Le maillage interne part de la **stratégie de mots-clés** → le cocon est la conséquence, pas le point de départ
- Priorité : transactionnel > décisionnel > informationnel
- La GSC contient TOUTES les données nécessaires — elle est juste mal visualisée
- Tout maillage manuel reste l'idéal, mais la GSC permet des **insights à 50%** pour accélérer
- **Le maillage ne se fait pas uniquement par sémantique — il se fait aussi par intention (tâche/action)** : une page "Know" doit pointer vers une page "Do"

---

## Étape 1 — Récupérer les données GSC

### Format attendu du fichier client
Demander à l'utilisateur d'exporter depuis la GSC :
- **Pages** : URL, Clics, Impressions, CTR, Position moyenne
- **Requêtes par page** (export "Pages" > clic sur une URL > "Requêtes")
- Période recommandée : **3 à 6 derniers mois**

Si l'utilisateur n'a pas les données, lui donner ces instructions d'export :
> GSC → Performance → Pages → Exporter en CSV. Puis Pages → clic sur une URL → Requêtes → Exporter.

---

## Étape 2 — Diagnostiquer la structure actuelle

À partir des données GSC, analyser en 4 axes :

### 2.1 — Identifier les pages stratégiques (pages mères potentielles)
Critères de sélection d'une page mère :
- Impressions élevées (forte visibilité thématique)
- Position moyenne entre 4 et 15 (potentiel de progression)
- Mot-clé principal = transactionnel/décisionnel

### 2.2 — Détecter les pages sous-maillées
Signes d'alerte :
- Bonne position mais CTR faible → manque de liens internes pour pousser l'autorité
- Impressions élevées mais clics stagnants → la page existe sémantiquement mais n'est pas renforcée
- Page orpheline = aucune page GSC ne mentionne cette thématique en secondaire

### 2.3 — Trouver les connexions sémantiques GSC
Méthode :
1. Prendre une page mère cible (ex: `/consultant-seo-paris`)
2. Lister toutes les requêtes GSC qui triggent cette page
3. Identifier les requêtes qui *auraient dû* déclencher d'autres pages mais déclenchent celle-ci → cannibalisation ou opportunité de maillage
4. Si une requête secondaire a des impressions → créer ou mailler une page fille sur cette requête

### 2.4 — Mesurer la puissance du maillage existant
Indicateur proxy GSC :
- Une page mère bien maillée = position stable et CTR > moyenne de la niche
- Une page mère mal maillée = oscillations de position, CTR bas malgré le volume
- Règle : **10 citations minimum** depuis des pages filles pour considérer une page mère "active"

---

## Étape 3 — Construire le plan de maillage

### Structure hiérarchique (cocon sémantique)

```
Page Mère (mot-clé principal business)
├── Page Fille 1 (requête secondaire transactionnelle)
│   ├── Page Petite-Fille A (longue traîne / micro-intention)
│   └── Page Petite-Fille B
├── Page Fille 2
│   └── Page Petite-Fille C
└── Page Fille 3
```

**Règles de maillage :**
- Pages mères liées entre elles (maillage horizontal niveau 0)
- Chaque page fille cite sa page mère + 1 ou 2 pages sœurs
- Chaque petite-fille cite sa page fille + sa page mère (lien profond)
- Ancres = requête exacte ou variante proche (jamais "cliquez ici")

### Maillage par intention (Know → Do) — couche complémentaire

Le maillage sémantique (même thématique) ne suffit plus. Il faut aussi mailler **par tâche/action** : une page qui explique un concept doit systématiquement pointer vers la page qui permet de le faire.

#### Classification des types de pages

| Type | Intention GSC | Description | Exemples |
|------|--------------|-------------|---------|
| **Know** | Informationnelle | L'utilisateur comprend, apprend | "qu'est-ce que le maillage interne", "comment fonctionne le CTR" |
| **Do** | Transactionnelle / Outil | L'utilisateur agit, utilise, achète | simulateur, template, outil, audit, prestation |
| **Know + Do** | Décisionnelle | L'utilisateur compare pour choisir | "meilleur outil SEO", "consultant SEO ou agence" |

#### Règle du lien Know → Do

> Chaque page **Know** doit contenir au moins **1 lien vers une page Do** thématiquement reliée.

L'objectif n'est pas seulement de transmettre du PageRank — c'est de **guider l'utilisateur vers l'action** après la lecture, ce qui améliore les signaux comportementaux de la page cible (temps sur page, taux de rebond, retour GSC).

#### Comment identifier les paires Know → Do depuis la GSC

1. Lister les pages avec des requêtes de type "comment faire X", "qu'est-ce que X", "pourquoi X" → ce sont les **Know**
2. Lister les pages avec des requêtes transactionnelles / des CTR élevés → ce sont les **Do**
3. Créer les ponts : chaque Know dont la thématique a un pendant Do doit le lier explicitement

#### Exemples de paires à créer

| Page Know (source) | Page Do (destination) | Ancre recommandée |
|--------------------|-----------------------|-------------------|
| "Comment faire un audit SEO" | Prestation audit SEO | "demander un audit SEO" |
| "Qu'est-ce qu'un cocon sémantique" | Template cocon / outil | "créer votre cocon sémantique" |
| "Pourquoi le CTR est important" | Outil de suivi CTR | "analyser votre CTR" |
| "Guide maillage interne" | Page contact / accompagnement | "optimiser votre maillage" |

#### Cas particulier : pages "Do" isolées
Une page Do sans pages Know qui pointent vers elle est **sous-exploitée**. Créer ou identifier des pages Know existantes qui peuvent l'alimenter = gains rapides sans créer de nouveau contenu.

### Template de plan d'action

Pour chaque page mère identifiée, produire :

| Page Mère | URL | Position actuelle | Objectif | Pages filles existantes | Liens manquants à créer |
|-----------|-----|-------------------|----------|--------------------------|--------------------------|
| ... | ... | ... | ... | ... | ... |

---

## Étape 4 — Prioriser les actions

### Matrice de priorisation

**Score d'urgence = (Impressions × 0.4) + (Potentiel position × 0.4) + (Business value × 0.2)**

Prioriser dans cet ordre :
1. **Quick Wins** : pages en position 4-10, impressions > 500/mois → ajouter des liens entrants depuis pages filles existantes
2. **Renforts** : pages mères sans 10 citations → identifier pages filles à créer ou à relier
3. **Maillage structurant** : pages orphelines avec potentiel → intégrer dans le cocon existant

---

## Étape 5 — Générer les recommandations concrètes

### Format de livrable

Pour chaque action, donner :
- **Page source** (où ajouter le lien) + **type d'intention** (Know / Do / Know+Do)
- **Page destination** (la page à renforcer) + **type d'intention**
- **Nature du lien** : sémantique (même thématique) ou intentionnel (Know → Do)
- **Ancre recommandée** (texte du lien)
- **Contexte** (dans quel paragraphe / section insérer)
- **Priorité** (Haute / Moyenne / Faible)

Exemple :
> Sur la page `/guide-maillage-interne` (**Know**), dans la section "Passer à l'action", ajouter un lien vers `/accompagnement-seo` (**Do**) avec l'ancre "optimiser votre maillage interne" — Lien intentionnel Know→Do — Priorité : HAUTE.

---

## Signaux GSC à surveiller après maillage

Après 4 à 8 semaines d'implémentation :
- Position moyenne de la page mère → doit progresser
- CTR de la page mère → doit augmenter (meilleure autorité = meilleur rankin)
- Nombre d'impressions des pages filles → doit croître (effet de cocon)
- Stabilité des positions → réduction des oscillations

---

## Points de vigilance

- **Ne pas automatiser à 100%** : le maillage part de la stratégie de mots-clés. Il faut "avoir le cocon dans la tête" avant de mailler
- **Cannibalisation** : si 2 pages répondent à la même intention, consolider avant de mailler
- **Ancres variées** : éviter de répéter la même ancre exacte sur toutes les pages filles
- **Cohérence thématique** : ne lier que des pages sémantiquement proches — un lien hors contexte dilue la puissance
- **Prioriser les pages business** : un blog informationnel ne doit pas recevoir plus de liens qu'une landing page transactionnelle
- **Maillage Know→Do ≠ maillage sémantique** : les deux coexistent. Ne pas confondre "même thématique" (sémantique) avec "même parcours utilisateur" (intentionnel). Les deux types de liens sont nécessaires et se renforcent mutuellement

---

## Rappels méthode

> "Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."
> "Une page mère doit avoir au moins 10 citations."
> "La Search Console a toutes les données — elle est juste mal visualisée."
> "Maillage manuel toujours : on a besoin des insights, pas de l'automatisation totale."
