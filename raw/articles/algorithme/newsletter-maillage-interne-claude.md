---
slug: newsletter-maillage-interne-claude
title: "14 articles, 0 lien interne. Le skill Claude qui a sorti 62 liens en 9 minutes."
author: "Timothée Boussardon"
date_added: 2026-05-02
type: newsletter
audience: cmo
topic: maillage-interne-ia
status: draft
---

# 14 articles, 0 lien interne. Le skill Claude qui a sorti 62 liens en 9 minutes.

J'ai audité mon propre blog cette semaine. Verdict : 14 articles, 0 lien interne. Pas un. Chaque article était orphelin (aucun lien entrant) et dead-end (aucun lien sortant). Le PageRank ne circulait nulle part. Aucun cocon. Aucune redistribution d'autorité.

Faire ce travail à la main : ouvrir chaque article, trouver les passages où mailler, choisir les ancres une par une, vérifier qu'on ne duplique pas, garder une trace. Compter 6 à 8 heures pour 14 articles. Et ça augmente exponentiellement avec le nombre de pages.

J'ai construit un skill Claude qui fait ça à la place. Il s'appelle `maillage-systeme`. Il a sorti 62 liens structurés en 9 minutes, avec ancre choisie + passage cible + audit trail Git. Je raconte ici ce qu'il fait et comment vous pouvez en avoir un pour votre site.

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

> **Screenshot 2** : extrait du fichier `internal-links.ts` montrant l'ANCHOR_HISTORY pour la page `process-seo-b2b-2026` — 5 ancres entrantes, 5 types différents, aucune dupliquée.

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

Densité moyenne finale : 4,4 liens par article, sous le plafond de 5/1 000 mots où la dilution s'installe.

> **Screenshot 3** : le rapport markdown généré par le skill, ouvert dans VSCode/Obsidian, section "Plan d'action par typologie" avec les 6 typologies et leur effort estimé.

---

## Comment vous en avez un pour votre site (4 étapes)

### Étape 1 — Lister les articles dans le repo

L'agent doit pouvoir lire votre catalogue d'articles sans le deviner. Le plus propre : un fichier source dans le repo qui sert de single source of truth.

Pour Organikk c'est `src/data/articles.ts` qui exporte un objet `articles` avec slug, title, category, sections, highlights par article. Si vous êtes sur WordPress ou Contentful, exportez la liste en JSON/CSV — n'importe quel format parsable suffit.

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

Le skill peut tourner mensuellement en routine schedulée (cron `0 1 1 * *` par exemple) pour vérifier qu'aucun nouvel article n'a échappé à la checklist. Notification email si une régression est détectée.

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

## La règle que j'applique

Le skill propose. Vous validez. Vous commitez.

Beaucoup veulent un agent qui ferme la boucle : suggestion détectée → l'agent édite l'article → commit auto. C'est la fausse bonne idée. Une ancre placée hors-contexte casse la fluidité de la phrase porteuse, et un lecteur qui clique sur une ancre creuse ne revient pas. La validation humaine sur la phrase porteuse est non-négociable.

Discipline : génération côté skill, choix de l'ancre côté humain, exécution dans Git.

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
