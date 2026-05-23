---
title: Séquençage Semaine 4 — Automatisations puis prospection
bootcamp: 4
semaine: 4
theme: on automatise le site (balisage, veille, publication) avant d'automatiser l'acquisition (prospection IA)
related:
  - "[[sequencage-semaine-3]]"
  - "[[skill-donnees-structurees]]"
  - "[[skill-maillage-systeme]]"
  - "[[session-2-redaction-resume-participants]]"
  - "[[session-2-redaction-debrief]]"
  - "[[observations-whatsapp-bootcamp]]"
source-workflow: "S4 = automatisations + prospection (cf. [[session-2-redaction-resume-participants]] L271). Séquençage créé mai 2026, grille validée : automatisations site J1-J3, prospection J4."
---

# Séquençage Semaine 4 — Bootcamp 4

**Logique de la semaine** : trois semaines de production derrière nous (mots-clés, rédaction, audit). Cette semaine on arrête de faire à la main ce qui peut tourner tout seul. On automatise le site d'abord (le balisage, la veille thématique, la publication), puis on automatise l'acquisition (la prospection IA). Une brique par jour, chacune utilisable seule, chacune installée chez vous, pas une démo qu'on regarde.

Pourquoi cet ordre : on ne lance pas la prospection avant que la machine de contenu soit autonome. Si tu signes un client et que ton site ne se balise pas seul, ne se nourrit pas seul, tu retombes dans le redémarrage perpétuel qu'on a passé trois semaines à tuer.

**Le squelette** : pas un workflow unique cette fois, quatre automatisations indépendantes. Chacune a son doc sur le Drive.

| Jour | Contenu | Skill / outil | Livrable |
|------|---------|---------------|----------|
| 1 | Données structurées (balisage auto) | `seo-donnees-structurees` (bundle) | Balisage qui se génère depuis le contenu, validé Rich Results |
| 2 | Automatisation revue de presse sur la thématique du client | skill projet `revue-presse-quotidienne` adapté | Une veille auto qui sort un chiffre sourcé pour les pages du client |
| 3 | Connexion site auto (WordPress, pipeline de publication) | tuto Romain + MCP WordPress | Le contenu validé part sur le site sans copier-coller |
| 4 | Prospection IA | système Anthony (à cadrer) | Une séquence de prospection qui tourne sur vos cibles |
| 5 | Call (10h00) | revue 2-3 setups + démo | "Le système qui bosse pendant que tu dors" |

Budget : 2,5-4h sur la semaine (le J3 dépend du CMS du client).

---

## Jour 1 — Données structurées (le balisage qui se génère tout seul)

Salut à tous,

Semaine 4, on bascule sur les automatisations. Premier module : les données structurées, le JSON-LD. Pas le balisage à la main case par case. Le balisage qui se génère depuis le contenu et qui se corrige tout seul quand le contenu change.

Le skill `seo-donnees-structurees` est HORS pack des 9, vraie nouvelle install, deux fichiers. Tout est dans le doc dédié sur le Drive : [[skill-donnees-structurees]], gardez-le ouvert, la pédagogie et le code y sont.

Les 3 règles, à retenir même si vous ne touchez pas le code :
- Source unique : tout le balisage sort d'un seul fichier, jamais écrit en dur dans une page
- Une entité référencée une fois : la marque et l'auteur déclarés une seule fois pour tout le site, chaque page pointe dessus. Google recolle et comprend une seule entité. C'est ça qui vous fait exister dans son knowledge graph
- Le schema se déduit du contenu, jamais saisi : une FAQ sur la page génère le FAQPage seule, une vidéo le VideoObject, un H2 d'étapes le HowTo

⚠️ Le piège : on n'invente jamais un signal. Pas de FAQPage si pas de FAQ visible, pas de note ou de prix invérifiable. Un faux signal structuré, Google le voit et dégrade la page.

