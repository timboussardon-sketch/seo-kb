---
title: "Skill workflow audit bootcamp — audit-engine-pipeline"
bootcamp: 4
semaine: 3
type: skill-distribuable
usage: "À mettre sur le Drive avec le doc workflow + les 2 variantes indexation-check"
related:
  - "[[workflow-audit-bootcamp4]]"
  - "[[skill-indexation-check]]"
  - "[[skill-indexation-check-cowork]]"
  - "[[sequencage-semaine-3]]"
---

# Skill `audit-engine-pipeline` — l'audit bout en bout (bootcamp 4)

Équivalent de `article-engine-pipeline` (S2) mais pour l'audit : **un skill qui enchaîne les 7 phases** du workflow resserré, appelle le bon sous-skill à chaque étape, et finit sur le rapport client.

C'est un **orchestrateur** : il ne remplace pas les sous-skills, il les pilote. Les sous-skills doivent être installés à part :
- `indexation-check` (variante terminal OU Cowork — une seule) — **hors pack des 9, à distribuer**
- `seo-quick-win` (pack des 9, #2)
- `seo-cannibalisation` (pack des 9, #3)
- `maillage-systeme` (pack des 9, #4)
- `maillage-interne-gsc` (passe data de la Phase 5) — **hors pack des 9, à distribuer**

## Procédure d'install (la même qu'en S1)

1. Dossier `~/.claude/skills/audit-engine-pipeline/`
2. Crée `SKILL.md`, colle tout le bloc entre les `=====`.
3. Relance Claude, vérifie avec `/skills`.

=====

---
name: audit-engine-pipeline
description: |
  Workflow d'audit SEO complet "bout en bout" — version bootcamp 4 resserrée, 7 phases enchaînées : Positionnement → Indexation → Quick Wins → Audit structurel Hn → Cannibalisation → Maillage → Synthèse & plan d'action 3 horizons. 100% données Google (GSC + Chrome ou terminal), aucun outil payant tiers. Orchestre les skills indexation-check, seo-quick-win, seo-cannibalisation, maillage-systeme et maillage-interne-gsc, et produit un rapport client au format "qui fait signer".

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "lance le workflow audit", "audit SEO complet", "audite ce site", "audit bootcamp", "déroule l'audit", "fais l'audit de [site]", "pipeline audit", "audit de A à Z", ou quand il fournit un export GSC + un sitemap en demandant un audit complet.

  Dérivé du Workflow V3 (Méthodologie Timothée Boussardon, avril 2026). Version resserrée : sans clusters AEO / analyse vectorielle / briefs de réécriture. Cible : sites de 30 à 1 000 pages.
---

# Skill — Audit SEO bout en bout (pipeline bootcamp 4)

Orchestrateur. Déroule les 7 phases DANS L'ORDRE, appelle le sous-skill à chaque étape, respecte les dépendances, stocke chaque sortie dans `audit/`, finit par le rapport. Une phase nourrit la suivante : ne jamais sauter une phase sans le documenter.

## Pré-requis — vérifier AVANT de lancer

- Export GSC en CSV (3-6 mois, toutes requêtes + toutes pages)
- URL du site + sitemap.xml accessible
- 5-10 requêtes business principales
- Sous-skills installés : `indexation-check`, `seo-quick-win`, `seo-cannibalisation`, `maillage-systeme`, `maillage-interne-gsc`
- Environnement : Claude Code (terminal) OU Cowork + extension Claude in Chrome

Si un pré-requis manque → le dire clairement et s'arrêter. Ne pas improviser un audit dégradé sans prévenir.

## Détection d'environnement (impacte les Phases 1 et 3)

Déterminer l'environnement avec l'utilisateur :
- **Terminal** (curl/grep dispo) → scraping via curl ; check indexation via `site:` + variantes du skill
- **Cowork** (pas de terminal) → scraping via extension Chrome ; check indexation via **croisement export GSC** ; en Phase 3, **prioriser** (ne jamais scraper tout le sitemap à l'aveugle dans Chrome)

## Pipeline

### Phase 0 — Positionnement (prompt, pas de sous-skill)

Lancer ce prompt sur l'export GSC + les requêtes business :

```
Pour chaque requête business : position moyenne, impressions, clics, CTR,
écart vs CTR attendu, URL qui ranke. Identifie les requêtes business
absentes de la GSC (= gaps critiques). Via recherche web : type de SERP
dominant + AI Overviews + top 3 par requête. Identifie les requêtes à fort
volume où le site ranke hors liste business (= opportunités cachées).
Tableau : | Requête | Position | Impressions | CTR | CTR attendu | Gap CTR | Type SERP | Priorité |
```

Stocker → `audit/00-positionnement.md`. Nourrit P1, P2, P3, P6.

### Phase 1 — Indexation

Appeler le skill `indexation-check` sur le sitemap + la liste d'URLs. Conserver strictement la distinction **« non indexée » / « non testable » / « présomption (absente GSC) »**. Stocker → `audit/01-indexation.md`.
→ Une page non indexée ne passera JAMAIS en quick win : on la signale, on ne l'optimise pas.

### Phase 2 — Quick Wins

Appeler `seo-quick-win` sur l'export GSC (pages position 3-12, impressions hautes, CTR sous-perf, impact estimé = impressions × delta CTR). Puis scrap des pages quick win (title/meta/Hn) → recommandations title/meta. Exclure branded + home. Stocker → `audit/02-quickwins.md`.

### Phase 3 — Audit structurel Hn (prompt + scrap, pas de sous-skill)

Récupérer **TOUTES** les URLs du sitemap (pas de cap à 50, le périmètre suit le site).
- Terminal : `curl -sL {URL} | grep -oE '<h[1-6][^>]*>'` puis lire le texte des balises, sur toutes les URLs.
- Cowork : Chrome lit les headings. Si gros sitemap → PRIORISER : d'abord les pages avec impressions GSC + les quick win (P2) + les position 4-20, le reste si le budget tokens le permet.

8 contrôles par page :
1. H1 unique et présent (0 = critique, >1 = à corriger)
2. Hiérarchie sans saut de niveau (H1→H3 sans H2 = cassé)
3. H1 vs intention (répond à la requête principale GSC ou générique/nom du site ?)
4. H2 vs micro-intentions (couvrent les requêtes GSC position 4-20 ?)
5. Hn génériques bannis (« Introduction », « Conclusion »… = signal faible/IA)
6. Hn sur-optimisés (mot-clé exact répété partout)
7. Passage Ranking (chaque H2 lisible en réponse autonome ?)
8. Pages sans structure (aucun Hn / div soup)

Sortie : tableau par URL `| URL | H1 ok | hiérarchie | H1↔intention | H2↔GSC | Hn génériques | verdict |` + anomalies critiques en tête (page business sans H1, H1 hors-sujet). Stocker → `audit/03-structure-hn.md`.

### Phase 4 — Cannibalisation

**Pré-condition** : compter les URLs distinctes dans la GSC.
- < 10 URLs → **SKIP**, documenter un diagnostic « sous-granularité », aller directement à la Phase 5.
- ≥ 10 → appeler `seo-cannibalisation` (détection conflits type A/B/C/Triade) + vérif Chrome des 2 URLs en conflit. Croiser avec la Phase 3 : H1/H2 qui se chevauchent = root cause contenu ; Hn distincts mais Google hésite = root cause maillage. Stocker → `audit/04-cannibalisation.md`.

### Phase 5 — Maillage (2 passes)

Crawl des liens internes via Chrome (matrice source→cible+ancre+position : orphelines, sur-linkées, ancres pourries), puis :
- **Passe structurelle** — appeler `maillage-systeme` : architecture en piliers (≥10 liens entrants ?), hub/satellite, orphelines/dead-end, diversification des ancres, croisement cannibalisations (P4). Ne dépend pas de la GSC, tourne toujours.
- **Passe data** — appeler `maillage-interne-gsc` : hiérarchie mère/fille/petite-fille (méthode Boussardon), pages stratégiques GSC sous-linkées, règles Know→Do. Croiser avec la passe structurelle : page forte en impressions GSC + orpheline = priorité absolue.
- ⚠️ Pas de GSC propre → ne lancer que la passe structurelle, documenter que la passe data est sautée.

Stocker → `audit/05-maillage.md`.

### Phase 6 — Synthèse & plan (prompt, pas de sous-skill)

Coller les synthèses P0→P5, lancer :

```
Génère le plan d'action en 3 horizons :
SEMAINE 1-2 (impact immédiat, zéro création) : déblocage indexation,
title/meta, corrections Hn rapides, liens internes, cannibalisation, GBP.
MOIS 1 (fondations) : optimisation pages, réécriture Hn hors-sujet,
restructuration maillage en piliers, résolution cannibalisations.
MOIS 2-3 (croissance) : nouvelles pages sur les gaps P0, outils.
Par action : | Action | Page | Type | Impact | Effort | Dépendances |
+ matrice de dépendances, actions parallélisables, KPIs par horizon.
```

Stocker → `audit/06-rapport.md`. **C'est le livrable final.**

## Garde-fous (NON-NÉGOCIABLES)

- **Lecture seule.** Aucune action de forçage d'indexation, aucune modif du site, aucune PR.
- **Aucun scraping Google automatique en Cowork** (CAPTCHA) → croisement export GSC à la place.
- Distinction stricte « non indexée » / « non testable » / « présomption ».
- **< 10 URLs GSC → skip Phase 4** (documenter, ne pas forcer).
- **Cowork + gros sitemap → Phase 3 priorisée via GSC**, jamais 800 URLs à l'aveugle dans Chrome.
- Si une phase échoue, la consigner dans le rapport (section « Limites ») et continuer les autres.
- Stocker chaque phase dans `audit/` AU FUR ET À MESURE, pas à la fin.
- Observation côté agent, décision côté humain.

## Livrable final

`audit/06-rapport.md` : synthèse exécutive en tête, anomalies critiques d'abord, plan d'action priorisé en 3 horizons, matrice de dépendances, KPIs. Format client. C'est ce livrable qui fait signer — pas les 6 fichiers de phase en vrac.

=====

## Note pour Tim (interne)

- **Nom** : `audit-engine-pipeline`, en parallèle strict de `article-engine-pipeline` (S2). Si tu préfères un nom bootcamp explicite (`workflow-audit-bootcamp`), dis-le, je renomme dossier + frontmatter.
- **C'est un orchestrateur, pas un monolithe** : il appelle `indexation-check` + `seo-quick-win` + `seo-cannibalisation` + `maillage-systeme`. Donc le message week-end doit lister CE skill **en plus** des sous-skills (3 sont dans le pack des 9, seul `indexation-check` est à ajouter). Préciser au groupe : installer `audit-engine-pipeline` ET `indexation-check` (la bonne variante), les 3 autres sont déjà là.
- **Skill vs doc workflow** : on a maintenant les deux. Le doc [[workflow-audit-bootcamp4]] = pédagogie (le groupe comprend chaque phase) ; le skill = exécution (Claude déroule tout seul). Cohérent avec ce que tu as dit en S2 (« moi j'utilise plus les skills que les workflows ») : le doc pour apprendre, le skill pour produire vite ensuite. À cadrer au call S3 : déroulez d'abord à la main avec le doc cette semaine, le skill c'est pour quand vous avez compris.
- Si tu modifies le doc workflow, répercute ici (les 7 phases doivent rester alignées doc ↔ skill).
