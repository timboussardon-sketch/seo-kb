# -*- coding: utf-8 -*-
# =====================================================================
# TEMPLATE EMAIL — Newsletter IA (design validé par Tim le 2026-07-15)
# Édition de référence : _EXEMPLE-2026-07-15-google-offensive-overview.html
# Envoyée à 100 inscrits Qadence via l'edge function send-campaign.
#
# DESIGN À CONSERVER pour les prochaines éditions :
#  - Titre H1 en dégradé vert Qadence (fallback vert plein #0E7A43 dans Gmail)
#  - Sections + étoiles en vert #1E9E5A ; barème ★ en tête
#  - « En résumé » en puces « : » (JAMAIS de tiret cadratin —, banni)
#  - Blocs « Pourquoi c'est important » : italique + fond vert clair dégradé
#  - Bloc SOURCES obligatoire, un lien réel par info (jamais de chiffre non sourcé)
#  - CTA = simple LIEN souligné « Tester Qadence → » (PAS de bouton :
#    Gmail supprime le fond CSS des boutons → texte blanc invisible)
#  - Styles 100% inline + tables ; font-family en guillemets SIMPLES
#
# POUR ENVOYER (voir mémoire reference_qadence_campagnes_email) :
#  1. Éditer le contenu (résumé, sujet, sources) dans ce fichier, exécuter
#     → produit un HTML dans SP. RETIRER le <link> Google Fonts pour l'envoi
#       (interdit en mail) et pointer le désabonnement vers un mail qui reçoit.
#  2. Régénérer CAMPAIGN_SECRET (supabase secrets set --project-ref ytgbnqqmcnhmscbvhoin)
#  3. POST {SUPABASE_URL}/functions/v1/send-campaign
#     headers: Authorization Bearer <service_role>, apikey, x-campaign-secret
#     body: { subject, html, recipients[], from:"Qadence <hello@qadence.io>",
#             reply_to:"tim.boussardon@gmail.com" }
#  Audience = 100 derniers inscrits joignables (union auth.users + google_connections,
#  hors @qadence.io / anonymes / désabonnés) — requête SQL via Management API.
# =====================================================================
import pathlib
SP = pathlib.Path("/private/tmp/claude-501/-Users-timothee/4bffcce3-a46c-4490-8d00-843e3b063e40/scratchpad")

INK="#14182b"; MUTED="#5a6681"; BLUE="#2559DD"; GOLD="#E8A317"
GREEN="#1E9E5A"; GREEN_DEEP="#0E7A43"
GRAD="linear-gradient(135deg,#0E7A43 0%,#1E9E5A 50%,#37c07d 100%)"
LINE="#e6e8ee"; HL="#f4f7ff"; BG="#f4f5f7"
FF="'Geist',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"

def grad_text(txt, extra=""):
    return (f'<span style="background:{GRAD};-webkit-background-clip:text;background-clip:text;'
            f'-webkit-text-fill-color:transparent;color:{GREEN_DEEP};{extra}">{txt}</span>')

def p(txt, size=15, color=INK, mt=0, mb=16, lh="1.6", weight="400"):
    return (f'<p style="margin:{mt}px 0 {mb}px;font-family:{FF};font-size:{size}px;'
            f'line-height:{lh};color:{color};font-weight:{weight}">{txt}</p>')

def h_section(txt):
    return (f'<p style="margin:0 0 20px;font-family:{FF};font-size:13px;letter-spacing:.09em;'
            f'text-transform:uppercase;color:{GREEN_DEEP};font-weight:700">{grad_text(txt)}</p>')

def h2(txt, stars=""):
    st = (f'<span style="color:{GREEN};font-size:14px;white-space:nowrap;letter-spacing:1px">&nbsp;&nbsp;{stars}</span>'
          if stars else "")
    return (f'<h2 style="margin:0 0 14px;font-family:{FF};font-size:20px;line-height:1.3;'
            f'color:{GREEN_DEEP};font-weight:700">{grad_text(txt)}{st}</h2>')

