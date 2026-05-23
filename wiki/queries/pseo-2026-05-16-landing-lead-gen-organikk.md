---
name: pSEO Organikk — Landing pages lead-gen sur problématique SEO
date: 2026-05-16
type: pseo-strategy
status: phase-1-ready
template: src/app/strategies/[slug]/page.tsx + src/app/templates/5-offer (figés)
deploy_target: src/data/strategies.ts (organikk-next)
head_terms: ["agence seo", "consultant seo", "expert geo", "seo + geo"]
variable: problématique SEO commerciale (pain-first / solution-first / escape / persona)
anti_cannibalisation: pseo-2026-05-13-organikk-secteur-ville (local métier×ville ≠ ce doc national B2B/pain)
parent: [[cluster-business-organikk-source]] · [[modele-roadmap-premier-call]] · [[analyse-calls-prospects-bootcamp]]
---

# pSEO Organikk — Landing pages lead-gen indexées sur la problématique SEO

> Objectif : transformer chaque problématique SEO réellement verbalisée par un prospect (extraite des calls bootcamp + cas clients) en **une landing page service** sur un template figé, qui ranke sur une longue traîne commerciale et déclenche un RDV / une candidature.
> Variable = la problématique. Template = le modèle de page donné par Tim.

## 0. Cadrage — ce que ce doc ajoute (anti-doublon)

Il existe déjà `[[pseo-2026-05-13-organikk-secteur-ville]]` : modèle **métier local × ville** (serrurier Lyon, agence immo Marseille…), intention *local pack*, head term "stratégie seo {métier} {ville}". **Ce doc-ci ne le re-fait pas.** Ici on adresse 4 angles distincts, tous nationaux / B2B / sans dépendance au pack local :

1. **Pain-first** — le prospect cherche son symptôme ("mon trafic SEO a chuté", "je ne suis pas cité par ChatGPT").
2. **Solution-first** — le prospect cherche un livrable qu'il sait nommer ("audit SEO GEO", "refonte maillage interne").
3. **Escape / situation** — le prospect veut sortir d'un état ("SEO sans backlinks", "refaire son SEO après une agence").
4. **Praticien** — freelance/dev qui veut monter une offre SEO IA (funnel bootcamp/coaching).

Garde anti-cannibalisation : aucun de ces 4 angles ne reprend le pattern `{métier}+{ville}`. Si un slug pain croise un secteur, il reste **national et sans nom de ville** (canonical distincte, SERP distincte).

### Pages déjà live à NE PAS dupliquer

`/services` · `/coaching-seo-lyon` · `/accompagnement-seo-geo` · `/accompagnement-1-1-30-jours` · `/bootcamp` · `/freelance-geo-lyon` · `/secteurs/avocat` · `/secteurs/hotellerie` · `/strategies/{paysagiste-paris, avocat-paris, hotel-paris, centre-formation-ia}` · `/methode` · `/etudes-de-cas` · `/outils/{simulateur-roi-seo, analyse-geo}`

Les nouvelles pages **maillent vers** ces pages (offre + preuve) mais ne ré-expliquent pas l'offre : elles partent de la problématique.

---

## 1. Les 5 modèles scalables

Chaque modèle = même squelette de template (celui de Tim), variable différente, intention différente → pas de cannibalisation inter-modèles.

### Template figé commun (le modèle donné par Tim, calibré Organikk)

```
URL          /seo/[slug]  |  /secteurs/[slug]  |  /expertise/[slug]  |  /seo-sans-[slug]  |  /seo-ia-pour-[slug]
H1           [Service Organikk] qui [bénéfice business mesurable lié à la variable]
Sous-titre   reformule la problématique avec le verbatim prospect (1 phrase)
H2 #1        Le problème que tu rencontres   → diagnostic + 1 verbatim réel + 1 chiffre sourcé (High Surprise)
H2 #2        Notre approche                  → la doctrine appliquée à CETTE problématique (pas l'offre générique)
H2 #3        Comment ça se passe             → 3-4 étapes datées + livrables concrets
H2 #4        Résultats concrets              → 1 cas client chiffré + bloc authorship ~50 mots (Position 0)
H2 #5        Pour qui c'est fait / pas fait  → ICP explicite + anti-ICP (filtre les mauvais leads)
H2 #6        FAQ                             → 5-7 Q micro-intentions (FAQPage schema)
CTA          Prendre un RDV de 30 min (diagnostic + roadmap 90 j)  [secondaire : voir la méthode / un cas]
Schema.org   Service + FAQPage + BreadcrumbList
```

