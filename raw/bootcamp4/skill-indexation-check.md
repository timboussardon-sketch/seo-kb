---
title: "Skill à installer avant la Semaine 3 — indexation-check"
bootcamp: 4
semaine: 3
type: skill-distribuable
usage: "À mettre sur le Drive + message WhatsApp le week-end avant le J1"
related:
  - "[[sequencage-semaine-3]]"
  - "[[workflow-audit-bootcamp4]]"
---

# Skill `indexation-check` — à installer avant lundi

Ce skill alimente la **Phase 1 (Audit d'indexation)** du workflow audit. Il n'est **pas** dans le pack des 9 skills installés en S1 — il faut l'ajouter avant le J1.

## Procédure d'install (la même qu'en S1)

1. Va dans le dossier des skills : `~/.claude/skills/` (Mac/Linux) ou `%USERPROFILE%\.claude\skills\` (Windows). S'il n'existe pas, crée-le.
2. Crée un sous-dossier : `~/.claude/skills/indexation-check/`
3. Dedans, crée un fichier `SKILL.md` et colle **tout le bloc ci-dessous** (entre les deux lignes `=====`).
4. Relance Claude Code. Vérifie avec `/skills` que `indexation-check` apparaît.

> ⚠️ **Pré-requis : ce skill tourne dans Claude Code (terminal).** Il utilise `curl` et `grep` pour interroger le web public (statut HTTP, robots.txt, sitemap, scraping `site:`). Si tu travailles uniquement sur Claude Cowork ou l'extension Chrome, il ne pourra pas s'exécuter tel quel — viens en MP ce week-end, on règle ça avant lundi, pas pendant la Phase 1.

=====

```markdown
---
name: indexation-check
description: |
  Audit d'indexation d'un site (B2B / éditorial / pSEO) sans outil tiers payant. Vérifie 9 points sur chaque URL : statut HTTP, blocages techniques, directives noindex, sitemap (présence + lastmod + cohérence), maillage interne entrant, longueur de contenu, statut d'indexation Google estimé. Sortie : rapport markdown avec synthèse, anomalies critiques en tête, anomalies mineures, recommandations priorisées. Distingue strictement "non indexée" et "non testable" (rate-limit Google). Aucune action de forçage, lecture seule sur le web public.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit indexation", "check indexation", "monitoring indexation", "vérifier l'indexation", "mes pages sont-elles indexées", "agent indexation", "routine indexation mensuelle", ou quand il fournit une liste d'URLs / un sitemap / un fichier `urls.txt` / `articles.ts` / `wiki.ts` en demandant un diagnostic d'indexation.

  Ce skill est conçu pour tourner en one-shot (audit ponctuel) ou en récurrent mensuel via `/schedule`. Cible : sites de 30 à 1 000 pages. Au-delà, brancher l'API Google Search Console officielle (voir section "Variante haute fiabilité").
---

# Skill — Audit d'indexation Claude

## Quand déclencher

- Audit ponctuel d'un site (avant call commercial, après une refonte, après un déploiement de cluster)
- Monitoring mensuel récurrent sur un client en accompagnement
- Diagnostic d'une chute de trafic non expliquée
- Pré-flight d'un projet pSEO (vérifier que la base technique est saine avant de scaler)

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Liste des URLs à monitorer (fichier dans le repo : `urls.txt`, `src/data/wiki.ts`, `src/data/articles.ts`) OU URL du sitemap.xml public du site | Oui |
| Domaine cible (ex : `site-client.fr`) | Oui |
| Périmètre du maillage à crawler (pages hubs : `/`, `/glossaire`, `/wiki`, footer, articles) | Recommandé |
| Service account GSC API (upgrade fiabilité) | Optionnel |

Minimum viable : une liste d'URLs et le domaine. Le reste se déduit.

## Architecture (3 couches)

```
1. Charger la liste des URLs (source de vérité humaine)
        ↓
2. COUCHE A — Audit technique (causes potentielles)
        ↓
3. COUCHE B — Statut d'indexation observable
        ↓
4. COUCHE C — Reporting markdown
```

La séparation causes / statut est volontaire. Le check v1 ne regardait que le statut, donc disait "OK 200" même quand la page portait un `noindex` accidentel. Le check v2 sépare strictement les deux.

## Pipeline (9 checks)

### COUCHE A — Audit technique (causes)

**1. HTTP check (404/500, redirects)**
Pour chaque URL :
\`\`\`bash
curl -sIL -A "Mozilla/5.0" -o /dev/null -w "%{http_code}|%{url_effective}" {URL}
\`\`\`
Note le code final ET la chaîne de redirects. 200 attendu. Toute redirection 301→200 systématique = dette à signaler (trailing slash, http→https).

**2. robots.txt non bloquant**
\`\`\`bash
curl -s https://{domaine}/robots.txt
\`\`\`
Pour chaque path, vérifie qu'aucune directive `Disallow:` ne le bloque pour `User-agent: *` ni `User-agent: Googlebot`.

**3. Pas de balise noindex (HTML + en-tête HTTP)**
\`\`\`bash
curl -sL -A "Mozilla/5.0" {URL} | grep -i 'name="robots"'
curl -sIL {URL} | grep -i 'x-robots-tag'
\`\`\`
Signaler toute présence de `noindex` ou `none`.

**4. Sitemap : présence + fraîcheur**
\`\`\`bash
curl -s https://{domaine}/sitemap.xml
\`\`\`
Pour chaque slug attendu, vérifie présence d'une `<loc>` et lis le `<lastmod>` associé. Flagger tout `lastmod` > 6 mois.

**5. Cohérence sitemap ↔ source de vérité**
Diff entre les slugs de la SOT (fichier humain) et les `<loc>` du sitemap :
- Slugs en source mais absents du sitemap → à ajouter au build
- `<loc>` en sitemap mais absente de la source → orpheline sitemap

**6. Maillage interne entrant**
Crawl les pages hubs (`/`, `/glossaire`, `/wiki`, footer, sample d'articles) et compte les liens internes entrants par URL cible.
- 0 lien entrant = orpheline (critique)
- 1 seul lien entrant = sous-maillée (à signaler)

**7. Longueur de contenu (proxy thin content)**
Pour chaque URL, extrais le texte du `<main>` ou `<article>` (à défaut du `<body>` moins `<nav>` et `<footer>`) et compte les mots.
- < 300 mots = thin (à creuser)
- 300-800 = court mais acceptable pour fiche atomique
- > 800 = OK

### COUCHE B — Statut d'indexation (sortie)

**8. Indexation Google estimée (scraping `site:`)**
\`\`\`bash
curl -sL -A "Mozilla/5.0 (Macintosh...)" "https://www.google.com/search?q=site:{URL}&hl=fr"
\`\`\`
**Garde-fous obligatoires :**
- Espacer les requêtes de 3 à 5 secondes (`sleep 4`)
- Détecter le blocage : `grep -E 'sorry/index|recaptcha|unusual traffic'`
- Si bloqué : marquer "non testable — rate limit", **pas** "non indexée"
- Retry une fois si réponse vide avant de conclure
- Marquer "indexée" si l'URL apparaît dans le HTML de réponse

Fiabilité ~40-60 % à cause du rate-limit. Pour 100 % de fiabilité, voir la variante GSC API.

### COUCHE C — Reporting

**9. Rapport markdown**
Structure obligatoire :
- Synthèse en tête (X/N par dimension, `✅` pour validé, `⚠️` pour anomalie)
- Anomalies CRITIQUES (action immédiate) — `noindex` accidentel, page orpheline, 404 sur page business
- Anomalies mineures — `lastmod` > 6 mois, sous-maillage, thin content
- Recommandations priorisées (2-5 actions, classées par impact estimé)
- Section "Limites du rapport" (ce qui n'a pas pu être testé et pourquoi)

## Sortie obligatoire

\`\`\`markdown
# Indexation check — {domaine} — {date}

## Synthèse

Vérifications validées :
✅ {check} : X / N
✅ ...

Vérifications avec anomalies :
⚠️ {check} : X / N ({Y détails})
⚠️ ...

## Anomalies CRITIQUES (action immédiate)

⚠️ {URL} — {anomalie détectée}
   {contexte : depuis quand, impact estimé en impressions ou clics}
   → {action concrète à mener}

## Anomalies mineures

- {liste compactée des points secondaires}

## Recommandations priorisées

1. {action 1} — {effort estimé}, {impact estimé}
2. {action 2} — ...
3. {action 3} — ...

## Limites de ce rapport

- {ce qui n'a pas pu être testé et pourquoi : rate-limit Google, JS rendu côté client, etc.}
\`\`\`

## Garde-fous (NON-NÉGOCIABLES)

- **Lecture seule** sur le web public. Aucune requête authentifiée non explicitement autorisée.
- **Aucune action de forçage d'indexation.** Pas de soumission GSC, pas de force-crawl.
- **Pas de modification du site.** Pas de PR sur les fichiers source. Sortie limitée à `reports/` ou directement dans la conversation.
- **Distinction stricte** "non indexée" vs "non testable" dans le rapport.
- **Priorité au signalement** : un `noindex` accidentel sur une page business doit remonter en TOP du rapport, pas en ligne 47 du tableau.
- Si un check échoue, continuer les autres et signaler dans la section "Limites".

> Discipline : observation côté agent, décision côté humain. Un agent qui peut "réparer" peut aussi tout casser un dimanche à 3 h du matin.

## Variante haute fiabilité — GSC URL Inspection API

Si l'utilisateur dispose d'un service account Google Cloud + propriété GSC :
1. Lire la clé JSON via secret stocké côté projet
2. Signer un JWT, échanger contre access token
3. POST sur `https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`
4. Statuts officiels disponibles : `INDEXED`, `DISCOVERED_NOT_INDEXED`, `CRAWLED_NOT_INDEXED`, `URL_IS_UNKNOWN_TO_GOOGLE`

Passe le check #8 de ~50 % à 100 % de fiabilité. Setup ~30 minutes. Lève le rate-limit Google (limite officielle 2 000 inspections / jour / propriété).

## Variante site JS rendu côté client (SPA)

Si le contenu principal est rendu côté client (Single Page Application), `curl` ne verra qu'une coquille HTML quasi vide. Brancher Playwright headless :
1. Lancer un browser headless
2. Charger l'URL, attendre `networkidle`
3. Comparer le HTML rendu vs le HTML servi par le serveur
4. Signaler tout contenu uniquement présent post-JS (= invisible pour les crawlers qui n'exécutent pas le JS)

À réserver aux sites SPA ou aux clusters critiques (~30 s par URL).

## Récurrence — programmation via `/schedule`

Pour transformer l'audit ponctuel en monitoring continu :
\`\`\`
/schedule
\`\`\`
Choix structurants :
- **Récurrence** : `cron_expression: "0 1 1 * *"` (1er de chaque mois, 01h UTC)
- **Alternative one-shot** : `run_once_at` à J+14 après un déploiement de cluster
- **Modèle** : `claude-sonnet-4-6` (Opus inutile pour ce job)
- **Tools** : `Bash, Read, Write, Edit, Glob, Grep`
- **Environment** : Default Anthropic Cloud

À chaque exécution : 5 à 10 min de tourner-en-fond, rapport posté dans la conversation (ou push d'une PR si configuré côté repo).

## Réutilisation client

Pour appliquer ce skill à un client en accompagnement :
1. Créer un fichier `urls-prio.txt` dans son repo (top 30 pages business) OU pointer le sitemap public
2. Adapter le périmètre du maillage (hubs spécifiques au site)
3. Schedule cron mensuel
4. Inclure le rapport mensuel dans la note de suivi

Coût marginal par client : ~15 min de setup, 0 € récurrent. À facturer dans la rétro mensuelle ou comme bonus différenciant en pitch.
```

=====

## Note pour Tim (interne)

- Contenu **identique au skill canonique** `~/.claude/skills/indexation-check/SKILL.md`, seule la section « Sources internes » (pointeurs vault privé) a été retirée pour la distribution. Si tu mets à jour le skill canonique, régénère ce fichier.
- **Décision de fond à trancher** : le skill est `Bash`/`curl` → Claude Code terminal obligatoire. Le reste du workflow audit (Phases 2-4) passe par l'extension Chrome. Donc Phase 1 = seule phase qui exige le terminal. Deux options : (a) assumer « la Phase 1 nécessite Claude Code, les autres non » et l'annoncer clairement au J1 ; (b) écrire une variante Chrome-only de l'audit d'indexation (Claude lit le sitemap + les pages via l'extension, sans curl) pour le sous-groupe non-terminal. Option (a) = zéro travail mais on perd les novices sur la P1 ; option (b) = un demi-skill à écrire mais le groupe entier suit. À voir selon la proportion réelle de gens sur terminal vs Cowork.
