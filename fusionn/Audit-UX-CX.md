# Audit UX et expérience client, Fusionn

Date : 2026-05-21. Audit en 3 lots : acquisition/onboarding, conversion/premium, rétention/workspace.

## Constat

Fusionn est riche en fonctionnalités, mais le parcours client fuit à chaque couture. Le produit délivre de la valeur une fois qu'on est dedans. Le problème est tout autour : l'acquisition perd les nouveaux venus, la promesse change trois fois entre la landing et l'app, la conversion est confuse, et rien ne fait revenir le client. Les chantiers à plus fort levier (réparer le tunnel d'acquisition, ajouter une boucle de rétention) sont peu coûteux au regard de leur impact.

## Tier 1, le tunnel d'acquisition fuit (priorité absolue)

1. **La confirmation email casse l'élan.** Inscription par email : l'utilisateur doit quitter Fusionn, ouvrir sa boîte mail, confirmer, revenir, se reconnecter. Le mot-clé qu'il avait tapé sur la landing est perdu. Point de chute n°1 du funnel. `AuthModal.tsx:120-126`. Fix : connexion immédiate (confirmation asynchrone non bloquante), et persister le mot-clé en localStorage pour le rejouer.
2. **Trois promesses produit incohérentes.** Landing : « en 1 clic, votre liste de mots-clés ». Onboarding : « analyse en 3 étapes ». App : un chat conversationnel. Aucune ne prépare à la suivante. Fix : aligner la promesse sur la réalité conversationnelle, montrer une vraie capture du chat.
3. **L'onboarding fait doublon avec le HeroInput.** 3 modales pour arriver à un écran (le HeroInput) qui propose déjà la même chose. `OnboardingOverlay.tsx` vs `HeroInput.tsx`. Fix : supprimer l'overlay ou le réduire à un seul écran, et le désactiver quand un mot-clé vient de la landing.
4. **Promesse freemium mensongère.** La landing annonce « accès complet aux résultats », « toutes les analyses » ; or des résultats sont verrouillés (`PremiumUpgradeBanner`). Promesse rompue juste avant l'achat. `Landing.tsx:638,644,656`. Fix : aligner le wording landing et modale sur la réalité.

## Tier 2, conversion lisible

5. **Trois quotas gratuits contradictoires.** 5 recherches (non renouvelables), 3 analyses HN, 5 analyses sémantiques, jamais expliqués ensemble. La modale affiche « 5 » HN au lieu de « 3 ». `types.ts:80-86`, `SubscriptionChoiceModal.tsx:150`. Fix : un récap unique et cohérent des quotas.
6. **Annuel présenté de façon trompeuse.** Affiché « 20€/mois » sans jamais montrer le débit réel (240€ en une fois), sans badge d'économie visible. `SubscriptionChoiceModal.tsx:210-230`. Fix : « 20€/mois, 240€ facturés une fois par an » + badge « -31% ».
7. **Le paywall arrive sans préavis.** À la 6e recherche, la modale de pricing remplace les résultats attendus, sans avertissement et sans rappeler la valeur déjà produite. `Compte.tsx:369-372`. Fix : message « dernière recherche gratuite » visible avant, et modale de blocage qui rappelle ce que l'utilisateur a généré.
8. **Messages d'erreur de checkout techniques.** « URL de redirection invalide », « Session expiree. » sans action proposée. `Compte.tsx:386-404`. Fix : messages orientés action.

## Tier 3, rétention (presque gratuit, données déjà présentes)

9. **Aucun mécanisme de rétention.** Pas de notification, pas d'email de relance, pas de rappel. `last_opened_at` est écrit mais jamais lu. Rien ne fait revenir le client. Fix : email/notif de reprise sur un projet laissé en cours.
10. **Aucune section « à reprendre ».** Un article à moitié rédigé ne génère aucun rappel. Fix : section « Reprendre » en tête du compte (basée sur `last_opened_at` + `editor_content` non vide). Meilleur ratio effort/impact.
11. **L'historique est un cimetière de recherches, pas de projets.** Les cartes ignorent `workspace_name`, l'extrait d'éditeur, les livrables produits. `DraggableSearchItem.tsx`. Fix : carte « projet » avec nom, extrait, badges de livrables.
12. **`created_at` muté à chaque ouverture.** Une analyse de janvier affiche « créé aujourd'hui ». `Compte.tsx:234`. Fix : ne jamais muter `created_at`, trier sur `last_opened_at`.
13. **Dédup historique par mot-clé seul.** Deux analyses du même mot-clé fusionnent, l'une disparaît. `Compte.tsx:73-83`. Fix : dédup par mot-clé + contexte, ou groupement visuel.

## Tier 4, workspace exploitable

14. **15 onglets à plat, sans hiérarchie.** L'utilisateur ne sait pas par où commencer. `ResultsNav.tsx:44-60`. Fix : 3 groupes (Comprendre / Produire / Décider), ordre suggéré, icônes uniques.
15. **Aucune action « quoi en faire ».** Chaque vue affiche un tableau, jamais comment l'exploiter (copier, exporter ce bloc, JSON-LD pour la FAQ, envoyer vers l'éditeur). Fix : encart « quoi en faire » + actions par vue.
16. **Conversationnel et workspace sont deux produits.** Pas de pont, pas de vocabulaire commun, transition sans atterrissage. Fix : fil d'Ariane partagé, écran d'accueil du workspace au premier passage.
17. **Onglets toujours visibles mais vides** avec un message qui ment (« sera généré lors de votre prochaine recherche » alors que c'est un bouton de génération). Fix : corriger le wording, état « cliquez pour générer ».

## Tier 5, dette et finitions

18. **Code mort.** `SidebarNavigation.tsx` (nav doublon, vocabulaire divergent) et `PremiumModal.tsx` (jamais importé). Fix : supprimer.
19. **Section témoignages.** (Correction : l'audit l'avait prise pour des photos de stock, mais Tim confirme que ce sont de vrais clients. La section est conservée.) Piste d'amélioration possible : ajouter un verbatim, un prénom et une activité sous chaque photo pour renforcer la preuve sociale.
20. **Wording et accents incohérents** dans toute l'app (texte accentué et non accentué mélangé). Fix : passe d'uniformisation.
21. **Mobile cassé.** Nav workspace = 15 onglets en scroll horizontal (moitié cachée) ; mode rédaction = éditeur à 50vh inutilisable ; `100vh` au lieu de `100dvh`. Fix : nav mobile en menu, éditeur plein écran en onglets, `100dvh`.

## Ordre d'attaque recommandé

Tier 1 d'abord : c'est le trou dans le seau, tout le reste sert peu si les nouveaux venus n'arrivent jamais à leur premier résultat. Puis Tier 3 (rétention), excellent rapport effort/impact car les données existent déjà. Puis Tier 2 (conversion), Tier 4 (workspace), Tier 5 (dette).
