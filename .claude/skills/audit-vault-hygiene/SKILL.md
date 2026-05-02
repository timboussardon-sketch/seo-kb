---
name: audit-vault-hygiene
description: |
  Audit hebdomadaire de l'hygiène du vault Obsidian seo-kb. Détecte les wikilinks cassés, les fichiers orphelins (sans backlink), les slugs dupliqués, les frontmatter invalides. Produit un rapport markdown actionnable dans wiki/audit/.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit du vault", "nettoyage vault", "liens cassés", "fichiers orphelins", "hygiène Obsidian", ou quand le workflow GH Actions audit-vault.yml se déclenche.
---

# Audit Vault Hygiene — Nettoyage hebdomadaire

Tu produis un rapport d'audit hygiène pour le vault Obsidian de Tim (`/Users/timothee/Documents/seo-kb/` en local, working directory du runner en GH Actions).

## OBJECTIF

Identifier la dette structurelle accumulée. Pas de réparation automatique : seulement un rapport actionnable que Tim peut traiter.

## PÉRIMÈTRE DU SCAN

Scan tout le vault sauf :
- `.git/`, `.obsidian/`, `.obsidian.broken/`, `.claude/`, `.github/`, `node_modules/`
- `_archive/` (legacy déjà rangé)
- `mockups/` (drafts en cours)

## ÉTAPE 1 — INVENTAIRE

```bash
# Liste de tous les fichiers .md utiles
fd -e md -E '.git' -E '.obsidian*' -E '.claude' -E '.github' -E '_archive' -E 'mockups' -E 'node_modules' . > /tmp/vault-files.txt 2>/dev/null \
  || find . -name "*.md" -not -path "./.git/*" -not -path "./.obsidian*/*" -not -path "./.claude/*" -not -path "./.github/*" -not -path "*/_archive/*" -not -path "./mockups/*" -not -path "./node_modules/*" > /tmp/vault-files.txt

wc -l /tmp/vault-files.txt
```

## ÉTAPE 2 — WIKILINKS CASSÉS

Extraire tous les wikilinks `[[slug]]` ou `[[slug|alias]]` du vault et vérifier que la cible existe.

```bash
# Extrait chaque wikilink avec son fichier source
while IFS= read -r f; do
  grep -oE '\[\[[^]]+\]\]' "$f" 2>/dev/null | while read link; do
    # Strip [[, ]], et ce qui suit | (alias) ou # (heading) ou ^ (block ref)
    target=$(echo "$link" | sed -E 's/^\[\[//; s/\]\]$//; s/\|.*//; s/#.*//; s/\^.*//')
    echo -e "$f\t$target"
  done
done < /tmp/vault-files.txt > /tmp/all-wikilinks.tsv

wc -l /tmp/all-wikilinks.tsv
```

Pour chaque target unique, vérifier qu'un fichier `<target>.md` existe quelque part dans le vault. Compose la liste des cassés :

```bash
# Pour chaque target unique
cut -f2 /tmp/all-wikilinks.tsv | sort -u > /tmp/unique-targets.txt

# Liste tous les basenames du vault (sans extension)
while IFS= read -r f; do
  basename "$f" .md
done < /tmp/vault-files.txt | sort -u > /tmp/vault-basenames.txt

# Targets qui n'ont pas de fichier correspondant
comm -23 /tmp/unique-targets.txt /tmp/vault-basenames.txt > /tmp/broken-targets.txt
wc -l /tmp/broken-targets.txt
```

Pour chaque cible cassée, lister les fichiers source qui la référencent :

```bash
while IFS= read -r target; do
  echo "## $target"
  grep -F "	$target" /tmp/all-wikilinks.tsv | cut -f1 | sort -u | sed 's/^/  - /'
  echo ""
done < /tmp/broken-targets.txt > /tmp/broken-report.md
```

**Filtre cosmétique** : exclus les targets qui sont en réalité des concepts cités à venir (Tim utilise parfois `[[concept-a-creer]]` comme placeholder). Si plus de 80 fichiers cassés, garde les 50 référencés par le plus de sources (= les plus prioritaires à créer ou réparer).

## ÉTAPE 3 — FICHIERS ORPHELINS (sans backlink)

Un fichier orphelin = aucun autre fichier du vault ne le référence via wikilink ou lien markdown.

```bash
# Pour chaque fichier du vault, compte combien de fichiers le référencent
while IFS= read -r f; do
  base=$(basename "$f" .md)
  # Cherche les références : [[base]], [[base|...]], [[base#...]], (base.md), [...](base)
  count=$(grep -lE "\[\[$base(\||#|\^|\])" /tmp/vault-files.txt 2>/dev/null | grep -v "^$f$" | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "$f"
  fi
done < /tmp/vault-files.txt > /tmp/orphans.txt
```

Sont exclus de la liste des orphelins (faux positifs attendus) :
- `wiki/index.md`, `wiki/log.md`, `MEMORY.md`, `CLAUDE.md`, `AGENTS.md`, `README.md`
- Fichiers dans `wiki/posts-linkedin/` (posts standalone)
- Fichiers dans `raw/revue-de-presse/` (chacun est autonome)
- Fichiers dans `raw/articles/` (drafts en cours)
- Fichiers dans `raw/agents/` et `raw/data/` (notes terrain)

