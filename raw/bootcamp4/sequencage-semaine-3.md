---
type: source
source_type: transcript
title: "Séquençage Semaine 3 — Bootcamp 4"
aliases: []
tags: []
created: 2026-05-21
updated: 2026-05-21
sources: 0
confidence: medium
status: draft
---

---
title: Séquençage Semaine 3 — Workflow audit resserré (réordonné : data GSC avant structurel)
bootcamp: 4
semaine: 3
theme: audit SEO complet, ordre data-first (positionnement/indexation → cannibalisation+maillage GSC → structurel Hn+maillage → quick wins+synthèse)
related:
  - "[[sequencage-semaine-2]]"
  - "[[workflow-audit-bootcamp4]]"
  - "[[skill-maillage-gsc-cannibalisation]]"
  - "[[skill-maillage-systeme]]"
  - "[[skill-indexation-check]]"
  - "[[skill-indexation-check-cowork]]"
  - "[[skill-workflow-mots-cles]]"
  - "[[session-3-audit-prep]]"
  - "[[session-3-audit-transcript]]"
  - "[[session-2-redaction-debrief]]"
  - "[[observations-whatsapp-bootcamp]]"
source-workflow: "[[workflow-audit-bootcamp4]] : 7 phases, dérivé du V3, mai 2026 ; réordonné mai 2026 (data GSC remontée au J2)"
---

# Séquençage Semaine 3 — Bootcamp 4

**Logique de la semaine** : on déroule le **workflow audit resserré**, mais réordonné par source de donnée. La donnée GSC d'abord (positionnement, indexation, puis cannibalisation + maillage data le même jour), le structurel ensuite (Hn + maillage structurel), la synthèse à la fin. Une phase nourrit la suivante. Chacun arrive au call avec un audit complet + un plan d'action 3 horizons sur un vrai site.

Pourquoi ce réordonnancement : la cannibalisation et le maillage GSC partent du **même export**, autant les enchaîner le même jour (J2, doc dédié [[skill-maillage-gsc-cannibalisation]]). L'audit Hn et le maillage structurel sont tous les deux du structurel **sans dépendance GSC**, ils vont ensemble (J3). Les quick wins et la synthèse ferment la semaine (J4) une fois tout le diagnostic posé.

**Le squelette = le doc workflow** (à mettre en MD sur le Drive). Version resserrée : retirés → clusters AEO, analyse vectorielle, briefs. Ajoutés → audit d'indexation (J1) et audit structurel Hn (J3). ⚠️ L'ordre des phases du doc workflow ne suit plus l'ordre des jours (re-cadrer dans le doc Drive).

| Jour | Contenu | Skill(s) | Livrable |
|------|---------|----------|----------|
| 1 | Setup + Positionnement + Indexation | aucun (prompt) + `indexation-check` | Checklist OK + tableau positionnement + rapport d'indexation |
| 2 | Cannibalisation + Maillage GSC (bundle) | `seo-cannibalisation` + `maillage-interne-gsc` | Cannibalisations (type + root cause) + plan de maillage data, conflits "maillage" résolus |
| 3 | Audit structurel Hn + Maillage structurel | scrap Hn + `maillage-systeme` | Tableau Hn par URL + audit du graphe interne (piliers, orphelines, ancres) |
| 4 | Quick Wins + Synthèse | `seo-quick-win` | Top quick wins chiffrés + **plan d'action 3 horizons (le rapport)** |
| 5 | Call (10h00) | revue 2-3 audits + démo mots-clés anti-ChatGPT | Rapport d'audit "format qui fait signer" |

Budget : 2,5-4h sur la semaine (le J3 dépend de la taille du sitemap).

---

## Jour 1 — Setup + Positionnement + Indexation

Salut à tous,

Semaine 3, on change de moteur. Les deux premières semaines on produisait du contenu avec le workflow rédaction, cette semaine on déroule l'autre gros workflow, l'audit. 100 % données Google, zéro outil payant. Vous avez le doc complet en MD sur le Drive, c'est lui le squelette, gardez-le ouvert à côté.

