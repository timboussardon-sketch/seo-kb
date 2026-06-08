---
name: preuves-feedback
description: |
  Crée ou met à jour une fiche preuve reliant un contenu publié à l'hypothèse de doctrine qu'il teste, à partir de la data fournie par Tim (export GSC, citations IA constatées, mesure client). Ferme la boucle sortie → apprentissage. Remplissage manuel : pas de pull GSC automatique.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "fiche preuve", "boucle preuves", "qu'est-ce que cet article a donné", "j'ai la data GSC de", "mesure J+30", "mesure J+90", "valider sur le terrain", ou fournit un export de perf sur une URL publiée.
---

# Preuves Feedback — fermer la boucle sortie → apprentissage

Vault : `/Users/timothee/Code/seo-kb/`. Tu écris dans `wiki/preuves/`.

## OBJECTIF

Relier ce qui est publié à ce que la doctrine prédit, et mesurer. C'est le seul mécanisme qui fait passer une hypothèse de `ouvert` à `validé`/`invalidé`. Sans data réelle fournie par Tim, pas de fiche concluante : on ne valide jamais sur une estimation (règle §5.4).

## ÉTAPE 1 — IDENTIFIER LE CONTENU ET L'HYPOTHÈSE

Demande ou déduis : quelle URL/contenu publié ? Quelle hypothèse de `wiki/hypotheses.md` ce contenu teste-t-il (H-XXX) ? Quelle prédiction chiffrée et falsifiable ? Si l'hypothèse n'est pas dans le registre, l'y ajouter d'abord (ou le signaler).

## ÉTAPE 2 — CRÉER OU RETROUVER LA FICHE

Slug : `wiki/preuves/YYYY-MM-DD-slug.md` (date de publication du contenu). Si elle existe, on la met à jour (jalon J+30 ou J+90). Sinon, copie `wiki/preuves/_template.md` et remplis le frontmatter (`hypothese`, `contenu`, `publie_le`, `jalon_30j`, `jalon_90j`).

## ÉTAPE 3 — REMPLIR AVEC LA DATA RÉELLE

Sources de vérité acceptées (au moins une, jamais inventée) :

- Export GSC sur l'URL : positions, impressions, CTR
- Citations IA constatées sur les requêtes cibles (ChatGPT / Perplexity / AI Mode), croise [[concepts/metriques-visibilite-geo]]
- Mesure client tierce : leads, réservations, closing

Remplis baseline puis le jalon concerné. Si Tim n'a pas encore la data, la fiche reste `status: en-cours`, on note la date du prochain jalon, on s'arrête là.

## ÉTAPE 4 — VERDICT

Quand un jalon est rempli, tranche : `concluante` / `non-concluante` / `bruitée`. Justifie en deux phrases ancrées sur les chiffres, sans enrobage (§11).

## ÉTAPE 5 — RÉPERCUTER

- Mettre à jour la ligne de l'hypothèse dans `wiki/hypotheses.md` (statut, lien vers la fiche) et le tableau de bord
- Mettre à jour la table "Fiches" de `wiki/preuves/index.md`
- Si `non-concluante` : ouvrir une entrée dans `wiki/contradictions.md`
- Append `wiki/log.md` : `## [YYYY-MM-DD] preuve | slug → verdict (H-XXX: statut)`

Termine par : `Preuve [slug] : jalon J+N rempli — verdict — effet sur H-XXX`

## CONTRAINTES

- Jamais de chiffre inventé ou estimé. Pas de data = fiche `en-cours`, point.
- Une fiche ne valide une hypothèse que si la prédiction était écrite de façon falsifiable AVANT la mesure. Si elle ne l'était pas, marquer `bruitée` et reformuler la prédiction pour le prochain test.
- Respecter l'anti-AI-writing §11. Pas de storytelling sur les résultats : des chiffres et un verdict.
