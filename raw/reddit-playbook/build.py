#!/usr/bin/env python3
"""Génère Playbook-Reddit-complet.html (DA Reddit : feed, posts, votes, flairs) + PDF.
Contenu : Playbook-Reddit-SEO-GEO.md + Routine-quotidienne.md + Journal.md, transposés en posts.
Regénérer après toute modif des .md : python3 build.py
"""
import re, subprocess, pathlib

SRC = pathlib.Path(__file__).parent
OUT = SRC / "Playbook-Reddit-complet.html"

def load(name):
    txt = (SRC / name).read_text()
    return re.sub(r"^---\n.*?\n---\n", "", txt, flags=re.S).lstrip()

def wikilinks(txt):
    m = {"Routine-quotidienne": ("#routine", "la routine quotidienne"),
         "Journal": ("#journal", "le journal"),
         "Playbook-Reddit-SEO-GEO": ("#tldr", "le playbook")}
    def rep(mo):
        key = mo.group(1).split("|")[0].strip()
        return f"[{m[key][1]}]({m[key][0]})" if key in m else mo.group(1)
    return re.sub(r"\[\[([^\]]+)\]\]", rep, txt)

playbook = wikilinks(load("Playbook-Reddit-SEO-GEO.md"))
routine = wikilinks(load("Routine-quotidienne.md"))
journal = wikilinks(load("Journal.md"))

# ── Découpe du playbook en sections (## ...) ──────────────────────────────
parts = re.split(r"\n(?=## )", playbook)
sections = []  # (title, md)
for p in parts[1:]:
    lines = p.split("\n")
    title = lines[0].lstrip("# ").strip()
    body = "\n".join(lines[1:]).strip().strip("-").strip()
    sections.append((title, body))

# Routine : titre h1 retiré (il devient le titre du post)
routine_body = re.sub(r"^# .*\n", "", routine, count=1).strip()
journal_body = re.sub(r"^# .*\n", "", journal, count=1).strip()

# ── Rendu pandoc en un seul appel ─────────────────────────────────────────
SEP = "\n\n<!--SPLIT-->\n\n"
all_md = SEP.join([md for _, md in sections] + [routine_body, journal_body])
html_all = subprocess.run(["pandoc", "-f", "markdown", "-t", "html"],
                          input=all_md, capture_output=True, text=True, check=True).stdout
chunks = [c.strip() for c in html_all.split("<!--SPLIT-->")]
sec_html = chunks[: len(sections)]
routine_html, journal_html = chunks[len(sections)], chunks[len(sections) + 1]

# ── Habillage Reddit ──────────────────────────────────────────────────────
def slugify(t):
    t = re.sub(r"[^a-z0-9]+", "-", t.lower().replace("é", "e").replace("è", "e")
               .replace("ê", "e").replace("à", "a").replace("ç", "c").replace("î", "i")
               .replace("ô", "o").replace("û", "u").replace("’", "").replace("'", ""))
    return t.strip("-")[:60]

def votes_for(title):
    h = sum(ord(c) * (i + 3) for i, c in enumerate(title))
    v = 140 + (h % 2900)
    return f"{v/1000:.1f} k".replace(".", ",") if v >= 1000 else str(v)

def coms_for(title):
    h = sum(ord(c) * (i + 7) for i, c in enumerate(title))
    return 18 + (h % 240)

FLAIRS = [
    ("En résumé", "TL;DR", "f-orange"),
    ("terrain de test", "TEST TERRAIN", "f-green"),
    ("exécution", "ROUTINE", "f-blue"),
    ("1. Le terrain", "CONTEXTE", "f-gray"),
    ("2. Reddit et les IA", "GEO", "f-orange"),
    ("3. La règle d", "RÈGLE D'OR", "f-red"),
    ("4. Étape par étape", "MÉTHODE", "f-blue"),
    ("5. Trouver", "MÉTHODE", "f-blue"),
    ("6. La règle 9:1", "RÈGLE D'OR", "f-red"),
    ("7. Les formats", "MÉTHODE", "f-blue"),
    ("7bis", "PROTOCOLE", "f-blue"),
    ("8. Faire ranker", "SEO", "f-orange"),
    ("9. Reddit comme machine", "INSIGHTS", "f-green"),
    ("10. Les pièges", "WARNING", "f-red"),
    ("11. Modération", "MODÉRATION", "f-red"),
    ("12. Le cas francophone", "FRANCE", "f-blue"),
    ("13. Outils", "OUTILS", "f-gray"),
    ("14. Plan 90 jours", "PLAN 90 J", "f-green"),
    ("15. Les métriques", "MÉTRIQUES", "f-green"),
    ("Note de fiabilité", "FACT-CHECK", "f-gray"),
    ("Sources", "SOURCES", "f-gray"),
]
def flair_for(title):
    for pref, label, cls in FLAIRS:
        if title.startswith(pref) or pref in title[:40]:
            return label, cls
    return "DOCTRINE", "f-gray"

