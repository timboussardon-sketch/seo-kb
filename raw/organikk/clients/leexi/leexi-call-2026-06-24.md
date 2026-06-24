---
type: call-transcript
call-type: call-suivi-client
prospect: Leexi.ai
date: 2026-06-24
status: transcript-nettoye
source: speech-to-text
participants:
  - "Timothée Boussardon (consultant SEO)"
  - "Baptiste (CTO, Leexi)"
  - "Mathieu (Leexi)"
  - "Sophie (marketing, Leexi)"
tags:
  - client
  - call-suivi
  - leexi
  - saas
  - transcript
  - mots-cles
  - cocons
related:
  - "[[leexi]]"
  - "[[leexi-call-2026-05-21]]"
---

# Call #2 · Leexi.ai — session de travail (validation des axes mots-clés)

Deuxième call avec Leexi.ai, ~5 semaines après le premier. Session de travail : Tim présente le bot SEO qu'il a commencé à construire, fait valider les trois grands axes de mots-clés, et cale la suite (cocons, mise en ligne via Strapi/MCP, traduction, optimisation des pages existantes). Côté client : **Baptiste** (CTO), **Mathieu**, et **Sophie** (marketing) qui rejoint en cours de call. La diarisation n'étant pas fiable, les interventions côté client sont regroupées sous le label **Leexi**.

---

## En résumé

- **Trois axes de mots-clés validés** pour démarrer la production :
  1. **RGPD / souveraineté / sécurité** — hébergement France/Europe, souveraineté des données, ISO 27001, EU AI Act, comparatifs RGPD vs outils américains. C'est un **no-go absolu** pour une partie des clients : porte d'entrée commerciale forte.
  2. **Fonctionnalités** — la transcription est la porte d'entrée (vocabulaire grand public), mais le vrai produit c'est résumés/comptes rendus, tâches de suivi, **intégrations CRM** (une page par CRM + un hub), **intégrations Meet/Teams/Zoom** (« comment intégrer un notetaker sur Meet »), **« passer de X à Y »**, app mobile / dictaphone.
  3. **Problématiques métier** — cas d'usage par secteur (conseil, RH, BTP, managers, recrutement, bancaire). Plus de volume, moins technique, très qualifié.
- **Secteurs prioritaires** retenus : conseil, comptabilité-finance, secteur public (« technologie » jugé trop large).
- **Écartés** : enregistrement téléphonique (besoin VOIP, fonctionnalité native prévue sept-oct), traduction juridique/médicale (trop niche), chatbot/assistant (trop générique).
- **Cocons** : 3-5 mots-clés business max au total (autorité thématique), 5-15 pages par cocon (~75 pages), objectif 40-50 pages à 3 mois. Réutiliser les 6 cocons existants plutôt qu'en créer de nouveaux.
- **Mise en ligne** : CMS **Strapi** + **MCP testé et fonctionnel** par Tim. Session de config 15-20 min calée **lundi 9h**.
- **Vieux contenu** : audit de cannibalisation à venir, suppression de 30-40 % des pages hors-sujet / zéro trafic (nettoyage = signal positif), conservation de l'antériorité, optimisation des pages en position 3-10 (pas les 50e).
- **Data propriétaire** : Tim a besoin de plus que le résumé Notion — calls clients, e-mails avec objections. Le questionnaire était rempli mais un bug d'affichage l'a masqué côté Tim ; il le récupère.
- **Suite immédiate** : Tim envoie les mots-clés + cocons, attaque création/optimisation des pages lundi, rapport hebdo, prochain call dans 15 jours.

---

## Décisions et points actés

