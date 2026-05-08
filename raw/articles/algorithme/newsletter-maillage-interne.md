---
slug: newsletter-maillage-interne
title: "0 → 62 liens internes : comment j'ai maillé mon blog en partant de zéro"
author: "Timothée Boussardon"
date_added: 2026-04-30
source_local: "/Users/boussardontimothee/Downloads/Cursor/organikk-next/newsletter-maillage-interne.md"
type: newsletter
topic: maillage-interne
---

# 0 → 62 liens internes : comment j'ai maillé mon blog en partant de zéro

J'ai audité mon propre blog cette semaine. Verdict : **14 articles, 0 lien interne**. Pas un. Chaque article était orphelin (aucun lien entrant) et dead-end (aucun lien sortant). Le PageRank ne circulait nulle part. Aucun cocon. Aucune redistribution d'autorité.

C'est le scénario classique du "blog avant maillage". Tu publies, tu publies, tu publies, et un jour tu réalises que tes articles vivent en silos. Bonne nouvelle : on construit propre, sans héritage à défaire.

Je raconte ici la méthode que j'ai appliquée, parce qu'elle marche aussi pour les sites de tes clients. **62 liens internes créés**, structurés sur 3 axes, en suivant un skill maison que j'ai documenté.

---

## Pourquoi un seul skill maillage ne suffit pas

J'ai longtemps utilisé un skill `maillage-interne-gsc` qui exploite la donnée Search Console. Il marche, mais il a 3 trous structurels.

| Trou | Conséquence |
|---|---|
| Pas de notion hub vs satellite | Toutes les suggestions arrivent au même niveau, l'autorité ne se concentre nulle part |
| Pas de gradient d'intention | Tu pointes des articles "concept" depuis tes pages "outil" alors que ça doit être l'inverse |
| Pas de mémoire entre articles | Chaque nouvel article ne met pas à jour les anciens pour qu'ils pointent vers lui |

Résultat : du maillage pertinent à l'unité, mais incohérent à l'échelle du blog. J'ai construit un skill complémentaire `maillage-systeme` qui raisonne sur 3 axes simultanés.

---

## Les 3 axes du maillage interne 2026

Un lien interne, ce n'est pas une décoration. C'est une promesse de continuité que tu fais sur trois canaux d'un coup.

| Axe | Lecture par | Critère de validation |
|---|---|---|
| **Topique** | Google (sémantique classique) | La cible parle-t-elle du même sujet ? |
| **Vectoriel** | LLM (embeddings) | L'ancre s'aligne-t-elle mathématiquement avec le passage cible ? |
| **Cognitif** | Humain | Le lecteur a-t-il envie de cliquer ? |

Si l'ancre rate l'un des trois, le lien est gaspillé. Une ancre "cliquez ici" rate les trois. C'est pour ça que les 5 types d'ancres ne se valent pas.

---

## L'architecture : 4 piliers, 4 hubs

J'ai classé mes 14 articles dans 4 piliers thématiques. Pas par catégorie technique : par cohérence sémantique. Chaque pilier a un hub (l'article central) et des satellites (les approfondissements).

### Pilier 1 — Stratégie SEO 2026

| Rôle | Article | Intention |
|---|---|---|
| HUB | Process SEO B2B 2026 | Know |
| Satellite | Ma stratégie SEO du moment | Know-décisionnel |
| Satellite | Roadmap SEO 2026 en 6 étapes | Know |
| Satellite | Trouver les meilleurs mots-clés SEO 2026 | Know-décisionnel |

### Pilier 2 — Outils IA & systèmes pour SEO

| Rôle | Article | Intention |
|---|---|---|
| HUB | 9 skills SEO à installer sur Claude | Know |
| Satellite | Wiki Claude + [[obsidian-as-ide|Obsidian]] | Know |
| Satellite | Audit SEO avec Claude — 7 phases | Know |
| Satellite | Créer un Bot IA pour son SEO | Know |
| Satellite | Premier agent SEO IA | Know |
| Satellite | Grok + SEO pipeline data | Know |

### Pilier 3 — SEO Local sectoriel (émergent)

| Rôle | Article | Intention |
|---|---|---|
| HUB | SEO serrurier Lyon — urgences locales | Know-décisionnel |
| Satellite | SEO agence immobilière Lyon 2026 | Know-décisionnel |

### Sous-cluster GEO (rattaché au Pilier 1, devient pilier autonome au 3e article)

