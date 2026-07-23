---
type: audit
title: Pré-audit KQUEO (kqueo.fr), note interne avant call
aliases: [pre-audit-kqueo, kqueo]
tags: [pre-audit, prospect, ecommerce, shopify, pseo, mobilier-ergonomique, organikk]
created: 2026-07-23
updated: 2026-07-23
sources: 1
confidence: medium
status: draft
---

# Pré-audit KQUEO (kqueo.fr)

Note interne de préparation. Ne se montre pas au prospect. Les livrables montrables sont `audit-kqueo-organikk.html` et `deck-kqueo-organikk.html`.

## En résumé

Fabricant français de mobilier ergonomique de bureau, boutique Shopify, vente directe aux particuliers et aux entreprises. 78 produits, 52 collections finement segmentées, 143 articles de blog, 23 pages. Les 143 articles sont informationnels (comment régler sa chaise, quelle couleur au bureau, soulager une sciatique). ChatGPT et les AI Overviews restituent ce type de réponse sans renvoyer de clic.

La data qui fait décider un acheteur entreprise est en ligne mais sans travail SEO : cinq installations nommées avec leurs volumes (Opéra Garnier 50 bureaux, IPTEK 33, EAS International 35, LOUMI 19, American Library in Paris 10), un ergonome, un showroom parisien, plus de 1 800 avis notés 9,4/10. Le tout tient sur une page de 1 100 mots dont le seul lien depuis l'accueil est en pied de page. Et la note de 9,4/10 n'est balisée sur aucune des six pages produit relevées.

On démarre sur le décisionnel d'équipement (par secteur, par nombre de postes, par financement) et sur la remise en état de la preuve. On ne touche pas aux 52 collections, elles sont déjà bien faites.

Sources : sitemaps kqueo.fr relevés le 23/07/2026 (`sitemap_products_1` 78, `sitemap_collections_1` 52, `sitemap_pages_1` 23, `sitemap_blogs_1` 147 entrées dont 4 pages de rubrique), pages `/`, `/pages/espace-professionnels`, `/pages/guide-amenagement-bureau-professionnel`, `/pages/formation-ergonomie-entreprise`, `/collections/mobilier-ergonomique-pour-les-professionnels`, six pages produit, `/robots.txt`, `/agents.md`. GSC non disponible, à récupérer au call.

## 1. Diagnostic prospect

**Identité.** Fabricant français de mobilier ergonomique de bureau. Gammes propriétaires : bureaux assis-debout (Dynamic, Lift, Space, Corner, Smooth, Connect, Bambou), chaises ergonomiques (Terrana, Moove, Zen, Flow, Sphera), accessoires de mouvement (tapis de marche Walker, pédalier Eliptic). Showroom à Paris, 6 rue Monsigny. Ligne dédiée aux professionnels : 01 76 36 21 37.

**Modèle et conversion.** Vente directe sur Shopify. Deux points de conversion distincts : l'achat en ligne pour le particulier (79 € à plus de 1 200 €), la demande de devis pour l'entreprise (tarifs dégressifs, montage, reprise de l'ancien mobilier, garantie étendue à 5 ans). Promotion active au moment du relevé (soldes jusqu'à -60 %).

**Data propriétaire mobilisable.** Cinq installations nommées avec volumes. Un ergonome identifié (Romain Morvan) qui anime les formations en entreprise. Plus de 1 800 avis vérifiés notés 9,4/10 (Société des Avis Garantis). Garantie 5 à 7 ans, 30 jours d'essai, 1 bureau acheté = 1 arbre planté. Peu de sites de cette catégorie ont autant de preuve nommée.

**Pain probable (analyse interne, ne pas balancer frontalement).** Ils ont investi dans un blog volumineux pensé pour un SEO d'avant les réponses génératives, et ils n'ont pas transposé cet effort côté décision d'achat entreprise. Le B2B semble arriver par bouche-à-oreille, salons et réseau (Preventica cité au blog), pas par le site. Résultat : la partie du chiffre d'affaires au panier le plus élevé dépend le moins du canal qu'ils alimentent le plus.

**À récupérer au call.** Impressions par mois, position moyenne, requêtes qui ramènent déjà des ventes et des devis, part du chiffre d'affaires entreprise, nombre de demandes de devis mensuelles, canal d'origine des projets d'aménagement.

## 2. L'angle : le décisionnel d'équipement d'abord

**Ce sur quoi ils sont défendables.** La décision d'équipement professionnel. ChatGPT n'a accès ni aux 50 bureaux installés à l'Opéra Garnier, ni à l'ergonome qui intervient sur site, ni au showroom où l'on essaie, ni aux 1 800 avis, ni à la garantie de sept ans. Sur « équiper un open space », « mobilier ergonomique pour coworking », « financer l'achat de bureaux assis-debout », celui qui cherche veut un fournisseur qu'il peut appeler dans la journée.

**Second levier.** Le décisionnel santé côté commerçant. Le blog traite déjà mal de dos, hernie discale, sciatique, canal carpien, mais rien ne relie ces sujets à une sélection de produits. 24 articles santé existent, aucun ne mène à une sélection de produits.