## ÉTAPE 4 — SLUGS DUPLIQUÉS

Deux fichiers avec le même basename dans 2 dossiers différents = collision de wikilinks (Obsidian prend le premier trouvé, comportement non-déterministe).

```bash
while IFS= read -r f; do
  basename "$f" .md
done < /tmp/vault-files.txt | sort | uniq -d > /tmp/duplicated-slugs.txt

while IFS= read -r slug; do
  echo "## $slug"
  grep "/$slug.md$" /tmp/vault-files.txt | sed 's/^/  - /'
  echo ""
done < /tmp/duplicated-slugs.txt > /tmp/duplicates-report.md
```

## ÉTAPE 5 — FRONTMATTER CASSÉ

Vérifier les fichiers de `wiki/concepts/`, `wiki/entities/`, `wiki/sources/`, `wiki/queries/`, `wiki/briefs/` :
- Frontmatter présent (commence par `---` à la ligne 1)
- YAML parseable (indentation cohérente, pas de tab, pas de string non quotée avec `:`)
- Champs requis selon le type :
  - `wiki/concepts/`, `wiki/entities/` : `aliases`, `tags`, `created`
  - `wiki/sources/` : `source_type`, `created`
  - `wiki/briefs/` : `query`, `created`

```bash
for dir in wiki/concepts wiki/entities wiki/sources wiki/queries wiki/briefs; do
  find "$dir" -name "*.md" 2>/dev/null | while read f; do
    head -1 "$f" | grep -q "^---$" || echo "MISSING_FM	$f"
  done
done > /tmp/frontmatter-issues.txt
```

(Pour les checks de champs requis, fais-les en lisant les frontmatter avec Read et en parsant le YAML manuellement — n'invente pas de validations qui ne sont pas explicitement définies ci-dessus.)

## ÉTAPE 6 — RÉDACTION DU RAPPORT

Date du jour : `date -u +%Y-%m-%d`

Écris le rapport dans `wiki/audit/YYYY-MM-DD-audit.md` :

```markdown
---
type: audit
title: Audit vault — YYYY-MM-DD
date: YYYY-MM-DD
tags: [audit, hygiene, vault]
status: report
---

# Audit vault — YYYY-MM-DD

> Snapshot hebdo de l'hygiène du vault. Pas d'action automatique : à toi de trier.
> Total fichiers scannés : N — Wikilinks scannés : M

## 🚨 Wikilinks cassés (top N par référencement)

### `[[slug-cassé-1]]` — référencé par K fichiers
- chemin/fichier-1.md
- chemin/fichier-2.md
…

(répète pour les top N — max 50)

**Total cassés : N — % du total : X%**

## 👻 Fichiers orphelins (sans backlink)

Fichiers qui n'ont aucun lien entrant. Soit à connecter au vault, soit à archiver.

- chemin/fichier-orphelin-1.md
- chemin/fichier-orphelin-2.md
…

**Total orphelins : N**

## 🪞 Slugs dupliqués

Collision : 2+ fichiers avec même nom → wikilinks ambigus.

### `slug-dupliqué-1`
- chemin/v1.md
- chemin/v2.md

(répète…)

**Total collisions : N**

## 📋 Frontmatter cassé ou manquant

- chemin/fichier.md — `MISSING_FM` (frontmatter absent)
- chemin/fichier.md — champ `aliases` manquant
…

**Total problèmes frontmatter : N**

## 📊 Synthèse

- Santé globale du vault : [bonne / moyenne / dégradée] selon ratio cassés/total
- Priorité n°1 : [le problème le plus urgent à traiter]
- Évolution vs semaine précédente : [si rapport précédent existe, comparer les chiffres]

---

*Audit généré automatiquement par le workflow `audit-vault.yml`. Pour traiter, ouvre les liens et fixe à la main, ou supprime les rapports anciens dans `wiki/audit/` une fois traités.*
```

## ÉTAPE 7 — COMPARAISON AVEC RAPPORT PRÉCÉDENT

Si un rapport `wiki/audit/YYYY-MM-DD-audit.md` plus récent que J-14 existe, lis-le et compare les totaux. Mets l'évolution dans la section "Synthèse" :

```
- Wikilinks cassés : 47 (+5 depuis dernier audit)
- Orphelins : 23 (-2)
- Collisions : 1 (=)
- Frontmatter : 8 (-3)
```

## ÉTAPE 8 — RÉSUMÉ EN 1 LIGNE

Termine ta réponse par :

```
Audit du [date] : N cassés / N orphelins / N collisions / N frontmatter — santé [globale]
```

## CONTRAINTES

- **Aucune réparation automatique**. Tu produis un rapport, pas plus.
- **Si un compteur dépasse 200**, tronque la liste à 50 et précise "+N autres non listés".
- **Pas d'invention** : si un script bash échoue, mentionne-le dans le rapport au lieu de combler avec des estimations.
- **Performance** : si le vault dépasse 2000 fichiers, considère ne scanner que les répertoires les plus volumineux (`raw/`, `wiki/`).
