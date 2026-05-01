---
type: concept
title: Programmatique SEO (pSEO)
aliases: [programmatique-pseo, pseo, programmatic-seo]
tags: [pseo, scalable, template, longue-traine, doctrine-tim]
created: 2026-04-13
updated: 2026-04-13
sources: 4
confidence: high
status: stable
---

# Programmatique SEO (pSEO)

**Définition opérationnelle Tim** : 1 template + 1 variable qui change = des centaines/milliers de pages uniques qui rankent chacune sur un mot-clé longue traîne. Le produit est la combinaison **base de données × structure de page**, pas le contenu écrit à la main.

## Principe

Identifier des modèles où la variable génère naturellement des intentions de recherche distinctes :

- ville × type de service
- profil voyageur × destination
- secteur × cas d'usage outil
- événement × offre associée
- contrainte × configuration produit

Chaque combinaison = 1 page = 1 mot-clé longue traîne. À partir de ~50 pages par modèle, le maillage interne crée une autorité topique difficile à attaquer.

## Différence avec contenu éditorial classique

| Éditorial | pSEO |
|---|---|
| 1 article = 1 sujet réfléchi | 1 template = N pages générées |
| Effort linéaire (1h/article) | Effort fixe (template) + marginal (data) |
| ~50-200 articles/an réaliste | ~500-5000 pages réalistes |
| Cible head terms et mid tail | Cible **longue traîne** majoritairement |

## Sources ingérées (4)

- [[sources/2026-04-12-tim-skills-seo-proprietary]] — skill `seo-programmatique-pseo` officiel (10 skills propriétaires Tim)
- [[sources/2026-04-13-prompt-pseo-produit-service]] — méga-prompt opérationnel sites produit/service
- [[sources/2026-04-13-prompt-pseo-non-produit]] — méga-prompt sites média/éditorial avec test substitution LLM
- [[sources/2026-04-13-victoria-garden-pseo]] — premier livrable client (5 modèles validés sur appart-hôtel Bordeaux)

## Règles non-négociables (issues des prompts opérationnels)

Les 7 règles qui s'appliquent à toute page pSEO produite par Tim :

1. **Contenu unique obligatoire** — template = structure, jamais texte. >30% de texte partagé entre 2 pages d'un même modèle = échec
2. **Zéro hallucination** — pas d'invention de chiffre, pas d'extrapolation
3. **Sourcing daté <3 ans** — toute donnée chiffrée a sa source ou devient qualitative
4. **Canonical propre** — 1 URL = 1 contenu
5. **Maillage différenciant** — graphe de liens unique par page
6. **Surprise Score** — chaque section apporte 1 élément High Surprise (cf. [[concepts/surprise-metric]])
7. **Grounding Score** — passage ancré 150-200 mots + bloc authorship ~50 mots par page (cf. [[concepts/grounding-score]] · [[concepts/passage-ranking]])

## Articulation 2 prompts produit vs non-produit

- **Sites produit/service** ([[sources/2026-04-13-prompt-pseo-produit-service]]) : moat naturel via data propriétaire. Pas de test substitution LLM obligatoire.
- **Sites non-produit** ([[sources/2026-04-13-prompt-pseo-non-produit]]) : aucun moat naturel. **Étape 0 substitution LLM obligatoire** + Règle 0 anti-substitution.

Le critère différenciant n'est pas le secteur — c'est la présence ou non d'une **donnée que seul le client possède** (prix réels, stock temps réel, configurations propriétaires, partenariats locaux).

## Limites

- Modèle exigeant en data : sans dataset propriétaire, le pSEO produit du contenu thin
- Risque de cannibalisation si 2 modèles ciblent la même intention
- ROI à 6-12 mois (pas un quick win)
- Coûts techniques (SSR, sitemap dynamique, schema markup) souvent sous-estimés

## Pages liées

[[sources/2026-04-13-prompt-pseo-produit-service]] · [[sources/2026-04-13-prompt-pseo-non-produit]] · [[sources/2026-04-13-victoria-garden-pseo]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[concepts/product-led-seo]] · [[concepts/test-substitution-llm]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/passage-ranking]] · [[concepts/fully-meets]]