**Ce qu'on ne fait pas en premier.** On ne retouche pas les 52 collections, elles sont segmentées et étoffées (2 400 à 2 650 mots relevés). On laisse « bureau assis-debout » générique : trop large, très disputé par les revendeurs et les places de marché, et le site y travaille déjà. On ne produit pas un article de blog de plus.

**Timing, le hook.** Ils ont déjà fait le travail le plus coûteux (catalogue segmenté, contenu abondant, preuve réelle). Il reste à réorienter cette production vers la décision d'achat. C'est le moment le moins cher pour le faire.

## 3. État des lieux SEO (relevé le 23/07/2026)

**Volumétrie.** 78 produits, 52 collections, 23 pages, 143 articles répartis en 4 rubriques (mobilier 66, environnement de travail 47, santé 24, actualités 10). Domaine canonique kqueo.fr, kqueo.com en redirection 301 propre.

**Ce qui est bien fait.** Les collections sont découpées par dimension (110 à 240 cm), par matière (verre, bambou, maille, cuir reconstitué, bouclette) et par usage (petit espace, open space, gaming, design). Elles portent du contenu. `BreadcrumbList` présent. Sitemaps propres, `agents.md` généré par Shopify (protocole UCP actif).

**Les trous.**
- Aucun `aggregateRating` sur les six pages produit testées, alors que le site affiche 9,4/10 sur plus de 1 800 avis. Le balisage `Product` est là, la preuve n'y est pas.
- La page `/pages/espace-professionnels` (1 100 mots) porte les cinq cas clients et n'est liée depuis l'accueil qu'en pied de page (position relevée à 91 % du document).
- Aucune page ne compare les gammes entre elles. Trois articles de blog traitent la technique (un moteur ou deux, pneumatique ou électrique, manuel ou motorisé), aucun ne tranche entre Dynamic et Lift.
- Le `h1` de l'accueil porte le logo en image, sans texte.
- Accueil : 1,99 Mo de HTML, premier octet mesuré à 1,03 s. Données structurées limitées à `Organization` et `WebSite`, aucun bloc `FAQPage` sur les guides et collections testés.
- `agents.md` est le fichier générique Shopify : il explique comment acheter, il ne dit rien des gammes, de l'ergonome ni des installations.

**Le signal.** `/pages/guide-amenagement-bureau-professionnel` (3 355 mots) et `/pages/formation-ergonomie-entreprise` (1 634 mots) existent déjà. Le modèle de page pro fonctionne chez eux, il n'a jamais été décliné.

## 4. La stratégie pSEO : croiser secteur, taille et motif

Le catalogue est découpé par produit. Les pages manquantes sont celles qui découpent par situation d'achat : secteur, taille du parc, financement, motif de santé.

**M1, secteur × équipement** (Do, BoFu)
- URL : `/pages/mobilier-ergonomique-[secteur]`. Coworking, collectivité, cabinet, bibliothèque, agence, industrie, établissement culturel.
- Variable : le secteur. ~8 à 12 pages.
- Donnée par page : l'installation réelle du secteur (volume, gamme posée, contrainte résolue), les services associés (montage, reprise, garantie étendue).
- Anti-thin : une page ne sort que si une installation ou un argument sectoriel réel la remplit. Pas de page pour un secteur sans référence.

**M2, nombre de postes × équipement** (Do, BoFu)
- URL : `/pages/equiper-[N]-postes`. 5, 10, 20, 30, 50 postes.
- Variable : la taille du parc. ~5 pages.
- Donnée par page : les volumes réellement livrés (10, 19, 33, 35, 50), délai, logistique, tarif dégressif, parcours de devis.
- Anti-thin : chaque page porte un cas chiffré et un volume réellement livré.

**M3, comparaison entre gammes** (Do, BoFu)
- URL : `/pages/[gamme]-ou-[gamme]`. Dynamic ou Lift, Lift ou Space, manuel ou électrique, un moteur ou deux.
- Variable : le couple de gammes. ~6 à 8 pages.
- Donnée par page : plateau, piètement, course de réglage, charge, prix, garantie, avis clients de chaque gamme.
- Anti-thin : consolider avec les trois articles de blog existants. Vérifier la cannibalisation avant publication.

**M4, financement et dispositifs** (Do, BoFu)
- URL : `/pages/financer-bureau-[dispositif]`. Amortissement, TVA, aides à l'aménagement de poste, budget CSE, forfait télétravail.
- Variable : le dispositif. ~5 pages.
- Donnée par page : le cadre réel du dispositif, ce que KQUEO fournit (facture, attestation, devis), lien vers le devis.
- Anti-thin : sourcer chaque dispositif sur la source officielle. Les deux articles de blog existants sont réécrits et redirigés, pas dupliqués.

**M5, motif de santé × sélection produits** (Do, BoFu)
- URL : `/collections/bureau-[motif]` et `/collections/chaise-[motif]`. Mal de dos, hernie discale, sciatique, canal carpien, grossesse.
- Variable : le motif. ~6 à 10 pages.
- Donnée par page : sélection de produits, critères de l'ergonome, avis des clients concernés, lien vers l'article de blog qui traite déjà le sujet.
- Anti-thin : collection marchande, pas article. L'article reste, il maille vers la collection.

