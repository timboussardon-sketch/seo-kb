---
type: source
source_type: client-note
title: "Alexia — résumé du call 1 (setup système Claude, 2026-06-24)"
aliases: [alexia-call-1-resume, alexia-call-setup-claude]
client: Alexia (agence Alexandrie / alexia.io)
tags: [alexia, client, accompagnement-1-1, resume-call, setup, skills, workflow, claude]
created: 2026-06-24
updated: 2026-06-24
sources: 1
confidence: high
status: stable
---

# Call 1 — Setup du système Claude (2026-06-24)

> Premier call de travail après le cadrage du [[alexia-call-cadrage|2026-06-10]]. Participants : Alexia Vigo (alexia.vigo@alexandrie.io), Tim Boussardon. Enregistré, pas partagé en vidéo. Notes brutes : Gemini.

## En résumé

Call d'installation : on structure les dossiers locaux d'Alexia (Cloud / Context / Skills / Workflow), on corrige le pack de skills, et on cale la méthode (skill vs workflow, contexte obligatoire, rédaction 80/20, surveillance des tokens). Décision : démarrer sur 5 clients prioritaires sur 30 jours, fondations d'abord, pas de résultats immédiats.

## Contexte client

- Portefeuille : 11-12 clients au total, dont 5-6 nouveaux. 4-5 sites importants à traiter en priorité (e-commerce + un site de lead gen en menuiserie sur mesure).
- Douleur principale : les rapports mensuels prennent 2-3 h par client et retardent tout le planning. Charge alourdie par la préparation des soldes, les briefs de rédaction et la hausse de fréquence des appels clients.
- Besoin exprimé : un tableau de bord centralisé pour suivre les décisions prises en réunion (sentiment de se perdre dans le suivi).
- Objectif de gain : libérer ~25 h/mois, à réinvestir dans la réflexion stratégique, pas dans l'exécution.

## Décisions

- **5 clients prioritaires testés en parallèle** sur 30 jours (recherche mots-clés → audit → rédaction → suivi), puis duplication.
- **Patience assumée** : le système complet demande ~30 jours pour être opérationnel. Priorité aux fondations, pas aux résultats immédiats.
- **Un seul espace de travail Claude** pour tous les clients (pas un projet par client) : l'IA apprend de toutes les expériences, succès comme erreurs.
- **Données en local d'abord**, indépendamment de Claude / ChatGPT : base de connaissances transférable vers n'importe quelle plateforme (Claude reste supérieur sur les tâches longues).
- **Résumé transmis à Adrien, vidéo non partagée** (confidentialité, confort d'Alexia).

## Méthode posée

- **Skill vs Workflow** : un skill = une tâche spécifique (ex. trouver des mots-clés business) ; un workflow = une chaîne de 8-9 skills pour un projet global. Le workflow se lance pour un nouveau client, les skills seuls pour des requêtes ponctuelles.
- **Le contexte fait tout** : sans données riches (Search Console, notes d'appels, briefs, personas, emails, SAV), Claude ne produit rien de probant. Le système doit être nourri.
- **L'IA assiste, ne remplace pas** : garde-fou contre la « dette cognitive ». Continuer les vérifications manuelles en Search Console pour rester un consultant pertinent.
- **Sourcing mots-clés sur Reddit et X (via Grok)** : partir des besoins réels et des émotions des utilisateurs, pas de listes de mots isolés.
- **Ton de voix** : fournir à Claude des exemples de contenus existants du client (vidéos YouTube, posts) pour qu'il modélise le ton, plutôt que de le décrire à la main.
- **Rédaction 80/20** : 80 % généré par l'IA, 20 % humain (anecdotes, données spécifiques). Créer des modèles de page (structure Hn, besoins sectoriels), s'appuyer sur des pages déjà validées comme exemples. L'IA excelle sur les pages factuelles (comparateurs, simulateurs). Pas de tout-automatique sans supervision (risque d'indexation).
- **Veille externe** : ajouter articles, influenceurs, chaînes YouTube dans un dossier de veille pour que l'IA s'enrichisse en continu.
- **Surveillance des tokens** : éviter les longs échanges conversationnels pour ajouter des outils (consomme inutilement). Ajout manuel des skills via « personnaliser » de préférence. Rester dans le budget de 20 €.

## Setup technique réalisé

- Structure de dossiers locale : racine **Cloud** avec sous-dossiers **Context** (ton de voix, stratégie), **Skills**, **Workflow**. Pensée pour une portabilité future vers Obsidian.
- Test de navigation : demander à l'IA de localiser un dossier précis (ex. « clustering ») pour valider qu'elle lit la structure locale.
- Installation des skills via l'interface « personnaliser » ; forcer le chemin d'accès si l'IA ne trouve pas une compétence. Toujours autoriser les accès.
- Vérifier l'usage réel des skills via la barre latérale (« flight bar ») des conversations : elle détaille fichiers et compétences sollicités.
- Lecture des fichiers Markdown sur Mac : utiliser un viewer dédié (type « MD Viewer »).
- Format des livrables : articles en `.md` ; pour le web, copier le texte dans un Google Doc puis exporter en MD.
- Constat : le pack de skills initial contient des erreurs de structure et des éléments manquants → Tim corrige.

## Prochaines étapes

**Tim**
- Corriger le pack de skills sur le dashboard (erreurs de contenu et de nommage).
- Transmettre les 8 compétences retravaillées pour intégration locale.

**Alexia**
- Envoyer par email la liste des 5 clients prioritaires (trafic + enjeux par client).
- Créer un compte Reddit (recherche de mots-clés et veille).
- Déployer et tester le système sur les 5 clients (mots-clés → audit → rédaction → suivi, sur 30 jours).
- Structurer l'arborescence locale (Cloud / Context / Skills / Workflow).
- Renommer les fichiers de skills aux noms corrects ; télécharger et réintégrer les compétences depuis le dashboard mis à jour ; supprimer le fichier résumé de compétences obsolète du dossier de contexte ; ajouter manuellement les 8 compétences dans le dossier local.
- Créer les personas des 5 sites cibles (via Claude).
- Documenter les process actuels (mots-clés, audit, rédaction).
- Centraliser les ressources de veille (sites, influenceurs, articles SEO) et synthétiser les échanges clients pour enrichir la base locale.
