---
title: "Jour 1 Semaine 4 — Données structurées automatiques (skill distribuable + pédagogie)"
bootcamp: 4
semaine: 4
jour: 1
type: skill-distribuable
usage: "Bundle Drive S4 J1. Skill HORS pack des 9, vraie nouvelle install. Le balisage qui se génère depuis le contenu = un module d'automatisation, cohérent avec le thème S4 (automatisations + prospection)."
related:
  - "[[sequencage-semaine-3]]"
  - "[[skill-maillage-systeme]]"
  - "[[skill-maillage-gsc-cannibalisation]]"
  - "[[session-2-redaction-resume-participants]]"
  - "[[observations-whatsapp-bootcamp]]"
---

# Jour 1 Semaine 4 — Le balisage qui se génère tout seul

Salut à tous,

Semaine 4, on bascule sur les automatisations. Premier module : les données structurées (le JSON-LD, schema.org). Pas le balisage à la main case par case. Le balisage qui se génère depuis le contenu, tout seul, et qui se met à jour quand le contenu change.

## Pourquoi c'est dans la semaine automatisations

Le schema fait à la main, c'est de la dette. Tu le tapes, tu modifies l'article trois semaines plus tard, le schema ment, Google dégrade ta page. Un balisage qui se dérive du contenu ne ment jamais : il dit exactement ce qui est sur la page, parce qu'il EST la page lue autrement. C'est exactement la logique de la semaine : ce qui peut se générer depuis ta donnée ne doit plus se taper.

Ce que ça te rapporte concrètement chez ton client : éligibilité aux rich results Google (FAQ, fil d'Ariane, vidéo, HowTo), et surtout une entité unique consolidée que les moteurs de réponse savent citer. C'est du levier AEO direct, pas de la déco technique.

## Les 3 règles, en clair

- Source unique : tout le balisage du site sort d'un seul fichier. Aucun bloc schema écrit en dur dans une page.
- Une seule entité, référencée, jamais répétée : l'identité (la marque, toi en tant qu'auteur) est déclarée une fois pour tout le site. Chaque page pointe dessus par référence. Google recolle tout et comprend une seule entité. C'est ça qui construit ta présence dans son knowledge graph, pas le fait de répéter ton nom partout.
- Le schema se déduit du contenu, jamais saisi : une FAQ sur la page génère le FAQPage toute seule. Une vidéo génère le VideoObject. Un H2 d'étapes génère le HowTo. Tu n'écris jamais le schema, tu écris le contenu, le schema suit.

## Le piège à éviter

On n'invente jamais un signal. Pas de FAQPage si la page n'a pas de FAQ visible. Pas de note, d'avis ou de prix qu'on ne peut pas prouver. Un faux signal structuré, Google le voit et il dégrade la page. Le balisage dit la vérité du contenu, sinon il se retourne contre toi.

## Site Next.js vs WordPress / no-code

Le code de référence ci-dessous est pour un site Next.js (App Router), comme organikk.co. Si ton client est sur WordPress ou un autre CMS, tu n'appliques pas le code, mais les 3 règles restent identiques : une entité référencée une fois, schema dérivé du contenu, jamais de faux signal. Sur WordPress ça passe par la config du thème ou un plugin de schema, pas par ce fichier. Si tu es dans ce cas, MP aujourd'hui, on cadre ta version sans terminal, on ne perd personne là-dessus.

---

## Procédure d'install / vérification

Skill HORS pack des 9. Vraie nouvelle install, deux fichiers.

1. Dossier `~/.claude/skills/seo-donnees-structurees/`
2. `SKILL.md` = le premier bloc entre `=====` ci-dessous
3. Sous-dossier `~/.claude/skills/seo-donnees-structurees/references/`
4. `references/schema-reference.ts` = le second bloc entre `=====` ci-dessous
5. Relance Claude, vérifie avec `/skills` (tu dois voir `seo-donnees-structurees`)

Déclenchement : il part tout seul dès que tu dis "données structurées", "JSON-LD", "schema.org", "rich results", "balisage", "FAQPage", "HowTo", ou tu l'appelles avec `/seo-donnees-structurees`.

GSC / terminal / WordPress qui coince ? MP aujourd'hui, pas jeudi.

=====