def why(inner):
    green_solid = "#edf8f0"
    green_grad = "linear-gradient(135deg,#eef9f2 0%,#e2f4ea 55%,#dcf1e6 100%)"
    green_label = "#1E9E5A"
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:6px 0 4px">'
            f'<tr><td style="background:{green_solid};background:{green_grad};'
            f'border-radius:12px;padding:18px 20px">'
            f'<p style="margin:0 0 10px;font-family:{FF};font-size:12px;letter-spacing:.06em;'
            f'text-transform:uppercase;color:{green_label};font-weight:700">Pourquoi c\'est important</p>'
            f'<div style="font-style:italic">{inner}</div></td></tr></table>')

def divider():
    return f'<tr><td style="padding:34px 0"><div style="height:1px;background:{LINE};line-height:1px">&nbsp;</div></td></tr>'

def b(t): return f'<strong style="color:{INK};font-weight:700">{t}</strong>'

# ---------- CONTENT ----------
rows = []

# EN RÉSUMÉ (resserré, en tirets, sans gras)
def dash(txt, mb=12):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 {mb}px">'
            f'<tr><td valign="top" style="font-family:{FF};font-size:15px;line-height:1.6;color:{INK};'
            f'padding-right:8px;width:14px">:</td>'
            f'<td valign="top" style="font-family:{FF};font-size:15px;line-height:1.6;color:{INK}">{txt}</td>'
            f'</tr></table>')

rows.append(h_section("En résumé"))
rows.append(dash("Depuis le 10 juillet, Google place une réponse générée par Gemini 3.5 Flash en tête de presque toutes les recherches. Les liens organiques restent affichés, mais sous cette réponse."))
rows.append(dash("Google cite surtout Reddit (≈21 %) et YouTube (≈19 %), loin devant les sites de marques (Ahrefs, juin 2026)."))
rows.append(dash("Les premières pertes tombent déjà : HubSpot -70 à -80 % de trafic organique, Chegg -49 %, DMG Media jusqu'à -89 % sur certaines requêtes."))
rows.append(dash("L'objectif du SEO se déplace : devenir la source que Google cite, pas seulement le premier lien.", mb=20))
star=lambda s: f'<span style="color:{GREEN};letter-spacing:1px">{s}</span>'
rows.append(p(f'{star("★★★★★")} impact majeur&nbsp;&middot;&nbsp; {star("★★★☆☆")} à surveiller &nbsp;&middot;&nbsp; {star("★☆☆☆☆")} information secondaire',
              size=13, color=MUTED, mb=0))

resume = "".join(rows)

# LE SUJET DU JOUR
sujet = []
sujet.append(h_section("Le sujet du jour"))
sujet.append(h2("Google fait désormais répondre l'IA avant les sites", "★★★★★"))
sujet.append(p(f"Depuis le {b('10 juillet')}, Google affiche une réponse générée par {b('Gemini 3.5 Flash')} en tête de la majorité des recherches. Cette fonctionnalité n'est plus réservée à l'onglet AI Mode : elle est désormais intégrée directement aux résultats classiques."))
sujet.append(p("Pour Google, il s'agit de la plus grande évolution de son moteur de recherche depuis 25 ans."))
sujet.append(p("Conséquence immédiate : les liens organiques ne disparaissent pas, mais ils sont repoussés sous la réponse IA. Sur de nombreuses recherches, ils ne sont même plus visibles sans faire défiler la page."))
sujet.append(p("Autre changement important : les internautes ne cherchent plus avec deux ou trois mots-clés. Ils posent désormais des questions complètes, souvent très précises. Les contenus optimisés uniquement autour d'une expression exacte risquent donc de perdre en visibilité."))
sujet.append(p(f"Les premiers impacts sont déjà visibles. HubSpot évoque une perte de {b('70 à 80 % de trafic organique')}, Chegg annonce {b('-49 %')}, tandis que DMG Media mesure jusqu'à {b('-89 %')} sur certaines requêtes. En parallèle, plusieurs éditeurs ont engagé une procédure contre Google au Royaume-Uni et DuckDuckGo affirme avoir enregistré {b('75 % d\'installations supplémentaires')} depuis les annonces de Google."))
sujet.append(why(
    p("Pendant des années, le SEO consistait à obtenir un clic.", mb=10) +
    p(f"Aujourd'hui, il faut d'abord obtenir une {b('citation')}.", mb=10) +
    p("Le vrai enjeu n'est plus uniquement de positionner une page en première position, mais de produire le contenu que Google jugera suffisamment fiable pour l'intégrer directement dans sa réponse.", mb=0)
))
sujet_html = "".join(sujet)

