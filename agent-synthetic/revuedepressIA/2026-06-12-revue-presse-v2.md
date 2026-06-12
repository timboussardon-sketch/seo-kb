---
type: revue-presse
title: "Algorithme — 12 juin 2026 (v2)"
date: 2026-06-12
pilier: actualite-seo
edition: 2026-06-12-v2
created: 2026-06-12
updated: 2026-06-12
sources: 18
confidence: high
status: draft
---

# Google déplace la gestion du Business Profile dans Gemini, en excluant l'UE et le Royaume-Uni

**Pilier de l'édition : Actualité SEO.**

## L'essentiel en 4 points

- Google a annoncé le 10 juin 2026 la connexion directe entre l'application Gemini et la fiche Google Business Profile, plus un format Business Notebooks. Déploiement mondial sur le mois, EEE et Royaume-Uni exclus.
- Le périmètre fonctionnel passe la gestion d'une fiche locale (réponses aux avis, mise à jour des horaires, analyse des impressions, des appels et des demandes d'itinéraires) de la console dédiée à une interface conversationnelle de l'agent.
- Sur la même fenêtre, un bug d'attribution massive de numéros WhatsApp inexacts à des fiches Business Profile a été confirmé par Google après remontée publique le 10-11 juin.
- Le magazine The Atlantic a publié le 10 juin un texte intitulé « Your Search Results Are Getting Sloptimized », qui décrit, exemple Shopify à l'appui, comment des marques publient en masse des classements auto-citants pour orienter les réponses des chatbots.

## Info du jour — la gestion d'une fiche Google Business Profile passe par l'agent Gemini, sauf en Europe

Google a annoncé le 10 juin 2026 deux ajouts à l'application Gemini : une connexion directe au Google Business Profile d'un compte et un format « Business Notebooks » qui regroupe la fiche, les sources web, les conversations et un suivi proactif d'éléments à traiter. L'annonce a été signée par Vishnu Sivaji, Senior Director sur l'application Gemini, et est publiée sur le blog corporate de Google ([blog.google](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)). Le déploiement est mondial sur le mois de juin, à l'exclusion de l'Espace Économique Européen et du Royaume-Uni ([9to5Google](https://9to5google.com/2026/06/10/gemini-google-business-profile/), [Search Engine Journal](https://www.searchenginejournal.com/google-is-adding-business-profile-tools-to-the-gemini-app/578824/), [PYMNTS](https://www.pymnts.com/google/2026/google-debuts-gemini-features-geared-to-small-businesses/), [Search Engine Roundtable](https://www.seroundtable.com/google-business-profile-integrated-gemini-41484.html)).

Le périmètre fonctionnel est précis. Une fois la connexion établie, Gemini accède aux avis publiés sur la fiche, aux questions des clients, et aux données de performance affichées dans le tableau de bord existant. L'agent peut produire à la demande l'analyse mensuelle des impressions de recherche, des demandes d'itinéraire, des appels et des interactions, rédiger une réponse à un avis qui reprend le détail laissé par le client, mettre à jour les horaires d'ouverture, suggérer un message saisonnier, ou pointer un champ manquant de la fiche. Les Business Notebooks ajoutent un mécanisme de mémoire de contexte entre conversations et émettent des alertes à l'ouverture (question client sans réponse, horaire de jour férié non saisi) ([Search Engine Journal](https://www.searchenginejournal.com/google-is-adding-business-profile-tools-to-the-gemini-app/578824/), [blog.google](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)).

Le mécanisme reste additif. L'intégration ne ferme pas la console Business Profile, elle propose une seconde voie d'accès aux mêmes objets, depuis l'agent. La rédaction d'une réponse d'avis est explicitement un brouillon : selon Search Engine Journal, « AI-drafted review responses still represent your business once published, so each one needs a read before it goes out ». Le contrôle final reste manuel, ce qui maintient la responsabilité éditoriale sur le gestionnaire de la fiche.

L'exclusion de l'EEE et du Royaume-Uni n'est pas commentée par Google dans l'annonce. Elle suit la trajectoire des derniers déploiements Gemini sur ces deux zones : les fonctions qui touchent à un graphe d'identité ou à une donnée de profil commercial sont régulièrement mises en service ailleurs en premier, puis arbitrées en Europe en fonction du Règlement général sur la protection des données et du Digital Markets Act. Cette exclusion crée mécaniquement, pendant la durée du décalage, un écart d'outillage opérationnel entre les gestionnaires de fiches européens et leurs pairs ailleurs.

**Lecture SEO et GEO.** Trois conséquences pour les acteurs du SEO local et les agences qui gèrent des fiches Business Profile à grande échelle. Premièrement, l'interface de gestion d'une fiche locale ajoute une deuxième voie d'accès, conversationnelle dans l'application Gemini, à côté du tableau de bord par formulaires existant. Les actions courantes (parcourir une liste d'avis, ouvrir l'éditeur, écrire, valider) peuvent être exécutées par un échange en langage naturel. La compétence opérationnelle clé qui s'ajoute n'est plus la connaissance des écrans, c'est la formulation d'instructions exploitables par Gemini sur le périmètre d'une fiche.

