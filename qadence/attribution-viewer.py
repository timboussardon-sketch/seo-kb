#!/usr/bin/env python3
"""
Sert Corpus-6-attribution.md en local, avec les cellules vides remplissables.

Lit le markdown, rend les 3 tables en HTML, transforme chaque cellule vide des
groupes B et C en menu déroulant du vocabulaire de classes.ts. Les choix sont
gardés dans le navigateur (localStorage) et réexportables en markdown.

Le fichier .md reste la source. Ce script ne l'écrit jamais.

Usage : python3 qadence/attribution-viewer.py [port]
"""

import http.server
import json
import os
import re
import socketserver
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(VAULT, "qadence", "Corpus-6-attribution.md")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

VOCAB = {
    "effort": ["agent", "client_cms", "redaction", "dev", "consultant"],
    "severity": ["critical", "minor"],
    "blastRadius": ["page", "template", "site"],
    "reversibility": ["commit", "index_slow"],
    "detectionLatency": ["immediate", "crawl", "gsc"],
}


def inline(s):
    s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="wl">\1</span>', s)
    return s


def render(md):
    """Markdown → HTML. Gère titres, tables, listes, paragraphes."""
    out, i = [], 0
    lines = md.split("\n")
    table_n = 0
    while i < len(lines):
        ln = lines[i]

        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1]):
            head = [c.strip() for c in ln.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            table_n += 1
            out.append(table_html(head, rows, table_n))
            continue

        if ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:])}</h2>")
        elif ln.startswith("# "):
            out.append(f"<h1>{inline(ln[2:])}</h1>")
        elif ln.startswith("---"):
            out.append("<hr>")
        elif re.match(r"^\d+\. ", ln):
            out.append(f"<p class='num'>{inline(ln)}</p>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "\n".join(out)


def table_html(head, rows, tid):
    """Cellule vide sur une colonne du vocabulaire → menu déroulant."""
    cols = [h.strip() for h in head]
    th = "".join(f"<th>{inline(h)}</th>" for h in cols)
    body = []
    for r_i, r in enumerate(rows):
        tds = []
        for c_i, cell in enumerate(r):
            col = cols[c_i] if c_i < len(cols) else ""
            if col in VOCAB and cell == "":
                key = f"t{tid}-r{r_i}-{col}"
                opts = "".join(f"<option value='{v}'>{v}</option>" for v in VOCAB[col])
                tds.append(
                    f"<td class='fill'><select data-k='{key}'>"
                    f"<option value=''>—</option>{opts}</select></td>"
                )
            else:
                cls = " num" if cell.replace(",", "").replace(" ", "").isdigit() else ""
                tds.append(f"<td class='{cls.strip()}'>{inline(cell)}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    return (
        f"<div class='tw'><table data-t='{tid}'><thead><tr>{th}</tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table></div>"
    )


PAGE = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Corpus 6 — attribution</title><style>
*{box-sizing:border-box}
body{margin:0;padding:48px 32px 120px;font-family:Geist,-apple-system,system-ui,sans-serif;
font-size:15px;line-height:1.65;color:#1c1e21;background:#F4F5F7}
main{max-width:1180px;margin:0 auto}
h1{font-size:28px;font-weight:600;letter-spacing:-.02em;margin:0 0 24px}
h2{font-size:19px;font-weight:600;letter-spacing:-.01em;margin:40px 0 12px}
h3{font-size:16px;font-weight:600;margin:28px 0 8px}
p{margin:0 0 12px;max-width:78ch}
hr{border:0;border-top:1px solid #E3E5E9;margin:36px 0}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;
background:#EBEDF1;padding:1px 5px;border-radius:4px}
.wl{color:#4F6BFF}
.tw{overflow-x:auto;background:#fff;border:1px solid #E3E5E9;border-radius:12px;margin:16px 0 28px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{text-align:left;font-weight:600;padding:11px 12px;background:#FAFBFC;
border-bottom:1px solid #E3E5E9;white-space:nowrap}
td{padding:10px 12px;border-bottom:1px solid #F0F1F4;vertical-align:top}
tr:last-child td{border-bottom:0}
td.num,th.num{font-variant-numeric:tabular-nums}
td.fill{padding:6px 8px;background:#FCFCFD}
select{font-family:inherit;font-size:13px;padding:5px 7px;border:1px solid #D8DBE0;
border-radius:7px;background:#fff;color:#1c1e21;min-width:118px}
select:focus{outline:2px solid #4F6BFF;outline-offset:-1px}
select.set{border-color:#4F6BFF;background:#F5F7FF;font-weight:500}
.bar{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid #E3E5E9;
padding:12px 32px;display:flex;gap:14px;align-items:center;justify-content:center}
button{font-family:inherit;font-size:14px;font-weight:500;padding:9px 16px;border-radius:9px;
border:1px solid #D8DBE0;background:#fff;color:#1c1e21;cursor:pointer}
button.p{background:#4F6BFF;border-color:#4F6BFF;color:#fff}
.count{font-size:13.5px;color:#6B7280;font-variant-numeric:tabular-nums}
textarea{position:fixed;inset:5% 8%;width:84%;height:84%;display:none;z-index:9;padding:20px;
font-family:ui-monospace,monospace;font-size:12.5px;border:1px solid #D8DBE0;border-radius:12px}
</style></head><body><main>__BODY__</main>
<textarea id="out" readonly></textarea>
<div class="bar">
  <span class="count" id="c"></span>
  <button onclick="reset()">Tout vider</button>
  <button class="p" onclick="dump()">Exporter en markdown</button>
</div>
<script>
const S=JSON.parse(localStorage.getItem('c6')||'{}');
const sels=[...document.querySelectorAll('select')];
function paint(){
  let n=0;
  sels.forEach(s=>{const v=S[s.dataset.k]||'';s.value=v;s.classList.toggle('set',!!v);if(v)n++});
  document.getElementById('c').textContent=n+' / '+sels.length+' cellules remplies';
}
sels.forEach(s=>s.onchange=()=>{
  S[s.dataset.k]=s.value;localStorage.setItem('c6',JSON.stringify(S));paint();
});
function reset(){if(confirm('Vider toutes les attributions ?')){localStorage.removeItem('c6');
  for(const k in S)delete S[k];paint()}}
function dump(){
  let md='';
  document.querySelectorAll('table').forEach(t=>{
    const heads=[...t.querySelectorAll('thead th')].map(h=>h.textContent.trim());
    md+='| '+heads.join(' | ')+' |\\n|'+heads.map(()=>'---').join('|')+'|\\n';
    t.querySelectorAll('tbody tr').forEach(tr=>{
      md+='| '+[...tr.children].map(td=>{
        const s=td.querySelector('select');return s?(s.value||''):td.textContent.trim();
      }).join(' | ')+' |\\n';
    });
    md+='\\n';
  });
  const o=document.getElementById('out');o.value=md;o.style.display='block';o.select();
  o.onblur=()=>o.style.display='none';
}
paint();
</script></body></html>"""


class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        with open(MD, encoding="utf-8") as f:
            html = PAGE.replace("__BODY__", render(f.read()))
        b = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), H) as httpd:
        print(f"http://localhost:{PORT}")
        httpd.serve_forever()
