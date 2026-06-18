---
name: seo-pre-audit
description: >
  Prépare un pré-audit SEO/GEO complet d'un prospect ou d'un client AVANT un
  call, à partir de sa seule URL et de données 100% publiques (aucun outil
  payant, aucune GSC requise). Déroule un protocole de collecte, fait tourner
  une grille de 7 insights business, et produit un document structuré prêt pour
  le call (diagnostic, angle, état SEO, stratégie pSEO multi-axes, roadmap 90
  jours, notes de call). Règle absolue : aucun volume, position ou trafic
  inventé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "prépare le pré-call",
  "fais un pré-audit", "audit avant call", "analyse ce prospect", "prépare-moi
  ce client avant le rendez-vous", "pré-call sur [site]", ou quand il fournit
  une URL de prospect/client en demandant une analyse stratégique avant un
  échange commercial.
---

# Pré-audit prospect (avant un call)

Ce skill produit le document qu'on prépare AVANT un call avec un prospect ou un nouveau client. Il transforme une simple URL en une analyse stratégique exploitable, sans aucun accès privé (pas de Google Search Console, pas d'outil payant). Tout repose sur ce qui est public et sur un raisonnement business structuré.

## Le principe de base

Un bon pré-audit ne récite pas des données. Il tranche 2 ou 3 décisions stratégiques nettes : sur quel terrain ce site est défendable, quel problème business lui coûte de l'argent, et par quoi on démarre. Le reste (volumes, positions, trafic) se confirme pendant le call, en demandant l'accès aux données. On ne le simule jamais.

## Règle dure, non négociable

Aucun volume de recherche, aucune position, aucun chiffre de trafic n'est inventé. Tout chiffre non vérifié est marqué `[À SOURCER]` ou « à récupérer au call ». La GSC du prospect est presque toujours indisponible avant le call : on la liste comme question à poser, on ne la devine pas. Un chiffre inventé dans un pré-audit, c'est la crédibilité perdue dès la première vérification.

## Déclencheur

L'utilisateur donne une URL (ou un nom + URL) et demande de préparer le pré-call ou le pré-audit. On déroule alors les trois phases dans l'ordre : collecte (A), grille des 7 insights (B), squelette de sortie (C).

---

## Phase A. Protocole de collecte (avant de raisonner)

Rassembler ce qui est public, dans cet ordre, en notant la source de chaque fait.

1. **Identité et business.** Site principal et sous-domaines liés, page activités/offres, mentions légales, LinkedIn, registres d'entreprises publics (date de création, taille, effectif, labels). On veut savoir : depuis quand ils existent, leur taille, combien de pôles ou métiers ils couvrent, qui décide.

