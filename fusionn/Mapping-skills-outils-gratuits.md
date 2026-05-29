---
date: 2026-05-29
sujet: Mapping de chaque skill SEO vers des outils gratuits (Product-Led SEO)
statut: draft v1, à arbitrer avec Tim
---

# Mapping skills → outils gratuits Fusionn

Pour chaque skill du dossier `~/.claude/skills/`, les outils gratuits qualitatifs qu'on peut en tirer (le skill entier ou juste une partie).

Légende statut :
- 🟢 en ligne sur fusionn.co
- 🟡 brief déjà rédigé (`Briefs-outils-product-led-seo.md`), pas encore codé
- 🔵 nouveau, à arbitrer

Faisabilité : « déterministe » = 0 LLM, gratuit, ne peut pas halluciner. « 1 call » = un appel Gemini Flash, coût marginal. « data » = source de données mobilisée.

---

## A. Mots-clés

**1. Générateur Google Suggest** `/generateur-mots-cles-google-suggest` — 🟢
Skill : seo-recherche-mots-cles. Expansion A-Z + modificateurs.
Requête Do : `générateur mots-clés gratuit`. Data : Google Suggest (gratuit). Déjà live.

**2. Explorateur de questions (People Also Ask / questions Suggest)** — 🔵
Skill : seo-recherche-mots-cles (partie « micro-intentions »). Tu entres un mot-clé, il sort les questions réelles (qui / quoi / comment / pourquoi / prix / avis) tapées autour.
Requête Do : `questions que se posent les gens sur [X]`, `people also ask outil`. Data : Suggest + variantes interrogatives (gratuit, déterministe). Extension naturelle de l'outil 1.

**3. Clusteriseur de mots-clés** — 🔵
Skill : seo-clustering-mots-cles (le skill entier). Tu colles une liste brute de N mots-clés, il les regroupe en clusters (1 cluster = 1 page) par proximité d'intention, nomme chaque cluster et désigne le pivot. Détecte les doublons / risques de cannibalisation.
Requête Do : `regrouper mots-clés outil`, `keyword clustering gratuit`, `quels mots-clés sur la même page`. Data : 1 call (ou embeddings côté client). Fort potentiel, peu d'équivalents FR gratuits.

**4. Détecteur de mots-clés qui convertissent** — 🔵 ⭐
Skill : seo-mots-cles-decisionnels (le skill entier). Tu colles ta liste, il classe chaque requête info vs décisionnel via les modificateurs (prix, tarif, avis, meilleur, comparatif, près de moi, devis…) et sort une shortlist triée par potentiel de conversion.
Requête Do : `mots-clés transactionnels`, `trier mots-clés par conversion`, `mots-clés qui rapportent`. Data : lexique de modificateurs, **100 % déterministe, 0 LLM, gratuit, infalsifiable**. Très on-doctrine (anti-LLM, focus Do).

---

## B. Sémantique et contenu

**5. Score sémantique** `/score-semantique` — 🟢
Skill : seo-preparation-semantique (mode audit) + seo-entites-vectorielles. Déjà live.

