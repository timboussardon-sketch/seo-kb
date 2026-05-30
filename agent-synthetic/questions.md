# Questions de l'agent — « comment faire mieux »

Écrit par l'agent 10 (auto-interrogation) à chaque édition. Deux niveaux :
- **Urgent** : remonté à Tim tout de suite (en bas du draft).
- **Hebdo** : groupé, présenté à la revue hebdo du vendredi.

L'agent répond lui-même à ce qu'il peut tester ; il garde pour Tim ce qui demande un arbitrage humain.

## Urgent (à trancher vite)

(vide pour l'instant)

## Pour la revue hebdo

- **Rubrique fixe ?** Faut-il une section récurrente « ce qu'un agent retiendrait de cette édition » pour forcer l'angle citation à chaque numéro ?
- **Format de l'édition de l'après-midi ?** Avec 2 éditions/jour, est-ce que celle de 16h doit passer en format court (une seule info) pour ne pas cannibaliser celle du matin ?
- **Valider les 3 sources auto-ajoutées (v3) ?** `cloudflare-radar` (0.85, données primaires crawl), `similarweb-geo` (0.78), `seer-interactive` (0.75). Toutes corroborées et au-dessus du seuil. Je les garde en `explore` → à confirmer en `exploit` ou à retirer.
- **Sources mises en attente (sous le seuil / mono)** : Conductor, TechnologyChecker, ALM Corp, vertu, InfoQ. Apparues une fois, autorité moyenne ou agrégateurs. Je ne les ajoute pas en autonomie. À trancher : en intègre-t-on certaines (InfoQ semble sérieux) ?
- **Diff de skill proposé ?** Aucun pour l'instant. Quand un pattern de titraille reviendra gagnant 3 fois, je proposerai ici un diff de `ton-de-voix-tim` à valider. Piste émergente : un garde-fou explicite « vérifier date primaire » dans le socle `revue-presse-quotidienne` (le piège fraîcheur s'est représenté ce run). À formaliser en diff si ça revient une 3e fois.

## Ce qui aurait rendu cette édition (v3) meilleure

- Un chiffre de conversion du trafic IA daté de 2026 et vérifié sur primaire (au lieu de Seer 2025) aurait renforcé la brève conversion. Les données 2026 existent (Similarweb) mais je n'ai pas confirmé le primaire faute de budget de fetch. À refaire proprement quand le sujet revient.
- Un retour terrain FR (un e-commerçant français face à UCP) aurait ancré l'info du jour côté lecteur. Aucune source FR fraîche trouvée sur UCP côté marchand. Candidat veille Abondance.

## À tester par l'agent lui-même (passe en directives.md)

- Tester 1 source neuve par édition (fait au run d'amorçage avec Lumar).

## Sources découvertes en autonomie (journal)

- **2026-05-30** : `lumar` (lumar.io, industry news SEO/IA) ajoutée en statut `explore`, trust 0.62. Corroborée par blog.google et SEJ sur I/O 2026, donc au-dessus du seuil d'auto-ajout (0.6 + corroboration). À confirmer ou retirer en revue hebdo.
- **2026-05-30 (v3)** : `cloudflare-radar` (blog.cloudflare.com / Radar) ajoutée en `explore`, trust 0.85, données primaires crawl-to-refer corroborées par TechnologyChecker + SEOmator. `similarweb-geo` (similarweb.com/blog/marketing/geo) en `explore`, trust 0.78, clickstream. `seer-interactive` (seerinteractive.com/insights) en `explore`, trust 0.75, études conversion. Les trois au-dessus du seuil d'auto-ajout (0.6 + corroboration). À confirmer/retirer en revue hebdo. Note vigilance fraîcheur enregistrée dans le registre pour Seer et Cloudflare (agrégateurs qui redatent en 2026 des études 2025).

## Propositions doctrine (à valider en revue hebdo, non appliquées)

- **Hypothèse candidate pour `wiki/hypotheses.md`** : « Avec le commerce agentique (UCP/Universal Cart), la qualité du flux produit structuré (attributs, prix, dispo, Conversational Attributes Merchant Center) devient un facteur de sélection plus fort que le contenu éditorial de la page pour les requêtes transactionnelles. » Prolonge `mots-cles-actionnels` et `agentic-search`. À tester quand des données de sélection d'agent seront publiques. Lié à la prédiction P-2026-05-30-2.
- **Signal pour `wiki/concepts/agentic-search.md`** : l'actu UCP conforte le concept (« être sélectionné par l'agent pour accomplir une tâche ») et le précise côté ACHAT (l'agent ne fait plus que lire/comparer, il transige). Candidat ajout d'une section « agent qui achète » au concept, à valider.

## Sous-skills créés en autonomie (journal)

Toute skill créée ou modifiée par l'agent est tracée ici, avec le commit git correspondant.

(vide pour l'instant)
