---
title: "Auditer et construire le maillage interne d'un site avec Claude"
slug: maillage-interne-claude
type: brief-ops
date: 2026-05-02
created: 2026-05-02
auteur: Tim Boussardon (Organikk)
category: Agents IA / Architecture éditoriale
keyword: maillage interne IA Claude
readTime: 9 min
status: prêt-à-implémenter
sources_internes:
  - raw/articles/algorithme/newsletter-maillage-interne.md
  - wiki/concepts/maillage-systeme.md
  - wiki/concepts/5-types-ancres.md
  - wiki/concepts/know-simple-know-do.md
  - wiki/syntheses/4-piliers-organikk.md
sources_externes:
  - https://claude.ai/code/skills (interface)
  - https://search.google.com/search-console (matrice de référence)
---

# Auditer et construire le maillage interne d'un site avec Claude

## Objectif

Remplacer 6 à 12 heures d'audit maillage manuel par un skill Claude qui ingère la liste des pages, calcule la matrice de liens existants, identifie les pages orphelines / dead-end / hubs sous-maillés, et propose les liens à créer avec **ancre + type + passage cible**, en respectant les 3 axes (topique, vectoriel, cognitif) et la diversification d'ancres.

Livrable : rapport markdown + plan d'action priorisé (Hub↔Satellite, Know→Do, Cross-pillar, Orphan-rescue).

## Cas d'usage déclencheurs

- Site qui vient de publier 10+ articles sans les mailler entre eux (cas classique du "blog avant maillage")
- Refonte d'un site avec migration d'URLs où le maillage doit être reconstruit
- Audit d'un prospect avant call commercial (preuve de valeur en 30 min)
- Site client en accompagnement où l'on veut garder un graphe sain à chaque nouvelle publication
- Migration depuis un outil tiers (Ahrefs, Semrush) vers un système propriétaire

## Stack technique

| Composant | Rôle | Coût |
|---|---|---|
| Skill [[concepts/maillage-systeme|maillage-systeme]] | Logique propriétaire — 3 axes, 5 ancres, hub/satellite | Plan Pro / Max |
| Skill `maillage-interne-gsc` (optionnel) | Croisement avec données comportementales GSC | Plan Pro / Max |
| Claude Code CLI | Orchestration locale | Plan Pro / Max |
| GitHub repo | SOT des articles + dépôt du rapport + fichier `internal-links.ts` versionné | Gratuit |
| Export GSC (optionnel) | 16 mois pour le scoring `(impressions × intention) + (gain authority × 0.4)` | Gratuit |

Aucun outil tiers payant requis pour la version baseline.

## Architecture

```
1. Inventaire articles (src/data/articles.ts ou liste URLs)
        ↓
2. Skill maillage-systeme : classification piliers + hub/satellite
        ↓
3. Calcul matrice liens existants (parsing contenu)
        ↓
4. Détection orphelines / dead-end / hubs sous-maillés
        ↓
5. Génération suggestions (3 ancres possibles par lien)
        ↓
6. Validation 5 critères + diversification ANCHOR_HISTORY
        ↓
7. Sortie : internal-links.ts mis à jour + rapport markdown
```

## Ce que le skill produit

| # | Sortie | Format | Action humaine |
|---|---|---|---|
| 1 | Classification piliers + intentions | tableau | valider |
| 2 | Identification des hubs (1 par pilier) | liste | valider |
| 3 | Cartographie des liens existants | matrice | lecture seule |
| 4 | Liste pages orphelines / dead-end | tableau | priorité absolue |
| 5 | Suggestions de liens (Hub↔Satellite, Know→Do, Cross-pillar, Orphan-rescue) | tableau avec 3 ancres par cible | choisir 1 ancre |
| 6 | Mise à jour `ANCHOR_HISTORY` | code TypeScript | commit |
| 7 | Plan d'action priorisé | checklist par typologie | exécuter |

## Étapes de mise en place

### 1. Single source of truth des articles

Dans le repo du site, un fichier qui exporte la liste des articles avec leur contenu structuré.

```ts
// src/data/articles.ts
export const articles: Record<string, Article> = {
  'process-seo-b2b-2026': {
    title: '...', sections: [...], category: '...', highlights: [...]
  },
  // 13 autres
}
```

À côté, le fichier qui devient la SOT du maillage — versionné en Git :

```ts
// src/data/internal-links.ts
export const ARTICLE_NODES: ArticleNode[] = [
  { slug, title, pillar: 'strategie', intention: 'know', isHub: true },
  // ...
]
export const ANCHOR_HISTORY: Record<string, AnchorEntry[]> = { ... }
export const FORCED_LINKS: ForcedLink[] = [ ... ]
```

