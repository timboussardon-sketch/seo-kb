# Briefs techniques — 4 outils Product-Led SEO pour fusionn.co

Préparé le 2026-05-23. Spec ready-to-code, doctrine-grounded sur le vault Tim.

## Principes communs aux 4 outils

- **Pas de gate, accès gratuit illimité** (choix produit Tim).
- **Routes 100% mot-clé exact** sans préfixe `/outils/`.
- **Une vraie page SEO par outil** : H1, sous-titre, copy lourde en doctrine, FAQ 8-10 questions, maillage interne. Page = pilier outil + outil dans la même URL.
- **Doctrine de Tim partout** : pas de blabla générique, on cite les positions tranchées (mots-clés actionnels, tabou visibilité, Imp_pos, etc.).
- **Footer** : nouvelle section "Outils" qui liste les 4 outils (cf. section finale).
- **Maillage** : chaque outil pointe vers `/compte` (page Do principale, conversion) + 2 autres outils + 1 article de blog pertinent.

---

# OUTIL 1 — Score Business d'un mot-clé

## URL et SEO

| | |
|---|---|
| **Slug** | `/score-business-mot-cle` |
| **H1** | Score Business d'un mot-clé : ce que Google ne dit pas |
| **Meta title** | Score Business mot-clé : calculer le vrai potentiel SEO (gratuit) |
| **Meta description** | Le volume Google ne dit rien du potentiel business d'un mot-clé. Notre score 0-100 mesure la probabilité de conversion réelle, pas le trafic. Test gratuit. |
| **Requêtes cibles** | score business mot-clé · calculer potentiel mot-clé seo · outil score mot-clé gratuit · ce mot-clé est-il rentable · valeur business mot-clé |

## Hero

```
[H1] Score Business d'un mot-clé : ce que Google ne dit pas

[Sous-titre] Le volume ne mesure que le trafic. Notre score 0-100 mesure 
la probabilité que la requête devienne un lead ou une vente. Saisissez 
votre mot-clé, on vous renvoie son score, son CPC, son intent et 5 
variantes à plus fort potentiel.

[Input : mot-clé]  [Bouton rouge : Calculer mon score]

3 outils proposés : Comparateur Volume vs Business · Test citation IA · Générateur Hn
```

## UI mockup

```
┌──────────────────────────────────────────────────────────────┐
│  agence seo paris                            [Calculer]      │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│        Score Business                                        │
│                                                              │
│              ╭───╮                                          │
│              │ 89│   High                                   │
│              ╰───╯                                          │
│                                                              │
│        CPC estimé : 12,40 €                                 │
│        Intent : Décisionnel + Transactionnel (actionnel)    │
│        Verdict : Mot-clé prioritaire à attaquer en page 1   │
│                                                              │
│        Pourquoi ce score ?                                   │
│        ✓ Modificateur géo "paris" = intention business      │
│        ✓ CPC élevé = compétition publicitaire = ROI prouvé  │
│        ✓ Pas saturé par les LLMs (substitution échoue)      │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  5 variantes à fort potentiel à attaquer ensuite             │
│  ─────────────────────────────────────────────────────────   │
│  agence seo paris pas cher              78  High             │
│  meilleure agence seo paris             74  High             │
│  tarif agence seo paris                 71  Medium           │
│  agence seo paris pour startup          66  Medium           │
│  audit gratuit agence seo paris         63  Medium           │
└──────────────────────────────────────────────────────────────┘

[CTA bloc noir] Analysez 100 mots-clés d'un coup avec Fusionn → /compte
```

## Inputs / Outputs

**Input** : 1 mot-clé (texte, 200 chars max, sanitize lowercase + trim).

**Output** :
- Score Business 0-100 (badge coloré High/Medium/Low)
- CPC estimé en euros
- Intent classification : Informationnel / Comparatif / Décisionnel / Transactionnel / Actionnel (= déci + trans, terme Tim)
- Verdict 1-phrase
- 3 raisons du score (bullet)
- 5 variantes longue traîne avec leur score

## Backend / Logique

**Endpoint** : `POST /functions/v1/keyword-business-score` (Supabase Edge Function existante à étendre, sinon créer)

