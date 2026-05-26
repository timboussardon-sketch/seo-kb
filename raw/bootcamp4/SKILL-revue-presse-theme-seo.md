---
name: revue-presse-theme-seo
description: |
  Brief quotidien SEO **ciblé sur une sous-thématique précise** : mots-clés, micro-intentions, contenu SEO, audit, maillage interne, données structurées, GEO/AEO, E-E-A-T, local SEO, programmatic SEO. Le participant choisit la thématique au lancement (paramètre), et le skill sort 3 à 5 infos qui ne traitent QUE de cette sous-thématique.

  Différent du skill `revue-presse-bootcamp` qui couvre tout le SEO/IA en généraliste. Ici, on creuse une sous-discipline à la fois. Utile pour monter en expertise sur un pilier, préparer un call client sur un sujet précis, ou alimenter un cluster de contenu.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : « brief SEO sur [thème] », « actus mots-clés du jour », « news micro-intentions », « revue contenu SEO », « ce qui se dit sur l'audit cette semaine », « brief link building », « brief E-E-A-T », « brief programmatic SEO ».

  Skill prêt à l'usage, rien à remplir. Installation : copier dans `~/.claude/skills/revue-presse-theme-seo/SKILL.md` puis lancer `/revue-presse-theme-seo <thème>` ou brancher `/schedule`.
---

# Brief SEO thématique

Tu produis un brief structuré centré sur **UNE seule sous-discipline SEO**. 3 à 5 infos, toutes sur le même angle, factuelles, sourcées.

## Thématique à passer en paramètre

Au lancement, l'utilisateur précise la thématique. Si absente, **demande-la** avec la liste suivante :

| Slug | Thématique | Ce qu'on couvre |
|---|---|---|
| `mots-cles` | Recherche de mots-clés | Outils, méthodologies, intention de recherche, volumes, longue traîne, clustering, mots-clés business |
| `micro-intentions` | Micro-intentions & PAA | Intent matching, Fully Meets, Quality Raters Guidelines, PAA optimization, intention informationnelle vs transactionnelle |
| `contenu` | Contenu SEO | Rédaction IA, briefs, passage ranking, FAQ, structure Hn, anti-IA writing, Information Gain |
| `audit` | Audit SEO | Indexation, structure technique, Core Web Vitals, crawl, robots.txt, sitemap, audit Hn |
| `maillage` | Maillage interne & link building | Architecture en piliers, ancres, pages orphelines, backlinks, autorité, anchor text |
| `donnees-structurees` | Données structurées / Schema.org | JSON-LD, FAQPage, HowTo, BreadcrumbList, knowledge graph, rich snippets |
| `geo-aeo` | GEO & AEO (IA générative) | SGE, AI Overview, SearchGPT, Perplexity citations, LLM SEO, Surprise Score |
| `e-e-a-t` | E-E-A-T & Quality Raters | Expérience, expertise, autorité, fiabilité, signaux d'auteur, signaux d'entité |
| `local-seo` | SEO local | Google Business Profile, Local Pack, NAP, citations locales, schema LocalBusiness |
| `pseo` | Programmatic SEO | Templates + variables, scalabilité, thin content, canonical, longue traîne programmatique |

Le participant peut aussi taper une thématique libre. Dans ce cas, tu cadres en 1 phrase ce qui est dans le scope et ce qui en sort, et tu valides avec lui avant de lancer le scan.

## Les sources à scanner (mêmes que `revue-presse-bootcamp`)

1. **ArXiv** (arxiv.org) — papers LLM, ranking, retrieval, RAG du dernier mois
2. **Médias SEO de référence** : Search Engine Land, Search Engine Journal, Google Search Central Blog
3. **Substack** : SparkToro de Rand Fishkin · iPullRank · Marie Haynes · Lily Ray · Aleyda Solis · Growth Memo de Kevin Indig · Zyppy Signal de Cyrus Shepard
4. **LinkedIn** : Aleyda Solis · Lily Ray · Glenn Gabe · Kevin Indig · Cyrus Shepard · Olivier Andrieu · Olivier Duffez
5. **Reddit** : r/SEO et r/bigseo, threads à fort engagement
6. **X/Twitter** : Barry Schwartz · Lily Ray · Glenn Gabe · Danny Sullivan · John Mueller · SearchLiaison (Google)
7. **Études quantitatives** : Seer Interactive · Ahrefs · Semrush · BrightEdge · ConvertMate · AirOps · HUMAN Security

**Spécifique à la thématique** : selon le slug choisi, privilégier les sources qui produisent du fond sur cette sous-discipline (ex. ArXiv prime sur la thématique `geo-aeo`, Search Engine Land prime sur `audit`, BrightEdge prime sur `pseo`).

## Étape 1, le scan ciblé

Lance 10 à 14 WebSearch **toutes orientées sur la thématique choisie**. Fenêtre 24 à 72 heures (un peu plus large que le brief généraliste, parce que les sous-thématiques ont moins de bruit quotidien). Jamais au-delà de 30 jours.

Construire les requêtes avec :
- Le vocabulaire de la thématique (ex. pour `mots-cles` : keyword research, search intent, long tail, keyword clustering, keyword difficulty)
- Le nom des outils dominants du sous-thème (ex. pour `audit` : Screaming Frog, Sitebulb, Lighthouse)
- Les acronymes de référence (PAA, EEAT, SGE, etc.)

## Étape 2, la sélection

Tu retiens 3 à 5 infos. Critères :

