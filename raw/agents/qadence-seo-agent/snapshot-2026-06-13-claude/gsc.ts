// Wrapper GSC simplifié pour le Squad — réutilise la logique du seo-agent
// Gère : token refresh, cache 2h, validation du site GSC, calcul des dates

const GSC_API = 'https://searchconsole.googleapis.com'

export interface GSCQuery {
  type:        'queries' | 'pages' | 'queries_pages' | 'totals'
  startDate?:  string
  endDate?:    string
  rowLimit?:   number
}

export interface GSCContext {
  user_id:    string
  domain:     string
  gscSite?:   string | null
  supabase:   any
}

export interface GSCResult {
  site?:      string
  dateRange?: { start: string; end: string }
  type:       string
  totalRows?: number
  rows:       any[]
  clicks?:    number
  impressions?: number
  ctr?:       string
  position?:  string
  fromCache?: boolean
  error?:     string
  details?:   any
}

const dimensionMap: Record<string, string[]> = {
  queries:       ['query'],
  pages:         ['page'],
  queries_pages: ['query', 'page'],
  totals:        [],
}

export async function fetchGSC(args: GSCQuery, ctx: GSCContext): Promise<GSCResult> {
  const { user_id, domain, gscSite, supabase } = ctx

  // 1) Résolution robuste de la connexion + token.
  //    Les sessions anonymes fragmentent les connexions sur plusieurs user_id pour un même
  //    compte Google. On résout dans l'ordre : (user_id+site) → (user_id) → (site, autre session)
  //    → (domaine, autre session). L'API GSC vérifie de toute façon les droits réels du token,
  //    donc un token sans accès au site renverra 403 — pas de fuite.
  const SEL = 'access_token, refresh_token, token_expiry, gsc_site, user_id'
  const pick = async (builder: any) => {
    const { data } = await builder.not('access_token', 'is', null).order('token_expiry', { ascending: false }).limit(1)
    const c = Array.isArray(data) ? data[0] : data
    return c?.access_token ? c : null
  }
  let conn: any = null
  if (gscSite) conn = await pick(supabase.from('google_connections').select(SEL).eq('user_id', user_id).eq('gsc_site', gscSite))
  if (!conn)   conn = await pick(supabase.from('google_connections').select(SEL).eq('user_id', user_id))
  if (!conn && gscSite) conn = await pick(supabase.from('google_connections').select(SEL).eq('gsc_site', gscSite))
  if (!conn && domain) {
    const cd = domain.replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '')
    conn = await pick(supabase.from('google_connections').select(SEL).ilike('gsc_site', `%${cd}%`))
  }
  if (!conn?.access_token) return { type: args.type, rows: [], error: 'Google Search Console non connectée' }
  const connUserId = conn.user_id || user_id

  // 2) Cache check (TTL 2h)
  const cacheKey = `${user_id}|${conn.gsc_site}|${args.type}|${args.startDate||''}|${args.endDate||''}|${args.rowLimit||''}`
  try {
    const { data: cached } = await supabase
      .from('gsc_cache')
      .select('data, cached_at')
      .eq('cache_key', cacheKey)
      .maybeSingle()
    if (cached && (Date.now() - new Date(cached.cached_at).getTime()) / 60_000 < 120) {
      return { ...cached.data, fromCache: true }
    }
  } catch {}

  // 3) Refresh token si expiré
  let accessToken = conn.access_token
  if (new Date(conn.token_expiry) <= new Date()) {
    const r = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type:    'refresh_token',
        refresh_token: conn.refresh_token,
        client_id:     Deno.env.get('GOOGLE_CLIENT_ID') || '',
        client_secret: Deno.env.get('GOOGLE_CLIENT_SECRET') || '',
      }),
    })
    const rd = await r.json()
    if (rd.access_token) {
      accessToken = rd.access_token
      let upd = supabase.from('google_connections').update({
        access_token: accessToken,
        token_expiry: new Date(Date.now() + rd.expires_in * 1000).toISOString(),
      }).eq('user_id', connUserId)
      if (conn.gsc_site) upd = upd.eq('gsc_site', conn.gsc_site)
      await upd
    }
  }

  // 4) Calcul des dates (clamp à J-3 max, GSC delay)
  const maxEnd = new Date(Date.now() - 3 * 86400000).toISOString().split('T')[0]
  const reqEnd = args.endDate || maxEnd
  const end    = reqEnd > maxEnd ? maxEnd : reqEnd

  let start = args.startDate || new Date(new Date(end).getTime() - 28 * 86400000).toISOString().split('T')[0]
  if (args.startDate && args.endDate) {
    const dur = Math.round((new Date(args.endDate).getTime() - new Date(args.startDate).getTime()) / 86400000)
    if (dur > 0) start = new Date(new Date(end).getTime() - dur * 86400000).toISOString().split('T')[0]
  }

  // 5) Validation du site GSC + auto-correction
  let targetSite = gscSite || conn.gsc_site
  try {
    const sr = await fetch(`${GSC_API}/webmasters/v3/sites`, {
      headers: { Authorization: `Bearer ${accessToken}` }
    })
    if (sr.ok) {
      const sd = await sr.json()
      const verified: string[] = (sd.siteEntry || [])
        .filter((s: any) => s.permissionLevel !== 'siteUnverifiedUser')
        .map((s: any) => s.siteUrl as string)
      if (verified.length > 0 && !verified.find(s => s === targetSite) && domain) {
        const cd = domain.replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '')
        const best = verified.find(s => {
          const c = s.replace('sc-domain:', '').replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '')
          return c === cd || c.endsWith('.' + cd) || cd.endsWith('.' + c)
        })
        if (best) targetSite = best
      }
    }
  } catch {}

  // 6) Body de la requête
  const body = args.type === 'totals'
    ? { startDate: start, endDate: end, dataState: 'final' }
    : {
        startDate: start, endDate: end,
        dimensions: dimensionMap[args.type] || ['query'],
        rowLimit:   args.rowLimit || 500,
        orderBy:    [{ fieldName: 'clicks', sortOrder: 'DESCENDING' }],
        dataState:  'final',
      }

  const resp = await fetch(
    `${GSC_API}/webmasters/v3/sites/${encodeURIComponent(targetSite)}/searchAnalytics/query`,
    {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
      body:    JSON.stringify(body),
    }
  )
  if (!resp.ok) {
    return { type: args.type, rows: [], error: `GSC API ${resp.status}`, details: await resp.json().catch(() => null) }
  }

  const gsc = await resp.json()

  // 7) Format de retour
  let result: GSCResult
  if (args.type === 'totals') {
    const r0 = (gsc.rows || [])[0] || {}
    result = {
      site: targetSite, dateRange: { start, end }, type: 'totals',
      clicks:      r0.clicks      || 0,
      impressions: r0.impressions || 0,
      ctr:         ((r0.ctr || 0) * 100).toFixed(1) + '%',
      position:    (r0.position || 0).toFixed(1),
      totalRows: 1, rows: [],
    }
  } else {
    const dims = dimensionMap[args.type] || ['query']
    const rows = (gsc.rows || []).map((row: any) => {
      const o: any = {}
      dims.forEach((d, i) => { o[d] = row.keys[i] })
      o.clicks      = row.clicks      || 0
      o.impressions = row.impressions || 0
      o.ctr         = ((row.ctr || 0) * 100).toFixed(1) + '%'
      o.position    = (row.position || 0).toFixed(1)
      return o
    })
    result = { site: targetSite, dateRange: { start, end }, type: args.type, totalRows: rows.length, rows }
  }

  // 8) Écriture cache (best-effort)
  try {
    await supabase.from('gsc_cache').upsert(
      { cache_key: cacheKey, data: result, cached_at: new Date().toISOString(), user_id },
      { onConflict: 'cache_key' }
    )
  } catch {}

  return result
}

// Helper pour vérifier si GSC est connectée pour un user/domain
export async function isGSCConnected(supabase: any, user_id: string): Promise<boolean> {
  const { data } = await supabase
    .from('google_connections')
    .select('id')
    .eq('user_id', user_id)
    .not('access_token', 'is', null)
    .limit(1)
  return !!(data && data.length > 0)
}
