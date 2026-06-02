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
   "Objectif : bâtir une autorité thématique sur une verticale de niche défendable, les balles de golf "
   "d'occasion, plutôt qu'un affrontement frontal avec les gros acteurs. Résultat : 1re position sur "
   "« balle de golf », devant Décathlon et Amazon, sans acheter un seul lien."))
st.append(P("État : projet pSEO actif sur les requêtes slope et handicap, base de ~40 parcours français "
   "(slope + SSS), calculateur de handicap interactif (formule FFGolf), page HTML sémantique brute "
   "(calculateur + tableau filtrable + sections par parcours). À venir : extension à ~100 parcours, "
   "Phase 2 pSEO (une URL par parcours) si la pilier performe."))

st.append(Paragraph("Analyse GSC : les pages winners", S["h1"]))
st.append(P("Les trois pages qui sur-performent partagent toutes l'intention « Do » (calculer, comparer, "
   "consulter). Ce sont des vecteurs multimodaux qu'aucun LLM ne remplace sur la page. Le réflexe "
   "transférable : lire la GSC, isoler le pattern des winners, le répliquer."))
# résumé chiffré sous forme de petit tableau (doc-like)
sumrows=[[Paragraph("Pages winners",S["th"]),Paragraph("Clics cumulés",S["th"]),
          Paragraph("Impressions (data connue)",S["th"])],
         [Paragraph("3 — toutes en intention Do",S["td"]),Paragraph("8 798",S["td"]),
          Paragraph("100 937+",S["td"])]]
st.append(TABLE(sumrows,[CW*0.40,CW*0.28,CW*0.32]))
st.append(Spacer(1,8))
st.append(Paragraph("Clics par page (12 derniers mois)", S["h3"]))
st.append(HBar(CW,[("Tableau comparatif de compression des balles",5652),
                   ("Calcul d'index de golf",1816),
                   ("Quiz « Quelle balle pour vous ? »",1330)]))
st.append(P("Reconstruction graphique à partir des chiffres GSC cités dans le doc source. Ce n'est pas "
   "une capture d'écran : positions associées 7,17 / 11,77 / 8,45.","cap"))
st.append(Spacer(1,6))
rows=[[Paragraph(x,S["th"]) for x in ["Page","Clics","Position","Impressions","Intention"]]]
for r in [("Tableau comparatif de compression","5 652","7,17","—","Consulter pour décider"),
          ("Calcul d'index de golf","1 816","11,77","77 786","Calculer son index"),
          ("Quiz « Quelle balle pour vous ? »","1 330","8,45","23 151","Profiler / décider"),
          ("Slope de votre golf","—","—","—","Consulter une valeur")]:
    rows.append([Paragraph(r[0],S["tdb"])]+[Paragraph(x,S["td"]) for x in r[1:]])
st.append(TABLE(rows,[CW*0.34,CW*0.12,CW*0.13,CW*0.18,CW*0.23]))
st.append(Spacer(1,6))
st.append(box(CW,"Lecture doctrinale",
   "Les « Do » gagnent parce qu'ils exigent un format (outil, calculateur, tableau) qu'un LLM ne peut pas "
   "exécuter à la place de l'utilisateur. Les « Know » informationnels se font manger par les AI "
   "Overviews ; les « Do » résistent. C'est la traduction concrète de l'anti-ChatGPT."))

st.append(Paragraph("La stratégie lue à travers la doctrine", S["h1"]))
st.append(Paragraph("1. Triade SERP : à quelle phase chaque move agit", S["h3"]))
st.append(bullets([
  "<b>Document Ranking.</b> On ne vise pas le head term tenu par les gros. On descend sur la verticale "
  "« balle de golf occasion » où le filtre d'admission est franchissable.",
  "<b>Passage Ranking.</b> Chaque page pSEO est faite pour que ses blocs Hn (150-200 mots) soient des "
  "vecteurs sémantiques denses, évalués seuls. Un tableau ou une section de parcours peut ranker seul.",
  "<b>Phase générative (citation IA).</b> Ranker ne suffit plus : il faut être cité. C'est là que jouent "
  "le Surprise Gap et l'Information Gain.",
]))
st.append(Paragraph("2. Know-Simple / Know / Do : pourquoi le « Do » gagne", S["h3"]))
st.append(P("Les pages winners sont toutes des « Do ». Une intention « Do » exige un format (outil, "
   "calculateur, tableau) qu'un LLM ne peut pas exécuter à la place de l'utilisateur. Les « Do » visent "
   "aussi le « Fully Meets » des Quality Raters."))
