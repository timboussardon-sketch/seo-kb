---
name: revue-presse-bootcamp
description: |
  Brief quotidien SEO/IA pour les participants du bootcamp. Tu scannes les sources de référence du secteur SEO/IA, tu sélectionnes 4 à 6 informations qui ont vraiment compté ces dernières 48h, et tu sors une fiche structurée prête à lire en 5 minutes le matin avec le café.

  Output = matière première d'information. Pas une newsletter, pas un éditorial, pas un post LinkedIn. Le participant lit le brief, sait ce qui s'est passé hier dans le SEO/IA, et décide après ce qu'il en fait (article, post, intervention call client, simple culture métier).

  TOUJOURS utiliser ce skill quand l'utilisateur dit : « revue de presse », « brief SEO/IA », « actus du jour », « qu'est-ce qui s'est passé hier en SEO », « brief quotidien », « news SEO », ou quand le cron / `/schedule` du matin se déclenche.

  Skill prêt à l'usage, rien à remplir. Installation : copier ce fichier dans `~/.claude/skills/revue-presse-bootcamp/SKILL.md` puis lancer `/revue-presse-bootcamp` ou brancher `/schedule`.
---

# Brief quotidien SEO/IA — Bootcamp

Tu produis chaque matin un brief structuré de l'actu SEO/IA des dernières 24 à 48 heures. Format informatif, factuel, scannable. Pas d'opinion, pas de doctrine, pas de CTA. Le lecteur veut savoir ce qui s'est passé hier, pas lire ton avis.

## Les sources à scanner, dans l'ordre

1. **ArXiv** (arxiv.org) — papers LLM, ranking, retrieval, RAG du dernier mois
2. **Médias SEO de référence** : Search Engine Land, Search Engine Journal, Google Search Central Blog (developers.google.com/search/blog)
3. **Substack** :
   - SparkToro de Rand Fishkin
   - iPullRank
   - Marie Haynes
   - Lily Ray
   - Aleyda Solis
   - Growth Memo de Kevin Indig
   - Zyppy Signal de Cyrus Shepard
4. **LinkedIn** : Aleyda Solis, Lily Ray, Glenn Gabe, Kevin Indig, Cyrus Shepard, Olivier Andrieu, Olivier Duffez
5. **Reddit** : r/SEO et r/bigseo, threads à fort engagement
6. **X/Twitter** : Barry Schwartz, Lily Ray, Glenn Gabe, Danny Sullivan, John Mueller, SearchLiaison (Google)
7. **Études quantitatives** : Seer Interactive, Ahrefs, Semrush, BrightEdge, ConvertMate, AirOps, HUMAN Security

Ces sources sont celles d'un consultant senior qui ont été sélectionnées sur 6 ans de pratique. Tu ne les remplaces pas, tu les complètes éventuellement avec une source repérée pendant le scan si elle est sérieuse (institut, paper, communiqué officiel).

## Étape 1, le scan

Lance au moins 12 WebSearch réparties sur les piliers SEO, IA et contenu. Fenêtre 24 à 48 heures, jamais au-delà de 30 jours. Tu vises 8 à 15 candidats bruts.

## Étape 2, la sélection

Tu retiens 4 à 6 infos. Critères :

- **Concret** : un fait, un chiffre, un changement vérifiable. Pas un « tendance », pas un « selon les experts ».
- **Impact** : ça change une décision pour un consultant SEO ou un patron de TPE qui fait du SEO. Pas une statistique décorative.
- **Frais** : daté des dernières 48h en priorité. Si tu remontes à 7 jours, c'est parce que rien de mieux n'est sorti.

Diversifie les angles : un mix algo Google + IA + outils + études quantitatives + jurisprudence/régulation si pertinent. Pas 5 infos sur le même update Google.

**Si aucune info ne coche les critères** → jour creux. Sors la mention « RAS — aucune info significative ces 48h » et stop. Mieux que du remplissage.

## Étape 3, l'approfondissement

Pour chacune des 4-6 infos retenues :

- **Source primaire** : remonte au papier / communiqué officiel / dataset brut via WebFetch. Les articles SEO se recopient en boucle, tu cherches l'origine.
- **Croisement** : au moins une 2e source qui confirme. Contradiction entre 2 sources → la noter, c'est un signal fort.
- **Méthode si étude** : combien d'unités, sur quelle période, avec quel outil.

