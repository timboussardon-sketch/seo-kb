---
type: playbook
title: "Qadence — Playbook growth (distribution)"
projet: qadence
created: 2026-07-04
updated: 2026-07-04
statut: draft
source: "[[raw/transcripts/video-growth-saas-ia-distribution]]"
---

# Qadence — Playbook growth

## En résumé

Qadence a un problème de distribution, pas un problème de produit. Le journal montre des features shippées chaque semaine depuis juin 2026 (boucle de résultat J+14/J+30, briefing proactif, 36 skills, crons autonomes) et zéro launch public. Le playbook applique la logique du transcript en mode bootstrap : un launch par semaine sur LinkedIn + X, des hooks qui empruntent des noms connus (Claude, Search Console), une amplification par le réseau perso dans la première heure, et un lead magnet hebdomadaire. Pas d'UGC farm, pas de paid, pas d'influenceurs payés avant d'avoir un format prouvé en organique.

## 1. Le filtre bootstrap : ce qui s'applique, ce qui ne s'applique pas

Le transcript décrit 4 moteurs. Qadence est bootstrap, solo, sans budget d'amplification. Le tri est le suivant.

| Moteur du transcript | Application Qadence |
|---|---|
| Product launches en cadence | **Le moteur central.** Coût = du temps. C'est le levier « Shipper » : un lancement par semaine, même histoire, nouvel angle. |
| Lead magnets LinkedIn | **Deuxième moteur.** Coûte du temps, pas d'argent. Tester sur le compte de Tim, garder ce qui marche. |
| Réseau perso (amplification) | **Oui, systématique.** Première heure de chaque launch : DM aux anciens du bootcamp, clients, réseau SEO LinkedIn. |
| Reddit marketing | **Oui pour l'EN.** Le reddit-cockpit existe déjà, il suffit d'y ajouter les threads où Qadence est la réponse. |
| Influenceurs micro-budget (200 à 1000 $ le post LinkedIn) | **Phase 2.** Seulement quand un lead magnet a prouvé sa viralité sur le compte de Tim. On paie pour dupliquer un format gagnant, jamais pour tester. |
| Whitelisting / ads | **Phase 3.** On sponsorise uniquement un post qui a déjà performé en organique. |
| UGC farm, clipping | **Non.** Réservé aux boîtes avec du cash et un produit mass market. |

Le principe du transcript qui reste vrai à toutes les échelles : personne ne se soucie du ROI d'un post isolé. L'objectif est que la niche SEO francophone (puis anglophone) voie passer Qadence plusieurs fois par semaine, jusqu'à ce que « agent SEO branché Search Console » évoque Qadence par réflexe.

## 2. Le moteur central : un launch par semaine

### La règle

Un jour fixe par semaine est le jour de lancement (le transcript cite Arcads : « every Wednesday is launch day »). Chaque semaine, une chose est annoncée publiquement, même si c'est une feature déjà en prod depuis un mois. Une feature non annoncée n'existe pas.

### Le stock de launches est déjà plein

Le journal Qadence contient des mois de matériel jamais annoncé. Inventaire au 2026-07-04 :

1. **La boucle de résultat** : l'agent re-mesure ses propres recos dans la GSC à J+14 et J+30 et affiche les deltas. Angle : un agent SEO qui rend des comptes sur ses conseils.
2. **Le briefing proactif** : l'agent ouvre la conversation avec l'état du site du jour, sans prompt. Angle : tu n'ouvres plus la GSC, elle vient à toi.
3. **La « prochaine meilleure action »** : chaque analyse finit par une carte impact / minutes / clics estimés / confiance. Angle : fin des audits de 40 pages, une action à la fois.
4. **Les crons autonomes** : positions à 7h, corrections à 8h30, rapport hebdo le lundi. Angle : « an SEO agent that works while I sleep » (le hook « fully autonomous » cité dans le transcript comme le plus performant du moment).
5. **Les 36 skills doctrine** : l'agent applique des méthodes écrites, pas de l'improvisation LLM. Angle : la différence entre un chat GPT-like et un agent outillé.
6. **Le bilingue FR/EN** : ouverture du marché anglophone. Angle secondaire, à combiner avec un launch produit.
7. **Les 3 actions gratuites** : le CTA permanent de chaque launch. On ne vend pas, on dit « teste, tu as 3 actions ».

