# Product-Led SEO — Extensions Chrome Organikk

Date : 2026-07-13
Skill : seo-product-led-seo
Contexte : brainstorm des extensions Chrome SEO créables, qui fonctionnent techniquement et qui sont pertinentes pour Organikk. Règle appliquée : chaque concept mobilise un skill propriétaire (feedback_modele_skill_obligatoire), sinon c'est de la commodité.

## Étape 1 — Analyse de la thématique

Produit/service : accompagnement SEO/GEO Organikk (bootcamp + prestation).
Données propriétaires : grille de scoring opendecoder (S_Pertinence + 3 bonus), checklist anti-IA writing, méthode Organikk (cluster AEO, entités vectorielles, maillage système), données d'accompagnement clients (anonymisées).
Ressources techniques : extension Chrome Manifest V3 = content scripts (lecture DOM de la page courante), fetch de pages du même site (host permissions), appel possible d'une edge function Supabase (pattern alexia-copilot déjà en prod). Pas de scraping de SERP tierces, pas de data concurrents (règle absolue).
Objectif conversion : email gate → pré-audit → accompagnement.

## Étape 2 — Micro-intentions "Do" de l'audience

Auditer : « est-ce que ma page peut être citée par ChatGPT / AI Overviews ? », « quelles pages optimiser en premier ? », « mon maillage interne tient-il ? »
Calculer : « quel est mon alignement sémantique avec ma requête cible ? »
Diagnostiquer : « mon contenu ressemble-t-il à du contenu IA générique ? »

## Étape 3 — Les 5 concepts

| Solution Produit | Micro-intention "Do" | Surprise Gap | Confidence Score (Preuves) | Action de Conversion |
|---|---|---|---|---|
| **Scanner d'extractibilité GEO** — un clic sur n'importe quelle page, l'extension note sa capacité à être citée par les moteurs génératifs | Auditer : « ma page est-elle citable par les IA ? » | La grille opendecoder (S_Pertinence + 3 bonus) appliquée en temps réel, calibrée sur nos audits clients | Score /100 + les 3 passages les plus citables + les 3 bloquants localisés dans le DOM | Rapport complet PDF contre email → pré-audit Organikk |
| **Overlay quick-win GSC** — s'injecte dans l'interface Search Console et colore les lignes à fort potentiel | Auditer/prioriser : « quelles pages optimiser en premier ? » | Courbe CTR de référence issue de nos données d'accompagnement, pas des benchmarks publics | Nombre de quick wins détectés + gain de clics estimé en fourchette (jamais une position annoncée comme un fait) | Export du plan d'action priorisé contre email |
| **Radar d'entités vectorielles** — tu saisis ta requête cible, l'extension extrait les entités de la page et mesure l'alignement | Calculer : « ma page couvre-t-elle les entités attendues ? » | Les 4 catégories d'entités de la méthode Organikk (techniques, preuves chiffrées, multimodal, Haute Surprise) | Grounding Score approximé + liste des entités manquantes par catégorie et par zone (H1, corps, FAQ) | Tableau complet des entités manquantes contre email |
| **Carte de maillage en un clic** — depuis une page du site, crawl léger du sitemap et audit du graphe interne | Auditer : « mon maillage tient-il ? » | Classification hub/satellite + règles de diversification d'ancres du skill maillage-systeme | Score de maillage + nombre de pages orphelines et dead-end + liste des ancres génériques | Plan de maillage complet contre email |
| **Détecteur de contenu commodité** — analyse le texte de la page et flagge les patterns d'écriture IA générique | Diagnostiquer : « mon contenu survivrait-il au test de substitution LLM ? » | La checklist anti-IA writing terrain de Tim (patterns précis, pas un détecteur statistique) | Score commodité /100 + passages flaggés avec le pattern nommé | Diagnostic de réécriture contre email → accompagnement |

Skills mobilisés, dans l'ordre : opendecoder-seo-scoring-system, seo-quick-win, seo-entites-vectorielles, maillage-systeme, ton-de-voix-tim (checklist anti-IA writing).

## Étape 4 — Faisabilité

Zéro backend, livrable en quelques jours : l'overlay GSC (content script qui lit le tableau déjà affiché, aucun appel API) et la carte de maillage (fetch du sitemap + pages du même site, tout client-side ; prévoir les host permissions).

Backend léger (edge function Supabase, pattern alexia-copilot) : le scanner d'extractibilité et le détecteur de commodité peuvent démarrer en heuristiques pur client (structure Hn, claims atomiques, patterns textuels) puis passer par un LLM pour affiner. MVP possible sans backend.

Backend obligatoire : le radar d'entités (embeddings pour la similarité cosinus). Le plus différenciant mais le plus long.

Risque commun : la review du Chrome Web Store (compter 1 à 2 semaines) et la maintenance de l'overlay GSC si Google change son DOM.

## Étape 5 — Recommandation et specs du premier MVP

Flagship recommandé : le Scanner d'extractibilité GEO. Plein cœur du positionnement Organikk, chaque scan est un lead, et le Surprise Gap (grille opendecoder) est impossible à copier sans la méthode.

Specs MVP : input = la page courante (DOM). Logique = extraction Hn + détection answer-first + claims atomiques + schema présent + longueur des chunks, scoring heuristique local, puis v2 avec appel edge function pour le jugement LLM. Output = score /100, 3 forces, 3 bloquants, surlignés dans la page. Gate = email pour le rapport PDF complet. Stack = Manifest V3, vanilla TS, edge function Supabase en v2.

Règles rappelées : tester le MVP avec un peu de trafic payant avant d'investir en SEO, et prévoir la version agent-friendly (endpoint API qui prend une URL et rend le score en JSON) pour l'Agentic SEO.

Quick win en parallèle : l'overlay GSC, zéro backend, utilisable dès demain en prestation comme démo en call.