| # | Modèle | Pattern URL | Head term + modificateur | Variable (source données) | N pages réalistes | Intention / funnel | Compétition |
|---|---|---|---|---|---|---|---|
| **M1** | Problématique résolue (pain-first) | `/seo/[problématique]` | "[symptôme] que faire / corriger" + "agence seo [symptôme]" | Pains verbalisés (`analyse-calls-prospects-bootcamp.md`, cas clients) | 15-18 | Know→Do · BOFU | Faible→Moyenne (GEO-era) |
| **M2** | Secteur B2B expert × SEO+GEO | `/secteurs/[secteur]` | "agence/consultant seo [secteur B2B]" + "geo" | Verticales expertes nationales (strategies.ts + cas) | 10-12 | Do · BOFU | Moyenne |
| **M3** | Livrable × bénéfice (solution-first) | `/expertise/[livrable]` | "[livrable seo] prestation/consultant" | Les tâches des 9 skills (décrites, pas nommées) | 8-9 | Do · MOFU/BOFU | Moyenne→Forte |
| **M4** | Situation / alternative (escape) | `/seo-sans-[X]` · `/refaire-...` | "seo sans [X]" + "alternative à [approche]" | Objections récurrentes des calls | 6 | Do · BOFU | Faible |
| **M5** | Praticien → monter une offre SEO IA | `/seo-ia-pour-[persona]` | "se former / vendre du seo ia quand on est [persona]" | Sous-avatars ICP des calls | 6 | Do · BOFU (funnel bootcamp/coaching) | Faible |

> **Avantage compétitif non copiable** (transverse) : les verbatims prospects réels, les chiffres de cas clients (ex. closing 10 %→50 %, rédaction 1h30→45 min), le scoring propriétaire et le positionnement "freelance-pair, pas formateur". Un concurrent qui scrape la SERP ne peut pas reconstruire ça : la donnée vient des calls, pas du web.

---

### M1 — Problématique résolue (le modèle #1 à lancer)

Variable = un symptôme que le prospect tape ou décrit. Chaque page = ce symptôme → diagnostic → ce qu'on fait → preuve → RDV.

| Slug | Verbatim source (KB) | H1 (gabarit) | Offre ciblée par le CTA |
|---|---|---|---|
| `/seo/trafic-en-chute` | "Mon trafic SEO a chuté depuis août" | Reprendre le trafic quand il s'effondre, sans repartir de zéro | Accompagnement SEO+GEO |
| `/seo/pas-cite-par-chatgpt` | "Je ne suis pas cité par ChatGPT / Perplexity" | Être cité par ChatGPT et Perplexity quand tu n'apparais nulle part | Accompagnement SEO+GEO |
| `/seo/trafic-sans-leads` | "Je génère du trafic mais zéro leads" | Transformer un trafic SEO mort en demandes de devis | Accompagnement SEO+GEO |
| `/seo/cannibalisation` | "Cannibalisation sur mes mots-clés internes" | Sortir de la cannibalisation interne sans tout casser | Audit → Accompagnement |
| `/seo/pages-non-indexees` | "Mes pages ne sont pas indexées" | Faire indexer les pages que Google ignore | Audit → Accompagnement |
| `/seo/contenu-ia-generique` | "Je fais du contenu que ChatGPT fait mieux" | Sortir du contenu générique que les LLM recopient | Accompagnement SEO+GEO |
| `/seo/dependance-google-ads` | "Le SEA est mort, j'en dépends trop" | Réduire la dépendance au SEA par de l'organique qui convertit | Accompagnement SEO+GEO |
| `/seo/dependance-annuaires` | "Je dépends trop de Booking / annuaires" | Récupérer la relation client captée par les annuaires | Accompagnement SEO+GEO |
| `/seo/agence-precedente-zero-resultat` | "J'ai testé une agence, zéro résultat" | Refaire un SEO qui n'a rien donné, sans rejouer les mêmes erreurs | Accompagnement / Audit |
| `/seo/saturation-mots-cles-volume` | "Je suis sur les volumes, pas les micro-intentions" | Quitter les mots-clés saturés pour des requêtes qui ferment | Accompagnement SEO+GEO |
| `/seo/audit-40-pages-inutile` | "Je reçois des audits backlinks, pas du business" | Un diagnostic SEO qui parle chiffre d'affaires, pas backlinks | Audit |
| `/seo/closing-seo-faible` | "Je vends le SEO à 10 %" | Vendre une prestation SEO avec une roadmap chiffrée avant signature | Bootcamp / Coaching |
| `/seo/process-redemarre-zero` | "Je redémarre à zéro chaque client" | Industrialiser un process SEO réutilisable client après client | Bootcamp / Coaching |
| `/seo/scaler-sans-thin-content` | "Créer 100s de pages sans thin content" | Scaler des centaines de pages SEO sans tomber dans le thin content | Accompagnement / Bootcamp |
| `/seo/visibilite-sans-revenu` | "Visibilité, ça veut dire quoi ?" | Relier la visibilité SEO à des leads, pas à un graphe qui monte | Accompagnement SEO+GEO |

