# -*- coding: utf-8 -*-
"""golfiller-strat.pdf — style Google Docs : Arial/Helvetica, texte noir,
tableaux à filets gris, accents bleu Google. Sobre, document de travail.
Visuels reconstruits à partir des données réelles du doc. Pas d'eyebrows,
pas de cartes/gradients (anti-patterns IA)."""
import os, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Flowable, ListFlowable, ListItem, HRFlowable, CondPageBreak, Image
)
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# ---- Couleurs Google Docs --------------------------------------------------
INK    = colors.HexColor("#202124")   # texte principal
GREY   = colors.HexColor("#5F6368")   # secondaire / sous-titre
GREY2  = colors.HexColor("#80868B")   # légendes
BLUE   = colors.HexColor("#1A73E8")   # accent / liens Google
BLUEDK = colors.HexColor("#1155CC")   # liens texte
GRID   = colors.HexColor("#D9D9D9")   # filets de tableau
HEADBG = colors.HexColor("#F3F3F3")   # fond entête de tableau
BOXBG  = colors.HexColor("#F8F9FA")   # encadré léger
WHITE  = colors.white

SANS, SANS_B, SANS_I = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
MONO = "Courier"

PAGE_W, PAGE_H = A4
MARGIN = 25.4 * mm     # 1 pouce, marge Google Docs par défaut
CW = PAGE_W - 2*MARGIN

# ---- Styles ----------------------------------------------------------------
ss = getSampleStyleSheet()
def style(n, **kw):
    base = kw.pop("parent", ss["Normal"]); return ParagraphStyle(n, parent=base, **kw)

S = {
 "title": style("title", fontName=SANS, fontSize=26, textColor=INK, leading=30, spaceAfter=2),
 "subtitle": style("subtitle", fontName=SANS, fontSize=13, textColor=GREY, leading=18, spaceAfter=2),
 "h1": style("h1", fontName=SANS_B, fontSize=16, textColor=INK, leading=20,
             spaceBefore=18, spaceAfter=6),
 "h2": style("h2", fontName=SANS_B, fontSize=12.5, textColor=INK, leading=16,
             spaceBefore=13, spaceAfter=4),
 "h3": style("h3", fontName=SANS_B, fontSize=10.5, textColor=INK, leading=14,
             spaceBefore=9, spaceAfter=2),
 "h4": style("h4", fontName=SANS_B, fontSize=10, textColor=INK, leading=13,
             spaceBefore=6, spaceAfter=1),
 "body": style("body", fontName=SANS, fontSize=11, textColor=INK, leading=16.5,
               spaceAfter=8, alignment=TA_JUSTIFY),
 "bull": style("bull", fontName=SANS, fontSize=11, textColor=INK, leading=16, spaceAfter=5),
 "cap": style("cap", fontName=SANS_I, fontSize=8.5, textColor=GREY2, leading=12,
              spaceBefore=3, spaceAfter=2),
 "capC": style("capC", fontName=SANS_I, fontSize=8.5, textColor=GREY2, leading=12,
               spaceBefore=4, spaceAfter=10, alignment=1),
 "th": style("th", fontName=SANS_B, fontSize=9.5, textColor=INK, leading=12),
 "td": style("td", fontName=SANS, fontSize=10, textColor=INK, leading=13.5),
 "tdb": style("tdb", fontName=SANS_B, fontSize=10, textColor=INK, leading=13.5),
 "box": style("box", fontName=SANS, fontSize=10.5, textColor=INK, leading=15.5),
}
def P(t, s="body"): return Paragraph(t, S[s])
def bullets(items, st="bull"):
    its=[ListItem(Paragraph(t,S[st]), leftIndent=12) for t in items]
    return ListFlowable(its, bulletType="bullet", bulletChar="•", bulletColor=INK,
                        bulletFontSize=8, leftIndent=15, spaceBefore=0, spaceAfter=2)

