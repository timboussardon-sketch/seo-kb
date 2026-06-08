---
title: Méthode Lead Gen SEO (Tim Boussardon / Organikk)
type: synthese
status: brouillon
date: 2026-05-08
sources:
  - "[[process-seo-b2b-2026]]"
  - "[[skill-product-led-seo]]"
  - "[[know-simple-know-do]]"
  - "[[analyse-calls-prospects-bootcamp]]"
  - "[[offre-bootcamp-seo-ia]]"
  - "[[methode-organikk-4-piliers]]"
  - "[[cluster-business-organikk-source]]"
  - "[[vendre-seo-ia-2026]]"
tags:
  - lead-gen
  - seo
  - methode
  - acquisition
  - b2b
---

# Méthode Lead Gen SEO

Doc de synthèse compilant tout ce que la KB contient sur la conversion du SEO en canal d'acquisition (et non plus de visibilité). Sert de socle pour les futurs articles piliers, briefs commerciaux, slides bootcamp. Synthèses voisines : [[syntheses/vendre-seo-ia-2026]], [[syntheses/workflow-complet-consultant-seo-ia]].

## 0. Thèse de fond

Le SEO n'est plus un canal de visibilité, c'est un canal d'acquisition au même titre que le SEA. Le mot "visibilité" évoque les réseaux sociaux et brouille la promesse côté client. On parle de mots-clés business, conversions, leads qualifiés.

Conséquence directe sur les KPI :

| À bannir         | À installer                    |
| ---------------- | ------------------------------ |
| Position moyenne | Leads SQL par URL              |
| Trafic total     | Revenue par cluster sémantique |
| Impressions      | CAC par mot-clé                |
| Backlinks        | Deals influencés SEO           |

Si le SEO augmente le trafic mais pas les leads qualifiés, ce n'est pas un problème SEO. C'est un problème de ciblage de mot-clé.

Source : [[process-seo-b2b-2026]]

## 1. Discovery interne : la data propriétaire est la seule vérité

Les outils classiques sont en retard sur la longue traîne LLM (passage de 4 mots à 24 mots en moyenne par requête). Les mots-clés qui convertissent sont des micro-intentions sans volume mesurable. Donc on ne les trouve pas dans les outils du marché.

### Stack d'extraction de micro-intentions

1. Calls commerciaux enregistrés (Gong, Modjo, Attention) : 10 à 20 formulations exactes par call deviennent des mots-clés bruts.
2. Tickets SAV (Zendesk, Freshdesk).
3. Chat support (Intercom, Crisp).
4. Avis publics (G2, Trustpilot, Capterra) : langages authentiques de prospects.
5. CRM, champ "raison du deal perdu" : objections réelles, freins psychologiques.
6. Post LinkedIn.
7. Communautés Slack/Discord
8. Google Search Console croisée avec le CRM : tracer les sessions organiques jusqu'aux opportunités closes pour reconstruire les requêtes gagnantes.

### Validation de conversion

Croiser GSC + CRM sur les deals déjà signés. Scoring d'un mot-clé : CPC × intention × proximité offre. Tout mot-clé bon CPC mais distance produit trop grande devient un orphelin et reste hors roadmap.

Source : [[process-seo-b2b-2026]]

## 2. Framework éditorial : Know-Simple / Know / Do

Cadre : [[concepts/know-simple-know-do]]. Remplace TOFU/MOFU/BOFU. Pensée linéaire en funnel devient atomes d'intention lisibles par les agents IA.

| Intention | Description | Format type | Schema | CTA |
|---|---|---|---|---|
| Know-Simple | Réponse factuelle courte | FAQ 50 à 100 mots, définition | FAQPage + DefinedTerm | Lien vers Know |
| Know | Comprendre en profondeur | Guide long, méthode, comparatif, essai thought leadership | HowTo + Article / ScholarlyArticle | Lien vers Do |
| Do | Accomplir une action concrète | Outil, calculateur, simulateur, comparateur, générateur, démo, formulaire | WebApplication / Service | Email + RDV |

### Règles de maillage

- Know vers Do prioritaire sur Know vers Know. Un utilisateur informé doit pouvoir agir avant de re-lire.
- Do vers page commerciale uniquement. Pas de fuite vers d'autres Know depuis une page Do.
- Toute page Do doit pouvoir être atteinte en 2 clics depuis la home et 1 clic depuis sa page Know parente.

