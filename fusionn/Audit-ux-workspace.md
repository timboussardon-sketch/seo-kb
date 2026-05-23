# Audit UX/UI — Workspace Fusionn

Date : 2026-05-21. Périmètre : la partie *workspace* de l'app (repo `~/Code/newFusionn`) — shell `WorkspaceLayout`, navigation d'onglets `ResultsNav`, dispatch des vues `ResultsContainer`, CSS global `index.css`, tokens `tailwind.config.js`.

Déclencheur : « les onglets, parfois gris, parfois blanc, c'est illisible ».

## 1. Cause exacte du « parfois gris, parfois blanc »

`WorkspaceLayout.tsx` (≈ l.419) : le fond de la zone de contenu est piloté par une **liste d'onglets codée en dur**.

```jsx
style={
  ['tools','microIntentions','faq','objections','semantic','models',
   'vecteurs','briefRedaction','hnStructure'].includes(analyzeSubView)
    ? { background: '#FFFFFF' }
    : undefined   // sinon le CSS applique #FAFAF9
}
```

9 onglets sur 15 passent en blanc pur, les 6 autres (Mots-clés, Clusters, Carte, Business, Stratégie pSEO, Conversation) retombent sur le gris `#FAFAF9`. Changer d'onglet fait sauter le fond. La liste n'encode aucune logique explicite (en réalité : « la vue rend-elle sa propre carte ou du contenu plat »).

## 2. Inconsistances classées par gravité

### Critique
- **A — Fond de page conditionnel** (ci-dessus).
- **B — Padding empilé.** `.workspace-strategy-content` met déjà `padding: 24px`. `microIntentions` rajoute `p-8 sm:p-10` (→ 56-64px), `actionPlan` rajoute `p-12` (→ 72px). Inset variable du simple au triple.
- **C — `bg-white` ≠ blanc.** `tailwind.config.js` redéfinit le token `white` → `#FAFAF9`. Les cartes en `className="bg-white"` sont donc `#FAFAF9`, invisibles sur une page `#FAFAF9`. Le reste du code utilise `#FFFFFF` littéral. Deux « blancs » contradictoires.

### Important
- **D — 3 quasi-blancs** sans règle : `#FFFFFF`, `#FAFAF9`, `#FAFAFA`.
- **E — 3 familles de gris** : palette *stone* définie dans le config Tailwind mais jamais utilisée ; *cool-gray* codé en dur dans le CSS ; *slate* codé en dur dans toute la vue Conversation.
- **F — 3 modèles d'onglet actif** : sidebar Stratégie (fond rosé + barre rouge), nav Rédaction (fond blanc + ombre), segmented control (texte foncé). Aucun composant d'onglet unifié.
- **G — Traitement « carte » incohérent** : vues nues / cartes bordées / bloc padé sans bordure.

### Mineur
- **H — CSS dupliqué** : `.streaming-cursor` ×2, `@keyframes fadeIn` ×2.
- **I — Échelle de rayons anarchique** : 4/6/8/10/12/16/20px.
- **J — Hovers incohérents** : `#F3F4F6` / `#E5E7EB` / `#F9FAFB`.
- **K — Deux noirs** : `#212121` et `text-gray-950` (`#030712`).
- **L — 3 mécanismes de style mêlés** : classes CSS, classes Tailwind, styles inline hex.

## 3. Corrections appliquées (2026-05-21)

### Fix immédiat — fin du clignotement
- Suppression du fond conditionnel : la page Stratégie est **toujours** `#FAFAF9`.
- Chaque vue « plate » est enveloppée dans une carte standard `.workspace-view-card` (blanc, bordure, rayon, padding uniques) → modèle « carte blanche sur fond gris » homogène sur tous les onglets.
- Suppression du padding ad hoc `p-8 sm:p-10` de `microIntentions`.

### Système de tokens
- Bloc `:root` de variables CSS (`--ws-bg-page`, `--ws-bg-card`, `--ws-border`, `--ws-text-*`, `--ws-brand`, `--ws-radius-*`).
- Migration du CSS workspace vers ces variables (valeurs identiques → zéro changement visuel).
- Unification `#FAFAFA` → `#FAFAF9`.
- Suppression des doublons CSS (`.streaming-cursor`, `@keyframes fadeIn`).

## 4. Reste à faire (non traité — risque ou refacto large)

- **Token `white` du Tailwind config** : pointe toujours sur `#FAFAF9`. Le remettre à `#FFFFFF` impacte tous les `bg-white` de l'app → à traiter à part, avec relecture.
- **Vue Conversation** : encore en palette *slate* codée en dur.
- **Composant d'onglet unifié** : les 3 modèles d'onglet actif (F) ne sont pas fusionnés.
- **Échelle de rayons** : à normaliser sur `--ws-radius-*`.