st.append(Paragraph("3. Entités vectorielles + Grounding Score", S["h3"]))
st.append(bullets([
  "<b>Entités techniques :</b> le vocabulaire obligatoire (slope, SSS, index, compression, carry).",
  "<b>Preuves quantitatives :</b> chiffres sourcés (Trackman, PGA Tour, FFGolf) au format chiffre + "
  "unité + contexte. Elles montent le Confidence Score de l'IA.",
  "<b>Vecteurs multimodaux :</b> le format attendu par une intention « Do ». Une page « Do » sans outil a "
  "un vecteur incomplet. C'est le Product-Led SEO.",
  "<b>Divergence (Haute Surprise) :</b> l'angle ou la data que le corpus n'a pas.",
]))
st.append(P("L'objectif n'est pas la proximité vectorielle maximale mais le Grounding Score optimal = "
   "proximité + divergence. Ni hors-sujet, ni redondant avec ce que le modèle sait déjà."))
st.append(Paragraph("4. Surprise Gap + Information Gain : ce qui fait citer", S["h3"]))
st.append(P("Apporter l'information manquante qui force le modèle à inclure la marque dans sa réponse. "
   "Chez Golfiller, la Haute Surprise vient de la data propriétaire agrégée des clients (distances réelles "
   "par profil, compression croisée) et d'angles contrariens. Benchmark GEO : citations verbatim sourcées "
   "= +41 % de visibilité, statistiques = +34 %. Test : si un concurrent recopie l'angle en 5 minutes, ce "
   "n'en est pas."))
st.append(Paragraph("5. RRF + micro-intentions et 6. Data propriétaire", S["h3"]))
st.append(P("Un cluster qui couvre toutes les sous-intentions (slope, index, compression, distance par "
   "club, choix de balle) améliore le score de fusion. Sans data unique injectée dans les pages, on "
   "retombe dans le corpus moyen de l'IA, donc dans la commodité. La data propriétaire alimente à la fois "
   "les preuves quantitatives, la Haute Surprise et les outils interactifs."))

st.append(Paragraph("Opportunités d'outils (vecteurs « Do »)", S["h1"]))
st.append(bullets([
  "<b>Calculette / simulateur d'index interactif.</b> /calcul-index-golf déjà à 1 816 clics, pos 11,77, "
  "77 786 impressions. Grappe captable ~20 000 imp/mois.",
  "<b>Quiz « Quelle balle pour vous ? ».</b> Page texte (1 330 clics, pos 8,45) à transformer en quiz. "
  "Conversion native, tech la plus simple.",
  "<b>Carte de score interactive / différentiel.</b> Carte digitale trou par trou + calcul auto + PDF.",
  "<b>Tableau de distance de clubs par profil.</b> Réplique du format « tableau » gagnant, filtrable. "
  "Haute Surprise : data agrégée clients.",
  "<b>Comparateur de balles côte à côte.</b> Rendre dynamique le tableau de compression. Bonus pSEO : "
  "URLs /comparer/pro-v1-vs-pro-v1x.",
]))
st.append(Paragraph("Priorisation", S["h3"]))
prio=[["Outil","Volume captable","Difficulté","ROI conversion","Prio"],
      ["Calculette index / handicap","~20k imp","Moyenne","Moyen","1"],
      ["Quiz « quelle balle »","~5k imp","Faible","Très fort","2"],
      ["Carte de score digitale","~2k imp","Moyenne","Faible","3"],
      ["Comparateur balles dynamique","~5k imp","Forte","Fort","4"],
      ["Tableau distance clubs","~1k imp","Faible","Faible","5"]]
prows=[[Paragraph(c,S["th"]) for c in prio[0]]]
for r in prio[1:]:
    prows.append([Paragraph(r[0],S["tdb"])]+[Paragraph(x,S["td"]) for x in r[1:]])
st.append(TABLE(prows,[CW*0.32,CW*0.19,CW*0.16,CW*0.21,CW*0.12],highlight=2))
st.append(Spacer(1,4))
st.append(P("Recommandation si un seul outil : le quiz « Quelle balle ». Tech simple, conversion directe, "
   "et il monte le CTR de la page texte existante qui plafonne en position 8,45."))

st.append(Paragraph("Créer un modèle de page et le lancer en production", S["h1"]))
st.append(P("La logique pSEO tient en une phrase : <b>1 template + 1 variable qui change = N pages "
   "uniques</b>, chacune sur une requête longue traîne. Le produit, c'est la combinaison base de données "
   "× structure de page, pas le texte écrit à la main."))
