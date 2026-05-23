---
title: "Skill à installer avant la Semaine 3 — indexation-check (variante Cowork)"
bootcamp: 4
semaine: 3
type: skill-distribuable
variante: cowork
usage: "À mettre sur le Drive + message WhatsApp le week-end avant le J1"
related:
  - "[[skill-indexation-check]]"
  - "[[sequencage-semaine-3]]"
  - "[[workflow-audit-bootcamp4]]"
---

# Skill `indexation-check` — variante Claude Cowork (sans terminal)

Même skill, même méthode, **même rapport** que la version terminale ([[skill-indexation-check]]). Seul le mécanisme de récupération change : au lieu de `curl`/`grep`, l'extension **Claude in Chrome** ouvre les URLs publiques, et le **croisement avec l'export GSC** (déjà produit en Phase 0 du workflow) remplace le scraping `site:`.

> **Installe UNE seule des deux versions, pas les deux.**
> - Tu es sur **Claude Code (terminal)** → installe [[skill-indexation-check]] (version `curl`).
> - Tu es sur **Claude Cowork / extension Chrome** → installe CELLE-CI.
> Les deux portent le même nom de skill (`indexation-check`), donc la Phase 1 du workflow fonctionne pareil dans les deux cas.

## Procédure d'install (la même qu'en S1)

1. Dossier des skills : `~/.claude/skills/` (Mac/Linux) ou `%USERPROFILE%\.claude\skills\` (Windows).
2. Crée le sous-dossier `~/.claude/skills/indexation-check/`
3. Dedans, crée `SKILL.md` et colle tout le bloc entre les lignes `=====`.
4. Relance Claude, vérifie avec `/skills`.

**Pré-requis Cowork :** extension Claude in Chrome connectée (la même que pour les Phases 2-4 du workflow) + l'export GSC CSV de la Phase 0. Pas de terminal requis.

=====

---
name: indexation-check
description: |
  Audit d'indexation d'un site (B2B / éditorial / pSEO) sans outil tiers payant — VARIANTE CLAUDE COWORK : récupération via l'extension Claude in Chrome + croisement export GSC, aucun terminal/Bash requis. Vérifie 9 points sur chaque URL : statut HTTP, blocages techniques, directives noindex, sitemap (présence + lastmod + cohérence), maillage interne entrant, longueur de contenu, statut d'indexation Google (déduit du croisement GSC). Sortie : rapport markdown avec synthèse, anomalies critiques en tête, anomalies mineures, recommandations priorisées. Distingue strictement "non indexée" et "non testable". Lecture seule, aucune action de forçage.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit indexation", "check indexation", "monitoring indexation", "vérifier l'indexation", "mes pages sont-elles indexées", "agent indexation", "routine indexation mensuelle", ou quand il fournit une liste d'URLs / un sitemap / un export GSC en demandant un diagnostic d'indexation.

  Cible : sites de 30 à 1 000 pages. Au-delà, brancher l'API Google Search Console officielle (section "Variante haute fiabilité").
---

# Skill — Audit d'indexation Claude (variante Cowork)

## Quand déclencher

- Audit ponctuel d'un site (avant call commercial, après refonte, après déploiement de cluster)
- Monitoring mensuel sur un client en accompagnement
- Diagnostic d'une chute de trafic non expliquée
- Pré-flight d'un projet pSEO

## Input requis

| Source | Obligatoire |
|--------|-------------|
| URL du sitemap.xml public OU liste des URLs à monitorer | Oui |
| Domaine cible (ex : `site-client.fr`) | Oui |
| Export GSC (CSV, toutes pages — celui de la Phase 0 du workflow audit) | Oui (sert le check #8) |
| Extension Claude in Chrome connectée | Oui |
| MCP Windsor.ai (GSC via API) | Optionnel (alternative à l'export CSV) |
| Service account GSC API | Optionnel (variante 100 % fiable) |

Minimum viable : sitemap + domaine + export GSC + Chrome connecté.

## Principe de la variante

Tout check qui passait par `curl` passe maintenant par **Chrome qui ouvre l'URL publique** (un `robots.txt`, un `sitemap.xml`, une page : ce sont juste des URLs, Chrome les ouvre, Claude lit le contenu). Le seul check qui ne se fait pas par observation directe — le statut d'indexation Google — se déduit du **croisement entre la liste d'URLs et l'export GSC** : une page qui reçoit des impressions dans la GSC est, par définition, indexée et servie. C'est plus fiable que le scraping `site:` (que la version terminale annonce elle-même à 40-60 %).

## Pipeline (9 checks)

### COUCHE A — Audit technique (causes)

**1. HTTP / 404 / redirects**
Via Chrome, ouvre chaque URL. Observe : la page charge-t-elle (contenu réel) ou affiche-t-elle une erreur / page 404 ? Note l'URL finale (après redirection éventuelle). ⚠️ La chaîne de redirects multi-sauts n'est pas observable précisément via Chrome → si une redirection est détectée mais la chaîne incertaine, marquer le détail "non testable" (section Limites), pas une fausse alerte.

**2. robots.txt non bloquant**
Via Chrome, ouvre `https://{domaine}/robots.txt`. Pour chaque path audité, vérifie qu'aucune directive `Disallow:` ne le bloque pour `User-agent: *` ni `Googlebot`.

