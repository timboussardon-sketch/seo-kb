---
type: pre-call
slug: modele-pre-call
title: "Modèle — Pré-call prospect (protocole + squelette)"
prospect: "[MODÈLE]"
date: 2026-06-04
statut: modèle réutilisable
tags: [acquisition, pre-call, modele, pseo, geo, organikk]
---

# Modèle — Pré-call prospect

> Ce fichier n'est pas un pré-call : c'est le **moule**. On le copie en `raw/organikk/pré-call/<slug-prospect>.md`, on déroule le protocole, on remplit le squelette. Référence vivante : [[proximit]] (cas réel abouti), avec [[centrale-directe]] et [[pangaea-sports]] comme variantes e-commerce.

---

## Comment s'en servir (déclencheur)

Tim donne une URL (ou un nom + URL) et dit « prépare le pré-call ». Claude :
1. déroule le **protocole de collecte** (section A) sans inventer un chiffre,
2. fait tourner la **grille des 7 insights business** (section B) : c'est le cœur, ce qui doit ressortir pour le call,
3. remplit le **squelette de sortie** (section C),
4. sauve dans `raw/organikk/pré-call/<slug>.md` et signale ce qui reste à confirmer au call.

Règle dure : aucun volume, position ou trafic inventé. Tout chiffre non vérifié = `[À SOURCER]` ou « à récupérer en GSC au call ». La GSC du prospect est presque toujours indisponible avant le call : on la liste comme question, on ne la simule pas.

---

## A. Protocole de collecte (avant de raisonner)

Claude rassemble ce qui est public, dans cet ordre, et note la source de chaque fait.

1. **Identité & business** : site vitrine + sites/sous-domaines liés, page activités/offres, mentions légales, LinkedIn, annuaire-entreprises.data.gouv.fr (SIREN → date de création, capital, effectif, labels). On veut : depuis quand, taille, combien de pôles/métiers, qui décide.
2. **Modèle économique** : qui paie, pour quoi, panier probable, cycle de vente (lead entrant vs appel d'offres vs bouche-à-oreille), point de conversion réel (devis, démo, prise de RDV, achat).
3. **État SEO technique, sans outil payant** : ouvrir `/sitemap.xml` (et les sitemaps Yoast/CMS), compter les pages utiles par section, repérer les pages géo ou décisionnelles déjà existantes, la fraîcheur (lastmod), l'archi d'URL. Une refonte en cours = signal majeur.
4. **Surface GEO** : le métier produit-il des requêtes décisionnelles qu'un AI Overview ne dévore pas (B2B de niche, data propriétaire) ou au contraire des requêtes informationnelles que l'IA avale ? C'est ce qui décide de l'angle.
5. **[[concepts/data-proprietaire|Données propriétaires]]** : produits maison, méthodo, cas clients, terrain, chiffres internes. C'est le carburant anti-IA et la défendabilité.
6. **À demander au call (jamais simulé)** : accès GSC (impressions/mois, position moyenne, top 10, requêtes qui rapportent, leads attribués au SEO), poids de chaque pôle dans le CA, qui décide, qui pilote la refonte.

Skills SEO mobilisables pendant la collecte/raisonnement : `seo-modeles-pseo`, `seo-mots-cles-decisionnels`, `seo-peurs-objections`, `seo-entites-vectorielles`, `seo-product-led-seo`, `seo-geo-audit`. On les appelle pour structurer, jamais pour habiller.

---

## B. La grille des 7 insights business (le cœur)

C'est ici que se joue le call. Pour chaque ligne, Claude répond factuellement à partir de la collecte. Si une réponse est faible, on la marque comme question à poser. Un pré-call réussi, c'est 2-3 de ces insights tranchés net.

| # | Insight business | La question qu'on se pose | Ce qu'on en sort pour le call |
|---|---|---|---|
| 1 | **Niche défendable** | Sur quel pôle/offre sont-ils difficiles à attaquer (peu d'acteurs nationaux, intention 100 % décisionnelle, data propriétaire, anti-ChatGPT) ? | Le terrain où on attaque en premier, et pourquoi pas le pôle généraliste le plus concurrentiel. |
| 2 | **Le pain qui coûte de l'argent** | Quel problème business non dit perdent-ils aujourd'hui (leads qui partent ailleurs, dépendance bouche-à-oreille, refonte jolie mais invisible, dilution sur trop de métiers) ? | Le diagnostic interne. Reformulé en « ce que ça vous coûte », jamais répété tel quel au prospect. |
| 3 | **Le levier [[concepts/pseo-data-driven-models\|pSEO multi-axes]]** | Comment découper chaque pôle en axes (× ville, × type de structure/entreprise, × fonctionnalité, × problématique) et où est le croisement qui crée l'autorité ? | La stratégie concrète : 4-6 modèles de pages, priorisés. Voir grille pSEO section C.4. |
| 4 | **Le chemin vers le lead** | Chaque page créée renvoie vers quoi ? Où est le point de conversion ? Un outil [[concepts/product-led-seo\|Product-Led]] (audit/calculateur gratuit) capterait-il l'email du décideur au bon moment ? | L'argument « ça ramène des demandes entrantes », pas « ça fait du trafic ». |
| 5 | **Le timing / le hook d'ouverture** | Qu'est-ce qui rend le moment opportun maintenant (refonte en cours, lancement produit, saisonnalité, perte de position) ? | La première phrase du call. Ex. refonte = « c'est le seul moment où intégrer l'archi SEO coûte presque rien ». |
| 6 | **Les objections probables** | Qu'est-ce qui va bloquer (« on a déjà une agence », « on fait notre site nous-mêmes », « le SEO c'est lent », budget) ? | La réponse préparée pour chaque frein, à dégainer sans hésiter. |
| 7 | **La sortie de call** | Avec quoi le prospect repart-il ? Quel format d'accompagnement colle à sa maturité (bootcamp intensif si quelqu'un suit en interne, accompagnement 6 mois si enjeu business fort) ? | Le closing : une roadmap 90 jours datée + la proposition d'accompagnement adaptée. |