## Étape 4, la rédaction (format brief)

Tu reproduis exactement cette structure :

```markdown
---
type: brief-seo-ia
date: YYYY-MM-DD
status: lu
---

# Brief SEO/IA — YYYY-MM-DD

## 1. [Titre court de l'info, format affirmation factuelle]

[2 à 3 phrases : le fait, la donnée chiffrée si dispo, ce qui est vérifié par la source primaire. Pas d'opinion.]

> Source primaire : [nom + lien]
> Date : YYYY-MM-DD
> Confidence : Haute / Moyenne / Basse
> Croisement : [2e source si dispo, sinon « source unique »]

---

## 2. [Titre court de l'info 2]

[Idem]

> Source primaire : ...
> Date : ...
> Confidence : ...
> Croisement : ...

---

## 3. [Titre court de l'info 3]

[Idem]

> Source primaire : ...
> Date : ...
> Confidence : ...
> Croisement : ...

---

## 4. [Titre court de l'info 4]

[Idem]

> Source primaire : ...
> Date : ...
> Confidence : ...
> Croisement : ...

[5 et 6 si pertinent — sinon 4 suffit]

---

## Sources écartées (optionnel, 3-5 lignes)

- [Titre] — [raison en 1 ligne : déjà vu, non vérifiable, hors scope]
- [Titre] — [raison]
```

## Étape 5, les vérifications avant sauvegarde

### Anti-hallucination

- Chaque info a une **source primaire avec lien clickable**. Si tu n'as pas trouvé l'origine, tu remplaces le candidat.
- Aucune date inventée. Si la date de publication est imprécise → « daté approximativement [période] » + Confidence Basse.
- Chaque chiffre est sourçable. Pas de « selon une étude récente » sans nom + lien.

### Anti-éditorial

- Pas de « ce que j'en pense », pas de « c'est important parce que ».
- Pas de superlatif vide (« majeur », « révolutionnaire », « historique »).
- Pas de tiret cadratin `—`, pas de wikilink `[[...]]`, pas d'emoji décoratif.
- Pas de CTA, pas de signature.

### Checklist de structure

- [ ] Frontmatter présent avec date et `status: lu`
- [ ] 4 à 6 infos numérotées
- [ ] Chaque info a son bloc source / date / confidence / croisement
- [ ] Aucune info non sourcée
- [ ] Mix d'angles (pas 5 infos sur le même sujet)

Si une vérification échoue → reprendre avant de sauvegarder.

## Étape 6, la sauvegarde

Récupère la date du jour avec `date +%Y-%m-%d`.

Chemin par défaut : `raw/revue-de-presse/YYYY-MM-DD-brief-seo-ia.md` dans le repo où tu lances le skill.

Si un fichier existe déjà pour ce jour → ajouter le suffixe `-bis`.

Termine ta réponse par une ligne : `Brief du [date] · [nombre d'infos retenues] · [piliers couverts]`.

## Notes finales

- **Jour creux assumé** : « RAS » vaut mieux qu'un brief faible.
- **Contradictions** : 2 sources se contredisent → mentionne explicitement.
- **Format stable** : ne pas improviser une nouvelle structure. Les participants s'habituent à ce format en 3 jours, autant être prévisible.

---

## ANNEXE — Brancher `/schedule` (cron remote)

Une fois le skill installé sous `~/.claude/skills/revue-presse-bootcamp/SKILL.md` :

1. Dans Claude Code (depuis le repo où tu veux que les briefs s'archivent), tape `/schedule`
2. Crée une routine :
   - **Cron** : `0 7 * * 1-5` (lundi-vendredi à 7h, avant l'ouverture machine)
   - **Repo** : ton vault / repo de travail
   - **Prompt** : `/revue-presse-bootcamp`
3. Active

La routine tourne sur l'infra Anthropic, MacBook fermé, commit auto dans le repo si configuré sous Git. Tu démarres ta journée avec le brief déjà sauvegardé, lecture en 5 minutes.

**Variante launchd local** : modèle dans `seo-kb/.claude/bin/run-revue-presse.sh` (à adapter, voir bootcamp).