| Sujet | Décision |
|---|---|
| Secteurs cibles | Conseil, comptabilité-finance, secteur public (technologie écarté car trop large) |
| Axe 1 mots-clés | RGPD / souveraineté / sécurité — **validé** |
| Axe 2 mots-clés | Fonctionnalités (CRM, intégrations visio, X→Y, app mobile) — **validé** |
| Axe 3 mots-clés | Problématiques métier par secteur — **validé** |
| Comparatifs | OK contre outils **américains** (angle RGPD/souveraineté), pas contre acteurs français/européens |
| Nb de pages | 3-5 mots-clés business → 5-15 pages/cocon → ~75 pages ; 40-50 à 3 mois |
| Cocons | Réutiliser les 6 cocons existants, ne pas en multiplier |
| CMS | Strapi + MCP (testé OK des deux côtés) ; session config lundi 9h |
| Traduction | FR d'abord (marché principal France/Belgique), Leexi gère la trad IA via ses scripts Strapi |
| Vieux contenu | Audit cannibalisation, suppression 30-40 % hors-sujet, garder antériorité, optimiser 3-10 |
| Images | Pas d'images IA ; copies d'écran, tableaux, quiz, outils, dégradés pour miniatures |
| Cadence | Rapport hebdo + call de suivi tous les 15 jours |

---

## Cadrage : secteurs et mots-clés prioritaires

**Timothée :** Avant de commencer, deux questions. Vous avez des secteurs en particulier à attaquer ? Médical, aéronautique, autre ?

**Leexi :** C'est en bas du document, rangé par taille. Les trois qui dominent : technologie, conseil, comptabilité-finance. Il y a aussi le secteur public — les boîtes du gouvernement, la ville de Cannes, plein de communes.

**Timothée :** « Technologie », c'est trop large, c'est un peu tout le monde. Je partirais plutôt sur conseil, comptabilité-finance et secteur public. L'idée, c'est d'attaquer des modèles de pages, mais pas tous les secteurs d'un coup — trois ou quatre maximum au début, et on voit ce qui ressort.

**Timothée :** Sur les deux mots-clés prioritaires que vous aviez notés, c'est des cibles fermes ou juste des pistes ?

**Leexi :** Plutôt des pistes. Pas des mots-clés sur lesquels on veut absolument sortir.

**Timothée :** Le volume nous intéresse peu de toute façon ; ce qui compte, c'est qu'il y ait du lead derrière. Ils feront partie de la liste, on remontera dessus.

## Présentation du bot

**Timothée :** Ce que j'ai fait ces deux semaines, c'est commencer à construire votre bot. L'idée, c'est qu'il m'aide d'abord à créer de meilleures pages, puis qu'une fois la prestation terminée, une personne en interne puisse l'utiliser pour créer des pages, des newsletters, des posts. Là, on a déjà : le contenu que vous m'avez donné, le contenu que j'ai trouvé, et une branche SEO — pour que quand vous poserez des questions SEO, il y ait un vrai socle.

