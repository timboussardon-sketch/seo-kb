#!/usr/bin/env python3
"""
MediaSEO — Veille pondérée.

Agrège un VIVIER multi-univers (Reddit, Hacker News, flux RSS officiels/études)
pour la revue quotidienne /MediaSEO. Le but est de SORTIR DE LA BULLE SEO :
on part de l'écosystème, on pré-trie par traction + fraîcheur, et le modèle
applique ensuite le filtre « impact Search ? » et le scoring éditorial /70.

Ce script NE FAIT PAS le scoring éditorial /70 (Nouveauté/Impact/Surprise/…),
qui demande le jugement du modèle. Il ne fait que collecter et pré-trier.

Sources prouvées : Reddit (flux .rss, le .json est bloqué en 403) + HN Algolia API.
Les flux RSS officiels/études sont best-effort : un flux qui échoue est ignoré.

Usage :
    python3 mediaseo-veille.py                 # écrit /tmp/mediaseo-vivier-<date>.md
    python3 mediaseo-veille.py --out PATH       # fichier de sortie
    python3 mediaseo-veille.py --json           # sortie JSON en plus du markdown
    python3 mediaseo-veille.py --days 30         # fenêtre de fraîcheur (défaut 120 = 4 mois)
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from xml.etree import ElementTree as ET

# UA navigateur : Reddit et certains CDN (Cloudflare) bloquent les UA "bot"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 MediaSEO/1.0")
TIMEOUT = 20

# --- Univers & pondération (reflète la charte MODELE.md ; SEO media = vérif only) ---
UNIVERSE_WEIGHT = {
    "google_openai": 30,   # officiel / produit / API
    "etudes": 20,          # Ahrefs, Adobe, Shopify, Cloudflare, Similarweb…
    "reddit_hn": 20,       # conversations
    "dev": 10,             # GitHub, Chromium
    "seo_media": 10,       # SEJ/SER/PPC Land — VÉRIFICATION seulement
    "signaux_faibles": 10, # brevets, docs, presse tech
}

# Subreddits -> univers (SEO core + écosystème pour casser la bulle)
REDDIT_SUBS = {
    "SEO": "reddit_hn", "bigseo": "reddit_hn", "TechSEO": "reddit_hn", "juststart": "reddit_hn",
    "ecommerce": "reddit_hn", "shopify": "etudes", "OpenAI": "reddit_hn",
    "artificial": "reddit_hn", "MachineLearning": "dev", "webdev": "dev",
    "SaaS": "reddit_hn", "Entrepreneur": "reddit_hn",
}

HN_QUERIES = ["AI search", "Google search", "SEO", "OpenAI", "Shopify",
              "web crawler", "Perplexity", "Anthropic", "Google AI"]
HN_MIN_POINTS = 100

# Flux RSS officiels / études / presse tech (best-effort : un flux qui échoue est ignoré)
RSS_FEEDS = {
    "https://developers.google.com/search/blog/feed.xml": "google_openai",
    "https://blog.google/products/search/rss/": "google_openai",
    "https://blog.google/technology/ai/rss/": "google_openai",
    "https://openai.com/blog/rss.xml": "google_openai",
    "https://ahrefs.com/blog/feed/": "etudes",
    "https://blog.cloudflare.com/rss/": "etudes",
    "https://arstechnica.com/ai/feed/": "signaux_faibles",
    "https://www.theverge.com/rss/index.xml": "signaux_faibles",
    "https://www.searchenginejournal.com/feed/": "seo_media",
}


def fetch(url, retries=2, backoff=6):
    """GET avec UA navigateur + retry/backoff sur 429/403 (Reddit rate-limite les bursts)."""
    last = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 403) and attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            raise
        except Exception as e:  # noqa: BLE001
            last = e
            if attempt < retries:
                time.sleep(backoff)
                continue
            raise
    raise last


def norm_title(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", (t or "").lower())).strip()


def parse_feed(raw):
    """Parse Atom (<entry>) ou RSS (<item>) -> liste de (title, link, date_str)."""
    out = []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return out

    def localtag(el):
        return el.tag.split("}")[-1]

    # Atom
    entries = [e for e in root.iter() if localtag(e) == "entry"]
    if entries:
        for e in entries:
            title = link = date = ""
            for c in e:
                lt = localtag(c)
                if lt == "title":
                    title = (c.text or "").strip()
                elif lt == "link":
                    link = c.get("href") or link
                elif lt in ("updated", "published"):
                    date = (c.text or "")[:10]
            out.append((title, link, date))
        return out
    # RSS
    items = [e for e in root.iter() if localtag(e) == "item"]
    for e in items:
        title = link = date = ""
        for c in e:
            lt = localtag(c)
            if lt == "title":
                title = (c.text or "").strip()
            elif lt == "link":
                link = (c.text or "").strip() or link
            elif lt in ("pubDate", "date"):
                date = (c.text or "").strip()
        out.append((title, link, date))
    return out


def in_window(date_str, cutoff):
    """True si pas de date OU date >= cutoff (ISO ou RFC822)."""
    if not date_str:
        return True
    for fmt in ("%Y-%m-%d", "%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
        try:
            d = dt.datetime.strptime(date_str.strip()[:31], fmt).date()
            return d >= cutoff
        except ValueError:
            continue
    return True  # date illisible -> on garde, le modèle tranchera


def collect_reddit(max_per_sub, cutoff, log):
    cands = []
    for i, (sub, universe) in enumerate(REDDIT_SUBS.items()):
        if i:
            time.sleep(4)  # Reddit rate-limite les bursts (429) ; pause obligatoire
        url = f"https://www.reddit.com/r/{sub}/top/.rss?t=week&limit={max_per_sub}"
        try:
            raw = fetch(url)
        except Exception as e:  # noqa: BLE001
            log.append(f"  reddit r/{sub}: ERREUR {e}")
            continue
        entries = parse_feed(raw)  # Atom Reddit : le titre du flux est hors <entry>, on garde tout
        kept = 0
        for rank, (title, link, date) in enumerate(entries):
            if not title or not link:
                continue
            if not in_window(date, cutoff):
                continue
            traction = max(5, 60 - rank * 3)  # position dans le top/week = proxy
            cands.append({
                "universe": universe, "source": f"r/{sub}", "title": title,
                "url": link, "date": date, "traction": traction,
            })
            kept += 1
        log.append(f"  reddit r/{sub}: {kept} candidats")
    return cands


def collect_hn(cutoff, log):
    cands = []
    for i, q in enumerate(HN_QUERIES):
        if i:
            time.sleep(0.5)
        # filtrage points côté client (le numericFilters Algolia renvoie parfois un 400)
        params = urllib.parse.urlencode({"query": q, "tags": "story", "hitsPerPage": 20})
        url = f"https://hn.algolia.com/api/v1/search?{params}"
        try:
            data = json.loads(fetch(url))
        except Exception as e:  # noqa: BLE001
            log.append(f"  hn '{q}': ERREUR {e}")
            continue
        kept = 0
        for h in data.get("hits", []):
            title = h.get("title") or h.get("story_title")
            link = h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
            if not title:
                continue
            pts = h.get("points") or 0
            if pts < HN_MIN_POINTS:
                continue
            date = (h.get("created_at") or "")[:10]
            if not in_window(date, cutoff):
                continue
            traction = min(100, 30 + pts // 10)
            cands.append({
                "universe": "reddit_hn", "source": f"HN ({q})", "title": title,
                "url": link, "date": date, "traction": traction,
                "points": pts, "comments": h.get("num_comments"),
            })
            kept += 1
        log.append(f"  hn '{q}': {kept} candidats")
    return cands


def collect_rss(cutoff, log):
    cands = []
    for url, universe in RSS_FEEDS.items():
        try:
            raw = fetch(url)
        except Exception as e:  # noqa: BLE001
            log.append(f"  rss {url}: ERREUR {e}")
            continue
        entries = parse_feed(raw)
        kept = 0
        for rank, (title, link, date) in enumerate(entries[:12]):
            if not title or not link:
                continue
            if not in_window(date, cutoff):
                continue
            w = UNIVERSE_WEIGHT.get(universe, 10)
            traction = max(10, w + 30 - rank * 2)
            cands.append({
                "universe": universe, "source": url.split("/")[2], "title": title,
                "url": link, "date": date, "traction": traction,
            })
            kept += 1
        log.append(f"  rss {url.split('/')[2]}: {kept} candidats")
    return cands


def dedupe(cands):
    seen_url, seen_title, out = set(), set(), []
    for c in sorted(cands, key=lambda x: -x["traction"]):
        u = c["url"].split("?")[0].rstrip("/")
        nt = norm_title(c["title"])
        if u in seen_url or (nt and nt in seen_title):
            continue
        seen_url.add(u)
        seen_title.add(nt)
        out.append(c)
    return out


UNIVERSE_LABEL = {
    "google_openai": "🏛️  Google / OpenAI / Anthropic (officiel, produit)",
    "etudes": "📊 Études (Ahrefs, Adobe, Shopify, Cloudflare…)",
    "reddit_hn": "💬 Reddit / Hacker News",
    "dev": "🛠️  Développeurs (GitHub, Chromium, ML)",
    "seo_media": "📰 SEO media (VÉRIFICATION seulement)",
    "signaux_faibles": "🔍 Signaux faibles / presse tech",
}


def render_markdown(cands, today, days):
    lines = [
        f"# MediaSEO — Vivier de veille — {today}",
        "",
        f"*{len(cands)} candidats, fenêtre {days} jours. Pré-tri par traction.*",
        "",
        "**Rappel modèle :** ce vivier n'est PAS filtré pour l'impact Search ni scoré /70.",
        "Pour chaque candidat : (1) impact Search ? sinon jette ; (2) score /70 (seuil 50) ;",
        "(3) angle ; (4) relie. SEO media = vérification, jamais point de départ.",
        "",
        "## 🔝 Top traction (tous univers)",
        "",
    ]
    for c in cands[:15]:
        d = f" · {c['date']}" if c.get("date") else ""
        lines.append(f"- `[{c['traction']:>3}]` **{c['title']}** — {c['url']} ({c['source']}{d})")
    lines.append("")
    by_u = {}
    for c in cands:
        by_u.setdefault(c["universe"], []).append(c)
    for u in UNIVERSE_WEIGHT:
        group = by_u.get(u, [])
        if not group:
            continue
        lines.append(f"## {UNIVERSE_LABEL.get(u, u)}  ({len(group)})")
        lines.append("")
        for c in group[:15]:
            d = f" · {c['date']}" if c.get("date") else ""
            extra = f" · {c['points']}pts" if c.get("points") else ""
            lines.append(f"- `[{c['traction']:>3}]` {c['title']} — {c['url']} ({c['source']}{d}{extra})")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--days", type=int, default=120)
    ap.add_argument("--max-reddit", type=int, default=12)
    args = ap.parse_args()

    today = dt.date.today()
    cutoff = today - dt.timedelta(days=args.days)
    log = ["Collecte :"]

    cands = []
    cands += collect_reddit(args.max_reddit, cutoff, log)
    cands += collect_hn(cutoff, log)
    cands += collect_rss(cutoff, log)
    cands = dedupe(cands)

    out_path = args.out or f"/tmp/mediaseo-vivier-{today}.md"
    md = render_markdown(cands, today, args.days)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    print("\n".join(log), file=sys.stderr)
    print(f"\n✅ Vivier : {len(cands)} candidats → {out_path}", file=sys.stderr)
    if args.json:
        jpath = out_path.rsplit(".", 1)[0] + ".json"
        with open(jpath, "w", encoding="utf-8") as f:
            json.dump(cands, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON : {jpath}", file=sys.stderr)
    print(out_path)


if __name__ == "__main__":
    main()
