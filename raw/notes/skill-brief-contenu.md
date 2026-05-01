---
name: seo-brief-contenu
description: >
  Produire un brief de contenu SEO complet avec structure Hn optimisée pour le Passage Ranking.
  Basé sur les vecteurs sémantiques, micro-intentions et signaux E-E-A-T — sans copier les concurrents.
  Le 4W Deep Reflection (Who/What/Why/How) est un pré-requis bloquant avant tout brief (méthode RAID Chen et al. 2025 AAAI 2026 arXiv:2508.11158).

  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : brief, structure Hn, plan de page,
  brief éditorial, architecture de contenu, "crée-moi un brief pour ce mot-clé",
  "comment structurer ma page sur [requête]", "quels H2 mettre dans cet article",
  "je veux rédiger sur X, donne-moi le plan", outline, squelette de page, hiérarchie de titres,
  ou demande un plan de rédaction SEO.
sources_internes:
  - wiki/concepts/4w-deep-reflection.md
  - raw/etudes-seo/etude-raid-gseo-2025.md
historique:
  - 2026-04-12 — version initiale courte (118 L)
  - 2026-04-18 — version Cursor étendue (255 L)
  - 2026-04-25 — fusion : base Cursor + ajout étape 0 obligatoire 4W Deep Reflection
---

# Skill 03 — Brief de Contenu & Structure Hn

## Rôle

Produire un brief de contenu complet basé sur les vecteurs sémantiques de la requête, les micro-intentions détectées, et la logique du Passage Ranking — sans copier la structure des concurrents et sans jamais donner la base Hn à l'IA pour qu'elle rédige seule.

---

## Réflexion appliquée (méthode Boussardon)

- La **structure Hn est la colonne vertébrale du ranking**. Un mauvais plan = un mauvais contenu, même bien rédigé.

- On ne regarde pas les concurrents pour copier leur structure — on les regarde pour **identifier ce qu'ils n'ont pas dit**.

- La structure doit être construite à partir des **vecteurs sémantiques et des micro-intentions**, pas à partir d'un prompt générique.

- Le brief est toujours **rédigé en premier par l'humain** (au moins les tirets et idées clés par H2). L'IA améliore, elle ne crée pas à partir de zéro.

- L'objectif **Fully Meets** impose de répondre à l'intention primaire ET aux sous-intentions — le plan doit couvrir les deux.

- Chaque H2 doit correspondre à un **vecteur sémantique attendu** par Google sur cette requête.

- La structure doit générer un **"Gradient de Surprise"** (High Surprise). Si les H2 se contentent d'énoncer des évidences, le contenu subira un "Weight Decay" (oubli adaptatif par l'IA). Un bon H2 apporte une information inattendue ou brise un pattern.

- **Le 4W Deep Reflection (Who/What/Why/How) est OBLIGATOIRE en pré-requis bloquant** — méthode RAID validée empiriquement (−3.18 sans, +4.72 avec, paper Chen et al. 2025 AAAI 2026 arXiv:2508.11158). Sans 4W : pas de brief.

---

## Données requises

| Source | Description | Obligatoire |
|--------|-------------|-------------|
| Mot-clé principal | + cluster de requêtes associées (GSC ou outil) | ✅ Oui |
| **Brief 4W (Who/What/Why/How)** | **Pré-requis bloquant — voir Étape 0** | ✅ **Oui** |
| Micro-intentions | Questions, sous-requêtes, FAQ patterns (sortie du 4W) | ✅ Oui |
| Contexte E-E-A-T | Expériences client, cas concrets, données propriétaires | Recommandé |
| Type de page | Landing page service, article blog, page pilier | Recommandé |

**Minimum viable :** Mot-clé principal + intention de la page + secteur d'activité + 4W rempli.

---

## Raisonnement de l'agent (étapes obligatoires)

L'agent DOIT suivre ces étapes **dans l'ordre** avant de répondre :

### Étape 0 — Brief 4W Deep Reflection (NOUVEAU 2026-04-25, OBLIGATOIRE)

Avant toute autre étape, produire le 4W (30 min, ordre strict) :

1. **Who** (5 min) — lister 4-6 rôles utilisateurs distincts qui poseraient une requête sur le sujet. Bias correction : pour B2B niché, compenser le biais "généraliste" du modèle (38 % Knowledge Producers selon RAID).
2. **What** (10 min) — pour chaque rôle, formuler 2-3 besoins informationnels précis → 8-18 micro-intentions au total.
3. **Why** (5 min) — identifier les mismatches entre l'intent que le LLM infère naturellement et les besoins réels listés. Le gap = ce que le contenu actuel manque.
4. **How** (10 min) — reconstruire l'intent élargi pour couvrir l'union des rôles sans diluer la spécificité.

**Sortie obligatoire** : tableau 4W en haut du brief (Persona | Besoins | Gap | Couverture).

### Étape 1 — Décoder la requête

Identifier l'intention primaire (informée par le 4W) :