**Algorithme** (déjà en prod côté Fusionn, à exposer en mode 1-shot) :
1. Normalise le mot-clé
2. Récupère CPC + volume via Google Ads (cache si dispo)
3. Calcule Score Business via algo Fusionn : `f(CPC, intent_signals, modificateurs_geo, longue_traîne_match, action_verbs)`
4. Classifie intent par regex sur modificateurs (`prix|tarif|comparatif|comment` etc.)
5. Test substitution LLM (heuristique) : si le mot-clé est un "qu'est-ce que", probabilité substitution élevée → minore le score
6. Génère 5 variantes via expansion semantic (déjà en prod) avec scoring

**Coût token** : 1 call Gemini Flash ~600 tokens out pour les variantes. Score lui-même est déterministe (0 token).

## FAQ doctrine-grounded (8 questions)

```
Q1. Pourquoi pas le volume Google ?

Parce qu'il est faussé. Les outils SEO classiques (Ahrefs, Semrush) 
projettent leur data depuis le marché anglophone et ne mesurent que 
le trafic, pas la conversion. Un mot-clé à 10 recherches mensuelles 
peut avoir un CPC de 100-200 € et générer dix fois plus de leads 
qu'un mot-clé à 5 000 recherches purement informationnelles.

Q2. C'est quoi un "mot-clé actionnel" ?

Terme signature de Tim : un mot-clé à la fois décisionnel ET 
transactionnel. L'utilisateur attend une action — démo, devis, 
contact, achat — pas juste une info. C'est le seul type qui génère 
du chiffre d'affaires en SEO B2B aujourd'hui.

Q3. Comment le Score Business est-il calculé ?

Trois signaux pondérés : (1) le CPC réel Google Ads, qui prouve 
qu'un marché paie pour la requête ; (2) la proximité avec une 
action (verbes "comparer", "calculer", "demander", modificateurs 
géo, longue traîne décisionnelle) ; (3) le test de substitution 
LLM — un mot-clé que ChatGPT peut traiter mieux que vous est mort 
avant d'exister.

Q4. Quel score viser ?

High (70-100) = pages à créer en priorité, attaque immédiate. 
Medium (40-69) = à intégrer dans le cluster du High correspondant 
(maillage). Low (0-39) = à éviter ou à traiter en FAQ, pas en page 
dédiée.

Q5. Pourquoi le CPC compte plus que le volume ?

Le CPC est la seule métrique de marché libre dans Google Ads. 
Personne ne paie 50 € pour un clic qui ne convertit pas. Le CPC 
est donc un proxy direct du potentiel business, contrairement au 
volume qui mesure juste l'intérêt général.

Q6. Ça remplace mes outils SEO classiques ?

Non. Le Score Business ne remplace pas Ahrefs ou Semrush, il 
remplace leur métrique "volume" comme critère de priorisation. 
Vous gardez vos outils pour le crawl et les backlinks, mais vous 
arrêtez de hiérarchiser vos mots-clés par leur trafic potentiel.

Q7. Et pour les LLMs (ChatGPT, Perplexity) ?

Les LLMs convertissent 4x plus que Google organique sur le même 
mot-clé (étude SEMrush). Notre score intègre la probabilité de 
citation LLM via le test de substitution : un mot-clé sur lequel 
ChatGPT ne sait pas répondre seul est un mot-clé à fort potentiel 
AEO.

Q8. Vous pouvez analyser plusieurs mots-clés d'un coup ?

Pas ici (un mot-clé à la fois). Pour batcher 100 mots-clés et 
voir leur Score Business comparé au volume, utilisez le 
[Comparateur Volume vs Business](/comparateur-volume-business-seo) 
ou ouvrez un compte Fusionn (3 requêtes gratuites).
```

## Maillage interne

**Liens sortants in-body** (in-FAQ + dans le copy de la page) :
- → `/comparateur-volume-business-seo` (ancre : "Comparateur Volume vs Business")
- → `/compte` (ancre : "ouvrir un compte Fusionn")
- → `/test-citation-chatgpt-perplexity` (ancre : "test de citation LLM")
- → `/blog/pourquoi-88-pourcent-sites-seo-napparaissent-pas-dans-ia` (article pilier B)

---

# OUTIL 2 — Comparateur Volume vs Score Business

## URL et SEO

| | |
|---|---|
| **Slug** | `/comparateur-volume-business-seo` |
| **H1** | Le volume Google ne suffit plus : comparez 10 mots-clés sur leur vrai potentiel business |
| **Meta title** | Comparateur Volume vs Score Business : prioriser ses mots-clés (gratuit) |
| **Meta description** | Le volume tue. Comparez vos 10 mots-clés sur leur Score Business 0-100 et identifiez le champion caché qui vous échappe. Gratuit, sans inscription. |
| **Requêtes cibles** | comparer mots-clés seo · mots-clés à fort potentiel business · volume seo ne sert à rien · prioriser ses mots-clés · calculer roi mot-clé · champion caché seo |