2. **Modèle économique.** Qui paie, pour quoi, panier probable, cycle de vente (lead entrant, appel d'offres, bouche-à-oreille), et le point de conversion réel (devis, démo, prise de rendez-vous, achat).

3. **État SEO technique, sans outil payant.** Ouvrir `/sitemap.xml` et les sitemaps du CMS, compter les pages utiles par section, repérer les pages géographiques ou décisionnelles déjà existantes, la fraîcheur (lastmod), l'architecture des URL. Une refonte en cours est un signal majeur.

4. **Surface GEO.** Le métier produit-il des requêtes décisionnelles qu'une réponse d'IA générative ne dévore pas (B2B de niche, data propriétaire), ou au contraire des requêtes informationnelles que l'IA avale entièrement ? C'est ce qui décide de l'angle.

5. **Données propriétaires.** Produits maison, méthodologie, cas clients, terrain, chiffres internes. C'est le carburant anti-IA et la défendabilité du site.

6. **À demander au call (jamais simulé).** Accès GSC (impressions par mois, position moyenne, top 10, requêtes qui rapportent, leads attribués au SEO), poids de chaque pôle dans le chiffre d'affaires, qui décide, qui pilote la refonte.

Skills complémentaires mobilisables pendant la collecte et le raisonnement, si disponibles : `seo-modeles-pseo`, `seo-mots-cles-decisionnels`, `seo-peurs-objections`, `seo-entites-vectorielles`, `seo-product-led-seo`, `seo-geo-audit`. On les appelle pour structurer l'analyse, jamais pour l'habiller.

---

## Phase B. La grille des 7 insights business (le cœur)

C'est ici que se joue le call. Pour chaque ligne, répondre factuellement à partir de la collecte. Si une réponse est faible, la marquer comme question à poser au call. Un pré-audit réussi, c'est 2 ou 3 de ces insights tranchés net.

| # | Insight | La question qu'on se pose | Ce qu'on en sort |
|---|---|---|---|
| 1 | **Niche défendable** | Sur quel pôle ou offre sont-ils difficiles à attaquer (peu d'acteurs nationaux, intention 100% décisionnelle, data propriétaire, requêtes que l'IA ne mange pas) ? | Le terrain où on attaque en premier, et pourquoi pas le pôle généraliste le plus disputé. |
| 2 | **Le pain qui coûte de l'argent** | Quel problème business non dit perdent-ils aujourd'hui (leads qui partent ailleurs, dépendance au bouche-à-oreille, site refait joli mais invisible, dispersion sur trop de métiers) ? | Le diagnostic interne. Reformulé en « ce que ça vous coûte », jamais répété tel quel au prospect. |
| 3 | **Le levier pSEO multi-axes** | Comment découper chaque pôle en axes (par ville, par type de structure, par fonctionnalité, par problématique) et où est le croisement qui crée l'autorité ? | La stratégie concrète : 4 à 6 modèles de pages, priorisés (voir squelette C.4). |
| 4 | **Le chemin vers le lead** | Chaque page créée renvoie vers quoi ? Où est le point de conversion ? Un outil gratuit (audit, calculateur) capterait-il l'email du décideur au bon moment ? | L'argument « ça ramène des demandes entrantes », pas « ça fait du trafic ». |
| 5 | **Le timing, le hook d'ouverture** | Qu'est-ce qui rend le moment opportun maintenant (refonte en cours, lancement produit, saisonnalité, perte de position) ? | La première phrase du call. Exemple : refonte en cours = « c'est le seul moment où intégrer l'archi SEO coûte presque rien ». |
| 6 | **Les objections probables** | Qu'est-ce qui va bloquer (« on a déjà une agence », « on fait notre site nous-mêmes », « le SEO c'est lent », budget) ? | La réponse préparée pour chaque frein, à dégainer sans hésiter. |
| 7 | **La sortie de call** | Avec quoi le prospect repart-il ? Quel format d'accompagnement colle à sa maturité ? | Le closing : une roadmap 90 jours datée et la proposition adaptée. |

Anti-bullshit : on ne parle pas de « visibilité », on parle de citations IA, de positions, de leads, de conversions. Pas de chiffre inventé. L'insight 2 (le pain) reste une analyse interne, on ne le balance pas frontalement au prospect.

---

## Phase C. Squelette de sortie (à remplir)

Ordre validé : En résumé, puis Diagnostic, Angle, État SEO, pSEO multi-axes, Roadmap 90 jours, Notes de call, À vérifier. Toujours ouvrir par le bloc « En résumé ». Pas de tiret cadratin nulle part. Style direct, factuel, tutoiement si c'est la voix de l'auteur.

