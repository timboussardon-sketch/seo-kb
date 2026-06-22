---
type: journal
project: golfiller
date: 2026-06-22
tags: [golfiller, journal, contenu, pages-data, gf-article, pseo, seo]
---

# Golfiller — Journal du 2026-06-22 : pages blog + pages-data

Session de production de contenu blog golfiller.fr. Refonte d'une page existante, nouvel article, deux nouvelles pages-data (outils), recherche de mots-clés data-directory, et formalisation du template officiel. Tout livré en HTML prêt à coller dans Shopify (vue code). Voir le cas global [[golfiller-strat]] et le tracker `prestation/clients/golfiller.md`.

## Ce qui a été produit (fichiers)

Outputs dans `content-brain/golfiller/outputs/` :
- `2026-06-22-classement-meilleures-balles-MAJ.html` — 1re passe : injection de data dans la page classement existante, sans style (rich-text Shopify).
- `2026-06-22-classement-meilleures-balles-STYLEE.html` — **version finale** : refonte de la page « meilleures balles » au template gf-article + couleurs de marque.
- `2026-06-22-balles-des-pros-STYLEE.html` — nouvel article « Quelles balles utilisent les pros du PGA Tour ? » (Top 8 + Tiger Woods).
- `2026-06-22-flex-shaft-vitesse-swing-STYLEE.html` — nouvelle page-data « Quel flex de shaft selon votre vitesse de swing ? ».
- `2026-06-22-convertisseur-yards-metres-mph-kmh-STYLEE.html` — nouvel outil « Convertisseur yards↔mètres / mph↔km/h ».

Template + mémoire :
- `raw/golfiller/pages/_TEMPLATE-gf-article-CSS.html` — template officiel ARTICLES formalisé (CSS + squelette + patterns).
- Mémoire auto : `reference_golfiller-gf-article-template` (couleurs marque + parades Shopify + patterns contenu).

## Détail des travaux

### 1. Refonte page « meilleures balles » (classement 7 catégories)
Page live importée de Medium (classes `graf--*`). Objectif : mettre à jour sans casser le SEO existant.
- Gardé tout le contenu d'origine + densifié.
- Injecté : compression chiffrée par modèle (AD333 68, Chrome Soft 72, TP5 85, TP5x 97, Z-Star 88), table distance/vitesse, table sélection distance triée par compression + prix occasion, maillage interne, bloc Sources.
- Refondue au template gf-article (cf. ci-dessous).

### 2. Article « balles des pros du PGA Tour »
Repris le texte fourni (Top 1-8 + Tiger Woods), enrichi : tableau récap du Top 8 (joueur/modèle/marque/compression, fort AEO), compression par modèle, section conversion « jouez la balle des pros en reconditionné », FAQ AEO, sources.

### 3. Template gf-article OFFICIEL formalisé (apprentissage clé)
La « bonne mise en page » = le template de la page live `balle-de-golf-pour-la-distance` (`.gf-article`), PAS le template Bebas Neue `.golf-page` (qui reste pour pages outils/landing).
- **Couleurs de marque pixel perfect** (relevées dans le thème Shopify, pas inventées) : teal `#108474` (liens/CTA/puces), turquoise `#5BD8C0` (fond en-têtes `th`), encre `#13241D`.
- **3 parades anti-thème Shopify** (le thème écrase le `<style>`, donc inline `!important`) : fond `th`, `summary` en flex, aération FAQ. Toggle `+/−` = vrai `<span class="gf-ico">` (pas `::after`).
- **Toujours coller en VUE CODE (`</>`)** sinon le `<style>`/`<script>` saute.

### 4. Recherche mots-clés « pages-data / directories »
24 mots-clés générés (familles : balles, parcours, clubs/fitting, index/score, conversions/conditions). Top 6 priorisé. Sortie type seo-recherche-mots-cles (sans volume). À ranger éventuellement dans `wiki/keywords/`.

### 5. Page-data n°4 : flex de shaft selon vitesse de swing
- Tableau flex L/A/R/S/X par vitesse driver (km/h + mph) + distance indicative.
- **Sourcing corrigé après retour d'un expert de Tim** : les fourchettes flex viennent de True Spec Golf, recoupées sur Golf.com + Golf Sidekick (chartes concordantes), affichées comme indicatives. Vitesses/distances = data golfiller (TrackMan/Shot Scope).
- 3 nuances d'expert intégrées : direction ≠ flex seul ; tempo/transition/profil du shaft comptent ; moyenne amateur 135-145 km/h (pas 150).

### 6. Page-data n°6 : convertisseur yards↔mètres / mph↔km/h
Outil pur (2 convertisseurs JS bidirectionnels + tables de référence), texte minimal et factuel. JS en addEventListener + DOMContentLoaded (compat Shopify).

### 7. Slope/SSS des golfs de France (mot-clé n°1) — NON produit
La page existe DÉJÀ sur golfiller.fr (35 golfs / 40 tracés, slope par couleur + SSS, calculateur handicap FFGolf, 35 fiches). Donc n°1 déjà capturée, on ne la duplique pas (cannibalisation). Data sourcée FFGolf + agrégateurs + sites clubs.

## Décisions / règles apprises
- Template ARTICLES = gf-article ; pages outils/landing = golf-page (Bebas).
- Couleurs de marque obligatoires (teal #108474, th turquoise #5BD8C0), jamais le vert générique du gf-article.
- Anti-thème Shopify : inline `!important` sur th, summary, aération FAQ ; coller en vue code.
- Data : soit propriétaire golfiller, soit sourcée et recoupée x2, jamais inventée. Retour expert intégré sur le flex.

## Opportunité repérée (à exploiter)
La page slope existante a une « balle recommandée » par parcours (Pro V1, Chrome Soft, AD333…). Si ces mentions ne sont pas des liens vers les collections/produits → conversion non exploitée. Action rapide possible : transformer chaque mention en lien.

## Reste à faire / prochaines pages-data candidates
- Vérifier/poser les **liens produits** des Top 5 (slugs `golfiller.fr/products/...` déduits, à confirmer).
- Choisir la prochaine page-data : Équivalent Pro V1 pas cher (conversion) · Prix moyen green fee par région (data tarifs déjà en main) · Loft des clubs.
- Slugs proposés : `flex-de-shaft-selon-vitesse-de-swing`, `convertisseur-yards-metres-mph-kmh`.

Pages liées : [[golfiller-strat]] · template `raw/golfiller/pages/_TEMPLATE-gf-article-CSS.html`