# ---- Bar chart minimal (style Google Sheets inséré) ------------------------
class HBar(Flowable):
    def __init__(self, w, data, rowh=10*mm):
        super().__init__(); self.w=w; self.data=data; self.rowh=rowh; self.h=rowh*len(data)+4
    def wrap(self,*a): return (self.w, self.h)
    def draw(self):
        c=self.canv; labw=62*mm; valw=18*mm
        cx=labw; cwid=self.w-labw-valw
        mx=max(v for _,v in self.data) or 1
        # axe léger
        c.setStrokeColor(GRID); c.setLineWidth(0.6); c.line(cx,0,cx,self.h-4)
        for i,(lab,val) in enumerate(self.data):
            y=self.h-4-(i+1)*self.rowh + 2.4*mm
            c.setFillColor(INK); c.setFont(SANS,9)
            words=lab.split(); cur=""; lines=[]
            for w in words:
                t=(cur+" "+w).strip()
                if c.stringWidth(t,SANS,9)<=labw-6: cur=t
                else: lines.append(cur); cur=w
            lines.append(cur); lines=lines[:2]
            ly=y+(3 if len(lines)>1 else 0)
            for ln in lines: c.drawString(0,ly,ln); ly-=9.5
            bw=cwid*(val/mx)
            c.setFillColor(BLUE); c.rect(cx,y-1,max(bw,2),5.6*mm-1,fill=1,stroke=0)
            c.setFillColor(INK); c.setFont(SANS_B,9)
            c.drawString(cx+bw+5,y+0.6,f"{val:,}".replace(","," "))

def TABLE(rows, widths, grid=True, header=True, highlight=None, valign="MIDDLE"):
    t=Table(rows, colWidths=widths)
    sty=[("VALIGN",(0,0),(-1,-1),valign),
         ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
         ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8)]
    if grid: sty.append(("GRID",(0,0),(-1,-1),0.75,GRID))
    if header: sty.append(("BACKGROUND",(0,0),(-1,0),HEADBG))
    if highlight is not None: sty.append(("BACKGROUND",(0,highlight),(-1,highlight),colors.HexColor("#E8F0FE")))
    t.setStyle(TableStyle(sty)); return t

def box(w, head, body):
    inner=[Paragraph("<b>%s</b>"%head, S["box"]), Spacer(1,2), Paragraph(body, S["box"])]
    t=Table([[inner]], colWidths=[w])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),BOXBG),
        ("BOX",(0,0),(-1,-1),0.75,GRID),
        ("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),
        ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
    ]))
    return t

# ---- Carte skill (façon fiche d'accompagnement, fait ressortir le skill) ---
def skill_card(cmd, what, when, inp):
    head=Paragraph("<font name='Courier'><b><font color='#1155CC'>%s</font></b></font>"%cmd, S["h3"])
    def row(lab, val): return Paragraph("<b>%s</b> %s"%(lab, val), S["box"])
    inner=[head, Spacer(1,5),
           row("Ce qu'il fait :", what), Spacer(1,3),
           row("Quand s'en servir :", when), Spacer(1,3),
           row("Ce qu'il faut lui donner :", inp)]
    t=Table([[inner]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),BOXBG),
        ("BOX",(0,0),(-1,-1),0.75,GRID),
        ("LINEBEFORE",(0,0),(0,-1),3,BLUE),
        ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),12),
        ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
    ]))
    return [CondPageBreak(38*mm), t, Spacer(1,8)]

SHOTS=os.path.join(os.path.dirname(__file__),"shots")
def shot(name, width_mm, caption):
    """Capture d'écran Fusionn : image centrée + légende, façon image insérée Google Docs."""
    path=os.path.join(SHOTS, name)
    iw,ih=ImageReader(path).getSize()
    w=width_mm*mm; h=w*ih/iw
    img=Image(path, width=w, height=h); img.hAlign="CENTER"
    return [CondPageBreak(h+16*mm), Spacer(1,4), img, Paragraph(caption, S["capC"])]

# ---- Rendu markdown (pour insérer les SKILL.md en intégralité) -------------
SKILLS_DIR = os.path.expanduser("~/.claude/skills")
DROP_SECTIONS = {"sauvegarde","concepts liés","concepts lies"}

def _esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def md_inline(s):
    s = s.replace("Money Page","page business").replace("money page","page business")
    s = _esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r'<font name="Courier" size="9">\1</font>', s)
    return s
def _is_internal(s):
    low=s.lower()
    return any(k in low for k in ["wiki/","agents.md","cf. kb","vault","hook §"])
