# Prestation — Leexi

- Slug : leexi
- Domaine : leexi.ai
- Type : B2B SaaS (notetaker IA, suite Leexi One en septembre 2026)
- Démarré : 2026-06-09
- Offre : système livrable (repo transférable `~/Code/leexi-seo` + pack doctrine en submodule)

## Où on en est
Étape courante : 6 (mots-clés business, recherche faite)
Prochaine action : clustering (1 cluster = 1 page) + priorisation, et toujours l'arbitrage Bloc 1 (réparation refonte) en parallèle

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
| 2026-06-12 | 3 | rapport de restitution GSC sur Google Doc, intro « En résumé : les 5 points à retenir », jargon traduit | [Google Doc](https://docs.google.com/document/d/1iVnT2wtNeS617iYQIXTCCuRi8kkdDYANNwEJChRR99E/) | aucun |
| 2026-06-12 | 3 + 14 | onglet Audit de l'espace client alimenté avec le diagnostic GSC (tiles KPI, 5 points, tables, plan 4 blocs), badge passé en Live | `organikk-next/public/espace-leexi/` | aucun |

| 2026-06-12 | 6 | recherche de mots-clés 4 territoires (cadrage Tim) : problématiques avant/pendant/après réunion × 3 personas, bas de funnel, 1 page par fonctionnalité + outils gratuits, RGPD/souveraineté ; 425 suggestions Google Suggest FR + croisement GSC, zéro volume inventé | `leexi-seo/production/recherche-mots-cles-2026-06-12.md` + onglet Mots-clés de l'espace client | seo-recherche-mots-cles |

## Spécificités client
- 1er cas du « système client livrable » 3 repos : seo-kb (privé) / leexi-seo (transférable) / organikk-seo-pack (doctrine vivante en submodule). Tout livrable vit dans le repo client, jamais ailleurs.
- Croissance GSC globale (+28 %) en trompe-l'œil : marque +45 % masque un hors-marque à −43 %. Toujours séparer branded/non-branded avant de conclure.
- Souveraineté = argument commercial n°1 mais 0 clic SEO : terrain vierge, dépend de faits de conformité validés juriste avant publication.
- Publication via Strapi (HTML ou push API, à trancher) ; CTA principal à trancher (essai gratuit vs démo).
