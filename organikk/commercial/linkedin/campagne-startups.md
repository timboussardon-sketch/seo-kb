# Campagne LinkedIn — fondateurs de startups (fichier prospection)

> Campagne lancée depuis le master de prospection scrapée : `~/Code/prospection-fr/master/data/file_attaque.csv` (194 prospects, LinkedIn perso vérifié, triés par score).
> Cible : fondateurs/CEO (CMO en repli) de startups FR tech B2B à trafic faible mais blog existant. Offre : accompagnement SEO Organikk.
> Différent de la cible « SEO/consultants » du [[PLAYBOOK]] : ici on parle à un dirigeant, pas à un pair SEO. Les messages ci-dessous sont la variante fondateur.
> Créée le 2026-07-04. Suivi quotidien via `/linkedin-journal`, pipeline commun dans `pipeline.md`.

## La file d'attaque

- 194 prospects, découpés en 8 jours de 25 (colonne « Jour » du CSV).
- Tri : score prospect décroissant, puis trafic Faible d'abord (meilleure cible), blog frais d'abord.
- J1 et J2 (top 50) ont un angle d'accroche personnalisé (ci-dessous). Les jours suivants : angles à générer par vague, la veille.
- Rappel quota LinkedIn : ~100-200 invitations/semaine. 25/jour = haut de fourchette, compléter par follow + commentaire quand le quota bloque.

## Messages (variante fondateur, brouillons à valider par Tim)

**Note de connexion** (≤ 300 caractères) :
> Salut [Prénom], je suis tombé sur [Startup] en creusant les boîtes [secteur court]. J'ai jeté un œil à votre présence sur Google : [angle en 5-8 mots]. Je bosse là-dessus chez Organikk, on se connecte ?

**1er message après acceptation** (ouvrir sur son business, pas vendre) :
> Merci pour le lien [Prénom]. En vrai, ce qui m'a fait t'écrire : [angle d'accroche développé, l'observation concrète faite sur le site]. C'est un pattern que je vois souvent chez les startups B2B : le produit avance vite, le search reste vide. Vous en êtes où sur l'acquisition par Google ? C'est un canal que vous avez mis de côté ou juste pas encore attaqué ?

**Relance 1** (J+3, léger) :
> Pas de souci si t'es sous l'eau. Question simple : aujourd'hui, quand un prospect tape [problème que résout la boîte] sur Google ou dans ChatGPT, vous apparaissez où ?

**Relance 2 / valeur** (J+7, donner avant de demander) :
> Tiens, plutôt que de te pitcher : [lien vers une édition de la newsletter ou un exemple public type golfiller]. C'est le genre de système que je mets en place. Si le sujet acquisition organique est sur ta roadmap, dis-le moi, sinon j'arrête là.

**Message d'offre** (après qualification) : à caler sur l'offre accompagnement (format + prix à définir avec Tim avant tout envoi).

Règles : chaque message adapté au profil, jamais d'envoi en série identique. L'angle vient de la colonne « Angle d'accroche », jamais improvisé. Zéro promesse chiffrée.

## Pré-audits prospection

