---
type: contenu
format: pilier
projet: qadence
cluster: A — agent seo
statut: draft à valider
requete_cible: agent seo
intention: Know → Do
url_cible: /agent-seo
capacite_qadence: l'agent branché GSC · table skills (36 slugs) · project_memory · 6 agents cron · track_reco + cron-reco-outcome
schema: Article + FAQPage
created: 2026-07-16
updated: 2026-07-16
regles: answer-first · passages ancrés 150-200 mots · ≥2 preuves atomiques/100 mots · TENSION→RÉSOLUTION→PREUVE · voix Tim tutoiement · zéro chiffre inventé · attribution systématique · ASSISTE jamais ne REMPLACE
sources_vault: [[agentic-search]], [[data-proprietaire]], [[memory-llm-vs-wiki-persistant]], [[persistent-wiki-vs-rag]], [[boucle-sortie-mesure]], [[preuve-atomique]], [[entities/qadence-seo-agent]], [[sources/2026-06-11-organikk-construire-agent-seo-claude]], [[sources/2026-03-13-algorithme-agents-seo-consultants]], [[sources/2026-01-28-organikk-premier-agent-seo-ia]]
surprise_gap: la brique qui paie n'est ni la mémoire ni les skills, c'est la boucle qui re-mesure. Personne n'en parle sur la SERP.
---

# Agent SEO

Un agent SEO est un système qui tient quatre composants : une mémoire de ton projet, des compétences encodées, des routines qui tournent sans toi, et des boucles qui re-mesurent ce qu'il a recommandé. Un chatbot SEO n'a que les compétences. C'est la seule différence qui compte, et c'est celle qui décide si tu récupères un conseil ou un résultat.

Ce découpage en quatre composants vient de l'architecture que j'ai documentée en construisant le mien (Timothée Boussardon, *Construire ton agent SEO sur Claude, de 0 à 1*, 11 juin 2026).

## Les quatre composants d'un agent SEO

**La mémoire.** L'état de ton projet : ce qui a été décidé, ce qui a été publié, ce qui a bougé.

**Les compétences.** Les process encodés une fois et rejoués à l'identique. Chez moi, ce sont 36 skills versionnés dans une table, synchronisés depuis mes fichiers de doctrine.

**Les routines.** Les tâches lancées à heures fixes, sans que tu les demandes. Qadence en fait tourner six en cron : surveillance quotidienne, quick wins et cannibalisation le lundi, maillage le 1er du mois.

**Les boucles.** Ce qui a été recommandé revient mesuré. C'est le composant que presque personne ne met en place.

Retire les boucles, tu as un assistant. Retire les routines, tu as une bibliothèque de prompts. Retire la mémoire, tu as un chatbot.

## Ce qui sépare un agent SEO d'un chatbot SEO

Attention à l'argument facile : « le chatbot repart de zéro à chaque conversation » est faux. ChatGPT Memory existe depuis février 2024, Claude Code écrit ses propres notes depuis la v2.1.59. Les deux persistent entre sessions.

La vraie limite est ailleurs, et elle est publiée par les éditeurs eux-mêmes. Claude Memory charge 200 lignes ou 25 Ko au démarrage. ChatGPT Memory retient des faits courts sur toi, dans un format interne, non exportable.

Ces mémoires servent à ce que l'IA te réponde mieux. Elles ne tiennent pas le dossier de ton site : la position de chaque page, la décision que tu as actée il y a six mois, la recommandation émise en mars et ce qu'elle a donné en mai. C'est une différence de finalité, pas de présence.

Un agent SEO tient ce dossier parce qu'il est branché sur la donnée qui le remplit. Qadence lit ta Search Console et compare 28 jours à 28 jours avant de répondre. Le chatbot, lui, répond sur le corpus moyen.

## La mémoire : trois régimes, pas un sac de faits

Une mémoire d'agent SEO utile sépare trois choses.

**Les faits ponctuels** : ton CMS, ton secteur, ton point de conversion.

**Les décisions actées** : les contraintes dures. Tu as refusé une tactique, tu as des URLs intouchables, ton périmètre de mots-clés est fermé. L'agent doit les respecter à six mois, pas les redécouvrir à chaque session.

**Les concepts déjà expliqués** : ce qu'on t'a expliqué une fois ne se réexplique pas.

Sur Qadence, ces trois régimes vivent dans une table `project_memory` et remontent dans le prompt dans un ordre imposé : contexte client, décisions actées, état SEO réel, journal du projet, recommandations passées avec leurs résultats.

La distinction de fond : une mémoire de LLM est un contexte injecté pour que l'IA parle mieux. Un dossier de projet est un artefact que tu possèdes, que tu relis sans IA, et que tu emportes si tu changes d'outil demain.

## Les compétences : ce qui est copiable ne vaut rien

Les skills sont la partie la plus visible d'un agent SEO, et la moins défendable. Un process d'audit se copie. Un prompt se copie.