⚠️ Deux choses à régler AUJOURD'HUI, même si on ne s'en sert qu'à partir de demain :
- **Chrome + l'extension Claude in Chrome** : on en a besoin au J2 (ouvrir les URLs en conflit), au J3 (scrap Hn + matrice de liens), au J4 (title/meta)
- **Le skill `indexation-check`** : il n'est PAS dans le pack des 9 de la S1. Vous avez reçu 2 versions ce week-end, terminal (Claude Code) ou Cowork (sans terminal). Installez UNE SEULE des deux selon votre setup, pas les deux.

Checklist pré-audit :
1. Export GSC en CSV, 3-6 derniers mois, **toutes les requêtes ET toutes les pages**. Un seul export, il sert toute la semaine, surtout le J2.
2. Chrome + extension connectée et testée
3. URL du site + son **sitemap.xml** accessible (liste complète des URLs, on en a besoin au J3)
4. Vos 5-10 requêtes business principales

Puis les deux phases les plus légères :

**Positionnement** (prompt seul) : collez l'export GSC + vos requêtes business. Claude sort le tableau position / impressions / CTR / gap / type SERP + vos gaps + opportunités cachées.

**Indexation** (`indexation-check`) : sur le sitemap + vos URLs, 9 points vérifiés. Logique : une page non indexée ne sera jamais un quick win, on la repère AVANT. ⚠️ « non indexée » ≠ « non testable ».

Livrable : checklist verte + tableau de positionnement + rapport d'indexation. Stocké dans `audit/`.

GSC / Chrome / skill qui coince ? MP aujourd'hui, pas vendredi.

---

## Jour 2 — Cannibalisation + Maillage GSC

Salut à tous,

Jour 2. La photo est posée hier, aujourd'hui on attaque le diagnostic le plus rentable de la semaine. Un seul export GSC, deux lectures. Doc dédié sur le Drive : [[skill-maillage-gsc-cannibalisation]], gardez-le ouvert, toute la pédagogie de la journée est dedans.

L'ordre n'est pas négociable : **cannibalisation d'abord, maillage ensuite**. La cannibalisation lit l'export par requête (quelles requêtes déclenchent 2+ URLs), le maillage lit le même export par page (qui mérite d'être mère, qui est sous-maillée). Si vous maillez avant d'avoir trié les conflits, vous bétonnez le problème.

**Cannibalisation** (`seo-cannibalisation`) :
- Pré-condition : moins de 10 URLs dans votre GSC → on skip, on documente un diagnostic de « sous-granularité » (constat valide, pas un échec), et on passe direct au maillage.
- Sinon : détection des conflits (type A mot-clé / B intention / C proximité / Triade SERP). Puis via Chrome on ouvre **les 2 URLs en conflit** et on tranche la root cause. Si les H1/H2 des deux pages se chevauchent → problème de **contenu** (différenciation ou fusion). Si les Hn sont distincts mais Google hésite quand même → problème de **maillage** (ni 301 ni fusion, ça part dans le plan de maillage juste après).

⚠️ La root cause se décide ici, sur les 2 pages ouvertes dans Chrome, pas sur l'audit Hn complet (lui, c'est demain, J3, sur tout le sitemap). L'audit Hn de demain **confirmera à l'échelle** vos verdicts d'aujourd'hui. Si une page se révèle hors-sujet au J3, on rouvre le conflit. Vos calls root-cause du J2 sont **provisoires jusqu'au J3**, ne fusionnez rien définitivement aujourd'hui.

**Maillage GSC** (`maillage-interne-gsc`) : sur le même export, hiérarchie mère/fille/petite-fille, pages fortes en impressions mais sous-linkées, règles Know→Do. Chaque cannibalisation classée « root cause = maillage » entre ici comme action : on désigne la mère (la transactionnelle / business), on coupe les liens qui nourrissaient la mauvaise page, on draine le cluster vers la mère avec une ancre qui porte l'intention Do. Triade SERP : on ne fusionne pas les flux, ancres distinctes vers chaque URL.

Livrable : cannibalisations (type + root cause) + plan de maillage data, avec chaque conflit « maillage » résolu par une action tranchée. Une cannibalisation « maillage » sans sa contrepartie dans le plan = livrable incomplet. Stocké dans `audit/`.

