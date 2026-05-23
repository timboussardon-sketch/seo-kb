---
slug: newsletter-maillage-interne-claude
title: "14 articles, 0 lien interne. Le skill Claude qui a sorti 62 liens en 9 minutes."
author: "Timothée Boussardon"
date_added: 2026-05-02
type: newsletter
audience: cmo
topic: maillage-interne-ia
status: draft
version: v2-skill-claude
supersedes: newsletter-maillage-interne
---

# 14 articles, 0 lien interne. Le skill Claude qui a sorti 62 liens en 9 minutes.

J'ai audité mon propre blog cette semaine. Verdict : 14 articles, 0 lien interne. Pas un. Chaque article était orphelin (aucun lien entrant) et dead-end (aucun lien sortant). Le PageRank ne circulait nulle part. Aucun cocon. Aucune redistribution d'autorité.

Faire ce travail à la main : ouvrir chaque article, trouver les passages où mailler, choisir les ancres une par une, vérifier qu'on ne duplique pas, garder une trace. Compter 6 à 8 heures pour 14 articles. Et ça augmente exponentiellement avec le nombre de pages.

J'ai construit un skill Claude qui fait ça à la place. Il s'appelle `maillage-systeme`. Il a sorti 62 liens structurés en 9 minutes, avec ancre choisie + passage cible + audit trail Git. Je raconte ici ce qu'il fait et comment vous pouvez en avoir un pour votre site.

---

## Pourquoi 0 lien interne, c'est pas un problème "esthétique"

Trois mécanismes algorithmiques cassent simultanément quand votre graphe interne est disjoint.

**1. PageRank interne non distribué.** Le PageRank originel (Page & Brin, 1998) modélise un random surfer qui suit les liens avec une probabilité (1 - d). Le Reasonable Surfer Model (Google patent US 7,716,225) raffine ce calcul en pondérant chaque lien par sa probabilité d'être cliqué — position dans la page, contexte des mots autour de l'ancre, ancre vs URL nue. Sans liens internes, vos pages ne reçoivent que le PageRank capturé par leurs backlinks externes. Aucune redistribution depuis les pages qui en ont accumulé.

**2. Topical authority fragmentée.** Google n'évalue plus la pertinence page par page. Il évalue des clusters thématiques, et c'est le maillage qui matérialise le cluster. Une page satellite mal mailée vers son hub ne bénéficie pas de l'autorité accumulée par le hub sur le mot-clé pilier. C'est mesurable : sur les tests internes, une page satellite passe de la position 18 à la position 5 sur sa requête longue traîne après 5 liens entrants depuis le hub et 2 satellites du même cluster, sans backlink externe ajouté.

**3. Crawl indexation retardée.** Une page orpheline accessible uniquement par sitemap met 3 à 12 semaines à être indexée. Une page avec ≥ 3 inbound links contextuels est généralement indexée sous 72h. Le delta vient de la façon dont Googlebot priorise sa file de crawl : les pages liées depuis des pages déjà crawlées remontent dans la queue.

Les trois effets se cumulent. Un graphe disjoint, c'est 3 leviers SEO neutralisés en même temps.

---

## Ce que le skill fait

Vous lui donnez la liste des articles du site. Il fait 7 choses :

