---
name: revue-presse-{{SLUG_CLIENT}}
description: |
  Ce skill génère chaque jour 1 chiffre / étude / fait sourcé pour {{NOM_CLIENT}} sur sa thématique « {{THEME_COURT}} ». Output = matière SEO brute, prête à injecter dans les pages du client (intro, FAQ, preuve atomique). PAS une newsletter, PAS un digest, PAS un post LinkedIn — c'est de la donnée datée et sourcée.

  Pipeline en 5 étapes : scan multi-sources sectorielles → sélection du chiffre du jour → approfondissement (source primaire + croisement) → rédaction format SEO brut → vérifications anti-hallucination.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : « revue de presse {{NOM_CLIENT}} », « chiffre du jour {{THEME_COURT}} », « data fraîche pour {{NOM_CLIENT}} », « veille {{THEME_COURT}} », ou quand le cron / `/schedule` du jour se déclenche.

  Dérivé du skill `revue-presse-quotidienne` (newsletter Algorithme de Tim). Ici on retire le format digest, on retire la doctrine Tim, on retire le CTA newsletter. On garde la rigueur de sourcing.
---

# Revue de presse — {{NOM_CLIENT}}

> ⚠️ **Avant d'installer ce skill** : remplis TOUS les blocs `{{...}}` ci-dessous avec les valeurs du client. Sans ça le skill produira de la news SEO générique inutile.
>
> Une fois rempli, sauvegarde ce fichier sous `~/.claude/skills/revue-presse-{{SLUG_CLIENT}}/SKILL.md` (créer le dossier au préalable).
>
> 1 client = 1 dossier de skill. Tu peux avoir `revue-presse-caroline-mutuelle/`, `revue-presse-franck-immobilier/`, etc., qui tournent en parallèle, chacun sur son cron `/schedule`.

---

## Ton rôle

Tu produis chaque matin **un chiffre exploitable** sur la niche « {{THEME_COURT}} » de {{NOM_CLIENT}}. Tu écartes le bruit, tu gardes ce qui change une décision pour les visiteurs des pages du client, et tu sors la donnée brute, datée, sourcée.

L'audience finale (les visiteurs des pages du client) : **{{AUDIENCE_VISITEURS}}**.
Exemple : « Dirigeants de TPE 5-50 salariés cherchant à équiper leur entreprise en mutuelle santé. »

## Le contexte du client

**Thématique précise** (2 lignes) :
{{THEME_DETAILLE}}

**Position éditoriale défendue par {{NOM_CLIENT}}** (sa doctrine, ce qu'il répète, ce qu'il a vu venir) :
{{DOCTRINE_CLIENT}}
Exemple : « Le client défend que les TPE sont sous-équipées et que les mutuelles standard ne couvrent pas leurs vrais besoins (santé mentale, longue durée). Toute statistique qui confirme ou contredit cette position est forte. »