Demain, le structurel : Hn + maillage structurel 💪

---

## Jour 3 — Audit structurel Hn + Maillage structurel

Salut à tous,

Jour 3. Hier on a posé le diagnostic data. Aujourd'hui on regarde la structure, sans GSC : la structure des pages (les Hn) et la structure des liens (le graphe interne). Les deux croisent les conflits d'hier.

**Audit structurel Hn** (scrap, pas de skill, c'est dans le doc workflow) : scan Hn de tout le sitemap (pas un échantillon de 50, le périmètre suit votre site). Pour chaque page, 8 contrôles : H1 unique et présent, hiérarchie sans saut de niveau, H1 qui matche l'intention, H2 qui couvrent les requêtes GSC position 4-20, Hn génériques bannis (« Introduction », « Conclusion »), sur-optimisation, Passage Ranking, pages sans structure.

→ **Croisement cannibalisation J2** : cet audit confirme à l'échelle vos verdicts root-cause d'hier. Deux pages d'un conflit dont les H1/H2 se chevauchent réellement = c'était bien du contenu. Hn distincts confirmés = c'était bien du maillage, le plan du J2 tient. Si un verdict tombe, on rouvre le conflit du J2.

**Maillage structurel** (`maillage-systeme`) : la passe qui raisonne sur l'architecture éditoriale, sans GSC. Via Chrome, matrice des liens internes → orphelines, sur-linkées, pages stratégiques sous-linkées, ancres pourries. Puis piliers (≥10 liens entrants ?), hub/satellite, dead-end, diversification des ancres. À croiser avec le J2 : une page forte GSC repérée sous-maillée hier + orpheline ici = priorité absolue. Les conflits « root cause = maillage » du J2 se résolvent structurellement ici.

⚠️ **Le point de charge variable de la semaine.** Le périmètre Hn suit le sitemap, pas un cap à 50. Terminal : illimité, gratuit, tapez tout. **Cowork** : si le sitemap est gros, priorisez le scrap, d'abord les pages avec impressions GSC + les position 4-20 + les pages impliquées dans un conflit du J2, le reste si le budget tokens le permet. On ne tape pas 800 URLs à l'aveugle dans Chrome. Si ça déborde, finissez le scan demain (le J4 est plus léger côté Hn).

Livrable : tableau Hn par URL (verdict + anomalies critiques en tête) + audit du graphe interne (piliers, orphelines, dead-end, ancres). Stocké dans `audit/`.

Demain : quick wins + le rapport final.

---

## Jour 4 — Quick Wins + Synthèse

Salut à tous,

Jour 4. Tout le diagnostic est posé. Aujourd'hui on sort les gains rapides, puis on consolide tout en un seul plan.

**Quick Wins** (`seo-quick-win`) :
- 2A : pages position 3-12, grosses impressions, CTR au sol → impact estimé en clics
- 2B : title/meta vs requêtes GSC. Bonne nouvelle, le scrap Chrome et l'audit Hn d'hier (J3) couvrent déjà ces pages, on réutilise, pas besoin de re-scraper. On compare title/meta aux requêtes et on sort la reco.
- 2C : présence locale (fiche GBP oui/non)

→ **Croisement Hn J3** : une page quick win dont le seul vrai problème est le Hn (déjà diagnostiqué hier) = quick win structurel, effort faible, impact rapide. Notez-les en tête.

**Synthèse** (Claude, prompt) : collez les synthèses de tous les jours (positionnement, indexation, cannibalisation, maillage data, Hn, maillage structurel). Claude génère le **plan d'action 3 horizons** :
- Semaine 1-2 : impact immédiat → déblocage indexation, title/meta, corrections Hn rapides, liens, cannibalisation tranchée, GBP
- Mois 1 : fondations → optimisation pages, réécriture des Hn hors-sujet, restructuration maillage en piliers
- Mois 2-3 : croissance → nouvelles pages sur les gaps du J1, outils

Livrable : top quick wins chiffrés + **le plan d'action 3 horizons**, format exécutif (synthèse en tête, critiques d'abord, plan priorisé). C'est ÇA le rapport qui fait signer, et c'est ÇA qu'on amène au call.

À demain pour le call 🙌

