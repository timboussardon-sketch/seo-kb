# Interview de cadrage client (batterie + protocole)

> Étape de la roadmap de prestation : **2b. Interview de cadrage** (Phase 0, après la signature et la récup des accès, avant l'analyse GSC de l'étape 3). Sert à une seule chose : que l'agent confirme qu'il a **bien compris le contexte** avant de produire quoi que ce soit. Rien ne se produit tant que le cadrage n'est pas validé par Tim.
>
> Réf : `prestation/roadmap.md` (étape 2b), skill `roadmap-prestation`, skill `seo-pre-audit` (le scan public qui pré-remplit les hypothèses).

## Principe

L'interview n'est pas un questionnaire froid. Avant de poser une question, l'agent a déjà tout ce qui est public (le scan de `seo-pre-audit`). Chaque question part donc d'une **hypothèse** tirée du public, et Tim confirme, corrige ou complète. On cadre en confirmant une compréhension, pas en partant de zéro.

L'interview couvre **tout le contexte** : le business et ses angles (offre qui fait le CA, modèle éco, différenciation), la cible, l'état SEO, la data, l'objectif de mission, la voix, la relation. Rien ne se produit tant que ce contexte n'est pas cadré et validé.

Format : **l'agent interviewe Tim** (pas le client). Interactif, via `AskUserQuestion`, en rounds thématiques (2 à 4 questions par appel). Pour chaque question, l'agent propose 2 à 4 réponses plausibles issues du scan public, et Tim tranche ou répond en libre (« Other »). Une réponse faible ou inconnue devient une **question à poser au client**, jamais une invention.

**Signaler les manques (obligatoire).** Si un document, un accès ou une donnée manque pour cadrer ou pour attaquer la suite (GSC, GA4, transcripts de calls, avis, CRM, cas clients chiffrés, ancienne stratégie, plan de refonte, guidelines de marque), l'agent le **dit explicitement** à Tim : quoi, pourquoi il en a besoin, ce que ça débloque. Il ne comble jamais un trou par une invention. La liste des manques fait partie de la sortie.

## Quand

