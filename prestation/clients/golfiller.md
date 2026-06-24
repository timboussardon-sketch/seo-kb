# Prestation — Golfiller

- Slug : golfiller
- Domaine : golfiller.fr
- Type : e-commerce (balles de golf occasion / reconditionnées)
- Démarré : 2026 (cas SEO phare)
- Offre : accompagnement SEO/GEO

## Où on en est
Étape courante : 9/quick-win (refonte de la page live « classement meilleures balles » par injection de data, sans casser la structure qui rank)
Prochaine action : Tim relit le HASA MAJ (`outputs/2026-06-22-classement-meilleures-balles-MAJ.html`) et le colle dans le rich-text Shopify. Bloqueur data toujours ouvert : distances RÉELLES par profil client (Haute Surprise) jamais reçues — la MAJ n'utilise que de la data publique sourcée. Ensuite : décision mise en ligne article distance, dupliquer le gabarit usage, pages de marque, titres faible CTR.

## Accès et data
- GSC : oui (export 6 mois + 90j) · GA4 : <à confirmer>
- Data propriétaire reçue : stratégie source (`raw/notes/golfiller-strat-source.md`)

## Journal des étapes faites
| Date       | Étape (roadmap) | Ce qui a été fait                                                                                                                                                       | Output                                                                           | Skill                                   |
| ---------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------- |
| 2026-06-10 | 3               | Analyse GSC 90 jours                                                                                                                                                    | [[queries/2026-06-10-golfiller-gsc-90j]]                                         | analyse GSC                             |
| 2026-06-10 | 3               | Analyse GSC 6 mois comparée (branded ↑, érosion non-branded, striking distance)                                                                                         | [[queries/2026-06-10-golfiller-gsc-6mois]]                                       | analyse GSC                             |
| 2026-06-10 | 8               | 7 modèles de pages pSEO scorés depuis la GSC                                                                                                                            | [[clusters/modeles-pseo-2026-06-10-golfiller]]                                   | seo-modeles-pseo                        |
| 2026-06-10 | 10              | Entités vectorielles page Money « balle(s) de golf » (défense pluriel + gisement 26 574 imp)                                                                            | [[queries/entites-2026-06-10-golfiller-balle-de-golf]]                           | seo-entites-vectorielles                |
| 2026-06-10 | 8               | Scrape blog + GSC non couvert : nouveau modèle directory « balle par usage/besoin »                                                                                     | [[clusters/modeles-pseo-2026-06-10-golfiller]]                                   | seo-modeles-pseo                        |
| 2026-06-10 | 11              | Brief Hn page template usage « balle de golf pour la distance »                                                                                                         | [[briefs/2026-06-10-balle-golf-distance]]                                        | seo-brief-contenu                       |
| 2026-06-10 | 12              | Article rédigé (draft, data catalogue sourcée, distances [À SOURCER])                                                                                                   | content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.md                | content-brain                           |
| 2026-06-10 | 12              | Set usage complet en HTML/CSS Shopify-ready (distance, contrôle, vent, durabilité, budget)                                                                              | content-brain/golfiller/outputs/2026-06-10-balle-golf-*.html                     | content-brain                           |
| 2026-06-22 | 9               | MAJ page live « classement meilleures balles » : compression chiffrée par modèle, table distance/vitesse, prix occasion, maillage interne (structure + liens conservés) | content-brain/golfiller/outputs/2026-06-22-classement-meilleures-balles-MAJ.html | content-brain                           |
| 2026-06-22 | 12              | Refonte « classement meilleures balles » au template gf-article + couleurs marque (teal #108474, th turquoise #5BD8C0)                                                  | outputs/2026-06-22-classement-meilleures-balles-STYLEE.html                      | content-brain                           |
| 2026-06-22 | 12              | Article « balles des pros du PGA Tour » (Top 8 + Tiger Woods, tableau récap AEO, conversion occasion)                                                                   | outputs/2026-06-22-balles-des-pros-STYLEE.html                                   | content-brain                           |
| 2026-06-22 | 11/12           | Recherche mots-clés pages-data (24 kw, top 6) + 2 pages-data : flex de shaft (sourcé True Spec/Golf.com/Golf Sidekick) et convertisseur yards/m + mph/kmh               | outputs/2026-06-22-flex-shaft-*.html, outputs/2026-06-22-convertisseur-*.html    | seo-recherche-mots-cles + content-brain |
| 2026-06-22 | —               | Formalisation template gf-article OFFICIEL (articles) + parades anti-thème Shopify                                                                                      | raw/golfiller/pages/_TEMPLATE-gf-article-CSS.html + mémoire                      | —                                       |

## Spécificités client
Long tail très forte sur URL unique (tarifs des parcours : 1 346 requêtes, 388 parcours nommés) : signal pSEO « 1 variable = 1 page » à industrialiser (parcours, modèle de balle, profil de joueur, marque). Couche « occasion / reconditionné » = cœur de l'offre Product-Led.