Source : [[know-simple-know-do]]

## 3. Product-Led SEO : les pages "Do" qui captent

Cadre : [[concepts/product-led-seo]]. Le produit (outil, calculateur, template) génère le trafic ET la conversion, à la place du texte passif. C'est le format que Google note [[concepts/fully-meets|"Fully Meets"]] sur l'échelle Quality Raters.

### Typologie de mots-clés à attaquer

- Calculer : ROI, budget, coût, simulateur
- Générer : document, checklist, template, brief
- Auditer : score, diagnostic, analyse, benchmark
- Comparer : options, offres, solutions
- Planifier : roadmap, calendrier, étapes

### Pattern Valeur Gratuite, Gate, Premium

```
1. Résultat partiel gratuit (score sur 100, par exemple)
   Email pour débloquer le rapport complet
   Upsell vers audit personnalisé avec un expert

2. Simulateur basique gratuit
   Email pour sauvegarder et recevoir les mises à jour
   Retargeting vers offre d'accompagnement

3. Checklist générée gratuitement
   Login pour télécharger le PDF
   Nurturing par séquence email avec cas clients
```

### Triple bénéfice

- Google classe la page "Fully Meets" (note maximale Quality Raters).
- Capture email immédiate parce que le CTA est le calcul lui-même.
- Concurrents text-only ne peuvent pas répliquer rapidement, donc avantage durable.

### Surprise Gap intégré dans l'outil

- Benchmark interne propriétaire (par exemple : corrélation fréquence de publication / croissance trafic sur 847 sites).
- Score prédictif basé sur un algo maison.
- Comparaison automatique avec N entreprises du secteur.

Source : [[skill-product-led-seo]]

## 4. Cartographie d'entités vectorielles (Grounding Score)

Cadres : [[concepts/entites-vectorielles]] et [[concepts/grounding-score]]. Pour qu'une page rank, elle doit être alignée mathématiquement avec l'intention de recherche dans l'espace vectoriel des LLM. Donc on cartographie les entités attendues.

### 4 catégories à mapper

1. Techniques : normes, certifications, frameworks, intégrations, stack.
2. Preuves quantitatives : chiffres sectoriels, benchmarks, résultats clients signés.
3. Vecteurs multimodaux : YouTube, vidéos, podcasts, schémas.
4. Divergence (Haute Surprise) : entités sur lesquelles les concurrents ne sont pas allés.

### Intentions B2B ultra-transactionnelles à mapper systématiquement

- "alternative à [concurrent]"
- "[outil A] vs [outil B]"
- "meilleur [outil] pour [cible]"
- "prix [outil]"
- "[outil] + [intégration]"

Source : [[process-seo-b2b-2026]] + skill `seo-entites-vectorielles`

## 5. Programmatique SEO : scaler sans tomber dans le thin content

La pSEO ancienne école (template creux, variable = nom de ville) est sanctionnée depuis Helpful Content Update. La bonne pSEO est un produit, pas un template.

### 3 couches obligatoires

1. Base de données structurée (Airtable, Notion, SQL). Pas Excel. Champs typés : variables principales, attributs, preuves chiffrées, exemples sectoriels, limites, cas d'usage.
2. Logique conditionnelle éditoriale. Le contenu change selon les variables. Paragraphe PME ≠ paragraphe ETI. Bloc technique si API, bloc no-code sinon.
3. Couche humaine ou IA supervisée. Exemples concrets, anecdotes, données fraîches, témoignages, captures écran.

### Combinaisons B2B qui marchent

- Ville × service (réglementation locale + écosystème + cas clients du territoire)
- Secteur × cas d'usage ("CRM cabinet d'avocat" + enjeux RGPD réels)
-  × alternative ("alternative HubSpot pour PME" + comparatif paramétré)
- Contrainte × configuration ("logiciel RH équipe 50" + fonctionnalités critiques)
- Intégration × plateforme ("Zapier pour Salesforce" + workflows concrets)

### Règle critique

Tester 10 URLs manuellement avant d'en générer 1000. Unicité de contenu supérieure à 60%, sinon Google considère la page non utile.

Source : [[process-seo-b2b-2026]] + [[concepts/programmatique-pseo]]

## 6. Objections clients comme source de pages

