---
title: "Roadmap SEO client 30/60/90 (skill distribuable + pédagogie)"
bootcamp: 4
semaine: 4
type: skill-distribuable
usage: "Bundle Drive. Skill distribuable. Roadmap SEO 30/60/90 en 2 phases (transac/décisionnel d'abord, info bas de funnel ensuite), doctrine anti-ChatGPT. Sortie pensée pour présentation prospect / proposition commerciale. SKILL.md sans dépendance vault."
related:
  - "[[skill-preparation-semantique]]"
  - "[[skill-donnees-structurees]]"
  - "[[skill-core-web-vitals]]"
  - "[[skill-workflow-mots-cles]]"
  - "[[skills-checklist-bootcamp4]]"
---

# Le skill qui transforme une liste de mots-clés en plan de prod vendable

Salut à tous,

Ce skill, c'est ta roadmap client. Tu lui donnes une thématique (ou une liste de mots-clés déjà qualifiée) et la Money Page de ton client, il te sort un calendrier de production sur 90 jours, découpé en deux phases, présentable tel quel en rendez-vous commercial. Pas un tableau de mots-clés brut : un plan d'action daté que ton prospect comprend et sur lequel il peut signer.

## La logique en 2 phases (le coeur du skill)

- **Phase 1 — transactionnel et décisionnel d'abord.** Les pages qui convertissent. Celles qui paient le SEO dès le premier mois. C'est ce qu'on produit en priorité, parce que c'est ça qui justifie le budget aux yeux du client.
- **Phase 2 — informationnel bas de funnel ensuite.** Les pages proches de la décision qui alimentent Phase 1 par maillage interne. Jamais d'informationnel pur (définitions, comparatifs génériques) : ça se fait manger par ChatGPT et les AI Overviews, c'est de l'effort gratuit.

L'ordre n'est pas négociable. Si tu commences par l'informationnel, tu fabriques de l'autorité que tu ne monétises pas, et le client ne voit pas de retour. Phase 1 d'abord, toujours.

## Pourquoi c'est un skill commercial

La sortie est faite pour être montrée à un prospect en RDV de découverte. Synthèse exécutive en tête, tableaux propres par mois, et une section "mots-clés rejetés" qui explique au client pourquoi on ne produit PAS certaines pages. Cette section vaut de l'or en vente : elle prouve que tu ne factures pas du volume au kilo, que tu protèges son budget contre les pages que l'IA va dévorer. C'est ton argument anti-agence-qui-pond-200-articles-inutiles.

## Le piège à éviter

Pas de roadmap sans Money Page identifiée. Si ton client ne sait pas où il convertit (quelle page, quel point de conversion), le skill bloque et te le fait poser. Un calendrier de production sans point de conversion, c'est un planning d'effort gratuit. Tu dois savoir où l'argent rentre avant de planifier ce qui amène le trafic.

Autre piège : les volumes. Le skill n'invente jamais un volume de recherche. Si tu ne lui donnes pas la data (GSC, Ahrefs, Semrush), il met `[À SOURCER]` et te le signale. Ne présente pas une roadmap avec des volumes inventés à un client, ça se retourne contre toi dès qu'il vérifie.

## Les 2 modes

- **Mode thématique** : tu donnes juste une thématique + la Money Page, le skill appelle `seo-recherche-mots-cles` en interne pour générer la liste, puis sort la roadmap.
- **Mode liste** : tu as déjà une liste de mots-clés qualifiée (par exemple sortie du workflow mots-clés S3), tu la donnes directement, il la découpe en 2 phases et la cale dans le calendrier.

Le skill détecte le mode tout seul selon ce que tu lui passes.

---

## Procédure d'install / vérification

Vraie nouvelle install, un seul fichier.

1. Dossier `~/.claude/skills/seo-roadmap-pseo/`
2. `SKILL.md` = le bloc entre `=====` ci-dessous
3. Relance Claude, vérifie avec `/skills` (tu dois voir `seo-roadmap-pseo`)

Déclenchement : il part dès que tu dis "roadmap SEO", "roadmap 90 jours", "calendrier de production SEO", "plan d'action SEO 30 60 90", "par où commencer en SEO", "quelles pages produire en premier", "roadmap pour un prospect", "proposition commerciale SEO", ou tu l'appelles avec `/seo-roadmap-pseo`.

