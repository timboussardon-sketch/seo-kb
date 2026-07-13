# Specs approfondies — Radar d'entités vectorielles + Carte de maillage (extensions Chrome)

Date : 2026-07-13
Skills mobilisés : seo-product-led-seo, seo-entites-vectorielles, maillage-systeme
Objectif : deux outils solides, pas jetables. Chaque décision technique ci-dessous vise la reproductibilité du score, la récurrence d'usage et la capitalisation de données propriétaires.

---

## 1. Radar d'entités vectorielles

### Ce que ça fait

L'utilisateur est sur une page (la sienne ou une page en cours de rédaction en préprod). Il saisit sa requête cible. L'extension mesure l'alignement sémantique page ↔ intention et sort : un Grounding Score approximé, le tableau des entités attendues en 4 catégories (méthode Organikk), et pour chaque entité manquante la zone où l'intégrer (H1/H2, corps, FAQ).

### Pipeline technique exact

Étape A — Extraction zonée (content script, client-side).
Le content script découpe le DOM en zones : H1, arborescence H2/H3, intro (premier bloc après le H1), corps par section Hn, FAQ (détection via JSON-LD FAQPage, `<details>`, ou patterns accordéon), données structurées JSON-LD. Chaque section Hn devient un chunk. Ce chunking aligné sur les Hn est délibéré : c'est l'unité du Passage Ranking, donc l'unité qui a du sens pour un score de citabilité.

Étape B — Référentiel d'entités attendues (edge function, caché).
Un appel LLM (Haiku 4.5, température 0, prompt versionné) génère le tableau canonique du skill : 10 entités par catégorie (Techniques, Preuves Quantitatives, Vecteurs Multimodaux, Divergence Haute Surprise). Règles du skill encodées dans le prompt : preuves au format [Chiffre+Unité+Contexte] sinon rejet ; divergence rejetée si copiable en 5 minutes.
Point clé de solidité : le résultat est mis en cache serveur avec pour clé `requête normalisée + version du prompt`. Même requête = même référentiel pour tout le monde et dans le temps. C'est ce qui rend le score comparable entre deux pages et entre deux dates. Et chaque nouvelle requête scannée enrichit un corpus propriétaire requête → entités qui prend de la valeur tout seul.

Étape C — Scoring (edge function).
Embeddings Gemini (infra alexia-copilot déjà en prod ; OpenAI exclu, billing bloqué). On embed : la requête (plus une expansion courte de micro-intentions), chaque chunk de page, chaque entité du référentiel.
Grounding Score = moyenne pondérée des similarités cosinus des top-k chunks vs la requête (approche multi-vecteur façon Muvera). Jamais la page entière moyennée en un seul vecteur : ça écrase le signal et donne un score mou identique partout.
Détection présence/absence d'entité : cosinus entité vs chunks au-dessus d'un seuil, avec fallback fuzzy-match. L'entité matchée hérite de la zone de son chunk → c'est ce qui permet le "manquant en FAQ" vs "manquant dans le corps".
Cas particulier Preuves Quantitatives : détection côté client des claims chiffrés déjà présents (regex chiffre+unité+contexte) pour distinguer "aucune preuve chiffrée" de "des chiffres mais pas ceux attendus".

Étape D — Restitution.
Score /100 affiché en bandes (fort / moyen / faible) avec l'explication du calcul, jamais un faux précis à la décimale. Gratuit : le score + les 3 entités manquantes les plus importantes. Contre email : le tableau complet 4 catégories × zones + recommandations d'implémentation (formulées "intègre dans une phrase porteuse", jamais une liste de mots à coller, règle anti-stuffing du skill).

### Ce qui le rend non jetable

- Mode suivi : re-scan de la même URL après modification → delta de score avant/après. L'outil s'insère dans le workflow de production d'article (on scanne chaque article après rédaction), pas un gadget qu'on essaie une fois.
- Historique par URL pour les comptes email (table scans).
- Le corpus requête → entités qui grossit à chaque scan = moat de données.
- Version agent-friendly dès la v2 : endpoint POST /radar {url, query} → JSON. L'extension devient l'interface grand public d'un endpoint que les élèves du bootcamp appellent depuis leurs workflows. Deux audiences, un seul moteur.

### Coûts et anti-abus

Embeddings Gemini quasi gratuits, 1 appel Haiku par requête nouvelle (caché ensuite). Quota anonyme 3 scans, email 10/mois, au-delà compte. Rate limit par IP sur l'edge function.

---

## 2. Carte de maillage en un clic

### Ce que ça fait

Depuis n'importe quelle page du site, l'extension crawle le site (sitemap ou BFS), construit le graphe de liens internes et rend l'audit du skill maillage-systeme : score, orphelines, dead-ends, hubs sous-maillés, qualité des ancres. Contre email : le plan de liens priorisé (source → cible, passage proposé, 3 ancres).

### Le point qui sépare l'outil sérieux du jouet

Ne compter QUE les liens contextuels in-body. Un compteur qui inclut nav, footer, sidebar et blocs "articles similaires" rend toutes les pages faussement bien maillées et l'audit est faux. Double détection :
- structurelle : exclusion des liens dans `<nav>`, `<footer>`, `<header>`, `[role=navigation]`, `<aside>`, et des blocs type "related" ;
- statistique : un lien avec la même ancre présent sur plus de ~70 % des pages crawlées = lien template, exclu.
C'est l'application directe de la règle du skill ("pas de Voir aussi, liens in-body uniquement") et c'est le Surprise Gap technique : personne ne fait cette distinction proprement.

