---
type: cluster-aeo
projet: qadence
created: 2026-07-16
title: "Cluster AEO — autorité resserrée « chatbot SEO » × « agent SEO » (qadence.io)"
skill: seo-cluster-aeo
statut: cadrage validé Tim — priorités à confirmer
tags: [cluster, aeo, qadence, agent-seo, chatbot-seo, topical-authority]
---

# Cluster AEO — « chatbot SEO » × « agent SEO »

Deux têtes, un seul graphe. Décision Tim du 16 juillet 2026 : l'autorité thématique de qadence.io se construit sur ces deux requêtes et rien d'autre.

## La thèse (ce qui tient tout le cluster)

Un chatbot SEO répond. Un agent SEO va chercher ta donnée, agit, et mesure ce qu'il a fait.

L'écart entre les deux tient en trois choses, et chacune est documentée dans le vault :

1. **L'accès à la donnée réelle.** Le chatbot raisonne sur le corpus moyen, l'agent lit ta Search Console ([[data-proprietaire]]).
2. **La mémoire.** Le chatbot retient des faits courts sur toi (ChatGPT Memory depuis février 2024, Claude Memory plafonnée à 200 lignes / 25 Ko), l'agent tient le dossier du projet : décisions actées, recommandations émises, résultats mesurés ([[memory-llm-vs-wiki-persistant]], [[persistent-wiki-vs-rag]]).