1. Après la signature et la récup des accès/data (fin d'étape 1).
2. Après le scan public de `seo-pre-audit` (l'agent a formé ses hypothèses).
3. Avant l'analyse GSC (étape 3) : le cadrage oriente ce qu'on cherche dans la data.

## Protocole (4 temps)

1. **Scan public.** Faire tourner la collecte de `seo-pre-audit` (identité, modèle éco, état SEO public, surface GEO, data propriétaire pressentie). Noter la source de chaque fait.
2. **Interview.** Dérouler la batterie ci-dessous par rounds. Chaque round = un `AskUserQuestion` de 2 à 4 questions, options pré-remplies avec les hypothèses du scan, reco en première position quand une hypothèse est solide. Ne pas enchaîner plus d'un round à l'aveugle : adapter les questions suivantes aux réponses reçues.
3. **Restitution (gate).** Rédiger un bloc **« Ce que j'ai compris »** (voir format de sortie), 15 lignes max, factuel, suivi de la liste des **docs/accès manquants** et des questions à poser au client. Faire valider par Tim : « c'est ça le contexte, il me manque ça, je pars là-dessus, ou on corrige ? ». On n'exécute pas l'étape 3 tant que ce n'est pas validé.
4. **Stockage.** Coller la version validée dans `prestation/clients/<slug>.md`, section « Cadrage (interview) », datée. Reporter les manques dans « Accès et data » du tracker.

## La batterie (resserrée, ~20 questions, 8 thèmes)

Chaque question porte l'angle SEO/GEO qu'elle débloque. Ne poser que ce que le scan public n'a pas déjà tranché nettement.

### 1. Business et modèle économique
1. **Offre qui fait le CA.** Quelle offre/produit porte réellement le chiffre d'affaires (vs le catalogue affiché) ? → sur quel terrain on attaque en premier.
2. **Point de conversion réel.** L'action qui compte : devis, démo, prise de RDV, achat, appel ? → vers quoi chaque page renvoie.
3. **Cycle et panier.** Achat court/impulsif ou long/réfléchi, panier moyen ? → intention à cibler (Do rapide vs réassurance longue).

### 2. Cible et décision
4. **ICP prioritaire.** Le persona qui compte le plus (secteur, taille, rôle) ? → angle des clusters.
5. **Qui décide, quel déclencheur.** Qui signe côté client et quelle situation déclenche la recherche ? → requêtes décisionnelles réelles.
6. **Zone et langue.** Géographie et langue de la cible (FR, EU, international, anglais tapé en FR) ? → périmètre pSEO et couche GEO.

### 3. Différenciation et data propriétaire
7. **Angle défendable.** Sur quoi sont-ils durs à attaquer (niche, data propriétaire, intention que l'IA ne mange pas) ? → le pilier d'autorité.
8. **Data propriétaire dispo.** Cas chiffrés, méthodo maison, terrain, chiffres internes disponibles ? → carburant anti-IA et citations IA (à réclamer si absent).
9. **Surprise gap.** Ce que les acteurs du marché (et les IA) ne disent pas et que le client peut dire ? → l'angle original.

### 4. État SEO et historique
10. **Refonte / migration.** Refonte ou migration récente ou en cours ? → préalable technique (301, canonicals, maillage) avant d'empiler du contenu.
11. **Ce qui a marché ou pas.** Actions SEO passées, résultats, agence précédente ? → ne pas refaire, capitaliser ce qui a pris.
12. **Incident connu.** Chute de trafic, pénalité, cannibalisation identifiée ? → priorités défensives.

### 5. Data et accès
13. **GSC / GA4.** Disponibles, sur quelle profondeur d'historique ? → faisabilité de l'étape 3, sinon étape 3 bloquée.
14. **Autres sources.** CRM, avis clients, tickets SAV, transcripts de calls, exports ? → matière pour verbatims, objections, ton de voix.

### 6. Objectif de la mission
15. **KPI de succès.** Ce que le client veut voir bouger (leads entrants, positions, citations IA, CA) ? → on parle résultats, jamais « visibilité ».
16. **Première preuve.** Échéance de la première preuve attendue et horizon de la mission ? → cadence de la roadmap 30/60/90.
17. **Périmètre et contraintes.** Budget de pages, techno du site, qui publie, contraintes techniques ? → ce qui est faisable vs à déléguer.

### 7. Voix et tabous
18. **Ton de voix.** Tutoiement/vouvoiement, registre, exemples de textes de référence du client ? → paramétrage voix pour l'étape 12.
19. **Mots et sujets bannis.** Secteur régulé, contraintes RGPD, mots interdits, sujets à éviter ? → garde-fous de rédaction.

### 8. Contexte relationnel
20. **Maturité et autonomie visée.** Niveau SEO de l'interlocuteur et jusqu'où il veut devenir autonome ? → dosage du « 0 à 1 puis autonomie » et de l'onboarding du bot.
21. **Ce qui serait un échec.** Ce qui rendrait la mission ratée à ses yeux, risque ou objection de fond ? → priorité cachée à sécuriser.

## Format de sortie (à valider puis stocker)

Bloc court, factuel, tutoiement, zéro chiffre inventé. Tout ce qui n'est pas tranché part en « À poser au client ».

```markdown
## Cadrage (interview) — <YYYY-MM-DD>

### Ce que j'ai compris
- Business : <offre qui fait le CA, point de conversion, cycle/panier>
- Cible : <ICP prioritaire, qui décide, déclencheur, zone/langue>
- Angle défendable : <pilier + data propriétaire + surprise gap>
- État SEO : <refonte/migration, historique, incident connu>
- Data dispo : <GSC/GA4, autres sources>
- Objectif : <KPI, première preuve datée, périmètre/contraintes>
- Voix et tabous : <registre, mots bannis, contraintes secteur>
- Relation : <maturité, autonomie visée, ce qui serait un échec>

### Docs / accès qui me manquent
- <doc ou accès> — pour <ce que ça débloque>
- <doc ou accès> — pour <ce que ça débloque>

### À poser au client (non tranché)
- <question 1>
- <question 2>

Validé par Tim le <date>. On enchaîne sur l'étape 3 (analyse GSC).
```

## Garde-fous

- Rien ne se produit avant validation du cadrage : c'est un gate, pas une formalité.
- Aucun chiffre, volume ou position inventé (règle dure de `seo-pre-audit`). Inconnu = « à poser au client ».
- On ne balance pas le diagnostic interne (le « pain ») frontalement au client : il alimente notre stratégie, pas le discours.
- Après édition, proposer `./kb rebuild`.

Statut : doctrine (batterie posée, pas encore éprouvée sur un vrai client).