---
name: seo-donnees-structurees
description: >
  Mise en place de données structurées JSON-LD automatiques sur un site Next.js
  (App Router) : graphe d'entité site-wide unique référencé par @id, et schémas
  par page DÉRIVÉS du contenu (Article, FAQPage, HowTo, VideoObject,
  BreadcrumbList) sans saisie manuelle. Généralisé à partir du système en
  production sur organikk-next (src/lib/schema.ts).

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "données structurées",
  "schema.org", "JSON-LD", "rich results", "rich snippets", "balisage",
  "FAQPage", "HowTo schema", "BreadcrumbList", "VideoObject", "entité Google",
  "knowledge graph du site", "@id graph", ou demande d'ajouter, refondre ou
  auditer le balisage structuré d'un site (en priorité Next.js App Router).
---

# Skill — Données structurées JSON-LD automatiques

## Quand déclencher

Ajouter, refondre ou auditer le balisage structuré d'un site. Objectif : éligibilité aux rich results Google ET consolidation d'une entité unique exploitable par les moteurs de réponse (AEO). Pas du schema décoratif, du schema qui sert le Grounding et la citation.

## Principe non-négociable

Trois règles, dans cet ordre. Si l'une saute, le skill a échoué.

1. **Source unique.** Tout le JSON-LD vient d'un seul module (`lib/schema.ts`). Aucun bloc schema écrit en dur dans une page.
2. **Une entité, référencée par `@id`.** Le graphe site-wide (Organization, WebSite, Person) est émis une seule fois dans le layout racine. Chaque page de contenu pointe vers ces nœuds par `@id` (author / publisher / isPartOf), elle ne redéclare jamais l'auteur ni l'éditeur. Google fusionne tous les blocs d'une page et consolide une seule entité. C'est ça qui construit le knowledge graph du site, pas la répétition.
3. **Le schema est dérivé du contenu, jamais saisi à la main.** Un champ schema qui n'est pas calculé depuis la donnée de la page est une dette : il se désynchronise au premier edit. Si on doit le taper deux fois, c'est cassé.

## Architecture de référence

Graphe site-wide (`siteGraph()`, émis dans le layout racine) :

- `Organization` (+ `ProfessionalService` si activité de service) avec `@id = {SITE_URL}/#organization`
- `WebSite` avec `@id = {SITE_URL}/#website`, `publisher` -> ref Organization
- `Person` (fondateur / auteur) avec `@id = {SITE_URL}/#person-...`, `worksFor` -> ref Organization
- `ImageObject` logo avec `@id = {SITE_URL}/#logo`, partagé par `logo` et `image`
- `sameAs` : profils sociaux réels (LinkedIn, YouTube, X, Substack). Pas d'URL inventée.

Refs légères exportées et réutilisées partout : `AUTHOR_REF = {'@id': PERSON_ID}`, `PUBLISHER_REF = {'@id': ORG_ID}`, `WEBSITE_REF = {'@id': WEBSITE_ID}`.

## Règle de dérivation automatique (le cœur du skill)

Chaque type de schema se déduit d'un signal présent dans la donnée de la page. Tableau de correspondance à appliquer :

| Signal dans le contenu | Schema émis | Dérivation |
|---|---|---|
| Toute page article / post | `Article` ou `BlogPosting` | titre, excerpt, date, section ; `wordCount` calculé par `countWords()` ; `keywords` depuis les highlights ; author/publisher/isPartOf = refs |
| Toute page (toujours) | `BreadcrumbList` | `breadcrumb()` à partir du chemin (Accueil > rubrique > titre) |
| Bloc `faq` présent dans les sections | `FAQPage` | `mainEntity` = map des items q/a en Question/Answer. Zéro saisie |
| Section `video` présente | `VideoObject` | ID YouTube extrait par regex de l'URL ; thumbnail + embedUrl déduits |
| H2 dont le titre matche un prédicat (ex. contient "prompt", "étapes", "tutoriel") | `HowTo` | collecte les H3 numérotés suivants + leur contenu (p / code / listes) en `HowToStep` |
| Page produit / offre avec prix | `Product` / `Offer` | depuis les champs prix/dispo de la donnée. Jamais de prix inventé |

Principe : on ne demande jamais à l'utilisateur "quel schema veux-tu". On lit la structure de la page et on émet ce que la structure prouve. Un schema sans preuve dans le contenu = suppression.

## Procédure