**6. Analyse de texte / GEO** `/analyse-texte` — 🟢
Skill : seo-geo-audit + seo-preparation-semantique. Produit principal. Déjà live (recouvre largement l'audit GEO).

**7. Cartographe d'entités sémantiques** — 🔵
Skill : seo-entites-vectorielles (partie « tableau d'entités »). Tu entres une requête cible, il sort les entités/termes à inclure par catégorie (techniques, preuves quantitatives, multimodal, divergence) avec densité cible.
Requête Do : `quels termes inclure dans ma page`, `entités sémantiques [mot-clé]`, `optimisation sémantique outil`. Data : 1 call. Recouvrement partiel avec Score sémantique : à positionner comme le volet « avant rédaction » (input) vs Score sémantique « après » (audit).

**8. Générateur de structure Hn** `/structure-h2-h3-seo` — 🟢
Skill : seo-brief-contenu (partie « structure Hn »). Déjà live.

**9. Générateur de brief SEO complet** — 🔵
Skill : seo-brief-contenu (le skill entier). Étend l'outil 8 : Hn + entités + micro-intentions + signaux E-E-A-T + format multimodal. Lourd, plutôt lead magnet PDF qu'outil instantané.
Requête Do : `brief SEO gratuit`, `plan de rédaction SEO`. Data : 1 call long.

**10. Carte sémantique vierge (mode création)** — 🔵
Skill : seo-preparation-semantique (mode création, 11 couches). Une requête, il génère tout ce que la page devrait contenir avant d'écrire une ligne. Différenciant fort, mais lourd : candidat lead magnet plutôt qu'outil léger.
Requête Do : `analyse sémantique [mot-clé]`, `préparation sémantique`. Data : 1 call long.

---

## C. Conversion et copy

**11. Détecteur d'IA writing / Anti-slop** — 🔵 ⭐
Skill : ton-de-voix-tim (checklist anti-AI writing). Tu colles ton texte, il surligne les patterns d'IA writing : tirets cadratins, mots interdits (crucial, comprehensive, landscape…), phrases en miroir, conclusion-résumé, formules creuses. Note un « score de slop ».
Requête Do : `mon texte fait-il IA`, `détecteur texte IA gratuit`, `anti AI writing`. Data : lexique + regex, **déterministe, 0 LLM**. Très viral, très on-brand, gratuit. Aucun équivalent FR sérieux.

**12. Générateur de peurs et objections** — 🔵
Skill : seo-peurs-objections (le skill entier). Tu entres thématique + persona, il sort un tableau pain points + verbatims « Haute Surprise » + les 3 objections critiques avec où les traiter.
Requête Do : `objections clients [secteur]`, `pain points outil`, `freins à l'achat`. Data : 1 call. Utile pour les rédacteurs et les pages de vente.

---

## D. Architecture et pSEO

**13. Générateur de cocon sémantique (cluster AEO)** — 🔵
Skill : seo-cluster-aeo (le skill entier). Un mot-clé pilier, il sort les 15+ pages satellites classées Know-Simple / Know / Do + le plan de maillage.
Requête Do : `créer un cocon sémantique`, `architecture de contenu outil`, `topical authority`. Data : 1 call. Différenciant (cadre Know/Do propre à Tim).

**14. Générateur de pages satellites (Money Page → Spokes)** — 🔵
Skill : seo-modeles-pseo (le skill entier). Tu décris ton offre + point de conversion, il génère les requêtes Ultra Business réellement tapées et les modèles de pages décisionnelles scorés (Proximité × Intention × Faisabilité).
Requête Do : `pages décisionnelles autour de mon offre`, `money page spokes`. Data : 1 call. Très commercial.

**15. Détecteur de modèles pSEO scalables** — 🔵
Skill : seo-programmatique-pseo (partie « identifier modèles »). Tu décris ton site/base de données, il propose des modèles template + variable et estime le volume de pages.
Requête Do : `programmatic SEO outil`, `créer des centaines de pages`. Data : 1 call.

**16. Roadmap SEO 30/60/90** — 🔵
Skill : seo-roadmap-pseo (le skill entier). Une thématique, il sort une roadmap 2 phases (transactionnel d'abord, info ensuite) lisible par un prospect.
Requête Do : `roadmap SEO`, `par où commencer en SEO`, `plan d'action SEO`. Data : 1 call. Excellent lead magnet / outil de RDV de découverte.

**17. Détecteur de pages orphelines / audit de maillage** — 🔵 ⭐
Skill : maillage-systeme (le skill entier, sans GSC). Tu colles un sitemap ou une liste d'URLs, il crawle le maillage interne et sort les orphelines, les dead-end, la profondeur, les hubs.
Requête Do : `pages orphelines outil`, `audit maillage interne gratuit`, `détecteur pages orphelines`. Data : crawl HTTP (gratuit, déterministe). Pas besoin de GSC, donc zéro friction. Fort.

**18. Analyseur de maillage interne (GSC)** — 🔵
Skill : maillage-interne-gsc (le skill entier). Tu uploades un export GSC + structure, il sort la hiérarchie mère / fille / orpheline et un plan de maillage Know→Do.
Requête Do : `maillage interne GSC`, `cocon SEO outil`. Data : parsing CSV côté client (gratuit). Friction : demande un export GSC.

---

## E. Technique

**19. Détecteur de quick wins SEO (GSC)** — 🔵 ⭐
Skill : seo-quick-win (le skill entier). Tu uploades ton export GSC, il sort les pages position 3-12 à fort volume d'impressions et CTR sous-performant, avec les leviers (title, méta, H1, FAQ).
Requête Do : `quick win SEO`, `pages proches du top 3`, `améliorer CTR SEO`. Data : parsing CSV, **déterministe, 0 LLM, gratuit**. Très actionnable, ROI immédiat pour l'utilisateur.

**20. Détecteur de cannibalisation (GSC)** — 🔵
Skill : seo-cannibalisation (le skill entier). Upload GSC, il repère les pages en compétition sur les mêmes requêtes, classe le type de conflit et recommande l'action (301, fusion, différenciation).
Requête Do : `cannibalisation SEO outil`, `deux pages même mot-clé`. Data : parsing CSV (déterministe). Friction : export GSC.

**21. Générateur de JSON-LD (données structurées)** — 🔵 ⭐
Skill : seo-donnees-structurees (partie génération). Tu remplis un formulaire, il sort le JSON-LD valide (Article, FAQPage, HowTo, BreadcrumbList, VideoObject).
Requête Do : `générateur json-ld`, `schema.org generator`, `générateur données structurées`. Data : **client-side, déterministe, 0 coût**. Requête Do à très gros volume, outil classique mais toujours recherché.

**22. Vérificateur d'indexation** — 🔵
Skill : indexation-check (le skill entier). Tu colles une liste d'URLs ou un sitemap, il check statut HTTP, noindex, présence sitemap, cohérence. Honnête sur la limite (statut Google réel = rate-limité, non garanti).
Requête Do : `vérifier indexation`, `mes pages sont-elles indexées`. Data : fetch HTTP (gratuit, déterministe).

**23. Audit Core Web Vitals** — 🔵
Skill : seo-core-web-vitals (le skill entier). URL → scores LCP / CLS / TBT mobile + 5 pires pages.
Requête Do : `audit core web vitals gratuit`, `score Lighthouse`. Data : API PageSpeed Insights (gratuite). Différenciation faible (PageSpeed existe déjà), à positionner « lecture SEO » du résultat.

---

## F. Méta et adjacents

**24. Test de citation IA (Citation Probe)** `/test-citation-ia-gemini` — 🟢
Skill : seo-geo-audit / cluster AEO. Déjà live.

**25. Comparateur Volume vs Score Business** `/comparateur-volume-business-seo` — 🟢
Skill : seo-mots-cles-decisionnels + recherche. Déjà live.

**26. Générateur d'idées d'outils SEO (méta)** — 🔵
Skill : seo-product-led-seo. Tu entres une thématique, il propose 5 concepts d'outils gratuits avec Surprise Gap. Niche (cible les SEO eux-mêmes), mais cohérent avec le positionnement Fusionn.

Skills non retenus pour un outil public : article-engine-pipeline et seo-workflow-article (rédaction long format, pas un outil instantané), kb-semantic-search / todo / organikk-* / bxble-directory / fusionn-trends-quotidien (hors périmètre outils publics Fusionn).

---

## Recommandations : les 6 à shipper en priorité

Critère : déterministe (gratuit, fiable, infalsifiable) OU 1 call léger, requête Do qui ne se fait pas manger par un AI Overview, et différenciation réelle.

1. **Détecteur de mots-clés qui convertissent** (4) — déterministe, doctrine pure.
2. **Détecteur de quick wins GSC** (19) — déterministe, ROI immédiat utilisateur.
3. **Détecteur d'IA writing / anti-slop** (11) — déterministe, viral, signature Tim.
4. **Générateur de JSON-LD** (21) — déterministe, gros volume de recherche.
5. **Clusteriseur de mots-clés** (3) — 1 call, peu de concurrents FR gratuits.
6. **Détecteur de pages orphelines / audit maillage** (17) — déterministe, zéro friction (pas de GSC requis).