# SOURCES CITÉES
src = []
src.append(h2("Du coup, quelles sources Google choisit-il de citer dans les Overviews&nbsp;?", "★★★★☆"))
src.append(p("Une étude d'Ahrefs publiée en juin montre un constat assez surprenant : les sites les plus cités par les AI Overviews ne sont pas les grandes entreprises."))
src.append(p(f"En tête figurent {b('Reddit')}, puis {b('YouTube')}, devant Wikipédia et même le blog officiel de Google."))
src.append(p("Autrement dit, Google privilégie très souvent des contenus issus de communautés ou de créateurs plutôt que des pages marketing soigneusement optimisées."))
src.append(p(f"La concentration est également très forte : selon Semrush, {b('les 20 domaines les plus cités représentent près des deux tiers des citations')}."))
src.append(p("Sur Reddit, les contenus qui ressortent le plus sont rarement les commentaires rapides. Ce sont plutôt des réponses détaillées, appuyées sur une expérience concrète, avec des exemples et des données."))
src.append(why(
    p("Être cité par une IA suit des règles orientées expérience client bien plus que du SEO Google. L'expérience vécue, les explications détaillées et les réponses utiles prennent de plus en plus de poids.", mb=12) +
    '<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0"><tr><td style="padding:0 0 8px">'
    + p("&#8226;&nbsp; Développer une présence là où l'IA va chercher ses informations (Reddit, YouTube&hellip;).", mb=0) +
    '</td></tr><tr><td>' +
    p("&#8226;&nbsp; Rédiger des contenus qui répondent réellement à une question, plutôt que des pages seulement pensées pour promouvoir un produit.", mb=0) +
    '</td></tr></table>'
))
src_html = "".join(src)

# EN BREF
def brief(stars, title, body):
    return (p(f'<span style="color:{GREEN};letter-spacing:1px">{stars}</span>&nbsp; {b(title)} {body}', mb=18))

bref = []
bref.append(h_section("En bref"))
bref.append(brief("★★★★★","Les éditeurs encaissent déjà le choc.",
    f"HubSpot annonce une baisse de {b('70 à 80 %')} de son trafic organique, Chegg {b('-49 %')}, et DMG Media jusqu'à {b('-89 %')} sur certaines requêtes. Plusieurs médias britanniques ont aussi déposé une plainte contre Google."))
bref.append(brief("★★★☆☆","Les LLMs redistribuent les cartes.",
    "Selon StatCounter, ChatGPT enregistre son niveau le plus bas en part de trafic référent, tandis que Gemini devient le deuxième LLM générateur de trafic devant Perplexity, qui recule. Si tu travailles ton GEO, mieux vaut diversifier ta présence que tout miser sur un seul LLM."))
bref.append(brief("★★☆☆☆","DuckDuckGo progresse.",
    f"Le moteur revendique {b('75 % d\'installations supplémentaires')} depuis les annonces de Google. Le mouvement reste limité, mais la recherche commence à se diversifier au-delà de Google."))
bref_html = "".join(bref)

