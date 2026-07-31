---
date: 2026-07-31
sujet: Outils gratuits Product-Led SEO pour qadence.io — mapping skills + recherche marché
statut: draft, à arbitrer avec Tim
skill: seo-product-led-seo
---

# Outils gratuits à créer pour Qadence.io

Méthode : skill `seo-product-led-seo` (pipeline micro-intentions Do) + deux agents de recherche web sur (1) le paysage général des outils SEO/GEO gratuits en 2026, (2) les outils gratuits déjà en ligne chez les 12 acteurs de la cartographie marché de Tim (Writesonic, Frase, AirOps, Profound, SEO Vendor, Semrush, Peec AI, Otterly, Scrunch, Evertune, Am I on AI, Rankscale). Aucune donnée de trafic ou de volume inventée : ce qui suit vient de recherche web réelle, datée du 31/07/2026, à revérifier avant tout lancement (corpus périssable).

**Résumé** : le terrain classique (générateur de mots-clés, JSON-LD, Core Web Vitals, meta generator, checker de visibilité IA générique) est saturé par des acteurs établis. L'angle le moins disputé et le plus cohérent avec le positionnement lead-gen de Qadence : croiser la vraie donnée Search Console de l'utilisateur (positions, impressions, CTR, citations IA) avec le potentiel de leads. Aucun des 12 acteurs scannés ne le fait.

---

## Déjà en ligne ou en prototype (à ne pas refaire)

- **Extension « Qadence IA »** (`organikk-extension`) — score de maillage interne /100, orphelines, culs-de-sac, textes de lien. En ligne.
- **Extension « Qadence — Performances Search Console »** (`gsc-keyword-tracker`) — clone GSC dans le popup, Vue d'ensemble + Performances. En ligne.
- **Prototype visibilité IA** (`qadence/prototypes/ai-visibility/`) — citations ChatGPT + Gemini sur des sujets dérivés de GSC. Codé, pas encore public/productisé. Base technique de l'outil P1-2 ci-dessous.

---

## Terrain confirmé saturé (à éviter)

| Terrain | Preuve | Acteurs déjà en place |
|---|---|---|
| Générateur de mots-clés générique | recherche web, 6+ formulations | Similarweb Generator, Semrush Keyword Magic, Mangools KWFinder, keywordtool.io |
| Générateur JSON-LD / schema.org | recherche web | jsonld.com, iLoveSchema, Axiolo, InstantSchema, SchemaMarkupGenerators.com |
| Robots.txt / sitemap tester | recherche web | CodeItBro, SearchVector, WebsiteAuditTools |
| Audit Core Web Vitals gratuit | recherche web | PageSpeed Insights / Lighthouse / CrUX (Google lui-même) |
| Générateur meta title/description | recherche web | vague d'outils IA génériques (Grammarly, SE Ranking, RyRob…) |
| Keyword difficulty checker | recherche web | Semrush, Backlinko, Keysearch |
| Checker de visibilité IA générique (sans data personnelle) | recherche web, 10+ acteurs confirmés | Frase (GEO Score Checker), Semrush (AI Search Visibility Checker), HubSpot AEO Grader, Ahrefs, Mangools, MoonRank, QuickSEO, SE Ranking, Am I on AI, Scrunch |
| Audit maillage interne / pages orphelines brut | recherche web | LinkBoss (suite complète gratuite sans compte), SEOAegis, Screaming Frog (500 URLs gratuit) |
| Détecteur de texte généré par IA | recherche web | GPTZero, ZeroGPT, Originality.ai, Copyleaks (+ hors sujet Qadence) |

---

## P1 — à créer en priorité (angle mort confirmé, GSC-exclusif)

### 1. Diagnostic des requêtes GSC à potentiel lead

