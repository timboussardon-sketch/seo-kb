---
type: source
source_type: note
title: "Guide : exploiter Fable 5 en agentique long + software engineering pour le SEO"
created: 2026-06-10
updated: 2026-06-10
tags: [fable-5, agentique, automatisation, product-led-seo, content-brain, geo]
sources: 3
confidence: medium
status: draft
---

# Fable 5 pour le SEO : agentique long + software engineering

> Fable 5 (Anthropic, sorti le 09/06/2026) : modèle frontière, état de l'art en ingénierie logicielle, vision et travail de connaissance, capable de tenir des tâches longues sur plusieurs jours. Prix 10/50 $ par M de tokens (2x Opus 4.8). Gratuit dans Pro/Max/Team jusqu'au 22/06, puis crédits. Rétention 30 jours sur tout le trafic.
> Sources : annonce Anthropic, Simon Willison, TechCrunch (voir bas de page).

## En résumé

Deux capacités à exploiter en priorité : les **tâches longues en autonomie** (multi-jours, agentique) et le **software engineering**. La première laisse tourner des chantiers que tu ne pouvais pas tenir à la main. La seconde te construit tes outils et accélère ta stack. Règle d'or sur les deux : l'autonomie sans garde-fou produit de la slope à l'échelle. Ton système (content-brain, quality gate, claims, preuves) EST le garde-fou. On encadre, on ne lâche pas le volant.

---

# Partie A : les tâches longues (agentique multi-jours)

## Le principe et sa limite

Fable 5 peut mener une tâche complexe pendant des jours sans qu'on le relance à chaque étape. C'est exactement le « ce qu'un humain ne peut pas tenir » de ton offre, mais transposé à un run unique au lieu d'une boucle planifiée. La limite : plus le run est long et autonome, plus une erreur de cadrage en entrée se démultiplie en sortie. Donc on verrouille l'entrée et on pose des points de contrôle.

## Les 3 chantiers à lui confier

### 1. Un cycle de contenu complet en autonomie
Enveloppe `content-brain` (briefing mémoire → `article-engine-pipeline` → fact-check au claim → gate de publi → prédictions J+30/J+90) dans un seul run Fable 5. Au lieu de piloter chaque phase, tu lui donnes le brief verrouillé et il déroule le cycle, en s'arrêtant aux gates.
- **Entrée verrouillée** : mot-clé business, intention, data métier scrapée, périmètre, KPI.
- **Sortie** : contenu prêt + ledger des claims + prédictions datées.

### 2. Audit de site entier + production des modèles de pages
En un run : `indexation-check` sur le sitemap complet, repérage des trous, puis `seo-modeles-pseo` pour construire les modèles de pages décisionnelles, puis génération des premières pages. Le multi-jours sert ici à enchaîner audit → architecture → production sans rupture.
- **Entrée** : sitemap, GSC, la money page, la data client.
- **Sortie** : rapport d'audit + tableau des modèles scorés (Proximité × Intention × Faisabilité) + pages prototypes.

### 3. Passe de maillage / cannibalisation à l'échelle
Sur des milliers d'URLs : `maillage-systeme` + `seo-cannibalisation` en continu sur tout le graphe, là où un humain abandonne après 200 lignes de tableur. Le run produit le plan de liens, les conflits d'intention, les fusions/301 à faire.
- **Entrée** : liste d'URLs / crawl / GSC.
- **Sortie** : plan de maillage (source, destination, ancre), conflits classés, actions priorisées.

## Comment l'encadrer (ton système = le garde-fou)

1. **Brief verrouillé en entrée.** Objectif, périmètre, KPI, data autorisée. Un run long part toujours d'un cadrage écrit, jamais d'un prompt vague.
2. **Checkpoints, pas un big-bang opaque.** Le run dépose des artefacts intermédiaires (rapport d'audit, tableau de modèles, ledger de claims) que tu peux lire et couper. Pas de « reviens dans 2 jours avec 300 pages ».
3. **Quality gate à chaque palier.** Tes 4 critères + anti-IA writing + claim = unité vérifiée (≥2 sources, primaire, anti-fraîcheur). Une page ne passe pas le gate, elle ne sort pas, même en autonomie.
4. **Prédictions datées → preuves.** Chaque lot produit pose des prédictions J+30/J+90 résolues par la GSC. L'autonomie ne dispense pas de la boucle apprentissage.
5. **Isolation pour ce qui écrit des fichiers.** Les passes qui modifient le repo tournent en worktree git pour éviter les conflits et pouvoir jeter d'un coup.

## Coût et data

- **2x Opus sur plusieurs jours = cher.** Tiering : Fable 5 orchestre et juge (brief, architecture, gate), les modèles cheap (Gemini Flash, Haiku, Sonnet) exécutent le volume. Les checkpoints servent aussi à couper avant de cramer des crédits.
- **Fenêtre gratuite jusqu'au 22/06** : c'est le moment de lancer les gros runs pendant que c'est inclus dans Pro/Max.
- **Rétention 30 jours** : anonymise la data client avant tout run long. Pour du brut identifiant (calls nominatifs, CRM), garde Opus 4.8 ou une voie zéro-rétention.

---

# Partie B : le software engineering

## 1. Tes outils Product-Led SEO
Calculateurs, simulateurs, générateurs, audits : c'est ta brique « Fully Meets » pour dominer les requêtes Do. Fable 5 les construit vite, dans ton design system.
- **Workflow** : `seo-product-led-seo` sort le concept + la spec (Surprise Gap, Confidence Score) → Fable 5 code l'outil (Next.js, tokens Organikk) → tu déploies.
- **Garde-fou** : `verify` (lance l'app, observe), `code-review` avant merge. Pas de merge aveugle d'un outil public.

## 2. Tes propres skills et le pack freelance
Le chantier en cours : porter les **16 skills SEO manquants** dans `organikk-seo-pack` (généricisation = retrait voix perso / chemins / clients). Fable 5 fait le gros du portage, tu valides le jugement. Pareil pour améliorer les skills existants.

## 3. Tes autres repos et sites clients
Dev plus rapide, refactors, tests, debug sur tes projets web et tes espaces clients. Le SWE SOTA réduit le temps passé sur la plomberie technique.
- **Garde-fou** : sur du code en prod (Supabase, Netlify), toujours tester en local et reviewer avant deploy. L'autonomie sur la data, jamais sur le code sans relecture.

## Le rappel sécurité
Fable 5 bloque cybersécurité / biologie / chimie et bascule sur Opus 4.8. Sans impact sur ton usage SEO, mais à savoir si un run touche à de la sécu (ex. audit d'une faille sur un site client : il refusera).

---

# À lancer cette semaine (fenêtre gratuite)

1. Un **run agentique long** sur un vrai chantier : audit complet + modèles de pages d'un de tes sites, encadré par les gates.
2. **Le portage des 16 skills** du pack freelance en SWE.
3. Un **test first-party** : même chantier sur Fable 5 vs Opus, on mesure l'écart réel (data pour ta Newsletter IA / tes études originales).

---

## Sources

- Anthropic, annonce Claude Fable 5 et Mythos 5 : https://www.anthropic.com/news/claude-fable-5-mythos-5
- Simon Willison, premières impressions : https://simonwillison.net/2026/Jun/9/claude-fable-5/
- TechCrunch, sortie Fable 5 : https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/

> À vérifier avant branchement technique : l'ID de modèle API exact et les conditions de rétention Enterprise (zéro-rétention ?). Les annonces presse ne les donnent pas.