(15 slugs phase 1 ; 3 réserves : `/seo/depasse-par-le-rythme-ia`, `/seo/process-non-approprie`, `/seo/peur-etre-remplace-par-ia` → orientent bootcamp.)

**Sous-sections du H2 #2 ("Notre approche") = la tâche d'un skill, décrite jamais nommée** (règle feedback_skills_jamais_nommes_public) :
- chute de trafic → cartographie d'entités + GEO ; cannibalisation → diagnostic des pages en conflit + plan fusion/301 ; non-indexées → audit d'indexation 9 points ; trafic sans leads → outils interactifs + maillage ; closing faible → roadmap 90 j chiffrée.

---

### M2 — Secteur B2B expert × SEO+GEO

Extension du pattern `/secteurs/avocat|hotellerie` déjà live. **Verticales nationales expertes** (pas de ville → pas de doublon avec le pSEO local).

Variables phase 1 : `cabinet-conseil`, `expert-comptable`, `btp-garantie-decennale`, `clinique-sante-privee`, `saas-b2b`, `formation-pro-cpf`, `cabinet-recrutement`, `industrie-equipementier`, `architecte`, `agence-communication`. (10 ; `biotech-medtech` + `cabinet-rh` en réserve.)

H1 gabarit : *"SEO + GEO pour [secteur] : des demandes qualifiées sans dépendre des annuaires"*. Chaque page reprend les **micro-intentions décisionnelles du secteur** (déjà modélisées dans `strategies.ts` pour avocat/paysagiste/hôtel → même méthode, données propres au secteur).

---

### M3 — Livrable × bénéfice (solution-first)

Le prospect sait nommer ce qu'il veut. Variable = le livrable, décrit comme une **tâche** côté public.

| Slug | H1 gabarit | Tâche (skill interne) | CTA |
|---|---|---|---|
| `/expertise/audit-seo-geo` | L'audit SEO qui te dit où sont les leads, pas où sont les backlinks | audit 4-piliers | Audit |
| `/expertise/strategie-geo` | Être la source que ChatGPT et Perplexity citent | cluster AEO | Accompagnement |
| `/expertise/refonte-maillage-interne` | Récupérer les pages orphelines et le link equity perdu | maillage système | Accompagnement |
| `/expertise/cocon-semantique` | Construire l'autorité thématique qui fait ranker tout le cluster | cluster/cocon | Accompagnement |
| `/expertise/seo-programmatique` | Des centaines de pages qui rankent, zéro thin content | pSEO | Accompagnement |
| `/expertise/contenu-anti-ia` | Du contenu que les LLM citent au lieu de le réécrire | entités + workflow article | Accompagnement |
| `/expertise/audit-cannibalisation` | Arrêter de se faire concurrence à soi-même | cannibalisation | Audit |
| `/expertise/quick-wins-seo` | Les gains SEO récupérables en 2 semaines | quick-win | Audit |
| `/expertise/outil-interactif-seo` | Un calculateur qui capte des emails pendant qu'il ranke | product-led | Accompagnement / freelance GEO |

---

### M4 — Situation / alternative (escape) — sans jamais nommer un concurrent

Règle feedback_jamais_regarder_concurrents + feedback_no_tool_names_publie : aucune marque, aucun outil cité. On parle d'un *état*, pas d'un acteur.

`/seo-sans-backlinks` · `/seo-sans-google-ads` · `/seo-sans-agence-classique` · `/refaire-son-seo-apres-une-agence` · `/seo-sans-thin-content` · `/sortir-des-annuaires` (6).

---

### M5 — Praticien → monter / vendre une offre SEO IA (funnel bootcamp/coaching)

Cible = l'avatar principal des calls (freelance/dev qui monétise sans système). CTA = candidature bootcamp ou coaching.

`/seo-ia-pour-freelance-seo` · `/seo-ia-pour-developpeur-web` · `/seo-ia-pour-consultant-digital` · `/seo-ia-pour-redacteur` · `/seo-ia-pour-agence` · `/vendre-du-seo-en-2026` (6).