## Hero

```
[H1] Le volume Google ne suffit plus

[Sous-titre] Vous avez 10 mots-clés en tête. Le volume dit "attaque celui 
de 5000". Le Score Business dit "attaque celui de 30". Lequel a raison ? 
Collez vos mots-clés, on vous montre votre champion caché.

[Textarea : 10 mots-clés (un par ligne)]
[Bouton rouge : Lancer la comparaison]
```

## UI mockup

```
┌──────────────────────────────────────────────────────────────┐
│ Collez 10 mots-clés (un par ligne)                            │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ agence seo                                                │ │
│ │ agence seo paris                                          │ │
│ │ comment choisir agence seo                                │ │
│ │ tarif agence seo                                          │ │
│ │ ...                                                       │ │
│ └──────────────────────────────────────────────────────────┘ │
│                              [Comparer les 10 mots-clés]      │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Mot-clé                  Volume   Score Business   Gap        │
│ ─────────────────────────────────────────────────────────    │
│ agence seo                14 800        38           -36       │
│ agence seo paris           2 400        89           +52       │  ⭐
│ comment choisir...         3 600        41             0       │
│ tarif agence seo             880        71           +28       │  ⭐
│ ...                                                          │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ ⭐ Votre champion caché : "agence seo paris"                  │
│                                                              │
│ 6,2x moins de volume que "agence seo" mais 2,3x plus de       │
│ Score Business. Si vous deviez n'attaquer qu'un mot-clé,      │
│ c'est celui-là.                                              │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [Graphique scatter plot]                                    │
│   Score                                                       │
│    100│           ⭐                                          │
│       │     •  •                                              │
│     50│        •     •                                        │
│       │              •      •                                 │
│      0└────────────────────────  Volume                       │
└──────────────────────────────────────────────────────────────┘

[CTA] Comparez 50 mots-clés en une fois sur Fusionn → /compte
```

## Inputs / Outputs

**Input** : textarea 10 lignes max (10 mots-clés), validation côté client (max 10, dédup).

**Output** :
- Tableau trié par Score Business desc : Mot-clé | Volume | Score | Bucket | Gap (Score - Volume_normalisé)
- "Champion caché" : le mot-clé avec le Gap maximum (volume bas mais score haut)
- Scatter plot Volume × Score avec champion en étoile
- Recommandation page-type pour chaque mot-clé (article cluster / page money / FAQ-page / à jeter)

## Backend / Logique

**Endpoint** : `POST /functions/v1/keywords-batch-score` (créer, batch les 10 keywords).

**Algorithme déterministe** :
1. Pour chaque mot-clé : appel à l'algo Score Business (mutualisé avec Outil 1)
2. Normalise les volumes (log-scale) pour la comparaison
3. Calcule le Gap : `score - log10(volume) * 10`
4. Identifie le champion = max(Gap)
5. Pour chaque mot-clé, recommande un format selon (score, volume, intent)

**Coût token** : 0 tokens. **Entièrement déterministe.** Le call à Google Ads pour les volumes/CPC est rate-limité côté Fusionn (cache 30j).

## FAQ doctrine-grounded (8 questions)

