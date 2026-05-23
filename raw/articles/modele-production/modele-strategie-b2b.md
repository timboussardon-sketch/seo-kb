---
type: modele-strategie-b2b
slug: modele-strategie-b2b
title: Modèle · Stratégie SEO B2B non-locale (SaaS, agence, prestation)
auteur: Timothée Boussardon
date: 2026-05-15
parent: "[[modele-strategie]]"
pattern: "[[modele-mots-clés]]"
tags:
  - modele
  - strategie
  - b2b
  - saas
  - non-local
  - reproduction
  - anti-hallucination
related:
  - "[[modele-strategie]]"
  - "[[modele-mots-clés]]"
  - "[[skill-programmatique-pseo]]"
  - "[[skill-entites-vectorielles]]"
  - "[[skill-product-led-seo]]"
  - "[[skill-cluster-aeo]]"
  - "[[ton-de-voix-tim]]"
---

# Stratégie SEO B2B pour [SECTEUR] sur [ICP] / [VERTICAL]

Variante du modèle de référence [[modele-strategie]] pour les activités B2B non-localisées géographiquement : SaaS, agence marketing, agence design, agence dev, cabinet de conseil, prestation expertise, formation pro, plateforme de mise en relation.

**Pré-requis non négociable** : ce modèle ne marche que si `[SECTEUR]` assume une niche verticale et un use case précis. Une "agence webmarketing tout-faire pour tout le monde" est inattaquable par construction. Le pré-requis est de choisir un ICP (Ideal Customer Profile) et un use case avant la stratégie. Exemples valides : "SaaS de scoring de leads pour PME tech industrielle B2B", "agence SEO pour cabinets d'avocats spécialisés en responsabilité médicale", "prestation d'audit RGPD pour scale-up SaaS de moins de 100 personnes".

**Variables à substituer dans tout le doc** : `[SECTEUR]` (type de produit ou service), `[ICP]` (profil client idéal nommé), `[VERTICAL]` (industrie ciblée), `[INTENTION-DOMINANTE]` (demo, audit gratuit, devis, comparaison fournisseurs, etc.), `[OUTIL-PRINCIPAL]` (simulateur ROI, comparateur fournisseurs, calculateur de coût, audit en ligne, quiz de maturité, configurateur), `[DURÉE-ROADMAP]` (12 mois standard B2B vu le cycle de décision long), `[CONTRAINTES-REGLEMENTAIRES]` (RGPD données client, SOC2 si SaaS, ISO 27001, ARC, DGE, certifications métier à vérifier).

---

## Discipline data et anti-hallucination (méta-section obligatoire)

Aucune stratégie n'est publiée tant que la discipline suivante n'a pas été respectée. Identique au modèle local, plus pertinente encore en B2B où la donnée chiffrée fait la crédibilité.

### Étape 1 · Créer le sources.md avant la rédaction

