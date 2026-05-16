---
type: register
title: Setup — pull GSC automatique (service account)
aliases: [setup-gsc, gsc-service-account]
tags: [meta, gsc, setup, preuves, automation]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: stable
---

# Setup — pull GSC automatique

> Le watcher CSV (`gsc-watcher`) marche déjà sans rien : dépose un export GSC manuel dans `raw/data/exports-gsc/` et les fiches preuves se remplissent. Ce document concerne l'étage du dessus : le pull API autonome via service account, pour que la boucle se nourrisse seule comme les autres.
>
> Tant que le credential n'est pas en place, `gsc-fetch.py` sort proprement en code 0 et la boucle reste en mode dépôt manuel. Aucune erreur, aucune dette.

## Ce que tu fais une fois (≈10 min, côté Google)

1. Console Google Cloud, projet existant ou nouveau. Active l'API **Google Search Console API**.
2. IAM → comptes de service → créer un compte de service (ex. `seo-kb-gsc-reader`). Pas besoin de rôle projet.
3. Sur ce compte de service : créer une clé, type **JSON**, télécharger.
4. Dans **Search Console**, propriété `organikk.co` → Paramètres → Utilisateurs et autorisations → ajouter l'email du service account (`...@...iam.gserviceaccount.com`) en accès **Restreint** (lecture suffit).
5. Dépose le JSON sur la machine, hors du repo :

```
mkdir -p ~/.config/seo-kb
mv ~/Downloads/<le-fichier>.json ~/.config/seo-kb/gsc-service-account.json
chmod 600 ~/.config/seo-kb/gsc-service-account.json
```

## Vérifier

```
~/.local/bin/seo-kb/.venv/bin/python ~/.local/bin/seo-kb/gsc-fetch.py
```

Sortie attendue : `OK — N lignes ... écrites dans raw/data/exports-gsc/gsc-auto-YYYY-MM-DD.csv`. Si erreur 403, le service account n'est pas (encore) utilisateur de la propriété. Si la propriété est de type préfixe d'URL et non domaine :

```
export GSC_SITE_URL="https://organikk.co/"
```

(à mettre dans le plist `com.timboussardon.gsc-pull` si besoin permanent).

## Ce qui tourne ensuite tout seul

Le 1er de chaque mois à 07:00, `com.timboussardon.gsc-pull` : pull API → CSV dans `raw/data/exports-gsc/` → skill `gsc-watcher` → fiches `wiki/preuves/` remplies → hypothèses de [[hypotheses]] mises à jour. La validation mensuelle des hypothèses (08:30 le même jour) tourne donc sur de la data fraîche.

## Sécurité

Le JSON vit dans `~/.config/seo-kb/`, jamais dans le repo. Un garde-fou `.gitignore` rejette tout `*service-account*.json` au cas où. Ne jamais committer ce fichier.

Pages liées : [[preuves/index]] · [[hypotheses]] · [[ingest-backlog]]