Les freins psychologiques sont des requêtes potentielles. On les pêche dans Grok (X/Twitter), Reddit, tickets SAV, reviews G2/Trustpilot.

### Traitement

- Option 1 : objection profonde + matière abondante (data, benchmarks, cas clients, démo) = page dédiée 1500 mots avec certifications, architecture, témoignages.
- Option 2 : objection ponctuelle = bloc FAQ dans une page pilier existante (gain en featured snippets et AEO).

Critère de choix : peut-elle tenir seule comme sujet à part entière, ou complète-t-elle un sujet plus large ?

Source : [[process-seo-b2b-2026]] + skill `seo-peurs-objections`

## 7. Vente du SEO : passer de 10% à 50% de closing

C'est la partie commerciale de la méthode. Un SEO bien architecturé qui ne se vend pas reste un cost center.

### 7 principes conversationnels

1. Bannir "visibilité". Dire "mots-clés business", "conversion", "leads qualifiés".
2. Data avant signature. Le closing passe de 10% à 50% quand on montre, pendant le call, les mots-clés business cibles (volume + CPC), la roadmap des 3 premiers mois, les positions actuelles vs potentielles, et les requêtes déjà gagnantes dans la GSC du prospect.
3. Règle 80/20. Ce qui ranke = 80% de consensus + 20% de data unique (calls, avis, jargon, chiffres).
4. Le prix n'est jamais le frein réel. Le frein, c'est le temps. Réponse : "3h par semaine intégrées au travail client, pas en plus."
5. Le call est un canal de conversion. Newsletter abonné, RDV 15 à 30 min (stats, 80/20, annulation sans frais, posture "pair not teacher"), email récap + Stripe.
6. Les prospects ont déjà testé l'IA. Ils en connaissent les limites. Ils veulent de la STRUCTURE, pas une découverte de l'IA.
7. Vendre un système, pas une formation.

| À dire | À éviter |
|---|---|
| Système SEO IA | Formation |
| Workflow propriétaire | Cours |
| Système | Apprentissage |

### Réponses types aux objections

| Objection | Réponse |
|---|---|
| "Ça change tout le temps" | 80% stable, 20% évolue. |
| "J'ai pas le temps" | 3h/semaine, intégré au travail client. |
| "C'est cher" | 1 client signé = amorti. 3 articles = remboursé. |
| "Je suis pas assez technique" | Zéro code. C'est de la réflexion. |

### Stats utiles à ressortir

- Rédaction : 1h30 à 45 min par article (divisé par 2).
- Closing : 10% à 50%.
- Top 2 sur "balle de golf" devant Décathlon et Amazon.
- 4× plus de conversions via ChatGPT que via Google.

Source : [[analyse-calls-prospects-bootcamp]] + [[vendre-seo-ia-2026]]

## 8. Architecture Organikk : 4 piliers de la méthode

Cadre : [[concepts/methode-organikk-4-piliers]] (synthèse [[syntheses/4-piliers-organikk]]). Le pilier AEO renvoie à [[concepts/aeo]] et [[concepts/agentic-search]] ; le carburant transverse reste la [[concepts/data-proprietaire]].

| Pilier | Question | Concept | KPI |
|---|---|---|---|
| Surprise Gap | Pourquoi on lit | Divergence vs consensus | Surprise Score par page |
| Grounding Score | Pourquoi on rank | Entités vectorielles + similarité cosinus | Alignment vs top 3 SERP |
| pSEO | Comment on scale | Modèles de pages data-driven | Pages indexées > 85% |
| AEO | Comment les LLM nous citent | Architecture AEO + citations IA | Taux de citation Perplexity / ChatGPT |

### Pyramide de dépendance

```
Surprise (fondation)
  Grounding
    pSEO
      AEO (architecture finale)
```

Sans Surprise, les pages sont génériques et ignorées des LLM. Sans Grounding, la pSEO est thin. Sans pSEO, l'AEO est incomplet (manque de surface). Sans AEO, on est invisible côté Agentic Search.

Source : [[methode-organikk-4-piliers]] + [[cluster-business-organikk-source]]

## 9. Avatar prospect bootcamp et déclencheurs d'achat

Le profil qui convertit (7 prospects sur 10) :