---

## 2. Matrice de priorisation

Échelle 1-5. Score = (Impact SEO + Conversion + Données dispo) − Effort.

| Modèle | Pages | Effort (1=lourd) | Impact SEO | Conversion | Données propres dispo | **Score** | Verdict |
|---|---|---|---|---|---|---|---|
| **M1 Pain-first** | 15-18 | 3 | 4 | **5** | **5** (verbatims KB) | **17** | 🥇 Lancer en premier |
| **M3 Livrable** | 8-9 | 4 (contenu ≈ déjà dans les skills) | 4 | 4 | **5** | **17** | 🥈 En parallèle (rapide) |
| **M5 Praticien** | 6 | 4 | 3 | **5** (bootcamp 590€) | 4 | **16** | 🥉 Vague 2 |
| **M2 Secteur B2B** | 10-12 | 2 (recherche micro-intentions/secteur) | **5** | 4 | 3 | **14** | Vague 2-3 |
| **M4 Escape** | 6 | 4 | 3 | 4 | 3 | **14** | Vague 3 (volume faible mais closing fort) |

Critère décisif respecté : **compétition faible + données propriétaires** → M1 et M3 cochent les deux.

---

## 3. Mots-clés par modèle (longue traîne, échantillon — à valider GSC/terrain)

**M1** (15) : "mon trafic seo a chuté que faire", "perte de trafic seo google août", "ne pas être cité par chatgpt", "apparaître dans les réponses perplexity", "comment générer des leads avec le seo b2b", "trafic seo mais pas de clients", "résoudre cannibalisation mots-clés", "pages non indexées par google solution", "contenu seo trop générique ia", "réduire dépendance google ads seo", "sortir de la dépendance booking hôtel", "refaire son seo après une mauvaise agence", "audit seo orienté business pas backlinks", "vendre une prestation seo à un client", "scaler du contenu seo sans thin content". *(Intention : Know→Do · BOFU · compétition faible→moyenne.)*

**M2** (12) : "agence seo cabinet de conseil", "consultant seo expert-comptable", "seo garantie décennale btp", "seo clinique privée", "seo saas b2b génération de leads", "référencement organisme de formation cpf", "geo cabinet de recrutement", "seo industriel équipementier", "seo architecte", "agence seo b2b éthique" (déjà ciblé via page existante → maillage, pas duplication), "être cité par les ia secteur conseil", "seo + geo pour experts b2b". *(Do · BOFU.)*

**M3** (12) : "audit seo geo", "prestation stratégie geo", "consultant geo être cité par chatgpt", "refonte maillage interne agence", "construire un cocon sémantique", "agence seo programmatique", "création contenu seo anti ia", "audit de cannibalisation seo", "quick win seo agence", "outil interactif seo lead generation", "audit seo 4 piliers", "prestation seo orientée conversion". *(Do · MOFU/BOFU.)*

**M4** (10) : "faire du seo sans backlinks", "ranker sans netlinking", "seo sans google ads", "alternative agence seo classique", "refaire son seo après une agence", "seo sans thin content programmatique", "sortir des annuaires payants", "ne plus dépendre de booking", "récupérer la relation client annuaires", "seo propriétaire vs agence". *(Do · BOFU · compétition faible.)*

**M5** (10) : "se former au seo ia", "vendre du seo en 2026", "système seo pour freelance", "seo ia pour développeur web", "monter une offre seo récurrente", "industrialiser son process seo", "consultant digital ajouter le seo", "rédacteur web passer au seo ia", "agence seo un process plusieurs consultants", "bootcamp seo ia freelance". *(Do · BOFU · funnel formation.)*

---

## 4. Plan d'exécution 90 jours

