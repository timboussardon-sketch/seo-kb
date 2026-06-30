---
name: algorithme-journal-design-system
description: Design system du journal web « Algorithme » (actu Search/SEO/IA). Tokens, typo, composants et règles pour produire toutes les pages.
type: reference
created: 2026-06-30
status: DA validée par Tim
templates:
  - templates/template-accueil.html   # page d'accueil de référence (palette Cobalt figée)
  - templates/explorateur-palettes.html # même DA, 9 palettes au choix (R&D couleurs)
---

# Design System · Journal « Algorithme »

> Journal web d'actualité **Search / SEO / IA**. Mise en page **presse old school** (Le Monde / NYT) avec une **couche futuriste discrète** (données en direct, monospace, ticker). Palette **calme et moderne**.
>
> **Avant de créer une nouvelle page**, lire ce fichier puis partir du template `templates/template-accueil.html`. Ne jamais réinventer les tokens : ils sont la source unique.

## ADN (3 principes non négociables)

1. **Old school dans la structure** : serif éditorial, colonnes, filets (rules), double filet de masthead, lettrine. Ça doit ressembler à un vrai quotidien.
2. **Futuriste dans la donnée** : monospace pour tout ce qui est métadonnée / chiffre / état (ticker, indices, horodatage, « en direct »). Le futur passe par la data, pas par des dégradés tape-à-l'œil.
3. **Couleur calme** : un seul accent par page (Cobalt validé), fond clair et froid, encre presque noire. La couleur souligne, elle ne crie pas.

Cohérent avec la doctrine de Tim : factuel, sobre, zéro effet gratuit.

---

## 1. Tokens couleur — palette **Cobalt** (validée)

Source unique. Toujours via variables CSS, jamais de hex en dur dans une page.

| Variable | Hex | Rôle |
|---|---|---|
| `--paper` | `#F7F8FA` | Fond de page (gris très clair, froid) |
| `--card` | `#FFFFFF` | Fond des cartes / encadrés / figures |
| `--ink` | `#0F1419` | Texte principal, filets forts |
| `--ink-soft` | `#566072` | Texte secondaire, chapôs, légendes |
| `--rule` | `#E3E7ED` | Filets de séparation |
| `--rule-soft` | `#EDF0F4` | Filets entre colonnes (plus discrets) |
| `--accent` | `#2563EB` | Accent unique : labels, chiffres, liens hover, lettrine, « en direct » |
| `--accent-2` | `#6B7686` | Métadonnée (byline, sources, horodatage) |
| `--night` | `#0E1626` | Bandeaux sombres : ticker + colonne « chronique » |
| `--night-ink` | `#C9D4E6` | Texte sur fond sombre |
| `--night-glow` | `#6BA1FF` | Accent lumineux sur fond sombre (prompt, ▲) |

**Sémantique data** : hausse = `--night-glow` (▲), baisse = `#E59B86` (▼). Jamais de vert/rouge criards.

### Palettes alternatives (R&D, gelées)
La DA est paramétrée : `templates/explorateur-palettes.html` contient 9 palettes calmes/modernes (Indigo, Cobalt, Émeraude, Violet doux, Bleu glacier, Corail, Graphite, Ambre, Mode nuit). **Cobalt est la retenue.** On ne déploie pas les autres sans nouvelle validation, mais elles restent dispo pour un éventuel mode sombre (palette « Mode nuit ») ou un habillage saisonnier.

---

## 2. Typographie

3 familles, chacune un rôle strict. Pas de 4e police.

| Famille | Usage | Détails |
|---|---|---|
| **Fraunces** (serif) | Titres, gros chiffres d'indice, lettrine, nom du journal | poids 600, `letter-spacing` léger ; l'italique 500 sert la chronique |
| **Newsreader** (serif) | Corps de texte, chapôs, tagline en italique | 18px / 1.5 ; chapô 20-21px |
| **Space Mono** (monospace) | Tout le futuriste : labels, ticker, byline, horodatage, indices | 10.5-12px, `letter-spacing .12em`, `UPPERCASE` |

**Échelle des titres** (Fraunces, line-height ~1.0) :
- Nom du journal (masthead) : **72px**
- Titre Une : **52px**
- Titre de section / chronique : **30px**
- Titre d'article (colonnes) : **22px**
- Chiffre d'indice : **30px**

Règle : la hiérarchie se lit à la **taille du serif** + au **label monospace** au-dessus, jamais à la couleur.

---

## 3. Grille & espacements