Autour de ça, je vais créer toute la data : des statistiques sur la prise de notes IA, des études de marché, qui viennent alimenter le bot. Cette data, vous pourrez l'utiliser dans des articles, des newsletters, et elle permet aussi au bot de sourcer ce qu'il sort (« j'ai vu cette statistique en février 2025 »). Ça donne des sources fiables pour créer des articles.

L'idée, c'est d'en faire un seul fichier en local, pour ne pas dépendre d'un modèle — on a vu ce qui se passe avec Fable. Que je sois sur GPT ou autre, je garde mon socle en local.

## Migration et redirections

**Timothée :** En première semaine, on a un peu rafraîchi le site. Il y a un petit problème de migration : 2-3 URLs qui marchaient bien sur l'ancien site et qu'il faut que je regarde. Des redirections probablement pas parfaites.

**Leexi :** L'administration a pris du temps à se mettre en place, ça a impacté notre score d'autorité. On avait quand même mis en place 100 % de redirections, normalement aucune page laissée de côté.

**Timothée :** Il faut vérifier ce que Google voit : un vrai 301, ou un faux 301 avec un 404 qui arrive avant. Ce n'est pas bloquant, ça prend du temps. Donnez-moi les trois grosses URLs de l'ancien site, je lance un audit.

## Stratégie : éviter les mots-clés « mangés » par les IA

**Timothée :** Le nom de marque est fort, mais il faut partir sur des modèles de pages qui évitent les mots-clés mangés par les IA — ceux où on demande à ChatGPT et où il n'y a pas de clic. « À quoi sert un outil de prise de notes IA » : pas de clic. « Quels sont les cinq meilleurs outils de prise de notes IA pour le secteur tech » : là, ça nous intéresse.

Et quand je dis IA, c'est en préparation de ce qui arrive sur Google. Le SEO classique, c'est encore 80-90 % du trafic, mais on ne crée pas les pages pour les trois prochains mois — on les crée pour les cinq prochaines années. L'idée : trouver des typologies de pages à attaquer sur les trois premiers mois, puis faire un premier bilan. À trois mois, on sera autour de 30 à 50 pages business. Le but, ce n'est pas de créer du slop : c'est que ces 40-50 premières pages soient parfaites — qu'elles convertissent et qu'elles rankent sur Google et les LLM.

## Axe 1 — RGPD, souveraineté, sécurité

**Timothée :** Premier axe : tout ce qui concerne « outil IA conforme RGPD », sécurité, prise de notes sécurisée. C'est un vrai sujet business pour vos clients ou pas ?

**Leexi :** Pour beaucoup de clients, c'est une priorité absolue. Sans ça, c'est un no-go direct — ça élimine beaucoup d'acteurs qui ne l'ont pas. Pas tous nos clients, mais un certain nombre, et pour eux c'est vraiment important.

**Timothée :** « Outil », c'est peut-être trop large. À part RGPD, quels autres mots ?

**Leexi :** RGPD, c'est un peu le mot fourre-tout. Mais ce qui compte aussi : hébergé en Europe, hébergé en France, et surtout la **souveraineté** — données stockées en Europe/France. C'est méga important pour cette typologie de clients. La France un peu plus, mais l'Europe ça passe.

**Timothée :** Faire des comparatifs RGPD avec les outils américains, c'est pertinent ?

**Leexi :** Très pertinent. C'est souvent la porte d'entrée : quand quelqu'un a un outil américain, on lui demande « ça ne te pose pas de problème d'envoyer toutes ces données aux États-Unis ? ». Généralement, si. On ne veut pas taper sur les concurrents français/européens, mais sur les américains, ça ne nous dérange pas de faire un vrai comparatif. Les Américains n'ont pas les mêmes contraintes : par défaut on impose des comportements de consentement qu'eux n'imposent pas.

**Leexi :** Le troisième mot, c'est sécurité. On passe beaucoup d'audits, on est certifié **ISO 27001**, nos clients nous auditent souvent. On finalise aussi NIS 2 et d'autres certifications. Et il y a l'**EU AI Act** : l'UE va le rendre obligatoire progressivement, comme le RGPD. Les Américains ne le font pas. Vraie différenciation.

## Axe 2 — Fonctionnalités

**Timothée :** La transcription, c'est la fonctionnalité la plus demandée ?

**Leexi :** C'est la porte d'entrée. Les gens pensent à ça au début, mais si tu n'as que de la transcription, ça ne sert à rien. Ce qu'il faut, ce sont de bons résumés, de bons comptes rendus, bien intégrés avec tes outils — poussés automatiquement dans le CRM, l'outil de ticketing, etc. — et des tâches de suivi créées à partir des meetings.

**Timothée :** La transcription est peut-être trop haut de funnel, mais elle reste pertinente : beaucoup de gens qui ne connaissent rien à l'IA utilisent ce mot pour parler de tout (un peu comme « RGPD » couvre souveraineté + sécurité). Les mots plus niches (EU AI Act, ISO 27001), ce sont les gens qui nous cherchent vraiment.

**Timothée :** « Réunion », « meeting », « compte rendu de réunion » : porte d'entrée majoritaire, on valide. « Traduction juridique », « traduction médicale » ?

**Leexi :** Trop niche, on risque de décevoir s'ils viennent pour ça.

**Timothée :** « Enregistrement téléphonique » pour les commerciaux ?

**Leexi :** Il faut un VOIP (Aircall, Ringover). On prévoit un truc directement sur le téléphone, mais c'est plutôt septembre-octobre. Pas prioritaire.

**Timothée :** On le garde en préparation, je passe pour l'instant.

### CRM et intégrations visio

**Timothée :** Sur l'autocomplétion CRM — remplir et pousser dans le CRM après une réunion — il y aura **une page par CRM** (Salesforce, HubSpot, Pipedrive…) plus **une page hub générale**. Un modèle de page, ça ira vite.

**Leexi :** Ça marche très bien, oui.

**Timothée :** Et les deux typologies qui marchent fort : « passer de X à Y » (d'un concurrent à Leexi) et « comment intégrer Leexi à Google Meet, Teams… ».

**Leexi :** Je pense qu'on a des articles qui marchent assez bien sur Google Meet.

**Timothée :** Vous avez des pages, mais elles ne rankent pas très bien — vous êtes sur le mot-clé « Google Meet » alors que le vrai mot-clé, c'est « comment intégrer un outil de prise de notes sur Meet ». Les trois gros : Meet, Teams, Zoom. Vous en faites d'autres que personne ne fait, donc on peut mettre du SEO dessus.

**Leexi :** Même si les gens sont sur Google (pas le plus RGPD), ils préfèrent que leurs transcripts soient stockés sur des serveurs européens — donc ils bossent avec nous.

### App mobile

**Timothée :** « App mobile / dictaphone » — app de prise de notes mobile, transcription mobile, résumé mobile. Vos clients sont plutôt PC ou mobile ?

**Leexi :** Dernière fois que j'ai regardé : ~15 000 utilisateurs mensuels sur ordi, ~5 000 sur téléphone (potentiellement les mêmes). Même en B2B, pour une réunion interne tu sors ton téléphone et tu enregistres.

**Timothée :** Bon filon à creuser. On a une app mobile, on le dit.

## Axe 3 — Problématiques métier

**Timothée :** Dernière typologie, la plus intéressante côté volume : les problématiques métier. « Comment faire une prise de notes en réunion », « comment avoir un suivi d'actions après un call ». On peut même cibler des métiers (commerciaux, etc.). Vous pouvez m'en citer 10-15-20 ?

**Leexi :** On a une page avec ~10 cas d'usage métier selon les industries. On a le cas d'usage pour le conseil, les RH, le BTP, les managers, le recrutement, le bancaire. Je peux te partager ça.

**Timothée :** Parfait. « Comment faire ceci pour les avocats », « pour les comptables » — très bien, ça passe. À confirmer au niveau de la demande.

## Cocons et autorité thématique

**Timothée :** Les axes vont permettre de remonter sur les mots-clés principaux (« outil de prise de notes IA »), mais comme vous n'êtes pas une grosse autorité et que c'est compétitif, l'intérêt pour Google c'est de vous voir bien positionné sur des mots-clés d'expertise métier. Moins de volume, mais c'est là qu'il y a du lead. Et demain, les gens ne taperont plus « outil de prise de notes » seul : ils taperont « outil de prise de notes + leur problème » ou « + leur secteur », parce que dans un LLM tu as déjà l'historique, donc il personnalise.

Je vais extraire **3 à 5 mots-clés business** que vous validerez cette semaine, et on construit les cocons autour. Mais de 0 à 3 mois, on n'attaque pas tout le cocon — on attaque les **micro-intentions** (longue traîne : prise de notes + secteur, + problématique). Un cocon, c'est 5 à 15 pages ; 5 cocons ≈ 75 pages ; objectif 40-50 à 3 mois, donc on aura quasi terminé.

**Leexi :** On a six cocons aujourd'hui. Tu en crées de nouveaux ou tu réutilises ?

**Timothée :** On réutilise ce que vous avez, on mixe avec ce que je trouve, et on ne fait ressortir que 3 à 5 mots-clés au total. Google veut que vous soyez une **entité thématique**, une autorité sur votre sujet — pas le « Leroy Merlin de la prise de notes ». Il faut absolument valider ces 3-5 mots-clés : s'il en manque un, je ne l'attaque pas dans mon plan.

## Mise en ligne : Strapi + MCP

**Timothée :** Comment on fait la mise en ligne ? Vous avez quelqu'un en interne, vous voulez le faire, ou je le fais ?

**Leexi :** On a quelqu'un en interne, il faudra une transmission. J'ai vérifié : le CMS **Strapi** a bien un MCP. J'ai déjà essayé de créer une page via le MCP, ça a marché sans problème.

**Timothée :** Alors tu le connectes à Claude en MCP, tu dis « crée cette page selon tel template » et c'est fait. J'ai testé : il a créé les metatitle, méta-descriptions, tout. Le maillage interne est un peu plus complexe (jusqu'à 1000 liens, une ancre par lien), mais le contenu est en markdown, donc un lien vers une autre page se rend directement. On peut se faire une **session de config à deux, 15-20 minutes**, pour être sûr que le MCP Strapi est bien branché.

**Timothée :** Le gros gain : un **modèle de design réplicable**. Tu changes un élément sur le modèle, ça change tes 100 pages d'un coup. Et le MCP me fait gagner 20-25 min de mise en page par article — sur 10 articles, c'est énorme. Mais on vérifie toujours derrière : ça c'est mon rôle, pas le vôtre.

## Maillage interne

**Timothée :** Le maillage interne premier niveau (« vous aimerez aussi » en fin de page), ce n'est pas suffisant. Il faut du vrai maillage sur des ancres précises **en début de page**, pas seulement en fin. Et construire le maillage autour des cocons : si tu as 15 pages par mot-clé, ça fait beaucoup de liens. J'ai un script qui le fait en automatique (mieux qu'à la main), mais je vérifie toujours. Le maillage, c'est un levier capital aujourd'hui — double intérêt : business (l'utilisateur passe d'une page utile à une autre) et sémantique (pour Google). Il faut équilibrer les deux.

## Images et contenu dynamique

**Timothée :** Pour les images, je ne fais pas d'images IA — c'est ce qui fait le plus « IA » et votre site est sombre, donc ça se voit. Je fais des copies d'écran, des petites infographies. Si vous trouvez un outil payant qui fait des images propres (~30-50 €/mois), on peut partir là-dessus. Sur les intégrations, des **copies d'écran** valent mieux que des images. Pour les miniatures, un **dégradé avec le mot qui résume l'article** fonctionne bien.

Mais l'important, c'est le **dynamisme**, pas l'image. Les gens lisent de moins en moins, ils scrappent les titres. Donc : FAQ, résumés, tableaux comparatifs, quiz, **un outil gratuit qui teste une fonctionnalité de Leexi en lien avec le thème de la page**, des captures du produit en plein milieu de l'article (utiliser l'espace pour vendre le produit plutôt que mettre une photo de quelqu'un au téléphone). On pourrait aussi **filmer une session Leexi** et la découper en shorts de 10 s pour illustrer les articles. Les pages font 500-600 mots, ce ne sont pas des guides.

## Vieux contenu, cannibalisation, optimisation

**Leexi :** Comment on gère un article déjà écrit mais moins bon, ou qui se cannibalise ? On le dégage ?

**Timothée :** Non, surtout pas — l'**antériorité** d'une page est précieuse. Si le mot-clé est intéressant pour vous et qu'il y a un peu de trafic et un intérêt sémantique, on garde et j'optimise. Avec le MCP, je peux récupérer la page et la modifier directement. Quand je dis 40-50 pages/3 mois, c'est de la **création** ; l'optimisation (un title, un ajout de texte, une FAQ basée sur des vecteurs sémantiques) ne compte pas là-dedans.

**Leexi :** Et le contenu d'il y a 4 ans, plus du tout pertinent ?

**Timothée :** Audit de cannibalisation : deux pages qui se battent sur le même mot-clé → on en supprime une. Nettoyer un site (supprimer 30-40 % du contenu hors-sujet ou à zéro trafic) fonctionne très bien aujourd'hui. La règle, c'est l'**autorité sémantique** : si un sujet est trop éloigné de « outil de prise de notes IA » (genre l'histoire du RGPD depuis 1900), ça dégage — tu ne seras jamais un expert RGPD pour Google, juste un outil de prise de notes qui fait du RGPD. On optimise les pages en position 3-10 pour les faire remonter ; on n'attaque pas les pages en 50e position.

**Timothée :** Pour rendre le contenu LLM-friendly : un petit **résumé en début de texte**, des blocs courts, du contenu **ultra dense** (le LLM n'a pas le budget de lire un texte qui brode). Sans tout casser : vos pages sont rédigées à la main, c'est bien, on les rend juste plus claires et plus denses.

## Data propriétaire : le nerf de la guerre

**Timothée :** Pour que vos futures pages soient meilleures que celles des autres acteurs, il me faut le **maximum de data propriétaire** : pas juste le Notion (qui est un résumé d'un résumé), mais des **calls clients**, des **e-mails clients avec des objections** — pour voir comment ils parlent, comment ils formulent leurs problèmes. C'est cette data qui permet de mettre, en FAQ, une objection client que les autres n'ont pas. Chaque mois, prends 15-20 min pour m'extraire 2-3 sources/articles intéressants, et éventuellement des sources d'autorité IA que vous suivez.

**Leexi :** J'avais rempli tout le questionnaire (drive), pas juste le Notion.

**Timothée :** Je ne l'ai pas vu, c'est un bug d'affichage de mon côté — je pensais que vous m'aviez donné juste le Notion. Je le récupère, c'est très intéressant.

**Timothée :** Le must : si vous créez votre propre clone (terminal + Obsidian) avec vos notes perso, on pourrait **croiser nos deux bots** pour une meilleure data. Mon IA SEO est meilleure que la vôtre parce que ça fait un an que je bosse dessus ; dans un an, votre système sera excellent. La data de Semrush, tous les autres acteurs l'ont — on se battrait sur les mêmes mots-clés. La data propriétaire, c'est ce qui permet d'attaquer des mots-clés originaux sur lesquels tu es sûr qu'il y a une demande (si tu construis une fonctionnalité, c'est qu'il y a une demande).

## Traduction

**Leexi :** On multiplie les mots-clés par le nombre de langues, ou on attaque juste la France ?

**Timothée :** On bosse en français d'abord.

**Leexi :** On a des scripts de traduction IA assez poussés dans Strapi. Si tu pousses en FR, on traduira. Pour l'instant on lance la traduction manuellement (un bouton par langue), mais 50 pages sur 3 mois ça fait 15/mois, on peut appuyer sur le bouton. La France reste notre marché SEO principal (France/Belgique francophone, de loin le plus de trafic).

## Clôture et suite

**Timothée :** Demain je vous envoie les mots-clés, je construis les cocons dans la foulée, et j'attaque les pages (création + optimisation) **lundi / début de semaine prochaine**. Je vous fais un **rapport toutes les semaines** et on se refait un **call dans 15 jours**. Il peut déjà y avoir du mouvement : votre site est ancien, des pages seront en ligne, on ne va pas attendre trois mois pour regarder.

**Actions actées :**
- **Tim** : envoie les 3-5 mots-clés business à valider + les cocons ; lance la création/optimisation des pages lundi ; récupère le questionnaire/drive ; envoie une invitation pour la session MCP **lundi 9h**.
- **Leexi** : valide les 3-5 mots-clés business ; partage les cas d'usage métier existants + les cocons ; remet dans un drive tout ce qui a été rempli dans le questionnaire ; fournit les 3 grosses URLs de l'ancien site pour l'audit migration.
- **Cadence** : rapport hebdo + call de suivi tous les 15 jours.

---

*(Fin du transcript nettoyé.)*