```
Q1. Pourquoi mettre fin au volume comme métrique ?

Trois raisons : (1) la data des outils SEO est projetée, pas réelle, 
et souvent calibrée sur le marché anglophone ; (2) un mot-clé à 500 
recherches peut rapporter moins qu'un mot-clé à 10 recherches si le 
CPC est 20x plus élevé ; (3) les requêtes à zéro volume mesuré 
cachent souvent des micro-intentions très qualifiées invisibles 
pour les outils.

Q2. C'est quoi le "Gap de Décision" ?

C'est la différence entre ce que dit le volume (priorise gros) et 
ce que dit le Score Business (priorise CPC + intent). Un Gap 
positif élevé = champion caché. Un Gap négatif = piège à trafic 
qui ne convertit pas.

Q3. Combien de mots-clés je peux comparer ?

10 mots-clés gratuitement et sans inscription. Pour batcher 50 à 
100 mots-clés (avec ajout automatique des variantes longue traîne 
de chaque), passez par Fusionn (3 requêtes gratuites).

Q4. Pourquoi le champion caché est souvent le bon choix ?

Parce que la concurrence n'a pas encore détecté l'opportunité. Les 
agences classiques visent les gros volumes : la SERP est saturée, 
les budgets backlinks sont énormes. Le champion caché a moins de 
concurrence ET plus de potentiel business → c'est le meilleur ROI.

Q5. Le volume ne sert vraiment à rien ?

Un peu, comme indicateur secondaire pour limiter le risque sur les 
mots-clés à zéro signal CPC. Mais il ne doit plus être le critère 
de priorisation principal. La hiérarchie de Tim : (1) intérêt 
business direct, (2) intérêt sémantique, (3) CPC, (4) volume en 
dernier ressort.

Q6. Comment vous calculez le CPC ?

Via la donnée Google Ads (Keyword Planner) — la seule source réelle 
et fiable du marché. Si un annonceur paie 50 € pour un clic, c'est 
qu'il a chiffré le LTV. Le CPC est donc le proxy le plus honnête 
du potentiel business.

Q7. Ça marche pour le B2B et le B2C ?

Oui pour les deux, avec une nuance : en B2C grand public (mode, 
food), le volume reste un indicateur utile parce que l'AOV est 
bas et la conversion fonctionne au volume. En B2B / services / 
SaaS, le Score Business surclasse systématiquement le volume.

Q8. Comment l'utiliser dans ma stratégie de contenu ?

Trois règles : (1) attaquez d'abord les High Score Business, peu 
importe leur volume ; (2) groupez les Medium autour du High 
correspondant pour créer un cluster (méthode du quadrillage 
sémantique) ; (3) ignorez ou traitez en simple FAQ les Low qui 
ont du volume mais zéro intent business.
```

## Maillage interne

- → `/score-business-mot-cle` (ancre : "Score Business d'un mot-clé")
- → `/compte` (ancre : "Fusionn")
- → `/structure-h2-h3-seo` (ancre : "générer une structure Hn pour vos champions")
- → `/blog/quadrillage-semantique-strategie-seo-face-ia` (ancre : "quadrillage sémantique")
- → `/blog/trouver-mots-cles-pertinents` (ancre : "méthodologie de sélection des mots-clés")

---

# OUTIL 3 — Générateur de structure Hn

## URL et SEO

| | |
|---|---|
| **Slug** | `/structure-h2-h3-seo` |
| **H1** | Structure H2/H3 SEO : générer un plan d'article qui ranke (gratuit) |
| **Meta title** | Générateur structure Hn SEO : plan d'article par mot-clé (gratuit) |
| **Meta description** | Donnez un mot-clé, recevez la structure Hn complète, avec micro-intentions intégrées et passage ancré prêt pour Position 0. Méthode Fusionn. |
| **Requêtes cibles** | structure h2 h3 seo · plan d'article seo · générateur plan seo gratuit · structure hn par mot-clé · structure article seo |

## Hero

```
[H1] Structure H2/H3 SEO : un plan d'article qui ranke en 10 secondes

[Sous-titre] Le passage ranking de Google ne ranke plus la page entière, 
il ranke chaque H2 séparément. Notre générateur sort une structure Hn 
qui matche les micro-intentions de la SERP, avec un passage ancré déjà 
positionné pour l'AI Overview.

[Input : mot-clé]
[Select : B2B / B2C / Local]
[Bouton rouge : Générer la structure]
```

## UI mockup

```
┌──────────────────────────────────────────────────────────────┐
│ Mot-clé : agence seo paris      Type : B2B          [Générer] │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ H1 : Agence SEO Paris : comment choisir la bonne en 2026     │
│                                                              │
│ Passage ancré (150-200 mots, à mettre dans les 300 premiers) │
│ ────────────────────────────────────────────────────────     │
│ Une agence SEO Paris coûte entre 1 500 et 8 000 € par mois.  │
│ La fourchette dépend de trois variables : la complexité de   │
│ votre SERP, votre maturité interne SEO, et le nombre de       │
│ pages à optimiser. [...]                                     │
│                                                              │
│ Plan Hn ─────────────────────────────────────────────────    │
│ ▼ H2 : Combien coûte une agence SEO à Paris en 2026 ?        │
│     intent : décisionnel (CPC élevé)                         │
│     ↳ H3 : Tarification au forfait vs à la performance        │
│     ↳ H3 : Cas client : ROI moyen observé                    │
│                                                              │
│ ▼ H2 : Critères pour choisir une bonne agence SEO Paris      │
│     intent : comparatif (décisionnel)                        │
│     ↳ H3 : E-E-A-T : signaux d'expertise à exiger            │
│     ↳ H3 : Méthode propriétaire vs templates                 │
│                                                              │
│ ▼ H2 : Audit gratuit : ce qu'une bonne agence vous donne     │
│     intent : actionnel (test de conversion)                   │
│                                                              │
│ ▼ H2 : Agences SEO Paris vs agences à distance               │
│     intent : objection (peur du local-only)                  │
│                                                              │
│ ▼ H2 : FAQ : 6 questions que tout prospect pose              │
│     intent : Fully Meets (cluster micro-intentions)          │
│                                                              │
│ Entités sémantiques à inclure :                              │
│ - SEO local, E-E-A-T, audit technique, backlinks éditoriaux  │
│ - Quartier Paris 11/16, secteur d'activité, KPI leads SQL    │
└──────────────────────────────────────────────────────────────┘

[CTA] Recevez le brief complet (FAQ + vecteurs + format multimodal) sur Fusionn
```

