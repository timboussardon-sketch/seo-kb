---
type: source
source_type: client-note
title: Leexi.ai — fiche client (fiche maître)
client: Leexi.ai
statut: client — production en cours
created: 2026-05-21
updated: 2026-06-24
tags: [client, organikk, leexi, saas, notetaker, geo, pseo]
related:
  - "[[leexi-call-2026-05-21]]"
  - "[[leexi-call-2026-06-24]]"
---

# Leexi.ai — fiche client

> Fiche maître du dossier client. Point d'entrée : tout ce qui concerne Leexi se range dans `raw/organikk/clients/leexi/`.

## En résumé

SaaS notetaker IA (prise de notes meetings avant/pendant/après), démarré début 2022, forte brand et acquisition très inbound (SEA + LinkedIn + stores mobiles + bouche-à-oreille). Le SEO n'a jamais été priorisé : **20 comptes SEO sur ~1000 créés en avril 2026** contre ~200 SEA et ~80 stores. Ils veulent professionnaliser le SEO et passer au GEO. Premier call de découverte le 2026-05-21 (Baptiste CTO + Mathieu), **deuxième call le 2026-06-24** (+ Sophie, marketing) : présentation du bot SEO, validation des 3 axes de mots-clés, calage de la production. Statut : **client — production lancée** (Tim envoie les 3-5 mots-clés business + cocons, attaque création/optimisation des pages dès la semaine du 30/06).

## Contacts

- **Baptiste** — CTO, bonnes notions techniques SEO, profil tech / IA-first
- **Mathieu** — Leexi
- **Sophie** — marketing (présente au call #2)

## Le produit

- Notetaker IA : briefing avant meeting, prise de notes pendant, résumés/tâches/gestion de projet après. Chatbot interne **« Ask Leexi »**.
- B2B, du solopreneur à la boîte de 1000. Assistant brandable côté client mais garde un **« Powered by Leexi »** (gros moteur de notoriété).

## État SEO (au call)

- **Site** : ~1050 URLs au sitemap, dont **280 pages FR**. ~50 pages de base × **7 langues** (traduction auto IA). **200-230 articles** écrits surtout à la main, beaucoup datés/obsolètes (héritage pré-pivot 2022).
- **Refonte en cours non terminée** : rebranding + refonte cocons sémantiques l'an passé ; liens internes de l'ancienne archi retirés, remis petit à petit ; chantier traduction côté IT en attente. **Les pages ne se référencent quasiment plus entre elles.**
- **GEO** : peu/pas cités dans les moteurs génératifs, sauf quelques sujets travaillés (sécurité). Demande explicite d'expertise GEO.
- **Outils / stack** : mots-clés via SE Ranking. CMS **Strapi** (intégration HTML possible, ou push API via Claude Code à arbitrer).
- **Process contenu** : pas de process structuré, manuel, pas d'exploitation de la data client (alors qu'ils ont « Ask Leexi » + tous les enregistrements de calls).

## Chiffres (avril 2026)

- ~1000 comptes B2B créés depuis le site (seul canal de création).
- Attribution : **20 SEO**, ~200 SEA, ~80 stores mobiles.
- Coût/lead SEA ~30-40 € (hors enchère sur la brand, qui le ferait chuter).
- LinkedIn : >1M d'impressions/an.
- Volume estimé « notetaker » & co : 9 000+/mois (Tim estime peut-être ~15 000).

## Angle Tim (la stratégie vendue)

- Le SEO sert à **récupérer des e-mails qualifiés**, pas du trafic. Chaque page doit avoir un intérêt de conversion.
- **Data propriétaire** = le vrai moat : agréger calls clients + e-mails + « Ask Leexi », en extraire problématiques/objections/mots-clés via skills.
- **Modèles de pages** (1 structure → duplication) : problématiques métier, cas d'usage, intégrations (« comment intégrer Zoom avec un notetaker »), « passer de X à Y » (Fathom/Whisper → Leexi), **outils gratuits** (ils en avaient un, décommissionné).
- **Bot/agent SEO autonome** livré en fin de mission : briefs, audits, maillage, contenu social — nourri par leur data. Logique 0→1 puis autonomie, pas d'engagement 24 mois.
- GEO = juste le SEO d'aujourd'hui : viser les requêtes que les LLM ne « mangent » pas (outils, use cases, comparatifs, problématiques).

## Périmètre proposé

- Phase 1 : identifier les mots-clés business/décisionnels + créer **30 à 50 pages business** (Tim rédige tout, comme une agence : audit technique, structure, maillage, intégration).
- Phase 2 : construction du bot, transfert d'autonomie. Bilan à 3 mois (leads ? rankings ?), puis arrêt ou poursuite vers ~100 pages.
- Côté Leexi : ils réfléchissent à recruter un profil junior IA-first à qui transmettre le système.

## Axes mots-clés validés (call #2, 2026-06-24)

1. **RGPD / souveraineté / sécurité** — hébergement France/Europe, souveraineté des données, ISO 27001, EU AI Act, comparatifs RGPD vs outils US. No-go absolu pour une partie des clients.
2. **Fonctionnalités** — transcription (porte d'entrée), résumés/comptes rendus, tâches de suivi, **intégrations CRM** (1 page/CRM + hub), **intégrations Meet/Teams/Zoom**, « passer de X à Y », app mobile/dictaphone.
3. **Problématiques métier** — cas d'usage par secteur (conseil, RH, BTP, managers, recrutement, bancaire).

Secteurs prioritaires : **conseil, comptabilité-finance, secteur public** (technologie écarté = trop large).
Écartés : enregistrement téléphonique (VOIP, fonctionnalité native prévue sept-oct), traduction juridique/médicale (trop niche), chatbot/assistant (trop générique).
Comparatifs : OK contre outils **américains** uniquement, pas contre acteurs français/européens.

## Points ouverts

- **Budget** : non défini, fonction de la valeur estimée (raisonnent en leads/ROI).
- **CMS Strapi** : tranché → **MCP Strapi** (testé OK des deux côtés). Session de config 15-20 min à caler (lundi 9h).
- **Traduction** : FR d'abord (marché principal). Leexi gère la trad IA via ses scripts Strapi.
- **Recrutement interne** d'un profil SEO côté Leexi.
- **Migration** : vérifier les redirections 301 sur les 3 grosses URLs de l'ancien site (audit à lancer).

## Suite immédiate

1. **Tim** : envoie les 3-5 mots-clés business à valider + les cocons ; lance création/optimisation des pages la semaine du 30/06 ; récupère le questionnaire/drive ; envoie invitation session MCP (lundi 9h).
2. **Leexi** : valide les 3-5 mots-clés ; partage cas d'usage métier + cocons existants ; remet le questionnaire dans un drive ; fournit les 3 grosses URLs de l'ancien site.
3. **Cadence** : rapport hebdo + call de suivi tous les 15 jours.

## Lien livrable

- Dashboard/propale en DA Leexi : c'est le **gabarit standard** des espaces clients Organikk (réf. `organikk-next/public/espace-leexi/index.html`).

## Sources dans ce dossier

- [[leexi-call-2026-05-21]] — transcript nettoyé du premier call de découverte (2026-05-21)
- [[leexi-call-2026-06-24]] — transcript nettoyé du call #2, session de travail / validation des axes mots-clés (2026-06-24)
