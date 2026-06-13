// Client Claude (API Anthropic Messages) + boucle tool-use bornée, pour Deno/Edge.
// Cœur réutilisable de la nouvelle couche d'agents qadence (remplace l'appel Gemini
// « one-shot » par un vrai agent : Claude décide quels outils appeler, itère, conclut).

const ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'

export type ClaudeModel = 'claude-sonnet-4-6' | 'claude-opus-4-8' | 'claude-haiku-4-5-20251001'

export interface ClaudeTool {
  name: string
  description: string
  input_schema: Record<string, unknown>
}

// Implémentation d'un outil : reçoit l'input validé par Claude, renvoie un résultat sérialisable.
export type ToolHandler = (input: any) => Promise<unknown>

export interface AgentLoopOpts {
  apiKey: string
  model?: ClaudeModel
  system: string
  userMessage: string
  tools: ClaudeTool[]
  handlers: Record<string, ToolHandler>
  maxRounds?: number // garde-fou anti-boucle + limite de temps edge (~150s)
  maxTokens?: number
  timeoutMs?: number
  onStep?: (msg: string) => void // trace (UI/log)
}

export interface AgentLoopResult {
  text: string // réponse finale de Claude (pas de tool_use)
  rounds: number
  toolCalls: { name: string; input: any }[]
  stopReason?: string
  usage?: any
}

async function callMessages(apiKey: string, body: Record<string, unknown>, timeoutMs: number) {
  const ctrl = new AbortController()
  const timer = setTimeout(() => ctrl.abort(), timeoutMs)
  try {
    const r = await fetch(ANTHROPIC_URL, {
      method: 'POST',
      headers: {
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json',
      },
      signal: ctrl.signal,
      body: JSON.stringify(body),
    })
    if (!r.ok) {
      const t = await r.text()
      throw new Error(`Anthropic ${r.status}: ${t.slice(0, 400)}`)
    }
    return await r.json()
  } finally {
    clearTimeout(timer)
  }
}

// Boucle agentique : Claude raisonne, appelle des outils (tool_use), reçoit les
// résultats (tool_result), recommence — jusqu'à une réponse texte finale ou maxRounds.
export async function runAgentLoop(opts: AgentLoopOpts): Promise<AgentLoopResult> {
  const model = opts.model ?? 'claude-sonnet-4-6'
  const maxRounds = opts.maxRounds ?? 8
  const maxTokens = opts.maxTokens ?? 8192
  const timeoutMs = opts.timeoutMs ?? 60_000

  const messages: any[] = [{ role: 'user', content: opts.userMessage }]
  const toolCalls: { name: string; input: any }[] = []
  let usage: any

  for (let round = 1; round <= maxRounds; round++) {
    const data = await callMessages(
      opts.apiKey,
      { model, max_tokens: maxTokens, system: opts.system, messages, tools: opts.tools },
      timeoutMs
    )
    usage = data.usage
    const content: any[] = data.content ?? []
    const stop = data.stop_reason

    // Réponse finale : pas d'appel d'outil → on agrège le texte et on sort.
    if (stop !== 'tool_use') {
      const text = content.filter((b) => b.type === 'text').map((b) => b.text).join('\n').trim()
      return { text, rounds: round, toolCalls, stopReason: stop, usage }
    }

    // Sinon : exécuter chaque tool_use, renvoyer les tool_result.
    messages.push({ role: 'assistant', content })
    const toolResults: any[] = []
    for (const block of content) {
      if (block.type !== 'tool_use') continue
      toolCalls.push({ name: block.name, input: block.input })
      opts.onStep?.(`outil: ${block.name}`)
      let resultText: string
      try {
        const handler = opts.handlers[block.name]
        if (!handler) throw new Error(`outil inconnu: ${block.name}`)
        const out = await handler(block.input)
        resultText = typeof out === 'string' ? out : JSON.stringify(out)
        if (resultText.length > 60_000) resultText = resultText.slice(0, 60_000) + '…[tronqué]'
      } catch (e) {
        resultText = `ERREUR outil: ${e instanceof Error ? e.message : String(e)}`
      }
      toolResults.push({ type: 'tool_result', tool_use_id: block.id, content: resultText })
    }
    messages.push({ role: 'user', content: toolResults })
  }

  // maxRounds atteint sans conclusion : on force une réponse finale sans outils.
  const data = await callMessages(
    opts.apiKey,
    {
      model,
      max_tokens: maxTokens,
      system: opts.system + '\n\nTu as atteint la limite d\'outils. Conclus MAINTENANT avec ce que tu as.',
      messages,
    },
    timeoutMs
  )
  const text = (data.content ?? []).filter((b: any) => b.type === 'text').map((b: any) => b.text).join('\n').trim()
  return { text, rounds: maxRounds, toolCalls, stopReason: 'max_rounds', usage: data.usage }
}