---

## Jour 5 — Call collectif

Salut à tous,

Jour 5 🎉 call à 10h00.

Ce que vous amenez :
- Votre audit complet (tous les jours) + le plan d'action 3 horizons sur un vrai site, au format client
- Les 3 actions que vous lanceriez dès demain matin si c'était votre client
- **1 question concrète** sur laquelle vous bloquez

Format du call :
- Tour de table express (1 min / personne) : site audité + le quick win n°1 trouvé
- Revue en live de 2-3 audits représentatifs
- **Démo : comment je trouve des mots-clés anti-ChatGPT.** Votre plan a un horizon « Mois 2-3 : nouvelles pages sur les gaps ». La vraie question : on crée quoi, sans pondre une page que ChatGPT mangera demain ? Je déroule en live, sur un cas réel, le passage du mot-clé large mangé par GPT au mot-clé décisionnel ultra-niché, et d'où viennent ces mots-clés (calls clients, SAV, archives), pas les outils du marché ni les PAA. Ces mots-clés repartent dans le moteur de rédaction de la S2.
- Q&R libre

L'audit n'est pas un livrable pour faire joli. C'est ce qui fait signer un client, et ce qui dit à votre moteur de contenu exactement où tirer.

À tout à l'heure 🙌

---

## Skills additionnels — Workflow mots-clés (autour du call J5)

Trois skills **hors workflow audit**, distribués avec la S3 parce qu'ils outillent ce qui se passe au call J5 et juste après. Pas l'audit lui-même.

Au J5 je démo les « mots-clés anti-ChatGPT », et le plan d'action sort un horizon « Mois 2-3 : nouvelles pages sur les gaps ». La question que tout le monde se pose à ce moment : on crée quoi, concrètement ? Ces trois skills sont la réponse outillée. Ils s'enchaînent.

1. `seo-recherche-mots-cles` : thématique → liste de mots-clés qualifiée (intention + volume + difficulté).
2. `seo-clustering-mots-cles` : la liste → clusters, 1 cluster = 1 page.
3. `seo-mots-cles-decisionnels` : les clusters → les requêtes qui convertissent vraiment.

La sortie repart dans `article-engine-pipeline` de la S2. L'audit recharge le moteur de contenu, ces trois skills disent où tirer.

Doc dédié sur le Drive : [[skill-workflow-mots-cles]]. Optionnels pour boucler l'audit J1-J4. Mais ce sont eux qui transforment l'horizon « Mois 2-3 » en backlog concret. Installe-les avant le call si tu veux suivre la démo en live.

---

## Notes pour Tim (interne)

