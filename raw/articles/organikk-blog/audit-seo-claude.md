---
source: "https://organikk.co/blog/audit-seo-claude"
slug: audit-seo-claude
title: "Audit SEO avec Claude : le workflow en 7 phases, Organikk"
author: "Timothée Boussardon"
date_published: 2026-04-05
date_scraped: 2026-04-30
description: "Méthodologie complète d'audit SEO avec Claude en 7 phases. Approche basée uniquement sur les données Google Search Console et la navigation Chrome. Claude Pro à 20 euros par mois suffit, aucun outil tiers payant nécessaire."
type: article-blog-organikk
---

# Audit SEO avec Claude : le workflow en 7 phases, Organikk

Cette méthode pour faire un **audit SEO complet avec Claude** n'utilise qu'un seul outil : **Claude Pro à 20€/mois** et vos données GSC.

Le workflow ci-dessous est ma **méthodologie d'avril 2026, en 7 phases**. Il est conçu pour **donner à Claude exactement le contexte dont il a besoin** pour produire un audit utile, **pas une analyse générique**.

Petite remarque : Il est possible de pousser beaucoup plus loin avec connexion MCP et passage en CLI. Mais ceci est une base pour vous aider à découvrir la puissance de Claude pour votre SEO. Libre à vous de pousser l'approche.

## 01 ·1. Skills

Pour installer un skill sur [[cli-tools-optional|Claude Code]], c'est trois étapes.

D'abord, trouve le dossier des skills. Sur Mac/Linux c'est ~/.claude/skills/, sur Windows c'est %USERPROFILE%\.claude\skills\. S'il n'existe pas, crée-le.

Ensuite, crée un sous-dossier pour ton skill, avec un nom court en kebab-case. Par exemple ~/.claude/skills/mon-skill/. Le nom du dossier c'est le nom du skill.

Enfin, dans ce sous-dossier, crée un fichier SKILL.md. C'est lui qui contient tout. Il commence obligatoirement par un bloc frontmatter YAML avec deux champs : name (identique au nom du dossier) et description (ce qui déclenche le skill, sois précis, Claude s'en sert pour décider quand l'activer). Sous le frontmatter, tu écris les instructions en markdown.

--- name: mon-skill description: À quoi sert ce skill et quand l'utiliser --- # Mon Skill Instructions détaillées ici...

Tu relances Claude Code et le skill est dispo. Tu peux vérifier qu'il est bien chargé en tapant /skills dans Claude Code.

Si ton skill a besoin de fichiers annexes (templates, scripts, références), tu les mets dans un sous-dossier references/ ou scripts/ à côté du SKILL.md, et tu les appelles depuis les instructions.

## 02 ·2. Workflow

Workflow V3. **100% données Google** (GSC + Chrome sur son site). Méthodologie Timothée Boussardon, avril 2026.

### Règles de scrapping de l'audit

- Analyse des URLs de votre site
- Les données viennent de la GSC + la recherche web Claude (qui montre qui est visible)
- Aucun outil payant tiers : tout fonctionne avec Claude Pro (20€/mois) + les données gratuites de Google

## 03 ·Phase 0 : Audit de positionnement

### Audit SEO & GEO sous 48h.

30 min en visio. Je reviens avec une analyse de vos opportunités réelles.