1. **Détecter le terrain.** Framework et version. Si Next.js : App Router ou Pages ? Lire la doc du projet (sur organikk-next : `node_modules/next/dist/docs/`, conventions imposées par AGENTS.md) avant d'écrire une ligne. Ne jamais présumer l'API metadata.
2. **Cartographier le modèle de données.** Où vivent les articles, pages, FAQ, vidéos (ex. `src/data/*.ts`). Identifier la forme des sections (le schema se dérive de là).
3. **Créer / refondre `lib/schema.ts`** : config d'identité en tête (SITE_URL, identité Organization/Person/sociaux), les nœuds, `siteGraph()`, les refs `@id`, les helpers `breadcrumb()` et `countWords()`. Partir de `references/schema-reference.ts`.
4. **Câbler le layout racine** : un seul `<script type="application/ld+json">` avec `siteGraph()`.
5. **Câbler chaque template de contenu** : construire un tableau `jsonLd[]` (Article + breadcrumb toujours, puis FAQ / Video / HowTo conditionnels selon les signaux), sérialisé dans UN script en tête de page.
6. **Dédupliquer.** Supprimer tout ancien bloc Organization/Person redéclaré dans les pages : tout passe par les refs `@id`.
7. **Valider** (voir checklist). Corriger jusqu'à zéro erreur.

## Émission

- Site-wide : un `<script type="application/ld+json">` dans le layout racine, contenu = `siteGraph()`.
- Par page : un seul `<script type="application/ld+json">` en tête, contenu = `JSON.stringify(jsonLd)` où `jsonLd` est le tableau des nœuds de la page.
- App Router : injection via `dangerouslySetInnerHTML` dans un Server Component. Ne pas utiliser de lib tierce, ce sont des objets JS purs.

## Validation (checklist, zéro erreur tolérée)

- [ ] Chaque `@id` site-wide est unique et stable, réutilisé par ref dans les pages
- [ ] Aucune page ne redéclare un nœud Organization ou Person en entier
- [ ] `Article` : headline non vide, `datePublished` valide, `wordCount` calculé (pas codé en dur), author/publisher en ref
- [ ] `FAQPage` émis seulement si un vrai bloc FAQ existe, et chaque réponse est du texte réel
- [ ] `HowTo` émis seulement si des étapes ordonnées existent réellement
- [ ] `VideoObject` : `contentUrl`/`embedUrl` résolus, thumbnail valide
- [ ] `BreadcrumbList` cohérent avec l'URL réelle
- [ ] JSON-LD valide et passe le test Rich Results de Google + le validateur schema.org
- [ ] Aucun champ inventé (prix, note, avis, premier sur X) sans preuve : un faux signal dégrade la note Google de la page

## Anti-patterns (à ne jamais faire)

