# Diagnostic Fusionn et plan d'action 90 jours — 2026-05-26

Snapshot des métriques, lecture vs benchmark SaaS, plan d'action chirurgical sur 3 mois. Doc à confronter à la prochaine revue (J+30, J+60, J+90).

⚠️ Chiffres sortis d'un export DB rapide style Bolt, à recouper. Ordres de grandeur, pas vérités absolues.

---

## 1. Le snapshot au 2026-05-26

### Stock

| Indicateur | Valeur |
|---|---|
| Total comptes | 684 |
| Premier compte | 10 décembre 2025 |
| Dernier compte | 19 mai 2026 |
| Premium actifs | 24 (3,5 %) |
| Gratuits | 660 (96,5 %) |
| MRR | 696 € (24 × 29 €) |
| ARR | 8 352 € |
| ARPU | 29 € |

### Acquisition par mois

| Mois | Inscriptions | Variation |
|---|---|---|
| Décembre 2025 | 290 | — (lancement) |
| Janvier 2026 | 213 | -27 % |
| Février 2026 | 75 | -65 % |
| Mars 2026 | 61 | -19 % |
| Avril 2026 | 28 | -54 % |
| Mai 2026 (au 19) | 17 | n/a |

**30 derniers jours : 24 inscrits.** Soit 12 fois moins qu'au pic. **7 derniers jours : 0 inscrit.** L'acquisition est à l'arrêt.

### Activation par tranche de recherches (vie entière)

| Tranche | Comptes | % du total |
|---|---|---|
| 0 recherche | 316 | 46,2 % |
| 1 recherche unique (testeurs) | 157 | 23,0 % |
| 2-5 recherches | 177 | 25,9 % |
| 6-10 recherches | 16 | 2,3 % |
| 10+ recherches (power users) | 18 | 2,6 % |

### Activité récente (sur 684 comptes total)

- **WAU** (cette semaine) : 9 → **1,3 %**
- **MAU** (30 derniers jours) : 56 → **8 %**
- Actifs 3 derniers mois : 150 (22 %)
- Churnés (inactifs 3+ mois parmi ceux qui avaient testé) : 162 / 368 = **44 %**

### Diagnostic activation détaillé

| Statut post-inscription | Comptes |
|---|---|
| Onboarding vu | 676 / 684 (98,8 %) |
| Connectés mais 0 recherche | 315 |
| Revenus >1h après inscription sans chercher | 18 |
| Jamais connectés | 1 |

L'onboarding n'est pas le problème (98,8 % le voient). Le passage à l'action immédiatement après si.

### Profil des testeurs et des power users

Les 157 testeurs "1 recherche unique" ont tous (100 %) utilisé l'onglet **table** (recherche sémantique). **Aucun** n'a exploré une seconde fonctionnalité. Voient le tableau, partent.

Les 18 power users ont fait **1 033 recherches en table** et 86 en tools (un seul user). Le aha moment est clair : c'est le tableau de mots-clés sémantiques. Les autres onglets (HN Score, Vecteurs, FAQ, Objections, GEO Sentinel, Micro-intentions) n'apparaissent pas comme moteurs de rétention dans les données.

### Churn

| Statut | Nb | Prix moyen |
|---|---|---|
| Actifs | 24 | (29 €/mois ou 19 €/mois équivalent annuel) |
| Annulés | 11 | 28 € |

**Churn 31 %** (11 / 35) sur les 6 mois. Concentré sur les mensuels à 29 €. Les annuels et plans hauts tiennent.

---

## 2. Vrais ratios à retenir

- **MAU 8 %** : très en dessous du benchmark SaaS B2B SMB sain (25-40 %).
- **WAU 1,3 %** : signal de produit non-habituel.
- **"Real users"** (≥ 2 recherches dans la vie) : 211 / 684 = **31 %**.
- **Power users** (10+ recherches) : 18 seulement = **2,6 %** — le vrai noyau dur.
- Le "53,8 % activés" affiché est trompeur. 23 % testent une fois et partent.

---

## 3. Trois fuites distinctes, pas une

Le tunnel a trois trous qu'il ne faut pas confondre.

**Fuite 1 — Acquisition à l'arrêt.** Zéro inscrit sur 7 jours, ÷12 par rapport au pic. Ce n'est pas une décélération post-launch normale, c'est une rupture sur les canaux. À investiguer : Search Console, social, PR, referrals.

