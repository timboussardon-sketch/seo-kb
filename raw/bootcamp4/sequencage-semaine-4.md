---
title: Séquençage Semaine 4 — Préparer, rendre parfait, planifier, vendre
bootcamp: 4
semaine: 4
theme: "4 skills : préparation sémantique → balisage auto → perf → roadmap client. De la matière d'une page jusqu'au plan de prod qu'on vend au client."
related:
  - "[[sequencage-semaine-3]]"
  - "[[skill-preparation-semantique]]"
  - "[[skill-donnees-structurees]]"
  - "[[skill-core-web-vitals]]"
  - "[[skill-roadmap-pseo]]"
  - "[[skills-checklist-bootcamp4]]"
  - "[[session-2-redaction-resume-participants]]"
  - "[[observations-whatsapp-bootcamp]]"
source-workflow: "S4 recentrée sur 4 skills (2026-05-28) : préparation sémantique, données structurées, Core Web Vitals, roadmap client. Bascule depuis le plan automatisations/prospection précédent (conservé en annexe)."
---

# Séquençage Semaine 4 — Bootcamp 4

**Logique de la semaine** : trois semaines de production derrière nous (mots-clés, rédaction, audit). Cette semaine on outille les deux bouts qui manquaient : ce qui se passe AVANT d'écrire une page (la matière sémantique), ce qui rend une page techniquement irréprochable (balisage + perf), et ce qui transforme tout ça en plan de production qu'on vend à un client (la roadmap).

Quatre skills, quatre jours, chacun utilisable seul, chacun installé chez toi, pas une démo qu'on regarde. Le J5 on déroule en live.

**Pourquoi cet ordre** : on part de la matière première d'une page (sémantique), on passe à ce qui la rend parfaite techniquement (balisage puis perf), et on finit sur le skill qui te fait gagner des clients (la roadmap commerciale). La semaine monte vers le business, elle ne s'éparpille pas dans la technique.

**Le squelette** : pas un workflow unique cette fois, quatre skills indépendants. Chacun a son bundle sur le Drive, prêt à copier-coller.

