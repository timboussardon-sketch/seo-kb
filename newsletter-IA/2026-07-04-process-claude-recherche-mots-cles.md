---
type: doctrine
title: "Newsletter : mon process Claude pour la recherche de mots-clés"
aliases: [newsletter-process-recherche-mots-cles]
tags: [seo, ia, keywords, newsletter, process-claude]
created: 2026-07-04
updated: 2026-07-04
sources: 4
confidence: high
status: draft
---

# Mon process Claude pour la recherche de mots-clés

*Pourquoi je ne pars plus d'un outil de mots-clés, et ce que Claude sort à la place.*

---

## Bloc 1. Le tableau

Tu paies un outil de mots-clés plus de 100 € par mois pour exporter des listes de requêtes. Voici ce qu'il fait, ce qu'il ne fait pas, et ce que Claude fait à sa place.

| Capacité | Outils de mots-clés (Semrush, Ahrefs, Keyword Planner) | Claude (avec process Organikk) |
| --- | --- | --- |
| Part de ton offre et de ton point de conversion pour qualifier chaque requête | Non, part d'une base de requêtes | Oui |
| Classe chaque mot-clé par intention Know-Simple / Know / Do reliée à la page que tu vas créer | Partielle (étiquette d'intention générique, sans lien avec ton offre) | Oui |
| Écarte les requêtes informationnelles que ChatGPT et les AI Overviews répondent à ta place | Non | Oui |
| Va chercher la data marché du jour (tarifs pratiqués, pain points en forum, acteurs en place) pour noter la difficulté | Non, base rafraîchie sur un cycle mensuel | Oui, recherche web en direct |
| Croise la liste avec ta Search Console (les requêtes où tu apparais déjà) | Partielle, import manuel | Oui |
| Regroupe les mots-clés en pages (1 cluster = 1 page) sur le partage de SERP | Partielle, regroupement par mot commun | Oui |
| Vérifie la cannibalisation avec tes pages existantes avant de créer | Non | Oui |
| Score chaque mot-clé sur son potentiel de conversion pour TON offre | Non, tri par volume | Oui, score Proximité × Intention × Faisabilité sur 125 |
| Sort une roadmap : quelles pages en premier, lesquelles ne jamais produire | Non, liste plate en CSV | Oui |

Le tableau dit l'essentiel. Les outils répondent à la question « qu'est-ce que les gens tapent ? ». Claude répond à une question différente : « laquelle de ces requêtes peut devenir un client, et quelle page je crée pour la prendre ? ».

---

## Bloc 2. Le hook

Ouvre le dernier export de mots-clés qu'on t'a livré. Compte les requêtes qui portent un signal de décision : prix, avis, alternative, sans engagement, vs. Tout le reste, ce sont des pages que tu vas payer à produire et dont l'IA donnera la réponse sans clic.

---

## Bloc 3. Le problème

Ce que la plupart des CMO croient : la recherche de mots-clés est un problème d'accès à la donnée. On s'abonne à un outil, on tape la thématique, on exporte 500 lignes triées par volume, on envoie au rédacteur. Job done.

Ce qui se passe vraiment : l'outil est une base de requêtes historiques. Il ne connaît ni ton offre, ni ton point de conversion, ni tes pages existantes. Il trie par volume. Or le volume n'est plus un critère de choix pertinent. Pourquoi ? Parce que les requêtes à gros volume sont massivement informationnelles, et l'informationnel est exactement ce que les moteurs de réponse absorbent en premier. Tu te retrouves à produire les pages les plus chères sur les requêtes qui rapportent le moins.

Le vrai livrable d'une recherche de mots-clés, c'est une liste courte de pages à produire, une liste de pages à ne PAS produire, et l'ordre d'attaque. Aucun export CSV ne contient ces trois décisions.

---

## Bloc 4. Pourquoi c'est urgent

Deux chiffres, deux études.

Quand un AI Overview s'affiche, le CTR de la position 1 chute de 58 % (Ahrefs, décembre 2025). Les sources citées dans la réponse récupèrent en revanche +120 % de clics par impression. La sanction et la récompense se jouent dès le choix des mots-clés, avant la première ligne rédigée.

L'AI Mode de Google traite déjà 40 % des requêtes en réponses synthétisées, pour 1 milliard d'utilisateurs mensuels (Google I/O, mai 2026). Une liste triée par volume te fait viser en priorité les requêtes qui basculent dans ce mode.

Bon. Une recherche de mots-clés qui ignore ces deux données produit une roadmap périmée avant la première page publiée.

---

## Bloc 5. La méthode

Mon process tourne en 5 étapes, chacune portée par un skill Claude distinct.

**Étape 1 : cadrer par l'offre, jamais par la thématique seule.** Avant de générer quoi que ce soit, Claude reçoit l'audience, le point de conversion (démo, audit, panier) et le marché géographique. Une requête sans lien avec le point de conversion sera générée puis écartée, en connaissance de cause.

**Étape 2 : générer large, avec la data du jour.** Expansion sémantique jusqu'à 50 à 150 requêtes brutes : modificateurs, questions type People Also Ask, longue traîne, variantes lexicales. En parallèle, Claude scrape la réalité du marché au moment T : tarifs pratiqués, pain points exprimés en forum, acteurs en place. C'est cette data qui rend la qualification honnête (un outil te donne une difficulté calculée sur des backlinks, pas sur la réalité commerciale du secteur).

**Étape 3 : qualifier chaque requête.** Intention Know-Simple, Know ou Do, difficulté en proxy déclaratif, étage de funnel. Règle maison : aucune colonne Volume dans le livrable. Les volumes restent dans l'outil quand on en a besoin pour arbitrer, ils ne pilotent jamais la sélection. Pas négociable.

**Étape 4 : regrouper en pages.** Deux requêtes qui affichent le même top 10 relèvent de la même intention, donc d'une seule page. Claude vérifie aussi la cannibalisation avec les pages déjà en ligne : un cluster qui recouvre une page existante est tué avant d'exister.

**Étape 5 : scorer et trancher.** Chaque cluster décisionnel reçoit un score Proximité × Intention × Faisabilité sur 125. Sortie en trois tiers : les pages à produire en premier, celles qui deviennent des sections, celles qu'on écarte. La décision finale reste chez moi (Claude propose, je tranche, dans cet ordre).

---

## Bloc 6. La preuve

Fin mai, j'ai passé la thématique « agence SEO » dans ce process pour mon propre projet, Fusionn. Deux sessions de travail. Résultat : 78 mots-clés qualifiés, regroupés en 50 clusters, dont 51 requêtes décisionnelles. Le scoring a sorti 10 pages Tier 1 à produire en premier, 15 sujets rétrogradés en sections, et 27 requêtes écartées : aucune page, jamais. Deux clusters ont été tués avant production parce qu'ils cannibalisaient des pages déjà en ligne. Le mot-clé le mieux scoré (100 sur 125) est une requête « alternative à » sur le nom d'un acteur majeur du secteur : une audience déjà déçue, en décision active, qu'aucun tri par volume n'aurait fait remonter.

Aucun outil du marché ne sort ce livrable. Un process le sort.

Si tu veux voir ce que ça donne sur ta thématique, réponds à ce mail avec ton site et ton point de conversion, je te montre les premières requêtes. Et si tu préfères construire le système chez toi : le process complet tient dans 3 skills Claude que j'installe avec mes clients en accompagnement.

Demain, tout le monde sortira la même liste de 500 requêtes en 30 secondes. La sélection restera le travail. Ne pas avoir peur de l'avenir. Mais le préparer.

---

## Sources (backstage, jamais dans la newsletter publiée)

- Ahrefs, AI Overviews reduce clicks by 58% : https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/
- Search Engine Land, AI Overviews CTR recovery study (+120 % clics/impression pour les sources citées) : https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566
- Google blog, Search I/O 2026 (AI Mode 40 % des requêtes, 1 Md utilisateurs) : https://blog.google/products-and-platforms/products/search/search-io-2026/
- Run réel du workflow : [[keywords/recherche-2026-05-27-agence-seo]] → [[keywords/clustering-2026-05-28-agence-seo]] → [[keywords/decisionnels-2026-05-28-agence-seo]]

## Notes d'édition

- Épisode 2 de la série « Mon process Claude pour... » (plan validé le 2026-07-04). Épisodes déjà publiés : maillage interne, audits sémantiques.
- Profondeur validée : process + teasing (les étapes et la logique en clair, les skills complets réservés à l'accompagnement).
- Le nom de l'acteur cité dans la requête « alternative à » reste anonyme dans la newsletter (règle : pas de nom d'agence dans les contenus mots-clés agence/consultant/outil SEO).
- Format hérité de la newsletter maillage du 2026-05-06 : tableau comparatif en bloc 1, hook coût business, problème, urgence sourcée, méthode racontée, preuve + CTA unique.
- Compte ~1 050 mots hors sources et notes.