[Réserver 30 min →](https://cal.com/tim-boussardon-yzrrb1/30min)

Skill : Aucun. Collecte de données. Source : Export GSC + recherche web Claude. Durée : 20-30 min.

### Prompt exact

Voici mon export GSC [période]. Et voici mes 5-10 requêtes business principales : [liste] 1. Pour chaque requête business, analyse mes données GSC :

- Ma position moyenne
- Mes impressions et clics
- Mon CTR (et l'écart avec le CTR attendu pour cette position)
- L'URL qui ranke 2. Identifie les requêtes business où je n'apparais PAS dans la GSC → Ce sont mes gaps critiques 3. Via recherche web, pour chaque requête business (y compris mes gaps) :
- Quels types de résultats dominent ? (guides, outils, pages services, annuaires)
- Y a-t-il des [[agentic-search|AI Overviews]] actifs sur cette requête ?
- Quels acteurs sont visibles en top 3 ? (juste les noms et URLs, pas de scrapping) 4. Depuis la GSC, identifie les requêtes à fort volume où je ranke mais qui ne sont PAS dans ma liste de requêtes business → Ce sont mes opportunités cachées Génère un tableau de synthèse : | Requête | Position GSC | Impressions | CTR | CTR attendu | Gap CTR | Type SERP | Priorité |

### Output attendu

- Tableau de positionnement par requête (données GSC réelles)
- Gaps : requêtes business sans présence
- Opportunités cachées : requêtes GSC à fort volume non exploitées
- Types de SERP par requête (via recherche web)

Ce que ça nourrit : Phase 1 (pages sous-performantes = quick wins) et Phase 3 (gaps et opportunités = base des clusters).

## 04 ·Phase 1 : Quick Wins

Skill : seo-quick-win. Source : Export GSC + Chrome (mon site). Durée : 15-20 min.

### Étape 1A, Identifier les opportunités via GSC

Voici mon export GSC [période]. Identifie les quick wins : Critères :

- Pages en position 3-12
- Impressions élevées (top 20% de mes pages)
- CTR sous-performant (écart > 1.5% vs CTR attendu pour la position) Pour chaque quick win, calcule :
- Delta CTR = CTR attendu
- CTR réel
- Impact estimé = Impressions × Delta CTR = clics potentiels gagnés Priorise par impact estimé (du plus élevé au plus bas).

### Étape 1B, Scrapper le contenu de MES pages via Chrome

Connecte-toi à Chrome et navigue sur [URL de mon site]. Pour chaque page identifiée comme quick win : 1. Ouvre MA page et extrait :

- Le title et la meta description actuels
- La structure Hn complète (H1 à H4)
- Le contenu du premier paragraphe (300 premiers mots)
- La présence ou absence de FAQ / données structurées
- Les liens internes entrants et sortants visibles
- La présence de preuves atomiques [Sujet + Relation + Donnée]
- Le nombre de mots total estimé 2. Depuis les données GSC, identifie pour chaque page :
- Toutes les requêtes pour lesquelles cette page reçoit des impressions
- Les requêtes à fort potentiel non exploitées (impressions élevées, position 10+) 3. Compare le title/meta actuel vs les requêtes GSC :
- Le title couvre-t-il les requêtes principales de la GSC ?
- La meta description incite-t-elle au clic pour ces requêtes ? Génère pour chaque page :
- Title actuel → Title recommandé (intégrant les requêtes GSC à fort potentiel)
- Meta actuelle → Meta recommandée
- Actions concrètes classées par impact (immédiat / 1 semaine / 1 mois)

### Étape 1C, Vérifier la présence locale

[Si MCP Local Falcon connecté] Lance un scan de visibilité locale :

- Vérifie la fiche Google Business Profile
- Score de visibilité dans le Local Pack pour les requêtes locales [Si pas de MCP Local Falcon] Vérifier manuellement si une fiche GBP existe. Recommandation : si pas de fiche GBP → création prioritaire (quick win #1).

### Output attendu

- Top 5-10 quick wins avec impact estimé en clics potentiels
- Diagnostic page par page basé sur GSC + contenu réel de mes pages
- Recommandations title/meta basées sur les requêtes GSC réelles
- Statut présence locale

## 05 ·Phase 2 : Détection des cannibalisations

Skill : seo-cannibalisation. Source : Export GSC + Chrome (vérification contenu). Durée : 15-20 min.

Pré-condition : Avant d'exécuter cette phase, vérifie dans l'export GSC combien d'URLs distinctes apparaissent. Si moins de 10 URLs, skip Phase 2 et documente un diagnostic de "sous-granularité" (pas assez de pages pour qu'il y ait de la cannibalisation), puis passe directement à Phase 3.

### Détection via GSC

Dans l'export GSC, détecte les cas de cannibalisation : 1. Pour chaque requête, vérifie si PLUSIEURS URLs de mon site reçoivent des impressions :

- Type A : même requête exacte → plusieurs URLs en impression
- Type B : requêtes très proches (même intention) → URLs différentes 2. Pour chaque conflit détecté, analyse :
- Position moyenne de chaque URL sur la requête
- Impressions et clics de chaque URL
- CTR de chaque URL
- L'une des URLs "vole-t-elle" les impressions de l'autre ?
- Les positions fluctuent-elles (signe que Google hésite) ? 3. Classifie chaque conflit :
- Type A (même mot-clé exact) → risque élevé
- Type B (même intention) → risque moyen
- Type C (proximité sémantique) → à surveiller
- [[triade-serp]] (2+ URLs dans le top 10) → opportunité positive Recommande l'action par conflit : 301, merge contenu, différenciation d'angle, renforcement maillage, ou aucune action.

### Vérification du contenu via Chrome

Pour chaque cannibalisation détectée via la GSC, connecte-toi à Chrome et ouvre les 2 URLs de MON site en conflit. Scrape leur contenu pour vérifier : 1. Les deux pages couvrent-elles RÉELLEMENT la même intention ? 2. Les H1 et H2 se chevauchent-ils ? 3. Les deux pages pointent-elles vers la même page pilier ? 4. Ont-elles des liens internes croisés ? Diagnostic : la cannibalisation est-elle un problème de contenu (pages trop similaires) ou un problème de maillage (Google ne comprend pas la hiérarchie) ?

### Output attendu

- Cannibalisations détectées via GSC + confirmées par lecture du contenu
- Diagnostic root cause : contenu vs maillage
- Action recommandée par conflit

## 06 ·Phase 3 : Architecture clusters AEO

Skill : seo-cluster-[[aeo]]. Source : Export GSC (toutes requêtes) + recherche web Claude + résultats Phases 0-2. Durée : 30-45 min.

### Étape 3A, Extraire l'univers sémantique depuis la GSC

Depuis l'export GSC complet : 1. Liste TOUTES les requêtes pour lesquelles mon site reçoit des impressions → C'est mon univers sémantique actuel vu par Google 2. Regroupe ces requêtes par thématique / cluster → Quels grands sujets Google associe-t-il à mon site ? 3. Pour chaque cluster identifié :

- Nombre total d'impressions
- Nombre de requêtes distinctes
- Position moyenne
- Y a-t-il une page pilier identifiable ? 4. Identifie les trous :
- Requêtes business (Phase 0) sans cluster GSC correspondant
- Clusters GSC sans page dédiée (le site ranke "par accident")

### Étape 3B, Compléter avec la recherche web

Via recherche web Claude, pour chaque cluster identifié : 1. Quels sont les sujets connexes que mon site ne couvre PAS ? (rechercher "[thématique du cluster] + guide / checklist / outil / comparatif") 2. Quels formats dominent pour ces requêtes ? (guide long, FAQ, outil interactif, tableau comparatif) 3. Les AI Overviews sont-ils actifs sur ces sujets ? Identifie les gaps de contenu :

- Sujets que mon audience cherche mais que je ne couvre pas
- Formats que Google favorise mais que je n'utilise pas

### Étape 3C, Construire les clusters

Mon site couvre [thématique]. Voici :

- Mon univers sémantique GSC : [synthèse 3A, clusters détectés]
- Mes pages existantes : [liste Phase 1]
- Les gaps identifiés : [liste 3A + 3B] Construis les clusters sémantiques optimisés AEO : Pour chaque cluster :
- 1 page pilier (Know, 3000+ mots)
- Pages satellites catégorisées : Know-Simple (20-30%) : réponses factuelles <50 mots, position 0 Know (40-50%) : explications profondes, 3000+ mots Do (20-30%) : micro-tâches, outils, workflows Minimum 15 pages satellites par cluster principal. Respecte le principe MECE. Pour chaque page satellite, indique :
- Si elle EXISTE déjà dans ma GSC (à optimiser) ou si elle est À CRÉER
- Le format gagnant pour cette requête
- Le schema.org recommandé
- La priorité (haute/moyenne/basse) Maillage : pilier ← satellites, Know → Do, Know-Simple → Know.

### Étape 3D, Score de priorité composite

Pour chaque page du cluster (existante ou à créer), calcule un score : Score = (Impressions_GSC × Delta_CTR × 0.4) + (Gap_couverture × 0.3) + (Rôle_dans_cluster × 0.3) Où :

- Impressions_GSC = impressions réelles GSC
- Delta_CTR = écart entre CTR actuel et CTR atteignable
- Gap_couverture = 1 si aucune page ne couvre ce sujet, 0.5 si partiellement
- Rôle_dans_cluster = pilier (×3), Do (×2.5), Know (×2), Know-Simple (×1) Ne passer en Phase 4 que les pages avec un score > [seuil à définir]. Les autres vont en "optimisation maillage seulement" (Phase 5).

### Output attendu

- Clusters construits à partir des données GSC réelles
- Gap analysis : sujets non couverts identifiés via GSC + recherche web
- Scoring de priorité pour filtrer les pages Phase 4
- Schéma de maillage cible

## 07 ·Phase 4 : Analyse vectorielle des pages stratégiques

Skill : seo-entites-vectorielles. Source : Chrome (contenu de mes pages) + GSC (requêtes associées). Durée : 20-30 min par groupe de 3-5 pages.

### Étape 4A, Extraire le contenu complet de MES pages

Connecte-toi à Chrome. Pour chaque page prioritaire (score > seuil en Phase 3) : 1. Ouvre MA page et extrait le contenu COMPLET :

- Texte brut de la page (tout le body visible)
- Structure Hn avec le contenu de chaque section
- Images : balises alt, légendes
- Données structurées présentes (JSON-LD)
- Liens internes (ancre + URL cible)
- Liens externes (ancre + URL cible) 2. Depuis la GSC, récupère pour cette page :
- TOUTES les requêtes pour lesquelles elle reçoit des impressions
- Les requêtes où elle est en position 1-3 (= bien couvertes)
- Les requêtes où elle est en position 4-20 (= partiellement couvertes)
- Les requêtes où elle apparaît en position 20+ (= mal couvertes)

Les requêtes GSC en position 4-20 sont le signal le plus précieux : Google considère ma page pertinente mais insuffisante. Les entités manquantes sont celles qui combleraient ce gap.

### Étape 4B, Analyse vectorielle

À partir du contenu de ma page + les requêtes GSC associées : Contenu actuel de ma page : [coller le contenu extrait en 4A] Requêtes GSC associées à cette page :

- Bien couvertes (position 1-3) : [liste]
- Partiellement couvertes (position 4-20) : [liste]
- Mal couvertes (position 20+) : [liste] Génère le tableau 4 colonnes : 1. Entités techniques (10+ termes du champ lexical expert) → Indique lesquelles sont DÉJÀ dans ma page vs MANQUANTES → Utilise les requêtes GSC position 4-20 comme indicateur 2. Preuves quantitatives (chiffres, études, benchmarks) 3. Vecteurs multimodaux (formats attendus : tableau, schéma, vidéo) 4. Éléments de divergence (ce que personne ne dit) Score de complétude actuel : X/10 Gap sémantique : liste des entités à ajouter en priorité

### Étape 4C, Check anti-IA du contenu existant

Pour chaque page extraite, analyse le contenu et détecte : 1. Patterns IA typiques :

- Listes à puces excessives (>50% du contenu en bullet points)
- Transitions génériques ("il est important de noter", "dans un monde où")
- Superlatifs creux ("révolutionnaire", "game-changer", "crucial")
- Structure répétitive (intro → 3 points → conclusion sur chaque section) 2. Absence de signaux humains/experts :
- Aucun chiffre propriétaire ou donnée terrain
- Aucune source nommée (étude, auteur, date)
- Aucune prise de position ou opinion assumée
- Aucune anecdote ou retour d'expérience
- Ton neutre sans voix auteur identifiable 3. Ratio preuves atomiques / affirmations vagues :
- Ratio idéal : > 40% de preuves atomiques Score Anti-IA : /10 (10 = contenu clairement humain et expert) Pour les pages <6/10 : flag "réécriture prioritaire"

## 08 ·Phase 5 : Audit du maillage interne

Skill : maillage-interne-gsc. Source : Chrome (crawl de mon site) + GSC. Durée : 20-30 min.

### Étape 5A, Cartographier les liens existants de MON site

Connecte-toi à Chrome. Navigue sur CHAQUE page de MON site et extrait : Pour chaque page :

- URL de la page
- Tous les liens internes (ancre texte + URL cible)
- Position du lien dans la page (navigation, body, footer, sidebar) Génère une matrice de liens internes : | Page source | Lien vers | Ancre utilisée | Position dans la page | Identifie :
- Pages orphelines (aucun lien entrant depuis une autre page du site)
- Pages sur-linkées (>20 liens entrants)
- Pages sous-linkées (pages stratégiques GSC avec <3 liens entrants)
- Ancres non-optimisées (textes type "cliquez ici", "en savoir plus") Croise avec la GSC :
- Les pages à fort potentiel GSC (impressions élevées) sont-elles bien linkées ?
- Les pages sans impressions GSC reçoivent-elles trop de liens ?

### Étape 5B, Diagnostic maillage avec méthode cocon

À partir de la matrice de liens extraite en 5A et de l'architecture des clusters définie en Phase 3 : 1. Vérifie la structure cocon : pilier → fille → petite-fille

- Chaque page pilier a-t-elle minimum 10 liens internes entrants ?
- Le maillage respecte-t-il la hiérarchie sémantique ? 2. Vérifie les flux Know → Do :
- Chaque page Know a-t-elle au moins 1 lien vers une page Do associée ?
- Les pages Do reçoivent-elles des liens des pages Know pertinentes ? 3. Vérifie les escalades Know-Simple → Know :
- Les pages Know-Simple pointent-elles vers les guides Know complets ? 4. Croisement avec Phase 2 (cannibalisation) :
- Les pages cannibalisées ont-elles un maillage qui les différencie ?
- Pointent-elles vers la même page pilier ? Génère les recommandations concrètes : | Page source | Lien à ajouter vers | Ancre recommandée | Justification |

## 09 ·Phase 6 : Briefs de contenu pour les pages prioritaires

Skill : seo-brief-contenu + seo-objections (pour pages commerciales). Source : Résultats Phases 0-5 + recherche web Claude. Durée : 15-20 min par brief.

### Pour pages Know (informatives)

Crée un brief de contenu SEO pour la page ciblant "[mot-clé]". Utilise :

- Les entités vectorielles identifiées en Phase 4 : [coller output]
- Les requêtes GSC associées (positions 4-20) : [coller output]
- Le format gagnant identifié via recherche web
- Le score Anti-IA de ma page actuelle : [score] (si page existante) Le brief doit contenir :
- Structure H1-H4 optimisée [[passage-ranking]]
- Pour chaque H2 : contenu attendu, micro-intention couverte, élément de surprise obligatoire
- Passage ancré (150-200 mots) extractible en Featured Snippet dans les 300 premiers mots
- Bloc auteur (~50 mots) répondant à 100% de la requête primaire
- Signaux [[e-e-a-t]] requis
- Formats multimodaux recommandés par section
- Si réécriture : indique les sections à garder / modifier / supprimer

### Pour pages Do (commerciales)

Avant de créer le brief pour "[page commerciale cible]" : 1. Via recherche web Claude, identifie les pratiques dominantes dans le secteur [secteur] pour ce type de page :

- Formats de pages commerciales qui performent
- Types de preuves sociales courantes
- CTA et mécaniques de conversion observées 2. Identifie les peurs et objections de mon audience B2B dans le secteur [secteur] (skill seo-objections) :
- Verbatim Haute Surprise
- Preuve Atomique [Sujet + Relation + Donnée]
- Format recommandé (case study, [[product-led-seo|calculateur]], garantie, FAQ) 3. Crée le brief intégrant les éléments de réassurance dans la structure Hn, en se différenciant par la [[data-proprietaire|data propriétaire]].

## 10 ·Phase 7 : Synthèse et plan d'action priorisé

Skill : Aucun, synthèse assistée par Claude. Durée : 20-30 min.

Voici les résultats de mon audit SEO complet : PHASE 0

- Positionnement : [coller synthèse] PHASE 1
- Quick Wins : [coller synthèse] PHASE 2
- Cannibalisations : [coller synthèse] PHASE 3
- Clusters AEO : [coller synthèse] PHASE 4
- Analyse vectorielle : [coller synthèse] PHASE 5
- Maillage interne : [coller synthèse] PHASE 6
- Briefs de contenu : [coller synthèse] Génère le plan d'action final en 3 horizons : SEMAINE 1-2 (Quick Wins) : Actions à impact immédiat, zéro création de contenu. Réécritures title/meta, liens internes à ajouter, résolutions cannibalisation, fiche Google Business Profile. MOIS 1 (Fondations) : Optimisation des pages existantes (réécriture avec briefs Phase 6), restructuration des clusters, maillage interne systématique. MOIS 2-3 (Croissance) : Création de nouvelles pages (briefs prêts), outils Product-Led, pages [[programmatique-pseo|pSEO]] si applicable. Pour chaque action : | Action | Page | Type | Impact estimé | Effort | Dépendances bloquantes |

## 11 ·Configuration minimale

Setup, Outils nécessaires

Audit complet, Export GSC + Chrome

Audit enrichi, MCP Windsor.ai (GSC via API) + Chrome + MCP Local Falcon

Audit sans GSC, Chrome seul (très limité, la GSC est quasi-indispensable)

## 12 ·Checklist pré-audit

- Export GSC téléchargé (CSV, 3-6 derniers mois, toutes requêtes + toutes pages)
- OU MCP Windsor.ai connecté (accès GSC + GA4 via API)
- Chrome ouvert avec extension Claude in Chrome connectée
- MCP Local Falcon connecté (optionnel, pour le SEO local)
- URL du site à auditer
- Liste de 5-10 requêtes business principales
- Connaissance du business model et des pages stratégiques
- Budget temps : prévoir 3-5h pour un audit complet

## FAQ

Parce qu'on n'en a plus besoin. Google Search Console donne la donnée la plus fiable : ce que les vrais utilisateurs tapent et cliquent sur ton propre site. Chrome avec l'extension Claude lit la SERP en temps réel. Le reste, c'est de l'agrégation de données externes que Claude peut analyser tout seul. Les outils tiers facturent l'agrégation. Toi, tu paies Claude Pro 20 euros par mois et tu raisonnes directement sur la data du client.

16 mois minimum. C'est la fenêtre maximale de GSC, et c'est ce qui te permet de comparer année sur année (YoY). Sans ce comparatif, tu ne peux pas détecter les pages en chute lente, les requêtes qui ont migré, ou l'impact des Core Updates. Si le client a moins de 16 mois d'historique, tu prends ce qu'il y a, mais tu signales que le diagnostic est partiel.

4 à 6 heures en suivant les 7 phases avec discipline. C'est plus rapide qu'un audit classique (12-20h) parce que Claude paralléllise l'analyse de la data. Le vrai goulot d'étranglement, c'est ta capacité à formuler des hypothèses business à partir des outputs. Pas la collecte.

L'audit outil produit une checklist : balises manquantes, vitesse, backlinks. C'est de la conformité technique. L'audit Claude raisonne sur la data du client (GSC + business model) et sort des hypothèses contextualisées : quelle URL ramène du lead, quelle requête est dévorée par les IA, quelle micro-intention n'est pas couverte. C'est de la stratégie, pas du diagnostic technique.

Non. Il accélère le diagnostic et structure la collecte. La décision stratégique (quoi attaquer, dans quel ordre, à quel budget) reste humaine. Le rôle de Claude ici, c'est d'éliminer 80 % du temps passé à compiler la data, pour que le consultant passe ses heures sur la valeur ajoutée : l'angle, le positionnement, la priorisation.

---

**Connecté avec :** [[cli-tools-optional]] · [[agentic-search]] · [[triade-serp]] · [[aeo]] · [[passage-ranking]] · [[e-e-a-t]]