| Rôle | Article | Intention |
|---|---|---|
| Hub provisoire | [[information-gain]] SEO & GEO | Know |
| Satellite | Étude 42 000 URLs — contenu IA & ranking | Know |

**La règle qui m'a guidé** : un cluster avec moins de 3 articles ne devient pas un pilier indépendant. Il reste sous-cluster jusqu'à atteindre la masse critique.

---

## Les 5 types d'ancres (et leur usage)

C'est le cœur de la méthode. Tu ne mets pas l'ancre que tu veux. Tu mets l'ancre qui convient au type de lien et à la diversification.

| Type | Quand l'utiliser | Quota par cible |
|---|---|---|
| **Exact match** | Première mention, mot-clé pilier exact | 1 max |
| **Partial match** | Variation autour du mot-clé pilier | 60-70 % des liens entrants |
| **Sémantique étendue** | Reformulation de la promesse cible | Le reste |
| **Naming/marque** | Concept que tu as nommé | À l'unité |
| **Contextuelle longue** | Liens enfouis, motivés par la curiosité | À l'unité |

**Exemple concret** sur mon blog. La page `process-seo-b2b-2026` (mon hub principal) reçoit 5 liens entrants. Voici la répartition des ancres :

| Source | Ancre | Type |
|---|---|---|
| ma-strategie-seo-du-moment | "le process B2B complet derrière cette stratégie" | partial |
| roadmap-seo-2026 | "process SEO B2B 2026" | exact |
| mots-cles-seo-2026 | "ma méthode pour ramener du lead qualifié" | sémantique |
| 9-skills-seo-claude | "le process B2B que ces skills servent" | contextuel |
| serrurier-lyon | "comment cette méthode tient en SEO local" | sémantique |

Aucune ancre dupliquée. Un seul exact match, sur la première mention. Les 4 autres tirent dans des directions sémantiques différentes pour que Google et les LLM voient une variété naturelle, pas une optimisation industrielle.

---

## Les 5 critères pour valider une ancre

À chaque ancre, je passe ce filtre. Si une ancre rate un critère, je la rejette.

| Critère | Question |
|---|---|
| Promesse cible | L'ancre reflète-t-elle ce que l'utilisateur va trouver, pas le H1 littéral ? |
| Phrase porteuse | La phrase reste-t-elle fluide à voix haute sans le lien ? |
| Diversification | Cette ancre est-elle déjà utilisée vers la même cible depuis ailleurs ? |
| Position | L'ancre porte-t-elle le verbe d'action ou le substantif central ? |
| Link context | Les 5 mots avant/après parlent-ils du sujet de la cible ? |

**Le critère qui tranche en cas d'hésitation** : l'ancre survivrait-elle à la suppression du lien ? Si la phrase reste informative et que tu peux retirer le lien sans rien casser, l'ancre est bonne. Si elle est plaquée, elle est fausse.

---

## Le résultat : 62 liens en 4 typologies

Voici le détail du travail concret sur mes 14 articles.

### Répartition par typologie

| Type de lien | Nombre | Rôle |
|---|---|---|
| Hub ↔ Satellite | 12 | Activer chaque cocon (le hub redistribue, les satellites pointent vers lui) |
| Know → Do | 8 | Orienter le funnel vers les pages business (`/services`, `/outils`, `/coaching`) |
| Cross-pillar | 6 | Anti-siloïsation, ponts entre piliers |
| Sous-cluster | 2 | Densifier le sous-cluster GEO |
| Pilier interne | 2 | Connecter les 2 articles SEO local |
| **Outbound page Do externe** | **2** | Vers `/services#audit`, `/outils/analyse-geo`, `/coaching-seo-lyon` (comptés ailleurs) |

### Bilan par article

| Article | Inbound | Outbound | Statut |
|---|---|---|---|
| 9-skills-seo-claude (HUB P2) | 6 | 6 | ✅ |
| process-seo-b2b-2026 (HUB P1) | 5 | 6 | ✅ |
| information-gain-geo (HUB GEO) | 3 | 2 | ✅ |
| serrurier-lyon (HUB P3) | 2 | 3 | ✅ |
| audit-seo-claude | 1 | 3 | ✅ |
| ma-strategie-seo-du-moment | 1 | 3 | ✅ |
| mots-cles-seo-2026 | 2 | 2 | ✅ |
| roadmap-seo-2026 | 1 | 1 | ✅ |
| wiki-ia-obsidian-claude | 1 | 1 | ✅ |
| creer-bot-ia-seo | 1 | 1 | ✅ |
| agent-seo-ia-simple | 1 | 1 | ✅ |
| grok-seo-pipeline-data | 1 | 1 | ✅ |
| semrush-contenu-ia | 1 | 1 | ✅ |
| agence-immobiliere-lyon | 1 | 1 | ✅ |

