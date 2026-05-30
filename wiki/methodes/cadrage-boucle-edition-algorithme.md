---
title: "Cadrage : SyntheticBrain, boucle d'édition auto-améliorante pour Algorithme"
type: cadrage
created: 2026-05-30
status: draft, en validation avec Tim
skill-socle: revue-presse-quotidienne
runtime: /agent-synthetic
decisions-tim:
  perimetre: "Algorithme, via le skill revue-presse-quotidienne"
  signal: "interne + data réelle (engagement lecteur) dès le départ"
  auto-modif: "données seulement, prompt figé et auditable"
  publication: "rien n'est envoyé pour le moment, à valider plus tard ; gate équilibré"
  cadence-voulue: "2 éditions par jour"
  probleme-connu: "le cron local ne tourne jamais de façon fiable"
---

# Cadrage : SyntheticBrain

Doc de cadrage pour transformer la génération d'« Algorithme » en un agent qui apprend d'une édition à la suivante. Nom du système : **SyntheticBrain**. Runtime : **`/agent-synthetic`**. Socle : le skill **`revue-presse-quotidienne`** existant, qu'on enveloppe sans le réécrire.

Statut : on ne code rien tant que la direction n'est pas validée. Rien n'est envoyé.

## 0. Honnêteté sur le premier jet

Le premier brouillon de ce cadrage citait des fichiers et des chemins inexistants (`boucle-apprentissage.md`, `wiki/doctrine/`, `kb/concepts.json`, `wiki/hypotheses/registre.md`). Supposés, pas vérifiés. Ce doc-ci est calé sur la vraie structure du vault, vérifiée le 2026-05-30.

## 1. Vrais chemins du vault (vérifiés)

| Élément | Chemin réel |
|---|---|
| Éditions Algorithme brutes | `raw/revue-de-presse/{YYYY-MM-DD}-revue-presse.md` |
| Registre hypothèses | `wiki/hypotheses.md` (fichier unique, H-001 à H-010) |
| Registre contradictions | `wiki/contradictions.md` (C-001 à C-013) |
| Journal append-only | `wiki/log.md` |
| Fiches preuves | `wiki/preuves/` (+ `index.md`, `_template.md`) |
| Concepts doctrine | `wiki/concepts/` (50 fichiers) |
| Index inversé + backrefs | `.claude/index/concepts.json` |
| CLI | `./kb` (rebuild, search, concepts, audit) |
| Synthèses hebdo | `wiki/syntheses/`, `wiki/revue-hebdo/` |
| Backlog d'ingest | `wiki/ingest-backlog.md` |

## 2. Ce qui existe déjà (boucle longue, mature)

Le second cerveau de Tim tourne déjà autour de la **doctrine**, avec une vraie vérité-terrain (GSC). Trois boucles sont fermées :

1. **Capture → digestion → synthèse** : `raw/revue-de-presse/` → `ingest-backlog-sweep` → `wiki/sources/` → `wiki/concepts/` → `wiki/syntheses/`.
2. **Décision → action → log** : `revue-hebdo` → `wiki/ingest-backlog.md` → exécution → `wiki/log.md`.
3. **Hypothèse → test → verdict** : `wiki/hypotheses.md` → `wiki/preuves/` → export GSC → verdict → ajuste la `confidence` des concepts. (Partiel : H-007 en test, baseline GSC bloquée par service account absent.)

Skills et déclencheurs existants : `revue-presse-quotidienne` (quotidien 9h), `algorithme-recap-hebdo`, `hypotheses-validation`, `resurgence-espacee` (mercredi), `revue-hebdo` (vendredi), `ingest-backlog-sweep` (lundi), `gsc-watcher`. LaunchAgents `com.timboussardon.*` + workflows GitHub (`revue-presse.yml`, `algorithme-recap-hebdo.yml`, `audit-vault.yml`).

Mapping du pattern de Tim sur l'existant :