Ma position tient en une phrase : tu ne paieras pas un agent pour ce qu'il sait faire, mais pour ce qu'il sait (Algorithme #5, 13 mars 2026).

Ce qu'il sait faire, c'est de la commodité. Ce qu'il sait, c'est ta Search Console, tes prix, tes résultats clients, tes décisions. Cette donnée-là, personne ne peut la reprendre.

Corollaire qui déplaît : si tu n'es pas bon en SEO, l'agent ne sera pas bon. Il rejoue ton process. Un process moyen encodé produit du moyen à grande vitesse.

## Les routines : l'agent travaille quand tu dors

Une routine est une tâche datée qui se déclenche sans toi et qui te remonte un écart.

Chez Qadence : surveillance quotidienne à 8h, quick wins et cannibalisation le lundi, maillage le 1er du mois, re-mesure des recommandations à 7h15.

L'intérêt n'est pas le gain de temps. C'est que la surveillance ne dépend plus de ta discipline. Une chute de positions repérée trois semaines plus tard coûte trois semaines.

## Les boucles : la brique la plus rentable

C'est le composant dont la SERP ne parle pas, et c'est celui qui paie.

Ce qui est publié revient mesuré. Une recommandation part avec ses métriques de départ. À J+14 et J+30, l'agent relit la Search Console, écrit le delta réel, et ce résultat revient dans le prompt de la session suivante.

Sans cette boucle, « ma méthode marche » est un argument commercial. Avec, c'est un fait mesuré.

J'ai classé les boucles devant la mémoire et devant les skills en termes de rentabilité. La raison est simple : c'est le seul composant qui empêche l'agent de te répéter une recommandation qui n'a rien donné.

## Ce qu'un agent SEO ne fait pas

Un agent SEO assiste, il ne remplace pas.

Mon agent fait environ 80 % de mon SEO. C'est mon estimation, pas une mesure : je la donne pour l'ordre de grandeur, pas comme un chiffre à citer.

Les 20 % restants ne sont pas les miettes. Ce sont la stratégie, la data propriétaire, et le jugement. L'agent ne décide pas de ton positionnement. Il ne va pas chercher un chiffre que toi seul détiens. Il ne tranche pas un arbitrage business.

Un mot sur l'hallucination, parce que la promesse « zéro hallucination » circule et qu'elle est vendeuse. Un agent branché sur ta donnée réelle ne devine pas tes chiffres, il les lit. Ça ne le rend pas infaillible sur son raisonnement. Sur Qadence, la règle est qu'un champ non étayable par un outil consulté est omis plutôt qu'estimé.

## Construire le tien ou brancher un agent existant

Les deux se tiennent.

**Construire.** Tu montes les quatre composants toi-même. Compte 10 minutes pour une première configuration utile, et un minimum de 3 à 4 skills pour que l'agent soit opérationnel. Le guide complet : [créer un agent SEO](/blog/creer-un-agent-seo) et [agent SEO sur Claude](/blog/agent-seo-claude).

**Brancher.** Tu connectes ta Search Console et les quatre composants sont déjà montés.

Le critère n'est pas technique. Si ton SEO est ta compétence et que tu veux le graver, construis. Si tu veux le résultat cette semaine, branche.

→ **[Connecte ta Search Console à Qadence](/app)** et regarde ce que l'agent sort sur tes 28 derniers jours.

## FAQ

**C'est quoi un agent SEO ?**
Un système qui tient quatre composants : mémoire du projet, compétences encodées, routines automatiques, boucles de mesure. Il travaille sur ta donnée réelle, pas sur un corpus général.

**Quelle différence entre un agent SEO et un chatbot SEO ?**
Le chatbot a les compétences. L'agent a en plus la mémoire du projet, les routines et les boucles, et il est branché sur ta Search Console. [Le comparatif complet](/agent-seo-vs-chatbot-seo).

**Un agent SEO remplace-t-il un consultant SEO ?**
Non. Il assiste. Il rejoue un process : si le process est mauvais, la sortie est mauvaise. La stratégie, la data propriétaire et le jugement restent humains.

**Un agent SEO hallucine-t-il ?**
Branché sur ta Search Console, il lit tes chiffres au lieu de les deviner. Son raisonnement reste faillible. La règle à exiger : un chiffre non étayé est omis, pas estimé.

**Faut-il savoir coder pour avoir un agent SEO ?**
Non pour brancher un agent existant. Pour construire le tien, il faut surtout savoir faire le SEO que tu vas encoder.

---

## Notes de production (hors page)

**Fact-check appliqué.** La formulation « le chatbot repart de zéro à chaque conversation » a été retirée : [[memory-llm-vs-wiki-persistant]] la marque explicitement comme factuellement fausse et à corriger dans les productions. La page l'attaque frontalement à la place, ce qui devient un angle.

**Claims sous réserve.**
- `data propriétaire = moat` : [[data-proprietaire]] est `confidence: high` sur convergence de sources, pas sur preuve terrain. Hypothèse H-007 `en-test`, jalon J+90 au 2026-08-14. La page l'énonce en position, jamais en fait démontré.
- `80 %` : estimation de Tim (2026-06-11), signalée comme telle dans la page.
- `0 hallucination` (Algorithme #5) : non repris tel quel, trop absolu. Reformulé sur le mécanisme réel (contexte fermé + champ non étayable omis).
- `10 minutes` / `3-4 skills` : repères de méthode (2026-01-28), pas des mesures.

**À vérifier avant publication.**
- Arbitrage home vs `/agent-seo` tranché dans le sens : pilier Know ici, home = Do transactionnel. La home doit être ajustée sinon les deux pages se cannibalisent.
- Les liens `/blog/creer-un-agent-seo`, `/blog/agent-seo-claude`, `/agent-seo-vs-chatbot-seo` pointent vers des pages non encore produites (mois 2 et mois 1 de la roadmap).