**3. Pas de balise noindex**
Via Chrome, ouvre la page et lis le HTML : présence d'une balise `<meta name="robots" content="noindex">` ? ⚠️ L'en-tête HTTP `X-Robots-Tag` n'est pas exposé de façon fiable par l'extension → marquer "non testable" pour ce sous-point. Compensation : un `noindex` (balise OU en-tête) a pour conséquence l'absence d'impressions GSC ; le check #8 fera donc remonter le **symptôme** même quand la cause par en-tête n'est pas directement lisible.

**4. Sitemap : présence + fraîcheur**
Via Chrome, ouvre `https://{domaine}/sitemap.xml`. Pour chaque slug attendu : présence d'une `<loc>` ? Lis le `<lastmod>`. Flagger tout `lastmod` > 6 mois.

**5. Cohérence sitemap ↔ source de vérité**
Diff entre les slugs de la source (liste fournie / pages connues) et les `<loc>` du sitemap :
- Slug en source mais absent du sitemap → à ajouter au build
- `<loc>` en sitemap mais inconnue de la source → orpheline sitemap

**6. Maillage interne entrant**
Via Chrome, navigue sur les pages hubs (`/`, `/glossaire`, `/wiki`, footer, échantillon d'articles). Pour chaque URL cible, compte les liens internes entrants observés.
- 0 lien entrant = orpheline (critique)
- 1 seul lien entrant = sous-maillée (à signaler)

**7. Longueur de contenu (proxy thin content)**
Via Chrome, lis le contenu principal de la page (zone `<main>`/`<article>`, à défaut le body hors nav/footer). Estime le nombre de mots.
- < 300 mots = thin (à creuser) · 300-800 = court mais acceptable · > 800 = OK

### COUCHE B — Statut d'indexation (sortie)

**8. Indexation Google — par croisement GSC (méthode principale)**
Croise la liste d'URLs (sitemap + source) avec l'**export GSC** :
- URL présente dans la GSC avec des impressions → **indexée et servie** ✅
- URL présente dans la GSC, 0 impression / 0 clic → indexée mais non servie (à surveiller)
- URL **absente de l'export GSC** (sur une période de 3-6 mois) → **forte présomption de non-indexation** → à flagger en anomalie, **sans conclure définitivement** (une page récente ou à zéro recherche peut être indexée sans impression)

Confirmation optionnelle des cas ambigus : l'utilisateur fait manuellement une recherche `site:{URL}` dans son navigateur et te donne le résultat (human-in-the-loop). Ne jamais scraper Google en automatique depuis l'extension (CAPTCHA + fiabilité nulle).

Alternative au CSV : si le **MCP Windsor.ai** (connecteur GSC) est branché, interroger directement les données GSC via le MCP au lieu de l'export CSV — même logique de croisement, données fraîches.

### COUCHE C — Reporting

**9. Rapport markdown** (structure identique à la version terminale)
- Synthèse en tête (X/N par dimension, ✅ / ⚠️)
- Anomalies CRITIQUES en premier (noindex sur page business, orpheline, 404 sur page business, page business absente de la GSC)
- Anomalies mineures (lastmod > 6 mois, sous-maillage, thin content)
- Recommandations priorisées (2-5 actions, par impact)
- Section "Limites de ce rapport" : tout ce qui est sorti "non testable" (X-Robots-Tag, chaîne de redirects, etc.) et pourquoi

## Sortie obligatoire

# Indexation check — {domaine} — {date}

## Synthèse
Vérifications validées : ✅ {check} : X / N …
Vérifications avec anomalies : ⚠️ {check} : X / N ({détails}) …

## Anomalies CRITIQUES (action immédiate)
⚠️ {URL} — {anomalie}
   {contexte : depuis quand, impact estimé}
   → {action concrète}

## Anomalies mineures
- {liste compactée}

## Recommandations priorisées
1. {action} — {effort}, {impact}
2. …

## Limites de ce rapport
- {ce qui n'a pas pu être testé et pourquoi : X-Robots-Tag non lisible via Chrome, redirects multi-sauts, page absente GSC = présomption non confirmée, etc.}

## Garde-fous (NON-NÉGOCIABLES)

- **Lecture seule.** Chrome n'ouvre que des URLs publiques. Aucune action authentifiée non autorisée.
- **Aucun forçage d'indexation.** Pas de soumission GSC, pas de force-crawl.
- **Aucun scraping Google automatique** depuis l'extension (CAPTCHA, fiabilité nulle). Le check #8 passe par le croisement GSC, pas par `site:` automatisé.
- **Pas de modification du site.** Sortie limitée au rapport dans la conversation.
- **Distinction stricte** "non indexée" vs "non testable" vs "présomption (absente GSC)". Une page absente de la GSC est une **présomption**, pas une conclusion.
- **Priorité au signalement** : une page business absente de la GSC ou un `noindex` accidentel remontent en TOP du rapport.
- Si un check échoue, continuer les autres et le consigner dans "Limites".

> Discipline : observation côté agent, décision côté humain.

## Variante haute fiabilité — GSC URL Inspection API

Si service account Google Cloud + propriété GSC : interroger l'endpoint URL Inspection (`INDEXED`, `DISCOVERED_NOT_INDEXED`, `CRAWLED_NOT_INDEXED`, `URL_IS_UNKNOWN_TO_GOOGLE`). Passe le check #8 de présomption à statut officiel 100 % fiable. Setup ~30 min. C'est le seul moyen de transformer la "présomption non-indexée" en certitude.

## Réutilisation client

1. Pointer le sitemap public + récupérer l'export GSC du client (ou brancher Windsor.ai sur sa propriété)
2. Adapter le périmètre maillage (hubs du site)
3. Refaire le croisement mensuellement, inclure le rapport dans la note de suivi

Coût marginal : ~15 min de setup, 0 € récurrent.

=====

## Note pour Tim (interne)

- **Décision (b) actée** : variante Cowork écrite. 7/9 checks identiques à la version terminale, 2 dégradés proprement en "non testable" (X-Robots-Tag, redirects multi-sauts), check #8 **renforcé** : croisement GSC (plus fiable que le `site:` scraping de la version terminale, ~40-60 %) — et les participants ont DÉJÀ l'export GSC via la Phase 0 du workflow, donc zéro outil en plus.
- **Même nom de skill** (`indexation-check`) dans les deux variantes : un participant installe celle qui matche son setup, la Phase 1 du workflow ne change pas. Bien marteler "une seule des deux, pas les deux" dans le message WhatsApp (sinon collision de skills chez les bidouilleurs).
- **Nouvelle dépendance d'ordre** : le check #8 Cowork a besoin de l'export GSC de la Phase 0. Dans le séquençage S3, la Phase 0 est déjà au J1 avant la Phase 1 — ordre cohérent, rien à changer. Juste vérifier que le message J1 fait bien produire l'export GSC AVANT de lancer `indexation-check`.
- **Windsor.ai** : mentionné comme alternative au CSV, pas comme obligation (le CSV de Phase 0 suffit). Ne pas en faire un prérequis, ça rajouterait une connexion MCP à débugger pour le groupe.
- Si tu mets à jour le skill canonique terminal, répercute ici (les 9 checks doivent rester alignés entre les deux variantes).