- Conteneur : `max-width 1200px`, padding latéral `28px`.
- Grille héro : `1.65fr / 350px` (corps + colonne d'indices). Bascule en 1 colonne sous **920px**.
- Colonnes du fil : `column-count: 3`, `column-gap: 30px`, filet `--rule-soft` entre colonnes. 1 colonne en mobile.
- Rythme : blocs séparés par des filets `1px solid --rule` ; masthead et footer en **double filet** `3px double --ink`.
- Espacement vertical de référence : 14 / 18 / 24 / 30px.

---

## 4. Composants (catalogue)

Chaque page se compose de ces briques. Code de référence dans le template.

### 4.1 Ticker « console » (haut de page)
Bandeau sombre `--night`, prompt `algorithme ~ $` en `--night-glow`, indices qui défilent en monospace (animation `scroll`, dupliquer la liste pour la boucle infinie). Hausse ▲ = glow, baisse ▼ = corail. **Rôle : signal « en direct ».**

### 4.2 Masthead
Double filet bas `3px double --ink`. 3 colonnes alignées en bas : (gauche) N° + édition en mono ; (centre) label mono + nom du journal en Fraunces 72 + tagline italique ; (droite) date + pastille `● En direct` en `--accent` qui pulse. En dessous : nav de sections en monospace, séparée par un filet.

### 4.3 Hero (Une)
Grille `1.65fr / 350px`.
- Colonne principale : label de rubrique mono `--accent` → titre Fraunces 52 → chapô Newsreader 21 avec **lettrine** (`::first-letter` en Fraunces `--accent`) → byline mono `--accent-2` (auteur · temps de lecture · fiabilité · maj) → figure 21/8 (filet + légende sur carte).
- Colonne latérale : panneaux « Indice du jour » et « Fil de la nuit ».

### 4.4 Panneau d'indices (`.panel`)
Carte `--card` + filet. Titre h4 monospace `--accent` avec carré plein avant, souligné d'un filet. Lignes `metric` : gros chiffre Fraunces `--accent` (ou `--accent-2` si baisse) + libellé `--ink-soft` aligné à droite, séparées en pointillés.

### 4.5 Fil de la nuit / brèves (`.tick`)
Horodatage mono `--accent-2` (largeur fixe 42px) + titre court. Séparateurs en pointillés. Sert aussi de « à lire aussi » avec `→` au lieu de l'heure.

### 4.6 Fil en colonnes (`.threecol`)
Label de section souligné d'un filet `2px solid --ink`. 3 colonnes, chaque article : source mono `--accent-2` → titre Fraunces 22 → résumé `--ink-soft` 16px. La Une de chapô porte la lettrine, pas ces articles.

### 4.7 Bande « chronique de Tim » (`.strip`)
Grille `210px / 1fr`. Colonne gauche sombre `--night` avec le label en mono. Colonne droite `--card` : titre Fraunces **italique** 30 + texte. Sert aux prises de position éditoriales (voix Tim, voir [[ton-de-voix-tim]]).

### 4.8 Footer
Double filet haut. Deux mentions en monospace `--ink-soft`.

---

## 5. Niveaux de fiabilité (héritage des brèves)

Affichés dans la byline, repris du système de revue de Tim :
🟢 Confirmé · 🟡 Témoignage · 🟠 Débat · 🔵 Analyse. Voir [[breves-ia]] / [[media-reference]].

---

## 6. Règles d'or (do / don't)

**À faire**
- Un seul accent par page. La couleur souligne un chiffre, un label, un lien actif.
- Tout ce qui est « donnée / état » passe en **monospace UPPERCASE**.
- Tout ce qui est « éditorial » passe en **serif**.
- Espacer par des **filets**, pas par des ombres lourdes.
- Chiffres et stats : factuels et sourcés (doctrine Tim). Pas de chiffre inventé dans une vraie page.

**À ne pas faire**
- Pas de 2e couleur d'accent, pas de dégradé voyant, pas de néon.
- Pas de hex en dur : toujours les variables.
- Pas de 4e police.
- Pas de tiret cadratim dans le copy (règle Tim).
- Pas d'effets futuristes gratuits : le futur, c'est la data en direct, pas la déco.

---

## 7. Créer une nouvelle page (recette)

1. Dupliquer `templates/template-accueil.html`.
2. Garder le bloc `:root` **tel quel** (tokens Cobalt). Ne toucher qu'au contenu.
3. Réutiliser les composants du §4 selon le gabarit voulu (accueil, rubrique, page article…).
4. Respecter l'échelle typo (§2) et la grille (§3).
5. Vérifier les règles d'or (§6), surtout : un seul accent, mono = data, serif = édito.
6. Tester en local (`python3 -m http.server`) et montrer l'URL à Tim avant tout déploiement.

### Gabarits à produire ensuite
- [ ] **Page article** (lecture d'un sujet : titre, chapô, corps en colonnes, encadré sources, blocs Limites/Sources, fiabilité).
- [ ] **Page rubrique** (liste filtrée : Google / Moteurs IA / Études…).
- [ ] **La stat du jour** (page-chiffre citable, cf. skill `seo-page-statistiques`).
- [ ] **Mobile** poussé (ticker et grilles adaptés).

---

## Liens
- Voix éditoriale : [[ton-de-voix-tim]]
- Système de fiabilité / production : [[media-reference]], [[breves-ia]]
- Templates HTML : `templates/template-accueil.html`, `templates/explorateur-palettes.html`