## Inputs / Outputs

**Input** :
- Mot-clé (texte, 200 chars max)
- Type d'audience (B2B / B2C / Local) — radio buttons

**Output** :
- H1 proposé
- **Passage ancré** (150-200 mots, doctrine Tim) prêt à coller en intro
- 5 H2 avec leur intent de SERP associé + 2 H3 sous chaque
- 5 entités sémantiques à inclure dans le corps
- Format recommandé (long article / cluster / FAQ-page)

## Backend / Logique

**Endpoint** : `POST /functions/v1/hn-structure-generate`

**Prompt LLM** (Gemini Flash, structured output JSON) :
```
Tu es l'expert SEO Tim Boussardon. Pour le mot-clé "{keyword}" 
en contexte {type}, produis une structure Hn optimisée pour le 
passage ranking Google et le Fully Meets des Quality Raters.

Règles strictes :
- H1 unique, 60-65 caractères, inclut le mot-clé exact
- Passage ancré 150-200 mots, structure SCQA, factuel chiffré
- 5 H2 matchant 5 micro-intentions distinctes (pas de "Introduction" 
  ni "Conclusion"), chaque H2 = 1 verbe d'action
- Pour chaque H2 : indique l'intent (informationnel / décisionnel 
  / comparatif / actionnel / objection / Fully Meets)
- 2 H3 sous chaque H2, dont au moins 1 H3 sur une donnée chiffrée
- 5 entités sémantiques distinctes (pas redondantes avec le 
  mot-clé), couvrant méthode + preuve + objection
- JSON strict, pas de markdown dans les valeurs

Output : {h1, passage_ancre, h2s: [{h2, intent, h3s: [...]}], 
  entites: [...], format_recommande}
```

**Coût token** : 1 call Gemini Flash, ~1500 tokens out. Possibilité de cacher les 500 mots-clés les plus populaires (24h cache) → ~0 token pour eux.

## FAQ doctrine-grounded (8 questions)

```
Q1. Pourquoi une structure Hn et pas juste un titre ?

Parce que Google ne ranke plus la page entière, il ranke chaque 
passage séparément (Passage Ranking, breveté 2021, en production 
depuis). Une structure Hn solide est l'unité d'optimisation 
réelle — chaque H2 est candidat à l'AI Overview pour sa 
micro-intention propre.

Q2. C'est quoi un "passage ancré" ?

Méthode Tim : un bloc de 150-200 mots placé dans les 300 premiers 
mots de la page, structuré pour être extrait tel quel en Featured 
Snippet ou AI Overview. La métrique Imp_pos (Position-Adjusted 
Word Count) montre que ce passage pèse exponentiellement plus que 
le reste du contenu côté visibilité GEO.

Q3. Pourquoi 5 H2 et pas plus ?

Au-delà de 5-7 H2, le poids de chaque ancre est dilué dans 
l'algorithme de retrieval. La règle Boussardon : un H2 = une 
micro-intention claire, jamais "Introduction" ni "Conclusion" 
(formes vides qui ne matchent aucune requête).

Q4. C'est quoi une "micro-intention" ?

Une variante précise d'une requête : pour "agence seo paris", les 
micro-intentions sont "combien ça coûte", "comment choisir", 
"audit gratuit", "agences vs freelance", "B2B vs B2C". Chaque 
micro-intention vit dans un H2 dédié. C'est ce qui permet de 
viser le Fully Meets des Quality Raters.

Q5. Le générateur sait gérer le B2B et le B2C ?

Oui, et c'est important : un H2 B2B parlera de "ROI", "LTV", 
"deal influencé", un H2 B2C parlera de "prix", "avis", "où 
acheter". Cocher le bon type change la structure entière, pas 
juste le wording.

Q6. Et pour les agents IA (Perplexity, ChatGPT) ?

La structure générée intègre les principes Structural Information 
GEO : Hn explicite, passage ancré en réponse directe (Answer 
Firstness), entités sémantiques distinctes. C'est ce qui maximise 
la probabilité d'être cité comme source dans les réponses 
générées (métrique Subjective Impression).

Q7. Je peux générer plusieurs structures par jour ?

Oui, gratuit illimité. Si vous voulez aller plus loin et obtenir 
le brief complet (FAQ stratégique, vecteurs sémantiques, format 
multimodal, signaux E-E-A-T), Fusionn produit le brief complet en 
30 secondes — 3 requêtes gratuites pour tester.

Q8. La structure est-elle générique ou propre à mon mot-clé ?

Chaque structure est générée à partir de votre mot-clé exact, 
sans template. Le générateur croise l'intent business du 
mot-clé, le type d'audience (B2B/B2C/Local), et les 
micro-intentions de la SERP réelle pour produire 5 H2 qui 
n'existent dans aucun outil concurrent.
```

