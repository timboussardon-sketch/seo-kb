---
type: skill-pattern
slug: modele-production
date: 2026-05-14
auteur: Tim Boussardon
statut: pattern-reference
tags:
  - skill-pattern
  - modele-production
  - pseo
  - strategie-mots-cles
  - reproduction
related:
  - "[[skill-programmatique-pseo]]"
  - "[[skill-entites-vectorielles]]"
  - "[[skill-product-led-seo]]"
  - "[[session-1-mots-cles-prep]]"
  - "[[session-2-redaction-prep]]"
  - "[[2026-04-25-pseo-data-driven-organikk-cursor]]"
---

# Modèle de production · Pattern pour stratégie de mots-clés par secteur

Pattern à appliquer pour produire une page HTML autonome qui cartographie l'ensemble de la stratégie de mots-clés d'un secteur, produit ou service donné. La page combine trois skills mobilisés en série et reproduit pixel-perfect la structure validée sur le cas agences immobilières Paris (2026-05-14).

Référence visuelle locale : `~/Downloads/test-pseo-agence-immo-paris-v2.html`.

---

## Quand déclencher ce pattern

À utiliser dès que je dois produire une stratégie de mots-clés complète sur :
- Un nouveau secteur (immobilier, SaaS RH, conseil RGPD, marketplace pros)
- Un nouveau produit ou service à scaler en SEO
- Une niche que je veux conquérir avec un système pSEO + entités + Product-Led

Phrases qui déclenchent ce pattern : « fais-moi une stratégie de mots-clés pour [X] », « stratégie pSEO complète sur [X] », « cartographie SEO du secteur [X] », « modèle de production sur [X] ».

---

## Output cible (à produire à l'identique)

Une page HTML autonome (un seul fichier `.html`, ouvrable directement dans le navigateur), respectant la structure et la mise en forme suivantes.

### Structure obligatoire en 5 parties