- 35 à 50 ans, médiane 42.
- Freelance ou indépendant.
- 3 à 15 ans dans le métier web.
- 2 à 8 clients actifs.
- CA de 2500 à 6000€/mois.
- Dénominateur commun = absence de système, pas niveau SEO.

### Douleurs classées par intensité

1. Redémarrage perpétuel (10/10) : chaque client = repartir de zéro.
2. IA sous-exploitée (9/10) : Claude utilisé à 30% au lieu de 80%.
3. Cercle vicieux temps / structure (8/10) : pas le temps de structurer, donc on perd du temps.
4. Peur d'obsolescence (7/10) : le train passe.
5. Contenu générique (7/10) : pas de data propriétaire.
6. Vente floue (6/10) : pitch générique, taux de signature bas.

### Déclencheur d'achat

Pas "apprendre le SEO". C'est "arrêter de perdre du temps".

Source : [[analyse-calls-prospects-bootcamp]]

## 10. Verbatims utiles pour rédactions futures

Verbatims de bootcamp à recycler dans les pages commerciales et la newsletter (vérifier l'autorisation avant publication nominative).

Sur le chaos et la demande de structure :

> "Mon process n'est pas optimal, je suis submergé." (Arnaud)
> "À chaque fois je rebricole sur d'autres choses." (Juliette)
> "Je copie les process des autres mais je me les suis pas appropriés." (Dev web)
> "Je n'ai pas un process carré." (Juliette)

Sur la peur du train IA :

> "Je suis en train de rater le train." (Julien)
> "Le train est en train de passer très, très vite et je ne le prends pas tant que ça." (Franck)

Sur la croyance en résultats réels :

> "Ta newsletter, tu donnes un angle différent par rapport aux autres." (Julien)

Source : [[analyse-calls-prospects-bootcamp]]

## 11. Chaîne de valeur Lead Gen SEO en une page

```
1. Découvrir : data interne (calls + CRM + GSC) > micro-intentions actionnelles
2. Architecturer : Know-Simple > Know > Do (atomes d'intention)
3. Amplifier : Product-Led + entités vectorielles + pSEO contrôlée
4. Convertir : objections en pages + data en amont du call (closing 80/20)
5. Systématiser : workflow reproductible 2 à 3 ans, pas de process ad-hoc
```

Métrique définitive : Leads SQL par URL. Pas impressions. Pas position. Pas trafic.

## 12. Roadmap d'implémentation type (90 jours)

- Jours 1 à 15 : extraction data interne (calls + CRM + GSC + reviews) et carte des micro-intentions.
- Jours 15 à 30 : framework Know / Do, sélection des 3 piliers Do prioritaires (calculateur, simulateur, audit).
- Jours 30 à 60 : production des pages piliers (1 Know de référence + 1 Do + maillage objections).
- Jours 60 à 75 : scale via programmatique SEO contrôlée sur les combinaisons validées (10 URLs test avant 100).
- Jours 75 à 90 : instrumentation conversion (CRM par URL, scoring CPC × intent × distance offre, dashboard leads SQL par cluster).

## 13. Pages cibles à dériver de cette synthèse

Pages piliers à écrire ensuite :
- "Lead gen SEO en B2B : la méthode complète" (pilier principal)
- "Pourquoi votre SEO génère du trafic mais pas de leads"
- "Product-Led SEO : transformer un outil en moteur d'acquisition"
- "Closing SEO : passer de 10% à 50% sans baisser les prix"

Pages satellites :
- "Know-Simple, Know, Do : le framework qui remplace le funnel"
- "Cartographier ses entités vectorielles avant d'écrire"
- "pSEO bien faite après Helpful Content Update"
- "Objection client en page SEO : décider entre page dédiée et bloc FAQ"

Outils Do à construire :
- Audit lead gen SEO (score sur 100 + 3 leviers prioritaires)
- Simulateur ROI SEO (mots-clés business × CPC × taux conversion)
- Générateur de roadmap 90 jours personnalisée

## TODO

- Sourcer chaque stat (1h30 à 45 min, 10% à 50%, 4× ChatGPT) avec un cas client précis dans `raw/journal/`.
- Vérifier les autorisations de citation nominative pour les verbatims bootcamp.
- Lier ce doc depuis [[index]] sous la section "Méthodes".
- Décider : pilier principal "Lead Gen SEO" en page commerciale Organikk, ou article de blog d'abord ?
