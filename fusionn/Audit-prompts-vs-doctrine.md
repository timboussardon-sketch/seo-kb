# Audit — Prompts IA Fusionn vs doctrine SEO (skills)

Date : 2026-05-21. Référence = les skills `~/.claude/skills/seo-*`. 17 fonctions auditées.

## Verdict global

| Fonction | Skill de référence | Verdict |
|---|---|---|
| generate-faq | article-engine-pipeline / faq-query | ✅ À JOUR |
| analyze-geo-sentinel | (aucun skill GEO) | ✅ Fidèle au fond, mais pas de skill |
| generate-micro-intentions | seo-recherche / seo-clustering | 🟠 Partiel |
| generate-vecteurs | seo-entites-vectorielles | 🟠 Partiel |
| analyze-semantic-score | seo-entites-vectorielles | 🟠 Partiel |
| generate-hn-structure | seo-brief-contenu | 🟠 Partiel |
| generate-objections | seo-peurs-objections | 🟠 Partiel |
| generate-tools | seo-product-led-seo | 🟠 Partiel |
| generate-business-score | seo-mots-cles-decisionnels | 🟠 Partiel |
| generate-models | (taxonomie décision) | 🟠 Partiel |
| generate-semantic-keywords | seo-recherche-mots-cles | 🔴 Obsolète |
| generate-semantic-analysis | seo-entites-vectorielles | 🔴 Obsolète |
| generate-brief | seo-brief-contenu | 🔴 Obsolète |
| generate-brief-redaction | seo-brief-contenu | 🔴 Obsolète |
| analyze-hn-score | seo-brief-contenu | 🔴 Obsolète |
| generate-pseo-strategy | seo-programmatique-pseo | 🔴 Obsolète |
| generate-topical-authority | seo-cluster-aeo | 🔴 Obsolète |

**Bilan : 1 à jour, 1 fidèle sans skill, 8 partielles, 7 obsolètes.** Les prompts Fusionn ont divergé de la doctrine codifiée dans les skills — la doctrine a évolué, l'app n'a pas suivi. Seul `generate-faq`, dérivé quasi mot-pour-mot du fichier de référence `faq-query.md`, est aligné — c'est le modèle à suivre.

## Divergences systémiques (transverses, prioritaires)

1. **Taxonomie d'intention obsolète.** Plusieurs fonctions utilisent encore `Informationnel/Comparatif/Transactionnel` ou `TOFU/MOFU/BOFU` au lieu de **Know-Simple / Know / Do**. `Know-Simple` est absent partout. `seo-cluster-aeo` interdit explicitement TOFU/MOFU/BOFU. → generate-semantic-keywords, generate-micro-intentions, generate-models, generate-topical-authority, generate-business-score.

2. **Règle anti-hallucination absente.** La règle « jamais de chiffre inventé → placeholder `[À SOURCER]` » est centrale (skills mots-clés, pSEO, entités). Plusieurs prompts font l'inverse : ils demandent au LLM d'inventer des scores (`relevance`, `cosine_similarity`, `intention_score`, difficulté pSEO). → generate-semantic-keywords, generate-micro-intentions, generate-pseo-strategy.

3. **Surprise Gap / Haute Surprise absent.** Pilier de la doctrine, absent de ~9 fonctions (entités, brief, structure, outils, pSEO, scores). Bien présent uniquement dans analyze-geo-sentinel et generate-objections.

4. **Anti-AI writing absent.** Aucun garde-fou anti-écriture-IA dans les prompts qui produisent du texte/recommandations (seules des règles de formatage JSON).

5. **Étapes de pipeline manquantes.** Gap concurrentiel, recommandations par zone (H1/corps/FAQ), maillage interne, Schema.org par page, roadmap, priorisation top 3 : les skills ont des pipelines en N étapes dont Fusionn n'implémente qu'une partie.

6. **Ne pas copier les concurrents.** La règle « regarder les concurrents pour ce qu'ils n'ont PAS dit » n'est nulle part ; generate-faq injecte même le top 10 Google pour « identifier les questions ».

## Bugs annexes découverts

- `generate-brief` lit `hnStructure.structure_html` → la colonne réelle est `structure_proposee` : le contexte Hn n'arrive jamais dans le brief.
- `generate-hn-structure` : le code lit `note_globale`, jamais produite par le prompt → score toujours 0.
- `generate-brief` et `generate-brief-redaction` sont deux décodages RRF quasi identiques — aucun des deux ne produit un vrai brief (structure Hn + FAQ + contenu par H2).
- `analyze-hn-score` (/10) et `generate-hn-structure` (/5) : deux barèmes incohérents pour auditer la même chose.
- `generate-topical-authority` : prompt rédigé en anglais alors que le marché est francophone.

## Skills manquants

- **GEO** : `analyze-geo-sentinel` encode 7 frameworks doctrinaux (Surprise, Grounding, Content Effort, RRF, RAG Structurer, Freshness, Action Engine) mais aucun skill ne les versionne.
- **Modèles pSEO** : `generate-models` n'a pas de skill source de vérité (d'où un patch « CONTEXTE GEO » pédagogique inline).

## Recommandation

Re-dériver chaque prompt obsolète/partiel depuis son skill, comme `generate-faq` l'a été depuis `faq-query.md`. Créer les 2 skills manquants. Ordre suggéré : corriger d'abord les 3 divergences systémiques (taxonomie, anti-hallucination, Surprise Gap) qui touchent le plus de fonctions, puis les 7 obsolètes une par une.