**Fuite 2 — Activation cassée.** 46 % s'inscrivent et ne lancent jamais une recherche. L'onboarding est vu à 98,8 %, donc c'est juste après que les gens décrochent. Pas de friction technique, pas de bug — c'est un problème de proposition de valeur immédiate.

**Fuite 3 — Rétention cassée à la 2e recherche.** 23 % font une recherche, voient le tableau, partent. Le tableau seul n'est pas un livrable. Il manque un "next step" évident qui montre la profondeur (brief, action plan, structure Hn).

---

## 4. Lecture vs benchmark SaaS

Segment de comparaison : SaaS B2B SMB freemium vertical marketing/SEO, stade early-stage. Sources : ChartMogul, OpenView, Baremetrics public.

| Métrique | Fusionn | Benchmark sain | Verdict |
|---|---|---|---|
| Free → paid conversion | 3,5 % | 2-5 % | Dans la norme |
| Activation (≥ 2 actions <7j) | ~31 % | 40-60 % | Bas |
| MAU / total signups | **8 %** | 20-40 % | **Très bas** |
| M3 churn (inactif 3+ mois) | 44 % | 25-35 % | Au-dessus |
| Churn payant brut | 5 %/mois | 3-7 % | Limite haute |
| ARPU | 29 € | 20-100 € | Correct |
| MRR 6 mois | 696 € | 5-15 k € | Pré-PMF |

Le seul écart violent au benchmark : MAU 8 % vs 25-40 %. Plus de 3 fois sous la médiane. C'est le signal que tout le travail produit n'a pas encore créé d'habitude.

### Comparaison aux concurrents directs

| Acteur | ARR estimé |
|---|---|
| Surfer SEO | 30-50 M$ |
| Frase | 5-10 M$ |
| NeuronWriter | 2-5 M$ |
| Clearscope | 20-30 M$ |
| **Fusionn** | **12 k$** |

À ce stade, l'écart est normal (3 à 7 ans d'avance pour eux). Le problème, c'est la trajectoire : Fusionn plafonne, ne rattrape pas.

---

## 5. Plan d'action 90 jours

Priorité dans cet ordre : **activation > acquisition > conversion**. Le levier le plus rapide est de transformer les 684 inactifs en MAU. Pas de feature nouvelle, pas de campagne paid, pas de course à Ahrefs.

### Sprint 1 — Casser la fuite d'activation (S1-S2)

**P0.1 — Email J+1 sur le brief synthèse pré-rempli**
- Cible : les 157 "1 recherche puis partis".
- Déclencheur : 24h après la 1re recherche, sans 2e action.
- Contenu : screenshot du Brief synthèse pré-rempli + 3 onglets non explorés + un seul CTA "Voir ton brief complet".
- Effort : 1 jour.
- Métrique : taux 1→2 recherches (baseline ~30 %, cible 50 % à J+30).

**P0.2 — Tour produit forcé après la 1re recherche**
- Modal automatique au chargement des résultats de la 1re recherche.
- Contenu : 3 slides Bento sur Brief synthèse / GEO Sentinel / pSEO. CTA direct sur chaque.
- Effort : 1-2 jours.
- Métrique : taux de clic sur un 2e onglet en 1re session (baseline ~0, cible 40 %).

**P0.3 — Décongelation du Brief synthèse pour les comptes existants**
- Cible : 211 real users qui ont 2-5 recherches mais ne reviennent plus.
- Action : email broadcast "On a sorti l'onglet Brief synthèse — voici ton premier sur {dernière recherche}".
- Effort : 0,5 jour.
- Métrique : retour de 5-10 % des dormants = +20-40 MAU instantanés.

### Sprint 2 — Comprendre le aha + relancer le top-funnel (S3-S4)

**P0.4 — Interviewer les 18 power users**
- 30 min visio. 5 questions :
  1. Comment as-tu découvert Fusionn ?
  2. À quel moment précis tu as compris la valeur ?
  3. Quel onglet tu utilises le plus, pourquoi ?
  4. Qu'est-ce qui te ferait passer à 50 €/mois ?
  5. Si tu devais pitcher Fusionn en 1 phrase à un confrère, tu dirais quoi ?
- Effort : 9h sur 2 semaines.
- Output : doctrine "pourquoi les gens paient Fusionn" → pivot positionnement homepage.

