# Prestation — Catherine

- Slug : catherine
- Domaine : consultante marketing (SEO/GEO), Canada
- Type : accompagnement 1:1 consultant (système Claude + Obsidian, calqué Alexia)
- Statut : démarrage (call découverte 2026-06-11, proposition 1 500 € HT ; espace client ouvert 2026-07-03)
- Offre : setup + workflows hebdo, mois 1 calls hebdo puis async

## Où on en est
Étape courante : phase de démarrage — questionnaire en ligne, en attente de ses réponses
Prochaine action : quand les réponses arrivent (admin.html ou table Supabase), préparer le cadrage et ouvrir les onglets suivants du dashboard (Programme, Ressources, Installation)

## Accès et data
- GSC : à confirmer (question 12 du questionnaire)
- Data propriétaire reçue : transcript call découverte + résumé/proposition (raw/organikk/clients/catherine/)
- Outillage connu : ChatGPT entraîné + Claude (premier jet révisé), SEMrush coupé (250 $ CAD/mois)

## Journal des étapes faites
| Date | Étape (roadmap) | Ce qui a été fait | Output | Skill |
|---|---|---|---|---|
| 2026-07-03 | 1 | Dashboard client créé (gabarit Alexia) : seul l'onglet Questionnaire est ouvert, le reste verrouillé. Réponses persistées en ligne (Supabase `client_selections`, doc_key `catherine-accompagnement`) + localStorage ; `admin.html` pour lire ses réponses. **Déployé sur organikk.co** (push validé par Tim, vérifié live : 200 + X-Robots-Tag noindex) | organikk.co/catherine-accompagnement/ | roadmap-prestation |

## Spécificités client
- Canada : tarif énoncé 1 500 € HT, conversion CAD + taxes à trancher avant facturation.
- Douleur n°1 : les rapports clients (outils compliqués, reprise à la main) ; douleur n°2 : par où commencer sur un nouveau client (éparpillement SEO/GEO).
- Ses process marketing hors SEO tournent bien : ne pas y toucher.
- Cas qui marche : nettoyage de conduits de ventilation (leads) — la méthode existe, elle n'est pas encodée.
- Questionnaire adapté en conséquence (rapports clients + par où commencer, pas de pré-rempli).
