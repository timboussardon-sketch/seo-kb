/* ALGORITHME · header + ticker + footer partagés (injectés sur chaque page) */
(function(){
  var DATE = "Mardi 30 juin 2026";
  var EDITION = "N° 412";

  var SECTIONS = [
    {k:"le-fil",     label:"Le fil",       href:"le-fil.html"},
    {k:"google",     label:"Google",       href:"rubrique-google.html"},
    {k:"moteurs-ia", label:"Moteurs IA",   href:"rubrique-moteurs-ia.html"},
    {k:"etudes",     label:"Études",       href:"rubrique-etudes.html"},
    {k:"outils",     label:"Outils",       href:"rubrique-outils.html"},
    {k:"analyses",   label:"Analyses",     href:"rubrique-analyses.html"},
    {k:"stat",       label:"La stat du jour", href:"stat-du-jour.html"}
  ];

  var TICKER = [
    ['AI Overviews FR','38% ▲','up'],
    ['Volatilité SERP','4,8',''],
    ['Citations answer-first','×2,1 ▲','up'],
    ['Clic organique info.','-6,3% ▼','dn'],
    ['Core update juin','jour 10','']
  ];

  var active = document.body.getAttribute('data-nav') || '';
  var isHome = document.body.getAttribute('data-page') === 'home';

  function navHTML(cls){
    return SECTIONS.map(function(s){
      return '<a href="'+s.href+'"'+(s.k===active?' class="'+cls+'"':'')+'>'+s.label+'</a>';
    }).join('');
  }

  // ---- ticker ----
  var items = TICKER.map(function(t){
    return '<span>'+t[0]+'&nbsp;<b'+(t[2]?' class="'+t[2]+'"':'')+'>'+t[1].replace(/ /g,'&nbsp;')+'</b></span>';
  }).join('');
  var ticker =
    '<div class="console"><div class="wrap">'+
      '<span class="prompt">algorithme&nbsp;~&nbsp;$</span>'+
      '<div class="tk">'+items+items+'</div>'+
    '</div></div>';

  // ---- header ----
  var head;
  if(isHome){
    head =
    '<header class="mh"><div class="wrap mh-top">'+
      '<div class="c"><div class="mono ed">'+EDITION+'</div><div class="mono ed">Édition du matin</div></div>'+
      '<div class="c m">'+
        '<div class="mono kick" style="margin-bottom:6px">Le quotidien du Search &amp; de l\'intelligence artificielle</div>'+
        '<a class="brand" href="index.html">Algorithme<span class="d">.</span></a>'+
        '<div class="tagl">« Ce qui change aujourd\'hui dans la façon dont on sera trouvé demain. »</div>'+
      '</div>'+
      '<div class="c r"><div class="mono ed">'+DATE+'</div><div class="mono live"><span class="dot"></span> En direct</div></div>'+
    '</div><div class="wrap"><nav class="sec mono">'+navHTML('on')+'</nav></div></header>';
  } else {
    head =
    '<div class="site-head"><div class="wrap bar">'+
      '<a class="brand-sm" href="index.html">Algorithme<span class="d">.</span></a>'+
      '<nav>'+navHTML('on')+'</nav>'+
      '<div class="actions">'+
        '<a class="btn btn-ico" href="recherche.html" title="Rechercher" aria-label="Rechercher">⌕</a>'+
        '<a class="btn btn-accent" href="newsletter.html">S\'abonner</a>'+
      '</div>'+
    '</div></div>';
  }

  // ---- footer ----
  var rubFoot = SECTIONS.map(function(s){return '<a href="'+s.href+'">'+s.label+'</a>';}).join('');
  var foot =
  '<footer class="site-foot">'+
    '<div class="wrap foot-grid">'+
      '<div class="foot-brand">'+
        '<a class="brand" href="index.html">Algorithme<span class="d">.</span></a>'+
        '<span class="tagl">Le quotidien indépendant du Search, du SEO et de l\'intelligence artificielle.</span>'+
        '<div class="mono live"><span class="dot"></span> En direct · mis à jour '+DATE+'</div>'+
      '</div>'+
      '<div><h5>Rubriques</h5>'+rubFoot+'</div>'+
      '<div><h5>Le journal</h5>'+
        '<a href="a-propos.html">À propos</a>'+
        '<a href="ligne-editoriale.html">Ligne éditoriale</a>'+
        '<a href="a-propos.html#redaction">La rédaction</a>'+
        '<a href="contact.html">Contact</a>'+
        '<a href="plan-du-site.html">Plan du site</a>'+
      '</div>'+
      '<div class="foot-news"><h5>La newsletter</h5>'+
        '<p class="mono" style="color:var(--ink-soft);margin:0 0 10px;letter-spacing:.04em">Le brief chaque matin, 6 h 40.</p>'+
        '<form onsubmit="return false"><input type="email" placeholder="vous@email.com" aria-label="Votre email"><button>S\'abonner</button></form>'+
        '<div class="foot-social"><a href="#" title="X">X</a><a href="#" title="LinkedIn">in</a><a href="#" title="RSS">rss</a></div>'+
      '</div>'+
    '</div>'+
    '<div class="foot-bottom"><div class="wrap mono">'+
      '<span>© 2026 Algorithme · tous droits réservés</span>'+
      '<span><a href="mentions-legales.html">Mentions légales</a> · <a href="confidentialite.html">Confidentialité</a> · <a href="cgu.html">CGU</a> · <a href="plan-du-site.html">Plan du site</a></span>'+
    '</div></div>'+
  '</footer>';

  document.body.insertAdjacentHTML('afterbegin', ticker + head);
  document.body.insertAdjacentHTML('beforeend', foot);
})();