# SOURCES (liens réels vérifiés)
SOURCES = [
 ("Google", "réponse Gemini 3.5 Flash en tête des recherches depuis le 10 juillet", "https://blog.google/products/search/ai-mode-search/"),
 ("Ahrefs (juin 2026)", "domaines les plus cités dans les AI Overviews (Reddit 21 %, YouTube 18,8 %)", "https://ahrefs.com/blog/most-cited-domains-ai-overviews/"),
 ("Semrush", "concentration des citations : le top 20 des domaines = 66 %", "https://www.semrush.com/blog/most-cited-domains-ai/"),
 ("Search Engine Land", "chute du trafic organique de HubSpot (-70 à -80 %)", "https://searchengineland.com/hubspot-seo-organic-traffic-drop-451096"),
 ("Tomasz Tunguz", "chute du trafic de Chegg (-49 %)", "https://tomtunguz.com/chegg-aio/"),
 ("Press Gazette", "DMG Media -89 % et plainte des éditeurs devant la CMA", "https://pressgazette.co.uk/platforms/uk-publishers-urge-cma-to-curb-google-in-uk-as-search-giant-ai-does-them-no-harm/"),
 ("TechCrunch", "hausse des installations de DuckDuckGo après le virage IA de Google", "https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/"),
 ("StatCounter", "parts de trafic référent des LLM (ChatGPT au plus bas, Gemini 2ᵉ)", "https://gs.statcounter.com/press/google-gemini-overtakes-perplexity-to-become-second-largest-source-of-ai-chatbot-referrals-to-websites"),
]
src_rows = []
src_rows.append(h_section("Sources"))
for name, claim, url in SOURCES:
    src_rows.append(
        f'<p style="margin:0 0 10px;font-family:{FF};font-size:13px;line-height:1.55;color:{MUTED}">'
        f'<a href="{url}" style="color:{GREEN_DEEP};text-decoration:none;font-weight:600">{name}</a> '
        f': {claim}</p>')
sources_html = "".join(src_rows)

# ---------- SHELL ----------
html = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light only">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<title>Newsletter IA</title></head>
<body style="margin:0;padding:0;background:{BG};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{BG};">
<tr><td align="center" style="padding:28px 12px 48px;">
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;">

    <!-- title -->
    <tr><td align="center" style="padding:4px 6px 26px;">
      <div style="font-family:{FF};font-size:25px;font-weight:800;letter-spacing:-.02em;line-height:1.2;color:{GREEN_DEEP}">{grad_text("Google lance son offensive Overview")}</div>
    </td></tr>

    <tr><td style="background:#ffffff;border:1px solid {LINE};border-radius:18px;padding:34px 34px 40px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
        <tr><td>{resume}</td></tr>
        {divider()}
        <tr><td>{sujet_html}</td></tr>
        {divider()}
        <tr><td>{src_html}</td></tr>
        {divider()}
        <tr><td>{bref_html}</td></tr>
        {divider()}
        <tr><td>{sources_html}</td></tr>
        <tr><td align="center" style="padding-top:34px">
          <a href="https://qadence.io" style="color:{GREEN_DEEP};font-family:{FF};font-size:16px;font-weight:700;text-decoration:underline">Tester Qadence&nbsp;&rarr;</a>
        </td></tr>
      </table>
    </td></tr>

    <!-- footer -->
    <tr><td style="padding:24px 8px 0;font-family:{FF};font-size:12px;line-height:1.6;color:{MUTED};text-align:center">
      Tu reçois cet email parce que tu es abonné à la Newsletter IA de Tim Boussardon (Organikk).<br>
      <a href="{{{{unsubscribe_url}}}}" style="color:{MUTED};text-decoration:underline">Se désabonner</a>
    </td></tr>

  </table>
</td></tr></table>
</body></html>"""

out = SP/"newsletter-ia.html"
out.write_text(html, encoding="utf-8")
print("written", out, len(html), "chars")