| Type | Signal | Objectif utilisateur |
|------|--------|---------------------|
| **Informationnelle** | comment, pourquoi, qu'est-ce que | Comprendre |
| **Transactionnelle** | acheter, prix, devis, urgence | Agir maintenant |
| **Navigationnelle** | [marque], [nom produit] | Trouver un site précis |
| **Décisionnelle** | meilleur, comparatif, avis, vs | Choisir avant d'agir |

Identifier les **intentions latentes** (ce que l'utilisateur ne formule pas mais cherche implicitement).

### Étape 2 — Lister les vecteurs sémantiques

Identifier les éléments attendus par Google sur cette requête :
- **Entités** (marques, normes, labels, lieux)
- **Co-occurrences** (termes qui apparaissent systématiquement avec le mot-clé)
- **Vocabulaire expert** du secteur (jargon technique légitime)

### Étape 3 — Identifier les micro-intentions

Issues directes du 4W "What" (étape 0.2). Mapper :
- **Avant** la décision (phase recherche)
- **Pendant** la décision (phase comparaison)
- **Après** la décision (phase action/validation)

### Étape 4 — Construire la structure Hn

```
H1 : Requête principale + différenciateur (donnée chiffrée ou angle unique)
│
├── H2 : [Vecteur sémantique 1] — Gradient de Surprise si possible
│   ├── H3 : Micro-intention A (persona X du 4W)
│   └── H3 : Micro-intention B (persona Y du 4W)
│
├── H2 : [Vecteur sémantique 2]
│   └── H3 : Sous-angle technique
│
├── H2 : [Vecteur sémantique 3]
│
└── H2 : FAQ décisionnelle (1 question par persona du 4W)
    ├── H3 : Question persona A
    ├── H3 : Question persona B
    └── H3 : Question persona C
```

**Règle du Gradient de Surprise :** Au moins 1 H2 doit apporter une information inattendue, contre-intuitive, ou que les concurrents évitent de mentionner.

### Étape 5 — Définir le contenu attendu par H2

Pour chaque H2, indiquer :
- Type de contenu (données chiffrées, FAQ, liste d'étapes, témoignage, tableau comparatif)
- Longueur indicative
- Éléments obligatoires

### Étape 6 — Identifier les signaux E-E-A-T à injecter

- **Experience** : cas clients réels, témoignages terrain
- **Expertise** : données propriétaires, méthodologie unique
- **Authoritativeness** : citations de sources reconnues, certifications
- **Trustworthiness** : transparence sur les limites, prix réels

### Étape 7 — Définir le format multimodal

Selon l'intention Fully Meets, identifier les formats requis :
- Vidéo démonstrative
- Tableau comparatif
- Calculateur/simulateur
- Schéma/infographie
- Template téléchargeable

**NE PAS répondre avant d'avoir complété chaque étape — incluant l'Étape 0 (4W).**

---

## Format de sortie OBLIGATOIRE

```
BRIEF — '[Mot-clé principal]'

## Brief 4W (pré-requis Chen et al. 2025)

| Persona (Who) | Besoins (What) | Gap (Why) | Couverture (How) |
|---|---|---|---|
| [Rôle 1] | [2-3 besoins] | [Mismatch identifié] | [Section du contenu] |
| [Rôle 2] | ... | ... | ... |
| [Rôle 3] | ... | ... | ... |
| ... (4-6 rôles total) | ... | ... | ... |

## Intention
- Primaire : [Type] — [Description]
- Latentes : [Liste, issues du 4W What]

## Vecteurs sémantiques clés
[Liste des entités, co-occurrences, vocabulaire expert]

## Structure Hn

H1 : [Titre optimisé avec différenciateur]

H2 : [Vecteur 1 — avec Gradient de Surprise si applicable]
  → Contenu attendu : [Type + éléments obligatoires]
  H3 : [Micro-intention pour persona X]
  H3 : [Micro-intention pour persona Y]

H2 : [Vecteur 2]
  → Contenu attendu : [Type + éléments obligatoires]

H2 : [Vecteur 3]
  → Contenu attendu : [Type + éléments obligatoires]

H2 : FAQ décisionnelle (1 question par persona du 4W)
  H3 : [Question bas de funnel persona A]
  H3 : [Question bas de funnel persona B]
  H3 : [Question bas de funnel persona C]

## Signaux E-E-A-T à injecter
- [Signal 1 + où l'insérer]
- [Signal 2 + où l'insérer]

## Format multimodal requis
- [Format 1 + justification]
- [Format 2 + justification]
```

---

## Exemple de sortie attendue

```
BRIEF — 'Remplacer batterie voiture électrique'

## Brief 4W

| Persona | Besoins | Gap vs SERP | Couverture |
|---|---|---|---|
| Propriétaire VE 5+ ans (batterie qui décline) | Coût réel, savoir si reconditionné fiable, durée intervention | Sites concurrents = prix abstraits sans modèle nommé | H2 #2 (tarifs par modèle 2024) |
| Acheteur VE occasion (méfiance batterie) | Diagnostic avant achat, garantie qui suit le véhicule | Aucun guide pré-achat dédié à la batterie | H2 #4 (3 critères prestataire) |
| Mécanicien indépendant (recherche prestataire B2B) | Liste fournisseurs reconditionnés sérieux | SERP captée par garages constructeurs | Annexe pro à prévoir |
| Conducteur LLD (bail entreprise) | Qui paie le remplacement, garantie LLD | Zone grise totale | Cocon dérivé |
| Sceptique VE (pas encore acheté) | Comprendre la dégradation pour décider achat | Articles "buy or not" mais pas d'angle batterie réel | H2 #3 (signes alerte) |

## Intention
- Primaire : Décisionnelle — l'utilisateur veut comprendre le coût et le process avant de choisir un prestataire
- Latentes : peur de l'arnaque, besoin de réassurance sur la durée de vie, question de la garantie

## Vecteurs sémantiques clés
prix, durée intervention, garantie, modèle (Tesla/Renault/Peugeot), autonomie après remplacement,
batterie reconditionnée vs neuve, aides ADEME, capacité kWh, dégradation normale

## Structure Hn

H1 : Remplacement batterie voiture électrique : prix réels, délais et ce que personne ne dit

H2 : [GRADIENT DE SURPRISE] L'erreur à 500€ que 90% des propriétaires font
  → Contenu attendu : Cas concret + piège à éviter + solution
  → Ce H2 brise le pattern "intro générique" et capte l'attention

H2 : Combien coûte réellement le remplacement ? (données 2024)
  → Contenu attendu : Tableau de prix par modèle, neuf vs reconditionné
  H3 : Prix batterie neuve par modèle (Tesla, Renault, Peugeot)
  H3 : Prix batterie reconditionnée — est-ce fiable ?
  H3 : Ce que votre assurance peut couvrir

H2 : Quand faut-il vraiment changer sa batterie ?
  → Contenu attendu : Tableau diagnostic avec seuils + signes d'alerte
  H3 : Les 4 signes qui ne trompent pas (persona Sceptique VE)
  H3 : Différence entre dégradation normale et défaut

H2 : Trouver un prestataire fiable : les 3 critères que personne ne mentionne
  → Contenu attendu : Checklist actionnable + red flags

H2 : FAQ décisionnelle (1 question par persona du 4W)
  H3 : Puis-je rouler avec une batterie dégradée à 70% ? (Propriétaire VE)
  H3 : Le remplacement remet-il le compteur de garantie à zéro ? (Acheteur occasion)
  H3 : En LLD, qui paie le remplacement de batterie ? (Conducteur LLD)
  H3 : Batterie chinoise vs européenne : quelle différence réelle ? (Sceptique VE)

## Signaux E-E-A-T à injecter
- 2 cas clients réels avec marque du véhicule + coût final + satisfaction (dans H2 prix)
- Mention certification/agrément du prestataire (dans H2 prestataire)
- Source ADEME pour les aides (dans H3 assurance)

## Format multimodal requis
- Calculateur de coût estimatif en haut de page (intention = "combien ça coûte")
- Tableau comparatif prix neuf/reconditionné par modèle (scannable)
```

---

## Ce que l'agent NE DOIT PAS faire

❌ **Sauter l'Étape 0 (4W)** — pré-requis bloquant. Sans tableau 4W en haut du brief, output invalide.

❌ Donner la base Hn complète à l'IA pour qu'elle rédige seule — la réflexion doit rester humaine

❌ Copier la structure des 3 premiers résultats Google — c'est la définition du contenu moyen

❌ Produire un plan générique sans identifier les vecteurs sémantiques réels de la requête

❌ Oublier les micro-intentions : un plan sans FAQ ou sous-angles est incomplet

❌ Ignorer le format multimodal : Google évalue si la page répond à l'intention avec le bon type de contenu

❌ Créer des H2 sans Gradient de Surprise — si tous les H2 sont prévisibles, le contenu sera oublié par les LLMs

❌ Proposer des H2 génériques comme "Introduction", "Conclusion", "Notre avis" — ce sont des vecteurs vides

❌ Ne pas tracer la couverture des personas du 4W dans les H3 / FAQ — le 4W doit être visible dans la structure

---

## Critère de qualité

La sortie est **bonne** si :

1. **Le tableau 4W est présent en haut du brief** (4-6 personas avec Besoins / Gap / Couverture)
2. Chaque H2 correspond à un **vecteur sémantique identifié** (pas un titre générique)
3. Le **Gradient de Surprise est présent** (au moins 1 H2 contre-intuitif ou différenciant)
4. La FAQ contient des **questions bas de funnel** (1 question par persona du 4W minimum)
5. Le brief inclut **au moins 2 signaux E-E-A-T propriétaires** avec emplacement précis
6. Le **format multimodal est justifié** par l'intention de la requête
7. Aucun H2 générique ("Introduction", "Conclusion", "À retenir")
8. Chaque persona du 4W est **traçable dans la structure Hn**