1. **Header** : h1 « Liste des mots-clés pour [X] » (pluriel exact, jamais « mot-clé » singulier).
2. **Bloc doctrine** (obligatoire, juste après le h1, 1 paragraphe court, ton de voix Tim, tutoiement, position tranchée). Reformulation et adaptation au mot-clé cible de la doctrine pixel-perfect : « ne pas refaire ce que les autres ont déjà produit, identifier 3 à 5 mots-clés business sur lesquels on a un différenciant, construire son autorité thématique autour de ces mots-clés, notamment en attaquant les micro-intentions et les problématiques que les prospects formulent vraiment ». Quatre piliers obligatoires : critique du status quo + 3 à 5 mots-clés business + autorité thématique + micro-intentions/problématiques client. Aucun ajout d'interprétation personnelle (sanctions Google, citations LLM, anti-IA writing) en dehors de ces 4 piliers.
3. **Partie 1 · Les micro-intentions sémantiques** : intro qui explique le découpage en longue traîne pour les LLMs + 12 listings de pages filles avec titres simples « Pages par [X] », intros « Pour quelqu'un qui cherche [Y] » zéro jargon, et 5 à 12 exemples de mots-clés par listing.
4. **Partie 2 · Les entités sémantiques** : intro qui explique pourquoi couvrir le titre ne suffit pas + matrice 4 colonnes (entités techniques, preuves quantitatives, vecteurs multimodaux, divergence) pour 3 grandes familles de pages.
5. **Partie 3 · Les outils pour récupérer un email du visiteur** : intro « pour ne pas rédiger pour rien » + 10 outils interactifs avec mécanique de capture + 7 mécaniques annexes.
6. **Partie 4 · Par où commencer** : tableau de priorisation à 6 colonnes (`#`, `Modèle`, `Pages`, `Effort`, `Conversion`, `Priorité`), scoré 1 à 5 dans les 3 colonnes finales. Effort = déterministe (profondeur du template × besoin d'expertise × données externes requises). Conversion = classification d'intention décisionnelle sur les modificateurs présents dans les exemples (signal `seo-mots-cles-decisionnels`). Priorité = `Conversion / Effort` arrondi à 1-5. Interdit d'ajouter une colonne Volume SEO ou Impact SEO sans Keyword Planner ou SERP probe réel. Interdit d'ajouter une colonne Data dispo sans input humain client. Mieux vaut moins de colonnes que des chiffres inventés.
7. **Partie 5 · Plan d'action en 3 étapes** : data propriétaire → méthode calibrée dans Claude → production. Tableau 3 lignes.
8. **CTA** : Bootcamp SEO+IA + Accompagnement 1:1 + Footer.

### Style visuel (pixel perfect)

- Police : Georgia / serif sur tout le corps
- Gradient bleu Organikk pixel-perfect sur les titres h1 et h2 : `linear-gradient(135deg, #4685F0, #1B3E8F)` avec `-webkit-background-clip: text`
- h3 en `#1B3E8F` plein, h4 idem
- Bordure inférieure du header en `2px solid #1B3E8F`
- Encadrés `.template`, `.entity-box`, `.tool`, `.phase` en `#fafbfd` avec bordure `#e3e7ed`
- Encadrés d'alerte (warning) en `#fff7e6` avec bord `#d4a017`
- Page pilier en gradient pastel `linear-gradient(135deg, #f0f4ff 0%, #e8eeff 100%)`
- CTA final en background `#1B3E8F` blanc inversé
- Police mono `'SF Mono', Menlo, monospace` pour les mots-clés et codes

### Règles de contenu

- Zéro mention visible du mot « skill » dans le contenu publié (autorisée dans le frontmatter et les commentaires HTML uniquement)
- Zéro jargon dans les titres de partie et de listing
- Jamais le mot « nuage », toujours « vecteur sémantique » ou « micro-intentions »
- Pas d'em-dash (— ou –), uniquement `.` `,` `:` `;` `(` `)`
- Pas de phrases staccato dans les intros (interdiction des séries « Sujet verbe. Sujet verbe. »)
- Pas de noms d'outils concurrents (Semrush, Ahrefs, Yoast), utiliser « outils du marché »
- Pas de chiffre inventé : tout chiffre cité dans la matrice de priorisation doit être marqué « à mesurer » s'il n'y a pas eu extraction Keyword Planner réelle

---

## Skills à mobiliser (dans l'ordre)

### Skill 1 · seo-programmatique-pseo

**Rôle.** Identifier les 12 listings de pages filles et leurs variables. Générer la matrice de priorisation. Sortir le plan d'action 90 jours.

**Mobilisation pour ce pattern.** Sert Partie 1 (génération des 12 listings + variables) et Partie 4 (format du tableau de priorisation, critères 1-5).

**Sortie attendue du skill.** Liste des templates avec pattern d'URL, head term fixe, modificateur variable, nombre de pages estimé, source de données. Plus la matrice de priorisation et le séquencement.

### Skill 2 · seo-entites-vectorielles

**Rôle.** Cartographier le vecteur sémantique attendu sur chaque grande famille de pages.

**Mobilisation pour ce pattern.** Sert Partie 2 (matrice 4 colonnes sur 3 familles de pages).

**Sortie attendue du skill.** Pour chaque famille : entités techniques (champ lexical expert), preuves quantitatives (chiffres datés, études), vecteurs multimodaux (formats attendus), éléments de divergence (ce que personne ne dit, Surprise Gap).

### Skill 3 · seo-product-led

**Rôle.** Identifier les outils interactifs gagnants sur les intentions Do du secteur.

**Mobilisation pour ce pattern.** Sert Partie 3 (10 outils + 7 mécaniques annexes).

**Sortie attendue du skill.** Liste de calculateurs, simulateurs, comparateurs, quiz adaptés au secteur, avec pour chaque outil sa mécanique de capture email associée (ce qu'on envoie par email contre l'email du visiteur).

---

## Procédure de reproduction sur un nouveau secteur

### Étape A · Cadrage initial

Avant tout, recueillir auprès du client ou poser soi-même :

- Mot-clé pilier (forme courte : « agence immobilière Paris », « logiciel RH PME », « consultant RGPD »)
- Persona cible (qui, quel problème, quelle phase du parcours)
- Offre principale (ce qu'on vend derrière)
- Concurrents directs (3 à 5)
- Données propriétaires disponibles (CRM, verbatims, chiffres internes, témoignages)
- Sources externes mobilisables (APIs sectorielles, statistiques publiques, annuaires)

### Étape B · Génération du contenu via les 3 skills

Dans Claude Cowork, lancer dans l'ordre, dans la même conversation :

1. **Skill 1** : « Applique seo-programmatique-pseo sur [mot-clé pilier]. Identifie 10-15 listings, leurs variables, et estime le nombre de pages générables par listing. »
2. **Skill 2** : « Applique seo-entites-vectorielles sur 3 grandes familles de pages identifiées. Sors la matrice 4 colonnes pour chacune. »
3. **Skill 3** : « Applique seo-product-led sur le secteur. Identifie 10 outils interactifs avec leur mécanique de capture email associée. »

### Étape C · Mise en HTML pixel-perfect

1. Dupliquer le fichier de référence `~/Downloads/test-pseo-agence-immo-paris-v2.html` en `~/Downloads/test-pseo-[secteur].html`
2. Substituer le contenu généré par les 3 skills dans les sections correspondantes
3. Adapter le H1, la lede, les 5 stats, le footer
4. Vérifier que les règles de contenu sont respectées (zéro nuage, zéro skill mentionné, zéro chiffre inventé dans la Partie 4)
5. Ouvrir dans le navigateur pour validation visuelle

### Étape D · Validation et itération

- Relire à voix haute la page entière pour détecter le ton IA
- Vérifier que chaque listing a son intro « Pour quelqu'un qui cherche [Y] » zéro jargon
- Vérifier que la matrice de Partie 4 est marquée « à mesurer » et non remplie de chiffres inventés
- Adapter le CTA aux liens organikk.co réels (bootcamp et accompagnement)

---

## Prompt à coller dans Claude pour déclencher le pattern

```
Applique le pattern [[modele-production]] sur le secteur suivant : [SECTEUR].

Contexte client :
- Mot-clé pilier : [...]
- Persona cible : [...]
- Offre principale : [...]
- Concurrents directs : [...]
- Data propriétaire disponible : [...]
- Sources externes mobilisables : [...]

Sortie attendue : une page HTML autonome reproduisant pixel-perfect la structure et la mise en forme de ~/Downloads/test-pseo-agence-immo-paris-v2.html, avec :
- Header h1 « Liste de mots-clés pour [SECTEUR] »
- Partie 1 · Les micro-intentions sémantiques : 10-15 listings avec titres simples, intros « Pour quelqu'un qui cherche [Y] » zéro jargon, et 5-12 mots-clés par listing
- Partie 2 · Les entités sémantiques : matrice 4 colonnes sur 3 familles de pages
- Partie 3 · Les outils pour récupérer un email du visiteur : 10 outils + 7 mécaniques annexes
- Partie 4 · Par où commencer : tableau de priorisation à remplir (cellules « à mesurer »)
- Partie 5 · Plan d'action en 3 étapes : data propriétaire, skills calibrés, production
- CTA bootcamp + accompagnement + footer

Respecte les règles : gradient bleu Organikk sur titres, Georgia serif, zéro mention de « skill » dans le contenu visible, zéro nuage, zéro chiffre inventé, pas d'em-dash, pas de noms d'outils concurrents.

Mobilise les 3 skills dans l'ordre : seo-programmatique-pseo → seo-entites-vectorielles → seo-product-led.
```

---

## Garde-fous appliqués (issus du skill pSEO)

- **Contenu unique obligatoire.** Chaque listing doit décliner du contenu réellement différent par variable. Le template définit la structure, pas le texte.
- **Données terrain, zéro hallucination.** Aucun chiffre inventé. Si une donnée n'est pas vérifiable, elle n'apparaît pas. Marquer `[DONNÉE À SOURCER]` dans le draft.
- **Sourcing horodaté.** Toute donnée chiffrée vient d'une source d'autorité datée de moins de 3 ans.
- **Canonical propre.** 1 URL = 1 contenu = 1 canonical.
- **Maillage différenciant.** Cross-linking entre listings sur les requêtes communes, sans cannibaliser les intentions.
- **Surprise Score.** Chaque famille doit contenir au moins 1 élément que les concurrents ne disent pas.
- **Grounding Score.** Passage ancré 150-200 mots + bloc authorship environ 50 mots prévus dans la structure de chaque page générée.

---

## Critères de réussite

La page est considérée comme livrée quand :

- Les 5 stats du header sont remplies avec les chiffres réels du secteur
- La page pilier est définie (URL, mot-clé, intention, rôle dans le cocon)
- 10 à 15 listings sont identifiés avec leurs variables et leurs exemples de mots-clés
- La matrice 4 colonnes est remplie pour 3 familles de pages
- 10 outils interactifs sont listés avec leur mécanique de capture
- Le tableau de Partie 4 est structuré, cellules marquées « à mesurer »
- Le plan d'action en 3 étapes est adapté au secteur
- Le CTA et le footer pointent vers les bons liens
- Le rendu visuel correspond à la référence (gradient, typographie, encadrés)

---

## Premier cas d'application (référence visuelle)

Secteur : agences immobilières à Paris. Page test produite le 2026-05-14. Sortie : 12 listings, 1 174 combinaisons générables (univers, pas cible), 87 notions à couvrir par page, 10 outils interactifs activables, 7 mécaniques de capture annexes.

Fichier de référence : `~/Downloads/test-pseo-agence-immo-paris-v2.html`. À utiliser comme template HTML de base pour les futures applications du pattern.

---

## Secteurs prioritaires à dupliquer ensuite

- SaaS B2B early stage
- Cabinets de conseil B2B (RGPD, RH, fiscal)
- Marketplaces professionnelles
- Services aux entreprises (comptabilité, paie, juridique)
- E-commerce de niche
- Formations et bootcamps spécialisés

---

## Sources et liens

- [[skill-programmatique-pseo]] · skill principal
- [[skill-entites-vectorielles]] · skill cartographie sémantique
- [[skill-product-led-seo]] · skill outils interactifs
- [[2026-04-25-pseo-data-driven-organikk-cursor]] · application initiale Organikk
- [[session-1-mots-cles-prep]] · bootcamp 4 session 1
- [[session-2-redaction-prep]] · bootcamp 4 session 2
- `~/Downloads/test-pseo-agence-immo-paris-v2.html` · première application visuelle du pattern