Anti-bullshit : pas de « visibilité », on parle citations IA / positions / leads / conversions. Pas de chiffre inventé. L'insight #2 (le pain) reste une analyse interne, on ne le balance pas frontalement au prospect.

---

## C. Squelette de sortie (à remplir)

Ordre validé : En résumé → Diagnostic → Angle → État SEO → pSEO multi-axes → Roadmap 90j → Notes call → À vérifier. Ouvre toujours par le bloc « En résumé ». Pas de tiret cadratin nulle part.

```markdown
---
type: pre-call
slug: pre-call-<prospect>
title: "Pré-call — <Prospect> (<domaine>)"
prospect: <Prospect>
date: <YYYY-MM-DD>
statut: prêt pour le call
tags: [acquisition, pre-call, pseo, <prospect>, <secteur>]
---

# Pré-call — <Prospect> (<domaine>)

## En résumé

[3-5 phrases. Qui ils sont, l'état SEO en une ligne, LE signal/preuve de pattern s'il existe, l'opportunité en une phrase (le levier pSEO multi-axes), par quoi on démarre et pourquoi. Finir par le hook du call et la reco de sortie.]

Sources : [liste des URLs et relevés, avec date]. SEO : [sitemaps relevés le YYYY-MM-DD]. GSC non disponible (prospect non connecté), à récupérer au call.

---

## 1. Diagnostic prospect

**Identité.** [Localisation, ancienneté, taille, labels, cible B2B/B2C.]

**Pôles / offres.** [Liste des métiers et des sites/sous-domaines associés.]

**Modèle & conversion.** [Qui paie, pour quoi, point de conversion réel.]

**Pain probable (analyse interne, pas à répéter tel quel).** [Insight #2 de la grille.]

**À récupérer au call (GSC).** [Impressions/mois, position moyenne, top 10, requêtes qui rapportent, leads SEO. Aucun chiffre avancé tant que la GSC n'est pas lue.]

---

## 2. L'angle : niche défendable d'abord

[Insight #1 : le pôle à attaquer en premier et pourquoi. Défendabilité (peu d'acteurs, intention décisionnelle, anti-IA Overview), data propriétaire réelle, potentiel Product-Led. Puis le second levier, puis ce qu'on ne fait PAS en premier (le pôle généraliste concurrentiel). Finir par le timing (insight #5).]

---

## 3. État des lieux SEO (sitemaps, YYYY-MM-DD)

[Par site/section : nombre de pages utiles, ce qui existe, ce qui est vide. Signal clé : la page géo/décisionnelle déjà présente qui prouve un pattern jamais décliné = l'ouverture pSEO.]

---

## 4. La stratégie pSEO : le croisement d'axes

[Le principe : l'autorité vient du croisement de plusieurs axes de découpe par pôle, pas d'un seul modèle. Puis, par pôle, lister les modèles M1, M2, M3... Chaque modèle :]

**M<n> — <Axe A> × <Axe B>** (intention visée)
- URL : /<pattern>/. Exemples de pages réelles.
- Variable : <la variable>. Volume estimé : ~N pages.
- Donnée par page : [ce qui remplit, terrain réel].
- Dédup / anti-thin : [ce qui existe déjà, la règle anti-page-vide].

### Priorisation

| Modèle | Pages possibles | Effort | Compétition | Intention/conversion | Données dispo | Priorité |
|---|---|---|---|---|---|---|
| M… | ~N | Faible/Moyen/Fort | Faible/Moyenne/Forte | Forte/Très forte | Fortes/Moyennes/Faibles | 1-5 |

Reco : [par quoi on démarre, l'ordre, pourquoi].

### Exemples de requêtes (volumes à sourcer, jamais inventés)
- M1 : [...]
- M2 : [...]

### 7 règles pSEO appliquées
Anti-thin, données terrain (zéro chiffre inventé), sourcing obligatoire, canonical propre, maillage différenciant par page, ≥1 élément Haute Surprise par section, passage ancré 150-200 mots + authorship par page.

---

## 5. Roadmap 90 jours

- Sem. 1-2 : [cadrage, variables, liste de requêtes par axe via seo-recherche-mots-cles + seo-mots-cles-decisionnels].
- Sem. 3-4 : [seo-entites-vectorielles + seo-cluster-aeo sur les piliers, construction des templates].
- Sem. 5-8 : [produire le pilote du modèle prioritaire, maillage croisé, resoumission GSC, contrôle indexation].
- Sem. 9-12 : [mesurer en GSC, garder ce qui indexe/performe, étendre le modèle gagnant, brancher l'outil Product-Led].

---

## 6. Notes pour le call (<durée>)

- Hook d'ouverture : « [insight #5, formulé] »
- Questions à poser : [qui décide, leads web vs autres, accès GSC, qui pilote la refonte, poids de chaque pôle dans le CA].
- Freins probables à lever : « [objection] » → [la réponse]. (insight #6)
- Closing : repartir avec la roadmap datée. [Bootcamp si quelqu'un suit en interne / accompagnement 6 mois si enjeu business fort]. (insight #7)

---

## 7. À vérifier / suite

- [Sitemaps ou pages à ouvrir pour confirmer.]
- Récupérer la GSC au call pour caler volumes, hiérarchie des cibles, chiffres J+90.
- Sortir la vraie liste de requêtes décisionnelles par axe prioritaire + le template de page du modèle gagnant.
```