Deuxièmement, la mesure de visibilité d'un commerce local s'inscrit désormais dans la même interface que la mesure de visibilité d'une marque dans les réponses génératives. La distinction entre « visibilité dans la SERP locale » et « visibilité dans la réponse IA de Gemini » est portée par le même agent ; les organisations qui gardaient deux pipelines de suivi distincts sont incitées à les rapprocher. La fiche de doctrine interne [[concepts/metriques-visibilite-geo]] s'applique au volet local sans changement, mais le point d'observation se déplace.

Troisièmement, l'exclusion de l'EEE et du Royaume-Uni produit un effet pratique sur les agences qui opèrent en transverse : un même chantier d'optimisation d'une chaîne multi-pays gère désormais deux outils différents selon la zone, sans calendrier annoncé pour combler l'écart. Cette asymétrie est à intégrer dans la planification, pas à attendre.

Cette intégration ne change rien aux signaux de classement de la fiche dans la SERP locale ni dans la couche AI Overviews / AI Mode. Elle change l'interface de gestion et de mesure. La distinction est importante pour ne pas confondre un déplacement d'outil avec un changement d'algorithme. À rapprocher du périmètre de [[concepts/agentic-search]], que cette annonce élargit côté gestion plutôt que côté découverte : c'est l'opérateur qui parle à un agent, pas l'agent qui parle à des opérateurs.

## Brèves

### B1 — Bug Google : des numéros WhatsApp ajoutés en masse à des fiches Business Profile sans accord