## Maillage interne

- → `/score-business-mot-cle` (ancre : "Score Business de ce mot-clé")
- → `/compte` (ancre : "le brief complet avec FAQ et vecteurs")
- → `/comparateur-volume-business-seo` (ancre : "Comparateur Volume vs Business")
- → `/blog/quadrillage-semantique-strategie-seo-face-ia` (ancre : "le quadrillage sémantique")

---

# OUTIL 4 — Test de citation LLM (Citation Probe)

## URL et SEO

| | |
|---|---|
| **Slug** | `/test-citation-chatgpt-perplexity` |
| **H1** | Êtes-vous cité sur ChatGPT, Perplexity et Gemini ? Test en direct (gratuit) |
| **Meta title** | Test citation ChatGPT Perplexity Gemini : visibilité IA (gratuit) |
| **Meta description** | 88% des sites SEO n'apparaissent pas dans les IA. Saisissez votre domaine, on lance 9 requêtes en direct sur ChatGPT, Perplexity et Gemini. Verdict immédiat. |
| **Requêtes cibles** | suis-je cité sur chatgpt · test visibilité chatgpt · ma marque sur perplexity · llm visibility checker · test citation ia gratuit · comment savoir si chatgpt me cite |

## Hero

```
[H1] Êtes-vous cité sur ChatGPT, Perplexity et Gemini ?

[Sous-titre] 88% des sites qui rankent sur Google ne sortent jamais sur 
les IA génératives. Saisissez votre domaine, on lance 9 requêtes 
typiques de votre secteur en direct sur les 3 LLMs. Verdict en 30 
secondes, gratuit, sans inscription.

[Input : votre domaine]
[Input : votre secteur (ex : agence SEO, SaaS RH)]
[Bouton rouge : Lancer le test]
```

## UI mockup

```
┌──────────────────────────────────────────────────────────────┐
│ Domaine : fusionn.co     Secteur : SEO B2B    [Lancer]        │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ ⏳ Analyse en cours...                                        │
│                                                              │
│ ✓ Requête 1/9 lancée sur ChatGPT                              │
│ ✓ Requête 1/9 lancée sur Perplexity                           │
│ ⋯ Requête 1/9 lancée sur Gemini                               │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Verdict                                                       │
│                                                              │
│  2 citations sur 27 possibles  →  Vous êtes invisible        │
│                                                              │
│  ChatGPT      :  ✗  ✗  ✗  ✗  ✗  ✗  ✗  ✗  ✗                  │
│  Perplexity   :  ✗  ✓  ✗  ✗  ✗  ✓  ✗  ✗  ✗                  │
│  Gemini       :  ✗  ✗  ✗  ✗  ✗  ✗  ✗  ✗  ✗                  │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Détail des requêtes testées                                  │
│                                                              │
│ 1. "Quelle agence SEO B2B recommander en France ?"           │
│    ChatGPT : non cité   Perplexity : non cité  Gemini : non  │
│                                                              │
│ 2. "Meilleurs outils SEO pour les LLMs en 2026"              │
│    ChatGPT : non cité   Perplexity : ✓ cité     Gemini : non │
│ ...                                                          │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Pourquoi vous n'êtes pas cité                                │
│ 3 causes structurelles + plan d'action immédiat              │
└──────────────────────────────────────────────────────────────┘

[CTA] Construisez votre stratégie AEO sur Fusionn → /compte
```