### Pipeline technique exact

Étape A — Crawl (service worker, client-side, zéro backend).
Découverte : robots.txt → sitemap(s), gestion des sitemap index et des .gz ; fallback BFS depuis la home si pas de sitemap. Normalisation d'URL stricte (trailing slash, protocole, suppression des fragments et des paramètres de tracking). Cap 500 pages (aligné sur la cible 30-1000 du skill indexation-check), concurrence 4-6 requêtes, timeout par page, respect de robots.txt. Permissions : activeTab + host permission optionnelle demandée au clic pour le domaine courant uniquement (évite le drapeau "peut lire tous vos sites" qui tue l'installation et complique la review du store).

Étape B — Graphe (client-side).
Parsing DOMParser, extraction des liens contextuels (cf. supra) avec : ancre, 5 mots avant / 5 mots après (le link context du skill), position dans le document. Graphe en mémoire, snapshot daté en IndexedDB. Le graphe complet ne quitte JAMAIS le navigateur ; seul un résumé anonymisé (compteurs, score) remonte au serveur. C'est un argument de confiance affiché : "vos données de crawl restent dans votre navigateur".

Étape C — Audit (client-side, règles du skill encodées telles quelles).
Par page : inbound contextuels, outbound contextuels, click depth (BFS depuis la home), longueur de contenu. Intention Know-Simple / Know / Do par heuristiques du skill (patterns de titre "qu'est-ce que / comment / guide", patterns d'URL /outils/ /audit /contact). Anomalies : orpheline (0 inbound), dead-end (0 outbound), hub sous-maillé (< 5 inbound satellites). Ancres : génériques (liste FR/EN "cliquez ici, en savoir plus, lire la suite…"), exact match dupliqué vers la même cible (interdit par la règle "1 exact max"), distribution exact/partial/sémantique par cible (cible 60-70 % partial), densité liens/1000 mots (plafond 5). Vérification finale = les règles de conservation de l'étape 7 du skill, ligne par ligne.

Étape D — Piliers et hubs (en deux temps).
v1 heuristique client-side : clustering par chemins d'URL + TF-IDF sur les titres, proposition de 3-5 piliers que l'utilisateur peut corriger à la main (le skill dit : l'outil propose, l'humain décide).
v2 : embeddings via la même edge function que le Radar → vrai clustering sémantique, désignation du hub par complétude. Synergie backend directe entre les deux outils.

Étape E — Plan de liens (edge function, gated email).
Scoring de priorité du skill en mode sans-GSC : Score = (position_business × poids_intention) + gain_authority × 0.4, ordre de priorité Hub→Satellite puis Know→Do puis cross-pillar puis orphelines. La rédaction des passages proposés et des 3 ancres (exact/partial/sémantique, testées contre les 5 critères du skill) passe par le LLM. C'est le livrable qui justifie l'email.

Étape F — Overlay in-page.
Sur la page courante : liens contextuels comptés en vert, liens template ignorés en gris, badge inbound/outbound/depth de la page. C'est la démo visuelle en call de prestation.

### Ce qui le rend non jetable

- Snapshots datés + delta entre deux crawls : nouvelles orphelines, liens perdus, score qui bouge. Routine mensuelle → rétention.
- Mode gouvernance : la checklist du Bloc 4 du skill (chaque nouvel article : ≥3 inbound, ≥3 outbound, 1 lien Do, 1 cross-pillar, pas d'ancre exacte dupliquée) vérifiée automatiquement sur la dernière page publiée. L'outil devient le garde-fou de publication, utilisé à chaque article.

---

## 3. Socle commun (l'architecture qui rend l'ensemble solide)

UNE seule extension, deux modules (deux onglets), et deux landing pages distinctes sur organikk.co (une par requête Do : audit maillage interne / grounding score). Les requêtes se captent par les landings du site, pas par le store ; une seule extension = une seule review, une seule maintenance, cross-sell interne entre les deux modules, et les deux partagent le même moteur d'extraction DOM.

Monorepo : package core (extraction zonée, crawler, normalisation URL, UI, client Supabase) + les deux modules. Manifest V3, TypeScript vanilla, pas de framework lourd, pas de code distant (règle du store). Une seule edge function Supabase multi-endpoints (/radar, /plan-maillage, /lead) sur le pattern alexia-copilot. Tables : entity_cache, scans, crawl_summaries, leads.

Funnel commun : valeur gratuite (score + top anomalies) → email (rapport complet) → upsell pré-audit Organikk. Chaque rapport envoyé se termine par le CTA pré-audit.

Risques et parades : review Chrome Web Store 1-2 semaines (permissions minimales, privacy policy, justification des host permissions) ; sites JS-only dont le HTML fetché est vide (détection : si le body parsé < seuil, message honnête "site à rendu client, crawl partiel" plutôt qu'un faux audit) ; coût LLM (cache agressif + quotas).

### Roadmap

Semaines 1-2 : socle + module maillage v1 (100 % client-side, zéro backend) → déjà démontrable en call.
Semaines 3-4 : edge function + Radar v1 + gates email.
Semaine 5 : landings + test trafic payant AVANT d'investir le SEO des landings (règle du skill product-led).
Ensuite : piliers sémantiques v2, historique/deltas, endpoint API public agent-friendly.

### Ordre de lancement

Maillage d'abord : zéro backend, utilisable en prestation immédiatement, il valide l'audience et le funnel email. Le Radar suit avec le backend, c'est lui le flagship différenciant long terme (corpus requête → entités + API).
