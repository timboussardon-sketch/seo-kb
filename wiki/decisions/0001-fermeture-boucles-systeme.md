---
type: decision
title: "ADR-0001 — Fermeture des trois boucles ouvertes du système"
aliases: [adr-0001, fermeture-boucles]
tags: [decision, adr, kb, automation, doctrine, moat]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: accepted
---

# ADR-0001 — Fermeture des trois boucles ouvertes du système

## Contexte

Audit du système au 2026-05-16. L'architecture est solide : séparation raw/wiki immuable, [[index|AGENTS.md]] comme schéma vivant, ~3 600 wikilinks, [[log]] append-only, dashboard quotidien, automations launchd. Le système capture et compile très bien. Il ne ferme pas ses boucles.

Trois boucles restaient ouvertes. Capture vers traitement : ratio raw→wiki sous 1, aucun radar sur le raw non digéré. Doctrine vers validation : beaucoup de claims "non validé" éparpillés, `test-terrain` à une seule source, le moat "data propriétaire" affirmé mais pas prouvé dans le vault. Sortie vers apprentissage : la performance des contenus publiés ne revenait jamais dans le wiki, `gsc-export` à zéro. En plus : pas de portes d'entrée humaines (index = catalogue plat, pas de MOC), pas de rituel de décision hebdo, pas de journal de décisions, pas de résurgence des notes oubliées.

## Décision

Fermer les trois boucles par des registres seedés avec le contenu réel du vault et des routines automatisées, sans toucher aux deux automations que Tim a explicitement mises hors scope (revue de presse quotidienne, lint hygiène hebdo GH Actions).

Boucle capture : registre [[ingest-backlog]] + skill `ingest-backlog-sweep` hebdo. Boucle validation : registres [[hypotheses]] et [[contradictions]] + skill `hypotheses-validation` mensuel. Boucle apprentissage : dossier [[preuves/index]] + skill `preuves-feedback` à la demande, remplissage manuel (pas de pull GSC pour l'instant). Navigation : [[000-home]] + cinq MOCs thématiques. Décision : dossier [[decisions/index|wiki/decisions/]] en ADR. Rituel : skill `revue-hebdo` le vendredi, distinct du lint technique. Résurgence : skill `resurgence-espacee` en milieu de semaine.

## Alternatives écartées

RAG / vector search au lieu de registres markdown : écarté, le système est sous le seuil des ~500 fichiers où le wiki + grep reste supérieur, et ça contredirait [[concepts/persistent-wiki-vs-rag]]. Un seul méga-registre "santé du vault" : écarté, mélanger backlog, hypothèses et contradictions tue la cadence de revue propre à chacun (hebdo vs mensuel). Tout passer en GitHub Actions : écarté, la revue de presse a déjà été migrée de GH Actions vers launchd faute d'`ANTHROPIC_API_KEY` disponible en CI ; on reste sur launchd local, pattern prouvé. Pull GSC automatisé tout de suite pour la boucle preuves : écarté à la demande de Tim, on livre la structure et le remplissage manuel d'abord pour démarrer la boucle sans dépendance externe fragile.

## Conséquences

Le schéma AGENTS.md passe en v2.6 : nouveaux types `register`, `moc`, `decision`, `proof` et formalisation des types déjà utilisés en pratique (`doctrine`, `synthesis`, `audit`, `revue-presse`, `pseo-strategy`). Quatre nouveaux LaunchAgents s'ajoutent aux quatre existants : surface d'automation plus large, donc plus de points de panne à surveiller dans le dashboard. Une hypothèse ne peut plus passer `validé` sans fiche preuve : la doctrine devient plus lente à affirmer mais opposable. La mémoire `canonical_vault_path` (qui pointait vers `/Users/timothee/Documents/seo-kb/`, chemin disparu) est corrigée vers `/Users/timothee/Code/seo-kb/`.

Dette acceptée : les registres sont seedés au 2026-05-16 mais leur valeur dépend de la discipline de revue. Si la revue hebdo et la validation mensuelle ne tournent pas, on aura ajouté des documents morts de plus. C'est le risque assumé, atténué par l'automation cron.

## Suivi

Skills : `.claude/skills/ingest-backlog-sweep/`, `hypotheses-validation/`, `preuves-feedback/`, `revue-hebdo/`, `resurgence-espacee/`. Routines : `.claude/launchd/com.timboussardon.{ingest-backlog,hypotheses-validation,revue-hebdo,resurgence}.plist`. Docs : [[ingest-backlog]] · [[hypotheses]] · [[contradictions]] · [[preuves/index]] · [[000-home]]. Entrée [[log]] du 2026-05-16.

Pages liées : [[decisions/index]] · [[000-home]] · [[hypotheses]]