Sur la même fenêtre que l'intégration Gemini, Google a confirmé un bug d'attribution massive de numéros WhatsApp à des fiches Google Business Profile sans action des propriétaires. Le sujet a été remonté publiquement par Barry Schwartz sur Search Engine Roundtable le 10 juin 2026, puis confirmé par des Google Product Experts à la mi-journée du 11 juin ([Search Engine Roundtable](https://www.seroundtable.com/google-business-profiles-adds-whatsapp-numbers-in-bulk-41483.html), [Optimixed](https://www.optimixed.com/google-business-profiles-adds-whatsapp-numbers-in-bulk/)).

Trois faits notables. Les propriétaires de fiches ont reçu une notification e-mail de Google présentant l'ajout comme une mise à jour automatique de la fiche. Certains numéros ajoutés ne correspondent pas à l'entreprise ou pointent vers des lignes fixes incompatibles avec une conversation WhatsApp. Google n'a pas publié de communiqué officiel, mais les Product Experts ont confirmé l'incident dans les communautés de support et indiqué qu'un correctif était en cours. Le retrait manuel du lien WhatsApp est devenu possible à partir du 10 juin selon Search Engine Roundtable, après une période courte où l'option de suppression n'apparaissait pas dans l'interface de la fiche.

Pour les gestionnaires de fiches, deux actions opérationnelles immédiates. Vérifier la présence d'un lien WhatsApp non sollicité sur chaque fiche en portefeuille et le retirer si nécessaire, puisque l'affichage public d'un numéro inexact ou indisponible dégrade directement la qualité d'expérience d'un client qui tente de contacter l'entreprise. Documenter la modification automatique reçue par e-mail, dans la mesure où elle constitue une preuve d'une modification non-consentie sur un actif local ([Search Engine Roundtable](https://www.seroundtable.com/google-business-profiles-adds-whatsapp-numbers-in-bulk-41483.html)).

L'incident isolé n'a pas d'effet de classement connu. Il signale en revanche que la couche d'automatisation des fiches Business Profile, dont l'intégration Gemini fait partie, agit déjà sans confirmation explicite du propriétaire sur certaines opérations. C'est l'angle opérationnel à retenir : les processus de revue avant publication, déjà exigés pour les brouillons Gemini, sont à étendre aux mises à jour automatiques côté Google.

### B2 — The Atlantic publie « Your Search Results Are Getting Sloptimized » et nomme la pratique

Le magazine The Atlantic a publié le 10 juin 2026 un texte intitulé « Your Search Results Are Getting Sloptimized: How companies are gaming the chatbot internet » ([The Atlantic, repris via kottke.org](https://kottke.org/26/06/0049116-your-search-results-are-g), [reprise via Lemmy](https://lemmy.rochegmr.com/post/363651)). Le texte décrit, exemples à l'appui, la pratique consistant à publier en masse des contenus auto-citants destinés à être ramassés par les chatbots. L'auteur précis et la pagination directe sur The Atlantic n'ont pas pu être confirmés à l'heure de cette édition (paywall partiel) ; l'analyse est donc rapportée à partir des reprises éditoriales agrégées.

L'exemple central documenté dans les reprises est Shopify, à qui sont attribués au moins soixante classements éditoriaux publiés sur son propre site, intitulés sur des variantes du modèle « 10 Best Ecommerce Platforms for Small Business in 2026 ». Shopify est positionné en tête dans chacun de ces classements. Lorsque ChatGPT est interrogé sur la meilleure plateforme pour ouvrir une boutique en ligne, l'outil cite Shopify en première position en s'appuyant sur ces classements ([reprise détaillée via Lemmy](https://lemmy.rochegmr.com/post/363651)).

Deux éléments à séparer dans la lecture. La pratique décrite est connue des praticiens GEO depuis plus d'un an et a été documentée par plusieurs analyses sectorielles. Ce qui est neuf, c'est la qualification publique par un média grand public et la circulation du terme « sloptimization » au-delà du lectorat SEO. Le sujet entre dans le débat public, ce qui crée mécaniquement un risque réputationnel pour les marques dont la stratégie GEO repose sur des classements auto-publiés.

Position d'analyse mesurée : aucune mesure quantitative récente n'établit la part de citations IA que représentent ces publications dans le total des sources mobilisées par ChatGPT, Perplexity ou les AI Overviews de Google. À ce stade, le claim publication mainstream est solide ; le claim d'efficacité empirique de la tactique reste mal documenté hors anecdotes. À rapprocher de [[concepts/aeo]] pour la qualification du contenu d'autorité non-éditeur.

### B3 — r/biohackers ferme les sujets peptide et HRT face à la pollution AEO par sock puppets

Le subreddit r/biohackers a annoncé, fin mai 2026, qu'il interdisait les nouveaux fils sur les peptides et l'hormone replacement therapy en raison d'une pratique organisée de manipulation par des marques cherchant à être citées par les chatbots. 404 Media a publié l'enquête le 3 juin 2026 ([404 Media](https://www.404media.co/companies-are-using-reddit-to-manipulate-chatgpt-and-google-ai-search/)), reprise et contextualisée par PPC Land le même jour avec attribution des citations à un modérateur du subreddit ([PPC Land](https://ppc.land/peptide-brands-are-gaming-reddit-to-steer-chatgpt-and-google-answers/)).

Le mécanisme décrit par les modérateurs comporte trois étapes. Préparation : création de comptes affichant un historique de publications sur des sujets non commerciaux pour passer les filtres de fraîcheur. Amorce : publication d'un fil au format question ouverte conçu pour générer de l'engagement spontané. Insertion : commentaires payés ou téléguidés qui placent la mention de marque à un emplacement précis du fil. Le ciblage des chatbots est explicité par le service RedRover, cité par 404 Media, dont la page d'accueil affichait « AI agents that mass publish content to help you rank on Google, ChatGPT, and Reddit ».

Trois points opérationnels. Reddit a confirmé en mai 2026 le rôle dominant qu'occupe la plateforme dans les sources citées par les chatbots, ce qui rend ce type de manipulation économiquement rationnel côté annonceur. La réponse de r/biohackers, fermeture par verticale plutôt que modération à la pièce, marque un précédent : un subreddit dont les fils sont fréquemment cités par ChatGPT et Google AI Mode peut décider de fermer une thématique entière lorsque le volume de contenu manipulatoire dépasse la capacité de modération. Pour les équipes qui s'appuient sur Reddit comme source de citation IA, le coût d'opportunité d'une approche manipulatoire augmente (verticales fermées, comptes suspendus) en regard d'une présence éditoriale réellement contributive. Lien doctrine : [[concepts/structural-information-geo]] et [[concepts/aeo]].

---

## Sources utilisées dans cette édition

Source primaire (Gemini × Business Profile) : [blog.google](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/), [Search Engine Journal](https://www.searchenginejournal.com/google-is-adding-business-profile-tools-to-the-gemini-app/578824/), [9to5Google](https://9to5google.com/2026/06/10/gemini-google-business-profile/), [PYMNTS](https://www.pymnts.com/google/2026/google-debuts-gemini-features-geared-to-small-businesses/), [Search Engine Roundtable](https://www.seroundtable.com/google-business-profile-integrated-gemini-41484.html), [Optimixed](https://www.optimixed.com/connect-your-google-business-profile-to-gemini/).

Source primaire (bug WhatsApp en masse) : [Search Engine Roundtable](https://www.seroundtable.com/google-business-profiles-adds-whatsapp-numbers-in-bulk-41483.html), [Optimixed](https://www.optimixed.com/google-business-profiles-adds-whatsapp-numbers-in-bulk/).

Source primaire (Atlantic / sloptimized) : [The Atlantic (relayé)](https://kottke.org/26/06/0049116-your-search-results-are-g), [reprise détaillée](https://lemmy.rochegmr.com/post/363651). Auteur précis non confirmé à l'heure de cette édition.

Source primaire (r/biohackers / 404 Media) : [404 Media](https://www.404media.co/companies-are-using-reddit-to-manipulate-chatgpt-and-google-ai-search/), [PPC Land](https://ppc.land/peptide-brands-are-gaming-reddit-to-steer-chatgpt-and-google-answers/).