**Pages à alimenter** (URLs où la donnée du jour peut s'intégrer) :
- {{URL_PAGE_1}}
- {{URL_PAGE_2}}
- {{URL_PAGE_3}}

## Les règles obligatoires

### Règle 1, connexion à la doctrine

Le chiffre du jour doit confirmer ou contredire la position défendue par {{NOM_CLIENT}} (cf. bloc `{{DOCTRINE_CLIENT}}` ci-dessus). Un chiffre orphelin (sans connexion à la doctrine) est écarté, même s'il est solide.

### Règle 2, ton de voix client (obligatoire pour la formulation prête à coller)

La fiche elle-même est de la matière brute (factuelle, neutre). Mais le bloc « **Formulation prête à coller** » va atterrir sur une page du client — il doit donc sonner comme le client, pas comme toi, pas comme un copywriter générique.

Avant de rédiger ce bloc, charge le fichier de voix du client : **{{VOIX_CLIENT_PATH}}**

Ce fichier contient les règles de voix du client : tutoiement / vouvoiement, vocabulaire interdit, formules signature, niveau de technicité, ton (chaleureux / institutionnel / cash / pédagogique). Il a été co-rédigé avec le client lors d'un call de 30 min (voir annexe « Préparer le fichier voix client »).

Si **{{VOIX_CLIENT_PATH}}** n'existe pas → arrêter le run et demander explicitement à l'utilisateur de le créer. Ne pas inventer la voix. Ne pas tomber dans le ton générique B2B ChatGPT.

### Règle 3, aucun éditorial dans le reste de la fiche

En dehors de la « Formulation prête à coller », tu ne rédiges pas un post LinkedIn ni une newsletter. Pas de CTA, pas de signature, pas d'aparté personnel, pas de hook. Le client (ou son consultant SEO) décide ensuite quoi en faire.

### Règle 4, aucun chiffre sans source primaire

Si tu ne peux pas remonter à l'étude / au dataset / au communiqué d'origine, tu écartes le candidat. Une citation de citation n'est pas une source.

## Étape 1, le scan des sources

Lance 8 à 12 WebSearch sur la thématique, fenêtre 48h (jamais > 30 jours).

**Sources prioritaires pour {{NOM_CLIENT}}, dans l'ordre** :

1. {{SOURCE_1}}
2. {{SOURCE_2}}
3. {{SOURCE_3}}
4. {{SOURCE_4}}
5. {{SOURCE_5}}

Exemple de remplissage pour une mutuelle TPE :
1. *ameli.fr / DREES (institut stats santé)*
2. *Argus de l'assurance (média sectoriel)*
3. *Fédération nationale de la mutualité française*
4. *INSEE — études entreprises de moins de 50 salariés*
5. *LinkedIn des 3-5 figures du secteur (DG mutuelles, courtiers spécialisés)*

Compléter si pertinent :
- Études quantitatives sectorielles (organismes professionnels, instituts publics)
- LinkedIn des figures de la niche
- ArXiv uniquement si pertinent (rare en B2B niche, garder pour les sujets tech)

## Étape 2, la sélection du chiffre du jour

Pour chaque candidat remonté en Phase 1, vérifie 3 critères :

| Critère | Question |
|---|---|
| **Décision** | Est-ce qu'il y a un chiffre ou un fait qui change une décision pour le visiteur des pages {{NOM_CLIENT}} ? |
| **Doctrine** | Le chiffre confirme ou contredit la position de {{NOM_CLIENT}} ? (cf. `{{DOCTRINE_CLIENT}}`) |
| **Vérifiable** | Source primaire accessible, méthodologie claire (échantillon, période, outil) ? |

Sélectionne le candidat qui coche les 3. Égalité → chiffre le plus précis.

**Si AUCUN candidat ne coche les 3 cases → jour creux.** Sortir une fiche « RAS — pas de signal exploitable aujourd'hui » et stop. Mieux ne rien sortir qu'une fiche de remplissage qui pollue les pages SEO du client.

## Étape 3, l'approfondissement

Pour le chiffre retenu :

- **Source primaire** : remonter au papier / étude / dataset brut via WebFetch. Vérifier méthodologie (combien d'unités analysées, sur quelle période, avec quel outil).
- **Croisement** : trouver au moins une 2e source qui confirme. Si tu trouves une contradiction entre deux sources, **garde-la**, c'est souvent là que vit l'angle d'injection.
- **Date** : si la source publie > 7 jours mais < 30, OK uniquement si rien de plus frais. Au-delà → écarter ou marquer `[ANCIEN — réf de fond]`.

## Étape 4, la rédaction (format SEO brut)

Tu reproduis exactement cette structure :

```markdown
---
type: revue-presse-client
client: {{NOM_CLIENT}}
date: YYYY-MM-DD
theme: {{THEME_COURT}}
status: matière-seo
---

# Revue {{NOM_CLIENT}} — YYYY-MM-DD

## Chiffre du jour

**[Le chiffre + le sujet en une phrase, format affirmation]**

> Source primaire : [nom + lien]
> Date publication : YYYY-MM-DD
> Méthodologie : [1 ligne — échantillon / période / outil]
> Confidence Score : Haute / Moyenne / Basse

### Contexte (3 lignes max)

[Qui a produit la donnée, sur quoi, pour qui. Aucun jargon.]

### Connexion à la doctrine {{NOM_CLIENT}}

[1-2 phrases : ce chiffre confirme / contredit la position « {{DOCTRINE_CLIENT}} » de la manière suivante…]

### Angle d'injection SEO

- **Page cible** : [URL parmi `{{URL_PAGE_1}}`, `{{URL_PAGE_2}}`, `{{URL_PAGE_3}}`]
- **Position recommandée** : intro / FAQ / preuve atomique en milieu d'article
- **Formulation prête à coller** : « [phrase courte avec le chiffre + source courte entre parenthèses] »

### Verbatim sourcé (1 à 3 phrases si dispo)

> « [citation textuelle de la source primaire] » — [auteur, source]

---

## Candidats écartés (3-5)

- [Titre 1] — [raison en 1 ligne]
- [Titre 2] — [raison en 1 ligne]
- [Titre 3] — [raison en 1 ligne]
```

## Étape 5, les vérifications avant sauvegarde

### Anti-hallucination

- Aucun chiffre sans source primaire dans le bloc citation (lien clickable obligatoire).
- Aucune date > 30 jours sauf paper fondateur explicitement marqué `[ANCIEN]`.
- 2 sources minimum croisées, sinon Confidence Basse explicite.

### Anti-superlatifs

Bannis dans toute la fiche : « majeur », « révolutionnaire », « historique », « sans précédent », « crucial ». Remplacer par le chiffre lui-même.

### Anti-éditorial

- Pas de CTA, pas de signature, pas de « ce que j'en pense ».
- Pas de digest (un seul chiffre, pas trois). Les candidats écartés vont en bas, pas en sujets co-vedettes.
- Pas de mise en forme newsletter (pas de « 🍿 », pas d'emoji décoratif).

### Checklist de structure

- [ ] Frontmatter présent avec `status: matière-seo`
- [ ] 1 chiffre du jour, 1 source primaire clickable
- [ ] Bloc « Connexion à la doctrine » rempli (pas vide)
- [ ] Page cible spécifiée parmi les 3 URLs du client
- [ ] Formulation prête à coller insérable telle quelle
- [ ] Candidats écartés listés (3-5)
- [ ] Aucun wikilink `[[...]]`, aucun tiret cadratin `—`, aucun emoji décoratif

Si une vérification échoue → reprends le passage avant de sauvegarder.

## Étape 6, la sauvegarde

Récupère la date du jour avec `date +%Y-%m-%d`.

Chemin : `{{REPO_CLIENT}}/raw/revue-de-presse/YYYY-MM-DD-revue-{{SLUG_CLIENT}}.md`

Si un fichier existe déjà pour ce jour, ajoute un suffixe `-bis`.

Termine ta réponse par une ligne au format : `Édition {{NOM_CLIENT}} · [date] · [chiffre court]`.

## Notes finales

- **Jour creux assumé** : « RAS » vaut mieux que du remplissage.
- **Contradictions** : si deux sources se contredisent, mentionne-le explicitement. C'est un signal de qualité, pas un défaut.
- **Surveillance équilibre** : si 3 fiches d'affilée traitent du même angle (ex. « réglementation »), force le 4e jour sur un autre angle (« usage », « technologie », « marché »).
- **Une mission qui se termine** = supprimer le skill (`rm -rf ~/.claude/skills/revue-presse-{{SLUG_CLIENT}}`) ET la routine `/schedule` associée.

---

## ANNEXE — Comment customiser ce skill (à faire UNE FOIS par client)

Avant de déposer ce SKILL.md, remplace **tous** les `{{...}}` :

| Placeholder | Quoi mettre | Exemple |
|---|---|---|
| `{{NOM_CLIENT}}` | Nom du client en clair | Caroline Mutuelle |
| `{{SLUG_CLIENT}}` | Slug kebab-case | caroline-mutuelle |
| `{{THEME_COURT}}` | 3-5 mots | mutuelle santé TPE |
| `{{THEME_DETAILLE}}` | 2 phrases qui cadrent la niche | « Mutuelles complémentaires santé pour entreprises de moins de 50 salariés, avec focus sur les surcomplémentaires longue durée et santé mentale. » |
| `{{AUDIENCE_VISITEURS}}` | L'avatar des visiteurs des pages | Dirigeants de TPE 5-50 salariés |
| `{{DOCTRINE_CLIENT}}` | La position éditoriale (à co-rédiger lors d'un call de 15 min avec le client) | « Les TPE sont sous-équipées en surcomplémentaires longue durée. » |
| `{{URL_PAGE_1/2/3}}` | URLs des 3 pages principales à alimenter | https://caroline-mutuelle.fr/tpe/longue-duree |
| `{{SOURCE_1}}` à `{{SOURCE_5}}` | Les 5 sources sectorielles préférées | DREES, FNMF, Argus de l'assurance, INSEE, LinkedIn des courtiers TPE |
| `{{REPO_CLIENT}}` | Chemin absolu du repo client | /Users/<toi>/Code/projet-caroline-mutuelle |
| `{{VOIX_CLIENT_PATH}}` | Chemin du fichier voix du client (à co-rédiger lors d'un call) | /Users/<toi>/Code/projet-caroline-mutuelle/source/voix-client.md |

**Tip** : ouvre ce fichier dans VS Code, fais Find/Replace, traite chaque placeholder une fois.

**Tip 2** : remplir les 5 sources avec le client (call 15 min) est la phase la plus importante. Sans sources sectorielles, le skill remonte du SEMrush et du Backlinko inutiles.

## ANNEXE — Préparer le fichier voix client (`{{VOIX_CLIENT_PATH}}`)

Co-rédigé avec le client lors d'un call de 30 min. Sans ce fichier, le skill ne peut PAS écrire la « Formulation prête à coller ». Voici le template à remplir :

```markdown
# Voix éditoriale — {{NOM_CLIENT}}

## Adresse au lecteur
Tutoiement / Vouvoiement / Mix : [choisir]
Exemple à imiter : « [phrase issue d'un texte signé par le client] »

## Vocabulaire interdit
- [terme jargon que le client refuse]
- [formule corporate qu'il ne veut pas]
- [anglicisme à proscrire]

## Vocabulaire signature
- [3-5 termes que le client utilise systématiquement]

## Niveau de technicité
[junior / mixte / expert] — exemple de mot-clé technique acceptable : [X]

## Ton dominant
[chaleureux / institutionnel / cash / pédagogique / engagé] — décrire en 2 phrases comment ça doit "sonner"

## Trois extraits canoniques (à copier-coller)

Extrait 1 (un email ou post du client) :
> « ... »

Extrait 2 :
> « ... »

Extrait 3 :
> « ... »

## Règles spécifiques
- [ex. jamais d'emoji]
- [ex. toujours un chiffre en intro]
- [ex. pas de "il est important de"]
```

Le fichier vit dans le repo du client (`{{VOIX_CLIENT_PATH}}`). Versionné en Git. Mis à jour quand le client corrige une livraison.

## ANNEXE — Brancher /schedule (cron remote)

Une fois le skill installé sous `~/.claude/skills/revue-presse-{{SLUG_CLIENT}}/SKILL.md` :

1. Dans Claude Code (depuis le repo client), tape `/schedule`
2. Crée une routine :
   - **Cron** : `0 8 * * *` (tous les jours à 8h)
   - **Repo** : `{{REPO_CLIENT}}`
   - **Prompt** : `/revue-presse-{{SLUG_CLIENT}}`
3. Active

La routine tourne sur l'infra Anthropic, MacBook fermé, commit auto dans le repo client si configuré sous Git.

**Variante launchd local** : si le repo n'est pas sous Git, modèle de script dans `seo-kb/.claude/bin/run-revue-presse.sh` (à adapter).
