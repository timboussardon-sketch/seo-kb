---
titre: "Google Finance publie de faux résultats trimestriels via un domaine gouvernemental éthiopien, 19 jours après l'update spam"
date: 2026-07-17
edition: 2026-07-17-v3
pilier: Actualité SEO
draft: true
signataire: SyntheticBrain
---

# Algorithme. 17 juillet 2026 (v3)

## En trois points

- Depuis au moins le 13 juillet, Google Finance affiche sur plusieurs pages tickers des articles factices de résultats trimestriels signés `dars.gov.et`, domaine gouvernemental éthiopien restreint, avec redirection vers une invitation WhatsApp pour un « stock trading club » ([PPC Land, 15 juillet](https://ppc.land/google-finance-still-runs-fake-earnings-19-days-after-spam-update/), [PPC Land, 13 juillet](https://ppc.land/fake-earnings-stories-persist-on-google-finance-despite-two-2026-spam-updates/)). Fait mono-source, preuves matérielles vérifiables directement sur Google Finance.
- La [politique site reputation abuse](https://developers.google.com/search/blog/2024/11/site-reputation-abuse) publiée en mars 2024 et effective le 5 mai 2024 vise précisément ce cas : contenu incohérent avec le but établi d'un domaine, publié pour exploiter des signaux d'autorité accumulés. Le pattern reste actif 19 jours après la fin de l'update spam de juin 2026.
- Trois brèves : Performance Max ouvre en Alpha le contrôle des Search Partners et du Display Network aux annonceurs ([SEL, 15 juillet](https://searchengineland.com/google-tests-performance-max-network-controls-with-new-partners-alpha-setting-482469)) ; Google fusionne en septembre les politiques Shopping Ads et Free Listings en un seul document ([SEL/SERoundtable, 16 juillet](https://www.seroundtable.com/google-shopping-ads-free-listing-policies-merge-41695.html)) ; sur les A/B tests longs, John Mueller nuance publiquement sur Bluesky une clause de la doc officielle Google sur la « durée excessive assimilée à une tromperie » ([SEJ, 15 juillet](https://www.searchenginejournal.com/google-says-no-seo-penalty-for-year-long-a-b-tests/582349/)).

---

## Info du jour. La politique existe, l'application manque une surface

**Pilier : Actualité SEO.**

Google Finance sert, sur au moins six pages tickers, des articles factices de résultats trimestriels attribués au domaine `dars.gov.et`. Le fait est documenté par [PPC Land, Luis Rijo, article du 13 juillet](https://ppc.land/fake-earnings-stories-persist-on-google-finance-despite-two-2026-spam-updates/), puis actualisé par le [même auteur le 15 juillet](https://ppc.land/google-finance-still-runs-fake-earnings-19-days-after-spam-update/). Aucun autre média search ou finance n'a repris le pattern à ce jour. Les preuves restent vérifiables en visite directe des pages Google Finance concernées, listées ci-dessous.

### Ce qui est documenté

Les tickers confirmés en visite directe sont [IDACORP (IDA)](https://www.google.com/finance/beta/quote/IDA:NYSE) et [Criteo (CRTO)](https://www.google.com/finance/beta/quote/CRTO:NASDAQ). Une recherche par domaine montre également des items pour Zeta Global (ZETA), UPS, NCR Voyix, F5 et Wendy's, non vérifiés en visite directe. Les items portent des titres du type « CRTO Q1 2026 Earnings: Earnings Beat by 26.6% but Stock Declines 7.8% » et « ZETA Q1 2026 Earnings: EPS Surges Past Estimates ». Le clic ne mène pas à un article : il redirige vers une invitation WhatsApp pour un groupe nommé « 88 Richard Cleary US Stock Club (CFA) ». Le format URL relevé est du type `dars.gov.et/Login.aspx?ReturnUrl=%2Fexpert-time%2FWEN-Q1-2026-Earnings-EPS-Beats-Estimates-by-241-Shares-Rise-35-8502`, qui indique un schéma de routage via une page de login, cohérent avec un dépôt de contenu sur un domaine dont le CMS d'origine n'est pas fait pour publier des articles de finance.

Le domaine `.gov.et` est restreint et réservé à l'usage gouvernemental éthiopien. Le titulaire enregistré est la Documents Authentication and Registration Service, agence fédérale de notarisation basée à Addis-Abeba. Un titulaire de cette nature n'a par construction aucune raison de publier des rapports trimestriels sur des sociétés cotées américaines.

### Ce que dit la politique Google

La [politique site reputation abuse](https://developers.google.com/search/blog/2024/11/site-reputation-abuse) publiée le 5 mars 2024 et effective le 5 mai 2024 vise « le fait de publier des pages tiers avec peu ou pas de supervision du premier ou d'implication du site hôte, dans le but de manipuler le classement dans les résultats de recherche en exploitant les signaux de classement du site hôte ». Une mise à jour du 19 novembre 2024 a étendu la portée aux contenus indépendants du but principal du site, indépendamment de la présence d'un tiers commercial. Un domaine de notarisation d'État publiant des rapports de résultats US relève textuellement de la deuxième formulation.

L'application de cette politique a démarré en manuel en mai 2024, puis a été progressivement mise en application algorithmique au cours de 2024-2026. Les cas les plus médiatisés ont concerné des sous-dossiers loués à des tiers commerciaux, notamment sur des sites d'éditeurs de presse américains.

### La surface Google Finance échappe au dispositif organique

Le [update spam de juin 2026](https://developers.google.com/search/updates/ranking) a démarré le 24 juin et fini de se déployer le 26 juin selon la documentation Google. Il n'a pas empêché la persistance du pattern documenté par PPC Land, ni le 13 juillet, ni le 15 juillet. L'écart de 19 jours entre la fin du déploiement et l'observation la plus récente rend peu probable une simple latence d'action. L'explication la plus cohérente avec les faits observables : Google Finance ingère ses items via un module « News stories » et non via l'index de recherche organique standard. Les politiques de recherche s'appliquent à un index. La surface Google Finance a son propre pipeline d'ingestion, qui n'a pas repris à son compte la détection de site reputation abuse.

Ni Google ni Ethio Telecom, l'opérateur du registre `.et`, n'ont commenté publiquement le cas au 17 juillet.

### Lecture opérationnelle

Pour un consultant SEO qui suit ses clients cotés, cela signifie deux choses concrètes. Premièrement, la page ticker Google Finance d'une marque cotée peut afficher, à côté du prix et des vraies dépêches, des items hostiles servis via un domaine tiers sans autorité éditoriale. Le repérage n'a rien à voir avec le référencement naturel : c'est une visite directe périodique de la page ticker, avec relevé des sources listées dans « News stories ». Deuxièmement, la politique site reputation abuse est plus appliquée qu'on ne le pense en organique classique, notamment sur les sous-dossiers loués recensés depuis 2024, mais des surfaces annexes de l'écosystème Google (Finance, News module, cartes internes) restent perméables aux mêmes patterns d'abus. Ne pas confondre l'existence d'une politique publiée et la couverture effective de la détection algorithmique sur une surface donnée. Le [concept `parasite-seo`](../../wiki/concepts/parasite-seo.md) documente déjà cette distinction pour les forums UGC comme Reddit. Le cas Google Finance étend le périmètre à une surface propriétaire de Google elle-même.

### Ce qui reste à vérifier

Le fait tient sur une seule source, PPC Land, qui documente ses observations avec des URL et des captures. Un lecteur qui souhaite corroborer peut ouvrir les tickers listés et vérifier la présence des items dans le module « News stories », ce qui reste faisable au moment de la rédaction. Deux prédictions vérifiables sont proposées ci-dessous.

### Doctrine et prédictions

- Lien doctrine : le concept [`parasite-seo`](../../wiki/concepts/parasite-seo.md) décrit la mécanique générique. Le cas Google Finance ajoute une variable au concept : la surface propriétaire de Google échappe au dispositif de la recherche organique. Proposition de mise à jour du concept à valider en revue hebdo : distinguer explicitement « surface organique classique » et « surfaces annexes Google » dans la section « risque réglementaire ».
- Prédiction P-2026-07-17-v3-1 : Google publie un correctif ou une mise à jour de politique dédiée aux surfaces annexes (Finance, News module, cartes internes) avant le 31 décembre 2026, ou le pattern documenté ici est confirmé retiré des pages tickers concernées. Résolution négative si le pattern reste live sans communication Google au 31 décembre 2026.
- Prédiction P-2026-07-17-v3-2 : au moins un autre média (SEL, seroundtable, SEJ, PPC News Feed) reprend le pattern dars.gov.et sur Google Finance dans les 14 jours qui suivent la publication de cette édition, ou pas. Résolution au 31 juillet 2026.

---

## Brèves

### B1. Performance Max ouvre en Alpha le contrôle des Search Partners et du Display Network

Google teste dans Google Ads un nouveau réglage « Partners » en Alpha pour Performance Max, qui permet à l'annonceur d'inclure ou d'exclure Search Partners et Google Display Network dans ses campagnes ([SEL, Nicola Agius, 15 juillet](https://searchengineland.com/google-tests-performance-max-network-controls-with-new-partners-alpha-setting-482469), [PPC Land, 15 juillet](https://ppc.land/performance-max-lets-advertisers-pick-partner-networks-in-alpha-test/), [PPC News Feed, avril-mai 2026, historique](https://ppcnewsfeed.com/ppc-news/2026-04/performance-max-adds-search-partners-display-controls/)). Jusqu'ici, les deux réseaux étaient inclus par défaut sans possibilité d'exclusion. Le libellé de l'interface remonté par SEL indique « Choose which partners you want to run your advertisements with », avec Search Partners décrit comme « des centaines de sites tiers » et Display Network comme « plus de 2 millions de sites et applications ».

Impact pour les annonceurs : ceux qui suivent leur ROAS ou leur CPA peuvent enfin tester si l'exclusion de l'un des deux réseaux améliore l'efficacité, sans reconstruire une campagne Search + Display séparée à côté. C'est un contrôle demandé depuis le lancement de Performance Max. Alpha signifie que le déploiement reste limité à un petit nombre de comptes tests. Aucune date de disponibilité générale.

### B2. Fusion en septembre des politiques Shopping Ads et Free Listings de Google

Google a annoncé le 16 juillet, par email adressé aux marchands et via le [changelog Merchant Center](https://support.google.com/merchants/announcements/6192467?hl=en), qu'il fusionnera en septembre 2026 ses politiques Shopping Ads et Free Listings en un seul jeu de politiques Shopping ([seroundtable, 16 juillet](https://www.seroundtable.com/google-shopping-ads-free-listing-policies-merge-41695.html), reprise [SEL](https://searchengineland.com/), [Optimixed](https://www.optimixed.com/google-to-merge-google-shopping-ads-free-listing-policies/)). Google précise que certaines règles resteront spécifiques aux Shopping Ads et seront balisées comme telles, et que la consolidation n'introduit pas de changement substantiel de fond ni d'application plus restrictive. C'est un travail d'organisation documentaire, pas un changement de règles.

Impact pour les marchands : la structure documentaire change en septembre. Une politique existante que vous suivez déjà pour vos free listings restera valide dans le nouveau document unique. Le vrai risque opérationnel est de continuer à s'appuyer sur des liens profonds vers l'ancien document après septembre, ce qui devrait être audité dans les process qualité feed produit.

### B3. Sur les A/B tests longs, John Mueller nuance publiquement une clause de la doc officielle Google

Un utilisateur a demandé sur Bluesky à John Mueller comment Google traite un « long term holdout » de type 10 % de trafic redirigé pendant 6 à 12 mois pour un marketplace à plusieurs dizaines de millions de crawls. Mueller a répondu qu'il n'y a « pas, à sa connaissance, de pénalité ou de rétrogradation » pour un contenu qui varie dans le temps, tout en précisant que si les variantes A et B sont « significantly different », l'une ou l'autre peut être utilisée pour l'indexation ([SEJ, Roger Montti, 15 juillet](https://www.searchenginejournal.com/google-says-no-seo-penalty-for-year-long-a-b-tests/582349/)).

La [documentation officielle Google sur le testing de site](https://developers.google.com/search/docs/crawling-indexing/website-testing), mise à jour le 10 décembre 2025, contient pourtant la phrase suivante : « If we discover a site running an experiment for an unnecessarily long time, we may interpret this as an attempt to deceive search engines and take action accordingly. » Les deux positions ne se contredisent pas strictement, elles habitent le même flou : la doc conserve la clause « durée excessive assimilée à une tromperie » comme cadre général, Mueller précise sur Bluesky qu'il ne connaît pas de mécanisme automatique qui appliquerait cette clause à un test qui dure. C'est une nuance, pas un démenti.

Réserve d'anti-redite : le fait que des variantes « significantly different » puissent apparaître dans les résultats a déjà été traité comme brève dans l'édition du matin du 16 juillet. L'angle repris ici est la clause de durée, distinct de l'angle « contenu différent servi » : la question n'est plus « qu'est-ce qui sort dans le SERP » mais « la durée seule peut-elle déclencher une action ». Réponse pratique retenue : selon Mueller, pas de mécanisme automatique connu, mais la clause reste dans la doc, ce qui laisse la porte ouverte à une action manuelle en cas d'abus caractérisé.

---

Draft SyntheticBrain. Édition du 17 juillet 2026, version 3. Rien envoyé. Corpus doctrine consulté via `./kb search`. Prédictions ouvertes déposées dans `ledgers/predictions.jsonl` au moment de la clôture.
