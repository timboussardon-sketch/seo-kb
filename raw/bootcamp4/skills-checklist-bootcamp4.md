---
title: Skills à avoir installés — checklist bootcamp 4 (état début Semaine 4)
bootcamp: 4
type: reference-participants
created: 2026-05-27
usage: "Doc partagé sur le cowork (Drive / Notion). Liste à jour de tous les skills et workflows qu'un participant doit avoir installés à fin S3 / début S4. Demande explicite des participants."
related:
  - "[[sequencage-semaine-4]]"
  - "[[skill-donnees-structurees]]"
  - "[[skill-core-web-vitals]]"
  - "[[skill-preparation-semantique]]"
  - "[[skill-roadmap-pseo]]"
  - "[[skill-indexation-check]]"
  - "[[skill-indexation-check-cowork]]"
  - "[[skill-maillage-systeme]]"
  - "[[skill-maillage-gsc-cannibalisation]]"
  - "[[skill-audit-engine-pipeline]]"
  - "[[skill-workflow-mots-cles]]"
  - "[[bundle-todo]]"
  - "[[observations-whatsapp-bootcamp]]"
---

# Skills à avoir installés — bootcamp 4

État au début de la Semaine 4 (27 mai 2026). Tout ce que tu dois avoir dans `~/.claude/skills/` (Claude Code, Mac/Linux) ou `%USERPROFILE%\.claude\skills\` (Windows) ou dans ton setup Cowork.

## Le pack des 9 (livré en S1)

Les 9 skills qu'on a installés au démarrage du bootcamp, avant la S1. Tu les as normalement tous. Si l'un manque, c'est qu'il y a eu un raté à l'install initiale, dis-le moi.

1. `seo-brief-contenu` — brief éditorial avec structure Hn
2. `seo-workflow-article` — pipeline rédaction 8 étapes
3. `article-engine-pipeline` — workflow rédaction bout en bout (orchestrateur)
4. `seo-entites-vectorielles` — entités sémantiques pour Grounding Score
5. `seo-cluster-aeo` — architecture cluster autour d'un mot-clé pilier
6. `seo-quick-win` — opportunités GSC positions 3-12 (pack #2)
7. `seo-cannibalisation` — cannibalisation depuis GSC (pack #3)
8. `maillage-systeme` — maillage interne structurel hub/satellite (pack #4)
9. `seo-programmatique-pseo` — systèmes de contenu programmatique scalable

Tout ce qui suit (sections 2 à 7) précise à quoi sert chacun + les ajouts hors pack S2/S3/S4.

## Comment vérifier ce que tu as

Dans Claude Code, tape `/skills`. Tu vois la liste de tout ce qui est installé. Si tu es sur Cowork, regarde la liste des skills connectés dans ton workspace.

Si un skill manque, retrouve son bundle dans le dossier Drive du jour de livraison (la pédagogie est dedans, le bloc à coller aussi).

---

## 1. Skills SEO — Mots-clés et architecture

Tout ce qui sert à partir d'une thématique ou d'une liste brute et arriver à des pages qui rankent.

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `seo-cluster-aeo` | Pack S1 | ✅ | Tu pars d'un mot-clé pilier, tu obtiens une architecture cluster (15+ pages satellites) optimisée pour les moteurs de réponse |
| `seo-recherche-mots-cles` | S3 bonus | ✅ | Une thématique → 50 à 150 mots-clés qualifiés (intention, volume, difficulté) |
| `seo-clustering-mots-cles` | S3 bonus | ✅ | Une liste brute → clusters exploitables (1 cluster = 1 page) |
| `seo-mots-cles-decisionnels` | S3 bonus | ✅ | Isole les requêtes transactionnelles qui convertissent, pas juste celles qui font du trafic |

Les 3 skills S3 bonus forment ensemble le **workflow mots-clés** : recherche → clustering → décisionnels. Bundle dédié sur le Drive : [[skill-workflow-mots-cles]].

## 2. Skills SEO — Brief et rédaction

Tout ce qui transforme un mot-clé ou un brief en article publié.

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `seo-brief-contenu` | Pack S1 | ✅ | Brief éditorial complet avec structure Hn optimisée Passage Ranking |
| `seo-workflow-article` | Pack S1 | ✅ | Pipeline de rédaction d'article en 8 étapes |
| `article-engine-pipeline` | Pack S1 | ✅ | Workflow rédaction de A à Z : décodage sémantique RRF + FAQ FM + rédaction 8 étapes + checklist fact-check |
| `seo-entites-vectorielles` | Pack S1 | ✅ | Cartographie des entités sémantiques (Grounding Score / similarité cosinus) pour aligner une page avec l'intention |
| `seo-programmatique-pseo` | Pack S1 | ✅ | Conception de systèmes de contenu programmatique (template + variable = centaines de pages) |

## 3. Skills SEO — Audit (Semaine 3)

Tout ce qui sert à diagnostiquer un site existant. Le workflow audit complet vit dans [[workflow-audit-bootcamp4]] (8 phases).

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `indexation-check` (variante terminal) | S3 hors pack | ❌ terminal uniquement | Audit indexation sur sitemap. Variante terminal pour Claude Code. **Choisis UNE des deux variantes, pas les deux.** |
| `indexation-check` (variante Cowork) | S3 hors pack | ✅ | Même skill, variante sans terminal. Bundle [[skill-indexation-check-cowork]]. **À installer si tu es sur Cowork.** |
| `seo-quick-win` | Pack S1 (#2) | ✅ | Pages en position 3-12 avec CTR sous-performant depuis ton export GSC |
| `seo-cannibalisation` | Pack S1 (#3) | ✅ | Détection des pages qui se cannibalisent sur le même mot-clé depuis la GSC |
| `maillage-systeme` | Pack S1 (#4) | ✅ | Maillage interne structurel (hub/satellite, ancres, orphelines). **Vérifier que tu as la version longue : si ton SKILL.md est court, le re-bundle S3 corrige.** |
| `maillage-interne-gsc` | S3 hors pack | ✅ | Maillage depuis data GSC (page mère/fille selon Boussardon) |
| `audit-engine-pipeline` | S3 orchestrateur | ⚠️ partiel | Orchestre toutes les phases d'audit. Sur Cowork tu peux le lancer mais la Phase 1bis (CWV) sera sautée |

## 4. Skills SEO — livrés en Semaine 4

Les 4 skills distribués pendant la Semaine 4. Deux techniques (balisage, perf), un de préparation amont (sémantique), un commercial (roadmap). Détail du séquençage dans [[sequencage-semaine-4]].

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `seo-donnees-structurees` | S4 hors pack | ✅ (principes), ⚠️ (code Next.js) | Balisage JSON-LD qui se génère depuis le contenu. Code Next.js + principes universels (3 règles valables sur tous CMS) |
| `seo-core-web-vitals` | S4 hors pack | ❌ terminal uniquement | Audit Lighthouse local mobile sur sitemap. **Requiert `npm install -g lighthouse` + `brew install jq`.** Pas utilisable sur Cowork pur. |
| `seo-preparation-semantique` | S4 hors pack | ✅ | Engine de préparation sémantique sans scraping SERP. La matière brute (entités pondérées, gap analysis, Surprise Score) qui alimente le brief et la rédaction. Remplace Surfer / NeuronWriter. |
| `seo-roadmap-pseo` | S4 hors pack | ✅ | Roadmap SEO 30/60/90 en 2 phases (transac/décisionnel d'abord, info bas de funnel ensuite). Sortie pensée pour présentation prospect / proposition commerciale. |

## 5. Skills SEO — pSEO et conversion (bonus pack S1)

Skills présents dans le bundle initial (Drive S1) mais hors des 9 piliers travaillés en session. À utiliser quand le cas client le demande (pSEO scalable, outils interactifs, contenu objection-driven).

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `seo-modeles-pseo` | S1 bonus | ✅ | Modèles de pages satellites décisionnelles autour d'une Money Page |
| `seo-product-led-seo` | S1 bonus | ✅ | Conception d'outils interactifs (calculateurs, simulateurs, générateurs) pour les requêtes Do |
| `seo-peurs-objections` | S1 bonus | ✅ | Pain points B2B et verbatims Haute Surprise pour contenu à haute conversion |

## 6. Outils transverses

Pas du SEO direct, mais des skills qu'on utilise dans la routine quotidienne du bootcamp.

| Skill | Livré | Cowork OK ? | À quoi ça sert |
|-------|-------|-------------|----------------|
| `ton-de-voix-tim` (ou ton de voix personnel) | S2 | ✅ | Applique ton ton de voix anti-IA writing. Le tien est à construire sur la base du worksheet S2 ([[ton-de-voix-worksheet]]) |
| `todo` | Bonus (J2 bis / J5) | ❌ terminal uniquement | Reconstruit ta todo depuis tes transcripts Claude Code locaux (lit `~/.claude/projects/`) |
| `revue-presse-quotidienne` (skill projet) | S4 J2 | ⚠️ via GitHub Action | Veille auto sur la thématique de ton client, sortie en chiffres sourcés exploitables en rédaction |

---

## Récap rapide — ce qui n'est PAS automatique pour Cowork

Si tu es sur Cowork (sans terminal local), ces skills ne tournent pas chez toi tels quels :

- `seo-core-web-vitals` — requiert Lighthouse CLI + jq, terminal obligatoire
- `indexation-check` variante terminal — utilise la variante Cowork à la place
- `todo` — lit le système de fichiers local, pas utilisable sur Cowork
- `audit-engine-pipeline` — fonctionne mais la Phase 1bis (CWV) sera sautée

Pas grave. Tu fais l'audit perf au prochain audit côté terminal, ou tu prends le rapport PageSpeed Insights public en complément.

## Récap rapide — les 4 skills de la Semaine 4

Les 4 nouveaux skills à installer cette semaine (en plus du pack S1 que tu as déjà) :

- `seo-donnees-structurees` — balisage JSON-LD auto
- `seo-core-web-vitals` — audit perf Lighthouse (terminal only)
- `seo-preparation-semantique` — engine sémantique sans SERP
- `seo-roadmap-pseo` — roadmap client 30/60/90

Bundles à coller : un doc Drive par skill ([[skill-donnees-structurees]], [[skill-core-web-vitals]], [[skill-preparation-semantique]], [[skill-roadmap-pseo]]).

---

## Comment installer un skill (rappel)

Vraie nouvelle install, format universel :

1. Dossier `~/.claude/skills/[nom-du-skill]/` (à créer s'il n'existe pas)
2. Dedans, fichier `SKILL.md` = le bloc entre `=====` dans le bundle Drive
3. Si le skill a un sous-dossier `references/`, le créer et y coller le second bloc (cas de `seo-donnees-structurees` uniquement)
4. Relancer Claude Code, vérifier avec `/skills`

Sur Cowork : suivre les instructions du bundle Cowork (typiquement une URL à connecter, pas un fichier à coller).

Skill qui ne se déclenche pas après install ? Vérifier que :
- Le fichier s'appelle bien `SKILL.md` (pas `skill.md`, pas `Skill.md`)
- Le frontmatter en tête (`---` ... `---`) est intact
- Tu as bien relancé Claude (juste recharger l'onglet ne suffit pas toujours)

Si ça coince : MP dédié, on débogue ensemble.

---

## Note pour Tim (interne)

- **Composition du pack S1 reconstruite, à valider.** Pas de liste canonique trouvée dans `bootcamp4/`. Reconstruite en croisant : (a) les `related:` de `session-1-mots-cles-prep.md` (seo-entites-vectorielles, seo-cluster-aeo, seo-quick-win, seo-brief-contenu), (b) les `related:` de `session-2-redaction-prep.md` + skills J1/J2 du séquençage S2 (seo-brief-contenu, article-engine-pipeline, seo-workflow-article, seo-entites-vectorielles, seo-programmatique-pseo), (c) les #s confirmés #2 (quick-win), #3 (cannibalisation), #4 (maillage-systeme) de l'audit-engine-pipeline. Total : 9 skills qui couvrent S1 (mots-clés) + S2 (rédaction) + S3 (audit). **Ma proposition** :
  1. `seo-brief-contenu`
  2. `seo-workflow-article`
  3. `article-engine-pipeline`
  4. `seo-entites-vectorielles`
  5. `seo-cluster-aeo`
  6. `seo-quick-win` (#2)
  7. `seo-cannibalisation` (#3)
  8. `maillage-systeme` (#4)
  9. `seo-programmatique-pseo`
- **Bonus S1 vs pack.** Le snapshot Obsidian `/Users/timothee/Documents/CLAUDE/claude-skills/` (créé 2026-04-27) contient 14 skills. Sur les 14 : 9 = pack ci-dessus, 3 = internes Organikk à exclure (organikk-blog-article, organikk-site, kb-semantic-search), 1 = HORS pack S3 (maillage-interne-gsc), et 3 sont des bonus S1 confirmés : `seo-peurs-objections`, `seo-product-led-seo`, `seo-modeles-pseo` (validé Tim 2026-05-27). Les autres skills présents dans `~/.claude/skills/` (`seo-preparation-semantique`, `seo-geo-audit`, etc.) ne sont PAS dans le bundle bootcamp et restent personnels à Tim.
- **Ordre du pack à valider.** Les #s 2/3/4 sont confirmés (audit-engine-pipeline les nomme). Le #1 et les #5-#9 ne sont nommés nulle part. J'ai gardé l'ordre logique du parcours (brief → rédaction → architecture → audit → scalabilité). À réordonner si tu as la numérotation officielle.
- **Statut Cowork vs Terminal.** J'ai fait l'effort de marquer `Cowork OK ?` sur chaque skill. À vérifier de ton côté pour les 9 du pack S1 : tous ne sont pas forcément exécutables sans terminal (en particulier ceux qui scrapent des URLs). J'ai marqué ✅ par défaut quand le skill est purement de l'analyse, mais à corriger si je me trompe sur un cas.
- **`article-engine-pipeline` vs `seo-workflow-article`.** Les deux existent dans `~/.claude/skills/`. Le premier orchestre (RRF + FAQ FM + workflow + fact-check), le second est juste les 8 étapes de rédaction. Dans le bootcamp, c'est probablement `article-engine-pipeline` qui est référencé (la version "bout en bout"). À confirmer.
- **`ton-de-voix-tim` vs ton perso.** Le skill `ton-de-voix-tim` applique TON ton de voix (anti-IA, tutoiement, etc.). Pour les participants, ils ont un ton à eux qu'ils doivent construire via [[ton-de-voix-worksheet]]. À clarifier dans la section 6 : ils n'installent PAS `ton-de-voix-tim` (c'est ton ton), ils créent leur propre skill `ton-de-voix-[prenom]`. Je l'ai écrit "ton-de-voix-tim (ou ton de voix personnel)" en provisoire, à reformuler quand tu valides.
- **`revue-presse-quotidienne` est un skill projet, pas un skill global.** Il vit dans un repo (`tim-claude-skills` ou `seo-kb/skills/revue-presse-quotidienne/`), il tourne en GitHub Action pour ta newsletter Algorithme. Pour le bootcamp J2 S4 il faut "le rebrancher sur la thématique du client" — pas documenté en pas-à-pas selon la note de [[sequencage-semaine-4]]. À cadrer : est-ce qu'on bundle un mode d'emploi pour les participants ou est-ce qu'on présente juste le principe au J2 ?
- **Format du doc.** Tableau plutôt que liste à puces : c'est cherchable, c'est imprimable, les colonnes Cowork OK + À quoi ça sert répondent aux deux questions que les participants posent vraiment ("est-ce que je l'ai installé ?" + "à quoi il sert déjà ce truc ?"). Section 7 absente : pas de skills internes Organikk dans ce doc (`organikk-blog-article`, `organikk-site`, `bxble-directory`, `fusionn-trends-quotidien`, `kb-semantic-search`) — ce sont les tiens, pas pour les participants.
- **Normalisation.** Doc sans em-dashes (règle maison). Wikilinks placés pour rebrancher la navigation Obsidian. À publier sur le Drive bootcamp + cowork une fois la composition pack S1 validée.