⚠️ Site WordPress ou no-code (beaucoup d'entre vous) : vous n'appliquez pas le code Next.js, mais les 3 règles restent obligatoires, via la config du thème ou un plugin schema. Le code est optionnel, les 3 règles ne le sont pas. Si vous êtes dans ce cas, MP aujourd'hui, on cadre votre version sans terminal, on ne perd personne là-dessus.

Livrable : le balisage du site du client se génère depuis le contenu et passe le test Rich Results de Google sans erreur.

Install ou WordPress qui coince ? MP aujourd'hui, pas vendredi.

---

## Jour 2 — Automatisation revue de presse sur la thématique du client

Salut à tous,

Jour 2. Hier le balisage se génère seul. Aujourd'hui c'est la veille qui tourne seule. On adapte l'automatisation revue de presse à la thématique de votre client : tous les jours, une étude ou un chiffre sourcé sur sa niche, prêt à alimenter ses pages.

Pourquoi : la fraîcheur est un signal. Une page qui s'appuie sur un chiffre de la semaine, sourcé, bat une page figée. Et ça nourrit le surprise score sans que vous passiez vos journées à scraper.

Le principe : le skill projet `revue-presse-quotidienne` (celui qui fait tourner ma newsletter Algorithme) se rebranche sur la thématique du client. Il scrape les sources de la niche, en sort un résumé daté avec le lien source, stocké pour que Claude le réinjecte en rédaction.

⚠️ On ne publie pas la veille brute. Elle alimente, elle ne remplace pas. Le chiffre sort dans une page seulement s'il est sourcé et vérifiable, sinon il dégrade la note (même règle qu'au fact-check de la S2).

Livrable : une automatisation qui sort chaque jour un chiffre sourcé exploitable sur les pages du client.

---

## Jour 3 — Connexion site auto (WordPress, pipeline de publication)

Salut à tous,

Jour 3. Le contenu est produit, validé, scoré. Reste le geste idiot qu'on fait encore à la main : le copier-coller dans le CMS. Aujourd'hui on coupe ça.

La plupart de vos clients sont sur WordPress. On branche la publication : le contenu validé part sur le site sans repasser par le copier-coller, avec ses titres, son balisage, ses images.

On s'appuie sur le tuto et le plugin de Romain (merci Romain), plus le plugin officiel côté WordPress. Romain fait une démo en direct aujourd'hui.

