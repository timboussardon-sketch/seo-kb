# Directives pour la prochaine édition

> PÉRIMÈTRE STRICT (Tim, 2026-05-30) : SEO, IA, LLM, Google, moteurs de recherche, search marketing. RIEN D'AUTRE. Test : « ça change la façon dont on est trouvé/lu/cité dans un moteur ? » Sinon, écarter.
>
> LIENS DE SOURCES (Tim, 2026-05-30) : TOUJOURS afficher le lien cliquable de chaque source dans le corps.


Écrit par l'agent 9 (calibration) à la fin de chaque édition. Lu par l'agent 0 (briefing) au début de la suivante. Garder court et actionnable.

## Édition 0 (amorçage, 2026-05-30)

Pas encore d'historique. Première édition à produire sans biais de boucle. Objectifs d'amorçage :

- Tenir les 4 critères de qualité dès la première : recoupement, angle inédit, lien doctrine, hook intelligent.
- Pour chaque info retenue, exiger au moins 2 sources indépendantes (recoupement).
- Lier au moins une info à un concept de la doctrine via `./kb search`.
- Tester le mode explore : trouver au moins 1 source nouvelle, hors liste socle, et la noter dans `source_registry.jsonl`.
- Logger au moins 1 prédiction datée dans `predictions.jsonl`.

## Directives pour la prochaine édition (écrit après 2026-05-30-v4)

- **Anti-redite (mis à jour v4)** : déjà traités, ne pas reprendre sans fait nouveau → « guide AEO du 15 mai », « Information Agents I/O » (v2), « commerce agentique / Universal Cart / UCP » (v3), Cloudflare crawl-to-refer (v3), conversion trafic IA vs volume (v3), **« llms.txt non utilisé par Google » + champ de recherche redessiné I/O + parts Gemini vs ChatGPT + CTR AIO recovery Seer (v4)**. Voir `said_index.jsonl`.
- **Leçon v4 (vérifier l'overlap avant de choisir l'info du jour)** : avant de figer l'info du jour, lire `runs.jsonl` champ `sujet_info_jour`/`sujets_candidats` des runs récents (y compris cloud), pas seulement `said_index.jsonl`. Le sujet llms.txt avait déjà été effleuré par le run cloud via le guide du 15 mai. Préférer un sujet vierge quand il en existe un d'aussi solide. Voir mistake M-004.
- **Pistes fraîches non encore traitées (candidates prochaine édition)** : fin du déploiement du core update de mai (bilan ≥1 semaine après le 4 juin) ; premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; remontées terrain sur le bloc Expert Advice des AIO (résout P-2026-05-30-1, échéance 2026-07-15) ; Perplexity / ChatGPT search côté citations (jamais traité en profondeur) ; tester une source FR de référence (Abondance).
- **Suivre en priorité** :
  - Fin du core update de mai (déploiement clos vers le 4 juin). Quand Google confirme la fin, candidat brève « bilan » si des verticaux gagnants/perdants nets se dégagent dans les données publiques. Attendre ≥1 semaine après la fin avant de citer des courbes.
  - Premières remontées terrain sur le checkout agentique UCP/Universal Cart (déploiement US « cet été »). Dès qu'un retailer publie un chiffre de ventes via agent → info du jour forte (résout aussi P-2026-05-30-2).
  - Parts de marché chatbots (Gemini vs ChatGPT) : guetter une mise à jour Similarweb postérieure à janv. 2026 pour avoir un chiffre dans la fenêtre fraîcheur. Angle « diversifier sa cible GEO » non encore utilisé.
- **Prédictions ouvertes à surveiller** : P-2026-05-30-1 (Expert Advice / citations première main, échéance 2026-07-15), P-2026-05-30-2 (vente checkout agentique, 2026-09-30), P-2026-05-30-3 (Googlebot < 27 % crawl IA, 2026-12-31).
- **Sources** : 3 sources fortes ajoutées en explore ce run (cloudflare-radar 0.85, similarweb-geo 0.78, seer-interactive 0.75). Les confirmer ou non en revue hebdo. Continuer 1 source neuve/édition. Penser à tester une source FR de référence (Abondance) la prochaine fois.

## À tester (issu de questions.md)

- Rubrique fixe « ce qu'un agent retiendrait » pour forcer l'angle citation (à valider en revue hebdo).

## À éviter (issu des critiques passées)

- Empiler des stats mono-source de blogs marketing. Toujours recouper avant de mettre un chiffre dans le corps.
- **Piège fraîcheur confirmé v3** : les résumés de WebSearch redatent en 2026 des études de 2025. RÈGLE : pour tout chiffre clé, ouvrir la source primaire et vérifier la date de publication ET la période de mesure avant de l'écrire. Si l'étude a > 30 j, soit on la date explicitement dans le corps, soit on ne la met pas en brève.
