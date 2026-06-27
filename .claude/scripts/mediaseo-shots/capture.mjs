#!/usr/bin/env node
/**
 * MediaSEO — Service de capture d'écran (preuve visuelle authentique).
 *
 * PRINCIPE NON NÉGOCIABLE : ce service NE GÉNÈRE JAMAIS d'image. Il capture la
 * vraie page (Playwright headless Chromium) ou retourne `status: "unavailable"`.
 * Il ne reconstitue rien, n'invente aucun score/commentaire/vue.
 *
 * Le LLM fournit seulement : { title, source, url, highlight?, selector? }.
 * Le service ouvre la page, attend, ferme les popups de consentement, détecte
 * les blocages/paywalls (Reddit anti-bot, login X, paywall) et, si tout va bien,
 * capture un PNG 1200px de large.
 *
 * Sources publiques (Google Search Central/Developers, OpenAI, Anthropic,
 * Cloudflare, GitHub, Hacker News, docs officielles) = fiables.
 * Reddit & X = bloqués/login par défaut → "Capture indisponible" (constaté).
 * Bloomberg/Reuters = paywall → "Capture indisponible".
 *
 * Usage :
 *   node capture.mjs --url "https://..." --title "..." [--out DIR] [--full-page]
 *   node capture.mjs --in items.json --out DIR        # items = [{title,source,url,highlight,selector}]
 *   echo '[{...}]' | node capture.mjs --out DIR        # JSON sur stdin
 *
 * Sortie : PNG dans OUT + manifest.json + manifest imprimé sur stdout.
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const BLOCK_MARKERS = [
  'whoa there, pardner',
  'blocked due to a network policy',
  'log in to continue',
  'sign in to x',
  'sign up to continue',
  'enable javascript and cookies to continue',
  'are you a robot',
  'verify you are human',
  'subscribe to read',
  'subscribe to continue',
  'this content is for subscribers',
];

// Interstitiels anti-bot JS (Cloudflare, wp.com…) : page de transition, PAS le contenu.
// On les attrape pour ne JAMAIS sauvegarder un challenge comme s'il s'agissait de la source.
const INTERSTITIAL_MARKERS = [
  'checking your browser',
  'this will only take a few seconds',
  'just a moment',
  'secured by',
  'needs to review the security of your connection',
  'verifying you are human',
  'please wait while we verify',
];

// Hôtes connus pour bloquer / exiger un login (on tente, mais on s'attend à un échec)
const RISKY_HOSTS = ['reddit.com', 'x.com', 'twitter.com', 'bloomberg.com', 'reuters.com', 'wsj.com'];

const CONSENT_SELECTORS = [
  '#onetrust-accept-btn-handler',
  'button:has-text("Accept all")',
  'button:has-text("Accept All")',
  'button:has-text("I agree")',
  'button:has-text("Tout accepter")',
  'button:has-text("J\'accepte")',
  'button:has-text("Agree")',
  'button:has-text("Accept")',
  '[aria-label="Accept all"]',
];

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
  '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36';

function args() {
  const a = process.argv.slice(2);
  const o = { out: 'shots', fullPage: false };
  for (let i = 0; i < a.length; i++) {
    if (a[i] === '--url') o.url = a[++i];
    else if (a[i] === '--title') o.title = a[++i];
    else if (a[i] === '--source') o.source = a[++i];
    else if (a[i] === '--in') o.in = a[++i];
    else if (a[i] === '--out') o.out = a[++i];
    else if (a[i] === '--full-page') o.fullPage = true;
  }
  return o;
}

function slugify(s) {
  return (s || 'shot').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60) || 'shot';
}

async function readItems(o) {
  if (o.url) return [{ title: o.title, source: o.source, url: o.url }];
  if (o.in) return JSON.parse(fs.readFileSync(o.in, 'utf-8'));
  const stdin = fs.readFileSync(0, 'utf-8').trim();
  if (stdin) return JSON.parse(stdin);
  throw new Error('Aucune entrée : --url, --in <file> ou JSON sur stdin.');
}

async function captureOne(ctx, item, outDir, fullPage) {
  const { title, url, source, selector } = item;
  let host = '';
  try { host = new URL(url).hostname.replace(/^www\./, ''); } catch { /* */ }
  const risky = RISKY_HOSTS.some((h) => host.endsWith(h));
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(4000);

    const readBody = async () => (await page.evaluate(
      () => (document.body && document.body.innerText) || '')).slice(0, 5000).toLowerCase();

    // Interstitiel JS (Cloudflare/wp.com) : on laisse une chance au challenge de se résoudre.
    let bodyText = await readBody();
    if (INTERSTITIAL_MARKERS.some((m) => bodyText.includes(m))) {
      await page.waitForTimeout(8000);
      bodyText = await readBody();
    }

    for (const sel of CONSENT_SELECTORS) {
      try {
        const b = page.locator(sel).first();
        if (await b.isVisible({ timeout: 400 })) { await b.click({ timeout: 1000 }); await page.waitForTimeout(400); }
      } catch { /* popup absent */ }
    }
    bodyText = await readBody();

    const marker = [...BLOCK_MARKERS, ...INTERSTITIAL_MARKERS].find((m) => bodyText.includes(m));
    if (marker) {
      return { title, source, url, status: 'unavailable', reason: `blocage/challenge/paywall ("${marker}")` };
    }
    if (bodyText.length < 40 && risky) {
      return { title, source, url, status: 'unavailable', reason: 'page vide / probable login requis' };
    }

    const file = path.join(outDir, `${slugify(title || host)}.png`);
    const target = selector ? page.locator(selector).first() : page;
    await target.screenshot({ path: file, fullPage: selector ? false : fullPage });
    return { title, source, url, status: 'ok', file, riskyHostTried: risky || undefined };
  } catch (e) {
    return { title, source, url, status: 'unavailable', reason: String(e.message || e).slice(0, 160) };
  } finally {
    await page.close();
  }
}

async function main() {
  const o = args();
  const items = await readItems(o);
  fs.mkdirSync(o.out, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    userAgent: UA,
    viewport: { width: 1200, height: 1600 },
    deviceScaleFactor: 1,
    locale: 'fr-FR',
  });
  const manifest = [];
  for (const item of items) {
    const r = await captureOne(ctx, item, o.out, o.fullPage);
    manifest.push(r);
    process.stderr.write(`${r.status === 'ok' ? '✅' : '⛔'} ${r.status.padEnd(11)} ${item.url}` +
      (r.reason ? `  (${r.reason})` : '') + '\n');
  }
  await browser.close();

  fs.writeFileSync(path.join(o.out, 'manifest.json'), JSON.stringify(manifest, null, 2));
  process.stdout.write(JSON.stringify(manifest, null, 2) + '\n');
}

main().catch((e) => { console.error('FATAL', e); process.exit(1); });