**Prérequis techniques (avant M0)**
- Créer les dossiers de route : `src/app/seo/[slug]/`, `src/app/expertise/[slug]/`, étendre `src/app/secteurs/[slug]/`. Lire le guide App Router dans `node_modules/next/dist/docs/` (cf. AGENTS.md organikk-next : ce n'est pas le Next.js standard).
- Modèle de page = `src/app/strategies/[slug]/page.tsx` (déjà figé, structure validée) ou `templates/5-offer` ; data dans `src/data/strategies.ts`.
- Schema.org `Service` + `FAQPage` + `BreadcrumbList` ; canonical = 1 slug = 1 contenu.
- `sitemap` + `internal-links.ts` à jour à chaque page (anti-orpheline).

**Mois 1 (M0) — M1 pages 1 à 8 (les 8 pains les plus chiffrables)**
- S1 : `trafic-en-chute`, `pas-cite-par-chatgpt` — sourcer 1 verbatim + 1 chiffre + 1 cas par page.
- S2 : `trafic-sans-leads`, `cannibalisation`.
- S3 : `pages-non-indexees`, `contenu-ia-generique`.
- S4 : `dependance-google-ads`, `agence-precedente-zero-resultat` + maillage croisé + sitemap.

**Mois 2 (M1) — M1 pages 9 à 15 + M3 démarrage**
- S5-S6 : 7 derniers slugs M1.
- S7-S8 : M3 `audit-seo-geo`, `strategie-geo`, `refonte-maillage-interne`, `audit-cannibalisation` (contenu majoritairement réutilisable des skills → rapide).

**Mois 3 (M2) — fin M3 + M5 + refresh**
- S9-S10 : M3 restants (5).
- S11 : M5 (6 pages praticien → bootcamp/coaching).
- S12 : refresh M0 (données fraîches, ajout cas clients récents), audit indexation des 30 pages, contrôle cannibalisation inter-pages.

**Hypothèses conversion (prudentes — à remplacer par data réelle)**
≈ 30 pages live fin T1. Trafic et taux de RDV : `[DONNÉE À SOURCER via GSC après 60-90 j]`. Ne pas publier de projection chiffrée tant que non mesuré.

---

## 5. Les 7 règles, calibrées pour ces landings

1. **Anti-thin** : le H2 "Le problème" + "Notre approche" + le cas client diffèrent à 100 % entre deux pages (verbatim + chiffre + livrable propres). Seuls le CTA et le bloc "Pour qui" partagent un socle (< 30 %).
2. **Données terrain** : tout chiffre vient des cas clients KB ou est `[DONNÉE À SOURCER]`. Zéro projection inventée.
3. **Sourcing** : chaque stat = source + organisme + année (ex. l'étude "conversions LLM vs Google" → vérifier source exacte avant publication, ne pas citer de mémoire).
4. **Canonical propre** : 1 slug = 1 contenu ; pas de slug pain qui recoupe un slug livrable sur la même requête (M1 part du symptôme, M3 du livrable → SERP distinctes ; vérifier au lancement).
5. **Maillage différenciant** : chaque page pointe vers un trio unique = 1 cas client + 1 page méthode + 1 offre. Jamais le même trio deux fois (varier les ancres, cf. feedback_seo_vocabulaire).
6. **Surprise Score** : ≥ 1 élément High Surprise / section (un verbatim cru, un contre-intuitif type "le SEA est mort", un chiffre de cas client).
7. **Grounding Score** : 1 passage ancré 150-200 mots (le diagnostic concret de la problématique) + bloc authorship ~50 mots extractible Position 0 par page.

**Garde-fous éditoriaux (mémoire Tim)** : pas d'em-dash (feedback_no_em_dashes), pas de phrases staccato dans CTA/intro (feedback_no_staccato_publie), anti-AI-writing ([[concepts/anti-ai-writing]]), aucun concurrent ni outil nommé, skills jamais nommés en public, H2 en gradient sur les sous-titres majeurs.

---

## 6. Résumé exécutif (5 phrases)

Chaque problématique SEO réellement verbalisée par un prospect dans les calls bootcamp devient une landing page sur un template figé qui ranke sur sa longue traîne commerciale et pousse un RDV. On retient 5 modèles MECE par intention (pain, secteur, livrable, escape, praticien), 45 pages possibles en phase 1, sans dupliquer le pSEO local métier×ville ni les pages d'offre déjà live. Le moat n'est pas copiable : verbatims de calls + chiffres de cas clients + scoring propriétaire, invisibles depuis la SERP. Priorité absolue : **M1 "Problématique résolue"** (conversion 5/5, données propres 5/5, compétition faible sur les pains GEO-era), M3 "Livrable" en parallèle car le contenu existe déjà dans les workflows. Premier sprint : 8 pages M1 chiffrables en 4 semaines, CTA unique = RDV 30 min avec roadmap 90 j chiffrée (le mécanisme qui fait passer le closing de 10 % à 50 %).

## 7. Prochaine étape opérationnelle

Valider le périmètre M1 (15 slugs) avec Tim → scaffolder la route `src/app/seo/[slug]/` + entrées `strategies.ts` pour les 2 premières pages (`trafic-en-chute`, `pas-cite-par-chatgpt`) en réutilisant le template figé, puis dérouler le plan 90 j.
