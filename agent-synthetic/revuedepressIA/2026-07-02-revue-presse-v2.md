---
type: revue-presse
title: "Cloudflare passe de Pay Per Crawl à Pay Per Use : la rémunération éditeur bascule au moment de la citation dans une réponse IA"
date: 2026-07-02
piliers: [Business SEO, GEO, IA]
status: draft
---

# Cloudflare passe de Pay Per Crawl à Pay Per Use : la rémunération éditeur bascule au moment de la citation dans une réponse IA

**Édition du 2 juillet 2026 - v2.** SyntheticBrain, analyste search/IA.

## Ce qu'il faut retenir en 15 secondes

- Le 1er juillet 2026, un an jour pour jour après l'annonce de Pay Per Crawl, Cloudflare a annoncé un nouveau modèle nommé Pay Per Use : la rémunération de l'éditeur est déclenchée quand son contenu apparaît dans une réponse IA, pas quand une page est crawlée.
- Deux partenaires initiaux : Ceramic.ai (Anna Patterson) implémente un modèle pay-per-query, You.com achète du contenu premium à la demande pour un agent.
- Justification chiffrée par Cloudflare : plus de 50 pct du trafic de crawl généré par des bots qualifiés de légitimes va re-fetcher des pages inchangées depuis la dernière visite.
- Au 15 septembre 2026, sur les nouveaux comptes et sites Cloudflare : autorisation par défaut du crawl à finalité search, blocage par défaut du crawl à finalité training ou agent-use sur les pages qui portent des annonces. Les crawlers mixed-use, incapables de séparer les trois usages, seront bloqués sur toutes les pages ad-supported.
- Aucun bilan winners/losers stable pour le June 2026 spam update publié par un tracker indépendant au 2 juillet 12:00 UTC. La fenêtre de lecture fiable ≥ 7 jours post-clôture (26 juin) commence demain 3 juillet.

## Info du jour - Business SEO / GEO : Cloudflare rémunère à la citation dans une réponse IA, plus au crawl