**P1.1 — Relancer le top-funnel sur UN canal, pas trois**
- Choix : LinkedIn Tim + cold outbound agences SEO francophones, en parallèle, 8 semaines.
- Effort : 3h/sem soit 24h.
- Métrique : +30 inscrits/mois sur des sources qualifiées (vs 17 ce mois-ci dont aucune mesurée).

### Sprint 3 — Resserrer la monétisation (M2)

**P1.2 — Cacher le mensuel 29 €, pousser l'annuel d'office**
- Sur le pricing public : annuel par défaut, mensuel en option grisée "Si tu hésites encore". Économie affichée vs mensuel.
- Effort : 2h frontend.
- Métrique : ratio annuel/mensuel sur les nouveaux conversions (cible 75 %).

**P1.3 — Trigger conversion sur la 5e recherche**
- À la 4e recherche, modal "Plus que 1 recherche gratuite — passe en annuel à 228 € et débloque tout".
- Effort : 1 jour.
- Métrique : conversion free→paid pour la cohorte "4+ recherches" (cible 10-15 %).

**P1.4 — Email J+25 sur les mensuels**
- Cible : ceux qui sont à 25 jours d'abonnement (avant fin du mois 1 où ils churnent).
- Contenu : "Tu as fait X recherches. Voici 3 trucs ajoutés et 1 power user qui dit Y" → preuve + rétention.
- Effort : 0,5 jour.
- Métrique : rétention M1 mensuels (baseline ~70 %, cible 85 %).

### Sprint 4 — Positionnement et différenciation (M3)

**P2.1 — Réécrire la homepage selon les interviews power users**
- Ne pas le faire en aveugle. Attendre les enseignements du Sprint 2.
- Effort : 2-3 jours.

**P2.2 — Publier l'article "Méthodologie Fusionn" (honest measurement)**
- Aligné sur l'angle marché : transparence des scores Surprise, Grounding, GEO Sentinel.
- Effort : 1,5 jour.
- Métrique : +3-5 backlinks éditoriaux, signal SEO long terme.

**P2.3 — Test multilingue : 1 page de landing en allemand sur le wedge AEO**
- Wedge marché européen identifié (peu de concurrents EU sur GEO/AEO).
- Effort : 1 jour.
- Métrique : 5-10 inscrits DE en 30 jours = signal de validation segment EU.

---

## 6. Ce qu'on ne fait PAS dans ces 90 jours

- Pas de course à Ahrefs/Semrush sur la donnée backlinks. Mauvais terrain.
- Pas de feature nouvelle. Les 6 onglets actuels suffisent — il faut les rendre visibles.
- Pas de refonte profonde du pricing. Juste un pivot annuel/mensuel.
- Pas de campagne paid. Sans CAC mesuré ni funnel solide, c'est jeter de l'argent.

---

## 7. Métriques cibles à J+90

| KPI | Aujourd'hui | Cible 90j |
|---|---|---|
| MAU | 56 (8 %) | 120-150 (18-22 %) |
| Inscrits/mois | 17 | 50-80 |
| Taux 1→2 recherches | ~30 % | 50 %+ |
| Conversion free→paid | 3,5 % | 5-7 % |
| Churn mensuel | 5 %/mois | 3-4 %/mois |
| MRR | 696 € | 1 500-2 000 € |

---

## 8. Risques à surveiller

**Le client à 240 € mensuel et autres ARPU hauts.** Vérifier que ces plans hauts existent vraiment et ne sont pas des paiements de service manuels. Si un de ces clients part, perte mécanique disproportionnée du MRR.

**L'effet "ressentiment freemium".** En cachant le mensuel 29 € (P1.2), risque de perdre les early adopters qui veulent tester sans engagement annuel. À monitorer : conversion globale ne doit pas chuter > 20 %.

**Acquisition LinkedIn fragile.** Si l'audience Tim sature, le canal s'éteint vite. Tenir un canal secondaire en backup (cold outbound agences).

---

## 9. Liens

- Repo Fusionn : `~/Code/newFusionn`
- Audit produit précédent : [[Audit-UX-CX]], [[Audit-ux-workspace]]
- Briefs outils complémentaires : [[Briefs-outils-product-led-seo]]
- Historique sessions : [[Historique]]
- Suivi état actuel : [[Suivi-Projet]]

---

À confronter à la prochaine revue (revue-hebdo du vendredi). Si une métrique de la grille ne bouge pas à J+30, le levier correspondant est mort, il faut en changer.
