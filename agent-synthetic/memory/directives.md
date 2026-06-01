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

## Directives pour la prochaine édition (écrit après 2026-05-30-v5)

- **Anti-redite (mis à jour v5)** : déjà traités, ne pas reprendre sans fait nouveau → « guide AEO du 15 mai », « Information Agents I/O » (v2), « commerce agentique / Universal Cart / UCP » (v3), Cloudflare crawl-to-refer (v3), conversion trafic IA vs volume (v3), « llms.txt non utilisé par Google » + champ de recherche redessiné I/O + parts Gemini vs ChatGPT + CTR AIO recovery Seer (v4), **« formats publicitaires payants dans AI Mode / GML 20 mai » + « ads ChatGPT OpenAI » + « divergence citations ChatGPT/Perplexity Averi 680M » + « Ahrefs 38 % citations AIO top-10 » + « dépréciation résultats enrichis FAQ » (v5)**. Voir `said_index.jsonl`.
- **Distinction à garder en tête (v5)** : la publicité payante dans la réponse générative (formats Gemini étiquetés Sponsored) est un sujet distinct du checkout agentique organique (UCP, v3). Ne pas confondre les deux dans une prochaine édition.
- **Leçon v4 maintenue (vérifier l'overlap avant de figer l'info du jour)** : lire `runs.jsonl` champ `sujet_info_jour`/`sujets_candidats` des runs récents (cloud inclus), pas seulement `said_index.jsonl`. Voir mistake M-004.
- **Pistes fraîches non encore traitées (candidates prochaine édition)** : bilan de fin de déploiement du core update de mai (attendre ≥1 semaine après le ~4 juin) ; premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; remontées terrain sur le bloc Expert Advice des AIO (résout P-2026-05-30-1, échéance 2026-07-15) ; suivi de la mise à disposition des formats pub AI Mode aux annonceurs (résout P-2026-05-30-5) ; tester une source FR de référence (Abondance), toujours pas fait.
- **Suivre en priorité** :
  - Bilan du core update de mai (déploiement clos vers le 4 juin). Candidat brève « bilan » si des verticaux gagnants/perdants nets se dégagent dans les données publiques, ≥1 semaine après la fin.
  - Premières remontées terrain sur le checkout agentique UCP/Universal Cart (déploiement US « cet été »). Un chiffre de ventes via agent → info du jour forte (résout P-2026-05-30-2).
  - Disponibilité effective des formats pub AI Mode (Conversational Discovery Ads, Highlighted Answers) pour les annonceurs, et premiers retours sur la frontière organique/payant dans la réponse (résout P-2026-05-30-5).
  - Nouvelle mesure de recouvrement de citations entre moteurs (suite Averi/Profound) : guetter une étude postérieure pour résoudre P-2026-05-30-6.
- **Prédictions ouvertes à surveiller** : P-1 (Expert Advice / citations première main, 2026-07-15), P-2 (vente checkout agentique, 2026-09-30), P-3 (Googlebot < 27 % crawl IA, 2026-12-31), P-4 (llms.txt non utilisé maintenu, 2026-12-31), P-5 (format pub AI Mode sorti du stade annonce, 2026-12-31), P-6 (recouvrement citations ChatGPT/Perplexity < 25 %, 2026-12-31).
- **Sources** : 3 sources ajoutées en explore ce run (ahrefs 0.8, averi 0.62, tryprofound 0.6). Les confirmer/retirer en revue hebdo. ahrefs est une source SEO de référence, bonne candidate au passage exploit. Continuer 1 source neuve/édition. Tester enfin une source FR de référence (Abondance) la prochaine fois.

## À tester (issu de questions.md)

- Rubrique fixe « ce qu'un agent retiendrait » pour forcer l'angle citation (à valider en revue hebdo).

## À éviter (issu des critiques passées)

- Empiler des stats mono-source de blogs marketing. Toujours recouper avant de mettre un chiffre dans le corps.
- **Piège fraîcheur confirmé v3** : les résumés de WebSearch redatent en 2026 des études de 2025. RÈGLE : pour tout chiffre clé, ouvrir la source primaire et vérifier la date de publication ET la période de mesure avant de l'écrire. Si l'étude a > 30 j, soit on la date explicitement dans le corps, soit on ne la met pas en brève.

## Directives pour la prochaine édition (écrit après 2026-06-01)

- **Anti-redite (mis à jour 2026-06-01)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « core update mai : fin de déploiement + faits procéduraux (absence de billet, cadence 6-7 sem) » (2026-06-01), « échéancier de retrait des résultats enrichis FAQ juin/août » (2026-06-01), « composition des sources moteurs de réponse : litige Reddit-Perplexity, YouTube devant Reddit » (2026-06-01), « parts de marché search IA vs Google/Bing StatCounter » (2026-06-01). Voir `said_index.jsonl`.
- **PRIORITÉ prochaine édition (le bilan reporté)** : le déploiement du core update de mai se termine ~4 juin. Dès qu'une analyse à large échantillon sort (SISTRIX/Lily Ray attendue ~5 juin, Sistrix Visibility, Semrush Sensor stabilisé), produire le bilan gagnants/perdants par vertical. Cela résout P-2026-06-01-1 (profil des perdants : déficit de signaux structurés vs vertical unique). C'est l'info du jour la plus forte disponible à court terme. Attendre la fin du déploiement + données stables, ne pas publier de liste avant le 4 juin.
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; remontées terrain sur le bloc Expert Advice des AIO (résout P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode aux annonceurs (résout P-2026-05-30-5) ; nouvelle mesure de recouvrement de citations entre moteurs (résout P-2026-05-30-6).
- **Sources** : Abondance enfin testée (directive tenue), ajoutée en explore 0.7, corroborée, bonne candidate au passage exploit en revue hebdo (source FR de référence). 3 autres explore ajoutées (digitalapplied, cmswire, searchlab). Continuer 1 source neuve/édition. Pour le bilan core update, viser une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) comme nouvelle source explore data.
- **Méthode confirmée 2026-06-01** : quand la semaine n'offre pas d'événement neuf, l'angle « ce que les données ne disent pas encore » + faits procéduraux est préférable à la redite ou à une liste gagnants/perdants prématurée. Assumer un novelty_score modeste (3/5) plutôt que de forcer.

## Prédictions ouvertes à surveiller (mis à jour 2026-06-01)

- P-2026-06-01-1 (profil des perdants core update mai = déficit signaux structurés, 2026-06-30, échéance courte).
- P-2026-06-01-2 (YouTube reste devant Reddit en citations moteurs de réponse, 2026-12-31).
- Plus les P-2026-05-30-1 à 6 déjà listées.
