# Plan de test des formats X (résoudre les contradictions sur ta propre data)

> Compagnon de [[Playbook-X-autorite-SEO-IA]] et [[Algo-Grok-X-decryptage]]. On ne tranche pas les débats du web par opinion, on les tranche sur ta data, en 4 semaines.
> Logique : claim → prédiction datée → mesure → verdict. La même boucle que SyntheticBrain, appliquée à X.

---

## En résumé

Deux contradictions du web restent ouvertes et ne se règlent que sur TON compte :
1. **Threads courts vs posts solo longs** : qui ramène le plus d'impressions + d'abonnés dans ta niche ?
2. **Vidéo native vs texte** : la vidéo vaut-elle l'effort pour toi ?

On teste les deux en parallèle sur 4 semaines, à variables contrôlées, avec une règle de décision fixée à l'avance (pour éviter de lire la data dans le sens qui t'arrange). À la fin, tu as deux verdicts chiffrés et tu réalloues ton temps en conséquence.

Pré-requis : Premium activé (sinon les impressions sont biaisées par le déboost non-Premium), et l'analytics natif X accessible.

---

## Les hypothèses (à dater aujourd'hui)

| # | Claim à tester | Prédiction par défaut (à confirmer/infirmer) | Resolve by |
|---|---|---|---|
| H1 | Les threads courts (3-6) battent les posts solo longs sur les impressions | Incertain, le web se contredit | J+28 |
| H2 | Les threads battent les posts solo sur les abonnés gagnés/post | Plausible (plus de surface) | J+28 |
| H3 | La vidéo native (> durée min) bat le texte sur impressions ET bookmarks | Incertain, contradiction franche | J+28 |
| H4 | Le post solo long a le meilleur ratio résultat/temps investi | Hypothèse perso à valider | J+28 |

Note : on mesure aussi le coût en temps de chaque format, parce que le bon format n'est pas le plus performant dans l'absolu, c'est le meilleur rendement par heure passée.

---

## Le protocole (variables contrôlées)

Le piège : l'algo Grok score par user, avec décroissance temporelle et cap de diversité. Un vrai A/B parfait est impossible. On neutralise donc le maximum de variables.

**3 bras, en rotation :**
- **A** : post solo long (1 post dense, format « affirmation + preuve + mini-démonstration »).
- **B** : thread court (3-6 posts, hook qui tient seul).
- **C** : vidéo native (toi face cam ou screen-record, > durée minimale, 60-140 s).

**Règles de contrôle :**
- **Même sujet, même pilier** sur une même semaine (ex : semaine 1 = AEO, semaine 2 = data GSC…). Tu ne compares pas « vidéo sur un sujet chaud » vs « texte sur un sujet tiède ».
- **Rotation des créneaux** : chaque bras passe à tour de rôle dans les 3 fenêtres (matin / midi / soir) pour neutraliser l'effet horaire.
- **Un seul format par jour** posté en « gros contenu » (le reste de la journée = tes posts courts habituels + reply game, qui continuent normalement).
- **Pas de lien dans le corps**, pour aucun bras (sinon tu mesures la pénalité lien, pas le format).
- **Même soin éditorial** partout (hook retravaillé, ton de voix Tim). On ne saborde pas un bras.

**Volume minimum pour que ce soit lisible :**
- Au moins **8 à 10 posts par bras** sur les 4 semaines (donc ~24-30 « gros contenus » au total, soit ~1/jour ouvré). En dessous, c'est du bruit, pas de la data.

---

## Les métriques (par post, à logger)

Pour chaque gros contenu, tu relèves à J+2 (le post a fini sa course) :

| Métrique | Pourquoi | Source |
|---|---|---|
| Impressions | reach brut | analytics X |
| Taux d'engagement | impressions => actions | analytics X |
| Réponses reçues | signal #1 (conversation) | post |
| Bookmarks | signal fort « à sauvegarder » | analytics X |
| Profile visits | intention de te suivre | analytics X |
| Nouveaux abonnés (estimés sur la fenêtre) | l'objectif réel | analytics X (courbe) |
| Temps de prod (minutes) | le rendement | toi |

**Métrique reine** = abonnés gagnés par heure investie (croise « nouveaux abonnés » et « temps de prod »). Métrique secondaire = bookmarks/impression (proxy d'autorité).

---

## La règle de décision (fixée AVANT de regarder la data)

Pour éviter le biais de confirmation, on décide maintenant comment on tranchera :

- Un bras « gagne » sur une métrique s'il dépasse les autres de **≥ 25 % en médiane** (pas en moyenne : la médiane résiste aux posts viraux aberrants).
- Si l'écart est **< 25 %**, on déclare **égalité** et on choisit le format au meilleur rendement temps (H4).
- On regarde la **médiane**, jamais le meilleur post (un viral ne fait pas une stratégie).
- Verdict écrit pour chaque hypothèse : **Confirmé / Infirmé / Égalité (rendement décide)**.

---

## Template de log (à copier par post)

```
- Date :
- Bras : A (solo long) / B (thread) / C (vidéo)
- Sujet / pilier :
- Créneau : matin / midi / soir
- Hook (1re ligne) :
- Impressions :
- Engagement % :
- Réponses :
- Bookmarks :
- Profile visits :
- Abonnés estimés gagnés (fenêtre) :
- Temps de prod (min) :
- Note libre (ce qui a marché / raté) :
```

Range les logs dans ce dossier (`raw/x-playbook/logs-test/`), un fichier par semaine. À J+28, on agrège et on remplit le tableau de verdicts.

---

## Tableau de verdicts (à remplir à J+28)

| # | Hypothèse | Médiane A | Médiane B | Médiane C | Écart | Verdict |
|---|---|---|---|---|---|---|
| H1 | impressions thread vs solo | | | n/a | | |
| H2 | abonnés/post thread vs solo | | | n/a | | |
| H3 | vidéo vs texte (impr. + bookmarks) | | | | | |
| H4 | meilleur rendement abonnés/heure | | | | | |

**Décision finale** : le ou les format(s) qui passent dans le playbook comme format par défaut, et celui qu'on abandonne ou réserve aux gros sujets.

---

## Boucle d'apprentissage

À J+28, ce test devient une brique de doctrine X : tu mets à jour le §3 « formats » du [[Playbook-X-autorite-SEO-IA]] avec les verdicts chiffrés (« sur mon compte, format X = +N % d'abonnés/heure, mesuré sur 4 semaines »). Ça remplace les « il paraît que » du web par ta propre preuve first-party, exactement le moat que tu défends en SEO.

Test suivant possible une fois celui-ci tranché : hooks (question vs affirmation tranchée vs data brute), ou heures de publication FR vs US.
