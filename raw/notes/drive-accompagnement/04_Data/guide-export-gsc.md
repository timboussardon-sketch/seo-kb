# Guide — Export Google Search Console

> La GSC est la seule source de vérité. Voici comment extraire les bonnes données.

---

## Export de base — Performances

### Où
Google Search Console → Performances → Résultats de recherche

### Paramètres
- **Période** : 3 derniers mois (par défaut) ou personnalisée
- **Type de recherche** : Web
- **Cocher** : Clics, Impressions, CTR moyen, Position moyenne

### Dimensions à exporter

**Export 1 — Par requêtes**
- Onglet "Requêtes"
- Exporter en CSV
- Nommer : `gsc-requetes-[date].csv`

**Export 2 — Par pages**
- Onglet "Pages"
- Exporter en CSV
- Nommer : `gsc-pages-[date].csv`

**Export 3 — Requêtes × Pages** (le plus utile)
- Onglet "Requêtes" → Cliquer sur une page → voir les requêtes associées
- Ou utiliser l'API GSC pour le croisement complet
- Nommer : `gsc-requetes-pages-[date].csv`

---

## Exports pour les skills

### Pour le skill Quick Win
- Export requêtes 3 derniers mois
- Filtrer : position > 3, impressions > 50

### Pour le skill Cannibalisation
- Export requêtes × pages
- Identifier les requêtes qui apparaissent sur plusieurs URLs

### Pour le skill Maillage Interne
- Export pages (toutes)
- Export requêtes par page

### Pour le skill Mots-clés Décisionnels
- Export requêtes 3 derniers mois
- Pas de filtre — on laisse le skill analyser

---

## Fréquence recommandée

| Export | Fréquence |
|--------|-----------|
| Requêtes | Mensuel |
| Pages | Mensuel |
| Requêtes × Pages | Mensuel |
| Avant chaque brief | Ponctuel (page ciblée) |

---

## Stockage

Tous les exports dans : `04_Data/exports-gsc/`
Format de nommage : `gsc-[type]-[AAAA-MM].csv`

---

## Rappel
- Semrush, Ahrefs = estimations. La GSC = données réelles.
- Le volume n'est pas un signal. Le delta impressions/clics l'est.