UP = '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M10 3l7 8h-4v6H7v-6H3z" fill="currentColor"/></svg>'
DOWN = '<svg viewBox="0 0 20 20" width="20" height="20"><path d="M10 17l-7-8h4V3h6v6h4z" fill="currentColor"/></svg>'
BUBBLE = '<svg viewBox="0 0 20 20" width="15" height="15" style="vertical-align:-2px"><path d="M10 2C5 2 1.5 5.1 1.5 9c0 2.2 1.2 4.2 3 5.5L4 18l4-1.6c.6.1 1.3.2 2 .2 5 0 8.5-3.1 8.5-7.6S15 2 10 2z" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'

def post(title, body_html, when, pid=None, extra=""):
    pid = pid or slugify(title)
    flair, fcls = flair_for(title)
    v, c = votes_for(title), coms_for(title)
    return f'''
<article class="post" id="{pid}">
  <div class="vote"><span class="up">{UP}</span><b>{v}</b><span class="down">{DOWN}</span></div>
  <div class="pbody">
    <div class="pmeta"><span class="flair {fcls}">{flair}</span> Posté par <a href="#">u/timboussardon</a> · {when}</div>
    <h2 class="ptitle">{title}</h2>
    <div class="pcontent">{body_html}</div>
    {extra}
    <div class="pactions">{BUBBLE} {c} commentaires &nbsp;·&nbsp; Partager &nbsp;·&nbsp; Enregistrer &nbsp;·&nbsp; Signaler</div>
  </div>
</article>'''

# Commentaire AutoModerator épinglé sous le TL;DR (les règles, en une bulle)
AUTOMOD = '''
<div class="comment automod">
  <div class="cav am">A</div>
  <div class="cbody">
    <div class="cmeta"><b class="am-name">u/AutoModerator</b> <span class="modtag">MOD</span> · épinglé</div>
    <p>Rappel des règles de r/PlaybookSEO : 95 % de contribution pour 5 % d'autopromo maximum, jamais deux fois le même commentaire, jamais le même lien plus de 2 fois par jour, et la machine ne publie jamais seule. Les infractions finissent en shadowban, et personne ne te préviendra.</p>
  </div>
</div>'''

posts = []
for i, (title, _) in enumerate(sections):
    when = "2 juil." if ("exécution" in title or "Note de fiabilité" in title) else "18 juin · m.à.j. 2 juil."
    pid = "tldr" if title.startswith("En résumé") else None
    extra = AUTOMOD if title.startswith("En résumé") else ""
    posts.append(post(title, sec_html[i], when, pid=pid, extra=extra))
    # Sommaire juste après le TL;DR
    if title.startswith("En résumé"):
        toc_items = "".join(
            f'<li><a href="#{ "tldr" if t.startswith("En résumé") else slugify(t)}">{t}</a></li>'
            for t, _ in sections
        ) + '<li><a href="#routine">Daily thread : la routine quotidienne (annexe A)</a></li>' \
          + '<li><a href="#journal">Le journal de suivi (annexe B)</a></li>'
        posts.append(post("Le sommaire, épinglé pour scroller utile",
                          f'<ol class="toc">{toc_items}</ol>', "18 juin", pid="sommaire"))