### Priorisation

| Modèle | Pages possibles | Effort | Compétition | Intention | Données dispo | Priorité |
|---|---|---|---|---|---|---|
| M1 secteur | 8 à 12 | Moyen | Faible | Très forte | Fortes (5 cas) | 1 |
| M2 nombre de postes | 5 | Faible | Faible | Très forte | Fortes | 2 |
| M5 motif de santé | 6 à 10 | Faible | Moyenne | Forte | Fortes (24 articles) | 3 |
| M4 financement | 5 | Moyen | Faible | Forte | Moyennes | 4 |
| M3 gammes | 6 à 8 | Faible | Faible | Forte | Fortes | 5 |

**Reco.** Démarrer par M1 et M2 : ce sont les deux modèles que la data client remplit immédiatement et qui visent le panier le plus élevé. M5 ensuite, parce qu'il rentabilise 24 articles déjà écrits pour un effort faible. M3 en dernier malgré son effort faible : il sert la conversion plus que l'acquisition.

**Chantier technique parallèle, hors production de pages.** Balisage `aggregateRating` sur les 78 produits, `h1` textuel en accueil, remontée de l'espace professionnels dans la navigation, réécriture d'`agents.md` avec gammes, garanties et références.

## 5. Roadmap 90 jours

- Sem. 1-2 : cadrage, connexion GSC, relevé de ce sur quoi le site ressort déjà (52 collections et 143 articles compris), liste des requêtes de décision par axe, arbitrage des secteurs à traiter selon les références disponibles.
- Sem. 3-4 : chantier technique (avis balisés, h1, navigation, agents.md), construction des gabarits M1 et M2, entretien avec l'ergonome pour capter la matière.
- Sem. 5-8 : production des premières pages M1 et M2, espace professionnels développé, maillage croisé depuis les collections et les articles concernés, contrôle d'indexation.
- Sem. 9-12 : M5 et M4, mesure GSC, optimisation de l'existant, décision autonomie avec l'agent SEO ou prolongation.

Rythme : 10 à 15 pages par mois, 45 à 50 à trois mois.

## 6. Notes pour le call

**Hook d'ouverture.** « Vous avez 50 bureaux posés à l'Opéra Garnier, 33 chez IPTEK, 35 chez EAS. La page qui raconte ça fait 1 100 mots et on la trouve seulement en pied de page. C'est là qu'il y a de l'argent à récupérer. »

**Questions à poser.**
- Quelle part du chiffre d'affaires vient des entreprises, et où vous voulez l'emmener ?
- D'où viennent les projets d'aménagement aujourd'hui : réseau, salons, site, appels d'offres ?
- Combien de demandes de devis par mois, et qui les traite ?
- Qui a la main sur le thème Shopify, et jusqu'où on peut modifier nous-mêmes ?
- Le blog, c'est produit en interne ou par une agence ? Depuis combien de temps ?
- Il y a un objectif sur le showroom, ou c'est accessoire ?

**Freins probables.**
- « On a déjà beaucoup de contenu. » → Oui, et c'est justement le sujet : 143 articles qui répondent à des questions que ChatGPT traite sans renvoyer de clic. On construit les pages qui portent une décision d'achat. Aucun article de blog supplémentaire.
- « Le SEO c'est lent. » → Le chantier technique sur les avis se voit en quelques semaines dans les résultats. Les pages d'équipement mettent plus longtemps et visent un panier à plusieurs milliers d'euros.
- « On travaille déjà avec quelqu'un. » → Demander ce qui est produit, à quel rythme, et sur quel type de page. Si la réponse est « des articles de blog », l'écart avec ce qu'on propose se voit tout seul.
- « Notre site est sur Shopify, on est limités. » → Le balisage des avis, les pages et les collections se font dans Shopify, souvent plus vite que sur un site sur mesure.
- Budget. → Le retour se calcule sur une seule commande d'équipement à 20 ou 50 postes.

**Closing.** Repartir avec la roadmap 90 jours datée, l'accès GSC demandé, et la liste des secteurs sur lesquels ils ont des références exploitables. Format probable : accompagnement 3 mois avec agent SEO à la clé, puis décision.

## 7. À vérifier / suite

- Confirmer en GSC ce sur quoi le site ressort déjà avant de figer la liste des modèles, en particulier sur les motifs de santé (les 24 articles peuvent déjà occuper le terrain).
- Vérifier la cannibalisation potentielle entre les collections existantes par usage (open space, petit espace) et les pages M1 secteur.
- Vérifier si les avis Société des Avis Garantis peuvent être balisés produit par produit ou seulement au niveau du site : ça change le chantier technique.
- Vérifier s'il existe d'autres domaines ou versions en ligne au-delà de kqueo.com.
- Demander les installations non publiées : cinq cas sont en ligne, il y en a probablement plus.

Liens : [[modele-deck-slides]], [[feedback_vocabulaire_livrables_clients]]