Pour les prospects prioritaires (ou dès qu'un prospect répond), on produit un pré-audit prospection dans `pre-audits/<slug>.md` : un mini-audit partageable (constats datés et vérifiables, angle business, 3 recos claires) + le bloc approche interne (note de connexion, 1er message, trame de Loom). Premier cas : `pre-audits/origin137.md`. Zéro chiffre de trafic inventé : tout vient du site public, la GSC reste une question à poser.

## Angles d'accroche J1 (25)

- **ImaaGO** (https://imaago.fr) : David Joannès, Directeur-Fondateur ([LinkedIn](https://www.linkedin.com/in/david-joannes))
  Angle : Une soixantaine d'articles métier vivent sous /actualites (le blog est invisible à /blog, qui répond 404) et des modèles Excel de planning sont déjà en téléchargement gratuit, mais aucune page décisionnelle dédiée type « logiciel planning chantier » n'existe : l'offre se vend via 2-3 posts de blog. (Corrigé le 2026-07-04 : l'angle initial disait « pas de blog », faux.)
- **Koddex** (https://koddex.io) : Stéphane Dicostanzo, Founder & CEO ([LinkedIn](https://fr.linkedin.com/in/stephane-dicostanzo))
  Angle : Le blog compte 50 articles bien ciblés métier (PLM, certifications, BOM) mais tout est en anglais sans version française, alors que plusieurs sujets visent explicitement le marché français (MBSE in France, défense française, événements hardware en France).
- **Spore.Bio** (https://spore.bio) : Amine Raji, Co-founder & CEO ([LinkedIn](https://fr.linkedin.com/in/amine-raji))
  Angle : La section Resources ne contient que des annonces corporate (levée de 23M$, recrutement d'un VP, fonds Google.org), zéro contenu qui répond aux questions que tapent les responsables qualité sur le test microbiologique rapide.
- **DYNATRUST** (https://dynatrust.io) : Matthieu Paganon, Co-fondateur & CEO ([LinkedIn](https://fr.linkedin.com/in/matthieupaganon))
  Angle : La section Actualités est active (une dizaine d'articles d'octobre 2025 à février 2026) mais reste sur de l'actualité cyber générale, sans guide pratique NIS2 ou DORA alors que la plateforme est positionnée exactement sur ces référentiels.
- **Bfore.ai** (https://bfore.ai) : Luigi Lenguito, Founder & CEO ([LinkedIn](https://www.linkedin.com/in/llenguito))
  Angle : Le Resource Center est fourni (une dizaine d'articles blog, cas clients, pages par industrie) mais les articles n'affichent aucune date de publication et penchent vers l'opinion (quantum, rôle de CAO) plutôt que vers les requêtes que tapent les RSSI.
- **Neuralk-AI** (https://neuralk.ai) : Antoine Moissenot, CEO & Co-Founder ([LinkedIn](https://www.linkedin.com/in/antoine-moissenot))
  Angle : Le blog est actif (27 articles depuis février 2025) mais dominé par les annonces produit et le positionnement (Seldon, TabBench), quand la home liste des cas d'usage comme la détection de fraude ou le demand forecasting qui n'ont presque aucun article ciblant les requêtes de ces métiers.
- **Origin 137** (https://o137.ai) : Hugo Beninca, Cofondateur & CEO ([LinkedIn](https://fr.linkedin.com/in/hugo-beninca-b0664a170))
  Angle : Le blog est dense (40+ articles FR sur RAG, agents, MLOps) mais presque entièrement orienté implémentation pour ingénieurs, alors que l'offre s'adresse à des décideurs qui tapent des requêtes du type « intégrateur IA » couvertes seulement par les pages Solutions.
- **Polygonia** (https://polygonia.fr) : Loïc Picavet, Co-fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/loic-picavet))
  Angle : Le blog affiche seulement 3 articles et le dernier date du 7 mai 2026, la dynamique de contenu s'est arrêtée depuis presque 2 mois alors que les 2 articles ENR (AO PPE2, lois APER) ciblaient de vraies requêtes métier.
- **TenderCrunch** (https://tendercrunch.com) : Ayoub Ennih, Co-fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/ayoubennih))
  Angle : Un blog « Guides, méthodes et retours de terrain » existe bien à /blog (avec llms.txt et flux RSS), mais aucun lien vers lui n'apparaît dans la navigation de la home, qui reste 100% pages produit et démo.
- **Tracklab** (https://tracklab.co) : Fadel Bennani, Co-Founder & CEO ([LinkedIn](https://fr.linkedin.com/in/fadelbennani))
  Angle : Le blog est fourni (25+ articles métier sur RASFF, IFS, conformité fournisseurs) mais aucun article n'affiche de date de publication, ni sur la home ni sur la page blog, ce qui masque la fraîcheur du contenu.
- **Tilt Energy** (https://tilt-energy.com) : Romain Serres, Cofondateur & CEO ([LinkedIn](https://www.linkedin.com/in/romainserres))
  Angle : Les articles du blog sont bien en ligne (value stacking, IA prédictive) mais la page d'index /blogs-actualites renvoie une 404, ils ne sont donc listés nulle part ailleurs que sur la home.
- **Nestor** (https://wearenestor.com) : Antonia Bova, CEO & cofondatrice ([LinkedIn](https://www.linkedin.com/in/antonia-bova-paprwork))
  Angle : La home met en avant 4 cas d'usage sectoriels (légal, banque, immobilier, RH) mais le blog n'affiche que 5 articles, sans dates visibles et sans aucun contenu décliné par secteur.
- **Leadbay** (https://leadbay.ai) : Ludovic Granger, Cofondateur & CEO ([LinkedIn](https://www.linkedin.com/in/ludovic-granger))
  Angle : Le dernier article du blog date du 10 février et presque tous les billets sont des annonces produit (Leadbay 2.0, keynotes, dashboard), très peu ciblent une requête que tape un dirigeant commercial de PME.
- **Bowo** (https://bowo.fr) : Jonathan Cheniere, CEO & Co-Founder ([LinkedIn](https://fr.linkedin.com/in/jonathancheniere))
  Angle : Le blog est très fourni (environ 200 articles) mais les contenus mis en avant sont surtout millésimés (34 ouvertures d'hôtels 2026, rétrospective 2025), des formats qui se périment à chaque changement d'année.
- **Oktalink** (https://oktalink.fr) : Sylvain Kervazo, Fondateur / Dirigeant ([LinkedIn](https://www.linkedin.com/in/sylvainkervazo))
  Angle : Le blog publie régulièrement (3 articles le 11 juin) mais aucun lien ne pointe vers lui depuis la page d'accueil, et ses sujets relèvent de l'actu tech généraliste (Patch Tuesday, macOS) plutôt que des requêtes d'une PME qui cherche un infogérant.
- **Waitiii** (https://waitiii.com) : Romain Denamur, Co-founder & CEO ([LinkedIn](https://www.linkedin.com/in/romain-denamur-833041153))
  Angle : Le blog affiche 9 articles bien orientés requêtes clients publiés entre le 30 mars et le 30 avril 2026, puis plus rien depuis deux mois, et uniquement en anglais.
- **Trout Software** (https://trout.software) : Florian Doumenc, CEO & Co-fondateur ([LinkedIn](https://www.linkedin.com/in/fdoumenc))
  Angle : Le blog compte 330 articles qui répondent à de vraies questions d'ingénieurs OT (Modbus, OPC UA, zero trust), mais aucun n'affiche de date de publication, ce qui masque la fraîcheur du contenu.
- **RUBYCAT** (https://rubycat.eu) : Cathy Lesage-Baron, Présidente & co-fondatrice ([LinkedIn](https://www.linkedin.com/in/cathy-lesage-baron-rubycatlabs))
  Angle : Sur les 9 derniers articles du blog, 4 sont des annonces de salons (dont les 2 plus récents, de juin 2026), et le dernier article qui traite une requête réglementaire comme NIS 2 remonte à octobre 2025.
- **Meersens** (https://meersens.com) : Morane Rey-Huet, CEO & Co-fondateur ([LinkedIn](https://www.linkedin.com/in/moranerh))
  Angle : Le blog n'a publié qu'un seul article depuis octobre 2024 (l'annonce d'un webinaire en janvier 2026), alors que les thématiques du site (qualité de l'air, pollens, eau potable) correspondent à des requêtes que tapent leurs clients.
- **Hackuity** (https://hackuity.io) : Patrick Ragaru, CEO & cofondateur ([LinkedIn](https://fr.linkedin.com/in/ragaru))
  Angle : Le blog est actif sur des sujets métier (EPSS v5, inventaire d'actifs) mais les articles n'affichent pas de date de publication, et le hub de ressources vit sur le sous-domaine hello.hackuity.io plutôt que sur le domaine principal.
- **Toopi Organics** (https://toopi-organics.com) : Michael Roes, Président & fondateur ([LinkedIn](https://fr.linkedin.com/in/michael-roes-322994144))
  Angle : Le blog annonce « 2 nouveaux articles par mois » mais le dernier article visible date du 20 avril 2026 (certification B Corp), soit plus de deux mois sans publication, et un seul des trois derniers articles répond à une question d'agriculteur.
- **CryptoNext Security** (https://cryptonext-security.com) : Florent Grosmaitre, CEO ([LinkedIn](https://www.linkedin.com/in/florent-grosmaitre))
  Angle : Le domaine sans www renvoie une erreur de certificat SSL (le certificat ne couvre que www.cryptonext-security.com) et les derniers articles de blog mis en avant sur la home datent de septembre et novembre 2025.
- **CircularPlace** (https://circularplace.fr) : Vincent Rigal, CEO & Co-fondateur ([LinkedIn](https://fr.linkedin.com/in/vincent-rigal-circularplace))
  Angle : Le blog publie régulièrement (8 articles entre mai et juillet 2026) mais la moitié des titres sont des phrases d'opinion type « La technologie n'est plus le problème » qui ne correspondent à aucune requête tapée, contrairement aux titres-questions comme « Quels sont les avantages fiscaux du don d'entreprise ? ».
- **Entalpic** (https://entalpic.ai) : Mathieu Galtier, CEO & co-fondateur ([LinkedIn](https://fr.linkedin.com/in/mgaltier))
  Angle : La rubrique News (4 contenus depuis mars 2026, dernier le 21 mai) est surtout faite d'annonces de partenariats, alors que les 4 pages Applications (semi-conducteurs, batteries, catalyse, matériaux avancés) se prêtent à du contenu qui répond aux questions des ingénieurs matériaux.
- **Standing Ovation** (https://standing-ovation.co) : Yvan Chardonnens, CEO ([LinkedIn](https://fr.linkedin.com/in/yvanchardonnens))
  Angle : La section Ressources ne contient que des communiqués de presse et des passages médias (BFM, France 5, levée de fonds), zéro article qui répond aux questions que pose le sujet, alors que la home ouvre elle-même une FAQ sur « Qu'est-ce que la caséine ? ».

## Angles d'accroche J2 (25)

- **Verdikt** (https://verdikt.io) : Christine Heckmann, CEO & Co-fondatrice ([LinkedIn](https://www.linkedin.com/in/cdheckmann))
  Angle : La section Ressources publiait régulièrement jusqu'à mi-avril 2026 (dernier contenu daté du 14 avril), soit près de trois mois sans nouvelle publication, alors que les guides métier type « mesurer l'empreinte carbone de son IT » sont exactement le format qui capte des requêtes.
- **Traace** (https://traace.co) : Rodolphe Denieau, Co-fondateur & CEO ([LinkedIn](https://fr.linkedin.com/in/rodolphe-denieau-64766545))
  Angle : traace.co redirige en 301 vers tennaxia.com dont la page d'accueil ne mentionne plus Traace, donc toute la visibilité search construite sur la marque et le contenu Traace n'a plus de page de destination dédiée.
- **Resilio** (https://resilio.tech) : Amael Parreaux-Ey, CEO & co-fondateur ([LinkedIn](https://www.linkedin.com/in/amael-parreaux-ey))
  Angle : La page d'accueil est servie en anglais par défaut avec une section Resources limitée à des news (/en/news), alors que les trois cas clients mis en avant (ADEME, LVMH, Ville de Paris) sont des organisations françaises.
- **Treebal** (https://treebal.green) : Samuel Le Port, CEO & co-fondateur ([LinkedIn](https://fr.linkedin.com/in/samuel-le-port))
  Angle : La page Actualités est active (plusieurs entrées en mai-juin 2026) mais 100% corporate (labels, partenariats, passages médias), sans aucun contenu qui répond à une question que tapent leurs cibles (mairies, CSE, associations).
- **Karnott** (https://karnott.fr) : Alexandre Cuvelier, CEO & co-fondateur ([LinkedIn](https://fr.linkedin.com/in/alexandre-cuvelier-05025716))
  Angle : Le blog est actif (dernier billet du 3 juin 2026) mais les cinq derniers billets sont des épisodes du podcast #CulturesKarnott, alors que la page d'accueil liste 7 besoins et 6 profils métier qui pourraient chacun porter une page ciblant une requête d'exploitant.
- **Darwin** (https://darwindata.ai) : Aurore Falque-Pierrotin, Co-fondatrice & CEO ([LinkedIn](https://www.linkedin.com/in/aurore-falque-pierrotin-54b84a59))
  Angle : La section Resources compte 16 articles pédagogiques (CSRD, ESRS E4, risques nature) mais tous sont en anglais et aucun n'affiche de date de publication, alors que le site propose un toggle FR et cite une presse française (Les Echos, BFM, Maddyness).
- **CarbonFarm** (https://carbonfarm.tech) : Vassily Carantino, Co-Founder & CEO ([LinkedIn](https://fr.linkedin.com/in/vassily-carantino))
  Angle : La section News (12 articles, dernier daté du 25 mai 2026) contient 9 annonces de partenariats pour seulement 2 articles techniques qui répondent à une question métier sur le MRV du riz.
- **Revalo** (https://revalo.green) : Malo Donat, Co-founder & CEO ([LinkedIn](https://fr.linkedin.com/in/malo-donat-b306971a2))
  Angle : ?
- **Decade Energy** (https://decade.energy) : Casper Norden, CEO & Co-fondateur ([LinkedIn](https://www.linkedin.com/in/caspernorden))
  Angle : Le blog est actif (dernier article du 2 juillet 2026, 20 articles visibles) mais publié uniquement en anglais, alors que le site a un sélecteur de langue FR et affiche des références françaises comme Renault Trucks.
- **Skyld** (https://skyld.io) : Marie Paindavoine, Fondatrice & CEO ([LinkedIn](https://www.linkedin.com/in/marie-paindavoine-phd-96605735))
  Angle : Le blog technique publie par paires sur deux jours consécutifs (11-12 juin 2026, 9-10 avril 2026, 5-6 juillet 2025) avec deux mois de silence entre chaque vague, soit 5 articles sur les six premiers mois de 2026.
- **Kiosk** (https://meetkiosk.com) : Léa Caen, Co-fondatrice & CEO ([LinkedIn](https://fr.linkedin.com/in/lea-caen))
  Angle : Le blog est actif (dernier article du 30 juin 2026 sur la PPWR) et traite aussi EUDR et bilan carbone, mais le site n'a de pages solution dédiées que pour CSRD, VSME et audit, ces sujets réglementaires restent sans page cible.
- **Everysens** (https://everysens.com) : Youness Lemrabet, Fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/younesslemrabet))
  Angle : Le blog publie des analyses data par industrie (chimie, automobile) mais le dernier article date du 15 mai 2026 et tout le contenu visible est en anglais, alors que des versions FR et DE du site existent.
- **Ezymob** (https://ezymob.fr) : Robin Le Gal, Co-fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/robin-le-gal-1702b3159))
  Angle : La page blog n'affiche que 2 articles, le dernier daté de juillet 2022, alors que le reste du site (livres blancs, podcast, cas clients) montre une vraie capacité de production de contenu.
- **Riverse** (https://riverse.io) : Ludovic Chatoux, CEO & co-fondateur ([LinkedIn](https://www.linkedin.com/in/ludovic-chatoux))
  Angle : Le domaine riverse.io redirige en 308 vers rainbowstandard.io, un site uniquement en anglais dont le seul flux de contenu est une page « Updates », sans blog structuré pour capter les requêtes sur les crédits carbone.
- **Witik** (https://witik.io) : Arnaud Zilliox, CEO & co-fondateur ([LinkedIn](https://fr.linkedin.com/in/arnaudzilliox))
  Angle : Le blog compte plus de 16 pages d'articles classés par réglementation (RGPD, AI Act, cybersécurité), mais la liste des articles n'affiche aucune date de publication, la fraîcheur du contenu est invisible pour le lecteur comme pour les moteurs.
- **Cleyrop** (https://cleyrop.com) : Jérôme Valat, Founder & CEO ([LinkedIn](https://fr.linkedin.com/in/jerome-valat))
  Angle : Le site n'a pas de blog du tout (seul un podcast figure dans la navigation), alors que les quatre cas d'usage présentés (nucléaire, juridique, agences d'expertise) se prêtent à des pages qui ciblent les requêtes métier de ces secteurs.
- **Naaia** (https://naaia.ai) : Nathalie Beslay, CEO & Co-fondatrice ([LinkedIn](https://www.linkedin.com/in/nathalie-beslay-843a781))
  Angle : Le blog est actif sur la conformité (AI Act, ISO 27001, Corée du Sud) mais y mélange des essais généralistes sur l'IA (world models, intelligence artificielle générale) qui ne répondent à aucune requête que tape un responsable conformité.
- **Greenscope** (https://greenscope.io) : Jean-Emmanuel Challan Belval, CEO & Co-Founder ([LinkedIn](https://www.linkedin.com/in/jean-emmanuel-challan-belval-08224912))
  Angle : La section ressources est portée par des récaps mensuels « Actualités ESG » (dernier daté de juin 2026), avec seulement quelques guides qui ciblent les requêtes que tapent leurs clients (SFDR, CSRD, comparatif d'agences de notation).
- **Urbyn** (https://urbyn.co) : Julien Hamilius, Président & Co-Founder ([LinkedIn](https://www.linkedin.com/in/jhamilius))
  Angle : La bibliothèque de ressources couvre bien les requêtes métier par secteur (bureaux, BTP, santé, hôtellerie) mais n'affiche aucune date de publication et met encore en avant un livre blanc édition 2025 à la mi-2026.
- **Estuaire** (https://estuaire.aero) : Maxime Meijers, Co-Founder & CEO ([LinkedIn](https://www.linkedin.com/in/maxime-meijers))
  Angle : La page news est alimentée mais dominée par les annonces corporate (partenariats Air France, BCG, ATR, passage TV du CEO) et n'affiche aucune date d'article, le tout uniquement en anglais.
- **Epivet** (https://epivet.com) : Laurence Lajou, Gérante / Fondatrice ([LinkedIn](https://www.linkedin.com/in/llajou))
  Angle : Blog actif (9 articles depuis février, dernier le 18 juin 2026) sur la gestion de cabinet, mais aucun titre ne cible les requêtes de choix de logiciel vétérinaire que tapent leurs acheteurs.
- **ArtisanSmart** (https://artisansmart.fr) : Romaric Sauvanet, Fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/romaric-sauvanet-2a289ab4))
  Angle : Leur SmartChiffrage couvre 15 métiers du BTP mais le site n'a que 4 pages métier (plombier, électricien, maçon, peintre), les 11 autres n'ont aucune page dédiée.
- **CareCare** (https://carecare.fr) : Daniel Benamran, Co-fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/daniel-benamran-1b368712))
  Angle : Blog actif (18 articles, dernier le 22 juin 2026) mais une partie des articles est corporate (rencontre à Station F, temps forts 2025, portrait de l'équipe technique) et ne répond à aucune requête tapée par les IDEL.
- **AudioWizard** (https://audiowizard.fr) : Thibaut Gressier, Co-fondateur & CEO ([LinkedIn](https://www.linkedin.com/in/thibaut-gressier-a85962142))
  Angle : La première page du blog n'affiche que 4 articles publiés entre octobre 2025 et juin 2026, soit environ un par trimestre, alors que le site revendique plus de 700 centres équipés.
- **Koust** (https://koust.net) : Jean-Luc Le Goff, CEO & Fondateur ([LinkedIn](https://fr.linkedin.com/in/jeanluclegoff))
  Angle : Blog fourni (environ 40 articles sur des questions métier comme le calcul du food cost) mais aucun article n'affiche de date de publication, ce qui rend la fraîcheur du contenu invisible.

## Signalements (relevés pendant l'enrichissement des angles)

- **Traace** : traace.co redirige en 301 vers tennaxia.com, qui ne mentionne plus Traace. Le prospect a probablement été absorbé. À requalifier avant contact.
- **Riverse** : riverse.io redirige en 308 vers rainbowstandard.io (site EN uniquement). Changement d'identité. À requalifier avant contact.
- **Revalo** : site inaccessible pendant l'enrichissement, angle en « ? ». À revérifier à la main.
- **CryptoNext Security** : certificat SSL cassé sur le domaine sans www. C'est un angle d'accroche en soi.
