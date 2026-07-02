# Prestation — Leexi

- Slug : leexi
- Domaine : leexi.ai
- Type : B2B SaaS (notetaker IA, suite Leexi One en septembre 2026)
- Démarré : 2026-06-09
- Offre : système livrable (repo transférable `~/Code/leexi-seo` + pack doctrine en submodule)

## Où on en est
Étape courante : 7 (architecture en cocons — 3 cocons mère/fille/petite-fille arrêtés, livrable client prêt à envoyer)
Prochaine action : (1) **envoyer le Google Doc** à Leexi pour validation des 4 mots-clés business + récupérer les cas clients chiffrés (carburant citation IA) + réponses HDS/URLs ancien site ; (2) **confronter l'overlap SERP réel** (SE Ranking) sur les pages P1, surtout zones à risque visio et ISO ; (3) réparer la refonte (301/canonicals/maillage, préalable technique non négociable) ; (4) brief par page de la vague 1.
À trancher : plus rien côté rangement (consolidation faite le 02/07, architecture canonique dans `leexi-seo/production/cocons/`). Restent les arbitrages client : faits de conformité publiables, CTA essai vs démo, mode de publication Strapi.

## Accès et data
- GSC : oui (4 exports dans `leexi-seo/data/gsc/`, manque l'export requête × page) · GA4 : non
- Data propriétaire reçue : brief client canonique (3 personas, 9 features, objections verbatim), questionnaire espace client (auto-sync Supabase → `data/questionnaire/`), call découverte du 21 mai. Manquent : calls de démo (voix client), faits de conformité publiables (hébergeur réel, périmètre ISO 27001)

## Journal des étapes faites
| Date | Étape (roadmap) | Ce qui a été fait | Output | Skill |
|---|---|---|---|---|
| 2026-05-21 | 2 | call découverte + dossier prospect | `raw/organikk/clients/leexi/` | aucun (gabarit pré-call) |
| 2026-06-09 | 1 | système livrable posé : repo transférable, pack submodule, 8 skills sync, questionnaire Supabase auto-pull, vault Obsidian navigable | repo `~/Code/leexi-seo` | aucun |
| 2026-06-09 | 1 | brief client canonique reçu et structuré | `leexi-seo` [[leexi-brief]] | aucun |
| 2026-06-09 | 3 | analyses GSC (synthèse + approfondie) : −43 % hors-marque en 6 mois, cause racine = refonte sans 301, souveraineté = 0 clic, 400k impressions sous-exploitées | [[analyse-gsc-leexi]] + [[analyse-gsc-approfondie-leexi]] | analyse GSC |
| 2026-06-09 | 6 (amorce) | audit thématique + étude marché notetakers FR + étude RGPD/souveraineté | [[audit-thematique-leexi]] · [[etude-marche-notetakers-fr]] · [[etude-rgpd-souverainete-leexi]] | deep-research |
| 2026-06-09 | 14 | espace client HTML (DA Leexi, devenu le format standard) | `organikk-next/public/espace-leexi/` | aucun |
| 2026-06-12 | 3 | rapport de restitution GSC sur Google Doc, intro « En résumé : les 5 points à retenir », jargon traduit | [Google Doc](https://docs.google.com/document/d/1Xw0cvggBsokPz_nKAJUCY-EuewdkYJkTcBlSQne6cUg/) | aucun |
| 2026-06-12 | 3 + 14 | onglet Audit de l'espace client alimenté avec le diagnostic GSC (tiles KPI, 5 points, tables, plan 4 blocs), badge passé en Live | `organikk-next/public/espace-leexi/` | aucun |

| 2026-06-12 | 6 | recherche de mots-clés 4 clusters (cadrage Tim) : problématiques avant/pendant/après réunion × 3 personas, bas de funnel, 1 page par fonctionnalité + outils gratuits, RGPD/souveraineté ; 425 suggestions Google Suggest FR + croisement GSC, zéro volume inventé | `leexi-seo/production/recherche-mots-cles-2026-06-12.md` + onglet Mots-clés de l'espace client | seo-recherche-mots-cles |

| 2026-06-12 | 14 | assistant de l'espace client connecté au vault Obsidian du client : RAG scopé par projet (kb_chunks.project), 109 chunks leexi ingérés, prompt vouvoiement, widget branché | `leexi-seo/scripts/export-kb-chat.py` + edge functions kb-chat/kb-ingest | aucun |

| 2026-06-12 | 14 | email de livraison (audit + stratégie mots-clés en ligne, annonce des 50 mots-clés la semaine du 15 juin) : brouillon Gmail prêt, modèle capitalisé en §2 d'emails.md | brouillon Gmail r6085825889555304583 | aucun |

| 2026-06-16 | 6 | approfondissement du cluster RGPD (1 des 4 clusters du 12/06) : 56 mots-clés groundés data réelle WebSearch (PAA + variantes tapées), 24 Do / 30 Know / 2 Know-Simple, 8 sous-clusters ; cadrage tranché par Tim : traduction juridique = feature produit → traitée en Do | `raw/organikk/clients/leexi/keywords/recherche-2026-06-16-rgpd.md` | seo-recherche-mots-cles |

| 2026-06-17 | 6 | stratégie de mots-clés des 3 premiers mois arrêtée : 3 clusters ordonnés par fonction. Cluster 2 intégrations (~55 KW : Teams/Meet/Zoom/Webex + CRM + productivité + technique, ancré sur l'acquis GSC à défendre) ; cluster 3 outils gratuits Product-Led (~50 KW, 1 outil = 1 page, 4 MVP) ; besoins Reddit capturés (verbatims collés main, Reddit bloque le crawler). Doc de référence unique consolidé | `leexi-seo/production/Strategie-clusters-leexi.md` (+ recherche-mots-cles-cluster2/cluster3, cluster3-outils-gratuits, besoins-reddit-cluster2) | seo-recherche-mots-cles + seo-product-led-seo |
| 2026-06-24 | 2 | call #2 (Baptiste CTO + Mathieu + Sophie marketing) : validation des axes mots-clés, calage prod, MCP Strapi tranché | `raw/organikk/clients/leexi/leexi-call-2026-06-24.md` | aucun |
| 2026-06-26 | 6 | inventaire complet 259 mots-clés : fan-out WebSearch parallèle par branche (PAA/SERP réelles) + confrontation GSC (signaux `teams compte rendu réunion automatique` pos 5,3 sans page, `agent ia entreprise` 310 impr, `best ai note taker for lawyers` EN) ; réparti en 5 seaux (Money / Longue traîne / Questions / Sous-exploitées / SERP faibles) ; comparatifs vs outils US uniquement | `keywords/liste-mots-cles-complete.md` + `keywords/clusters-2026-06-26.md` | seo-recherche-mots-cles + seo-clustering-mots-cles |
| 2026-06-26 | 7 | architecture restructurée en 3 cocons mère/fille/petite-fille : (1) notetaker/réunion produit, (2) RGPD différenciateur, (3) couche GEO transversale (problèmes métier « comment… », citation IA + maillage, PAS un cocon produit) ; arbitrage cannibalisation explicite, décision couche GEO ≠ doublon des usages | `keywords/cocon-1/2/3-*.md` + `keywords/arborescence-cocons.md` | seo-cluster-aeo |
| 2026-06-26 | 7 | livrable client : 4 mots-clés business + 3 cocons à valider, Google Doc mère/fille/petite-fille (vrais mots-clés), voix Tim factuelle, titres bleus | [Google Doc archi](https://docs.google.com/document/d/1dhQOMflYoDcTsSWELYZWZYBUGTiYWpJfI89TTtdJTPM/) + [Google Doc mots-clés business](https://docs.google.com/document/d/1hsVZmZvzh6RcGzaDSRDVUHs0JNCE4cB3KCk18GcSjxw/) + `livrable-mots-cles-business.md` | aucun |
| 2026-07-02 | 7 | consolidation de l'architecture du 26/06 dans le vault Obsidian client (`production/cocons/`, 6 fichiers, wikilinks raccordés), supersession du découpage 17/06 marquée sur `Strategie-clusters-leexi.md`, 000-home + Journal du repo client mis à jour (la session du 26/06 n'y était pas loggée), notes de canonicité posées côté seo-kb | `leexi-seo/production/cocons/` (commit 0205437) | aucun |
| 2026-07-02 | 8 (optimisation existant) | quick wins mots-clés business : 10 pages en ligne positionnées (pos 2-16) mais sous-optimisées, croisement GSC 09/06 × fetch on-page live ; les 2 plus grosses pages (51 810 impr cumulées) ont un CTR ≤ 0,23 % avec title/H1 hors requêtes ; MC4 RGPD = 0 page (création cocon 2, pas un quick win) ; pari J+30 posé au ledger de la boucle | `leexi-seo/production/quick-wins/quick-wins-mots-cles-business-2026-07-02.md` | seo-quick-win |

## Spécificités client
- Relancer `python3 scripts/export-kb-chat.py` (repo leexi-seo) après toute session qui modifie le vault, pour que l'assistant de l'espace reste à jour.
- 1er cas du « système client livrable » 3 repos : seo-kb (privé) / leexi-seo (transférable) / organikk-seo-pack (doctrine vivante en submodule). Tout livrable vit dans le repo client, jamais ailleurs.
- Croissance GSC globale (+28 %) en trompe-l'œil : marque +45 % masque un hors-marque à −43 %. Toujours séparer branded/non-branded avant de conclure.
- Souveraineté = argument commercial n°1 mais 0 clic SEO : terrain vierge, dépend de faits de conformité validés juriste avant publication.
- Publication via Strapi (HTML ou push API, à trancher) ; CTA principal à trancher (essai gratuit vs démo).