// ─── Variante STREAMING : émet {thinking} pendant les outils et {text} en direct ───
// (pour le contrat SSE du front qadence). Réutilise system/tools/handlers de AgentLoopOpts.
function thinkMsg(tool: string): string {
  return ({
    search_kb: 'Je consulte le vault de Tim…',
    gsc_query: 'Je récupère la Search Console…',
    load_skill: 'Je charge la méthode de Tim…',
    update_memory: 'Je note ça en mémoire…',
  } as Record<string, string>)[tool] ?? `Outil : ${tool}`
}

export async function runAgentLoopStream(
  opts: AgentLoopOpts & { emit: (ev: { thinking?: string; text?: string; memory_updated?: boolean }) => void }
): Promise<{ rounds: number; toolCalls: { name: string; input: any }[] }> {
  const model = opts.model ?? 'claude-sonnet-4-6'
  const maxRounds = opts.maxRounds ?? 8
  const maxTokens = opts.maxTokens ?? 4096
  const messages: any[] = [{ role: 'user', content: opts.userMessage }]
  const toolCalls: { name: string; input: any }[] = []

  for (let round = 1; round <= maxRounds; round++) {
    const res = await fetch(ANTHROPIC_URL, {
      method: 'POST',
      headers: { 'x-api-key': opts.apiKey, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
      body: JSON.stringify({ model, max_tokens: maxTokens, system: opts.system, messages, tools: opts.tools, stream: true }),
    })
    if (!res.ok || !res.body) throw new Error(`Anthropic ${res.status}: ${(await res.text().catch(() => '')).slice(0, 300)}`)

    const reader = res.body.getReader()
    const dec = new TextDecoder()
    let buf = ''
    const blocks: any[] = []           // contenu de la réponse assistant (text + tool_use), dans l'ordre
    let stopReason = ''
    let curToolJson = ''               // accumulateur input_json du tool_use courant
    let curIdx = -1

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buf += dec.decode(value, { stream: true })
      let nl: number
      while ((nl = buf.indexOf('\n')) >= 0) {
        const line = buf.slice(0, nl).trim()
        buf = buf.slice(nl + 1)
        if (!line.startsWith('data:')) continue
        let ev: any
        try { ev = JSON.parse(line.slice(5).trim()) } catch { continue }
        if (ev.type === 'content_block_start') {
          curIdx = ev.index
          if (ev.content_block?.type === 'tool_use') { blocks[curIdx] = { type: 'tool_use', id: ev.content_block.id, name: ev.content_block.name, input: {} }; curToolJson = '' }
          else { blocks[curIdx] = { type: 'text', text: '' } }
        } else if (ev.type === 'content_block_delta') {
          if (ev.delta?.type === 'text_delta') { opts.emit({ text: ev.delta.text }); if (blocks[ev.index]) blocks[ev.index].text += ev.delta.text }
          else if (ev.delta?.type === 'input_json_delta') { curToolJson += ev.delta.partial_json }
        } else if (ev.type === 'content_block_stop') {
          const b = blocks[ev.index]
          if (b?.type === 'tool_use') { try { b.input = curToolJson ? JSON.parse(curToolJson) : {} } catch { b.input = {} } }
        } else if (ev.type === 'message_delta') {
          if (ev.delta?.stop_reason) stopReason = ev.delta.stop_reason
        }
      }
    }

    const content = blocks.filter(Boolean)
    if (stopReason !== 'tool_use') return { rounds: round, toolCalls }

    messages.push({ role: 'assistant', content })
    const toolResults: any[] = []
    for (const b of content) {
      if (b.type !== 'tool_use') continue
      toolCalls.push({ name: b.name, input: b.input })
      opts.emit({ thinking: thinkMsg(b.name) })
      let resultText: string
      try {
        const out = await opts.handlers[b.name](b.input)
        if (b.name === 'update_memory') opts.emit({ memory_updated: true })
        resultText = typeof out === 'string' ? out : JSON.stringify(out)
        if (resultText.length > 60_000) resultText = resultText.slice(0, 60_000) + '…[tronqué]'
      } catch (e) {
        resultText = `ERREUR outil: ${e instanceof Error ? e.message : String(e)}`
      }
      toolResults.push({ type: 'tool_result', tool_use_id: b.id, content: resultText })
    }
    messages.push({ role: 'user', content: toolResults })
  }
  return { rounds: maxRounds, toolCalls }
}
