---
client: leexi
type: cluster
theme: Couche GEO transversale (ex-cocon 3) — problèmes métier + hub agent IA
date: 2026-06-26
statut: architecture validée — couche GEO/maillage (décision 2026-06-26)
pilier: capter le problème métier non résolu → citation IA + maillage vers les pages business
related:
  - "[[leexi]]"
  - "[[cocon-1-notetaker-reunion]]"
  - "[[cocon-2-prise-de-notes-rgpd]]"
---

# Couche GEO transversale (ex-cocon 3)

> **Décision 2026-06-26.** Les pages « usage métier » (Sales / CS / Recrutement) existent déjà dans le [[cocon-1-notetaker-reunion]] (intention produit, volume Google, conversion). Refaire des pages persona ici = cannibalisation. Le « cocon 3 » n'est donc **pas un 3e cocon de pages produit** : c'est une **couche transversale GEO + maillage** posée par-dessus les cocons 1 et 2.
>
> **Ce qu'elle garde** : uniquement les pages « problème » dont la requête a une **SERP distincte** (ou pas de SERP Google du tout, réponse IA only) + le **hub agent IA** (intention agent ≠ notetaker, signal GSC réel).
> **Ce qu'elle ne garde pas** : les angles « comment… » qui partagent la SERP d'une page produit du cocon 1. Ceux-là sont **repliés dans le cocon 1** sous forme de H2 / FAQ (voir section 3).
>
> **Rôle de chaque page conservée** : se faire citer par ChatGPT / Perplexity / AI Overviews sur un problème métier, puis mailler vers la page du cocon 1 ou 2 qui convertit. Ce n'est pas une page de volume Google, c'est une page de citation IA + de maillage.

## Cadrage
- **Format** : answer-first, problème en H1, réponse extractible (procédure / tableau / définition), data propriétaire Leexi, CTA vers la page business.
- **Test d'admission d'une page** : sa requête a-t-elle une SERP distincte d'une page produit du cocon 1 ? Si oui → page propre ici. Si non → repli en H2/FAQ dans le cocon 1.
- **Mesure** : citations IA constatées + trafic référent (ChatGPT/Perplexity) + leads assistés via maillage. Pas le volume GSC.

---

## 1. Pages problème conservées (SERP distincte / réponse IA only)

> Critère retenu : angle quasi absent des SERP FR aujourd'hui, donc zéro cannibalisation du cocon 1, et répondu par les moteurs IA.

### Sales
| Page (problème) | Pourquoi elle reste (vs cocon 1) | Maille vers |
|---|---|---|
| Comment remplir son CRM après un rendez-vous sans saisie manuelle | Angle « CRM auto-update », pain distinct de la page produit « synchronisation CRM » | Intégrations CRM + essai |
| Comment suivre les objections clients sur tout le pipeline | Angle « suivi des objections sur le pipeline » absent des SERP produit | Cas d'usage Sales + essai |

### Customer Success
| Page (problème) | Pourquoi elle reste | Maille vers |
|---|---|---|
| Comment réussir un onboarding client sans prendre de notes en réunion | Angle « sans prendre de notes » quasi absent des SERP | Cas d'usage CS + essai |
| Comment préparer un QBR à partir des verbatims clients | Angle « à partir des verbatims » distinct de la page QBR produit | Cas clients + essai |
| Comment ne plus oublier les actions de suivi après une réunion client | Problème universel, formulation négative sans SERP produit | Essai gratuit |

### Recrutement
| Page (problème) | Pourquoi elle reste | Maille vers |
|---|---|---|
| Comment structurer le débrief d'un entretien sans biais | Angle « sans biais » distinct de la page « débrief candidat » produit | Cas d'usage recrutement + essai |

## 2. Hub agent IA (cocon autonome)

> Intention distincte du notetaker (signal GSC `agent ia entreprise` : 310 impr, pos 4,1). Pas de doublon possible avec les cocons 1/2. Traité en hub haut-funnel qui maille vers le notetaker.

| Page | Intention | Maille vers |
|---|---|---|
| Qu'est-ce qu'un agent IA en entreprise (définition + cas d'usage) | Know-Simple | Hub → assistant réunion |
| Différence entre assistant IA et agent IA en entreprise | Know-Simple | Hub → assistant réunion |
| Assistant IA pour les réunions d'équipe : quel outil choisir | Know/Do | Assistant de réunion IA + essai |
| Meilleur agent IA pour entreprise / PME (comparatif 2026) | Do | Comparatif + tarifs |
| Agent IA pour équipe commerciale / sales | Know/Do | Cas d'usage Sales + intégrations CRM |
| Comment utiliser un agent IA pour automatiser les comptes rendus | Do | Pont vers le cocon 1 (compte rendu auto) |

## 3. Angles repliés dans le Cocon 1 (H2 / FAQ, pas de page propre)

> Ces formulations partagent la SERP d'une page produit existante. On ne crée pas de page : on enrichit la page produit du cocon 1 avec une section / FAQ qui répond à la question « comment… ». Ça nourrit aussi le GEO sans cannibaliser.

| Angle « comment… » | Page du cocon 1 qui l'absorbe |
|---|---|
| comment automatiser le compte rendu d'un call commercial | Usage Sales : compte rendu rendez-vous commercial |
| comment comparer deux candidats sur les mêmes critères | Usage Recrutement : comparer candidats après entretien |
| comment gagner du temps sur les comptes rendus d'entretien | Usage Recrutement : compte rendu entretien d'embauche |
| comment gérer les comptes rendus de mission en cabinet de conseil | Secteur : cabinet de conseil |
| comment automatiser les comptes rendus de rendez-vous client en cabinet comptable | Secteur : cabinet comptable |
| comment automatiser le PV d'un conseil municipal / instance publique | Secteur : conseil municipal / secteur public |

---

## Maillage interne (règle de la couche)
- **Sens unique** : chaque page problème conservée → la page business du cocon 1 ou 2 qui convertit. C'est la fonction de la couche.
- **Hub agent IA** : pilier définition → décline vers assistant réunion / cas d'usage → pont vers le compte rendu auto du cocon 1.
- **Angles repliés** : vivent en H2/FAQ dans le cocon 1, donc maillage interne natif à la page produit.

## Données à re-sourcer avant publication (doctrine : aucun chiffre inventé)
- « 61 % appliquent les actions décidées en réunion » (attribué HBR par les réponses IA) → source primaire ou retrait.
- « PV de conseil municipal : 2-4 h → -70/-80 % » → re-sourcer (rapport Sénat 2025 cité, à vérifier).
- Stats d'usage Leexi (gain de temps réel) = data propriétaire à fournir, carburant de citation IA.

## Roadmap
- **Vague 1** : hub agent IA (définition + assistant réunion d'équipe) + débrief sans biais + CRM sans saisie. Les plus citables, zéro cannibalisation.
- **Vague 2** : objections pipeline, onboarding sans notes, QBR verbatims, actions de suivi, reste du hub agent IA.
- **En parallèle** : enrichir les pages cocon 1 concernées avec les 6 angles repliés (section 3).