- Redéclarer l'auteur et l'éditeur sur chaque page au lieu de référencer par `@id`
- Écrire du JSON-LD en dur dans le JSX d'une page
- Émettre un `FAQPage` ou `HowTo` "au cas où" sans contenu correspondant visible sur la page (risque de pénalité, et c'est du mensonge à Google)
- Mettre `aggregateRating` / `Review` / prix non vérifiables
- Multiplier les `<script ld+json>` redondants au lieu d'un tableau unique par page
- Hardcoder `wordCount`, des dates ou des compteurs au lieu de les dériver de la donnée
- Présumer l'API Next.js sans lire la doc de la version du projet

## Référence d'implémentation

`references/schema-reference.ts` : module généralisé prêt à adapter (config d'identité en tête, nœuds, `siteGraph`, refs `@id`, `breadcrumb`, `countWords`, builders `articleSchema` / `faqSchema` / `videoSchema` / `howToFromSections`). C'est la version dé-Organikk-isée du système en production sur `organikk-next/src/lib/schema.ts`. L'adapter au modèle de données du site cible, ne pas le copier tel quel.

## Concepts liés

`aeo` · `grounding-score` · `entites-vectorielles` · `passage-ranking` · `knowledge-graph` · `e-e-a-t`

=====

/**
 * RÉFÉRENCE — Données structurées JSON-LD automatiques (Next.js App Router)
 *
 * Version généralisée du système en production sur organikk-next
 * (src/lib/schema.ts). À ADAPTER au modèle de données du site cible,
 * pas à copier tel quel.
 *
 * Principe : source unique, une entité référencée par @id, schema dérivé
 * du contenu. Ces fonctions ne renvoient que des objets JS purs : c'est
 * le consumer (layout / page, Server Component) qui les sérialise dans
 * un <script type="application/ld+json">.
 *
 * Câblage type :
 *
 *   // app/layout.tsx (Server Component)
 *   import { siteGraph } from '@/lib/schema'
 *   <script type="application/ld+json"
 *     dangerouslySetInnerHTML={{ __html: JSON.stringify(siteGraph()) }} />
 *
 *   // app/blog/[slug]/page.tsx
 *   const jsonLd = [
 *     articleSchema(article, url),
 *     breadcrumb([...]),
 *     ...(faqBlock ? [faqSchema(faqBlock.items)] : []),
 *     ...(video ? [videoSchema(video, article)] : []),
 *     ...howToFromSections(article.sections),
 *   ]
 *   <script type="application/ld+json"
 *     dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
 */

// ─────────────────────────────────────────────────────────────────────────
// 1. CONFIG D'IDENTITÉ — la seule zone à éditer par site
// ─────────────────────────────────────────────────────────────────────────

export const SITE_URL = 'https://example.com'

const IDENTITY = {
  orgName: 'NomDeLaMarque',
  orgDescription: 'Phrase de positionnement, claire, sans superlatif invérifiable.',
  orgSlogan: 'Baseline courte',
  foundingYear: '2020',
  isProfessionalService: true, // ajoute le @type ProfessionalService
  logoPath: '/logo.png',
  knowsAbout: ['SEO', 'GEO', 'AEO'],
  serviceType: ['SEO', 'Audit SEO'],
  areaServedCountry: 'France',
  locality: 'Lyon',
  region: 'Auvergne-Rhône-Alpes',
  countryCode: 'FR',
  email: 'contact@example.com',
  language: 'fr-FR',
  orgSameAs: [
    'https://www.linkedin.com/company/...',
    'https://www.youtube.com/@...',
  ],
  person: {
    slug: 'prenom-nom',
    name: 'Prénom Nom',
    givenName: 'Prénom',
    familyName: 'Nom',
    jobTitle: 'Consultant SEO & GEO',
    aboutPath: '/a-propos',
    portraitPath: '/portrait.png',
    sameAs: [
      'https://www.linkedin.com/in/...',
      'https://x.com/...',
    ],
  },
} as const

// ─────────────────────────────────────────────────────────────────────────
// 2. IDs STABLES + REFS LÉGÈRES
// ─────────────────────────────────────────────────────────────────────────

export const ORG_ID = `${SITE_URL}/#organization`
export const WEBSITE_ID = `${SITE_URL}/#website`
export const PERSON_ID = `${SITE_URL}/#${IDENTITY.person.slug}`
const LOGO_ID = `${SITE_URL}/#logo`

export const AUTHOR_REF = { '@id': PERSON_ID } as const
export const PUBLISHER_REF = { '@id': ORG_ID } as const
export const WEBSITE_REF = { '@id': WEBSITE_ID } as const

// ─────────────────────────────────────────────────────────────────────────
// 3. NŒUDS SITE-WIDE
// ─────────────────────────────────────────────────────────────────────────

const organizationNode = {
  '@type': IDENTITY.isProfessionalService
    ? ['Organization', 'ProfessionalService']
    : 'Organization',
  '@id': ORG_ID,
  name: IDENTITY.orgName,
  legalName: IDENTITY.orgName,
  url: SITE_URL,
  description: IDENTITY.orgDescription,
  slogan: IDENTITY.orgSlogan,
  foundingDate: IDENTITY.foundingYear,
  logo: {
    '@type': 'ImageObject',
    '@id': LOGO_ID,
    url: `${SITE_URL}${IDENTITY.logoPath}`,
    contentUrl: `${SITE_URL}${IDENTITY.logoPath}`,
    caption: IDENTITY.orgName,
  },
  image: { '@id': LOGO_ID },
  founder: { '@id': PERSON_ID },
  knowsLanguage: IDENTITY.language,
  knowsAbout: IDENTITY.knowsAbout,
  serviceType: IDENTITY.serviceType,
  areaServed: { '@type': 'Country', name: IDENTITY.areaServedCountry },
  address: {
    '@type': 'PostalAddress',
    addressLocality: IDENTITY.locality,
    addressRegion: IDENTITY.region,
    addressCountry: IDENTITY.countryCode,
  },
  email: IDENTITY.email,
  contactPoint: {
    '@type': 'ContactPoint',
    email: IDENTITY.email,
    contactType: 'customer support',
    areaServed: IDENTITY.countryCode,
    availableLanguage: 'French',
  },
  sameAs: IDENTITY.orgSameAs,
}

const personNode = {
  '@type': 'Person',
  '@id': PERSON_ID,
  name: IDENTITY.person.name,
  givenName: IDENTITY.person.givenName,
  familyName: IDENTITY.person.familyName,
  url: `${SITE_URL}${IDENTITY.person.aboutPath}`,
  image: {
    '@type': 'ImageObject',
    url: `${SITE_URL}${IDENTITY.person.portraitPath}`,
  },
  jobTitle: IDENTITY.person.jobTitle,
  worksFor: { '@id': ORG_ID },
  knowsAbout: IDENTITY.knowsAbout,
  sameAs: IDENTITY.person.sameAs,
}

const websiteNode = {
  '@type': 'WebSite',
  '@id': WEBSITE_ID,
  url: SITE_URL,
  name: IDENTITY.orgName,
  description: IDENTITY.orgSlogan,
  inLanguage: IDENTITY.language,
  publisher: { '@id': ORG_ID },
}

/** Graphe site-wide : à émettre UNE fois dans le layout racine. */
export function siteGraph() {
  return {
    '@context': 'https://schema.org',
    '@graph': [organizationNode, websiteNode, personNode],
  }
}

// ─────────────────────────────────────────────────────────────────────────
// 4. HELPERS DÉRIVÉS
// ─────────────────────────────────────────────────────────────────────────

/** Fil d'Ariane. Toujours émis, dérivé du chemin réel de la page. */
export function breadcrumb(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      item: it.url,
    })),
  }
}