- **Dans le scope** : si l'info déborde sur une autre sous-discipline, tu l'écartes même si elle est forte. Pureté thématique.
- **Concret** : un fait, un chiffre, un changement vérifiable. Pas de « tendance » ou « selon les experts ».
- **Impact** : ça change une décision pour un consultant qui pratique cette sous-discipline aujourd'hui.
- **Frais** : 48h en priorité. Jusqu'à 30 jours pour un paper fondateur ou un changement d'algo lent.

Diversifie à l'intérieur de la thématique : un mix recherche académique + pratique terrain + changement algo si pertinent. Pas 5 infos sur le même outil.

**Si moins de 3 infos passent le filtre** → jour creux pour cette thématique. Sors la mention « RAS sur [thème] cette semaine » et stop. Pas de remplissage.

## Étape 3, l'approfondissement

Pour chaque info retenue :

- **Source primaire** : remonter au papier / communiqué / dataset via WebFetch.
- **Croisement** : au moins une 2e source qui confirme.
- **Méthode si étude** : échantillon, période, outil.
- **Connexion à la pratique** : 1 phrase qui dit comment un consultant peut s'en servir dans sa semaine.

## Étape 4, la rédaction (format brief thématique)

```markdown
---
type: brief-seo-theme
theme: <slug-thématique>
date: YYYY-MM-DD
status: lu
---

# Brief SEO — <thématique> — YYYY-MM-DD

## 1. [Titre court, format affirmation factuelle]

[2 à 3 phrases : le fait, la donnée, ce qui est vérifié par la source primaire. Pas d'opinion.]

> Source primaire : [nom + lien]
> Date : YYYY-MM-DD
> Confidence : Haute / Moyenne / Basse
> Croisement : [2e source si dispo, sinon « source unique »]
> Utilisation pratique : [1 phrase — comment un consultant s'en sert cette semaine]

---

## 2. [Titre court de l'info 2]

[Idem — toujours sur la même thématique]

> Source primaire : ...
> Date : ...
> Confidence : ...
> Croisement : ...
> Utilisation pratique : ...

---

## 3. [Titre court de l'info 3]

[Idem]

> Source primaire : ...
> Date : ...
> Confidence : ...
> Croisement : ...
> Utilisation pratique : ...

[4 et 5 si pertinent — minimum 3]

---

## Sources écartées (hors scope ou non vérifiables)

- [Titre] — [raison : hors scope <thème>, déjà vu, non vérifiable]
- [Titre] — [raison]
```

## Étape 5, vérifications avant sauvegarde

### Anti-dérive thématique

- Aucune info ne déborde sur une autre sous-discipline SEO. Si une info touche 2 thématiques, garde-la uniquement si l'angle dominant est celui choisi.
- Le titre du brief inclut le slug thématique.

### Anti-hallucination

- Source primaire avec lien clickable obligatoire.
- Aucune date inventée. Date imprécise → Confidence Basse + mention.
- Chaque chiffre est sourçable.

### Anti-éditorial

- Pas de « ce que j'en pense », pas de superlatif.
- Pas de tiret cadratin, pas de wikilink, pas d'emoji décoratif.
- Pas de CTA, pas de signature.

### Checklist de structure

- [ ] Frontmatter avec `theme: <slug>` et `status: lu`
- [ ] 3 à 5 infos numérotées, toutes dans le scope thématique
- [ ] Chaque info a son bloc source / date / confidence / croisement / utilisation pratique
- [ ] Aucune info hors thème
- [ ] Sources écartées listées (3-5 max)

## Étape 6, la sauvegarde

`date +%Y-%m-%d` puis sauvegarder dans :

`raw/revue-de-presse/YYYY-MM-DD-brief-<slug-thème>.md`

Si un fichier existe déjà pour ce jour + ce thème → ajouter le suffixe `-bis`.

Termine par : `Brief <thème> du [date] · [nb d'infos] · [angle dominant]`.

## Notes finales

- **Jour creux assumé** : RAS thématique vaut mieux qu'un brief tiré par les cheveux.
- **Rotation hebdo recommandée** : lundi `mots-cles`, mardi `contenu`, mercredi `audit`, jeudi `geo-aeo`, vendredi `maillage`. Permet de tourner sur toutes les briques en 1 semaine sans surcharge cognitive.
- **Mix avec `revue-presse-bootcamp`** : le brief généraliste reste utile pour ne pas rater une info hors thématique du jour. Les 2 skills sont complémentaires.

---

## ANNEXE — Brancher `/schedule` (cron remote)

### Setup mono-thème (1 routine = 1 thème fixe)

1. `/schedule`
2. Routine :
   - **Cron** : `0 7 * * 1-5` (lundi-vendredi à 7h)
   - **Repo** : ton vault de travail
   - **Prompt** : `/revue-presse-theme-seo mots-cles` (remplacer par le thème voulu)
3. Active

### Setup rotation 5 thèmes (1 par jour ouvré)

5 routines `/schedule`, une par jour :

| Cron | Thème |
|---|---|
| `0 7 * * 1` (lundi 7h) | `mots-cles` |
| `0 7 * * 2` (mardi 7h) | `contenu` |
| `0 7 * * 3` (mercredi 7h) | `audit` |
| `0 7 * * 4` (jeudi 7h) | `geo-aeo` |
| `0 7 * * 5` (vendredi 7h) | `maillage` |

Tous les briefs s'archivent dans le même dossier, indexables par le nom de fichier (`brief-<slug>.md`).

### Variante launchd local

Modèle de script dans `seo-kb/.claude/bin/run-revue-presse.sh` (à adapter, voir bundle bootcamp).