### 2. Installer le skill `maillage-systeme`

```bash
mkdir -p ~/.claude/skills/maillage-systeme
# coller SKILL.md avec frontmatter + instructions
```

Le skill encode :
- Classification [[syntheses/4-piliers-organikk|4 piliers]] + intention [[concepts/know-simple-know-do|Know-Simple/Know/Know-decisionnel/Do]]
- Règle hub : 1 par pilier, isHub=true reçoit le plus de liens entrants
- [[concepts/5-types-ancres|5 types d'ancres]] : exact match (1 max/cible), partial (60-70 %), sémantique étendue, naming/marque, contextuelle longue
- 5 critères de validation par ancre (promesse cible, phrase porteuse, diversification, position, link context)
- Cross-pillar obligatoire : ≥1 lien sortant par pilier vers un autre pilier
- Plafond densité : 5 liens / 1 000 mots

### 3. (Optionnel) Chaîner avec `maillage-interne-gsc`

Si le site a 6 mois+ de Search Console :

```bash
mkdir -p ~/.claude/skills/maillage-interne-gsc
# coller SKILL.md
```

Le second skill ajoute le scoring `(impressions × intention) + (gain authority × 0.4)` pour prioriser les suggestions selon le potentiel business réel, pas seulement la cohérence éditoriale.

### 4. Lancer l'audit

```bash
claude
> /maillage-systeme audit
```

Claude lit `articles.ts`, applique la classification, calcule la matrice, détecte les anomalies, génère les suggestions. Sortie : rapport markdown + diff sur `internal-links.ts`.

### 5. Validation humaine + commit

Pour chaque suggestion proposée :
- Choisir 1 ancre parmi les 3 proposées (selon contexte de la phrase porteuse)
- Vérifier que la phrase d'insertion reste fluide à voix haute
- Commit incrémental : 1 lien par commit pour traçabilité, ou 1 typologie par commit

### 6. Gouvernance à chaque nouvelle publication

À chaque nouvel article, checklist :
- [ ] ≥ 3 liens entrants depuis 3 articles existants
- [ ] ≥ 3 liens sortants vers des articles existants
- [ ] ≥ 1 lien sortant vers une page Do (`/services`, `/outils`, `/contact`)
- [ ] ≥ 1 lien sortant vers un autre pilier (cross-pollination)
- [ ] Aucune ancre exact match dupliquée vers la même cible
- [ ] Tous les liens in-body, aucun en bloc "Voir aussi"

## Variations possibles

### Multi-clients
Un seul skill, plusieurs repos. Adapter le prompt pour pointer sur le `articles.ts` du client en cours. Le ANCHOR_HISTORY reste isolé par projet (commité dans chaque repo).

### Maillage e-commerce (catalogue)
Adapter la classification : pilier = catégorie produit, hub = page catégorie, satellites = fiches produits. Le scoring devient `(impressions × marge produit) + (intention transactionnelle × 0.5)`.

### Maillage local (multi-villes)
Pilier = ville, hub = page ville-mère, satellites = pages services × ville. Cross-pillar = lien entre villes adjacentes (Lyon ↔ Villeurbanne, Paris ↔ Nanterre).

### Audit récurrent automatisé
Combiner avec une routine `schedule` mensuelle qui lance l'audit, génère le rapport, push une PR. Permet de détecter les régressions de maillage après un commit (article ajouté sans liens entrants, hub qui perd ses satellites).

### Maillage multi-langues
Ajouter une dimension "langue" dans le ARTICLE_NODES. Cross-pillar interdit entre langues (l'utilisateur ne saute pas de FR à EN). Maillage hreflang séparé.

## Limites et garde-fous

### Limites techniques
- **Détection des liens existants** : si le contenu est dans une CMS externe (WordPress, Contentful), le parsing demande un crawl HTML. Sur Next.js avec articles en TypeScript, c'est trivial.
- **Diversification ancres** : Claude propose 3 ancres mais peut produire des variations sémantiquement trop proches. Validation humaine reste indispensable sur la diversité.
- **Score d'autorité interne** : sans données GSC, le scoring repose sur des heuristiques (longueur, profondeur de pilier, fraîcheur). Moins précis qu'avec GSC mais utilisable.

### Garde-fous design
- Aucune modification automatique du contenu des articles (Claude génère un diff, jamais d'auto-commit)
- ANCHOR_HISTORY versionné en Git → audit trail complet de chaque ancre choisie
- Limite stricte 1 exact match par cible — bloquant en validation
- Plafond densité 5 liens / 1 000 mots — alerte si dépassé
- Pas de "Voir aussi" automatique : tous les liens sont contextuels, in-body, à un passage précis

> Le maillage est une promesse de continuité que tu fais sur trois canaux d'un coup (Google, LLM, humain). Si l'ancre rate l'un des trois, le lien est gaspillé.

## Sortie attendue

Fichier `reports/maillage-{date}.md` structuré :

```markdown
# Audit maillage interne — 2026-05-02

## Synthèse
- Articles analysés : N
- Liens existants : X
- Liens suggérés : Y
- Pages orphelines : Z
- Pages dead-end : W
- Hubs sous-maillés (< 3 liens entrants) : V
- Cross-pillar manquant : par pilier

## Classification piliers
[Tableau : pilier → articles → hub/satellite → intention]

## Cartographie liens existants
[Matrice : source → target → ancre → type]

## Suggestions de liens (priorisées)
[Tableau : source | target | 3 ancres possibles | type | passage cible]

## Plan d'action par typologie
1. Hub ↔ Satellite (priorité haute)
2. Know → Do (orientation funnel)
3. Cross-pillar (anti-siloïsation)
4. Orphan-rescue (sauvetage des pages isolées)

## Mises à jour ANCHOR_HISTORY
[Diff TypeScript prêt à commit]
```

## Exemple d'output réel

Voici à quoi ressemblerait le rapport généré sur le blog Organikk au 2 mai 2026, avant l'ajout du wiki et après l'audit initial des 14 articles.

---

```markdown
# Audit maillage interne — 2026-05-02

Repo : organikk-next
Articles analysés : 14
Skill : maillage-systeme v1
Durée d'exécution : 9 min 12 s

## Synthèse

- Liens existants : **0** (blog avant maillage — 100 % d'articles orphelins ET dead-end)
- Liens suggérés : **62**
- Pages orphelines : **14 / 14** ⚠️
- Pages dead-end : **14 / 14** ⚠️
- Hubs identifiés : **4** (1 par pilier)
- Hubs sous-maillés (< 3 liens entrants) : **4 / 4** (état initial)
- Cross-pillar manquant : 4 / 4 piliers

## Classification piliers

| Pilier | Hub | Satellites | Intention dominante |
|---|---|---|---|
| Stratégie SEO 2026 | process-seo-b2b-2026 | ma-strategie, roadmap, mots-cles | Know |
| Outils IA & systèmes | 9-skills-seo-claude | wiki-obsidian, audit-claude, creer-bot, agent-simple, grok | Know |
| SEO Local sectoriel | strategie-seo-serrurier-lyon | agence-immobiliere-lyon | Know-decisionnel |
| GEO (sous-cluster) | information-gain-geo | semrush-contenu-ia | Know |

## Cartographie liens existants

```
(matrice vide — aucun lien interne avant audit)
```

## Suggestions de liens (top 20 sur 62)

### Priorité HAUTE — Hub ↔ Satellite (active les cocons)

| Source | Target | Ancre choisie | Type | Passage cible |
|---|---|---|---|---|
| ma-strategie-seo-du-moment | process-seo-b2b-2026 | "le process B2B complet derrière cette stratégie" | partial | "Le résultat condensé de 6 ans..." |
| roadmap-seo-2026 | process-seo-b2b-2026 | "process SEO B2B 2026" | exact | "Roadmap SEO pratique..." |
| mots-cles-seo-2026 | process-seo-b2b-2026 | "ma méthode pour ramener du lead qualifié" | sémantique | (à placer dans la section MVS) |
| audit-seo-claude | 9-skills-seo-claude | "le système de skills que j'utilise" | partial | (intro audit) |
| wiki-ia-obsidian-claude | 9-skills-seo-claude | "la couche d'expertise par-dessus le wiki" | sémantique | (conclusion) |
| creer-bot-ia-seo | 9-skills-seo-claude | "9 skills SEO sur Claude" | exact | (section skills) |

### Priorité HAUTE — Know → Do (orientation funnel)

| Source | Target | Ancre choisie | Type |
|---|---|---|---|
| audit-seo-claude | /services#audit | "demander un audit terrain sous 48h" | sémantique |
| process-seo-b2b-2026 | /services#audit | "audit complet de votre canal d'acquisition" | sémantique |
| information-gain-geo | /outils/analyse-geo | "tester ton information gain sur un échantillon" | sémantique |
| mots-cles-seo-2026 | /outils/simulateur-roi-seo | "calculer le ROI prévisionnel d'un mot-clé" | sémantique |
| strategie-seo-serrurier-lyon | /coaching-seo-lyon | "se faire coacher pour exécuter cette roadmap" | sémantique |

### Priorité MOYENNE — Cross-pillar (anti-siloïsation)

| Source | Target | Ancre choisie | Type |
|---|---|---|---|
| process-seo-b2b-2026 | 9-skills-seo-claude | "l'outillage IA qui exécute cette méthode" | contextuel |
| process-seo-b2b-2026 | information-gain-geo | "information gain SEO" | exact |
| audit-seo-claude | information-gain-geo | "mesurer ce que ton contenu apporte de neuf" | sémantique |
| strategie-seo-serrurier-lyon | process-seo-b2b-2026 | "comment cette méthode tient en SEO local" | sémantique |
| information-gain-geo | semrush-contenu-ia | "l'étude 42 000 URLs sur le contenu IA" | exact |

## Plan d'action par typologie

| Typologie | Nombre | Effort estimé |
|---|---|---|
| Hub ↔ Satellite | 12 | 1h30 (édition contextuelle) |
| Know → Do | 8 | 45 min |
| Cross-pillar | 6 | 30 min |
| Orphan-rescue | 28 | 2h (priorité 2) |
| Sous-cluster GEO | 2 | 10 min |
| Pilier interne (local) | 2 | 10 min |
| **Total** | **62** | **~5h** |

## Mises à jour ANCHOR_HISTORY (extrait diff)

```typescript
// src/data/internal-links.ts
export const ANCHOR_HISTORY: Record<string, AnchorEntry[]> = {
  'process-seo-b2b-2026': [
    { source: 'ma-strategie-seo-du-moment',    anchor: 'le process B2B...', type: 'partial' },
    { source: 'roadmap-seo-2026',              anchor: 'process SEO B2B 2026', type: 'exact' },
    { source: 'mots-cles-seo-2026',            anchor: 'ma méthode pour ramener du lead qualifié', type: 'sémantique' },
    { source: '9-skills-seo-claude',           anchor: 'le process B2B que ces skills servent', type: 'contextuel' },
    { source: 'strategie-seo-serrurier-lyon',  anchor: 'comment cette méthode tient en SEO local', type: 'sémantique' },
  ],
  // ... 13 autres entrées
}
```

## Vérifications de gouvernance (post-audit)

- 0 page orpheline ✅
- 0 page dead-end ✅
- Densité moyenne : 4,4 liens / article (sous le plafond 5/1000 mots) ✅
- 1 exact match max par cible ✅ (vérification automatique sur ANCHOR_HISTORY)
- Cross-pillar activé : 6/6 piliers ont ≥1 lien sortant cross-pillar ✅

## Limites de ce rapport

- Sans GSC en input, le scoring de priorité repose sur des heuristiques éditoriales (longueur, profondeur de pilier). Pour un site avec 6 mois+ d'historique GSC, chaîner avec le skill `maillage-interne-gsc` pour ajouter le scoring `(impressions × intention) + (gain authority × 0.4)`.
- Les passages cibles sont indicatifs ("à placer dans la section MVS") — la position exacte demande validation humaine sur la fluidité.
- L'audit suppose que `articles.ts` reflète le contenu publié à 100 %. Si le CMS modifie le contenu post-build, faire tourner un crawler en amont.
```

---

**Lecture du rapport — 30 secondes pour le décideur** :
- 14/14 orphelins ET dead-end = blog totalement non-maillé, urgence absolue
- 62 liens à créer en ~5h de travail
- Hub identifié pour chaque pilier = architecture claire, pas de débat
- ANCHOR_HISTORY pré-rempli = audit trail prêt pour Git
- Densité finale projetée 4,4/article = sain, pas de spam

C'est exactement ce que le rapport doit produire : un constat brutal sur l'état initial, un plan d'action chiffré, et un fichier TypeScript prêt à commit pour qu'aucune ancre ne soit dupliquée par erreur la prochaine fois.

## Réutilisation client

Pour appliquer ce système à un client en accompagnement :
1. Importer la liste des articles du client dans `articles.ts` (export depuis CMS si besoin)
2. Lancer `/maillage-systeme audit` → 10-15 min sur 50-100 articles
3. Réviser les suggestions en visio avec le client (45 min)
4. Implémenter les 60-80 % de suggestions validées
5. Programmer un audit récurrent mensuel (skill + routine schedule) pour détecter les régressions

Coût marginal par client : ~30 min de setup, ~2h de validation des suggestions. Différenciant majeur en pitch (livrable concret avant signature).