```markdown
# Pré-audit — <Prospect> (<domaine>)

## En résumé

[3 à 5 phrases. Qui ils sont, l'état SEO en une ligne, le signal ou la preuve
de pattern s'il existe, l'opportunité en une phrase (le levier pSEO multi-axes),
par quoi on démarre et pourquoi. Finir par le hook du call et la reco de sortie.]

Sources : [URLs et relevés, avec date]. SEO : [sitemaps relevés le YYYY-MM-DD].
GSC non disponible (prospect non connecté), à récupérer au call.

## 1. Diagnostic prospect

**Identité.** [Localisation, ancienneté, taille, labels, cible B2B/B2C.]
**Pôles / offres.** [Liste des métiers et des sites associés.]
**Modèle et conversion.** [Qui paie, pour quoi, point de conversion réel.]
**Pain probable (analyse interne, pas à répéter tel quel).** [Insight 2.]
**À récupérer au call (GSC).** [Impressions/mois, position moyenne, top 10,
requêtes qui rapportent, leads SEO. Aucun chiffre avancé tant que la GSC n'est
pas lue.]

## 2. L'angle : niche défendable d'abord

[Insight 1 : le pôle à attaquer en premier et pourquoi. Défendabilité (peu
d'acteurs, intention décisionnelle, requêtes que l'IA ne mange pas), data
propriétaire réelle, potentiel d'outil gratuit. Puis le second levier, puis ce
qu'on ne fait PAS en premier (le pôle généraliste disputé). Finir par le timing
(insight 5).]

## 3. État des lieux SEO (sitemaps, YYYY-MM-DD)

[Par site ou section : nombre de pages utiles, ce qui existe, ce qui est vide.
Signal clé : la page géo ou décisionnelle déjà présente qui prouve un pattern
jamais décliné = l'ouverture pSEO.]

## 4. La stratégie pSEO : le croisement d'axes

[Le principe : l'autorité vient du croisement de plusieurs axes de découpe par
pôle, pas d'un seul modèle. Puis, par pôle, lister les modèles M1, M2, M3.
Chaque modèle :]

**M<n> — <Axe A> × <Axe B>** (intention visée)
- URL : /<pattern>/. Exemples de pages réelles.
- Variable : <la variable>. Volume estimé : ~N pages.
- Donnée par page : [ce qui remplit la page, terrain réel].
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
Anti-thin, données terrain (zéro chiffre inventé), sourcing obligatoire,
canonical propre, maillage différenciant par page, au moins un élément de Haute
Surprise par section, passage ancré de 150 à 200 mots avec authorship par page.

## 5. Roadmap 90 jours

- Sem. 1-2 : [cadrage, variables, liste de requêtes par axe (recherche de
  mots-clés + mots-clés décisionnels)].
- Sem. 3-4 : [entités vectorielles + cluster sur les piliers, construction des
  templates].
- Sem. 5-8 : [produire le pilote du modèle prioritaire, maillage croisé,
  resoumission GSC, contrôle d'indexation].
- Sem. 9-12 : [mesurer en GSC, garder ce qui indexe et performe, étendre le
  modèle gagnant, brancher l'outil gratuit].

## 6. Notes pour le call (<durée>)

- Hook d'ouverture : « [insight 5, formulé] »
- Questions à poser : [qui décide, leads web vs autres, accès GSC, qui pilote la
  refonte, poids de chaque pôle dans le CA].
- Freins probables à lever : « [objection] » → [la réponse]. (insight 6)
- Closing : repartir avec la roadmap datée + la proposition adaptée à la
  maturité du prospect. (insight 7)

## 7. À vérifier / suite

- [Sitemaps ou pages à ouvrir pour confirmer.]
- Récupérer la GSC au call pour caler les volumes, la hiérarchie des cibles, les
  chiffres J+90.
- Sortir la vraie liste de requêtes décisionnelles par axe prioritaire + le
  template de page du modèle gagnant.
```

---

## Checklist de qualité avant de livrer

- Le bloc « En résumé » ouvre le document et tranche l'opportunité en une phrase.
- 2 ou 3 insights de la grille sont tranchés net, pas noyés.
- Zéro chiffre inventé : chaque volume/position/trafic est sourcé ou marqué à récupérer.
- L'angle dit clairement par quoi on démarre ET ce qu'on ne fait pas en premier.
- Chaque modèle pSEO a une variable réelle et une donnée qui remplit la page (pas de page vide).
- Le hook d'ouverture et les réponses aux objections sont prêts à dire à l'oral.
- Pas de jargon vide, pas de « visibilité », pas de tiret cadratin.
