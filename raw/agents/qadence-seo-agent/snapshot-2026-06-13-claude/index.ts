// seo-agent-claude — cœur conversationnel de qadence SOUS CLAUDE = le cerveau SEO de Tim.
// Croise sa DOCTRINE (skills) · son VAULT Obsidian (search_kb) · la DATA réelle (GSC).
// STREAMING SSE au contrat du front : data: {thinking|text|memory_updated|done} puis [DONE].
//
// Body: { message, user_id, domain, gscSite?, history? }

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import { fetchGSC } from './gsc.ts'
import { runAgentLoopStream, type ClaudeTool } from './claude.ts'

const cors = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
}

const TOOLS: ClaudeTool[] = [
  {
    name: 'search_kb',
    description:
      "Interroge le SECOND CERVEAU de Tim (vault Obsidian : doctrine, stratégies, cas clients, décisions). " +
      "À utiliser dès que la question touche méthode/stratégie/position de doctrine/cas vécu.",
    input_schema: { type: 'object', properties: { query: { type: 'string' } }, required: ['query'] },
  },
  {
    name: 'gsc_query',
    description:
      "Données RÉELLES Search Console. type='totals'|'pages'|'queries'. Dates YYYY-MM-DD. Aucun chiffre site sans cet outil. Période fraîche = J-32→J-4.",
    input_schema: {
      type: 'object',
      properties: { type: { type: 'string', enum: ['totals', 'pages', 'queries'] }, startDate: { type: 'string' }, endDate: { type: 'string' }, rowLimit: { type: 'number' } },
      required: ['type', 'startDate', 'endDate'],
    },
  },
  {
    name: 'load_skill',
    description:
      "Charge un SKILL de Tim (méthode pas-à-pas). slugs: quick_win, cannibalisation, brief_contenu, maillage_interne, " +
      "mots_cles_decisionnels, objections_clients, score_geo, score_semantique, audit_gsc, content_gaps, strategie_seo.",
    input_schema: { type: 'object', properties: { slug: { type: 'string' } }, required: ['slug'] },
  },
  {
    name: 'update_memory',
    description: "Mémorise un fait durable sur le projet (secteur, objectif, contraintes, décisions). key court, value concis.",
    input_schema: { type: 'object', properties: { key: { type: 'string' }, value: { type: 'string' } }, required: ['key', 'value'] },
  },
]

function systemPrompt(voice: string, domain: string, today: string, memory: string): string {
  return [
    "Tu es l'agent SEO/GEO de Timothée Boussardon (qadence). Tu N'ES PAS un assistant générique : tu ES son système.",
    'Tu raisonnes et réponds avec SA doctrine et SA voix.',
    '',
    '## Méthode (non négociable)',
    "- Question méthode/stratégie/doctrine/cas vécu → `search_kb` pour t'ancrer dans SON vault (cite sa pensée, pas du générique).",
    '- Tâche SEO précise (quick win, maillage, brief, cannibalisation…) → `load_skill` AVANT, puis suis sa méthode.',
    '- Tout chiffre du site vient de `gsc_query` (réel), jamais inventé.',
    '- Fait durable appris sur le projet → `update_memory`.',
    '- Doctrine > générique : conversion > trafic, mots-clés décisionnels > informationnel, intention business, GEO = Generative Engine Optimization.',
    '',
    `## Contexte\nSite : ${domain || '(non précisé)'} · Aujourd'hui : ${today}`,
    memory ? `## Mémoire projet\n${memory}` : '',
    '',
    '## Voix de Tim (applique-la à TOUTE réponse)',
    voice || '(tutoiement, direct, pédagogique, anti-IA writing, positions tranchées)',
  ].filter(Boolean).join('\n')
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors })

  let body: any
  try { body = await req.json() } catch { return json({ error: 'payload invalide' }, 400) }
  const { message, user_id, domain, gscSite, history } = body
  if (!message || !user_id) return json({ error: 'message et user_id requis' }, 400)

  const apiKey = Deno.env.get('ANTHROPIC_API_KEY')
  if (!apiKey) return json({ error: 'ANTHROPIC_API_KEY manquante' }, 500)
  const supabase = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!)
  const KB_URL = Deno.env.get('KB_SEARCH_URL'), KB_KEY = Deno.env.get('KB_SEARCH_KEY')
  const encoder = new TextEncoder()

  const stream = new ReadableStream({
    async start(controller) {
      const emit = (ev: Record<string, unknown>) => controller.enqueue(encoder.encode(`data: ${JSON.stringify(ev)}\n\n`))
      try {
        const { data: voiceRow } = await supabase.from('skills').select('prompt').eq('name', 'ton_de_voix_tim').maybeSingle()
        const { data: mem } = await supabase.from('project_memory').select('key,value').eq('user_id', user_id).eq('domain', domain ?? '')
        const memStr = (mem ?? []).map((m: any) => `${m.key}: ${typeof m.value === 'string' ? m.value : JSON.stringify(m.value)}`).join('\n').slice(0, 3000)
        const today = new Date().toISOString().split('T')[0]
        const histTxt = Array.isArray(history) && history.length
          ? 'Historique récent:\n' + history.slice(-6).map((h: any) => `${h.role}: ${h.content}`).join('\n') + '\n\n'
          : ''

        await runAgentLoopStream({
          apiKey,
          system: systemPrompt(voiceRow?.prompt ?? '', domain ?? '', today, memStr),
          userMessage: histTxt + 'Question: ' + message,
          tools: TOOLS,
          emit,
          handlers: {
            search_kb: async (input) => {
              if (!KB_URL || !KB_KEY) return { error: 'vault non configuré' }
              const r = await fetch(KB_URL, { method: 'POST', headers: { apikey: KB_KEY, Authorization: `Bearer ${KB_KEY}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ query: input.query, match_count: 6 }) })
              return await r.json()
            },
            gsc_query: async (input) =>
              await fetchGSC({ type: input.type, startDate: input.startDate, endDate: input.endDate, rowLimit: Math.min(input.rowLimit ?? 250, 500) }, { user_id, domain, gscSite: gscSite ?? null, supabase }),
            load_skill: async (input) => {
              const { data } = await supabase.from('skills').select('prompt').eq('name', input.slug).maybeSingle()
              return data?.prompt ? { slug: input.slug, prompt: data.prompt } : { error: `skill ${input.slug} introuvable` }
            },
            update_memory: async (input) => {
              await supabase.from('project_memory').upsert({ user_id, domain: domain ?? '', key: String(input.key).slice(0, 80), value: String(input.value).slice(0, 2000) }, { onConflict: 'user_id,domain,key' })
              return { ok: true }
            },
          },
          maxRounds: 8,
          maxTokens: 4096,
        })
        emit({ done: true })
        controller.enqueue(encoder.encode('data: [DONE]\n\n'))
      } catch (e) {
        emit({ text: `\n\n⚠️ Erreur : ${e instanceof Error ? e.message : String(e)}` })
        emit({ done: true })
      } finally {
        controller.close()
      }
    },
  })

  return new Response(stream, { headers: { ...cors, 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', Connection: 'keep-alive' } })
})

function json(b: unknown, s = 200) {
  return new Response(JSON.stringify(b), { status: s, headers: { ...cors, 'Content-Type': 'application/json' } })
}