| Agent voulu | Déjà couvert par | Horizon |
|---|---|---|
| 1 Veille | `revue-presse-quotidienne` | quotidien |
| 2 Synthèse | `revue-presse-quotidienne` + `algorithme-recap-hebdo` | quotidien/hebdo |
| 3 Recherche (preuves) | `preuves-feedback`, `wiki/contradictions.md` | mensuel |
| 4 Mémoire | `wiki/concepts/`, `wiki/hypotheses.md`, `concepts.json` | continu |
| 5 Stratégie | `wiki/hypotheses.md` | mensuel |
| 6 Journal | `hypotheses-validation`, `revue-hebdo` | hebdo/mensuel |

Conclusion : le pattern existe déjà pour la doctrine. **Ce qui manque, c'est la boucle édition vers édition** : l'agent ne sait pas si l'édition d'hier était bonne et ne s'en sert pas pour faire mieux aujourd'hui.

## 3. Les 5 trous à combler (confirmés par l'exploration)

1. **Engagement lecteur** : aucune mesure d'opens, clics, réactions par édition. Pas de vérité-terrain de lecture.
2. **Calibration des sources** : aucun score « cette source a donné du vérifié vs du bruit », aucun poids appris.
3. **Wording performant** : aucune accumulation des critiques éditoriales en style maison qui se durcit.
4. **Anti-redite structurée** : limité à un match de titre sur J-1, pas de mémoire de thèmes couverts.
5. **Prédictions calibrées** : les « infos du jour » ne sont jamais confrontées a posteriori. Pas de score de justesse.

SyntheticBrain comble exactement ces cinq trous, et rien d'autre.

## 4. SyntheticBrain : la boucle d'édition

ADN à ne jamais perdre : Algorithme est une **revue de presse**. Elle va voir beaucoup de sources, elle **recoupe**, et elle sort une newsletter avec une **vraie titraille**. SyntheticBrain doit rendre ça meilleur à chaque édition, pas juste l'automatiser.

`/agent-synthetic` enveloppe `revue-presse-quotidienne` avec un agent d'entrée (0), une veille agentique, un moteur de recoupement, et trois agents de sortie (7, 8, 9).

**Phase PRODUIRE (chaque run)**

| # | Agent | Rôle |
|---|---|---|
| 0 | Briefing | Lit la mémoire : directives d'hier, prédictions ouvertes, anti-redite, poids et registre des sources, règles de titraille |
| 1 | Veille agentique | Deux modes. **Exploit** : sources connues pondérées. **Explore** : part des sujets chauds du jour, cherche activement de nouvelles sources (WebSearch, qui publie sur ce sujet, quels comptes, quels flux), les évalue et les propose au registre. La liste n'est jamais figée |
| 2 | Recoupement | Croise les sources entre elles. Une info portée par plusieurs sources indépendantes monte. Une info isolée est marquée fragile. C'est le coeur d'une vraie revue de presse |
| 3 | Connexions doctrine | Lie l'actu à la doctrine via `./kb search` et `concepts.json` |
| 4 | Fact-check à verdict | Vérifié / réfuté / incertain. Croise avec le recoupement. Seul le vérifié entre dans le corps |
| 5 | Stratégie + prédictions datées | Chaque prédiction loggée avec sa date de résolution |
| 6 | Rédaction + titraille | `ton-de-voix-tim` + skills GEO. Soigne les titres comme un objet de première classe (plusieurs candidats, le meilleur selon les règles apprises) |
| 7 | Critique + quality gate | Note la rubrique et la titraille, une passe de révision, gate équilibré |

**Phase APPRENDRE (après coup)**

| # | Agent | Rôle |
|---|---|---|
| 8 | Mémoire | Pousse les prédictions vers `wiki/hypotheses.md`, les croyances vérifiées vers `wiki/concepts/`, met à jour l'anti-redite et le registre des sources |
| 9 | Journal + calibration | Confronte prédictions échues, recoupements et engagement à la réalité, repondère les sources, écrit les directives et les règles de titraille de demain |
| 10 | Auto-interrogation | L'agent se demande explicitement « qu'est-ce qui aurait rendu cette édition meilleure ? ». Il écrit des questions ouvertes : pour lui-même (à tester au prochain run) et pour Tim (à trancher en revue). C'est le moteur d'amélioration dirigée |

La self-amélioration = les agents 9 et 10 écrivent des fichiers et des questions que l'agent 0 relit. C'est la seule mécanique, et elle reste auditable.