| # | Action | Sortie |
|---|---|---|
| 1 | Classification par pilier + intention (Know / Know-decisionnel / Do) | tableau |
| 2 | Identification du hub par pilier (l'article central) | liste |
| 3 | Cartographie des liens existants | matrice |
| 4 | Détection des orphelines, dead-end, hubs sous-maillés | tableau d'anomalies |
| 5 | Suggestions de liens (Hub↔Satellite, Know→Do, Cross-pillar, Orphan-rescue) | tableau avec 3 ancres possibles par cible |
| 6 | Mise à jour de l'historique des ancres pour éviter les duplications | code TypeScript versionné |
| 7 | Plan d'action priorisé par typologie | checklist |

Pas de "Voir aussi" en bas d'article. Pas de bloc "Articles similaires" automatique. Tous les liens sont contextuels, in-body, à un passage précis avec une raison de cliquer.

> **Screenshot 1** : sortie du skill dans le terminal Claude Code, montrant le tableau de classification des 14 articles en 4 piliers avec hub identifié.

---

## Pourquoi un seul skill ne suffit pas

J'utilisais avant un skill `maillage-interne-gsc` qui exploite la donnée Search Console. Il marche, mais il a 3 trous structurels.

| Trou | Conséquence |
|---|---|
| Pas de notion hub vs satellite | Toutes les suggestions au même niveau, l'autorité ne se concentre nulle part |
| Pas de gradient d'intention | Tu pointes des articles "concept" depuis tes pages "outil" alors que ça doit être l'inverse |
| Pas de mémoire entre articles | Chaque nouvel article ne met pas à jour les anciens pour qu'ils pointent vers lui |

Résultat : du maillage pertinent à l'unité, mais incohérent à l'échelle du blog. J'ai construit `maillage-systeme` pour combler ces 3 trous. Les deux skills se chaînent : architecture éditoriale d'abord, donnée comportementale ensuite.

---

## Les 3 axes que le skill respecte

Un lien interne, ce n'est pas une décoration. C'est une promesse de continuité que vous faites sur trois canaux d'un coup.

| Axe | Lecteur | Critère de validation |
|---|---|---|
| Topique | Google | La cible parle-t-elle du même sujet ? |
| Vectoriel | LLM (embeddings) | L'ancre s'aligne-t-elle mathématiquement avec le passage cible ? |
| Cognitif | Humain | Le lecteur a-t-il envie de cliquer ? |

**Axe topique (Google, modèle BM25 + signaux topicaux).** L'ancre + son contexte des 5 mots avant/après doivent appartenir au champ lexical de la page cible. C'est la composante "classique" — TF-IDF côté source, vérification de cohérence avec le H1 + intro de la cible. Si tu ancres "stratégie de contenu" mais que la cible parle de calcul de ROI, le signal est cassé.

**Axe vectoriel (LLM, embeddings, RAG).** Les LLM génératifs (et donc les Answer Engines : Perplexity, ChatGPT Search, AI Overviews) ne lisent pas votre site comme Google. Ils découpent vos pages en passages, embeddent chaque passage, et matchent contre le vecteur de la requête utilisateur. Le score qui décide d'une citation, c'est la similarité cosinus entre le passage cité et la requête. Une ancre bien ciblée crée un alignement vectoriel : le passage source contient un fragment qui pointe vers la cible, et la cible elle-même est embeddée avec un vecteur proche. Résultat : vos deux pages se renforcent dans l'index vectoriel des Answer Engines. C'est le grounding score.

**Axe cognitif (humain, information scent).** Le concept vient de la théorie du foraging informationnel (Pirolli & Card, Xerox PARC). Le lecteur évalue inconsciemment si un lien va le rapprocher de son objectif — c'est le scent. Une ancre "cliquez ici" a un scent nul. Une ancre qui reformule la promesse de la cible a un scent fort. Le scent gouverne le CTR du lien interne, qui est lui-même un signal repris par le Reasonable Surfer.

Si l'ancre rate l'un des trois, le lien est gaspillé. Une ancre "cliquez ici" rate les trois. C'est pour ça que les 5 types d'ancres ne se valent pas.

---

## Les 5 types d'ancres et leur quota

| Type | Quand l'utiliser | Quota par cible |
|---|---|---|
| Exact match | Première mention, mot-clé pilier exact | **1 max** (bloquant) |
| Partial match | Variation autour du mot-clé pilier | 60-70 % des liens entrants |
| Sémantique étendue | Reformulation de la promesse cible | le reste |
| Naming/marque | Concept que vous avez nommé | à l'unité |
| Contextuelle longue | Liens enfouis, motivés par la curiosité | à l'unité |

Le skill applique ce quota automatiquement. Si vous avez déjà 1 exact match vers une cible, il refuse d'en proposer un second et bascule sur partial.

### Pourquoi le quota et l'ANCHOR_HISTORY versionné

L'over-optimization penalty sur ancres exact match est documentée depuis Penguin (2012) côté backlinks externes. Côté maillage interne, le mécanisme est moins agressif mais le pattern est identique : si 8 articles pointent vers `/services/seo` avec l'ancre exacte "stratégie SEO B2B", Google interprète ça comme du link sculpting manuel et pondère à la baisse chaque occurrence (loi du 1/N appliquée aux ancres dupliquées).

La règle qu'on applique :

- **1 exact match max par cible**, posé sur la première mention contextuelle (la première fois où le terme apparaît dans la phrase porteuse, en respectant le test à voix haute)
- **60-70 % de partial match** : variation naturelle autour du mot-clé pilier ("comment construire une stratégie SEO B2B", "approche SEO orientée business", "méthode SEO pour le B2B")
- **20-30 % de sémantique étendue** : reformulation de la promesse cible sans le mot-clé ("le système qui fait passer une page de la position 18 à la 5")
- **Naming/marque** à l'unité : un concept que vous avez nommé (ex : "Surprise Gap", "process en 8 étapes")
- **Contextuelle longue** à l'unité : ancres enfouies dans une phrase, motivées par la curiosité du lecteur ("ce que j'ai testé sur 14 articles cette semaine")

Sans mémoire d'ancres versionnée, vous repostez les mêmes exacts sans le savoir. Le `ANCHOR_HISTORY` est un objet TypeScript versionné en Git qui trace, pour chaque page cible, l'ensemble des ancres déjà utilisées, leur source, et leur type. Le skill consulte ce fichier avant chaque suggestion. Si l'exact match est déjà posé, il refuse et bascule sur partial. Diff visible dans la PR — vous voyez ce qui change avant de merger.

C'est la même logique qu'un schema versionné en migration de DB. Single source of truth, audit trail, rollback possible.

> **Screenshot 2** : extrait du fichier `internal-links.ts` montrant l'ANCHOR_HISTORY pour la page `process-seo-b2b-2026` — 5 ancres entrantes, 5 types différents, aucune dupliquée.

---

## Hub & Spoke vs graphe distribué

Deux topologies possibles pour un blog SEO. Elles ne se valent pas algorithmiquement.

**Distributed mesh (chaque article lie chaque article).** Vous obtenez un graphe presque complet, in-degree et out-degree élevés partout. Problème : la link equity est distribuée uniformément. Aucune page ne capte plus d'autorité qu'une autre. Sur un cluster de 8 articles où vous voulez positionner le hub sur "stratégie SEO B2B" (la requête business), le hub reçoit autant que les autres satellites — il ne s'impose pas. Google ne sait pas laquelle de vos 8 pages est la cible canonique.

**Hub & Spoke (bipartite hub-satellite).** Le hub reçoit des liens entrants depuis tous les satellites de son pilier (in-degree fort). Le hub redistribue vers les satellites via des liens contextuels in-body (out-degree fort, mais asymétrique : chaque satellite reçoit moins que le hub n'envoie). Résultat : la link equity converge vers le hub, qui devient la page la mieux positionnée du cluster sur le mot-clé pilier. Les satellites bénéficient de la cross-pollination quand le hub redistribue.

Dans un cluster bien construit :
- Le hub a ≥ 5 inbound depuis ses propres satellites
- Chaque satellite a ≥ 1 inbound depuis le hub
- Chaque satellite a ≥ 1 outbound cross-pillar (vers un autre cluster, pour éviter la siloïsation)

C'est la classe d'architecture validée empiriquement par les studies de Backlinko et de Moz sur des clusters de 50+ pages. C'est ce que le skill construit par défaut, en désignant automatiquement le hub via un scoring sur la complétude du contenu et la position business du mot-clé pilier.

---

## Taxonomie d'intention : Know-Simple, Know, Know-décisionnel, Do

L'autre erreur classique : mailler sans gradient d'intention. Le skill applique la taxonomie héritée des Quality Rater Guidelines de Google + le framework AEO.

| Intention | Description | Poids dans le scoring |
|---|---|---|
| Know-Simple | Définition courte, réponse directe | 0.3 |
| Know | Guide approfondi, méthode, comparatif | 0.5 |
| Know-décisionnel | Comparatifs orientés achat, "X vs Y" | 0.8 |
| Do | Outil, simulateur, formulaire, démo, contact | 1.0 |

La règle algorithmique : **le maillage Know → Do passe avant le maillage Know → Know**. Une page qui explique un concept doit toujours pointer vers la page qui permet de l'exécuter. Si vous expliquez "comment auditer un maillage interne" et que vous ne pointez pas vers `/audit-seo`, vous générez du trafic curieux qui ne convertit pas.

Le scoring d'urgence du skill applique ça mathématiquement :

```
Score(lien) = (impressions_cible × poids_intention) + (gain_authority × 0.4)

avec gain_authority = {
  1.0 si la source est un hub,
  0.5 si la source est un satellite déjà bien mailé,
  0.2 sinon
}
```

Sur Organikk, sans data GSC (site jeune), j'ai utilisé un proxy `position_business` à la place des impressions. Les liens Know → Do sortent automatiquement en haut de la priorisation.

---

## Ce que le skill a sorti pour Organikk

| Typologie | Nombre | Rôle |
|---|---|---|
| Hub ↔ Satellite | 12 | Activer chaque cocon |
| Know → Do | 8 | Orienter le funnel vers les pages business |
| Cross-pillar | 6 | Anti-siloïsation, ponts entre piliers |
| Orphan-rescue | 28 | Sauvetage des pages isolées |
| Sous-cluster GEO | 2 | Densifier le sous-cluster GEO |
| Pilier interne (local) | 2 | Connecter les 2 articles SEO local |
| **Total** | **62** | **0 orpheline · 0 dead-end** |

Densité moyenne finale : 4,4 liens par article, sous le plafond de 5/1 000 mots où chaque lien commence à voir son poids dilué par le 1/N (N = nombre total de liens sortants de la page).

Click depth moyenne avant audit : indéfinie pour les orphelines, 1 pour le reste. Click depth moyenne après : 2,1, avec 100 % des pages atteignables en ≤ 3 clics depuis la home.

> **Screenshot 3** : le rapport markdown généré par le skill, ouvert dans VSCode/Obsidian, section "Plan d'action par typologie" avec les 6 typologies et leur effort estimé.

---

## Comment vous en avez un pour votre site (4 étapes)

### Étape 1 — Lister les articles dans le repo

L'agent doit pouvoir lire votre catalogue d'articles sans le deviner. Le plus propre : un fichier source dans le repo qui sert de single source of truth.

Pour Organikk c'est `src/data/articles.ts` :

```typescript
export const articles: Article[] = [
  {
    slug: "process-seo-b2b-2026",
    title: "Process SEO B2B 2026",
    pillar: "seo-b2b",
    intent: "know-decisional",
    keywordTarget: "stratégie SEO B2B",
    excerpt: "...",
    sections: ["...", "..."],
  },
  // ...
]
```

Si vous êtes sur WordPress ou Contentful, exportez la même structure en JSON via API et le skill la consomme — n'importe quel format parsable suffit.

À côté, un fichier `internal-links.ts` qui maintient l'historique des ancres déjà posées :

```typescript
export const ANCHOR_HISTORY: Record<string, AnchorRecord[]> = {
  "process-seo-b2b-2026": [
    { source: "comment-auditer-maillage", anchor: "process SEO B2B", type: "exact" },
    { source: "guide-cocon-semantique", anchor: "approche orientée business", type: "partial" },
    { source: "skill-claude-maillage", anchor: "le système que j'applique sur Organikk", type: "semantic" },
    // ...
  ],
}
```

Versionné en Git. Diff lisible. Rollback possible. Le skill consulte avant chaque proposition.

### Étape 2 — Installer le skill

Sur Mac/Linux :

```bash
mkdir -p ~/.claude/skills/maillage-systeme
# y placer SKILL.md avec frontmatter + instructions
```

Le SKILL.md encode toutes les règles : 3 axes, 5 types d'ancres, hub vs satellite, cross-pillar obligatoire, plafond densité. Vous le configurez une fois, il s'applique sur tous vos clients.

> **Screenshot 4** : le fichier SKILL.md ouvert dans VSCode, montrant le frontmatter (name, description) et les premières règles.

### Étape 3 — Lancer l'audit

Dans Claude Code :

```
/maillage-systeme audit
```

Sortie : rapport markdown avec 7 sections + diff sur le fichier `internal-links.ts` (votre source de vérité versionnée en Git pour l'historique des ancres).

> **Screenshot 5** : terminal Claude Code après lancement de la commande, montrant le déroulé des 7 étapes.

### Étape 4 — Validation et commit

Pour chaque suggestion, le skill vous donne 3 ancres possibles. Vous choisissez celle qui s'insère le mieux dans la phrase porteuse, vous éditez l'article, vous commitez.

Critère qui tranche en cas d'hésitation : l'ancre survivrait-elle à la suppression du lien ? Si la phrase reste informative et que vous pouvez retirer le lien sans rien casser, l'ancre est bonne. Si elle est plaquée, elle est fausse.

> **Screenshot 6** : vue diff GitHub sur un commit qui ajoute 3 liens internes, montrant les changements minimaux dans 3 fichiers articles + 1 update sur internal-links.ts.

---

## La règle que j'applique à chaque nouvelle publication

Une fois le maillage initial fait, il faut une checklist pour ne pas re-glisser vers un graphe disjoint dans 6 mois. Voici celle que j'applique avant chaque mise en ligne :

- [ ] Le nouvel article reçoit ≥ 3 liens entrants depuis 3 articles existants
- [ ] Le nouvel article contient ≥ 3 liens sortants vers des articles existants
- [ ] 1 lien sortant minimum vers une page Do (`/services`, `/outils`, `/contact`)
- [ ] 1 lien sortant minimum vers un autre pilier (cross-pollination)
- [ ] Aucune ancre exact match dupliquée vers la même cible
- [ ] Tous les liens in-body, aucun en bloc "Voir aussi"

Le skill peut tourner mensuellement en routine schedulée (cron `0 1 1 * *`) qui :

- Détecte les nouveaux articles publiés depuis le dernier run
- Vérifie qu'ils respectent la checklist (≥ 3 inbound, ≥ 3 outbound, 1 Know→Do, 1 cross-pillar)
- Détecte les régressions (un article qui passe orphelin parce qu'un lien a été supprimé)
- Génère un rapport Markdown commit en PR sur le repo
- Notifie par email si une régression est détectée

Vous reviewez la PR, vous mergez les suggestions qui collent au contexte. Discipline mensuelle, pas trimestrielle.

---

## FAQ

### Quelle différence avec un outil classique type Linkilo, Link Whisper ou Internal Link Juicer ?

Trois différences structurelles.

| | Plugin WordPress classique | Skill Claude |
|---|---|---|
| Logique | Match sémantique brut entre paragraphes | 3 axes (topique + vectoriel + cognitif), hub/satellite, intention |
| Ancres | Suggestions sans diversification | Quota 5 types + ANCHOR_HISTORY versionné |
| Stack | WordPress only, plugin propriétaire | N'importe quel CMS, code en Git, vous gardez la main |
| Coût | 60 à 300 €/an récurrent | 0 € après setup (Claude Pro inclus) |

L'autre point : un plugin WordPress sort des suggestions sans contexte d'intention. Le skill comprend qu'une page Know doit pointer vers une page Do, pas l'inverse. C'est ce qui distingue un maillage qui convertit d'un maillage qui décore.

### Pourquoi mailler en interne ?

Trois raisons cumulées.

1. **Autorité topique** : Google récompense les sites qui couvrent un sujet en profondeur, pas en largeur. Un cluster bien maillé fait passer une page satellite de la position 18 à la position 5 sur sa requête, sans aucun backlink externe.
2. **Conversion** : 8 liens Know → Do bien placés orientent du contenu informationnel vers vos pages business. Sans ces ponts, le SEO produit du trafic curieux qui ne paye jamais.
3. **Crawl** : Googlebot suit les liens internes pour découvrir les nouvelles pages. Une page orpheline peut mettre 3 mois à être indexée, contre 3 jours quand elle est bien maillée.

### Où je consulte le rapport ?

Dans le repo Git de votre site, fichier `reports/maillage-{date}.md` créé par le skill. Le diff sur `internal-links.ts` arrive dans la même session — vous le commitez si vous validez.

Si vous avez chaîné avec une routine schedulée mensuelle, le rapport arrive en PR GitHub avec notification email. Vous reviewez les suggestions, vous mergez celles qui collent au contexte de chaque phrase porteuse.

---

## La règle non-négociable : human-in-the-loop sur la phrase porteuse

Le skill propose. Vous validez. Vous commitez.

Beaucoup veulent un agent qui ferme la boucle complètement : suggestion détectée → édition automatique → commit auto. C'est la fausse bonne idée pour une raison technique précise.

Le scoring algorithmique du skill (axes topique + vectoriel + cognitif) valide la pertinence d'une ancre dans l'absolu. Il ne valide pas son intégration dans la phrase porteuse spécifique de l'article source. Or c'est la phrase porteuse qui détermine si le lien est lu naturellement ou s'il sonne plaqué. Une ancre placée hors-contexte casse la fluidité, casse le scent, et casse le CTR du lien — donc casse les 3 axes en aval.

Le test à voix haute reste manuel. Vous lisez la phrase porteuse à voix haute, sans le lien. Si elle reste informative et fluide, l'ancre est intégrée. Si elle clopine, l'ancre est plaquée — vous reformulez la phrase ou vous changez l'ancre parmi les 3 propositions.

Discipline : génération côté skill, choix de l'ancre côté humain, exécution dans Git.

C'est ce qui sépare un maillage qui convertit d'un maillage qui décore.

---

*Si vous voulez que je regarde le maillage de votre site et que je vous livre le rapport complet sans engagement, [demandez un audit ici](https://organikk.co/contact). 30 min en visio, je reviens avec le plan complet.*

---

## Annexe — Screenshots à shooter avant publication

1. Sortie skill dans le terminal Claude Code : tableau classification piliers + hubs identifiés
2. Extrait `internal-links.ts` montrant ANCHOR_HISTORY pour `process-seo-b2b-2026`
3. Rapport markdown ouvert dans VSCode/Obsidian, section "Plan d'action par typologie"
4. Fichier SKILL.md ouvert dans VSCode (frontmatter + premières règles)
5. Terminal Claude Code après lancement de `/maillage-systeme audit` (déroulé des 7 étapes)
6. Vue diff GitHub d'un commit ajoutant 3 liens internes (changements minimaux + update internal-links.ts)