Premier essai conseillé : lance-le en mode thématique sur le secteur d'un client réel, avec sa Money Page. Tu verras la sortie que tu peux mettre dans une proposition commerciale dès aujourd'hui.

=====

---
name: seo-roadmap-pseo
description: |
  Construit une roadmap SEO 30/60/90 jours à partir d'une thématique ou d'une liste qualifiée de mots-clés. Découpe la production en deux phases : Phase 1 (transactionnels + décisionnels — les pages qui paient le SEO et qui ne se font pas manger par les LLMs) puis Phase 2 (informationnels bas de funnel qui alimentent le maillage vers Phase 1). Doctrine anti-ChatGPT : on ne produit pas pour des requêtes qu'un AI Overview va dévorer.

  Pipeline en 5 étapes : cadrer la Money Page + point de conversion → importer/générer la liste de mots-clés → classifier en 2 phases avec filtre anti-LLM → prioriser chaque phase par (volume × conversion × faisabilité) → calendrier 30/60/90 avec rythme de production réaliste. Sortie : un livrable lisible par un prospect.

  Deux modes acceptés : input = thématique brute (le skill appelle `seo-recherche-mots-cles` en interne) OU input = liste déjà qualifiée (intent / volume / difficulté).

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "roadmap SEO", "roadmap 90 jours", "roadmap pSEO", "calendrier de production SEO", "plan d'action SEO 30 60 90", "phasage production contenu", "par où commencer en SEO", "quelles pages produire en premier", "roadmap pour un prospect", "proposition commerciale SEO".

  Skill de conversion / commercial : la sortie est conçue pour être présentée en RDV de découverte ou en proposition commerciale. Distinct de `seo-programmatique-pseo` (qui conçoit les MODÈLES de pages scalables) et de `seo-modeles-pseo` (qui sort les modèles de Spokes autour d'une Money Page). Ici on séquence la production dans le temps.
---

# Skill — Roadmap SEO pSEO 30/60/90

## Quand déclencher

Construire une roadmap de production SEO sur 3 mois pour un site, un client ou un prospect. Objectif : transformer une thématique ou une liste de mots-clés en un calendrier de pages à produire, classées en deux phases, présentable tel quel à un décideur.

## Doctrine

- **Une roadmap SEO 2026 ne produit pas d'informationnel pur.** L'informationnel pur (définitions, comparatifs génériques, simulateurs sans data propriétaire) se fait manger par ChatGPT et les AI Overviews. Toute page de la roadmap doit soit convertir directement, soit nourrir une page qui convertit par maillage interne.
- **Deux phases, dans cet ordre, jamais l'inverse.** Phase 1 = transactionnels et décisionnels (les pages qui paient le SEO). Phase 2 = informationnels bas de funnel qui alimentent Phase 1 par maillage interne. Si tu commences par Phase 2, tu fabriques de l'autorité que tu ne monétises pas.
- **Pas de roadmap sans Money Page identifiée.** Si l'utilisateur ne sait pas où il convertit, le skill bloque et exige la réponse. Un calendrier sans point de conversion est un calendrier d'effort gratuit.
- **Pas de volumes inventés, pas de conversion hallucinée.** Si les volumes ne sont pas dans la liste fournie, placeholder `[À SOURCER]`. Si la conversion ne peut pas être estimée depuis la donnée client, placeholder `[À ESTIMER]`. Ne jamais combler avec une moyenne sectorielle générique.
- **Rythme de production réaliste.** 3 à 5 pages par semaine maximum si une équipe d'1 à 2 rédacteurs. Au-delà, on bascule sur du pSEO scalable (cf. `seo-programmatique-pseo`).

## Input requis

| Source | Obligatoire | Défaut |
|--------|-------------|--------|
| URL ou nom du site + secteur | Oui | — |
| Money Page (l'URL qui convertit, ou la page de conversion à créer) | Oui | — |
| Point de conversion (achat, lead, prise de rendez-vous, inscription, etc.) | Oui | — |
| Persona principal | Oui | — |
| Mode A : Thématique brute (2-3 phrases) | Oui en mode A | — |
| Mode B : Liste de mots-clés qualifiée (intent / volume / difficulté) | Oui en mode B | — |
| Capacité de production (pages/semaine, taille équipe rédac) | Recommandé | 3 pages/semaine |
| Données propriétaires disponibles (catalogue, FAQ, cas clients, chiffres) | Recommandé | — |

## Pipeline (5 étapes)

### Étape 1 — Cadrer la Money Page et le point de conversion

Avant toute prod, on verrouille le point d'arrivée. Sans Money Page identifiée, on bloque.

Demander explicitement à l'utilisateur si pas fourni :
- Quelle URL convertit aujourd'hui ? (ou quelle URL va être créée pour convertir si le site n'a pas encore de page commerciale dédiée)
- Quel est le point de conversion mesurable ? (achat, lead, rendez-vous, inscription, devis)
- Quelle est l'offre vendue depuis cette page ? (en une phrase claire)
- Quel est le persona qui convertit ? (B2B / B2C, taille d'entreprise, niveau de maturité)

Si l'utilisateur dit "je ne sais pas" sur la Money Page → arrêter, lui demander de définir d'abord. Une roadmap sans Money Page n'a pas de sens.

### Étape 2 — Importer ou générer la liste de mots-clés

**Mode A — Thématique brute fournie** : appeler `seo-recherche-mots-cles` en interne avec la thématique + secteur + persona + offre. Récupérer la liste de 50 à 150 mots-clés qualifiés (intent / volume / difficulté). Continuer avec cette liste.

**Mode B — Liste qualifiée fournie** : valider la forme. La liste doit avoir minimum 3 colonnes : mot-clé, intent (Know-Simple / Know / Do), volume. Si une colonne manque, le skill demande à l'utilisateur de compléter (typiquement il manque l'intent → le skill peut le qualifier lui-même, voir Étape 3).

Cas dégradé Mode B : si la liste a moins de 30 mots-clés, suggérer d'enrichir via `seo-recherche-mots-cles` avant de continuer. 30 mots-clés c'est en-dessous du seuil utile pour découper en deux phases proprement.

### Étape 3 — Classifier en 2 phases avec filtre anti-LLM

Pour chaque mot-clé, le ranger dans une des trois catégories :

**Phase 1 — Transactionnel + Décisionnel** : tout ce qui signale une intention d'achat ou de prise de décision commerciale.
- Intent = Do (achat, devis, inscription, contact)
- Modificateurs décisionnels : "tarif X", "prix X", "X près de moi", "X [localité]", "comment acheter X", "comparatif X spécifique au marché", "meilleur X pour [persona précis]", "X pour [contrainte forte]", "X avis", "X retour d'expérience"
- Marqueur fort : le chercheur est prêt à signer ou à demander un devis. Le mot-clé exprime un besoin concret, contextualisé.

**Phase 2 — Informationnel bas de funnel** : informationnel mais proche de la décision, qui alimente Phase 1 par maillage interne.
- Intent = Know mais avec contraintes spécifiques
- Modificateurs BoFu informationnels : "comment choisir un X", "X pour [contrainte précise]", "X selon [critère]", "quand utiliser X", "X vs Y dans le cas spécifique de Z", "erreurs à éviter avec X", "checklist X"
- Marqueur fort : le chercheur n'achète pas tout de suite mais cadre sa décision. Il converge.

**Rejet — Informationnel pur / mangé par LLM** : à exclure de la roadmap, à signaler explicitement dans le rapport.
- Définitions génériques ("qu'est-ce que X", "définition X")
- Comparatifs sans contexte ("X vs Y" sans niche)
- Simulateurs / calculateurs génériques sans data propriétaire
- "Comment X" sans complément spécifique (= tutoriel basique)
- Tout ce qu'un AI Overview résume en 3 phrases et dont la SERP montre déjà des AI Overviews actifs

**Filtre supplémentaire** : croiser avec la mention "AI Overview actif" si l'info est disponible (recherche web Claude). Une requête avec AI Overview actif et intent = Know-Simple = rejet automatique.

Si plus de 80% de la liste tombe en "rejet" → alerter l'utilisateur : son input est trop informationnel pur, la roadmap n'a pas de carburant transactionnel. Soit l'offre n'a pas de demande directe (problème plus profond que le SEO), soit la liste de mots-clés a été générée sans angle commercial. Ne pas continuer mécaniquement, dire ce qui ne va pas.

### Étape 4 — Prioriser à l'intérieur de chaque phase

Pour chaque mot-clé conservé (Phase 1 et Phase 2), calculer un score de priorité sur 4 critères :

| Critère | Échelle | Poids |
|---------|---------|-------|
| Volume mensuel | 0-3 (3 = >1000, 2 = 100-1000, 1 = 10-100, 0 = <10 ou inconnu) | ×2 |
| Force de l'intent (transactionnel/décisionnel/BoFu) | 0-3 (3 = Do net, 2 = décisionnel, 1 = BoFu, 0 = limite) | ×3 |
| Potentiel conversion (estimation depuis offre + persona) | 0-3 (3 = match parfait offre, 2 = match large, 1 = match indirect) | ×2 |
| Faisabilité production (donnée propriétaire dispo, complexité contenu) | 0-3 (3 = data prête, 2 = à collecter facile, 1 = à produire from scratch, 0 = bloquant) | ×1 |

Score = (volume × 2) + (intent × 3) + (conversion × 2) + (faisabilité × 1). Max = 24.

Trier les mots-clés de Phase 1 par score décroissant. Idem Phase 2. C'est l'ordre de production.

Si le volume est `[À SOURCER]` → noter 1 par défaut (moyen) et marquer la ligne pour estimation manuelle ultérieure. Ne pas inventer.

### Étape 5 — Calendrier 30/60/90 jours

Étaler la production selon le rythme déclaré (défaut : 3 pages/semaine = 12 pages/mois).

**Mois 1 (Jours 1 à 30) — Phase 1 prioritaire** :
- Produire les 8 à 12 premiers mots-clés Phase 1 (les plus scorés)
- Cible : pages qui peuvent convertir dès leur publication
- Côté technique : balisage propre (Article + FAQ si applicable, cf. `seo-donnees-structurees`), maillage entrant depuis la Money Page existante si déjà là
- Côté contenu : 1 passage ancré 150-200 mots et 1 bloc authorship 50 mots par page (Grounding Score, cf. `seo-workflow-article`)

**Mois 2 (Jours 31 à 60) — Fin Phase 1 + démarrage Phase 2** :
- Finir le reste des mots-clés Phase 1 prioritaires (jusqu'à épuisement du score >12)
- Démarrer Phase 2 : les pages info BoFu qui pointent vers les pages Phase 1 produites au Mois 1
- Côté maillage : chaque page Phase 2 publiée dans ce mois doit pointer vers au moins 2 pages Phase 1 produites au Mois 1 (sinon elle ne sert pas la conversion)

**Mois 3 (Jours 61 à 90) — Bulk Phase 2** :
- Produire le reste de Phase 2 (informationnel BoFu)
- Côté maillage interne : compléter le réseau, vérifier qu'aucune page Phase 1 n'est orpheline et que chaque page Phase 2 alimente bien Phase 1
- Côté mesure : début des premiers signaux GSC (positions, impressions) sur les pages Mois 1, ajuster Mois 4+ en conséquence

**Garde-fou rythme** : si le score total impose plus de pages que le rythme déclaré × 12 semaines, signaler l'écart à l'utilisateur. Ne pas réduire la liste mécaniquement, montrer la queue de priorité et proposer soit (a) d'augmenter la capacité de production, soit (b) de basculer un pan en pSEO scalable (cf. `seo-programmatique-pseo`).

## Output obligatoire

Format markdown, livrable tel quel à un prospect ou à une équipe interne.

```markdown
# Roadmap SEO 30 / 60 / 90 — [Nom du site] — [date]

**Money Page** : [URL ou page à créer]
**Point de conversion** : [achat / lead / RDV / inscription]
**Persona ciblé** : [persona]
**Capacité de production déclarée** : [X pages/semaine]

## Synthèse exécutive (5 phrases)

[Résumé du plan : nombre total de pages, équilibre Phase 1 / Phase 2, premier mot-clé à attaquer, signal attendu fin Mois 1, signal attendu fin Mois 3]

## Mois 1 (Jours 1-30) — Phase 1 prioritaire

Objectif : poser les pages qui peuvent convertir dès publication.

| Semaine | Mot-clé | Intent | Volume | Score | Type de page | Donnée propriétaire requise |
|---------|---------|--------|--------|-------|--------------|----------------------------|
| S1 | [mot-clé #1] | Do | [vol] | [score] | [type] | [donnée] |
| S2 | ... | ... | ... | ... | ... | ... |

Total Mois 1 : [N] pages

## Mois 2 (Jours 31-60) — Fin Phase 1 + démarrage Phase 2

Objectif : finir les pages décisionnelles, démarrer le maillage Phase 2 vers Phase 1.

| Semaine | Mot-clé | Phase | Intent | Volume | Score | Pointe vers (page Phase 1 du Mois 1) |
|---------|---------|-------|--------|--------|-------|--------------------------------------|
| S5 | ... | 1 | ... | ... | ... | — |
| S6 | ... | 2 | Know BoFu | ... | ... | [URL page Phase 1] |

Total Mois 2 : [N] pages

## Mois 3 (Jours 61-90) — Bulk Phase 2

Objectif : compléter le maillage informationnel BoFu vers les pages Phase 1.

| Semaine | Mot-clé | Intent | Volume | Score | Pointe vers (page Phase 1) |
|---------|---------|--------|--------|-------|----------------------------|
| S9 | ... | Know BoFu | ... | ... | [URL] |

Total Mois 3 : [N] pages

## Mots-clés rejetés (informationnel pur / mangé par LLM)

Ces mots-clés ne sont pas produits. Ils déclenchent des AI Overviews ou seraient absorbés par ChatGPT : produire ces pages = effort perdu.

| Mot-clé | Raison du rejet |
|---------|-----------------|
| ... | AI Overview actif sur la SERP |
| ... | Définition générique, sans angle propriétaire |

## Indicateurs de suivi

- Fin Mois 1 : pages Mois 1 indexées, premières positions GSC (généralement 50-100), pas encore de clics
- Fin Mois 2 : pages Mois 1 en position 20-50, premières impressions, signaux maillage internes en place
- Fin Mois 3 : pages Mois 1 en position 10-30 si Phase 1 bien ciblée, premiers clics, première conversion mesurable

À recalibrer dès la première mesure GSC réelle. Ces fourchettes sont des ordres de grandeur, pas des promesses.

## Au-delà des 90 jours

- Pages Phase 1 sous-performantes après 90 jours → passer en `seo-quick-win` (positions 3-12 avec gap CTR)
- Nouveaux mots-clés à ajouter → boucler avec `seo-recherche-mots-cles` + relancer ce skill
- Si volume scalable détecté (>50 pages potentielles sur un même template) → basculer en `seo-programmatique-pseo`

---

*Roadmap construite sans donnée concurrentielle scrappée et sans volume inventé. Les volumes marqués `[À SOURCER]` doivent être complétés depuis GSC / Ahrefs / Semrush avant exécution. Méthodologie : doctrine 2 phases anti-ChatGPT — Phase 1 transactionnel/décisionnel d'abord, Phase 2 informationnel BoFu en alimentation.*
```

## Règles absolues

- **Pas de roadmap sans Money Page identifiée.** Si l'utilisateur ne peut pas la nommer, stopper et exiger la réponse. Une roadmap sans point de conversion = effort gratuit.
- **Pas d'informationnel pur dans le plan.** Catégorie "rejet" obligatoire dans l'output. Si l'utilisateur insiste pour produire de l'informationnel pur, expliquer pourquoi c'est consommé par les LLMs et refuser de le mettre dans la roadmap (le mettre dans une section "à reconsidérer" si vraiment l'utilisateur force).
- **Pas de volume inventé.** Placeholder `[À SOURCER]` obligatoire si la donnée n'est pas dans la liste fournie. Le scoring utilise alors un volume neutre (1) et la ligne est marquée pour estimation manuelle.
- **Pas de conversion hallucinée.** L'estimation de potentiel de conversion vient de l'offre du client + de son persona, jamais d'une moyenne sectorielle générique. Si l'offre n'est pas claire, placeholder `[À ESTIMER]`.
- **Phase 1 toujours avant Phase 2.** L'inverse fabrique de l'autorité non monétisée. Si l'utilisateur veut commencer par Phase 2, expliquer pourquoi c'est faux puis lui laisser le choix.
- **Pas de calendrier irréaliste.** 3 à 5 pages/semaine maximum en rédaction manuelle. Au-delà, c'est du pSEO scalable, on bascule de skill (`seo-programmatique-pseo`).
- **Chaque page Phase 2 maille vers au moins 1 page Phase 1.** Une page Phase 2 sans lien sortant vers Phase 1 est une page Phase 2 qui ne sert pas la conversion : la signaler dans le rapport.

## Edge cases

- **Money Page pas encore créée** : OK, on l'inclut comme première livraison du Mois 1 (avant les pages SEO). Le calendrier devient : S0 (avant J1) = créer la Money Page, S1+ = pages SEO.
- **Aucun mot-clé transactionnel/décisionnel dans la liste** : alerter, refuser de produire. Le problème est plus profond que le SEO (l'offre ou l'audience n'a pas de demande directe).
- **Plus de 80% d'informationnel pur dans la liste** : alerter, refuser de produire sans réviser la liste. Soit l'angle commercial manque, soit la recherche de mots-clés a été générée sans cadrage offre.
- **Liste avec moins de 30 mots-clés** : suggérer d'enrichir via `seo-recherche-mots-cles` avant de produire la roadmap. En dessous de 30, le découpage 2 phases manque de matière.
- **Capacité de production non déclarée** : utiliser 3 pages/semaine par défaut et le signaler dans l'output (hypothèse explicite).
- **Site existant avec contenu déjà publié** : croiser avec un export GSC pour éviter de produire des pages qui rankent déjà (cannibalisation potentielle, cf. `seo-cannibalisation`).
- **Prospect en RDV de découverte (livrable commercial)** : la sortie doit être lisible par un non-SEO. Garder les tableaux propres, mettre la synthèse exécutive en tête, expliquer le rejet informationnel pur dans le ton "pourquoi on ne fait pas ça" (pédagogique, pas technique).

## Concepts liés

`pseo` · `decisionnel-vs-informationnel` · `anti-chatgpt` · `money-page-and-spokes` · `maillage-interne` · `surprise-score` · `grounding-score` · `quick-win`

## Skills voisins (à appeler ou à enchaîner)

- `seo-recherche-mots-cles` — en amont mode A (génère la liste)
- `seo-clustering-mots-cles` — en amont si l'utilisateur veut regrouper par page avant de roadmaper
- `seo-mots-cles-decisionnels` — pour affiner l'isolation Phase 1 si la liste est ambiguë
- `seo-programmatique-pseo` — en aval si la roadmap révèle des templates scalables (>50 pages sur un même pattern)
- `seo-modeles-pseo` — pour les Spokes décisionnels autour de la Money Page
- `seo-quick-win` — pour la mesure des pages Mois 1 après 90 jours
- `seo-cannibalisation` — pour vérifier en amont qu'aucune page ne ranke déjà sur les mots-clés ciblés

## Sauvegarde

Output dans `wiki/roadmaps/roadmap-YYYY-MM-DD-{slug-client}.md` si la KB seo-kb existe, sinon dans le dossier de travail actuel.

=====

## Note pour Tim (interne)

- **SKILL.md reproduit verbatim** depuis `~/.claude/skills/seo-roadmap-pseo/SKILL.md` (créé hier). Pas de nettoyage nécessaire : pas de dépendance vault dure, la ligne de sauvegarde a déjà un fallback ("si la KB seo-kb existe, sinon dossier de travail actuel"). Seul l'exemple de tableau Output a été légèrement raccourci pour le bundle (lignes "..." en moins), le reste est identique.
- **Skill neuf, jamais testé en prod.** Je l'ai écrit hier sur ta dictée (2 modes, sortie 30/60/90, doctrine 2 phases). Avant de le donner aux participants ce serait bien que TU le lances une fois sur un cas réel (un de tes clients) pour vérifier que la sortie te convient. Si un truc cloche dans le scoring ou le phasage, on corrige le SKILL.md source ET ce bundle avant distribution.
- **Pas encore push sur le repo `tim-claude-skills`.** Le SKILL.md est dans `~/.claude/skills/` mais pas commit. Pour le ZIP du jour ça n'a pas d'importance (le script `bundle-skills-bootcamp.sh` prend le dossier local), mais si tu veux le remote à jour : `cd ~/.claude/skills && git add seo-roadmap-pseo && git commit -m "Add seo-roadmap-pseo" && git push`.
- **Positionnement commercial assumé.** J'ai poussé l'angle "livrable prospect / proposition commerciale" dans la pédagogie, parce que tu m'avais dit "pour donner au prospect". Si en fait tu le présentes aux participants comme un outil interne (pas un livrable vendeur), je réécris l'intro en 2 minutes.
- **Cohérence checklist.** À ajouter dans `[[skills-checklist-bootcamp4]]` (section mots-clés/architecture ou une nouvelle section "conversion") si tu veux que la checklist reste à jour. Dis-moi, je le fais.
- **Normalisation.** Doc sans em-dashes dans la pédagogie (règle maison). Le bloc SKILL.md conserve ses tirets techniques.