## 4 bis. Ce qui rend SyntheticBrain agentic et pas un cron

- **Veille non figée** : le set de sources grandit et se nettoie tout seul. Une source qui amène souvent du vérifié et du cliqué monte ; une source qui amène du bruit est retirée. Le registre est un organe vivant, pas une constante du script.
- **Recoupement actif** : l'agent ne fait pas confiance à une source unique. Il cherche la corroboration, comme un journaliste.
- **Apprentissage via skills** (voir section 5 bis) : ce que l'agent apprend ne reste pas inerte dans un JSON, ça change la façon dont les skills sont appelés et appliqués.
- **Auto-interrogation** : à chaque édition, l'agent produit sa propre liste de « comment faire mieux ».

## 5. La mémoire SyntheticBrain (choix « données seulement »)

Dossier `agent-synthetic/` (emplacement exact à confirmer : à la racine de seo-kb pour le versionnage git). Le prompt et les skills restent figés. Seuls ces fichiers évoluent :

| Fichier | Contenu | Lu par | Écrit par |
|---|---|---|---|
| `directives.md` | Consignes pour la prochaine édition | agent 0 | agent 8 |
| `source_weights.json` | Poids par source (vérifié vs bruit) | agents 0, 1 | agent 8 |
| `wording_rules.md` | Style maison accumulé | agent 5 | agent 8 |
| `predictions.jsonl` | Prédictions datées + résolution | agents 0, 8 | agents 4, 8 |
| `said_index.jsonl` | Thèmes déjà traités (anti-redite profond) | agents 0, 1 | agent 7 |
| `engagement.jsonl` | Opens/clics par édition et section | agents 0, 9 | hook futur |
| `calibration.md` | Score dans le temps | humain, agent 9 | agent 9 |
| `source_registry.jsonl` | Toutes les sources connues : score de confiance, dernière contribution utile, statut explore/exploit/retiré | agents 0, 1, 2 | agents 8, 9 |
| `headlines.jsonl` | Titres testés et leur performance, sert à apprendre la titraille | agents 0, 6 | agent 9 |
| `questions.md` | Les « comment faire mieux » écrits par l'agent : à tester, à trancher par Tim | agent 0, Tim | agent 10 |

## 5 bis. Apprentissage via skills (réconciliation avec « données seulement »)

Tim veut que l'agent apprenne via des skills, tout en gardant un prompt figé et auditable. Les deux se concilient sur trois niveaux :

1. **La mémoire est en données, l'action passe par les skills.** Les fichiers ci-dessus sont la mémoire. À chaque étape, l'agent appelle les bons skills (`revue-presse-quotidienne`, `ton-de-voix-tim`, `seo-geo-audit`, `kb-semantic-search`), et ce qu'il a appris change *comment* il les appelle (quelles sources, quelles règles de ton, quels seuils).
2. **Les règles apprises alimentent les skills.** `wording_rules.md` et `headlines.jsonl` deviennent des entrées que la rédaction injecte dans `ton-de-voix-tim`. Le skill ne change pas, son carburant s'enrichit.
3. **Skills par diff validé (décision Tim).** L'agent ne modifie ni ne crée un skill tout seul. Quand il repère qu'un pattern mérite de durcir un skill (par exemple un nouveau pattern de titraille pour `ton-de-voix-tim`, ou un nouveau sous-skill `titraille`), il **propose un diff** dans `questions.md`. Tim le valide à la revue hebdo avant application. C'est le seul cas où un prompt bouge, et jamais sans validation humaine.

## 5 ter. Définition d'une grande édition (la cible de calibration)

C'est la grille que l'agent 9 utilise pour se noter et que l'agent 7 (quality gate) applique. Quatre critères, pondérés selon Tim :

1. **Solidité du recoupement** : info vérifiée, croisée entre sources indépendantes, zéro bruit. La crédibilité.
2. **Angle inédit / surprise** : l'info ou la lecture que personne d'autre ne sort. Le Surprise Gap.
3. **Lien avec la doctrine** : relier l'actu aux piliers et concepts de Tim, donner une grille de lecture, pas empiler des news.
4. **Hook intelligent** : un titre et une accroche qui montrent qu'on est allé creuser et qu'on apporte de la valeur. **Jamais racoleur.** La titraille prouve la pertinence et la profondeur, elle ne vend pas du vide.

