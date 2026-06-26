---
client: leexi
type: cluster
theme: Notetaker IA / prise de notes de réunion (pilier produit)
date: 2026-06-26
skill: seo-cluster-aeo
statut: architecture cocon — à valider avant production
pilier: notetaker IA / prise de notes de réunion par IA
branches: 7
grounding: WebSearch 2026-06-26 (SERP, PAA, autocomplétion réelles)
related:
  - "[[leexi]]"
  - "[[cocon-2-prise-de-notes-rgpd]]"
---

# Cocon 1 — Notetaker IA / prise de notes de réunion

> Pilier produit cœur de Leexi. Architecture AEO : 1 page = 1 intention de SERP, Know-Simple / Know / Do, maillage intentionnel des pages Know/info vers les pages Do (outil + démo).
> Grounding : data réelle WebSearch du 2026-06-26 (SERP, People Also Ask, variantes réellement tapées). Pas de colonne Volume (décision Tim). Difficulté = proxy déclaratif.

## Cadrage
- **Mot-clé pilier** : `prise de notes de réunion IA` / `notetaker IA` (page money produit, hub du cocon).
- **Point de conversion** : essai / démo (e-mail qualifié).
- **Logique** : le cœur produit (réunion, comptes rendus, transcription) attire l'intention large ; les branches sectorielles, cas d'usage et intégrations qualifient ; les outils gratuits captent des e-mails (Product-Led) ; la conformité ISO et les cas clients ferment sur la réassurance.
- **Frontière avec le Cocon 2** : ici la conformité = **angle ISO / sécurité / hébergement / certifications** (signal de confiance produit). Le **RGPD pur** (légal, enregistrement, consentement) reste dans le [[cocon-2-prise-de-notes-rgpd]]. Une page par angle, jamais les deux (MECE).
- **Absorption de la couche GEO (décision 2026-06-26)** : les pages usage (branche 4) et secteur (branche 2) **absorbent en H2/FAQ** les angles « comment… » repliés depuis la [[cocon-3-middle-funnel-metier|couche GEO]] (ex-cocon 3) : compte rendu d'un call commercial, comparer deux candidats, gagner du temps sur les CR d'entretien, CR de mission en conseil, CR en cabinet comptable, PV de conseil municipal. Pas de page dédiée pour ces angles, ils enrichissent la page produit correspondante (bon pour le GEO, zéro cannibalisation).

---

## Page pilier

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| **Notetaker IA / prise de notes de réunion par IA** (pilier) | Know + Do | Page produit answer-first + démo intégrée | SoftwareApplication + FAQPage | Haute |

---

## Branche 1 — Notetaker + type de réunion

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Compte rendu de réunion automatique (IA) | Do | Page produit + exemple généré | SoftwareApplication | Haute |
| Compte rendu de réunion d'équipe | Do | Guide + modèle + CTA | HowTo | Moyenne |
| Compte rendu de réunion client | Do | Guide + modèle | HowTo | Moyenne |
| Compte rendu d'entretien d'embauche | Do | Guide + modèle (→ branche recrutement) | HowTo | Moyenne |
| Compte rendu de CODIR / comité de direction | Do | Guide longue traîne | HowTo | Basse |
| Compte rendu de point projet / réunion projet | Do | Guide longue traîne | HowTo | Basse |
| Compte rendu de one-to-one | Know + Do | Guide structurant (peu couvert FR) | HowTo | Basse |
| PV de CSE par IA (délai légal 15 j, R2315-25) | Do | Guide réglementaire + outil | HowTo | Moyenne |
| Comment faire un compte rendu de réunion | Know | Guide pédago (aimant trafic) → maille vers pilier | Article | Moyenne |

## Branche 2 — Notetaker + secteur

> Secteurs prioritaires validés : **conseil, comptabilité-finance, secteur public**. Autres secteurs porteurs en second rideau.

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Compte rendu de réunion IA pour cabinet de conseil / consultant | Do | Page sectorielle + cas d'usage | SoftwareApplication | Haute |
| Compte rendu de réunion IA pour cabinet comptable / expert-comptable | Do | Page sectorielle | SoftwareApplication | Haute |
| Compte rendu IA conseil municipal / collectivités | Do | Page secteur public (verbatim, délibérations) | SoftwareApplication | Haute |
| Compte rendu IA commission / comité (secteur public) | Do | Déclinaison administrative | SoftwareApplication | Basse |
| Notetaker IA pour avocat / cabinet d'avocats | Do | Page sectorielle (→ conformité Cocon 2) | SoftwareApplication | Moyenne |
| Outil IA compte rendu RH | Do | Page sectorielle (→ recrutement) | SoftwareApplication | Moyenne |
| Prise de notes IA pour managers | Do | Page persona transverse | SoftwareApplication | Basse |
| Notetaker IA pour PME | Do | Page segment taille | SoftwareApplication | Basse |

