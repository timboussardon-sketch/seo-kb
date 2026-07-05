---
type: source
source_type: article
title: Construire ton agent SEO sur Claude, de 0 à 1
aliases: [construire-agent-seo-claude]
tags: [organikk, blog, tim, agent-ia, claude, systeme, seo]
created: 2026-06-11
updated: 2026-07-05
sources: 1
confidence: high
status: stable
---

# Construire ton agent SEO sur Claude, de 0 à 1

**Auteur** : Timothée Boussardon (organikk.co/blog)
**Type** : article de blog
**URL** : https://organikk.co/blog/construire-agent-seo-claude/
**Date publication** : 2026-06-11

## Contexte
Tim détaille comment transformer Claude d'un chatbot en agent SEO autonome, du zéro à la version 1. L'agent repose sur 4 composants : mémoire (un vault de fichiers markdown), compétences (les skills versionnés), routines (tâches lancées à heures fixes) et boucles (mesure qui corrige les décisions). Il documente la migration de Cowork vers le duo Terminal (Claude Code) + Obsidian, la structure du vault (raw/ immuable + wiki/ digéré), la doctrine AGENTS.md lue à chaque session, les 9 skills SEO, 4 workflows, un contrôle qualité bloquant et 3 boucles d'apprentissage.

## Chiffres / faits clés
- L'agent fait environ 80 % du SEO de Tim ; les 20 % restants = stratégie, data propriétaire, jugement.
- Migration Cowork → Terminal + Obsidian en 15 minutes (même dossier, deux interfaces).
- 9 skills SEO encodés (quick-win, cannibalisation, maillage, pSEO, entités vectorielles, cluster AEO, product-led, peurs-objections, brief contenu).
- Workflow d'audit SEO en 8 phases, durée 2-3 heures.
- 7 règles non négociables ; contrôle qualité à 4 critères, tous obligatoires.
- Routines cloud plafonnées : 5/jour sur Pro, 15/jour sur Max ; abonnement Claude Pro ~20€/mois.

## Citations marquantes
> "Demain, les boîtes ne paieront plus pour du TJM." (attribution: Tim, 2026-06-11)

> "Mon agent fait 80 % de mon SEO." (attribution: Tim, 2026-06-11)

> "Ce qui est publié revient mesuré." (attribution: Tim, 2026-06-11)

## Angle SEO à retenir
La valeur ne réside plus dans les skills isolés (copiables) mais dans l'architecture système, la data propriétaire en entrée, les boucles de mesure et le jugement humain en sortie. La boucle 3 (sortie → apprentissage) est la plus rentable : chaque page publiée reçoit une fiche preuve avec prédictions datées (J+30 / J+90), que la Search Console vient mesurer pour corriger la doctrine. Sans elle, "ma méthode marche" reste un argument commercial ; avec, c'est un fait mesuré. Condition technique : le vault reste en local sur le disque, jamais dans iCloud/Drive/OneDrive (la synchro casse la lecture des fichiers).

## Limites
Article méthodologique et commercial (positionnement Organikk face à la commoditisation du SEO). Décrit l'architecture d'un système personnel sans exposer de résultats client mesurés. Les 80 % sont une estimation de l'auteur, pas une mesure.

## Pages liées
**Entity** : [[entities/organikk-co]] · [[entities/qadence-seo-agent]] · [[entities/obsidian]] · [[entities/gsc]] · [[entities/karpathy]]
**Concepts** : [[concepts/ingest-workflow]] · [[concepts/regle-ia-ne-le-fait-pas-je-le-fais-pas]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/data-proprietaire]] · [[concepts/anti-ai-writing]] · [[concepts/objection-confidentialite-rgpd]] · [[concepts/obsidian-as-ide]]