## Inputs / Outputs

**Input** :
- Domaine (URL ou nom de marque), 200 chars max
- Secteur (texte libre, 100 chars max)

**Output** :
- Score de citation global : X / 27 (où 27 = 9 prompts × 3 LLMs)
- Verdict en 1 phrase : "Vous êtes invisible" / "Présence faible" / "Bonne visibilité AEO"
- Matrice 9 × 3 (prompts × LLMs) avec ✓ ou ✗
- 9 prompts testés affichés (transparence)
- 3 causes structurelles d'invisibilité (basées sur la doctrine Tim)
- Plan d'action 5 étapes (lien vers ressources Fusionn)

## Backend / Logique

**Endpoint** : `POST /functions/v1/llm-citation-probe`

**Algorithme** :
1. À partir du secteur, génère 9 prompts types via template fixe (pas de LLM call pour cette étape, déterministe) :
   - 3 prompts "recommandation" (Quelle X recommander en France ?)
   - 3 prompts "comparatif" (Meilleurs outils X en 2026 ?)
   - 3 prompts "comment" (Comment faire X efficacement ?)
2. Lance les 9 prompts sur les 3 LLMs en parallèle (27 calls API)
3. Pour chaque réponse, détecte si le domaine ou la marque est mentionné (regex + fuzzy match sur le nom de domaine et ses variantes)
4. Compile le score et la matrice
5. Génère les 3 causes via heuristique sur le score (pas de LLM call)

**Coût token / API** : ~27 calls, mix Gemini Flash (gratuit/peu cher) + Perplexity API + ChatGPT API. Coût estimé : **$0.05-0.10 par test**. **Rate-limit obligatoire** : 1 test par IP toutes les 24h pour éviter abus.

**Anti-abus** :
- Rate-limit IP : 1 test / 24h
- Captcha (Turnstile Cloudflare) pour le bouton "Lancer le test"
- Email optionnel pour relancer un test (mais pas obligatoire, no gate)

## FAQ doctrine-grounded (8 questions)

```
Q1. Pourquoi 88% des sites ne sortent pas dans les IA ?

Parce que le ranking Google et la citation LLM ne mesurent pas la 
même chose. Google ranke par optimisation (backlinks, mots-clés, 
technique). Les LLMs citent par autorité de marque (fréquence du 
nom dans le corpus d'entraînement) et par pertinence sémantique 
(proximité vectorielle entre votre contenu et la requête). Un 
site peut être top 1 Google et invisible sur ChatGPT.

Q2. Quels LLMs vous testez ?

Trois : ChatGPT (OpenAI), Perplexity (Perplexity AI), Gemini 
(Google AI). Ces trois moteurs couvrent ensemble 80-85% du trafic 
LLM mondial. Claude et Mistral ont des parts plus faibles, mais 
peuvent être ajoutés sur demande.

Q3. Pourquoi 9 prompts par LLM, pas 1 ?

Parce qu'une seule requête ne mesure rien (variance haute, biais 
du prompt). On teste 9 prompts couvrant 3 types d'intention 
(recommandation, comparatif, comment) pour mesurer une vraie 
visibilité, pas un coup de chance. La méthode est documentée dans 
le rapport.

Q4. Quels sont les 3 causes d'invisibilité ?

Selon notre cadre AEO : (1) absence d'autorité de marque dans le 
corpus d'entraînement (vous n'êtes pas cité ailleurs sur le web) ; 
(2) contenu insuffisamment structuré pour le passage ranking ; 
(3) pas de signal Surprise — votre contenu reproduit la moyenne 
statistique du web, l'algorithme Titans le filtre.

Q5. Si je ne suis cité nulle part, je fais quoi ?

Trois priorités, dans l'ordre : (1) faire citer votre marque sur 
Reddit, LinkedIn, YouTube, et les forums sectoriels — c'est ce 
qui nourrit le corpus LLM ; (2) restructurer vos pages avec un 
passage ancré et des H2 par micro-intention ; (3) injecter de la 
data propriétaire chiffrée (un Surprise Gap) que personne d'autre 
ne possède.

Q6. Le test marche pour les marques B2B et B2C ?

Oui, la méthode est sectorielle (vous renseignez votre secteur), 
les 9 prompts sont adaptés. En B2B, on teste plus les prompts 
"recommandation" et "comparatif". En B2C, plus de "comment". 
L'algorithme s'adapte automatiquement.

Q7. À quelle fréquence relancer le test ?

Tous les 30-60 jours. Le corpus des LLMs se rafraîchit avec un 
biais de récence (Recency Bias) : 65% des citations LLM concernent 
du contenu publié dans les 12 derniers mois. Un site qui n'a pas 
publié récemment peut disparaître des réponses en 6 mois.

Q8. Le test est vraiment gratuit ?

Oui, 1 test par 24h et par IP. Pour des tests illimités, un 
historique mensuel, et un benchmark contre 5 concurrents, ouvrez 
un compte Fusionn (3 requêtes gratuites pour démarrer).
```