> ⚠️ Formulation interdite sur tout le cluster : « le chatbot repart de zéro à chaque conversation ». [[memory-llm-vs-wiki-persistant]] la marque factuellement fausse et à corriger dans les productions Tim. La distinction correcte est une différence de **finalité** (mémoire pour l'IA vs dossier que tu possèdes), pas de présence.
3. **La boucle de résultat.** Le chatbot recommande et disparaît, l'agent re-mesure sa recommandation à J+14 et J+30 ([[boucle-sortie-mesure]], cron `cron-reco-outcome`).

C'est le pitch produit déjà en prod (« votre partenaire SEO connecté à votre GSC, pas un chatbot qui invente »), transformé en architecture de contenu. Le gradient chatbot → agent est le fil de chaque page.

Conséquence de cadrage : le cluster « chatbot SEO » n'est pas un cluster adverse. C'est la porte d'entrée. Les gens tapent « chatbot SEO » parce que c'est le mot qu'ils connaissent, et on les emmène vers l'agent.

## Périmètre : ce qui entre, ce qui sort

| Entre | Sort |
|---|---|
| Faire son SEO **avec** une IA conversationnelle (chatbot, prompts, ChatGPT/Claude/Gemini pour le SEO) | Être **cité par** les IA : GEO, AEO, AI Overviews, « être visible sur ChatGPT », llms.txt |
| Agents SEO : définition, construction, mémoire, outils, autonomie, branchement GSC | SEO IA au sens large, « outil SEO IA », « référencement IA » |
| Tout ce qui compare chatbot et agent | Les clusters « Comment faire X » de [[strategie-contenu]] (maillage, cannibalisation, Core Web Vitals, brief) |

Cette sortie de périmètre annule de fait les cocons 2, 4, 5 et 6 du fichier [[clusters-2026-07-13-seo-ia-llm-geo]] (SEO ChatGPT « être cité », GEO/AEO, AI Overviews, visibilité IA). Ils restent en réserve, ils ne se produisent pas.

Elle règle aussi l'ambiguïté signalée le 13 juillet entre « chatgpt pour le seo » et « comment utiliser l'ia pour le seo » : les deux tombent sous la tête « chatbot SEO », donc une seule page, sur le hub.

## Les deux piliers

| Page | URL | Requête pivot | Intention | Rôle |
|---|---|---|---|---|
| Pilier A | `/agent-seo` | agent seo | Know | Hub de catégorie. Définit l'agent par ce qu'il fait que le chatbot ne fait pas. |
| Pilier B | `/chatbot-seo` | chatbot seo | Know | Hub d'entrée. Tranche les deux lectures de la requête, assume la limite du format. |
| Pont | `/agent-seo-vs-chatbot-seo` | agent seo vs chatbot seo | Know | Relie les deux hubs. Porte la thèse en entier. |

**Arbitrage à trancher (bloquant).** Le fichier du 13 juillet note que la page d'accueil cible déjà « agent seo ia » en intention Do. Si `/agent-seo` sort en pilier Know sans rien changer, les deux pages se cannibalisent sur la même requête. Recommandation : `/agent-seo` prend la requête générique en Know, la home se recentre sur l'intention transactionnelle et la marque (« essayer Qadence »), et la home devient le Do vers lequel tout le cluster pointe. À valider avant la première publication.

## Cluster A — « agent seo »

| # | Requête cible | Intention | Format | Schema.org | Couverture vault | Priorité |
|---|---|---|---|---|---|---|
| A1 | agent seo search console | Know | Démonstration sur donnée réelle | TechArticle | Forte (entité Qadence, pipeline GSC) | Haute |
| A2 | créer un agent seo | Know | Guide 0 → 1 | HowTo | Forte (2 sources : construire-agent-seo-claude, premier-agent-seo-ia) | Haute |
| A3 | agent seo claude | Know | Guide outillé | HowTo | Forte (refonte Claude 2026-06-13, snapshot code) | Haute |
| A4 | mémoire d'un agent seo | Know | Explication architecturale | TechArticle | Forte (memory-llm-vs-wiki-persistant, 3 régimes `project_memory`) | Haute |
| A5 | agent seo autonome | Know | Cadrage des limites | Article | Forte (agentic-search, 6 agents cron) | Moyenne |
| A6 | que sait faire un agent seo | Know | Tableau des compétences, sorti du corpus des skills | ItemList | Forte (table `skills`, 36 slugs) | Haute |
| A7 | prompt système agent seo | Know | Anatomie d'un prompt système | TechArticle | Forte (tim-prompt-systeme-fusionn, garde-fous Qadence) | Moyenne |
| A8 | agent seo mcp | Know | Explication + branchements | TechArticle | Moyenne (23 fichiers, pas de note dédiée) | Moyenne |
| A9 | agent seo gratuit | Know-Simple | Réponse courte + orientation | FAQPage | Faible (position produit à écrire) | Moyenne |
| A10 | agent seo n8n | Know | Comparaison d'approches | Article | **Trou** (4 fichiers) | Basse |
| A11 | agent seo open source | Know | Panorama | Article | **Trou** (3 fichiers) | Basse |

## Cluster B — « chatbot seo »

| # | Requête cible | Intention | Format | Schema.org | Couverture vault | Priorité |
|---|---|---|---|---|---|---|
| B1 | chatgpt pour le seo | Know | Guide d'usage honnête + limites | HowTo | Forte | Haute |
| B2 | prompt seo | Know | Bibliothèque de prompts sortie des skills | ItemList | Forte (123 fichiers, doctrine skills) | Haute |
| B3 | chatbot seo qui invente des données | Know | Démonstration chiffrée | Article | Forte (data-proprietaire, preuve-atomique, garde-fous) | Haute |
| B4 | analyser sa search console avec un chatbot | Know | Guide + limite du copier-coller | HowTo | Forte (page 01 déjà rédigée, à réancrer) | Haute |
| B5 | faire un audit seo avec chatgpt | Know | Protocole + ce qu'il rate | HowTo | Forte (skill audit_gsc, Jade) | Moyenne |
| B6 | claude pour le seo | Know | Guide outillé | HowTo | Forte (43 fichiers) | Moyenne |
| B7 | gemini pour le seo | Know | Guide outillé | HowTo | Moyenne (86 fichiers, mais surtout de l'ère legacy) | Basse |
| B8 | chatbot seo connecté à ses données | Know | Explication du branchement | TechArticle | Forte (pipeline GSC, kb-search) | Moyenne |
| B9 | chatbot seo gratuit | Know-Simple | Réponse courte + orientation | FAQPage | Faible | Moyenne |

## Pages Do (outils, pas du texte)

| # | Page | Requête servie | Ce que c'est | Schema.org | Priorité |
|---|---|---|---|---|---|
| D1 | `/app` (business page) | agent seo ia, essayer | L'agent branché GSC. Cible de tout le maillage. | WebApplication | Existante |
| D2 | Comparateur chatbot nu ↔ agent branché | agent seo vs chatbot seo | Même question posée aux deux, l'écart s'affiche. Sort du corpus d'évals (`evals/run-evals.mjs`, 10 prompts dorés). | WebApplication | Haute |
| D3 | Générateur de prompt SEO | prompt seo | Le visiteur décrit sa situation, sort un prompt système monté sur les skills. | WebApplication | Haute |
| D4 | Audit GSC gratuit | audit seo avec chatgpt, agent seo gratuit | Connexion GSC, un diagnostic, une action chiffrée. | WebApplication | Moyenne |

D2 est la page la plus défendable du cluster : personne d'autre ne peut la produire, elle repose sur un corpus interne, et elle démontre la thèse au lieu de l'affirmer.

## Maillage interne

```
                    /chatbot-seo  ←→  /agent-seo-vs-chatbot-seo  ←→  /agent-seo
                          ↑                      ↓                        ↑
                    B1…B9 (satellites)          D2               A1…A11 (satellites)
                          ↓                      ↓                        ↓
                    ─────────────────────  /app (Do)  ─────────────────────
```

Règles :

- Chaque satellite pointe vers **son hub** et vers **le Do**. Jamais satellite → satellite sauf dépendance réelle (A4 mémoire → A7 prompt système).
- Le pont est le seul lien horizontal entre les deux hubs. Il porte l'ancre « la différence entre un chatbot SEO et un agent SEO ».
- Know → Do prioritaire sur Know → Know ([[know-simple-know-do]], [[maillage-systeme]]).
- Ancres diversifiées, jamais l'exact match répété ([[5-types-ancres]]).
- Chaque page se termine par le même renvoi que le reste du système Qadence : l'agent fait ça sur ton site, avec ta Search Console.

## Roadmap

| Mois | Ce qui sort | Pourquoi dans cet ordre |
|---|---|---|
| Mois 1 | Piliers A et B + le pont + D2 | Les trois pages qui portent la thèse, plus l'outil qui la prouve. Sans elles, les satellites n'ont nulle part où pointer. |
| Mois 2 | A1, A2, A3, A4, A6 + B1, B3, B4 | Les 8 satellites à couverture vault forte et à proximité business directe. |
| Mois 3 | B2 + D3, puis A5, A7, B5, B6, B8 + D4 | La paire prompt SEO (page + générateur) sort ensemble, sinon la page Know n'a pas de Do. |
| Réserve | A8, A9, B7, B9 | Se produisent quand la matière existe. |
| Écarté | A10, A11 | Trou vault. Tant que Tim n'a pas écrit la matière, la page serait du corpus moyen. |

## Ce qui reste ouvert

1. **Home vs `/agent-seo`** : arbitrage de cannibalisation à trancher avant la première ligne (voir plus haut).
2. **Le SERP overlap n'est pas vérifié.** Les regroupements ci-dessus sont une hypothèse d'intention. Trois paires sont à contrôler en priorité : A2 ↔ A3 (créer un agent seo / agent seo claude), B1 ↔ B5 (chatgpt pour le seo / audit seo avec chatgpt), A9 ↔ B9 (les deux « gratuit »). Si les SERP se recouvrent, on fusionne.
3. **Règle des 70 %** ([[corpus-avant-pages]]) : la colonne couverture vault est un comptage de fichiers, pas une lecture. Chaque page se re-vérifie au moment de la produire, et une couverture faible annule la page au lieu de la remplir au corpus moyen.

## Concepts liés

[[agentic-search]] · [[data-proprietaire]] · [[memory-llm-vs-wiki-persistant]] · [[persistent-wiki-vs-rag]] · [[boucle-sortie-mesure]] · [[know-simple-know-do]] · [[maillage-systeme]] · [[surprise-gap]] · [[grounding-score]] · [[entities/qadence-seo-agent]] · [[Corpus-Qadence]] · [[strategie-contenu]] · [[clusters-2026-07-13-seo-ia-llm-geo]]