posts.append(post("Daily thread : la routine quotidienne (annexe A)", routine_html, "2 juil.", pid="routine"))
posts.append(post("Le journal de suivi (annexe B)", journal_html, "2 juil.", pid="journal"))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');
:root{
  --bg:#DAE0E6; --card:#fff; --line:#ccc; --ink:#1c1c1c; --meta:#787c7e;
  --orange:#FF4500; --blue:#0079D3; --downblue:#7193FF; --votebg:#F8F9FA;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:'IBM Plex Sans',-apple-system,sans-serif;font-size:15.5px;line-height:1.6}
a{color:var(--blue);text-decoration:none} a:hover{text-decoration:underline}
.mono{font-family:'IBM Plex Mono',monospace}

/* ── Topbar ── */
.topbar{background:#fff;border-bottom:1px solid #edeff1;padding:8px 20px;display:flex;align-items:center;gap:16px;position:sticky;top:0;z-index:9}
.logo{display:flex;align-items:center;gap:8px;font-weight:700;font-size:17px;letter-spacing:-.02em}
.logo .disc{width:30px;height:30px;border-radius:50%;background:var(--orange);color:#fff;display:flex;align-items:center;justify-content:center}
.searchbar{flex:1;max-width:560px;background:#f6f7f8;border:1px solid #edeff1;border-radius:20px;padding:8px 16px;font-size:13.5px;color:var(--meta)}
.searchbar:hover{border-color:var(--blue)}
.tb-user{margin-left:auto;font-size:12.5px;color:var(--meta)}
.tb-user b{color:var(--ink)}
.karma{color:var(--orange);font-weight:600}

/* ── Bannière ── */
.banner{background:linear-gradient(90deg,#FF4500,#FF6A1A);height:104px}
.subhead{background:#fff;padding:0 20px 12px}
.subhead .inner{max-width:1020px;margin:0 auto;display:flex;align-items:flex-end;gap:16px;transform:translateY(-18px)}
.sub-avatar{width:76px;height:76px;border-radius:50%;background:#fff;border:4px solid #fff;box-shadow:0 1px 4px rgba(0,0,0,.18);display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;color:var(--orange)}
.sub-title h1{font-size:26px;font-weight:700;letter-spacing:-.02em}
.sub-title .rname{font-size:14px;color:var(--meta)}
.joinbtn{margin-left:auto;margin-bottom:10px;background:var(--orange);color:#fff;font-weight:600;font-size:14px;border:none;border-radius:20px;padding:7px 22px}

/* ── Layout feed + sidebar ── */
.wrap{max-width:1020px;margin:18px auto 60px;padding:0 20px;display:flex;gap:22px;align-items:flex-start}
.feed{flex:1;min-width:0}
.sidebar{width:300px;flex-shrink:0;position:sticky;top:62px;order:2}
@media(max-width:900px){.sidebar{display:none}}

/* ── Sidebar « À propos » ── */
.about{background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden;margin-bottom:16px}
.about .ahead{background:var(--orange);color:#fff;font-weight:600;font-size:13.5px;padding:10px 14px}
.about .abody{padding:12px 14px;font-size:13.5px}
.about .abody p{margin:0 0 12px;color:#4a4a4a}
.stat{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid #edeff1;font-size:13px}
.stat:last-of-type{border-bottom:none}
.stat b{font-size:14px}
.stat span{color:var(--meta);text-align:right;max-width:170px}
.rule{font-size:12.5px;color:var(--meta);padding:8px 0 0;border-top:1px solid #edeff1;margin-top:8px}

/* ── Post ── */
.post{background:var(--card);border:1px solid var(--line);border-radius:6px;display:flex;margin-bottom:14px;overflow:hidden}
.post:hover{border-color:#898989}
.vote{width:44px;background:var(--votebg);padding:10px 0;display:flex;flex-direction:column;align-items:center;gap:2px;flex-shrink:0}
.vote .up{color:var(--orange)} .vote .down{color:#b8bcc0}
.vote b{font-size:12.5px;font-weight:700}
.pbody{padding:10px 18px 8px;min-width:0;flex:1}
.pmeta{font-size:12px;color:var(--meta);margin-bottom:6px}
.pmeta a{color:var(--meta);font-weight:500}
.flair{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.04em;border-radius:10px;padding:2px 9px;margin-right:8px;vertical-align:1px}
.f-orange{background:#FF4500;color:#fff}
.f-blue{background:#0079D3;color:#fff}
.f-green{background:#0DD3BB;color:#053c36}
.f-red{background:#EA0027;color:#fff}
.f-gray{background:#edeff1;color:#1c1c1c}
.ptitle{font-size:20px;font-weight:600;line-height:1.3;letter-spacing:-.01em;margin-bottom:12px}
.pactions{font-size:12.5px;font-weight:600;color:var(--meta);padding:10px 0 6px;border-top:1px solid #edeff1;margin-top:14px}

/* ── Contenu de post ── */
.pcontent p{margin:0 0 14px}
.pcontent h2{font-size:17px;font-weight:700;margin:26px 0 10px;padding-bottom:6px;border-bottom:1px solid #edeff1}
.pcontent h3{font-size:15.5px;font-weight:700;margin:20px 0 8px}
.pcontent ul,.pcontent ol{margin:0 0 14px;padding-left:24px}
.pcontent li{margin:4px 0}
.pcontent strong{font-weight:600}
.pcontent blockquote{border-left:4px solid #c8ccd0;padding:2px 0 2px 14px;margin:0 0 14px;color:#4a4a4a}
.pcontent table{width:100%;border-collapse:collapse;margin:14px 0 18px;font-size:13.5px}
.pcontent thead th{text-align:left;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--meta);border-bottom:2px solid #1c1c1c;padding:6px 10px 6px 0}
.pcontent tbody td{border-bottom:1px solid #edeff1;padding:8px 10px 8px 0;vertical-align:top}
.pcontent code{font-family:'IBM Plex Mono',monospace;font-size:12.5px;background:#f6f7f8;border:1px solid #edeff1;border-radius:4px;padding:1px 5px}
.pcontent pre{background:#f6f7f8;border:1px solid #edeff1;border-radius:6px;padding:12px 16px;overflow-x:auto;margin:0 0 14px}
.pcontent pre code{background:none;border:none;padding:0;font-size:12.5px;line-height:1.6}
.pcontent hr{border:none;border-top:1px solid #edeff1;margin:22px 0}
ol.toc{padding-left:26px}
ol.toc li{margin:7px 0;font-size:14.5px}

/* ── Commentaires ── */
.comment{display:flex;gap:10px;margin:16px 0 4px;padding:12px;border-radius:6px}
.comment.automod{background:#eefaf0;border:1px solid #cdeed3}
.cav{width:30px;height:30px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:14px}
.cav.am{background:#46A758}
.cbody{font-size:13.5px;line-height:1.55;min-width:0}
.cbody p{margin:0}
.cmeta{font-size:12px;margin-bottom:4px;color:var(--meta)}
.am-name{color:#2f7a3d}
.modtag{background:#46A758;color:#fff;font-size:10px;font-weight:700;border-radius:3px;padding:1px 5px;vertical-align:1px}

/* ── Print ── */
@media print{
  body{background:#fff}
  .topbar,.joinbtn{position:static}
  .searchbar{display:none}
  .wrap{display:block;max-width:none;padding:0 4mm}
  .sidebar{position:static;width:auto;display:block;margin-bottom:14px}
  .post{break-inside:auto;box-shadow:none}
  .pmeta,.comment,.about,table,blockquote,pre{break-inside:avoid}
  .vote{break-inside:auto}
  .ptitle{break-after:avoid}
  a{color:var(--ink)}
  @page{margin:12mm 10mm}
}
"""

html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>r/PlaybookSEO · Le playbook Reddit d'Organikk</title>
<style>{CSS}</style>
</head>
<body>

<div class="topbar">
  <div class="logo"><span class="disc">{UP}</span> playbook</div>
  <div class="searchbar">Rechercher dans r/PlaybookSEO</div>
  <div class="tb-user"><b>u/timboussardon</b> · karma <span class="karma">à construire (c'est le sujet)</span></div>
</div>

<div class="banner"></div>
<div class="subhead"><div class="inner">
  <div class="sub-avatar">r/</div>
  <div class="sub-title"><h1>Le playbook Reddit d'Organikk</h1><div class="rname">r/PlaybookSEO · être lu par Google, cité par les IA</div></div>
  <button class="joinbtn">S'abonner</button>
</div></div>

<div class="wrap">
<aside class="sidebar">
  <div class="about">
    <div class="ahead">À propos de la communauté</div>
    <div class="abody">
      <p>Faire de Reddit un canal SEO + GEO sans se faire bannir. Doctrine, routine et journal, sur data sourcée. Les chiffres fragiles sont signalés comme tels.</p>
      <div class="stat"><b>20,6 M</b><span>utilisateurs Reddit estimés en France</span></div>
      <div class="stat"><b>top 5</b><span>des domaines les plus visibles sur Google US</span></div>
      <div class="stat"><b>60 M$/an</b><span>payés par Google pour la data Reddit</span></div>
      <div class="stat"><b>&lt; 20</b><span>upvotes sur 80 % des posts cités par les IA (Semrush)</span></div>
      <div class="rule">Créé le 18 juin 2026 · vérifié contre ~25 sources le 2 juil. · terrain de test : Qadence.io</div>
      <div class="rule">Règle n°1 : la machine ne publie jamais seule.</div>
    </div>
  </div>
</aside>

<main class="feed">
{''.join(posts)}
</main>
</div>

</body>
</html>"""

OUT.write_text(html)
print(f"HTML: {OUT} ({len(html)//1024} Ko, {len(posts)} posts)")
