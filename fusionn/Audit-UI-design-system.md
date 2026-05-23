# Audit UI/UX — Design system Fusionn

Audit du 2026-05-22. Question de départ de Tim : le fond gris du site est-il une bonne idée, ou faut-il passer sur fond blanc avec cartes grises ? Analyse de toutes les pages et de la partie `/compte`.

---

## 1. Verdict sur la question du fond

**Le fond gris clair + cartes blanches est le bon choix. Ne pas inverser.**

C'est le standard des dashboards SaaS (Linear, Stripe, Vercel, Notion). Les cartes blanches se détachent du fond, on obtient hiérarchie et profondeur sans bordures lourdes ni ombres marquées.

**Fond blanc + cartes grises est à éviter.** Deux raisons :
1. Les cartes « s'enfoncent » au lieu de ressortir. On perd la lecture en blocs.
2. Surtout : le contenu de Fusionn (tables, inputs, champs) est déjà blanc. Une carte grise contenant une table blanche posée sur une page blanche, c'est trois niveaux de surface mal séparés. Le blanc doit rester réservé aux surfaces de données.

**Mais le vrai problème est ailleurs.** Le gris actuel `#FAFAF9` est tellement clair (du blanc avec un point de tan) qu'il ne se voit presque pas. Résultat : le site n'est ni franchement blanc, ni un vrai dashboard à cartes qui ressortent. Il est coincé entre les deux. C'est sûrement ça que tu ressens comme « pas net ».

**La correction n'est pas de retirer le gris, c'est d'assumer le pattern** : un gris de page un peu plus présent (tout en restant clair) pour que les cartes blanches ressortent vraiment.

---

## 2. Ce qui va bien

- Un design system existe : variables CSS `--ws-*` dans `src/index.css`. Bonne base.
- Le pattern fond gris / cartes blanches dans le workspace est le bon.
- Le rayon de 12px sur les cartes, la bordure `#E5E7EB`, la couleur de marque `#FF371C` : cohérents quand ils sont utilisés.

---

## 3. Les vrais problèmes (par ordre d'impact)

### P0 — Le champ de recherche du Hero est vert

`HeroInput.tsx` : l'input principal a une bordure `2px solid #244831` (vert forêt) et une ombre teintée vert. La marque Fusionn est orange `#FF371C`. L'élément le plus important et le plus regardé de l'app est dans une couleur qui n'appartient pas à la marque, et qui n'apparaît nulle part ailleurs. Incohérence visuelle majeure.

### P0 — Prolifération de gris quasi identiques

Cinq quasi-blancs se partagent les mêmes rôles sans règle : `#FAFAF9` (page), `#FAFAFA` (item grisé), `#F9FAFB` (hover), `#F8FAFC` (zones détail), `#F3F4F6` (hover). L'œil ne les distingue pas, mais le code et la cohérence en souffrent. Il faut 3 ou 4 surfaces, pas 6.

### P1 — Le gris de page est trop subtil

`#FAFAF9` est à un point du blanc. Les cartes blanches ne ressortent donc pas. C'est la cause directe du ressenti « bof » sur le fond.

### P1 — Tokens dupliqués

- `#FF371C` et `#FE371C` : deux rouges de marque pour le même usage, différence invisible.
- `#212121` et `#1A1A1A` : deux noirs de texte, idem.

### P1 — Typographie trop fine

Corps de texte en Inter **300** (light), titres Poppins **500**. Sur une app de données, du texte light à 13-14px fatigue la lecture et manque d'assise. Standard UI : corps en **400**, titres en **600**.

### P2 — Incohérences de finition

- Bordures : 1px sur les cartes, 2px sur les modales.
- Rayons : 4px, 8px, 12px, 16px, 20px coexistent.
- Paddings de cartes : 14, 16, 20, 24, 32px sans logique.
- `.glass-card` : classe définie, utilisée nulle part. Code mort.

### P2 — App grise vs pages marketing blanches

Blog, Glossaire, Conditions, etc. sont en blanc plein ; l'app (`/compte`) est grise. Ce n'est pas un défaut en soi (marketing aéré vs app dashboard, c'est un split classique), mais ça doit être un choix assumé, pas un hasard.

---

## 4. Recommandations

### Palette de surfaces — à consolider (P0)

| Token | Avant | Après | Usage |
|---|---|---|---|
| `--ws-bg-page` | `#FAFAF9` | `#F4F5F7` | Fond de page / shell app |
| `--ws-bg-card` | `#FFFFFF` | `#FFFFFF` | Cartes, surfaces de données |
| `--ws-bg-subtle` | `#FAFAF9` | `#F4F5F7` | Sidebar (= fond de page) |
| `--ws-bg-hover` | `#F3F4F6` | `#EEF0F2` | Survols, états inactifs |
| `--ws-border` | `#E5E7EB` | `#E5E7EB` | Bordures (inchangé) |

Supprimer `#FAFAFA`, `#F9FAFB`, `#F8FAFC` : tout remapper sur les 4 tokens ci-dessus. `#F4F5F7` est un gris froid, propre, qui fait ressortir les cartes blanches sans être lourd. Si tu tiens au côté chaud, garder une version chaude type `#F6F5F3`, mais un cran plus marqué que `#FAFAF9`.

### Cartes (P1)

Garder le blanc, bordure 1px `#E5E7EB`, rayon 12px. Optionnel : une ombre chuchotée `0 1px 2px rgba(0,0,0,0.04)` pour un soupçon d'élévation. Avec un fond de page enfin visible, même la carte plate fonctionne.

### Couleur de marque (P0)

Une seule : `#FF371C`. Supprimer `#FE371C`. Hover de marque : `#E62E13` (déjà utilisé sur le bouton Relancer).

### Hero (P0)

Bordure de l'input : passer de `#244831` (vert) à `#E5E7EB` au repos, `#FF371C` au focus. Ombre neutre. L'input redevient cohérent avec la marque.

### Typographie (P1)

Corps Inter `300` → `400`. Titres Poppins `500` → `600`. Gain de lisibilité immédiat sur toute l'app.

### Finitions (P2)

- Bordures : 1px partout. Les modales se distinguent par l'ombre, pas par une bordure 2px.
- Rayons : échelle resserrée à 8px (contrôles), 12px (cartes), 16px (modales). Abandonner 4px et 20px.
- Texte : un seul noir, `#1A1A1A`.
- Supprimer `.glass-card`.

---

## 5. Plan d'application

Tout se joue dans `src/index.css` (les variables `--ws-*`) pour 80 % de l'effet : consolider les tokens là, et la majorité des composants suit automatiquement. Restent les valeurs en dur hors variables (le vert du Hero, les `#FAFAFA`/`#F9FAFB`/`#F8FAFC` inline, les poids de police) à corriger composant par composant.

Ordre conseillé : P0 d'abord (Hero + consolidation des gris + marque unique) — fort impact visuel, faible risque. Puis P1 (gris de page plus présent, typo). Puis P2 (finitions).

**Aucun de ces changements ne demande de revoir l'architecture.** C'est de la cohérence et du calibrage, pas une refonte.