## Maillage interne

- → `/compte` (ancre : "construisez votre stratégie AEO")
- → `/score-business-mot-cle` (ancre : "Score Business")
- → `/structure-h2-h3-seo` (ancre : "structurer vos pages pour le passage ranking")
- → `/blog/pourquoi-88-pourcent-sites-seo-napparaissent-pas-dans-ia` (ancre : "pourquoi 88% des sites SEO n'apparaissent pas dans les IA")
- → `/blog/ma-reflexion-du-moment-sur-le-seo-ia` (ancre : "ma réflexion sur le SEO IA")

---

# SECTION OUTILS DANS LE FOOTER

## Design

Ajouter une 4e colonne dans `src/components/Footer.tsx` (ou nouveau bloc selon le layout actuel), titre **"Outils gratuits"**.

```
Outils gratuits
- Score Business d'un mot-clé
- Comparateur Volume vs Business
- Structure H2/H3 SEO
- Test citation ChatGPT/Perplexity
```

Chaque lien `<Link>` (React Router) avec ancre = le H1 court de l'outil. Hover orange `#FF371C`.

## Stratégie de maillage globale

| | Score Business | Comparateur | Structure Hn | Citation Probe |
|---|---|---|---|---|
| **Outbound depuis Landing** | ✓ (hero secondary CTA) | ✓ (bento card) | ✓ (bento card) | ✓ (footer + section IA) |
| **Outbound vers /compte** | ✓ | ✓ | ✓ | ✓ |
| **Outbound vers blog** | quadrillage + 88% | quadrillage + trouver-mots-cles | quadrillage | 88% + ma-reflexion |
| **Outbound inter-outils** | → Comparateur, Structure | → Score, Structure | → Score, Comparateur | → Score, Structure |

**Page Landing à enrichir** :
- Section bento : ajouter une 6e tuile "Outils gratuits" qui pointe vers les 4 outils
- Hero : ajouter sous la barre de recherche un mini-link "Ou testez gratuitement nos outils →"

**Section FAQ globale Landing** :
- Ajouter 2-3 questions qui pointent vers les outils :
  - "Comment savoir si mon mot-clé vaut la peine ?" → /score-business-mot-cle
  - "Est-ce que mon site apparaît sur ChatGPT ?" → /test-citation-chatgpt-perplexity

## Cluster SEO résultant

L'ensemble des 4 outils + leur maillage construit un **3e pilier SEO sur le site Fusionn** :
- Pilier blog A : Stratégie SEO face à l'IA (hub : quadrillage)
- Pilier blog B : Visibilité AEO dans les LLMs (hub : 88%)
- **Pilier outils C : Product-Led SEO** (hub naturel : Score Business, le plus cherché)

C'est l'extension manquante du cluster blog. Les outils convertissent (page Do des Quality Raters), le blog éduque (page Know).

---

# RECAP IMPLÉMENTATION (ordre suggéré pour demain)

1. **Comparateur Volume vs Business** (Outil 2) — 0 LLM, déterministe, le plus rentable. ~4h dev.
2. **Score Business mot-clé** (Outil 1) — réutilise l'algo, 1 call Gemini Flash. ~4h dev.
3. **Générateur Hn** (Outil 3) — prompt LLM, 1 call. ~6h dev.
4. **Citation Probe** (Outil 4) — multi-LLM API + rate-limit + captcha. ~10h dev. **Coût récurrent par usage**.
5. **Section Footer + maillage Landing** — ~1-2h.

Total estimé : 2-3 jours de dev pour les 4 outils + maillage complet.