def _code_block(txt):
    # Paragraph stylé (et non Table) pour pouvoir se découper entre deux pages.
    p=ParagraphStyle("code",parent=S["body"],fontName="Courier",fontSize=8.5,leading=11.5,
                     alignment=TA_LEFT,textColor=INK,backColor=BOXBG,borderColor=GRID,
                     borderWidth=0.5,borderPadding=8,spaceBefore=2,spaceAfter=6)
    txt=txt.replace("Money Page","page business").replace("money page","page business")
    return Paragraph("<br/>".join(_esc(l) for l in txt.split("\n")), p)
def _quote_block(txt):
    p=ParagraphStyle("q",parent=S["body"],fontName=SANS_I,textColor=GREY,alignment=TA_LEFT)
    t=Table([[Paragraph(md_inline(txt),p)]],colWidths=[CW])
    t.setStyle(TableStyle([("LINEBEFORE",(0,0),(0,-1),3,BLUE),("BACKGROUND",(0,0),(-1,-1),BOXBG),
        ("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return t
def _md_table(tb):
    grid=[[c.strip() for c in r.strip().strip("|").split("|")] for r in tb]
    grid=[r for r in grid if not all(re.match(r"^:?-{2,}:?$", (c or "x")) for c in r)]
    if not grid: return Spacer(0,0)
    ncol=max(len(r) for r in grid); grid=[r+[""]*(ncol-len(r)) for r in grid]
    rows=[[Paragraph(md_inline(c),S["th"]) for c in grid[0]]]
    for r in grid[1:]: rows.append([Paragraph(md_inline(c),S["td"]) for c in r])
    return TABLE(rows,[CW/ncol]*ncol,valign="TOP")
def render_md(text):
    lines=text.split("\n")
    if lines and lines[0].strip()=="---":
        for j in range(1,len(lines)):
            if lines[j].strip()=="---": lines=lines[j+1:]; break
    fl=[]; i=0; n=len(lines); skip=False
    bullet=re.compile(r"^\s*([-*]|\d+\.)\s+")
    while i<n:
        raw=lines[i]; s=raw.strip()
        mh=re.match(r"^(#{1,6})\s+(.*)$", s)
        if mh:
            lvl=len(mh.group(1)); title=mh.group(2).strip()
            if title.lower() in DROP_SECTIONS: skip=True; i+=1; continue
            skip=False
            if lvl==1: i+=1; continue
            fl.append(Paragraph(md_inline(title), S["h3" if lvl==2 else "h4"])); i+=1; continue
        if skip or s=="": i+=1; continue
        if s.startswith("```"):
            i+=1; buf=[]
            while i<n and not lines[i].strip().startswith("```"): buf.append(lines[i]); i+=1
            i+=1; fl.append(_code_block("\n".join(buf))); continue
        if s.startswith("|"):
            tb=[]
            while i<n and lines[i].strip().startswith("|"): tb.append(lines[i].strip()); i+=1
            fl.append(_md_table(tb)); continue
        if s.startswith(">"):
            buf=[]
            while i<n and lines[i].strip().startswith(">"): buf.append(lines[i].strip().lstrip(">").strip()); i+=1
            fl.append(_quote_block(" ".join(buf))); continue
        if bullet.match(raw):
            while i<n and bullet.match(lines[i]):
                li=lines[i]; i+=1
                if _is_internal(li): continue
                indent=len(li)-len(li.lstrip(" ")); c=li.strip()
                mnum=re.match(r"^(\d+)\.\s+(.*)$", c); mbul=re.match(r"^[-*]\s+(.*)$", c)
                if mnum: prefix="<b>%s.</b> "%mnum.group(1); bodyt=mnum.group(2)
                elif mbul: prefix="•  "; bodyt=mbul.group(1)
                else: prefix=""; bodyt=c
                left=14+(18 if indent>=2 else 0)
                ps=ParagraphStyle("li",parent=S["body"],leftIndent=left,firstLineIndent=-12,
                                  spaceAfter=2,alignment=TA_LEFT)
                fl.append(Paragraph(prefix+md_inline(bodyt), ps))
            continue
        buf=[]
        while i<n and lines[i].strip()!="" and not bullet.match(lines[i]) and not lines[i].strip().startswith(("#","|","```",">")):
            buf.append(lines[i].strip()); i+=1
        para=" ".join(buf)
        if para and not _is_internal(para): fl.append(Paragraph(md_inline(para), S["body"]))
    return fl

# ---- Page chrome (sobre, façon doc : juste un n° de page) ------------------
def chrome(c, doc):
    c.saveState()
    c.setFillColor(GREY2); c.setFont(SANS,9)
    c.drawRightString(PAGE_W-MARGIN, 14*mm, "%d" % doc.page)
    c.restoreState()

OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","golfiller-strat.pdf"))
doc=BaseDocTemplate(OUT, pagesize=A4, leftMargin=MARGIN, rightMargin=MARGIN,
                    topMargin=24*mm, bottomMargin=20*mm, title="Golfiller — Stratégie SEO",
                    author="Organikk")
frame=Frame(MARGIN,18*mm,CW,PAGE_H-24*mm-18*mm,id="body")
doc.addPageTemplates([PageTemplate(id="main",frames=[frame],onPage=chrome)])

# ---- Story -----------------------------------------------------------------
st=[]
# Titre du document (façon "Titre / Sous-titre" Google Docs)
st.append(Paragraph("Golfiller : Stratégie SEO", S["title"]))
st.append(Spacer(1,4))
st.append(HRFlowable(width="100%", thickness=0.75, color=GRID, spaceBefore=2, spaceAfter=10))

st.append(Paragraph("Objectif et contexte", S["h1"]))
st.append(P("Golfiller (golfiller.fr), e-commerce de balles de golf d'occasion et reconditionnées. "
   "Objectif : bâtir une autorité sur une niche défendable, les balles de golf d'occasion, plutôt que de "
   "viser les mêmes requêtes génériques que les gros acteurs. Résultat : 1re position sur « balle de "
   "golf », devant Décathlon et Amazon, sans un seul backlink."))
st.append(P("État : projet pSEO actif sur les requêtes slope et handicap, base de ~40 parcours français "
   "(slope + SSS), calculateur de handicap interactif (formule FFGolf), page HTML sémantique brute "
   "(calculateur + tableau filtrable + sections par parcours). À venir : extension à ~100 parcours, "
   "Phase 2 pSEO (une URL par parcours) si la pilier performe."))

st.append(Paragraph("Analyse GSC : les pages winners", S["h1"]))
st.append(P("Les trois pages qui sur-performent ont un point commun : elles font faire quelque chose à "
   "l'internaute. Calculer un index, comparer deux balles, consulter un parcours. Ce sont des outils, pas "
   "des articles. Une IA résume un texte, mais elle ne fait pas tourner un calculateur à la place de "
   "l'utilisateur. Le réflexe à garder : lire la Search Console, repérer ce qui marche, le répliquer."))
st.append(box(CW,"Ce que ça veut dire",
   "Les pages qui demandent une action résistent. Les pages qui ne font qu'informer se font absorber par "
   "les réponses IA de Google, qui donnent la réponse sans renvoyer de clic. Un calculateur ou un tableau "
   "interactif n'a pas ce problème : l'utilisateur doit venir sur la page pour s'en servir."))

st.append(Paragraph("La réflexion derrière la stratégie", S["h1"]))
st.append(Paragraph("1. Pourquoi les pages-outils gagnent", S["h3"]))
st.append(P("Les trois pages qui marchent sont des outils, pas des articles. Une IA recopie et résume un "
   "texte sans difficulté, mais elle ne remplit pas un calculateur ni ne trie un tableau à la place de "
   "l'internaute. C'est aussi ce que Google met en avant : une page qui règle le besoin sur place, sans "
   "renvoyer l'internaute chercher ailleurs."))
st.append(Paragraph("2. Ce qu'une page doit contenir pour être prise au sérieux", S["h3"]))
st.append(bullets([
  "<b>Le vocabulaire du métier :</b> slope, SSS, index, compression, carry. Sans lui, la page ne parle "
  "pas le langage du sujet.",
  "<b>Des chiffres sourcés :</b> données Trackman, PGA Tour, FFGolf, avec leur unité et leur contexte. "
  "C'est ce qui rend la page crédible pour une IA qui cherche une source fiable à citer.",
  "<b>Le bon format :</b> une requête « calculer son index » attend un calculateur, pas un paragraphe. "
  "Une page sans l'outil attendu est incomplète.",
  "<b>Une donnée ou un angle que personne d'autre n'a.</b>",
]))
st.append(P("Le bon dosage n'est pas de répéter ce que tout le monde dit. C'est de coller au sujet tout en "
   "apportant quelque chose que les autres pages n'ont pas. Ni hors-sujet, ni redondant."))
st.append(Paragraph("3. Ce qui fait qu'une IA cite la marque", S["h3"]))
st.append(P("Une IA cite la source qui apporte l'information qu'elle ne trouve pas ailleurs. Chez "
   "Golfiller, cette information vient de la donnée maison : les distances réelles mesurées par profil de "
   "joueur, les compressions croisées, agrégées à partir des clients. Repère simple : si un concurrent "
   "peut recopier l'angle en cinq minutes, ce n'est pas un avantage."))
st.append(Paragraph("4. Couvrir tout le sujet, avec sa propre donnée", S["h3"]))
st.append(P("Une page isolée ne suffit pas. Il faut traiter toutes les questions du sujet : le slope, "
   "l'index, la compression, la distance par club, le choix de balle. Plus l'ensemble est complet, plus "
   "Google lit le site comme une référence sur la verticale. Et sans donnée propre dans les pages, on "
   "retombe sur ce que l'IA sait déjà, donc sur du contenu interchangeable. La donnée maison alimente tout "
   "le reste : les chiffres, l'angle unique, les outils."))

st.append(Paragraph("Opportunités d'outils à créer", S["h1"]))
st.append(bullets([
  "<b>Calculette / simulateur d'index interactif.</b> La page /calcul-index-golf est déjà à 1 816 clics "
  "et 77 786 impressions, en position moyenne 11,77. La rendre interactive la fait monter.",
  "<b>Quiz « Quelle balle pour vous ? ».</b> Page texte (1 330 clics, pos 8,45) à transformer en quiz. "
  "Conversion native, tech la plus simple.",
  "<b>Carte de score interactive / différentiel.</b> Carte digitale trou par trou + calcul auto + PDF.",
  "<b>Tableau de distance de clubs par profil.</b> Réplique du format « tableau » qui gagne déjà, "
  "filtrable. Sa valeur unique : la donnée agrégée des clients.",
  "<b>Comparateur de balles côte à côte.</b> Rendre dynamique le tableau de compression. Bonus pSEO : "
  "URLs /comparer/pro-v1-vs-pro-v1x.",
]))
st.append(P("Si on ne lance qu'un seul outil : le quiz « Quelle balle pour vous ». C'est le plus simple à "
   "mettre en place, il convertit directement, et il relance une page de texte qui stagne aujourd'hui."))

st.append(Paragraph("Créer un modèle de page et le lancer en production", S["h1"]))
st.append(P("La logique pSEO tient en une phrase : <b>1 template + 1 variable qui change = N pages "
   "uniques</b>, chacune sur une requête longue traîne. Le produit, c'est la combinaison base de données "
   "× structure de page, pas le texte écrit à la main."))
for h,b in [
 ("1. Choisir le modèle (template + variable)",
  "Le template « page parcours » se décline sur la variable « parcours » (base de ~40 parcours français : "
  "slope + SSS). Autres variables activables : la balle (comparateur), le profil (tableau de distances). "
  "Chaque combinaison vise une question différente, ce qui évite que deux pages se fassent concurrence sur "
  "la même requête."),
 ("2. Garantir l'unicité réelle, pas le copier-coller",
  "Règle non négociable : plus de 70 % du contenu change entre deux pages, et la transformation porte sur "
  "le fond (slope, SSS, sections propres au parcours), pas seulement sur la variable. Des pages générées "
  "en changeant un seul mot se font rétrograder ou désindexer par Google en quelques jours."),
 ("3. Injecter sa propre donnée",
  "La valeur vient des chiffres eux-mêmes (base de parcours construite à la main, données clients "
  "agrégées), pas du commentaire autour. On s'appuie sur des sources officielles, jamais de récupération "
  "sauvage. C'est ce qui nourrit à la fois les chiffres, l'angle unique et le calculateur."),
 ("4. Construire une page simple et propre",
  "Calculateur de handicap (formule FFGolf), tableau filtrable, sections par parcours, en HTML net, sans "
  "fioritures. Objectif : chaque section de la page se suffit à elle-même et peut se positionner seule sur "
  "sa requête."),
 ("5. Lancer par paliers, piloté par la GSC",
  "Pilote d'abord (page pilier + base ~40 parcours), on mesure en Search Console, et on n'étend (Phase 2 : "
  "une URL par parcours, ~100 parcours) que si la pilier performe. Jamais des centaines de pages d'un "
  "coup : on valide le modèle sur un échantillon, puis on industrialise."),
]:
    st.append(Paragraph(h,S["h3"])); st.append(P(b))

st.append(Paragraph("Les outils (« skills ») mobilisés", S["h1"]))
st.append(P("Chaque étape de la stratégie s'appuie sur un outil dédié. Ce sont des assistants spécialisés, "
   "chacun avec un rôle précis. Voici, dans l'ordre où on les utilise, ce que fait chacun, à quel moment, "
   "et ce qu'il faut lui fournir pour qu'il travaille."))

SKILL_CARDS=[
 ("/seo-quick-win",
  "Repère les pages déjà proches du top 3 (positions 3 à 12) qui reçoivent beaucoup d'affichages mais "
  "peu de clics. Ce sont les gains les plus rapides : on optimise l'existant avant de créer.",
  "Dès qu'on a les données Search Console du site.",
  "Un export Search Console (fichier CSV)."),
 ("/seo-modeles-pseo",
  "Trouve les pages « business » à créer autour d'une page de vente, à partir des requêtes qu'un client "
  "tape vraiment quand il est sur le point de décider.",
  "Pour choisir quelles pages valent le coup, avant d'en produire des centaines.",
  "La page de vente visée et l'action qu'on attend du visiteur (achat, devis, contact)."),
 ("/seo-roadmap-pseo",
  "Met les pages à produire dans l'ordre, sur un plan d'exécution daté et priorisé.",
  "Une fois les modèles de pages choisis, pour planifier le déploiement.",
  "La liste des modèles de pages retenus."),
 ("/seo-entites-vectorielles",
  "Liste tout ce qu'une page doit contenir pour que Google et les IA la reconnaissent comme experte du "
  "sujet : le bon vocabulaire, les chiffres, le format attendu, l'angle que personne d'autre n'a.",
  "Avant de rédiger une page, ou pour auditer une page existante.",
  "La requête visée (par exemple « calculer son index de golf »)."),
 ("/seo-preparation-semantique",
  "Donne la carte complète de ce qu'une page doit couvrir sur un sujet. En mode audit, il prend une page "
  "existante et liste précisément ce qui lui manque.",
  "Au moment de cadrer une page, en création comme en correction.",
  "La requête (création) ou la page existante à auditer (audit)."),
 ("/seo-product-led-seo",
  "Conçoit des outils interactifs (calculateur, simulateur, quiz, comparateur) qui captent les requêtes "
  "où l'internaute veut faire quelque chose, pas seulement lire.",
  "Pour transformer une page de texte en page-outil (par exemple le quiz « quelle balle pour vous »).",
  "La thématique et le besoin concret de l'utilisateur."),
 ("/seo-programmatique-pseo",
  "Conçoit un système de pages en série : un seul modèle, une variable qui change, et des centaines de "
  "pages uniques qui se positionnent chacune sur une requête de longue traîne.",
  "Quand on veut couvrir une verticale à grande échelle (une page par parcours de golf, par exemple).",
  "La verticale visée et la base de données qui fait varier les pages (les ~40 parcours)."),
]
for cmd, what, when, inp in SKILL_CARDS:
    for f in skill_card(cmd, what, when, inp): st.append(f)

st.append(Paragraph("Trouver ces mots-clés avec Fusionn", S["h1"]))
st.append(P("Une fois Fusionn branché, repérer les bonnes requêtes ne se fait plus à la main. Ce qu'on a "
   "fait sur Golfiller (lire la donnée, repérer ce qui marche, le répliquer), l'outil l'enchaîne onglet "
   "par onglet."))
# capture : synthèse "Ce qu'il faut retenir"
for fl in shot("synth_p.png", 150, "Sortie Fusionn : la synthèse « Ce qu'il faut retenir » résume les "
               "sujets à couvrir, les outils et les objections en tête de résultats."): st.append(fl)

st.append(Paragraph("1. Lancer la recherche sur la verticale", S["h3"]))
st.append(P("Quelques mots de départ suffisent (« balle de golf occasion », « index golf », « slope "
   "parcours »). Si la propriété Search Console de golfiller.fr est reliée, le classement des requêtes "
   "part directement des vraies données du site."))
st.append(Paragraph("2. Onglet Mots-clés : garder ce qui convertit", S["h3"]))
st.append(P("La liste arrive notée, avec l'intention de chaque requête et son regroupement par sujet. On "
   "garde celles où l'internaute veut agir (calculer son index, comparer deux balles), on écarte les "
   "requêtes purement informatives, déjà absorbées par les réponses IA de Google."))
for fl in shot("table_p.png", 152, "Onglet Mots-clés : chaque requête est notée, étiquetée selon "
               "l'intention, et regroupée par sujet."): st.append(fl)
st.append(Paragraph("3. Onglet Micro-intentions : couvrir toutes les sous-questions", S["h3"]))
st.append(P("Il découpe le sujet en sous-questions réelles : slope, index, compression, distance par "
   "club. C'est ce qui permet de traiter le sujet en entier et de repérer les angles que personne "
   "n'a couverts."))
st.append(Paragraph("4. Onglet Outils : les formats interactifs à créer", S["h3"]))
st.append(P("Il propose les outils adaptés à chaque requête : calculateur, comparateur, quiz. Ce sont "
   "exactement les opportunités listées plus haut."))
st.append(Paragraph("5. Onglet Stratégie programmatique : les lots de pages à produire", S["h3"]))
st.append(P("Il regroupe les pages à produire en lots, classés par priorité, les plus rentables d'abord. "
   "C'est la mise en pratique du « 1 modèle + 1 variable = N pages » : une page par parcours, par balle, "
   "par profil."))
# capture : navigation du workspace (les onglets, par groupe)
for fl in shot("nav_p.png", 56, "La navigation du workspace, organisée en trois temps : Comprendre, "
               "Produire, Décider."): st.append(fl)
st.append(Spacer(1,2))
st.append(box(CW,"Ce que Fusionn ne fait pas à ta place",
   "Choisir la verticale défendable, injecter la data propriétaire (relevés clients, base parcours), "
   "trancher la Haute Surprise. Ce qu'il fait : le travail répétitif de croiser donnée, intention et "
   "sémantique pour faire remonter les requêtes « Do » qu'on aurait ratées à la main, et les ranger en "
   "lots prêts à produire."))

# ---- Bloc auteur : photo + liens réseaux sociaux ---------------------------
_LK='<a href="%s"><font color="#1155CC">%s</font></a>'
_links="     ·     ".join([
    _LK % ("https://www.linkedin.com/in/timothee-boussardon/", "LinkedIn"),
    _LK % ("https://algorithme.substack.com/", "Substack — newsletter Algorithme"),
    _LK % ("https://www.youtube.com/@ethicseo", "YouTube"),
])
_av=Image(os.path.join(SHOTS,"tim.png"), width=24*mm, height=24*mm); _av.hAlign="CENTER"
_txt=[
    Paragraph("Timothée Boussardon",
              ParagraphStyle("an",parent=S["body"],fontName=SANS_B,fontSize=12.5,leading=15,spaceAfter=1)),
    Paragraph("Consultant SEO IA · Organikk · organikk.co",
              ParagraphStyle("ar",parent=S["body"],fontSize=9.5,textColor=GREY,leading=13,spaceAfter=6)),
    Paragraph(_links, ParagraphStyle("al",parent=S["body"],fontSize=9.5,leading=14)),
]
_card=Table([[_av,_txt]], colWidths=[30*mm, CW-30*mm])
_card.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("BACKGROUND",(0,0),(-1,-1),BOXBG),("BOX",(0,0),(-1,-1),0.75,GRID),
    ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),10),
    ("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12),
]))
st.append(CondPageBreak(44*mm))
st.append(HRFlowable(width="100%", thickness=0.75, color=GRID, spaceBefore=16, spaceAfter=12))
st.append(_card)

doc.build(st)
print("OK ->", OUT)