for h,b in [
 ("1. Choisir le modèle (template + variable)",
  "Le template « page parcours » se décline sur la variable « parcours » (base de ~40 parcours français : "
  "slope + SSS). Autres variables activables : la balle (comparateur), le profil (tableau de distances). "
  "Chaque combinaison vise une micro-intention distincte, ce qui évite la cannibalisation."),
 ("2. Garantir l'unicité réelle, pas le copier-coller",
  "Règle non négociable : plus de 70 % du contenu change entre deux pages, et la transformation porte sur "
  "le fond (slope, SSS, sections propres au parcours), pas seulement sur la variable. Une génération à "
  "variable bête se fait downgrader ou désindexer par le Helpful Content en quelques jours."),
 ("3. Injecter la data propriétaire",
  "La valeur vient des chiffres eux-mêmes (base parcours construite à la main, data clients agrégée), pas "
  "du commentaire. Stack APIs officielles, zéro scraping interdit. C'est ce qui alimente les preuves "
  "quantitatives, la Haute Surprise et le calculateur."),
 ("4. Construire en HTML sémantique brut",
  "Calculateur de handicap (formule FFGolf) + tableau filtrable + sections par parcours, balises natives "
  "uniquement, zéro CSS ni JS superflu. Objectif : chaque bloc Hn est un passage dense, rankable seul."),
 ("5. Lancer par paliers, piloté par la GSC",
  "Pilote d'abord (page pilier + base ~40 parcours), on mesure en Search Console, et on n'étend (Phase 2 : "
  "une URL par parcours, ~100 parcours) que si la pilier performe. Jamais des centaines de pages d'un "
  "coup : on valide le modèle sur un échantillon, puis on industrialise."),
]:
    st.append(Paragraph(h,S["h3"])); st.append(P(b))

st.append(Paragraph("Les skills à utiliser", S["h1"]))
st.append(P("Chaque étape, du cadrage du modèle à la page, a son skill. Vous ne les avez pas : ils sont "
   "donc reproduits ici en intégralité, tels quels. Pour chacun : quand le déclencher, la doctrine, les "
   "inputs requis, le pipeline complet et les règles. Vous pouvez les appliquer directement, à la main ou "
   "via votre propre assistant."))

SKILL_FILES=[
 ("/seo-programmatique-pseo","seo-programmatique-pseo"),
 ("/seo-modeles-pseo","seo-modeles-pseo"),
 ("/seo-roadmap-pseo","seo-roadmap-pseo"),
 ("/seo-product-led-seo","seo-product-led-seo"),
 ("/seo-entites-vectorielles","seo-entites-vectorielles"),
 ("/seo-preparation-semantique","seo-preparation-semantique"),
 ("/seo-quick-win","seo-quick-win"),
]
for cmd, folder in SKILL_FILES:
    path=os.path.join(SKILLS_DIR, folder, "SKILL.md")
    try:
        txt=open(path, encoding="utf-8").read()
    except Exception:
        continue
    st.append(CondPageBreak(70*mm))
    st.append(HRFlowable(width="100%", thickness=0.75, color=GRID, spaceBefore=10, spaceAfter=6))
    st.append(Paragraph("<font name='Courier' color='#1155CC'>%s</font>"%cmd, S["h2"]))
    for f in render_md(txt): st.append(f)

st.append(Paragraph("Trouver ces mots-clés avec Fusionn", S["h1"]))
st.append(P("Le repérage des requêtes « Do » n'a rien d'artisanal une fois Fusionn branché. Le réflexe "
   "transférable du cas Golfiller (lire la donnée, isoler le pattern des winners, le répliquer) est "
   "précisément ce que l'outil enchaîne, onglet par onglet."))
# capture : synthèse "Ce qu'il faut retenir"
for fl in shot("synth_p.png", 150, "Sortie Fusionn : la synthèse « Ce qu'il faut retenir » résume clusters, "
               "outils et objections en tête de résultats."): st.append(fl)

st.append(Paragraph("1. Lancer la recherche sur la verticale", S["h3"]))
st.append(P("Seed minimal (« balle de golf occasion », « index golf », « slope parcours »). Si la "
   "propriété GSC golfiller.fr est branchée (sélecteur de propriété), le scoring part de la vraie data "
   "du site."))
st.append(Paragraph("2. Onglet Mots-clés → trier le Do du Know", S["h3"]))
st.append(P("La liste qualifiée arrive avec sa pertinence, son intention et son cluster. On garde le "
   "décisionnel (calculer, comparer, consulter), on écarte l'informationnel que les AI Overviews vont "
   "manger."))
for fl in shot("table_p.png", 152, "Onglet Mots-clés : chaque requête notée en pertinence et taggée "
               "Do / Know, regroupée par cluster."): st.append(fl)
st.append(Paragraph("3. Onglet Micro-intentions → couvrir la grappe", S["h3"]))
st.append(P("Il éclate le sujet en sous-intentions réelles (slope, index, compression, distance par "
   "club). La matière du RRF et le repérage des trous que personne n'adresse."))
st.append(Paragraph("4. Onglet Outils → sortir les vecteurs multimodaux", S["h3"]))
st.append(P("Il propose les formats « Do » associés (calculateur, comparateur, quiz). Le Product-Led "
   "sorti de force, exactement les opportunités listées plus haut."))
st.append(Paragraph("5. Onglet Stratégie programmatique → lots de pages", S["h3"]))
st.append(P("Les playbooks regroupent les pages à produire en lots scorés et priorisés (P0 d'abord). La "
   "traduction directe de « 1 template + 1 variable = N pages » : une URL par parcours, par balle, par "
   "profil."))
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
