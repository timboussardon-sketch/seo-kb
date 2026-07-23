# Prestation — KQUEO

- Slug : kqueo
- Domaine : kqueo.fr (Shopify, 5 ans)
- Type : e-commerce B2C, mobilier de bureau ergonomique
- Démarré : non signé au 2026-07-23 (propale en cours)
- Offre : accompagnement système SEO, 2 mois de mission à 1 400 € HT/mois (mois 1 analyse + data + construction, mois 2 entraînement + automatisation), puis 3 mois de suivi. En complément du consultant rédacteur en place.

## Où on en est
Étape courante : **2, pré-call et diagnostic d'entrée** (fait). Call de découverte tenu le 23/07.
Prochaine action : envoi de la proposition (deck + email). À la signature, enchaîner sur l'étape 1 (accès et data propriétaire) puis l'étape 3 (analyse GSC), qui conditionne tout le reste.

## Accès et data
- GSC : **non** (à récupérer, bloque l'étape 3) · GA4 : **non** (à récupérer)
- Data propriétaire disponible mais non reçue : 1 800+ avis notés 9,4/10, cinq installations nommées avec volumes, un ergonome (Romain Morvan, déjà filmé avec eux), 143 articles dont 24 sur la santé, partenariats sociaux (couturiers, gamers), showroom Paris.
- Personne ne connaît aujourd'hui les requêtes qui convertissent. C'est le premier trou à combler.

## Cadrage (interview)
Cadrage tiré du call de découverte du 23/07, pas d'une interview `interview-cadrage.md` séparée. À revalider à la signature.

**Ce que j'ai compris.**
E-commerce Shopify de mobilier de bureau ergonomique, 5 ans, panier moyen autour de 400 €. Le SEO pèse 30 à 40 % du chiffre d'affaires. Les positions se dégradent de mois en mois, la perte est concentrée sur les bureaux, catégorie où ils étaient forts sur « bureau assis-debout ». Le blog est la première source de trafic et ne convertit pas ; c'est la page d'accueil qui convertit, donc les requêtes portant leur nom. Aucun suivi de conversion par requête n'existe.

Contrainte dure : **le B2B est interdit par le fondateur**, alors que 40 % des commandes viennent déjà de sociétés. Motif : rupture de stock côté particuliers et entreprise non structurée pour ces volumes. La responsable e-commerce a porté le sujet et perdu l'arbitrage. On ne le remet pas sur la table.

Dispositif humain : Clément, consultant SEO externe, deux jours par mois, rédige seul et à la main, suit les positions et jamais la conversion, ne fait ni la technique ni la publication. Qualité jugée bonne, vitesse jugée insuffisante. Mathias, développeur interne, absorbe toutes les demandes techniques. La responsable e-commerce fait la publication à la main : Notion vers Drive vers Shopify.

Ce qu'ils achètent réellement : quelqu'un d'autonome sur la technique et la publication, l'automatisation de la chaîne de publication, et de la hauteur sur les process et les indicateurs. Pas un rédacteur de plus.

Budget déjà en place à réaffecter : 500 €/mois chez Semjuice (achat de liens), qu'ils arrêtent, engagement trimestriel à échéance.

## Séquence proposée (mode BRIEF)

Phases de `roadmap.md`, adaptées au cas KQUEO. Les étapes B2B de la v1 du pré-audit sont retirées.

| Ordre | Étape roadmap | Objectif pour KQUEO | Skill | Input requis | Statut |
|---|---|---|---|---|---|
| 1 | **1** Onboarding et accès | GSC + GA4, avis, matière de l'ergonome, ton de voix, accès Shopify et Notion | aucun | client | bloqué (pas d'accès) |
| 2 | **3** Analyse GSC | Trouver ce qui convertit vraiment, la perte réelle sur les bureaux, les requêtes en position 5-15 | analyse GSC, `maillage-interne-gsc`, `seo-cannibalisation` | 4 exports GSC | bloqué par 1 |
| 3 | **5** Audit technique | Balisage `aggregateRating` sur 78 produits, `h1` texte en accueil, `FAQPage`, `agents.md` | `seo-donnees-structurees`, `seo-core-web-vitals` | accès thème | prêt |
| 4 | **13 (anticipée)** Automatisation de la publication | Supprimer la recopie Notion vers Shopify à la main | aucun (dev) | accès API Shopify | prêt, fort effet perçu |
| 5 | **6** Mots-clés décisionnels | Motifs de santé, personas d'usage, comparaisons de gammes | `seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-decisionnels` | GSC | bloqué par 2 |
| 6 | **8** Modèles pSEO | M1 santé, M2 persona, M3 gammes, M5 dimension | `seo-modeles-pseo`, `seo-programmatique-pseo` | sortie de 5 | à venir |
| 7 | **9** Product-Led SEO | Brancher leur quiz sur des landing pages, ajouter calculateur de hauteur et simulateur d'encombrement | `seo-product-led-seo` | date de sortie du quiz | à venir |
| 8 | **10** Peurs et objections, entités | Défendre « bureau assis-debout » où ils reculent | `seo-peurs-objections`, `seo-entites-vectorielles` | GSC | à venir |
| 9 | **7** Architecture et maillage | Relier les 24 articles santé aux collections marchandes | `seo-cluster-aeo`, `maillage-systeme` | sortie de 6 | à venir |
| 10 | **11-12** Briefs et rédaction | Briefs pour Clément, qui garde la plume | `seo-brief-contenu`, `content-brain` | validation du partage des rôles | à venir |
| 11 | **13-14** Système et espace client | Agent SEO KQUEO sur leur data, dashboard | — | data propriétaire | à venir |
| 12 | **15** Suivi par preuves | GSC à J+30 et J+90 sur les pages publiées | `indexation-check` | temps | à venir |

## Spécificités client

- **Le B2B est hors périmètre par décision du fondateur**, malgré 40 % de commandes professionnelles. Ne pas le rouvrir. Les installations nommées servent de preuve, jamais de cible d'acquisition.
- **Clément reste à la rédaction.** Organikk prend la technique, les process, la publication, les indicateurs et le système. Le partage des rôles doit être posé noir sur blanc au démarrage, sinon friction assurée.
- **L'automatisation de la publication n'est pas du SEO** mais c'est le besoin le plus concret exprimé au call, et elle débloque toute la production. Elle est remontée très tôt dans la séquence pour cette raison.
- **Deux interlocuteurs, deux attentes.** La responsable e-commerce veut de la hauteur et de la vitesse. Mathias veut ne plus être le passage obligé de toute demande technique. Les deux doivent y trouver leur compte.
- Aucun achat de lien. Ils arrêtent Semjuice, et on ne rachète rien tant qu'une page n'est pas dans le top 10.

## Journal des étapes faites
| Date | Étape (roadmap) | Ce qui a été fait | Output | Skill |
|---|---|---|---|---|
| 2026-07-23 | 2 | Pré-audit sur pages publiques (angle B2B, invalidé le jour même) | [[pre-audit-kqueo]] v1 | `seo-pre-audit` |
| 2026-07-23 | 2 | Call de découverte, cadrage réel | [[2026-07-23-call-decouverte]] | — |
| 2026-07-23 | 2 | Pré-audit refondu sur le décisionnel B2C | [[pre-audit-kqueo]] v2 | `seo-pre-audit` |