/**
 * Compte les mots de n'importe quelle structure de sections.
 * Parcours défensif : additionne toute valeur string, quelle que soit
 * la forme du contenu. Sert à dériver wordCount, jamais à le coder en dur.
 */
export function countWords(value: unknown): number {
  if (typeof value === 'string') {
    return value.trim().split(/\s+/).filter(Boolean).length
  }
  if (Array.isArray(value)) {
    return value.reduce<number>((n, v) => n + countWords(v), 0)
  }
  if (value && typeof value === 'object') {
    return Object.values(value).reduce<number>((n, v) => n + countWords(v), 0)
  }
  return 0
}

// ─────────────────────────────────────────────────────────────────────────
// 5. BUILDERS PAR TYPE — adapter les noms de champs au modèle du site
// ─────────────────────────────────────────────────────────────────────────

type ArticleLike = {
  title: string
  excerpt: string
  date: string
  category?: string
  highlights?: string[]
  sections: unknown
}

/** Article / BlogPosting dérivé de la donnée. Auteur/éditeur par ref @id. */
export function articleSchema(a: ArticleLike, url: string, ogImage = `${SITE_URL}/og.png`) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: a.title,
    description: a.excerpt,
    url,
    datePublished: a.date,
    dateModified: a.date,
    articleSection: a.category,
    inLanguage: IDENTITY.language,
    isAccessibleForFree: true,
    wordCount: countWords(a.sections),
    keywords: a.highlights?.join(', '),
    image: ogImage,
    author: AUTHOR_REF,
    publisher: PUBLISHER_REF,
    isPartOf: WEBSITE_REF,
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
  }
}

/** FAQPage : émis SEULEMENT si un vrai bloc FAQ existe sur la page. */
export function faqSchema(items: { q: string; a: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map(({ q, a }) => ({
      '@type': 'Question',
      name: q,
      acceptedAnswer: { '@type': 'Answer', text: a },
    })),
  }
}

/** VideoObject : ID YouTube extrait par regex, thumbnail + embed déduits. */
export function videoSchema(
  video: { url: string; caption?: string },
  ctx: { title: string; excerpt: string; date: string },
) {
  const ytId =
    video.url.match(/(?:youtu\.be\/|v=|shorts\/|embed\/)([\w-]{11})/)?.[1] ?? null
  return {
    '@context': 'https://schema.org',
    '@type': 'VideoObject',
    name: video.caption ?? ctx.title,
    description: ctx.excerpt,
    uploadDate: ctx.date,
    thumbnailUrl: ytId ? `https://i.ytimg.com/vi/${ytId}/maxresdefault.jpg` : undefined,
    contentUrl: video.url,
    embedUrl: ytId ? `https://www.youtube-nocookie.com/embed/${ytId}` : video.url,
  }
}