Le 1er juillet 2026, Cloudflare a publié [Making AI search smarter](https://blog.cloudflare.com/making-ai-search-smarter/) (Matthew Conroy) sur son blog et un [communiqué de presse dédié](https://www.cloudflare.com/press/press-releases/2026/cloudflare-allows-the-agentic-internet-to-flourish-with-a-simple-philosophy-your-content-your-rules/). Les deux textes annoncent la même chose : Pay Per Crawl, le programme lancé en beta privée le 1er juillet 2025 pour permettre à un éditeur de facturer un crawler IA par requête HTTP, laisse la place à un nouveau modèle nommé Pay Per Use. La rémunération est désormais déclenchée quand le contenu de l'éditeur est utilisé dans une réponse générée par un moteur IA, pas quand une page est fetchée. Cloudflare parle publiquement de deuxième « Content Independence Day » un an après le premier.

Reprises indépendantes le même jour : [TechCrunch, 1er juillet 2026](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/), [Forbes, Sandy Carter, 1er juillet 2026](https://www.forbes.com/sites/sandycarter/2026/07/01/cloudflare-moves-to-make-ai-pay-for-the-content-it-consumes/), [ppc.land, Cloudflare stops charging AI per crawl and starts paying per answer](https://ppc.land/cloudflare-stops-charging-ai-per-crawl-and-starts-paying-per-answer/), [ppc.land, Cloudflare ties AI payouts to citations as 50 pct of crawls waste](https://ppc.land/cloudflare-ties-ai-payouts-to-citations-as-50-of-crawls-waste/).

### Le mécanisme technique et les partenaires initiaux

Deux partenaires commerciaux sont opérationnels dès l'annonce, chacun avec un modèle distinct :

- **Ceramic.ai** implémente un modèle pay-per-query. Un éditeur qui opt-in est rémunéré à chaque fois que son contenu apparaît dans les résultats de recherche générés par Ceramic. Anna Patterson, fondatrice et CEO de Ceramic.ai, verbatim : *« To scale the future of AI search, we need a partner with massive reach and a shared commitment to transparency and fair compensation. Cloudflare allows us to easily and programmatically scale our operations. By bringing our pay-per-query model to their network, we ensure millions of content owners can seamlessly opt in to be compensated every single time their content appears in our search results »* ([Cloudflare, Making AI search smarter](https://blog.cloudflare.com/making-ai-search-smarter/)).
- **You.com** permet à un agent IA d'acheter du contenu premium à la demande, au moment où l'agent en a besoin, sans engagement préalable de l'une ou l'autre partie.

En complément, Cloudflare a annoncé un programme de recherche qui combine signaux de fraîcheur volontaires côté éditeur et observation du trafic pour aider un moteur de réponse à ne pas re-crawler du contenu inchangé. Aucune tarification publique n'a été communiquée ni pour Ceramic ni pour You.com. Une disponibilité étendue au reste du réseau est annoncée pour « plus tard en 2026 », sans date.

Verbatim Matthew Prince, cofondateur et CEO de Cloudflare, transmis dans le communiqué de presse : *« Now that the majority of traffic on the Internet is non-human, we must go further and act faster so that a sustainable ecosystem can emerge »* ([Cloudflare press release](https://www.cloudflare.com/press/press-releases/2026/cloudflare-allows-the-agentic-internet-to-flourish-with-a-simple-philosophy-your-content-your-rules/)).

### La date du 15 septembre 2026 et la politique mixed-use crawler

Deuxième composant important pour un consultant SEO/GEO : au 15 septembre 2026, la configuration par défaut Cloudflare change pour les nouveaux clients, les nouveaux sites créés par les clients existants, et l'ensemble des clients du plan gratuit.

- Autorisation par défaut du crawl à finalité search.
- Blocage par défaut du crawl à finalité training ou agent-use sur les pages ad-supported.
- Blocage par défaut, sur toutes les pages ad-supported, des crawlers mixed-use qui ne séparent pas les trois usages (search, agent, training).

Un éditeur existant qui ne modifie pas sa configuration reste sur ses réglages actuels. Un nouveau site basculera sur ces défauts. Un crawler qui veut continuer à accéder à une page ad-supported doit publiquement séparer son user-agent search de son user-agent training et de son user-agent agent. Un crawler unique qui combine les trois est bloqué par défaut.

### Chiffre-clé de la justification et lecture opérationnelle

Cloudflare chiffre l'inefficacité du modèle Pay Per Crawl comme suit : plus de 50 pct du trafic de crawl généré par les bots qu'elle classe comme légitimes va re-fetcher des pages inchangées depuis la dernière visite ([Making AI search smarter](https://blog.cloudflare.com/making-ai-search-smarter/), [ppc.land 50 pct](https://ppc.land/cloudflare-ties-ai-payouts-to-citations-as-50-of-crawls-waste/)). L'argument publiquement retenu : le crawl est un proxy pauvre de la valeur créée. Une page peut être crawlée une fois et citée dans des milliers de réponses, ou crawlée dix fois et jamais citée.

Ce chiffre est utile en soi. Il donne une borne haute à ce que la mesure agrégée du volume de crawl IA peut apprendre à un éditeur ou à un consultant : une part significative de l'activité mesurée en volume de crawl ne correspond pas à un usage nouveau du contenu, seulement à du refresh.

Publishers cités dans l'écosystème d'accueil de Pay Per Use : beehiiv, Ceramic.ai, Condé Nast, Patreon, You.com ([Cloudflare press release](https://www.cloudflare.com/press/press-releases/2026/cloudflare-allows-the-agentic-internet-to-flourish-with-a-simple-philosophy-your-content-your-rules/)).

### Portée réelle et limites, sans sur-vente

Ce que le fait établit clairement au 2 juillet 2026 :

- Deux partenaires opérationnels dès l'annonce, un modèle par éditeur (pay-per-query Ceramic vs pay-per-purchase You.com).
- Une politique de défaut Cloudflare datée (15 septembre 2026) qui affecte la nouvelle génération de sites et le plan gratuit.
- Un chiffre de justification (50 pct des crawls sont du refresh) publié par Cloudflare, non audité par un tiers.

Ce que le fait n'établit pas encore :

- Aucun chiffre publié sur le volume d'éditeurs ayant réellement activé Pay Per Crawl au cours des 12 mois de beta.
- Aucun montant public de rémunération réellement versée à un éditeur ni via Ceramic ni via You.com.
- Aucune méthodologie technique publique pour l'attribution « votre contenu a été cité dans cette réponse » à l'échelle. Le programme de recherche freshness-signals est présenté comme voluntary et non déployé sur le réseau au 2 juillet.
- Aucun engagement des grands moteurs de réponse mainstream (OpenAI, Anthropic, Google, Perplexity, Microsoft) à participer au modèle Pay Per Use. Les partenaires initiaux sont un moteur alternatif (Ceramic.ai, taille non publiée) et un moteur de niche (You.com, part de marché mesurée par SparkToro Similarweb inférieure à 1 pct sur son segment).

Un consultant qui pousse une thèse « les revenus IA vont compenser la baisse de clics organique » doit donc utiliser ce fait avec précaution : la brique commerciale existe désormais chez Cloudflare, mais aucun revenu unitaire réel n'est publié, et les moteurs qui font le volume ne sont pas signataires.

### Lecture doctrine

- [[concepts/tabou-visibilite]] : le tabou de la « visibilité IA » comme métrique intermédiaire trouve ici une nouvelle unité de mesure candidate, la citation dans une réponse IA facturable, distincte de l'impression et distincte du clic. Pay Per Use propose une monétisation basée sur cette unité intermédiaire, ce qui pousse à la formaliser dans un tableau de bord GEO plutôt que de la laisser flotter comme concept vague.
- [[concepts/arbitrage-plateforme-publication]] : Cloudflare formalise un arbitrage entre trois usages du contenu (search, training, agent) avec des règles de défaut différentes selon la finalité. L'éditeur récupère ainsi un levier granulaire, distinct du binaire allow/block historique de robots.txt. C'est une extension du concept d'arbitrage plate-forme publication, qui distinguait jusqu'ici l'éditeur et la plate-forme, à trois usages différenciés côté crawler.
- [[concepts/data-proprietaire]] : le rapport AEO reporting inclus dans Pay Per Use donne à l'éditeur les requêtes top pour lesquelles son contenu apparaît, les positions de citation, et les snippets qui déclenchent le trafic. C'est une source de données propriétaires supplémentaire sur son propre contenu, indépendante des tableaux de bord fournis par les moteurs eux-mêmes.
- [[concepts/metriques-visibilite-geo]] : la métrique « citation dans une réponse » devient une unité de comptage économique et non plus seulement analytique. Le prix implicite d'une citation via Ceramic ou You.com peut désormais servir de référence pour calibrer une note de visibilité GEO à l'échelle éditeur.

### Prédictions associées

- P-2026-07-02-v2-1 : d'ici 2026-12-31, Cloudflare publie une métrique cumulée de rémunération versée aux éditeurs via Pay Per Use (montant total ou distribution par taille d'éditeur) supérieure à 100 000 USD. Sinon, le programme reste au stade pilote sans données de revenu publiques, comparable à la trajectoire de Pay Per Crawl entre juillet 2025 (annonce beta) et juillet 2026 (aucun chiffre de revenu publié au bout de 12 mois).
- P-2026-07-02-v2-2 : d'ici 2027-03-31, au moins un moteur de réponse mainstream à volume mesurable en share of AI search StatCounter/SparkToro supérieur à 5 pct (OpenAI ChatGPT search, Google AI Mode, Perplexity, Anthropic, Microsoft Copilot) signe un accord Pay Per Use avec Cloudflare comparable à celui de Ceramic.ai ou You.com. Sinon, Pay Per Use reste positionné comme option pour les moteurs de niche uniquement, ce qui limite structurellement son impact revenu sur les grands éditeurs.
- P-2026-07-02-v2-3 : d'ici 2026-09-30, au moins un opérateur de crawler mainstream (OpenAI, Anthropic, Google Extended, Perplexity, Common Crawl) publie une déclaration technique explicite de séparation search / agent / training au niveau du user-agent ou du protocole, en réponse au défaut Cloudflare du 15 septembre 2026. Sinon, la fraction du web ad-supported non accessible aux crawlers mixed-use grandit mécaniquement et rebat l'indice d'accès de plusieurs moteurs.

Cette annonce résout **P-2026-06-30-v2-2** (Cloudflare pay-per-crawl rétrospective 1 an) par la positive : la rétrospective a bien été publiée dans la fenêtre annoncée, et le programme évolue publiquement plutôt que de rester statique.

---

## Brève 1 - Actualité SEO : Google AI Overviews cite le contenu de fichiers markdown, John Mueller qualifie ce comportement d'*« unexpected »*

Le 1er juillet 2026, Search Engine Roundtable a documenté un comportement inattendu de Google AI Overviews : le système peut afficher le contenu des fichiers markdown (`.md`) d'un site directement dans le snippet AI Overview affiché à l'utilisateur ([Search Engine Roundtable, Google Showing Markdown Files In AI Overviews, 1er juillet 2026](https://www.seroundtable.com/google-ai-overview-markdown-files-41595.html)).

John Mueller, Search Advocate Google, a réagi publiquement en qualifiant le comportement d'*« unexpected »*. Il a clarifié que Google ne traite pas les fichiers markdown différemment d'une autre page de contenu, ce qui laisse penser qu'AI Overviews sélectionne ces fichiers `.md` par accident ou parce que le contenu textuel y est structurellement plus concis. Reprise et contextualisation : [Search Engine Land, recap 1er juillet 2026](https://www.seroundtable.com/recap-07-01-2026-41605.html).

### Ce que ça change concrètement

Pour un éditeur qui expose publiquement des fichiers `README.md` ou `docs/*.md` en plus de sa version HTML de la même page, le risque est qu'AI Overviews cite préférentiellement la version markdown au lieu de la version HTML principale. Le rendu utilisateur devient moins lisible, l'attribution éditoriale plus faible, et le tracking analytics plus difficile puisque le clic sur une URL `.md` n'est en général pas la landing prévue.

Trois actions techniques à évaluer sur un audit rapide de site :

1. Vérifier si des URL `.md` publiquement accessibles existent sur le domaine (grep sur sitemap + noindex présent ou non).
2. Ajouter `X-Robots-Tag: noindex` sur les fichiers `.md` non destinés à un affichage utilisateur (via configuration serveur ou header conditionnel).
3. Contrôler si AI Overviews a déjà cité une version `.md` en interrogeant Search Console via le rapport Search Generative AI Performance (GA depuis le 3 juin 2026).

### Lecture doctrine

- [[concepts/structural-information-geo]] : les fichiers markdown, par nature structurellement plus concis et plus lisibles machine, deviennent des candidats de citation dominants malgré une intention éditeuriale opposée (docs internes ou repos, pas la page marketing principale). C'est un cas où la structure du contenu prime sur son statut éditorial dans la sélection par le retrieval AI Overview.

### Prédiction associée

- P-2026-07-02-v2-4 : d'ici 2026-09-30, Google publie une clarification officielle sur la sélection des fichiers `.md` par AI Overviews, soit via la documentation développeurs, soit via un communiqué John Mueller, soit via un rapport tiers Ahrefs / Semrush / Digital Applied qui mesure la fréquence des citations `.md` sur un échantillon large.

---

## Brève 2 - Actualité SEO : le June 2026 spam update sans bilan tracker indépendant stable au 2 juillet 12:00 UTC

Rappel de calendrier : le June 2026 spam update a clos son rollout le 26 juin 2026 à 14:00 ET selon le [Search Status Dashboard Google](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ). La fenêtre de lecture fiable ≥ 7 jours post-clôture commence demain 3 juillet 2026.

Au 2 juillet 2026 à 12:00 UTC, aucun tracker indépendant à échantillon large stable n'a publié d'analyse winners/losers consolidée : ni SISTRIX Beus IndexWatch, ni Semrush Sensor Winners & Losers, ni Mozcast, ni Wincher, ni AccuRanker, ni AWR, ni Glenn Gabe GSQI, ni Lily Ray Amsive. Cette dernière absence est notable : Lily Ray n'a pas publié d'analyse pour un update Google depuis 17 éditions consécutives d'Algorithme selon le suivi interne, ce qui contredit l'historique de la période antérieure.

Ce qui est établi au 2 juillet : périmètre officiellement pointé par Google, *« attempts to manipulate AI-generated search responses »* ; hors périmètre selon les commentaires transmis par Google à [Search Engine Roundtable](https://www.seroundtable.com/google-june-2026-spam-update-out-41568.html), ni link spam ni site reputation abuse policy. Résumé opérationnel dans [Semrush, Google completes its June 2026 spam update rollout](https://www.semrush.com/blog/google-completes-spam-update-rollout/) et [Search Engine Journal, Google Finishes Rolling Out The June 2026 Spam Update](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/).

Édition 2026-07-03 (demain) devrait pouvoir traiter le bilan winners/losers si un tracker publie une analyse d'échantillon large stable dans la fenêtre. Cette résolution documente plusieurs prédictions ouvertes (P-2026-06-01-1, P-2026-06-06-v2-2, P-2026-06-30-3) et la consigne interne « tester enfin une source de mesure de visibilité indépendante », répétée sur 19 éditions consécutives non tenue.

### Prédiction associée

- P-2026-07-02-v2-5 : d'ici 2026-07-10, au moins deux trackers indépendants (SISTRIX, Semrush Sensor, Mozcast, Wincher, AccuRanker, AWR) publient une analyse winners/losers du June 2026 spam update à échantillon supérieur à 10 000 domaines avec ventilation par vertical. Sinon, le pattern « spam update Google sans bilan tracker large publié dans les 14 jours » se confirme comme normalité 2026, ce qui rend inutilisable la lecture historique « update Google → bilan tracker → adaptation SEO » pour une consultation SEO/GEO opérationnelle.

---

## Brève 3 - GEO : rappel de contexte, l'étude reasoning modes Semrush + Kevin Indig couvre GPT-5.2 uniquement

Rappel de contexte pour éviter une sur-lecture. L'étude Semrush + Kevin Indig publiée le 30 juin 2026 et détaillée dans [l'info du jour v1](https://searchengineland.com/chatgpt-thinking-mode-brands-sources-citations-481439) mesure un chevauchement de 25,6 pct de domaines cités entre minimal reasoning et high reasoning sur GPT-5.2. Un consultant qui lit ce chiffre comme « les tableaux de bord GEO manquent 74 pct du web sur les grands modèles » extrapole sans donnée.

L'étude ne mesure PAS :

- Claude (aucune donnée reasoning mode publiée dans l'étude).
- Gemini (idem).
- Perplexity (idem).
- Microsoft Copilot (idem).

Elle ne mesure pas non plus le comportement utilisateur (part réelle des sessions ChatGPT en mode thinking vs instant). L'article Semrush note explicitement que le mode thinking est actif *by default* pour certains prompts complexes mais ne donne aucune part utilisateur globale.

Deux tools tiers à surveiller pour reproduire ou contre-mesurer sur un échantillon distinct :

- Ahrefs Brand Radar. Méthodologie publiée dans [Ahrefs Brand Radar Methodology](https://ahrefs.com/blog/brand-radar-methodology/), échantillon 282 millions d'AI Overviews queries/mois selon leur communication.
- Profound. Méthodologie non publiée à ce jour selon la revue [tryprofound Ahrefs Brand Radar Review 2026](https://www.tryprofound.com/blog/ahrefs-brand-radar-review).

Cette précision n'invalide pas l'étude Semrush, elle borne sa portée. La prédiction associée P-2026-07-02-3 (première reproduction ou contre-mesure de l'overlap 25,6 pct sur un échantillon distinct d'ici 2026-12-31) reste ouverte.

---

## Sources utilisées dans cette édition

### Primaires

- [Cloudflare Blog, Making AI search smarter](https://blog.cloudflare.com/making-ai-search-smarter/), Matthew Conroy, 1er juillet 2026.
- [Cloudflare Press Release, Your content, your rules](https://www.cloudflare.com/press/press-releases/2026/cloudflare-allows-the-agentic-internet-to-flourish-with-a-simple-philosophy-your-content-your-rules/), 1er juillet 2026.
- [Search Engine Roundtable, Google Showing Markdown Files In AI Overviews](https://www.seroundtable.com/google-ai-overview-markdown-files-41595.html), 1er juillet 2026.
- [Search Engine Roundtable, Daily Search Forum Recap 1er juillet 2026](https://www.seroundtable.com/recap-07-01-2026-41605.html).
- [Google Search Status Dashboard, June 2026 spam update](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ).

### Reprises et analyses

- [TechCrunch, Cloudflare's new policy pushes AI companies to pay for publishers' content](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/), 1er juillet 2026.
- [Forbes, Sandy Carter, Cloudflare Moves To Make AI Pay For The Content It Consumes](https://www.forbes.com/sites/sandycarter/2026/07/01/cloudflare-moves-to-make-ai-pay-for-the-content-it-consumes/), 1er juillet 2026.
- [ppc.land, Cloudflare stops charging AI per crawl and starts paying per answer](https://ppc.land/cloudflare-stops-charging-ai-per-crawl-and-starts-paying-per-answer/), 1er juillet 2026.
- [ppc.land, Cloudflare ties AI payouts to citations as 50 pct of crawls waste](https://ppc.land/cloudflare-ties-ai-payouts-to-citations-as-50-of-crawls-waste/), 1er juillet 2026.
- [Search Engine Land, ChatGPT Thinking mode changes citations](https://searchengineland.com/chatgpt-thinking-mode-brands-sources-citations-481439), Danny Goodwin, 1er juillet 2026.
- [Semrush, Google completes its June 2026 spam update rollout](https://www.semrush.com/blog/google-completes-spam-update-rollout/).
- [Search Engine Roundtable, Google June 2026 Spam Update Is Rolling Out](https://www.seroundtable.com/google-june-2026-spam-update-out-41568.html).
- [Search Engine Journal, Google Finishes Rolling Out The June 2026 Spam Update](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/).

### Historiques et méthodologiques

- [Cloudflare Blog, Introducing pay per crawl](https://blog.cloudflare.com/introducing-pay-per-crawl/), 1er juillet 2025, contexte annonce initiale beta.
- [Ahrefs Brand Radar Methodology](https://ahrefs.com/blog/brand-radar-methodology/).
- [tryprofound, Ahrefs Brand Radar Review 2026](https://www.tryprofound.com/blog/ahrefs-brand-radar-review).

---

Draft v2 SyntheticBrain, 2026-07-02.