**Total : 62 liens internes (32 outbound, 30 inbound).** 0 page orpheline. 0 page dead-end. Densité moyenne 4 liens par article, sous le plafond de 5/1000 mots où la dilution s'installe.

---

## Les 4 leçons pour appliquer ça aux sites de tes clients

**1. Une page mère n'est pas une catégorie technique.**
C'est l'article le plus stratégique du pilier, celui qui définit le vocabulaire et reçoit le plus de liens internes. Sur mon blog, le hub du Pilier 1 n'est pas l'article le plus court ni le plus joli. C'est celui qui contient TOUS les concepts du pilier ([[data-proprietaire|data propriétaire]], mots-clés actionnels, [[programmatique-pseo|programmatique]], [[product-led-seo|Product-Led]], micro-intentions). Les autres approfondissent un aspect.

**2. Le maillage Know → Do passe avant le maillage Know → Know.**
Une page qui explique un concept doit toujours pointer vers la page qui permet de l'exécuter (outil, audit, démo). C'est le levier de conversion le plus négligé. Mes 8 liens Know → Do orientent du contenu informationnel vers `/services#audit`, `/outils/analyse-geo`, `/coaching-seo-lyon`. Sans ces ponts, le SEO produit du trafic curieux qui ne paye jamais.

**3. Pas de "Voir aussi" en bas d'article.**
Le contexte de lien est dilué. Liens contextuels in-body uniquement, dans des phrases naturelles. Sur mon blog, j'ai supprimé tous les blocs "Articles similaires" automatiques au profit de liens éditorialisés à des passages précis. Effet : Google pondère mieux chaque lien, le lecteur clique parce qu'il a une vraie raison.

**4. Le cross-pillar pollination compte autant que le maillage intra-cluster.**
J'ai imposé qu'au moins 1 lien sortant par pilier pointe vers un autre pilier. Sans ça, tu construis des silos thématiques que Google et les LLM ne savent pas relier. Mes 6 liens cross-pillar (process → 9-skills, audit → info-gain, serrurier → process) donnent au moteur un graphe connecté, pas 4 îlots.

---

## La règle de gouvernance que j'applique maintenant

À chaque nouvelle publication d'article, je passe cette checklist avant de mettre en ligne :

- [ ] Le nouvel article reçoit ≥ 3 liens entrants depuis 3 articles existants
- [ ] Le nouvel article contient ≥ 3 liens sortants vers des articles existants
- [ ] 1 lien sortant minimum vers une page Do (`/services`, `/outils`, `/contact`)
- [ ] 1 lien sortant minimum vers un autre pilier (cross-pollination)
- [ ] Aucune ancre exact match dupliquée vers la même cible
- [ ] Tous les liens sont in-body, aucun en bloc "Voir aussi"

C'est ce qui empêche le blog de glisser à nouveau vers un graphe disjoint dans 6 mois.

---

## Pour aller plus loin

Le skill `maillage-systeme` que j'ai construit pour ce travail est documenté ici (gabarit [[cli-tools-optional|Claude Code]], à coller dans `.claude/skills/`). Il fait l'audit du graphe, propose les 3 ancres par lien, prioritise par score `(impressions × intention) + (gain authority × 0.4)`. Une fois calibré sur ton premier client, il tourne en 30 min sur les suivants.

Et si ton site a déjà 6 mois de Search Console, chaîne-le avec `maillage-interne-gsc` : architecture éditoriale d'abord, donnée comportementale ensuite. Les deux ne s'opposent pas, ils se renforcent.

---

*Cette édition documente un cas concret sur mon propre blog. Les mêmes principes s'appliquent en B2B SaaS, e-commerce et SEO local — seuls les KPIs changent. Si tu veux que je regarde le maillage de ton site, [demande un audit ici](https://organikk.co/services#audit) — 30 min en visio, je reviens avec le plan complet.*

---

**Connecté avec :** [[obsidian-as-ide]] · [[information-gain]] · [[data-proprietaire]] · [[product-led-seo]] · [[programmatique-pseo]] · [[cli-tools-optional]]
