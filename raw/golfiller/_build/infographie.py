# -*- coding: utf-8 -*-
"""Infographie Golfiller pour la newsletter / LinkedIn / X. Sortie PNG portrait."""
from PIL import Image, ImageDraw, ImageFont

W,H = 1080, 2160
BG_TOP=(9,13,24); BG_BOT=(12,20,40)
WHITE=(244,247,252); MUTED=(138,147,168); FAINT=(92,102,124)
ACCENT=(37,227,152)      # vert menthe vif
CARD=(20,27,46); CARDBRD=(38,48,74)
LINE=(34,43,68)

F="/System/Library/Fonts/Supplemental/"
def font(name,size): return ImageFont.truetype(F+name, size)
BLACK=lambda s: font("Arial Black.ttf", s)
BOLD =lambda s: font("Arial Bold.ttf", s)
REG  =lambda s: font("Arial.ttf", s)

img=Image.new("RGB",(W,H),BG_TOP); d=ImageDraw.Draw(img)
# fond dégradé vertical
for y in range(H):
    t=y/H
    d.line([(0,y),(W,y)], fill=tuple(int(BG_TOP[i]+(BG_BOT[i]-BG_TOP[i])*t) for i in range(3)))
# halo léger en haut
glow=Image.new("L",(W,H),0); gd=ImageDraw.Draw(glow)
gd.ellipse([-300,-500,700,500], fill=40)
img.paste(Image.new("RGB",(W,H),ACCENT), (0,0), glow.point(lambda p:int(p*0.18)))
d=ImageDraw.Draw(img)

M=84
def tw(s,f): b=d.textbbox((0,0),s,font=f); return b[2]-b[0]
def th(s,f): b=d.textbbox((0,0),s,font=f); return b[3]-b[1]
def text(x,y,s,f,fill=WHITE,spacing=0):
    if spacing==0:
        d.text((x,y),s,font=f,fill=fill); return
    cx=x
    for ch in s:
        d.text((cx,y),ch,font=f,fill=fill); cx+=tw(ch,f)+spacing
def center(y,s,f,fill=WHITE):
    d.text(((W-tw(s,f))/2,y),s,font=f,fill=fill)
def rrect(box,r,fill=None,outline=None,wd=1):
    d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=wd)

# barre d'accent haut
d.rectangle([0,0,W,10],fill=ACCENT)

# kicker
y=78
d.ellipse([M,y+6,M+16,y+22],fill=ACCENT)
text(M+30,y,"ALGORITHME  ·  CAS CLIENT",BOLD(24),MUTED,spacing=3)

# titre
y=150
d.text((M,y),"Golfiller passe",font=BLACK(74),fill=WHITE); y+=88
d.text((M,y),"devant les géants",font=BLACK(74),fill=WHITE); y+=88
d.text((M,y),"de sa catégorie.",font=BLACK(74),fill=WHITE); y+=104
d.text((M,y),"Sans acheter un seul lien.",font=BLACK(46),fill=ACCENT); y+=92

# sous-titre
d.text((M,y),"Search Console, 3 derniers mois. Chiffres réels, rien d'arrondi.",
       font=REG(26),fill=MUTED); y+=70

# grille de stats 2x2
stats=[("9 600","clics en 3 mois"),
       ("233 000","impressions"),
       ("11 %+","CTR des pages-outils  (≈4 % sur le site)"),
       ("0","lien acheté")]
gx=M; gy=y; gw=(W-2*M-28)//2; gh=190
for i,(num,lab) in enumerate(stats):
    cxp=gx+(i%2)*(gw+28); cyp=gy+(i//2)*(gh+24)
    rrect([cxp,cyp,cxp+gw,cyp+gh],22,fill=CARD,outline=CARDBRD,wd=2)
    d.text((cxp+34,cyp+34),num,font=BLACK(72),fill=ACCENT)
    # label éventuellement sur 2 lignes
    f=REG(25); words=lab.split(); cur=""; lines=[]
    for w in words:
        t=(cur+" "+w).strip()
        if tw(t,f)<=gw-68: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur)
    ly=cyp+128
    for ln in lines[:2]:
        d.text((cxp+34,ly),ln,font=f,fill=MUTED); ly+=30
y=gy+2*gh+24+60

# bloc contraste
d.text((M,y),"ON VOUS DIT",font=BOLD(26),fill=FAINT)
d.text((W/2+20,y),"CE QUE JE FAIS",font=BOLD(26),fill=ACCENT); y+=54
rows=[("Acheter des liens","Des pages qu'on utilise"),
      ("Publier toujours plus","Des pages qui font une action"),
      ("Copier le top 10","Dire ce que les autres taisent")]
for a,b in rows:
    d.line([(M,y-10),(W-M,y-10)],fill=LINE,width=2)
    d.text((M,y+8),a,font=REG(30),fill=MUTED)
    d.text((W/2-30,y+6),"→",font=BOLD(30),fill=FAINT)
    d.text((W/2+20,y+8),b,font=BOLD(30),fill=WHITE); y+=64
y+=40

# bandeau "l'actu confirme"
rrect([M,y,W-M,y+232],22,fill=(15,22,40),outline=CARDBRD,wd=2)
d.text((M+34,y+28),"L'ACTU CONFIRME",font=BOLD(24),fill=ACCENT)
acts=["CTR en position 1 : 27 %  →  11 %",
      "Pages avec tableau : +25,7 % de citations par les IA",
      "Trafic IA : 0,5 % des visites, mais 12 % des inscriptions"]
ay=y+76
for a in acts:
    d.ellipse([M+34,ay+10,M+44,ay+20],fill=ACCENT)
    d.text((M+60,ay),a,font=REG(27),fill=WHITE); ay+=48
d.text((M+34,y+232-2-4),"",font=REG(10),fill=MUTED)
y+=232+18
d.text((M,y),"Sources : Search Engine Land · AirOps · Pew Research · Ahrefs",
       font=REG(20),fill=FAINT); y+=70

# footer
d.line([(M,y),(W-M,y)],fill=LINE,width=2); y+=30
d.text((M,y),"Le bootcamp SEO IA reprend le 1ᵉʳ juillet.  16 places.",font=BOLD(30),fill=WHITE); y+=44
d.text((M,y),"organikk.co/bootcamp",font=BOLD(30),fill=ACCENT); y+=58
d.text((M,y),"Timothée Boussardon  ·  Organikk  ·  newsletter Algorithme",font=REG(24),fill=MUTED)

import os
out=os.path.join(os.path.dirname(__file__),"infographie-golfiller.png")
img.save(out)
print("OK",out, img.size)