- **Réordonnancement S3 acté (mai 2026).** Ancienne grille : J2 quick wins+Hn, J3 cannibalisation, J4 maillage+synthèse. Nouvelle : J2 cannibalisation+maillage GSC (bundle [[skill-maillage-gsc-cannibalisation]]), J3 Hn+maillage structurel, J4 quick wins+synthèse. Logique : grouper par **source** (data GSC au J2, structurel au J3), pas par numéro de phase. Le doc workflow [[workflow-audit-bootcamp4]] reste le squelette mais son ordre de phases ne suit plus l'ordre des jours, à re-cadrer dans le doc Drive (action ouverte).
- **⚠️ Tension d'ordre J2/J3 à marteler au cadrage.** Ancienne grille : Hn (J2) précédait cannibalisation (J3), le croisement Hn était déjà fait. Là c'est inversé : la cannibalisation (J2) décide la root cause AVANT l'audit Hn complet (J3). Résolution retenue : au J2 la root cause se tranche sur les 2 pages ouvertes dans Chrome (check manuel léger, c'était déjà le geste de l'ancien J3 cannibalisation), le J3 confirme à l'échelle. Calls root-cause du J2 explicitement « provisoires jusqu'au J3 ». À marteler au J2 sinon certains fusionneront sur un verdict non confirmé.
- **Statut pack des skills.** `seo-cannibalisation` = pack des 9 (#3, vérif/re-bundle). `maillage-interne-gsc` = hors pack, vraie install J2. `maillage-systeme` = pack #4, re-bundle J3 pour dossier autonome (cf. [[skill-maillage-systeme]]). `indexation-check` = hors pack, double variante terminal/Cowork, une seule. `seo-quick-win` = pack #2. Hors pack à distribuer Drive avant lundi : `maillage-interne-gsc`, `indexation-check` (bonne variante), + re-bundles `maillage-systeme` et `seo-cannibalisation`. Message WhatsApp week-end dédié sinon ça bloque dès le J2.
- **Le bundle J2** [[skill-maillage-gsc-cannibalisation]] contient déjà la pédagogie complète (un export deux lectures, ordre, Triade SERP, cas plombier) + les 2 SKILL.md nettoyés. C'est le doc Drive du J2, pas besoin d'en refaire un.
- **✅ `indexation-check` double variante prête.** Terminal `curl` [[skill-indexation-check]], Cowork [[skill-indexation-check-cowork]]. 7/9 checks identiques, 2 dégradés en « non testable », check #8 renforcé via croisement GSC. Une seule par participant, J1 inchangé.
- **Friction Chrome** (J2 ouverture URLs conflit, J3 scrap Hn + matrice liens, J4 title/meta). Le groupe n'a jamais touché ça en S1/S2, ~30-40 % novices techniques ([[observations-whatsapp-bootcamp]]). Installer/connecter au J1. Sonnet pour le scrap, Opus pour l'analyse.
- **⚠️ J3 = nouveau point de charge variable** (avant c'était le J2). Hn périmètre = sitemap, pas de cap. Terminal illimité gratuit. Cowork lourd : prioriser via impressions GSC + position 4-20 + pages d'un conflit J2. Si gros sitemap, le scan déborde sur le J4 (volontairement plus léger côté Hn). À cadrer au J3.
- **Pré-condition cannibalisation (<10 URLs → skip)** désormais au J2. Diagnostic « sous-granularité » = livrable valide, désamorce la frustration des petits sites, on enchaîne direct sur le maillage data du J2.
- **Le vrai livrable commercial = la Synthèse J4** (plan 3 horizons), format exécutif. Pas les sorties de skill en vrac.
- **Boucle S2 ↔ S3** : plus de phase briefs (retirée). Le lien se fait au call, les mots-clés anti-ChatGPT + l'horizon « Mois 2-3 » repartent dans `article-engine-pipeline` de la S2. L'audit recharge le moteur de contenu, il ne finit pas en PDF mort (répond au doute « je refais ce que je faisais déjà », observations §9).
- **Démo impérative au call : mots-clés anti-ChatGPT** ([[session-3-audit-prep]] TODO). Cas réel, « plombier Paris → plombier urgence douche italienne nuit 15e », source = calls / SAV / archives. Montrer la sortie terminal/Obsidian comme en S2 en prévenant que ça ne ressemble pas à Claude.
- **Skills additionnels mots-clés ajoutés (S3).** `seo-recherche-mots-cles` + `seo-clustering-mots-cles` + `seo-mots-cles-decisionnels`, bundle [[skill-workflow-mots-cles]]. Hors workflow audit : ils outillent la démo J5 et l'horizon « Mois 2-3 ». Les 3 sont neufs (commit `a9b4eae`, mai 2026), hors pack des 9. Distribution Drive : à ajouter au message week-end comme bonus, « install si tu veux suivre la démo », pas comme prérequis bloquant. Le J1-J4 n'en a pas besoin, ne pas alourdir un week-end déjà chargé en installs.
- **Questions de fond à intégrer au cadrage** (carry-over S2) : Cécile (web inaccessible aux artisans → l'audit + l'anti-ChatGPT sont la réponse), Juliette (architecture hubs/piliers → le maillage structurel J3 est le moment naturel pour y revenir).
- **Replay / résumé** : fournir le Google Doc résumé S2 + transcript/replay (Anne l'a redemandé) avant le call S3.
- **À garder en MP, pas en plénière** : README par client (1V1 Jamel), mise à jour des skills.
- **Normalisation appliquée à ce doc** : em-dashes retirés (règle maison contenu Organikk), « SEMRush » → « outils du marché » dans la démo call (règle pas de nom d'outil concurrent publié). Le fond et l'ordre des jours = nouvelle grille validée.