À ce rythme, 7 launches = 7 semaines couvertes sans rien développer de nouveau. Ensuite la roadmap alimente la machine : la règle devient « toute feature mergée entre dans la file de launch ».

### Anatomie d'un launch Qadence (les 3 piliers du transcript)

**La copie.** Le hook d'abord, 75 % du temps de production dessus. Règles tirées du transcript, adaptées :

- Qadence est un nobody : le nom n'apparaît jamais dans le hook. Le hook emprunte des noms que la cible connaît : Claude, Search Console, ChatGPT, Opus. « Claude + Search Console » arrête le scroll d'un SEO ; « Découvrez Qadence » n'arrête personne.
- On montre une transformation, jamais une feature. Pas « on a lancé track_reco » mais « mon agent SEO vérifie tout seul à J+14 si ses recos ont fait gagner des clics, et il affiche les deltas ».
- Deuxième phrase = preuve. Un chiffre réel tiré de la GSC de Tim ou d'un site pilote, jamais inventé. Si aucun chiffre n'est disponible : `[À SOURCER]` et on choisit un autre angle en attendant.
- Phrase 1 radicale, phrase 2 preuve, corps ensuite. Le corps peut être plus calme que le hook, pas l'inverse.

**La vidéo.** Un screen record de 30 à 60 secondes de l'agent en train de travailler suffit. Le transcript est clair : les gens adorent voir un workflow s'exécuter (effet « boîte de Pandore »). L'agent Qadence qui déroule une analyse, pose une carte NBA et enregistre une reco est exactement ce format. Format vertical pour LinkedIn, natif X en 16:9. Pas de montage lourd : la fraîcheur bat la production.

**L'amplification.** La première heure décide de la portée. Checklist à chaque launch :

- DM le jour même à une liste fixe : anciens des bootcamps #4 et #5, clients accompagnement, pairs SEO du réseau LinkedIn. Message court : « je viens de publier ça, un like ou un commentaire m'aide beaucoup dans la première heure ».
- Publier aux heures de pointe de la cible (matin 8h-9h ou midi, heure de Paris).
- Répondre à chaque commentaire dans l'heure.
- Cross-post X et LinkedIn le même jour, hooks adaptés à chaque plateforme (2 premières phrases sur LinkedIn, premières lignes sur X, per le transcript).

### La règle « volume + qualité »

Le transcript tranche le débat : les deux, et quand la feature est terne, on l'emballe dans un sujet qui excite (l'exemple de l'API présentée via un workflow Gumloop). Version Qadence : une feature technique (cache prompt, context editing) ne se lance pas seule, elle se raconte à travers son effet (« l'agent coûte 10 fois moins cher à faire tourner, donc le plan gratuit existe »).

## 3. Deuxième moteur : le lead magnet hebdomadaire

Le canal bootstrap le plus rentable selon le transcript : lead magnets LinkedIn testés sur son propre compte, puis dupliqués via influenceurs et ads quand un format gagne.

Application :