/**
 * HowTo dérivé des sections : détecte un H2 dont le titre matche `predicate`,
 * collecte les H3 numérotés suivants + leur contenu en HowToStep.
 * Renvoie [] si aucune étape réelle (jamais de HowTo vide).
 *
 * Adapter la forme des sections au modèle du site. Le défaut reproduit le
 * heuristique organikk : H2 contenant "prompt".
 */
type Section =
  | { type: 'h2'; title: string }
  | { type: 'h3'; title: string; content?: string }
  | { type: 'p' | 'code'; content: string }
  | { type: 'ul' | 'ol'; content: string[] }
  | { type: string; [k: string]: unknown }

export function howToFromSections(
  sections: Section[],
  predicate: (h2Title: string) => boolean = (t) => /prompt/i.test(t),
) {
  const out: Record<string, unknown>[] = []
  for (let i = 0; i < sections.length; i++) {
    const s = sections[i]
    if (s.type !== 'h2' || !predicate((s as { title: string }).title)) continue
    const steps: { name: string; text: string }[] = []
    let j = i + 1
    while (j < sections.length) {
      const t = sections[j]
      if (t.type === 'h2') break
      if (t.type === 'h3' && /^\d+\.\s/.test((t as { title: string }).title)) {
        const stepName = (t as { title: string }).title.replace(/^\d+\.\s*/, '').trim()
        const parts: string[] = []
        const c = (t as { content?: string }).content
        if (c) parts.push(c)
        let k = j + 1
        while (k < sections.length) {
          const u = sections[k]
          if (u.type === 'p' || u.type === 'code') { parts.push((u as { content: string }).content); k++ }
          else if (u.type === 'ul' || u.type === 'ol') { parts.push((u as { content: string[] }).content.join('\n')); k++ }
          else break
        }
        if (parts.length) steps.push({ name: stepName, text: parts.join('\n\n') })
        j = k
      } else j++
    }
    if (steps.length) {
      out.push({
        '@context': 'https://schema.org',
        '@type': 'HowTo',
        name: (s as { title: string }).title,
        step: steps.map((st, idx) => ({
          '@type': 'HowToStep',
          position: idx + 1,
          name: st.name,
          text: st.text,
        })),
      })
      break // un seul HowTo par page
    }
  }
  return out
}

=====

## Note pour Tim (interne)

- **Pas de `sequencage-semaine-4.md`.** Seuls S2 et S3 existent. Ce doc place le skill en J1 S4 comme tu l'as demandé, mais le séquençage S4 complet n'existe pas encore. Quand tu le construiras : thème S4 = **automatisations + prospection** (source : [[session-2-redaction-resume-participants]] L271 "on bascule sur les automatisations et la prospection en S4"). Le skill données structurées rentre comme premier module "automatisation" (le balisage qui se génère depuis le contenu = une vraie automatisation), J1 cohérent. À intégrer dans le tableau S4 quand il sera fait.
- **Autres briques S4 repérées** (à caser dans le séquençage quand tu le fais) : démo plugin WordPress de Romain, système de prospection IA d'Anthony, automatisation revue de presse sur la thématique du client (cf. [[observations-whatsapp-bootcamp]] + transcript S2). La prospection n'est pas couverte par un skill existant : prévoir.
- **⚠️ Risque audience.** Le debrief S2 alerte : "bien cadrer pour qu'on ne perde pas la moitié du groupe en S4 sur Obsidian/technique" ([[session-2-redaction-debrief]] L234). Ce skill est technique (Next.js). J'ai ajouté dans la pédagogie une section "Site Next.js vs WordPress / no-code" qui rabat les 3 règles sur n'importe quel CMS et renvoie en MP les non-techniques. Beaucoup de participants sont sur WordPress (cf. Romain). À marteler au J1 : le code est optionnel, les 3 règles sont obligatoires pour tous.
- **Statut pack.** `seo-donnees-structurees` = HORS pack des 9, vraie nouvelle install (2 fichiers : SKILL.md + references/schema-reference.ts). Message WhatsApp week-end dédié comme pour `maillage-interne-gsc` en S3, sinon ça bloque au J1.
- **Source canonique.** Le skill dérive de `organikk-next/src/lib/schema.ts` (prod). Non modifié. Si tu fais évoluer le code Organikk, régénère ce bundle.
- **Normalisation.** Doc sans em-dashes (règle maison). Le bloc SKILL.md et le bloc `.ts` sont reproduits verbatim depuis `~/.claude/skills/seo-donnees-structurees/`.