⚠️ C'est le point technique le plus variable de la semaine. Connexion au CMS, droits, plugin : ça dépend du site du client. Si le client n'est pas sur WordPress ou que l'accès n'est pas dispo, on cadre une alternative (export propre prêt à coller, ou connexion sur l'autre CMS). On ne bloque personne, on documente le cas et on avance.

Livrable : un contenu validé qui arrive sur le site cible sans copier-coller manuel.

---

## Jour 4 — Prospection IA

Salut à tous,

Jour 4. Le site est autonome (balisage, veille, publication). Maintenant on automatise ce qui fait vivre l'activité : trouver et toucher les bons clients.

Anthony présente son système de prospection IA. L'idée : arrêter la prospection au doigt mouillé, brancher un système qui cible, qui prépare l'approche avec votre data, et qui tourne pendant que vous bossez le SEO.

⚠️ La prospection automatisée, ce n'est pas du spam de masse. On vise juste, on personnalise avec de la vraie data sur la cible, sinon ça brûle votre nom. Le système sert votre réflexion, il ne la remplace pas, exactement comme pour le contenu.

Livrable : une séquence de prospection cadrée qui tourne sur vos cibles réelles.

À demain pour le call 🙌

---

## Jour 5 — Call collectif

Salut à tous,

Jour 5 🎉 call à 10h00.

Ce que vous amenez :
- Vos automatisations installées (balisage, veille, publication) sur un vrai site, plus votre setup prospection
- Le geste manuel que vous avez tué cette semaine, et le temps que ça vous rend
- **1 question concrète** sur laquelle vous bloquez

Format du call :
- Tour de table express (1 min / personne) : quelle automatisation tourne déjà chez vous
- Revue en live de 2-3 setups représentatifs
- **Démo : le système qui bosse pendant que tu dors.** On déroule en live l'enchaînement complet sur un cas réel : la veille sort un chiffre le matin, il alimente une page, la page se balise seule, elle part sur le site, et la prospection tourne en parallèle. C'est ça qu'on vend, pas des heures.
- Q&R libre

Quatre semaines, c'est bouclé. Vous n'avez plus un workflow, vous avez un système. La différence : un workflow vous fait gagner du temps, un système vous fait gagner des clients pendant que vous dormez.

À tout à l'heure 🙌

---

## Notes pour Tim (interne)

- **Séquençage S4 créé from scratch (mai 2026).** Il n'existait aucun `sequencage-semaine-4`. Grille validée : automatisations site J1-J3, prospection J4, call J5 (modèle S3). Thème confirmé par [[session-2-redaction-resume-participants]] L271 ("on bascule sur les automatisations et la prospection en S4").
- **⚠️ À ne pas oublier (rappel Tim 2026-05-23) :** caser le **skill sémantique** (`seo-preparation-semantique` ou `seo-entites-vectorielles`, à trancher) **en plus** du reste, et confirmer les **données structurées** (déjà au J1). Le skill sémantique n'est pas encore placé dans la grille J1-J5 — soit on l'insère en module bonus, soit on le branche en amont de la rédaction (boucle S2 ↔ S4), soit on bascule un autre jour. À cadrer avant d'envoyer les messages WhatsApp.
- **J1 = bundle déjà prêt** [[skill-donnees-structurees]] (skill + code verbatim + pédagogie). Rien à refaire pour le J1.
- **J2 à confirmer.** Le skill projet `revue-presse-quotidienne` existe (GH Action, fait tourner Algorithme, cf. [[skill-donnees-structurees]] note + archi ia-employe). Mais "le rebrancher sur la thématique d'un client" n'est pas documenté en pas-à-pas. Action : produire un bundle J2 (comme le J1) avec la procédure d'adaptation client, sinon le J2 est creux. Pas encore fait.
- **J3 dépend de Romain.** Le module s'appuie sur son plugin WordPress + tuto (romainfillatre.fr) et le plugin officiel `enable-abilities-for-mcp` / `github.com/WordPress/mcp-adapter` ([[observations-whatsapp-bootcamp]] L78-79). Démo Romain "possible" mentionnée, pas confirmée. Action : caler la démo avec Romain AVANT le J3, sinon basculer en module dirigé par toi. Risque si Romain indispo.
- **J4 = trou réel.** Anthony a "proposé son système de prospection IA pour S4" ([[observations-whatsapp-bootcamp]] L142), mais je n'ai aucun détail de ce système, aucun skill associé. Le J4 est écrit au niveau principe seulement, volontairement. Action obligatoire : cadrer le contenu réel avec Anthony, ou le remplacer par un module prospection à toi. Ne pas distribuer le J4 tel quel sans ce cadrage.
- **⚠️ Risque audience technique** ([[session-2-redaction-debrief]] L234 : "ne pas perdre la moitié du groupe en S4 sur Obsidian/technique"). J1 (Next.js) et J3 (WordPress/MCP) sont les plus durs. Garde-fous mis : J1 a la section WordPress/no-code + renvoi MP ; J3 a l'alternative no-WordPress. À marteler chaque jour : le code est optionnel, le principe est obligatoire.
- **Livrables S4 ≠ S3.** Pas d'`audit/`, ce sont des automatisations installées et qui tournent. Le "format qui fait signer" de la S3 devient ici "le système qui tourne sans toi".
- **Boucle S2 ↔ S4.** Le J2 (veille auto) referme la boucle : la revue de presse client réalimente `article-engine-pipeline` de la S2. À expliciter au call.
- **Normalisation.** Doc sans em-dashes (règle maison). Messages WhatsApp prêts à coller. Tableau J1-J5 à figer une fois J2/J3/J4 confirmés (Romain, Anthony, bundle revue-presse client).