- **1 lead magnet par semaine sur le compte LinkedIn de Tim**, en plus du launch. La matière existe déjà dans le vault : grilles d'audit, méthodes des skills, workflows Claude + GSC, checklists doctrine. Chaque lead magnet est un extrait de doctrine actionnable, avec commentaire pour recevoir le document.
- Le lead magnet ne parle pas de Qadence : il démontre la méthode que Qadence exécute. Le CTA final renvoie vers l'agent (« cette méthode, l'agent l'applique en 2 minutes sur ta Search Console, 3 actions gratuites »).
- Tenir un tableau de bord simple : hook, format, vues, commentaires, inscriptions Qadence dans les 72h. Au bout de 8 à 10 semaines, les 2 ou 3 formats gagnants sont identifiés.
- **Phase 2** (quand un format a prouvé) : payer 2 ou 3 créateurs LinkedIn de la niche SEO/marketing FR (fourchette du transcript : 200 à 1000 $ le post) pour publier le même lead magnet, puis sponsoriser leur post (whitelisting). On achète la duplication d'un format prouvé, pas un test.

## 4. Reddit pour le marché EN

Le transcript cite un cas : un produit bootstrap parti de zéro uniquement en Reddit marketing. Qadence est bilingue depuis la phase 1 i18n et le reddit-cockpit tourne déjà. Extension : ajouter aux subreddits surveillés les threads « SEO tool », « Search Console analysis », « AI SEO agent », et répondre en voix documentation avec Qadence en mention quand le thread s'y prête. Le clic reste manuel, comme prévu par le cockpit.

## 5. Ce qu'on ne fait pas (et pourquoi)

- **Pas d'UGC farm.** Modèle réservé aux produits consumer avec budget. La cible de Qadence (SEO, consultants, fondateurs) ne se convertit pas via des comptes TikTok faceless.
- **Pas de paid avant un format organique prouvé.** Le transcript le dit pour les bootstrap : le temps remplace le budget. Le paid arrive en phase 3 sur des créatives déjà validées en organique.
- **Pas d'achat de posts d'influenceurs en phase de test.** On teste sur le compte de Tim, gratuit, puis on duplique ce qui gagne.
- **Aucun chiffre inventé dans les hooks.** Règle absolue du vault. La preuve sociale vient de data first-party réelle (GSC de Tim, sites pilotes, chiffres d'usage Qadence) ou elle n'apparaît pas.

## 6. Rythme hebdomadaire

| Jour | Action |
|---|---|
| Lundi | Choisir le launch de la semaine dans la file + écrire 3 hooks candidats, en retenir 1. |
| Mardi | Enregistrer le screen record (30-60 s), écrire le post LinkedIn + le post X. |
| Mercredi | **Launch day.** Publication matin, DM d'amplification dans l'heure, réponses aux commentaires. |
| Jeudi | Lead magnet LinkedIn (peut s'appuyer sur le récap jeudi existant). |
| Vendredi | Relever les stats (vues, commentaires, inscriptions), noter dans le tableau de bord, mettre à jour la file de launches. |

Charge estimée : 2 à 3 heures par semaine, l'essentiel sur le hook et le screen record.

## 7. Mesure

On ne juge pas un post isolé. On juge la machine, au mois :

- Nombre de launches publiés (cible : 4/mois, zéro semaine blanche).
- Inscriptions Qadence par semaine (la table users fait foi).
- Meilleur hook du mois (à recycler avec un nouvel angle).
- Signaux d'omniprésence : mentions spontanées de Qadence dans des commentaires, DM entrants, threads Reddit.

## 8. File de launches (démarrage)

1. **Semaine 1** : la boucle de résultat. Hook candidat : « Mon agent SEO revient tout seul à J+14 vérifier dans la Search Console si ses recos ont fait gagner des clics. » Preuve : premiers deltas réels attendus mi-juillet 2026 (`agent_recos` remplit depuis le 2026-07-03) ; si pas encore de data, décaler et lancer le briefing proactif d'abord.
2. **Semaine 2** : le briefing proactif. Screen record de l'ouverture du chat avec l'état du site déjà posé.
3. **Semaine 3** : « works while I sleep ». Les 3 crons (7h, 8h30, lundi) racontés en une journée type.
4. **Semaine 4** : la carte « prochaine meilleure action ». Hook sur la fin des audits-fleuves.

Chaque launch publié est journalisé dans [[qadence/Journal]] avec le hook utilisé et les stats à J+3.