## Branche 3 — Générateur / outil gratuit (Product-Led, aimants de leads)

> Pages **Do = outils interactifs**, pas du texte. Objectif e-mail qualifié, pas trafic. Template téléchargeable = lead magnet contre e-mail.

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Générateur de compte rendu de réunion gratuit | Do | **Outil interactif** (upload audio → CR) | WebApplication | Haute |
| Transcription audio gratuite en ligne (sans inscription) | Do | **Outil interactif** | WebApplication | Haute |
| Transcrire une réunion Google Meet / Teams / Zoom (gratuit) | Do | Outil + guide par plateforme (pSEO) | WebApplication | Haute |
| Modèle de compte rendu de réunion (Word / à télécharger) | Do | **Template téléchargeable** (lead magnet) | HowTo | Moyenne |
| Modèle de PV / procès-verbal de réunion | Do | Template (→ niche CSE / collectivités) | HowTo | Moyenne |
| Exemple de compte rendu de réunion | Know-Simple | Page exemple → maille vers générateur | Article | Moyenne |
| Générateur de minutes de réunion | Do | Outil longue traîne | WebApplication | Basse |

## Branche 4 — Cas d'usage par fonction

### 4a. Sales / commercial
| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Compte rendu de réunion / rendez-vous commercial automatique | Do | Page usage + synchro CRM | SoftwareApplication | Haute |
| Résumé d'appel commercial IA | Do | Page feature (AI call summarizer) | SoftwareApplication | Moyenne |
| Compte rendu de discovery call | Do | Page jargon sales (quasi vierge) | HowTo | Moyenne |
| Compte rendu de démo produit | Do | Page usage | HowTo | Basse |
| Synchronisation des notes de réunion au CRM (HubSpot / Salesforce) | Do | Page usage (→ branche intégrations) | SoftwareApplication | Moyenne |
| Modèle de compte rendu de visite commerciale | Know-Simple | Template (aimant) | HowTo | Basse |

### 4b. Customer Success
| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Compte rendu de réunion client / point client | Do | Page usage CS | SoftwareApplication | Moyenne |
| QBR (Quarterly Business Review) : préparer et documenter | Know + Do | Guide + modèle QBR | Article | Moyenne |
| Notes d'onboarding client | Do | Page usage | HowTo | Basse |
| Résumé de réunion client automatique | Do | Page feature | SoftwareApplication | Basse |

### 4c. Recrutement
| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Compte rendu d'entretien d'embauche (IA) | Do | Page usage + modèle | SoftwareApplication | Haute |
| Débrief candidat / modèle de débrief d'entretien | Know + Do | Guide + scorecard structurée | HowTo | Moyenne |
| Prise de notes d'entretien de recrutement | Do | Page usage RH | SoftwareApplication | Moyenne |
| Synthèse / comparaison de candidats après entretien | Do | Page usage (décision d'embauche) | HowTo | Basse |

## Branche 5 — Intégrations

> Visio > CRM > VoIP > agenda / productivité. Marques d'outils **autorisées** (cibles d'intégration validées). Hub par catégorie maillant les pages par outil.

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Notetaker IA pour Google Meet | Know + Do | Page intégration | SoftwareApplication | Haute |
| Prise de notes IA pour Microsoft Teams (sans licence Copilot) | Do | Page intégration | SoftwareApplication | Haute |
| Notetaker IA pour Zoom (transcription FR) | Know + Do | Page intégration | SoftwareApplication | Haute |
| Hub CRM : notetaker IA + CRM | Know | Hub maillant les pages par CRM | CollectionPage | Moyenne |
| Intégrer un notetaker à HubSpot | Do | Page intégration | SoftwareApplication | Moyenne |
| Notetaker pour Salesforce | Do | Page intégration | SoftwareApplication | Moyenne |
| Intégration notetaker IA Pipedrive | Do | Page intégration (PME FR) | SoftwareApplication | Basse |
| Prise de notes IA Sellsy (CRM français) | Do | Page intégration (souveraineté) | SoftwareApplication | Basse |
| Transcription d'appel Aircall / Ringover IA | Do | Page intégration VoIP | SoftwareApplication | Basse |
| Notetaker IA + Google Agenda / Outlook (déclenchement auto) | Know-Simple | Page intégration | SoftwareApplication | Basse |
| Envoyer le compte rendu de réunion dans Slack / Notion | Do | Page intégration productivité | SoftwareApplication | Basse |

## Branche 6 — Cas clients / preuves d'usage (E-E-A-T)

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Études de cas : prise de notes IA en entreprise | Know | Case studies (pilier E-E-A-T) | Article | Haute |
| Avis / retours d'expérience notetaker IA | Know | Page avis réels (pas un comparatif) | Review | Moyenne |
| Gain de temps : compte rendu IA (data chiffrée) | Know | Page chiffrée + témoignage | Article | Moyenne |