- **Skill** : `seo-mots-cles-decisionnels` + `seo-quick-win`, appliqués à la vraie donnée GSC (pas une liste collée)
- **Micro-intention Do** : « quelles requêtes de mon site génèrent (ou pourraient générer) des demandes entrantes »
- **Surprise Gap** : aucun outil trouvé dans les deux recherches ne croise positions/impressions/CTR réelles avec une détection d'intention d'achat. Les classificateurs d'intention existants (Ad School Master, SERP Intent Analyzer…) travaillent sur du texte de mot-clé isolé, jamais sur la vraie Search Console du site.
- **Faisabilité** : déterministe (lexique de modificateurs Do, comme `seo-mots-cles-decisionnels`), une fois GSC connectée
- **Action de conversion** : connecter Google Search Console = onboarding direct dans Qadence (pas besoin d'un gate email séparé, la connexion GSC EST la conversion)

### 2. Simulateur de visibilité IA sur les vraies requêtes GSC

- **Skill** : prototype `ai-visibility` existant (ChatGPT + Gemini)
- **Micro-intention Do** : « suis-je cité par ChatGPT sur les mots-clés qui m'amènent déjà du trafic »
- **Surprise Gap** : les 10+ checkers identifiés (Frase, Semrush, HubSpot, Ahrefs…) testent des prompts génériques déconnectés du site réel. Aucun ne part de la Search Console personnelle de l'utilisateur.
- **Faisabilité** : coût API réel (non nul), à gater après un premier passage gratuit (cohérent avec le quota produit existant, 2 audits gratuits à vie)
- **Action de conversion** : rapport complet + suivi dans le temps = compte payant

### 3. Quick win finder GSC sans plafond

- **Skill** : `seo-quick-win`
- **Micro-intention Do** : « quelles pages sont en position 4-20 et prêtes à mieux ranker »
- **Surprise Gap** : le terrain existe (GSC Wizard, GSCTool, Search Console Tools) mais chaque acteur bride son gratuit (GSC Wizard limite à 5 mots-clés). Un outil Qadence sans plafond se différencie par la générosité, pas la nouveauté.
- **Faisabilité** : déterministe, une fois GSC connectée
- **Action de conversion** : finir chaque quick win sur « voici la page à transformer en page de conversion », pas juste la position

### 4. Pages orphelines priorisées par potentiel lead

- **Skill** : `maillage-interne-gsc`, en extension du score déjà livré dans l'extension Qadence IA
- **Micro-intention Do** : « quelles pages orphelines auraient dû me ramener des demandes »
- **Surprise Gap** : LinkBoss et consorts listent les pages orphelines mais aucun ne les priorise par potentiel commercial. Attention : la détection brute d'orphelines est saturée, seule la couche « priorité lead » est différenciante, à ne pas vendre comme un simple clone.
- **Faisabilité** : déterministe (crawl + GSC), complexité moyenne
- **Action de conversion** : liste complète gratuite, plan de maillage détaillé = compte

---

## P2 — solides, terrain moins vérifié par la recherche (pas mentionnés chez les 12 acteurs scannés)

### 5. Roadmap SEO 90 jours orientée leads
Skill `seo-roadmap-pseo`. Do : « plan d'action SEO gratuit », « par où commencer ». Bon lead magnet, angle 90 jours pas retrouvé chez les concurrents scannés.

### 6. Générateur de pages satellites autour d'une page de conversion
Skill `seo-modeles-pseo`. Do : « quelles pages créer autour de mon offre ». Jamais « Money Page » dans la copy, toujours « page de conversion » ou « business page ».

### 7. Audit de cannibalisation GSC
Skill `seo-cannibalisation`. Do : « deux pages sur la même requête ». Pas identifié chez les 12 acteurs scannés, niche mais propre.

---

## Non retenus / à écarter

- Détecteur de texte IA / anti-slop, générateur JSON-LD, checker robots.txt/sitemap, audit Core Web Vitals, générateur meta title/description, générateur de mots-clés générique, keyword difficulty checker, checker de visibilité IA SANS data GSC : terrain saturé par des acteurs établis (voir tableau ci-dessus), aucune différenciation réelle disponible pour Qadence.
- Audit maillage brut (sans priorisation lead) : LinkBoss couvre déjà ce terrain gratuitement et sans friction.

---

## Point de vigilance méthodologique

L'absence de résultat sur une recherche web (notamment pour l'outil P1-1, « diagnostic requêtes GSC à potentiel lead ») ne garantit pas à 100 % qu'aucun petit acteur mal référencé ne le fasse déjà. À reverifier manuellement avant lancement si l'exhaustivité totale est nécessaire.

Sources : recherche web réelle du 31/07/2026 (deux agents dédiés), croisée avec `seo-kb/fusionn/Mapping-skills-outils-gratuits.md` (méthode identique appliquée à Fusionn.co, pour éviter tout doublon entre les deux produits de Tim).