Le quality gate équilibré bloque l'auto-envoi si l'un de ces critères s'effondre, en particulier le recoupement (un claim non corroboré dans le corps) ou un hook qui glisse vers le racoleur.

## 6. Cadence et le problème du cron (diagnostic 2026-05-30)

Tim veut **2 éditions par jour**. Constat actuel :

- Le LaunchAgent `com.timboussardon.revue-presse.plist` est chargé, dernier exit 0, mais ne tire qu'**une fois à 9h00**.
- Les éditions produites ont des trous (présentes le 30, 27, 23, 22, 21, 19, 18 ; manquantes 24, 25, 26, 28, 29).
- Cause la plus probable : `StartCalendarInterval` ne rattrape pas un run manqué si le Mac est en veille ou fermé à 9h. Sur un portable, c'est la raison classique du « le cron ne tourne jamais ».
- Cause secondaire possible : `claude -p` headless échoue parfois, et le script avale l'erreur (`|| echo ... ; exit 0`), donc launchd croit que tout va bien.
- Il existe aussi un workflow GitHub `revue-presse.yml` (cloud, fiable), ce qui crée une redondance à clarifier.

Pistes pour 2x/jour fiable (à trancher au chantier dédié, pas maintenant) :
- Soit cloud via GitHub Actions (fiable même Mac éteint, mais auth claude headless à régler), 2 crons/jour.
- Soit local avec deux créneaux + un rattrapage au réveil (`RunAtLoad` + garde idempotente déjà présente).

## 7. Publication

Rien n'est envoyé. SyntheticBrain produit le draft dans `raw/revue-de-presse/` plus les artefacts d'apprentissage. L'envoi email est un chantier ultérieur, infra à trancher quand la boucle aura fait ses preuves. Quality gate : seuil équilibré (la plupart passent, les cas douteux basculent en draft signalé).

## 8. Décisions prises (Tim, 2026-05-30)

1. Périmètre : Algorithme, via le skill socle `revue-presse-quotidienne`.
2. Nom : SyntheticBrain. Runtime : skill `/agent-synthetic`. Mémoire : dossier `agent-synthetic/` à la racine de seo-kb (versionné git).
3. Signal : interne + engagement lecteur dès le départ.
4. Apprentissage : la mémoire est en données ; l'agent propose des diffs de skills que Tim valide à la revue hebdo. Jamais d'auto-modif du prompt.
5. Découverte de sources : auto-ajout au-dessus d'un seuil de confiance (source corroborée), retrait du bruit, tout journalisé. En dessous du seuil, validation à la revue hebdo.
6. Grande édition = recoupement solide + angle inédit + lien doctrine + hook intelligent non racoleur (section 5 ter).
7. Cadence voulue : 2 éditions/jour. Cron défaillant, à fiabiliser **maintenant** avec une alternative au launchd local (voir section 6).
8. Envoi : rien pour l'instant.
9. Quality gate : équilibré.
10. Auto-interrogation : questions groupées à la revue hebdo du vendredi (une note urgente seulement si vraiment bloquant).
11. Garde-fou de l'autonomie : autonome sur la data, jamais sur le code sans diff validé. Tout commité en git, listé dans `questions.md`, remonté en revue hebdo.

## 9. Reste à trancher au moment du chantier concerné (pas bloquant pour le chantier 1)

1. 2x/jour : quels deux créneaux, et fiabilisation cloud (GitHub Actions) ou local (deux créneaux + rattrapage au réveil) ?
2. On garde le workflow GitHub `revue-presse.yml` en parallèle ou on consolide ?
3. Infra d'envoi email, le jour où on enverra.

## 10. Découpage en chantiers (rien n'est lancé)

1. Le cerveau : `agent-synthetic/` + skill `agent-synthetic` (agents 0, 7, 8), run en draft.
2. Fact-check + calibration : agents 3 et 4 avec verdict et prédictions datées.
3. Fiabilisation cron 2x/jour.
4. Engagement lecteur (data réelle) puis, plus tard, envoi.