Pour chaque application `[SECTEUR] + [ICP]`, créer un fichier `raw/data/strategies-b2b/[secteur]/sources.md` qui liste codes NAF, URLs canoniques (INSEE pour démographie d'entreprises, Xerfi pour études sectorielles, France Num pour numérisation PME, observatoires métiers spécifiques), variables à remplir, sources à exclure formellement.

### Étape 2 · Règle absolue de rédaction

Aucun chiffre n'apparaît dans la stratégie tant qu'il n'est pas rattaché à une ligne du sources.md avec URL canonique et date d'extraction. Placeholder explicite sinon.

### Étape 3 · Pipeline de collecte hiérarchisé B2B

Niveau 1, sources publiques structurées : INSEE base SIRENE par code NAF, France Stratégie, France Num, observatoires sectoriels (CINOV, Syntec, etc.), data.gouv.fr.

Niveau 2, sources semi-structurées : études Xerfi, panoramas Gartner / Forrester accessibles partiels, baromètres associations professionnelles (Syntec Numérique, French Tech, etc.), publications spécialisées (Maddyness, FrenchWeb, USINE-DIGITALE selon vertical).

Niveau 3, data terrain client : volumes traités, paniers moyens, durées de cycle, taux de transformation, NPS, témoignages clients vérifiés et nommés (avec accord client).

### Étape 4 · Fact-check avant publication

Chaque chiffre a une URL source consultable au jour de publication. Chaque logo client utilisé a une autorisation écrite. Chaque cas client publié a un accord daté.

### Étape 5 · Sources à exclure formellement

Pas de Semrush, pas d'Ahrefs, pas de crawl des sites concurrents pour piquer des chiffres. La data sectorielle vient des sources officielles et études référencées. La data terrain vient du client.

---

## Thèse centrale (à adapter selon le secteur)

**À l'ère du GEO, les stratégies SEO génériques ne suffisent plus pour se différencier et amener un trafic qualifié sur ses pages. Seules les pages ultra-spécialisées par expertise rankent et se font citer par les moteurs génératifs** (ChatGPT, Perplexity, Google AI Overviews).

C'est encore plus vrai en B2B qu'en local. Un CMO qui cherche un fournisseur ne tape plus "agence SEO" sur Google, il pose une question pointue à ChatGPT type "quelle agence SEO pour cabinet d'avocats spécialisé en responsabilité médicale ?", "meilleur SaaS de scoring de leads pour PME industrielle française", "comment auditer la conformité RGPD d'un SaaS RH de 30 personnes ?". Les modèles génératifs vont citer les sources qui ont publié de la matière experte sur ces requêtes précises. Les généralistes restent invisibles.

Pour un acteur du `[SECTEUR]`, ça veut dire arrêter d'attaquer le mot-clé générique (`[SECTEUR]` seul, ou pire `agence`, `SaaS`, `consultant`) et assumer une niche verticale + use case nommé. Le mot-clé cible devient `[SECTEUR] pour [ICP]` ou `[SECTEUR] [VERTICAL] [USE-CASE]`.

Quatre patterns observés (à choisir selon le secteur) :

- Spécialisation verticale ultra-niche (un seul ICP nommé, un seul use case nommé, refus assumé de servir les autres)
- Transparence radicale sur les prix et la méthode (alors que le marché B2B reste sur "demandez un devis" sans aucun repère)
- Média expert avec data sectorielle propriétaire (publier ce que personne d'autre ne publie)
- Outil Product-Led qui livre de la valeur avant la demande de demo (calculateur ROI, audit gratuit en ligne, configurateur)

La stratégie priorise la génération de leads qualifiés (SQL, MQL selon nomenclature client) plutôt que le trafic, en visant les requêtes décisionnelles à fort intent commercial.

Implémentation en roadmap trois phases ciblant **30 mots-clés prioritaires sur [DURÉE-ROADMAP] mois** (12 mois standard pour un cycle de décision B2B).

---

## 01 · Vue d'ensemble de la stratégie

[Décrire en 1 paragraphe le profil de l'ICP cible et son intention dominante au moment de la recherche. Identifier le trou de marché concret : ce que les concurrents font mal ou ne font pas sur cette niche.]

Principe central : **la seule métrique qui compte est le nombre de leads qualifiés en pipeline avec ARR ou volume de mission valorisable**, pas le trafic ou les impressions.

---

## 02 · Diagnostic marché et opportunités SEO B2B

### Contexte sectoriel

[Statistiques sectorielles : taille de marché TAM/SAM/SOM si disponible, nombre d'acteurs B2B sur la verticale, taille moyenne des deals, durée de cycle moyenne. Sources : Syntec Numérique, Xerfi, France Stratégie, observatoires métier.]

### Diagnostic concurrentiel digital

[Mapping rapide des concurrents directs sur les requêtes décisionnelles : qui ranke, sur quoi, avec quelle valeur ajoutée. Identifier les requêtes où la SERP est polluée par les comparateurs génériques (G2, Capterra, Wynd, Sortlist) sans expert métier de référence.]

### Proposition d'angle différenciant

[En une phrase, le positionnement différenciant. Exemple SaaS : "seul SaaS de scoring de leads conçu spécifiquement pour les PME industrielles B2B françaises avec intégration Sage/EBP native". Exemple agence : "seule agence SEO qui ne sert que les cabinets d'avocats spécialisés en responsabilité médicale et publie son taux de réussite anonymisé".]

---

## 03 · Trois facteurs de ranking Google pour 2026

Section invariante. Ces 3 facteurs s'appliquent à tous les secteurs B2B.

### 1. Surprise · Apporter une information que les autres ne donnent pas

Google récompense les pages qui ajoutent une information neuve à la requête, pas celles qui répètent ce que les comparateurs et annuaires disent déjà.

Pour chaque requête cible, lister ce que les pages classées 1-10 disent et identifier ce qu'elles ne disent pas. La donnée terrain propriétaire (taux de conversion observés, ARR moyen par segment, durée d'implémentation réelle, ROI mesuré chez les clients, mix marchés cibles) que personne ne publie est exactement ce qui ranke.

Le moat n'est ni le branding ni le territoire : c'est l'information sectorielle que vous seul pouvez publier parce que vous l'avez vue sur 50+ clients.

### 2. Densité d'information · Ne pas blablater pour rien dire

Chaque ligne apporte une information ou un chiffre. Pas de phrase de transition, pas de paraphrase, pas de "comme nous l'avons dit", pas de mise en bouche marketing.

Une bonne page B2B tient en 1500-2000 mots avec 40 informations utiles (chiffres, exemples nommés, comparatifs précis), pas en 4000 mots avec les mêmes informations diluées dans du remplissage corporate.

Test simple : si on retire une phrase, est-ce qu'un acheteur B2B perd un repère pour décider ? Si non, à retirer.

### 3. Utilité concrète pour le visiteur

Google fait évaluer ses résultats par des évaluateurs humains. Pour une requête transactionnelle B2B, la page qui mérite la note maximale délivre tout de suite : `[OUTIL-PRINCIPAL]` ou fourchette de prix indicative, cas clients comparables nommés, durée d'implémentation, prérequis techniques, contact direct accessible.

Les outils interactifs (calculateur de ROI, audit en ligne, configurateur) et les CTA transparents font mieux que les formulaires de demande de demo qui cachent le prix.

Commun aux 3 facteurs : aucun ne récompense le volume. Tous récompensent l'information neuve, la concentration informationnelle, et l'utilité pour l'acheteur B2B.

---

## 04 · Cocon sémantique et architecture de pages

L'architecture du site suit une hiérarchie en trois niveaux. Une page mère par grand sujet (cas d'usage principal, verticale ICP, méthode), des pages filles qui traitent les sous-sujets précis, et des pages petites-filles pour les requêtes ultra-spécifiques (longue traîne décisionnelle métier).

Le maillage entre toutes ces pages se fait à la main, lien par lien, sans plugin automatique. C'est ce qui distingue un site qui ranke d'un site qui empile du contenu sans cohérence.

Concrètement, on commence par identifier 30 mots-clés décisionnels, on construit le cocon sémantique autour, et on publie environ 10 pages par mois.

### Cocon 1 · [USE CASE PRINCIPAL]
[Le cocon le plus transactionnel : le use case central que le SaaS résout ou la prestation principale. Exemple SaaS scoring : "scoring de leads B2B industriel". Exemple agence : "SEO cabinet d'avocats". 5 à 8 mots-clés décisionnels.]

### Cocon 2 · [USE CASES ADJACENTS]
[Sous-intentions concrètes adjacentes au use case principal. Pour un SaaS scoring : qualification leads inbound, enrichissement données, intégrations CRM. 4 à 6 mots-clés.]

### Cocon 3 · [VERTICAL CIBLÉ]
[Pages spécifiques par verticale ICP. Exemple : SaaS scoring pour industrie, pour ESN, pour cabinets de conseil. Si un seul ICP, ce cocon décline les sous-segments. 4 à 6 mots-clés.]

### Cocon 4 · [TRANSPARENCE PRIX ET MÉTHODE]
[Le cocon "rassurance" B2B : grille tarifaire publique (ou fourchette), méthodologie détaillée, durée d'implémentation, garanties. Rarissime en B2B donc différenciant fort. 4 à 6 mots-clés.]

### Cocon 5 · [LONGUE TRAÎNE USE CASE PRÉCIS]
[Combinaisons use case + taille entreprise + budget + intégration : "SaaS scoring leads 50-200 salariés intégration Salesforce 500 euros mois". 4 à 6 mots-clés.]

### Cocon 6 · [GUIDES ET CONFIANCE]
[Comparaisons fournisseurs (sans noms de concurrents), check-lists d'achat, glossaires métier, critères de choix, anti-greenwashing/anti-bullshit. 3 à 5 mots-clés.]

---

## 05 · Ancrage cas client et preuves métier

Une page service B2B sans cas client ne ranke pas et ne convertit pas. La crédibilité passe par : études de cas nommées avec chiffres clients vérifiés (avec accord signé), logos clients avec lien vers étude de cas correspondante, témoignages vidéo de clients identifiés (CEO, CMO, RevOps), publications conjointes avec clients (co-webinaires, co-études, prises de parole croisées).

Pas de logo client sans étude de cas associée. Pas d'étude de cas sans chiffre vérifié et daté. Pas de témoignage anonyme.

Signaux E-E-A-T spécifiques B2B : certifications métier (SOC2 Type II, ISO 27001, RGPD ARC, DGE, agréments sectoriels), avis G2 / Capterra / TrustRadius / Welcome to the Jungle selon segment, prises de parole conférences sectorielles datées, publications media spécialisé.

---

## 06 · Roadmap opérationnelle en trois phases

### Phase 1 (mois 0 à 3) · Pages décisionnelles + `[OUTIL-PRINCIPAL]`

- Déployer 10 pages par mois sur les requêtes décisionnelles haute valeur (cocons 1, 2, 3 prioritairement)
- Intégrer `[OUTIL-PRINCIPAL]` sur chaque page ciblée : signal de qualité minimum, note maximale si la valeur est délivrée dans la page
- Optimiser présence G2 / Capterra / Sortlist (ou équivalent vertical) : descriptif, screenshots, premiers avis vérifiés
- Implémenter la structure H1 H2 pour le [[passage-ranking]] : chaque H2 égale 150 à 200 mots autonomes
- Poser le maillage interne dès la semaine 1
- Vérifier l'indexation Search Console sous 48 heures

### Phase 2 (mois 3 à 6) · Études de cas + longue traîne + transparence prix

- Publier 3 à 5 études de cas clients détaillées avec chiffres vérifiés (durée, ROI, MRR ou pipeline débloqué)
- Déployer le cocon 4 (transparence prix et méthode) : page tarifs publique ou fourchette, FAQ honoraires / abonnements
- Créer les pages longue traîne cocon 5 (use case + taille entreprise + intégration spécifique)
- Ajouter des éléments E-E-A-T : interventions conférences sectorielles, publications media référencées, livres blancs téléchargeables (capture email)
- Produire 5 à 10 vidéos courtes (vecteurs multimodaux) : visite produit, témoignage client, intervention CEO sur sujet vertical
- Lancer le cocon 6 (guides et confiance)

### Phase 3 (mois 6 à 12) · Newsletter, podcast, communauté

- Lancer une newsletter mensuelle B2B : 1 édition égale 1 sujet sectoriel pointu (data terrain, décryptage tendance, étude de cas anonyme)
- Format : data terrain plus analyse expert plus conseil actionnable plus offre directe ou audit gratuit
- Thèmes prioritaires : retour d'expérience client, panorama sectoriel daté, comparaison de méthodes, anti-bullshit
- Publier chaque édition comme article du site : signal de récence plus potentiel de backlink naturel
- Lancer ou être invité sur des podcasts métier (canal backlink B2B sous-exploité)
- Animer ou participer à une communauté Slack/Discord vertical, Substack co-author, LinkedIn newsletter
- Fidéliser le segment direct : la base email est l'actif principal en B2B (vs base prospects louée chez comparateur)
- Mesurer les recherches de marque : la hausse de "[nom de votre marque] [use case]" égale signal qualité pour les LLMs

---

## 07 · `[OUTIL-PRINCIPAL]` · Le différenciateur principal

[Décrire la mécanique du calculateur, simulateur, audit ou configurateur central à la stratégie.]

Mécanique type B2B : **[VARIABLE 1] + [VARIABLE 2] + [VARIABLE 3] = [VALEUR FOURNIE IMMÉDIATEMENT] + capture email pro**.

Exemples de combinaisons à implémenter (à adapter au secteur) :

- Calculateur ROI : taille équipe + volume mensuel + outil actuel → économie ou gain annuel projeté + capture email
- Audit en ligne : URL du site + verticale + objectif → diagnostic en 10 points + capture email pour rapport détaillé
- Configurateur : besoin métier + taille structure + intégrations souhaitées → recommandation produit + tarif estimé + capture email
- Quiz de maturité : 10 questions sur la pratique actuelle → niveau de maturité + axes d'amélioration prioritaires + capture email
- Comparateur de méthodes : critères de choix + contexte → comparaison personnalisée + capture email

Pourquoi ça fonctionne : la plupart des acteurs B2B cachent la valeur derrière une demande de demo. L'outil casse le pattern. Il répond à la première question universelle de l'acheteur ("ça va me coûter quoi, ça va me rapporter quoi, est-ce que c'est fait pour moi ?") avant d'exiger un appel commercial. Page que Google considère comme répondant parfaitement à l'intention, lead qualifié à la sortie.

---

## 08 · Idées de mots-clés décisionnels

Un mot-clé décisionnel B2B est une requête tapée par un acheteur prêt à comparer les options et passer à l'acte : il connaît son problème, il cherche le bon fournisseur ou la bonne méthode. À l'opposé des requêtes d'exploration "qu'est-ce que le SEO B2B" qui veulent juste comprendre un sujet.

Format de la matrice (à remplir avec les 30 mots-clés du secteur) :

```
mot-clé, intention, cocon associé, mois de production, format ou outil
```

Exemple de ligne SaaS scoring : `meilleur saas scoring leads pme industrielle, transactionnel, cocon 3, M1, comparateur intégré`

Légende des mois :
- **M1** : impact business immédiat, à lancer Phase 1
- **M2** : mois 2 à 3 de production, Phase 1 fin et début Phase 2
- **M3** : mois 4 à 12, Phase 2 et Phase 3

Distribution typique observée en B2B :
- 7 à 10 mots-clés en M1 (les plus décisionnels, type "meilleur [SECTEUR] pour [ICP]", "comparatif [SECTEUR]", "alternative à [concurrent générique]")
- 10 à 12 mots-clés en M2 (le cœur de la matrice, intentions claires, use case précis)
- 8 à 12 mots-clés en M3 (longue traîne, ultra-niche par taille entreprise + intégration + budget, requêtes IA)

---

## 09 · Erreurs critiques à éviter

- Cacher les prix derrière "demandez un devis" : inverse le signal d'utilité que Google récompense, et fait fuir 60% des acheteurs en phase de short-list
- Acheter des backlinks : créer du contenu si utile qu'il génère des liens naturels (podcasts métier, presse spécialisée, partenaires verticaux)
- Page "Agence SEO" générique sans verticale : segmenter par ICP, par use case, par intégration
- Audit 6 mois avant publication : publier 30 mots-clés rapidement, indexer, observer Search Console
- Zéro preuve d'expertise visible : afficher certifications, logos clients (avec accord), prises de parole, publications datées
- Demande de demo sans contexte tarifaire : `[OUTIL-PRINCIPAL]` interactif avant la prise de contact
- Contenu IA générique non supervisé : filtré aux mises à jour majeures Google, demande data terrain et angle métier identifiable
- Multiplier les pages "pour SaaS / pour PME / pour scale-up" sans data verticale réelle
- Page speed avant contenu : 80 % contenu, 20 % technique, l'indexation bat la vitesse
- Négliger la newsletter ou le podcast Phase 3 : c'est le meilleur générateur de backlinks naturels B2B et le seul actif que vous possédez (vs base prospects louée chez comparateur)

---

## 10 · Checklist de lancement semaine 1

1. Valider les 30 mots-clés décisionnels avec data prospection terrain (CRM, qualification leads sortants, retours commerciaux)
2. Construire le cocon sémantique (mère, filles, petites-filles) sur spreadsheet avant production
3. Optimiser les fiches sur G2 / Capterra / Sortlist / Welcome to the Jungle (selon segment) avec descriptifs précis et premiers avis vérifiés
4. Publier la première landing page sur la requête principale avec `[OUTIL-PRINCIPAL]` intégré
5. Intégrer les avis G2 / Capterra directement sur la page (pas en liens externes)
6. Vérifier l'indexation en Search Console sous 48 heures après publication
7. Définir le planning de publication : 10 pages par mois avec assignations de mots-clés par cocon
8. Écrire la page mère cocon avec structure [[passage-ranking]] : chaque H2 égale réponse autonome 150 à 200 mots
9. CTA principal accessible above the fold : `[OUTIL-PRINCIPAL]` ou demo flexible plus contact direct
10. Configurer le tracking des conversions réelles (MQL, SQL, leads qualifiés) plutôt que vanity metrics (sessions, impressions)

---

## 11 · FAQ stratégique

Cinq questions canoniques observées sur les applications B2B publiées. À adapter au secteur tout en gardant la structure.

### Pourquoi `[OUTIL-PRINCIPAL]` plutôt qu'un formulaire de demo ?

[Réponse type : parce qu'un acheteur B2B veut savoir combien ça coûte, combien ça rapporte, et si c'est fait pour son contexte avant de booker un appel commercial. L'outil capte cette intention, donne une réponse utile en moins de 2 minutes, et l'acheteur décide d'aller plus loin. Google récompense les pages qui répondent directement à l'intention du visiteur. C'est aussi la meilleure défense contre les comparateurs génériques qui captent la requête sans expertise verticale.]

### Combien de temps avant les premiers leads qualifiés en pipeline ?

[Réponse type : 3 à 4 mois sur les requêtes décisionnelles ultra-spécialisées (longue traîne use case précis). 6 à 9 mois pour accrocher les premières positions sur les requêtes plus disputées type "meilleur [SECTEUR] pour [ICP]". Le cycle de décision B2B étant long (3 à 9 mois entre première recherche et signature), l'engagement total se mesure sur 12 à 18 mois.]

### Faut-il vraiment des backlinks pour ranker en B2B sur une niche ?

[Réponse type : oui mais pas n'importe lesquels. Pas les annuaires DA80 génériques tech. Ce qui compte : la presse métier (Maddyness, FrenchWeb, USINE-DIGITALE, JDN selon vertical), les podcasts sectoriels, les communautés Slack/Discord verticales, les newsletters Substack indépendantes du segment, les co-publications avec clients ou partenaires. Un backlink métier pertinent vaut cinquante backlinks d'annuaires obsolètes.]

### 30 mots-clés c'est suffisant pour couvrir une niche B2B ?

[Réponse type : largement suffisant. La matrice de combinaisons (intention, taille entreprise, intégration, budget, use case sous-précis) couvre les vrais cas d'usage qui génèrent des leads qualifiés. Au-delà, on dilue l'autorité sur des requêtes à très faible volume. Mieux vaut 30 pages qui rankent et convertissent que 200 qui plafonnent et ne génèrent que du trafic non qualifié.]

### Comment se différencier des comparateurs B2B qui dominent la SERP de mon segment ?

[Réponse type : trois leviers concrets. Premièrement, la longue traîne décisionnelle ultra-spécialisée (use case précis + taille entreprise + intégration + budget) que les comparateurs ne couvrent pas. Deuxièmement, `[OUTIL-PRINCIPAL]` qui donne la valeur avant la prise de contact. Troisièmement, études de cas clients nommées avec chiffres vérifiés et accord signé. C'est ce qui transforme une SERP polluée par les comparateurs génériques en avantage : on devient l'expert identifié sur la verticale.]

---

## 12 · À retenir

La stratégie SEO B2B 2026 priorise la précision verticale sur le volume, les use cases ultra-spécifiques sur les mots-clés génériques, et la captation directe sur la dépendance aux comparateurs. Implémentation sur 12 mois en 3 phases, avec insistance sur la data terrain propriétaire (chiffres clients, taux de conversion observés, durées de cycle), la concentration informationnelle, et les marqueurs E-E-A-T spécifiques au segment (certifications SOC2 ISO RGPD, logos clients vérifiés, prises de parole sectorielles datées).

Le moat ultime n'est ni le branding ni la levée de fonds : c'est la data terrain propriétaire et la verticalisation assumée que ni un concurrent généraliste ni un comparateur ne peuvent reproduire, et que les moteurs génératifs priorisent en citation.

---

## Notes pour adapter le template à un nouveau secteur B2B

Quatre variables principales varient systématiquement d'une application à l'autre. Le reste est invariant.

**Variable 1 · La durée de roadmap.** 12 mois standard pour la plupart des activités B2B (cycle de décision long). 18 mois pour les deals entreprise/grands comptes avec procurement complexe (SaaS enterprise, conseil stratégique, infra critique). 9 mois pour les segments PME-PME courts (formation, agence projet ponctuel).

**Variable 2 · L'outil Product-Led principal.** Toujours présent, mais sa nature change selon le segment. Calculateur ROI pour les SaaS avec valeur quantifiable (productivité, économie, MRR débloqué). Audit en ligne pour les agences (SEO, design, dev, RGPD). Configurateur pour les outils à plusieurs intégrations / options. Quiz de maturité pour les segments où l'acheteur ne sait pas où il en est (data, transformation digitale, cybersécurité). Comparateur transparent pour les marchés saturés où l'on assume une comparaison honnête.

**Variable 3 · Les 6 cocons sémantiques.** La structure en 6 cocons est invariante, mais le contenu de chaque cocon dépend du secteur. Le cocon 3 "Verticale ciblée" est spécifique au B2B et remplace la géographie locale. Le cocon 4 "Transparence prix" est encore plus différenciant en B2B qu'en local car le standard de marché reste "demandez un devis".

**Variable 4 · Le niveau de spécialisation verticale.** Le pré-requis non négociable du modèle. Si `[SECTEUR]` ne peut pas assumer une niche verticale + use case nommé, le modèle ne marche pas et la conclusion est de revenir à la table de l'offre avant de faire du SEO. Test de validité : peut-on écrire "seul `[SECTEUR]` qui sert exclusivement `[ICP]` sur `[USE-CASE]`" sans mentir ? Si oui, le modèle s'applique. Si non, retravailler le positionnement d'abord.

**Variable 5 · Les contraintes réglementaires sectorielles.** Variable héritée du modèle local. En B2B, particulièrement critique pour santé (RGPD données de santé, HDS), finance (AMF, ACPR), conseil en investissement, données personnelles (CNIL, RGPD), cybersécurité (ANSSI, SecNumCloud). Si applicable, valider chaque page côté juridique avant publication.

Tout le reste (les 3 facteurs de ranking, l'ancrage cas client, la roadmap 3 phases, le format de matrice 30 mots-clés, la checklist semaine 1, la structure FAQ, et surtout la discipline data anti-hallucination en méta-section) est repris pixel-perfect d'une application à l'autre.

---

## Sources et liens

- Modèle parent : [[modele-strategie]] (variante locale, applications Lyon et Paris)
- Pattern global : [[modele-mots-clés]]
- Skills mobilisés : [[skill-programmatique-pseo]], [[skill-entites-vectorielles]], [[skill-product-led-seo]], [[skill-cluster-aeo]], [[ton-de-voix-tim]]
- Concepts liés : [[e-e-a-t]], [[fully-meets]], [[passage-ranking]], [[product-led-seo]], [[anti-ai-writing]], [[data-proprietaire]], [[surprise-score]], [[densite-information]]

## Différences-clés avec [[modele-strategie]] (variante locale)

| Section | Modèle local | Modèle B2B non-local |
|---|---|---|
| Variable principale | `[VILLE]` | `[ICP]` + `[VERTICAL]` |
| Section 02 contexte | Statistiques nationales + opportunité ville | Statistiques sectorielles + diagnostic concurrentiel digital |
| Section 05 ancrage | Photos chantiers géolocalisés, partenariats locaux, Google Business Profile | Études de cas nommées, logos clients, certifications SOC2/ISO, présence G2/Capterra |
| Cocon 5 | Géographie précise (arrondissements, quartiers) | Use case + taille entreprise + intégration |
| Erreurs cocon 4 | Cacher les prix | Cacher prix + cacher méthode |
| Phase 3 backlinks | Presse locale, mairies, partenaires métier zone | Podcasts métier, presse sectorielle, communautés verticales, Substack |
| Métrique principale | Nombre de devis qualifiés signés | Nombre de leads qualifiés en pipeline (MQL/SQL, ARR ou volume mission)|
| Pré-requis non négociable | Légitimité terrain (SIRET, ancrage local réel) | Spécialisation verticale + use case nommé (refus du généralisme) |