## Branche 7 — Conformité ISO / sécurité / preuves E-E-A-T

> Angle **ISO / hébergement / certifications / chiffrement** — distinct du RGPD pur (Cocon 2). Différenciateurs Leexi : ISO 27001, hébergement France, chiffrement.

| Page | Intention | Format | Schema.org | Priorité |
|---|---|---|---|---|
| Notetaker IA certifié ISO 27001 | Do | Page réassurance | SoftwareApplication | Haute |
| Outil de prise de notes IA sécurisé (hub sécurité) | Know | Hub maillant la branche | CollectionPage | Moyenne |
| Notetaker IA hébergé en Europe / en France | Do | Page souveraineté | SoftwareApplication | Moyenne |
| IA souveraine de prise de notes de réunion | Know | Page positionnement (pas SEO géo) | Article | Basse |
| Chiffrement des données d'un outil de prise de notes IA | Know | Page technique de confiance | Article | Basse |
| Notetaker IA SOC 2 | Do | Page réassurance acheteur entreprise | SoftwareApplication | Basse |
| Certifications d'un outil de transcription IA (checklist ISO/SOC 2/RGPD) | Know-Simple | Contenu extractible (IA) | FAQPage | Basse |

---

## Maillage interne (règles)

- **Pilier ↔ branches** : le pilier `notetaker IA` maille vers chaque tête de branche ; chaque tête de branche remonte au pilier (ancre = mot-clé pilier).
- **Know → Do** : toute page Know/info (« comment faire un compte rendu », « QBR », « gain de temps ») pointe vers une page Do (générateur, page produit sectorielle ou démo). Jamais une page Know en cul-de-sac.
- **Hubs** : `hub CRM`, `hub sécurité` regroupent et maillent leurs pages-outil ; les pages-outil remontent au hub.
- **Croisements inter-branches** : secteur ↔ cas d'usage (cabinet comptable ↔ compte rendu client), recrutement ↔ entretien d'embauche, intégrations ↔ sales (synchro CRM).
- **Pont vers Cocon 2** : les pages avocat / RH / secteur public / santé maillent vers les pages RGPD correspondantes du [[cocon-2-prise-de-notes-rgpd]] (ancre = angle conformité légale), sans dupliquer l'angle.

## Roadmap (priorisation effort × conversion)

- **Vague 1 (Haute)** — pilier + têtes Do à fort intent : `compte rendu de réunion automatique`, secteurs conseil / comptable / public, générateur gratuit + transcription gratuite, intégrations Meet / Teams / Zoom, `compte rendu rendez-vous commercial`, `compte rendu entretien d'embauche`, `notetaker ISO 27001`, études de cas.
- **Vague 2 (Moyenne)** — déclinaisons par type de réunion, cas d'usage CS, hubs CRM/sécurité, intégrations CRM principales, débrief candidat, modèles téléchargeables.
- **Vague 3 (Basse)** — longue traîne (CODIR, one-to-one, managers/PME, Pipedrive/Sellsy/VoIP, SOC 2, IA souveraine).

> Objectif client : 40-50 pages à 3 mois. Le Cocon 1 fournit la majorité du volume Do ; le [[cocon-2-prise-de-notes-rgpd]] apporte l'autorité conformité et les comparatifs.

## Sources (grounding 2026-06-26)
- https://www.leexi.ai/fr/assistant-ia/prise-de-notes-ia/outils-comptes-rendus-reunion/
- https://www.leexi.ai/fr/assistant-ia/prise-de-notes-ia/top-8-outils-ia-gratuits/
- https://www.noota.io/fr/blog/comptes-rendus-de-reunion-ia
- https://www.noota.io/products/interview-report
- https://www.ringover.fr/blog/outil-ia-pour-compte-rendu-de-reunion
- https://flowt.fr/blog/ia-pour-compte-rendu-de-reunion-gratuit-top-8-des-outils-2026/
- https://www.recapro.ai/fr/cas-usage-services-publics
- https://www.agilotext.com/blog/articles/comment-utiliser-l-ia-pour-rediger-un-pv-cse-guide-pratique
- https://www.seedext.com/articles/automatiser-compte-rendu-de-reunions-commerciales
- https://www.lmcp.fr/du-suivi-a-la-strategie-comment-les-qbr-renforcent-votre-demarche-customer-success/
- https://taleez.com/blog/rediger-un-compte-rendu-dentretien-dembauche-efficace
- https://www.claap.io/fr-fr/blog/interview-debrief-template
- https://www.leexi.ai/fr/integrations/visio-conference/microsoft-teams/comment-utiliser-l-ai-note-taker-sur-teams/
- https://www.leexi.ai/fr/securite/certifications-audits-conformite-reglementaire/top-5-outils-ia-certifies-iso27001/
- https://propulslead.com/post/crm-augmentes-ia-hubspot-salesforce-pipedrive-comparatif/