| Jour | Contenu | Skill | Livrable |
|------|---------|-------|----------|
| 1 | Préparation sémantique (ce que ta page doit contenir) | `seo-preparation-semantique` | La carte sémantique d'une page cible, prête à alimenter le brief |
| 2 | Données structurées (le balisage qui se génère seul) | `seo-donnees-structurees` | Balisage JSON-LD validé Rich Results sur une page client |
| 3 | Core Web Vitals (la perf qui fait ranker) | `seo-core-web-vitals` | Audit perf d'un site avec les 5 pires pages priorisées |
| 4 | Roadmap client (le plan de prod qu'on vend) | `seo-roadmap-pseo` | Une roadmap 30/60/90 présentable en RDV commercial |
| 5 | Call (10h00) | revue 2-3 setups + démo | "De la matière première au plan qu'on vend" |

Budget : 2,5-4h sur la semaine.

**Les 4 bundles sont déjà sur le Drive aujourd'hui.** Tu peux tout installer d'un coup si tu veux prendre de l'avance, ou suivre jour par jour. Les messages ci-dessous sont la trame du déroulé.

---

## Jour 1 — Préparation sémantique (ce que ta page doit contenir)

Salut à tous,

On démarre la semaine 4 par le début d'une page : sa matière sémantique. Avant d'écrire, avant même de faire le brief, il faut savoir tout ce que la page doit contenir pour ranker. C'est le rôle du skill `seo-preparation-semantique`.

Tu lui donnes une requête + un profil, il te sort les entités pondérées, le lexique signature, les pain points, les preuves chiffrées à aller chercher, la gap analysis vs les concurrents, et un Surprise Score sur 100. Le tout sans scraper Google.

Pourquoi sans SERP : les outils type Surfer ou NeuronWriter te disent "mets ces mots parce que tes concurrents les ont". Tu écris la même page que tout le monde, l'AI Overview te résume en trois phrases, terminé. Ce skill fait l'inverse : il te donne la carte attendue ET ta divergence, ce que tu dis que personne d'autre ne dit. C'est ça qui te fait citer.

Deux modes :
- Création : une requête + un profil → la carte d'une page à écrire
- Audit : tu colles en plus un contenu existant → le diff entre ce que ta page couvre et la carte attendue, avec plan de correction

⚠️ Le cosinus et le Surprise Score sont simulés (projection corpus Claude), pas calculés par une API d'embeddings. Le skill le marque lui-même. Ne vends pas ces chiffres comme une mesure exacte à un client : c'est une estimation pour prioriser.

⚠️ Ce skill ne rédige pas. Il sort la matière. La structure Hn, c'est `seo-brief-contenu`. L'article, c'est `article-engine-pipeline`.

Bundle complet (pédagogie + bloc à coller) : [[skill-preparation-semantique]].

Livrable : la carte sémantique d'une requête de ton client, prête à alimenter un brief.

Install ou déclenchement qui coince ? MP aujourd'hui, pas vendredi.

---

## Jour 2 — Données structurées (le balisage qui se génère tout seul)

Salut à tous,

Jour 2. Hier tu sais ce que ta page doit contenir. Aujourd'hui on s'occupe de comment Google la comprend : le balisage, le JSON-LD, schema.org. Pas le balisage à la main case par case. Le balisage qui se génère depuis le contenu et qui se corrige tout seul quand le contenu change.

Le skill `seo-donnees-structurees`. Les 3 règles, à retenir même si tu ne touches pas le code :
- Source unique : tout le balisage sort d'un seul fichier, jamais écrit en dur dans une page
- Une entité référencée une fois : la marque et l'auteur déclarés une seule fois pour tout le site, chaque page pointe dessus. Google recolle et comprend une seule entité. C'est ça qui te fait exister dans son knowledge graph
- Le schema se déduit du contenu, jamais saisi : une FAQ génère le FAQPage seule, une vidéo le VideoObject, un H2 d'étapes le HowTo

⚠️ Le piège : on n'invente jamais un signal. Pas de FAQPage si pas de FAQ visible, pas de note ou de prix invérifiable. Un faux signal structuré, Google le voit et dégrade la page.

⚠️ Site WordPress ou no-code (beaucoup d'entre vous) : tu n'appliques pas le code Next.js, mais les 3 règles restent obligatoires, via la config du thème ou un plugin schema. Le code est optionnel, les 3 règles ne le sont pas. Si tu es dans ce cas, MP aujourd'hui, on cadre ta version sans terminal.

Bundle complet : [[skill-donnees-structurees]].

Livrable : le balisage du site d'un client se génère depuis le contenu et passe le test Rich Results de Google sans erreur.

---

## Jour 3 — Core Web Vitals (la perf qui fait ranker)

Salut à tous,

Jour 3. La page est balisée, Google la comprend. Reste à savoir si elle est rapide, parce que la perf mobile est un facteur de ranking direct. Aujourd'hui on audite la performance d'un site complet avec `seo-core-web-vitals`.

Le skill crawle ton sitemap, passe Lighthouse mobile sur 50 pages en parallèle, et sort un rapport avec les 5 pires URLs à corriger en priorité, le LCP element identifié page par page, et le breakdown qui dit où le temps part. Pas un score PageSpeed copié-collé, un vrai diagnostic exploitable.

Pourquoi c'est rentable chez un client : tu poses un baseline en début de mission, tu corriges les 5 pires, tu re-mesures la semaine d'après, tu prouves le gain en chiffres. PageSpeed cliqué URL par URL sur 50 pages, oublie, ça prend des jours.

⚠️ Skill terminal uniquement. Il requiert Lighthouse en CLI (`npm install -g lighthouse`) et `jq` (`brew install jq`). Si tu es sur Cowork pur sans terminal, tu ne peux pas le lancer tel quel. Pas grave : tu prends le rapport PageSpeed Insights public en attendant, ou tu fais l'audit perf depuis une machine avec terminal. MP si tu veux qu'on pose Node ensemble.

⚠️ Les 3 règles : mobile uniquement (Google indexe mobile-first), pas de score halluciné (URL qui crash = marquée ERROR, jamais un faux 0), pas de reco sans opportunity Lighthouse correspondante.

Bundle complet : [[skill-core-web-vitals]].

Livrable : l'audit perf d'un site client avec les 5 pires pages et leur plan de correction.

---

## Jour 4 — Roadmap client (le plan de prod qu'on vend)

Salut à tous,

Jour 4. Tu sais préparer une page, la baliser, la rendre rapide. Aujourd'hui on assemble tout ça en un plan de production sur 90 jours que tu présentes à un client. C'est le skill qui transforme ton expertise en proposition commerciale : `seo-roadmap-pseo`.

Tu lui donnes une thématique (ou une liste de mots-clés) + la Money Page du client, il sort un calendrier 30/60/90 découpé en deux phases :
- Phase 1 — transactionnel et décisionnel d'abord. Les pages qui convertissent, celles qui paient le SEO dès le premier mois. C'est ça qui justifie le budget au client.
- Phase 2 — informationnel bas de funnel ensuite. Les pages proches de la décision qui alimentent Phase 1 par maillage. Jamais d'informationnel pur : ça se fait manger par ChatGPT, c'est de l'effort gratuit.

L'ordre n'est pas négociable. Si tu commences par l'informationnel, tu fabriques de l'autorité que tu ne monétises pas et le client ne voit pas de retour.

Pourquoi c'est ton meilleur argument de vente : la sortie a une section "mots-clés rejetés" qui explique au client pourquoi tu ne produis PAS certaines pages. Ça prouve que tu ne factures pas du volume au kilo, que tu protèges son budget contre les pages que l'IA va dévorer. C'est ton anti-agence-qui-pond-200-articles.

⚠️ Pas de roadmap sans Money Page. Si le client ne sait pas où il convertit, le skill bloque et te le fait poser. Un planning sans point de conversion, c'est de l'effort gratuit.

⚠️ Pas de volume inventé. Si tu ne donnes pas la data GSC/Ahrefs, le skill met `[À SOURCER]`. Ne présente jamais une roadmap avec des volumes inventés à un client.

Bundle complet : [[skill-roadmap-pseo]].

Livrable : une roadmap 30/60/90 sur un cas client réel, présentable telle quelle en RDV de découverte.

À demain pour le call 🙌

---

## Jour 5 — Call collectif

Salut à tous,

Jour 5 🎉 call à 10h00.

Ce que tu amènes :
- Tes 4 skills installés et testés sur un cas réel
- Au moins une carte sémantique, un audit perf OU une roadmap client que tu as produit cette semaine
- **1 question concrète** sur laquelle tu bloques

Format du call :
- Tour de table express (1 min / personne) : quel skill t'a le plus servi cette semaine
- Revue en live de 2-3 setups représentatifs
- **Démo : de la matière première au plan qu'on vend.** On déroule en live l'enchaînement complet sur un cas réel : la prépa sémantique sort la carte d'une page, la page se balise seule, on vérifie sa perf, et on cale le tout dans une roadmap 90 jours présentable au client.
- Q&R libre

Quatre semaines, c'est bouclé. Tu n'as plus des skills isolés, tu as une chaîne complète : trouver les mots-clés, préparer, rédiger, auditer, baliser, optimiser, et vendre le plan. C'est ça que tu factures.

À tout à l'heure 🙌

---

## Notes pour Tim (interne)

- **S4 recentrée sur 4 skills (2026-05-28).** Bascule depuis le plan "automatisations + prospection" (conservé en annexe ci-dessous). Raison de la bascule : les 4 skills (sémantique, données structurées, CWV, roadmap) sont prêts et distribuables aujourd'hui, sans dépendance externe, alors que le plan automatisations/prospection dépendait de Romain (démo WordPress jamais confirmée) et d'Anthony (système prospection = trou réel jamais cadré). On livre du concret plutôt que du "à confirmer".
- **Ordre proposé à valider.** J'ai mis sémantique (J1, la matière) → données structurées (J2) → CWV (J3) → roadmap (J4, le commercial). L'arc monte vers le business. Si tu préfères grouper le technique (données structurées + CWV en J1-J2) et mettre sémantique + roadmap autour, dis-moi, je réordonne en 2 minutes.
- **Tout est livré aujourd'hui sur le Drive.** Les 4 bundles ([[skill-preparation-semantique]], [[skill-donnees-structurees]], [[skill-core-web-vitals]], [[skill-roadmap-pseo]]) sont prêts à copier-coller. Le découpage J1-J4 est pédagogique (un message WhatsApp par jour), pas une contrainte d'install. Tu peux dire au groupe "tout est dispo, je vous déroule un skill par jour".
- **CWV terminal-only = même risque audience qu'avant.** Le J3 (Core Web Vitals) ne tourne pas sur Cowork pur. Garde-fou mis dans le message J3 (PageSpeed public en repli + renvoi MP). À marteler : c'est le seul des 4 qui exige un terminal.
- **Roadmap jamais testé en prod.** Cf. note de [[skill-roadmap-pseo]] : lance-le une fois sur un cas client avant le J4 pour valider la sortie. Si le scoring ou le phasage cloche, on corrige avant distribution.
- **Sémantique nettoyé pour distribution.** Le bundle [[skill-preparation-semantique]] retire les refs à ton vault (doc source 1245 lignes + chemin sauvegarde). Version dé-vault-isée, comme données structurées. Détail dans la note du bundle.
- **Cohérence checklist : fait.** Les 4 skills sont dans [[skills-checklist-bootcamp4]] section 4 + récap S4 mis à jour.
- **Normalisation.** Doc sans em-dashes (règle maison). Messages WhatsApp prêts à coller.

---

## Annexe — Version précédente S4 (automatisations + prospection, non retenue)

Plan initial créé en mai 2026, basculé le 2026-05-28 vers les 4 skills. Conservé ici pour mémoire (dépendances Romain / Anthony / revue-presse à réutiliser si tu remontes un module automatisation plus tard).

| Jour | Contenu | Skill / outil | Statut à la bascule |
|------|---------|---------------|---------------------|
| 1 | Données structurées | `seo-donnees-structurees` | Conservé (passé en J2 dans le nouveau plan) |
| 2 | Automatisation revue de presse sur la thématique du client | skill projet `revue-presse-quotidienne` adapté | Jamais documenté en pas-à-pas. Trou. |
| 3 | Connexion site auto (WordPress, pipeline publication) | tuto Romain + MCP WordPress | Dépendait de Romain, démo jamais confirmée |
| 4 | Prospection IA | système Anthony | Trou réel, jamais cadré avec Anthony |
| 5 | Call | revue + démo | Conservé (réorienté) |

Briques à réutiliser si module automatisation futur :
- Démo plugin WordPress de Romain (romainfillatre.fr) + plugin officiel `enable-abilities-for-mcp` / `github.com/WordPress/mcp-adapter`
- Système de prospection IA d'Anthony (à cadrer avec lui)
- `revue-presse-quotidienne` rebranché sur la thématique d'un client (referme la boucle S2 ↔ S4)
- Risque audience technique signalé en S3 debrief ([[session-2-redaction-debrief]] L234 : "ne pas perdre la moitié du groupe sur Obsidian/technique")
