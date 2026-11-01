#!/usr/bin/env python3
"""Erzeugt alle Sprachfassungen der Website und das Sprachmenue im Kopf jeder Seite.

Einzige Quelle der Wahrheit bleibt die deutsche Seite:
  * Englisch  steht wie bisher in der en:-Tabelle der deutschen Seite
              (Rest in tools/i18n_en.py). Ergebnis: <seite>-en.html, /en.
  * FR/ES/IT/PT-BR stehen in tools/i18n/<sprache>.json, Schluessel ist der
              DEUTSCHE Text. Ergebnis: /fr/<seite>, /es/..., /it/..., /pt-br/...
Aendert sich ein deutscher Text, findet der Generator keine Uebersetzung mehr,
setzt dort die englische Fassung ein und meldet die Stelle. So kann eine
Sprachfassung nie still einen veralteten Inhalt (Version, Preis) zeigen.

Ausserdem pflegt das Skript auf JEDER Seite zwei markierte Bloecke:
  <!--LANG-HEAD--> ... <!--/LANG-HEAD-->   hreflang, Stil, Sprung zur Wunschsprache
  <!--LANG-MENU--> ... <!--/LANG-MENU-->   das Sprachmenue im Kopf
Was zwischen den Markern steht, wird bei jedem Lauf neu geschrieben.

AUFRUF (im Wurzelverzeichnis des Repos):
  python3 tools/build-i18n.py              alles erzeugen
  python3 tools/build-i18n.py --check      nichts schreiben, Exit 1 bei Drift
  python3 tools/build-i18n.py --export     tools/i18n/source.json (Texte zum Uebersetzen)
  python3 tools/build-i18n.py --review     tools/i18n/gegenlesen-<sprache>.csv neu schreiben
  python3 tools/build-i18n.py --import-review fr datei.csv
                                           Spalte "Korrektur" nach tools/i18n/fr.json uebernehmen

BEIM RELEASE: Download-Links nur in der DEUTSCHEN Seite umstellen (index.html,
mac.html, ...), danach dieses Skript laufen lassen - es traegt sie in alle
Sprachen. Wer weiter per sed auch en.html/mac-en.html anfasst, muss das Skript
trotzdem laufen lassen, sonst bleiben /fr/ usw. auf der alten Version stehen
(tools/check-links.py meldet das).
"""
import csv, html, io, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_en as EN

BASE = EN.BASE
I18N_DIR = os.path.join("tools", "i18n")
ASSET_V = "1"                       # Cache-Buster fuer lang-menu.css/.js (7 Tage immutable)

LANGS = ["de", "en", "fr", "es", "it", "pt-br"]
NEW = ["fr", "es", "it", "pt-br"]
HREFLANG = {"de": "de", "en": "en", "fr": "fr", "es": "es", "it": "it", "pt-br": "pt-BR"}
OG_LOCALE = {"de": "de_DE", "en": "en_US", "fr": "fr_FR", "es": "es_ES", "it": "it_IT", "pt-br": "pt_BR"}
PADDLE_LOCALE = {"fr": "fr", "es": "es", "it": "it", "pt-br": "pt"}
NAME = {"de": "Deutsch", "en": "English", "fr": "Français", "es": "Español",
        "it": "Italiano", "pt-br": "Português (Brasil)"}
CODE = {"de": "DE", "en": "EN", "fr": "FR", "es": "ES", "it": "IT", "pt-br": "PT"}
LABEL = {"de": "Sprache", "en": "Language", "fr": "Langue", "es": "Idioma",
         "it": "Lingua", "pt-br": "Idioma"}
# Steht im Menue hinter einer Sprache, fuer die es die Seite nicht gibt - in
# DIESER Sprache, damit der Leser vor dem Klick weiss, was ihn erwartet.
FALLBACK_NOTE = {"fr": "page en anglais", "es": "página en inglés",
                 "it": "pagina in inglese", "pt-br": "página em inglês",
                 "de": "Seite auf Englisch", "en": "page in English"}

# ------------------------------------------------------------ Seitenmodell ---
# Jede Gruppe = eine Seite in allen Sprachen, die es von ihr gibt.
#   urls  : Sprache -> URL-Pfad (nur ECHTE Fassungen, daraus wird hreflang)
#   files : Sprache -> Datei
#   kind  : "gen"    DE-Quelle, alle anderen Sprachen werden erzeugt
#           "pair"   DE und EN von Hand gepflegt (Rechtsseiten u. a.)
#           "inpage" EINE Datei, DE/EN per JS umgeschaltet (Changelog, Presse ...)
#           "404"    Fehlerseite, Menue fuehrt auf die Startseiten


def new_path(lang, de_p):
    return "/%s/" % lang if de_p == "/" else "/%s%s" % (lang, de_p)


def new_file(lang, de_f):
    return "%s/%s" % (lang, de_f)


GROUPS = []
for _de_f, (_en_f, _de_p, _en_p, _t, _d) in sorted(EN.PAGES.items()):
    g = {"kind": "gen", "src": _de_f,
         "urls": {"de": _de_p, "en": _en_p}, "files": {"de": _de_f, "en": _en_f}}
    for _l in NEW:
        g["urls"][_l] = new_path(_l, _de_p)
        g["files"][_l] = new_file(_l, _de_f)
    GROUPS.append(g)
PAIR_SLUGS = ("agb", "datenschutz", "impressum", "widerruf", "security", "open-source")
for _s in PAIR_SLUGS:
    GROUPS.append({"kind": "pair", "urls": {"de": "/" + _s, "en": "/%s-en" % _s},
                   "files": {"de": _s + ".html", "en": _s + "-en.html"}})
for _s in ("changelog", "press", "videos", "manage-license"):
    GROUPS.append({"kind": "inpage", "urls": {"de": "/" + _s, "en": "/" + _s},
                   "files": {"de": _s + ".html"}})
GROUPS.append({"kind": "404", "urls": {}, "files": {"de": "404.html"}})
HOME = next(g for g in GROUPS if g.get("src") == "index.html")["urls"]


def linkmap(lang):
    """Interne Links einer deutschen Quellseite -> Ziel in `lang`."""
    m = {}
    for g in GROUPS:
        if g["kind"] == "gen":
            de_p, de_f, tgt = g["urls"]["de"], g["files"]["de"], g["urls"][lang]
            m[de_p] = tgt; m["/" + de_f] = tgt; m[de_f] = tgt
        elif g["kind"] == "pair":
            # Rechtsseiten gibt es nur DE/EN. Aus FR/ES/IT/PT fuehrt der Link auf
            # die englische Lesefassung (Entscheidung offen, siehe tools/i18n/README.md).
            de_p = g["urls"]["de"]
            m[de_p] = g["urls"]["en"]; m[de_p + ".html"] = g["urls"]["en"]
            m[de_p.lstrip("/") + ".html"] = g["urls"]["en"]
    return m


# --------------------------------------------------------------- Uebersetzer ---
class Tr:
    """Sucht Uebersetzungen nach deutschem Text; merkt sich Fehlendes und alles Gefragte."""
    def __init__(self, lang):
        self.lang = lang
        p = os.path.join(I18N_DIR, lang + ".json")
        self.d = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}
        self.missing, self.asked = {}, {}

    def __call__(self, de, en, page, kind, is_html=False):
        de = de if de is not None else ""
        a = self.asked.setdefault(de, {"de": de, "en": en, "kind": kind, "html": is_html, "pages": []})
        if page not in a["pages"]:
            a["pages"].append(page)
        v = self.d.get(de)
        if v:
            return v
        self.missing.setdefault(page, set()).add(de[:60])
        return en


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def attr(s):
    return esc(s).replace('"', "&quot;")


def jsonstr(s):
    return json.dumps(s, ensure_ascii=False)[1:-1]


def parse_table(src, name):
    """Liest die <name>:-Tabelle der i18n-Konstante als dict (einfach gequotete JS-Strings)."""
    ei = src.index("\n %s: {" % name)
    m = re.search(r"\n\s*\}\s*[;,]", src[ei:])
    block = src[ei:ei + m.start()]
    out = {}
    for k, v in re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*'((?:[^'\\]|\\.)*)'\s*,?\s*$",
                           block, re.M):
        out[k] = v.replace("\\'", "'").replace('\\"', '"').replace("\\\\", "\\")
    return out


def replace_i18n(src, value_for):
    """Ersetzt den Inhalt jedes [data-i18n]/[data-i18n-html]-Elements.
    value_for(key, inner, is_html) liefert den neuen Inhalt oder None (dann bleibt er)."""
    out, pos = [], 0
    pat = re.compile(r'<([a-zA-Z][\w-]*)\b[^>]*?data-i18n(-html)?="([^"]+)"[^>]*>')
    while True:
        m = pat.search(src, pos)
        if not m:
            out.append(src[pos:]); break
        tag, is_html, key = m.group(1), bool(m.group(2)), m.group(3)
        depth, i = 1, m.end()
        open_re = re.compile(r"<%s\b" % re.escape(tag), re.I)
        close_re = re.compile(r"</%s\s*>" % re.escape(tag), re.I)
        while depth > 0:
            no, nc = open_re.search(src, i), close_re.search(src, i)
            if not nc:
                raise SystemExit("kein </%s> fuer data-i18n=%s" % (tag, key))
            if no and no.start() < nc.start():
                depth += 1; i = no.end()
            else:
                depth -= 1; i = nc.end()
                if depth == 0:
                    inner_end, close_end = nc.start(), nc.end()
        inner = src[m.end():inner_end]
        val = value_for(key, inner, is_html)
        out.append(src[pos:m.end()])
        out.append(inner if val is None else (val if is_html else esc(val)))
        out.append(src[inner_end:close_end])
        pos = close_end
    return "".join(out)


def apply_literals(src, mapping):
    """Ersetzt hartkodierte Literale NUR in Textknoten ausserhalb von <script>/<style>.
    value= bleibt deutsch: das sendet das Support-Formular ab."""
    keys = sorted(mapping, key=len, reverse=True)
    parts = re.split(r"(<script\b.*?</script>|<style\b.*?</style>)", src, flags=re.S)
    for i in range(0, len(parts), 2):
        seg = re.split(r"(<[^>]*>)", parts[i])
        for j in range(0, len(seg), 2):
            for k in keys:
                seg[j] = seg[j].replace(k, mapping[k])
        parts[i] = "".join(seg)
    return "".join(parts)


def rewrite_links(src, lmap, absolute):
    """Interne Links auf die Zielsprache drehen. absolute=True: relative Pfade
    absolut machen (Seiten in /fr/ usw. liegen eine Ebene tiefer)."""
    keep = re.compile(r"^(/|#|[a-zA-Z][a-zA-Z0-9+.-]*:)")

    def one(u):
        base, sep, rest = re.match(r"([^?#]*)([?#]?)(.*)", u).groups()
        if base in lmap:
            return lmap[base] + sep + rest
        if absolute and u and not keep.match(u):
            return "/" + u
        return u

    def rep(m):
        a, q, v = m.group(1), m.group(2), m.group(3)
        if a == "srcset":
            v = ", ".join(" ".join([one(p.split()[0])] + p.split()[1:]) for p in v.split(","))
        elif a == "href":
            v = one(v)
        elif absolute:
            v = "/" + v if v and not keep.match(v) else v
        return '%s=%s%s%s' % (a, q, v, q)
    return re.sub(r'\b(href|src|srcset|poster|data-src-[a-z]+)=(["\'])([^"\']*)\2', rep, src)


# ------------------------------------------------------ Kopf und Menue (HTML) ---
def alternates(g):
    return {l: g["urls"][l] for l in LANGS if l in g["urls"]}


def head_block(g, cur):
    """Inhalt zwischen <!--LANG-HEAD--> und <!--/LANG-HEAD-->."""
    lines = []
    alt = alternates(g)
    if g["kind"] in ("gen", "pair"):
        for l, u in alt.items():
            lines.append('<link rel="alternate" hreflang="%s" href="%s%s">' % (HREFLANG[l], BASE, u))
        lines.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (BASE, alt.get("en", alt["de"])))
    lines.append('<link rel="stylesheet" href="/lang-menu.css?v=%s">' % ASSET_V)
    if g["kind"] in ("gen", "pair"):
        # Nur bei ausdruecklich gewaehlter Sprache springen (gesetzt vom Menue).
        # Ohne Wahl bleibt der Besucher, wo er ist - er hat die URL bewusst aufgerufen.
        lines.append("<script>try{var p=localStorage.getItem('satk-lang'),a=%s;"
                     "if(p&&p!=='%s'&&a[p])location.replace(a[p]+location.search+location.hash);}catch(e){}</script>"
                     % (json.dumps(alt, separators=(",", ":")), cur))
    lines.append('<script src="/lang-menu.js?v=%s" defer></script>' % ASSET_V)
    return "<!--LANG-HEAD-->\n%s\n<!--/LANG-HEAD-->" % "\n".join(lines)


GLOBE = ('<svg class="lm-globe" aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9.5"/>'
         '<path d="M2.5 12h19M12 2.5c2.6 2.7 3.9 5.9 3.9 9.5s-1.3 6.8-3.9 9.5M12 2.5C9.4 5.2 8.1 8.4 8.1 12s1.3 6.8 3.9 9.5"/></svg>')
CHEV = ('<svg class="lm-chev" aria-hidden="true" width="9" height="6" viewBox="0 0 12 8" fill="currentColor">'
        '<path d="M6 8L0 0h12z"/></svg>')


def menu_block(g, cur, floating=False):
    """Inhalt zwischen <!--LANG-MENU--> und <!--/LANG-MENU-->."""
    kind, alt = g["kind"], alternates(g)
    items = []
    for l in LANGS:
        note = ""
        if kind == "404":
            href, target = HOME[l], l
        elif l in alt:
            href, target = alt[l], l
        else:                                   # Seite gibt es in l nicht -> Englisch
            href, target = alt["en"], "en"
            note = '<small>%s</small>' % FALLBACK_NOTE[l]
        cur_attr = ' aria-current="true"' if l == cur else ""
        items.append('<li><a href="%s" lang="%s" hreflang="%s" data-lang="%s"%s>%s%s</a></li>'
                     % (href, HREFLANG[l], HREFLANG[target], l, cur_attr, NAME[l], note))
    extra = ""
    if kind == "inpage":
        extra = " data-inpage data-labels='%s'" % json.dumps({l: LABEL[l] for l in ("de", "en")})
    btn = ('<button type="button" class="lm-btn" aria-expanded="false" aria-controls="lm-list">'
           '%s<span class="lm-code">%s</span><span class="lm-sr"> – %s: %s</span>%s</button>'
           % (GLOBE, CODE[cur], LABEL[cur], NAME[cur], CHEV))
    return ('<!--LANG-MENU--><div class="lm%s"%s>%s<ul class="lm-list" id="lm-list" hidden>%s</ul></div><!--/LANG-MENU-->'
            % (" lm-float" if floating else "", extra, btn, "".join(items)))


OLD_SWITCH = re.compile(r"<script>\s*\nfunction switchLang.*?</script>\n?", re.S)
OLD_REDIRECT = re.compile(r"<script>\n// Auto-redirect to [A-Z]{2} version.*?</script>\n?", re.S)
OLD_HREFLANG = re.compile(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?')
OLD_LANGSW = re.compile(r'<div class="lang-sw">.*?</div>', re.S)


def put_blocks(s, g, cur):
    """Kopf- und Menue-Block einsetzen. Idempotent: vorhandene Marker werden ersetzt,
    beim ersten Lauf werden die alten DE/EN-Umschalter entfernt."""
    hb, floating = head_block(g, cur), False
    if "<!--LANG-HEAD-->" in s:
        s = re.sub(r"<!--LANG-HEAD-->.*?<!--/LANG-HEAD-->", lambda m: hb, s, count=1, flags=re.S)
    else:
        s = OLD_HREFLANG.sub("", s)
        s = OLD_SWITCH.sub("", s)
        s = OLD_REDIRECT.sub("", s)
        m = re.search(r'<link rel="canonical" href="[^"]*">\n', s)
        if m:
            s = s[:m.end()] + hb + "\n" + s[m.end():]
        else:
            s = s.replace("</head>", hb + "\n</head>", 1)
    if "<!--LANG-MENU-->" in s:
        floating = 'class="lm lm-float"' in s
        mb = menu_block(g, cur, floating)
        s = re.sub(r"<!--LANG-MENU-->.*?<!--/LANG-MENU-->", lambda m: mb, s, count=1, flags=re.S)
    elif OLD_LANGSW.search(s):
        s = OLD_LANGSW.sub(lambda m: menu_block(g, cur), s, count=1)
    else:                                       # Seiten ohne Kopfzeile (Rechtsseiten, 404)
        s = re.sub(r"(<body[^>]*>\n?)", lambda m: m.group(1) + menu_block(g, cur, True) + "\n", s, count=1)
    return s


# ------------------------------------------------------- Seite uebersetzen ---
GEN_NOTE = ("<!-- GENERIERT von tools/build-i18n.py aus %s - NICHT von Hand aendern.\n"
            "     Aenderungen gehoeren in die deutsche Seite (bzw. ihre en:-Tabelle oder\n"
            "     tools/i18n/<sprache>.json), danach `python3 tools/build-i18n.py`. -->\n")
DEAD_AUTOSET = re.compile(r"\n?try \{\n?\s*const saved = localStorage\.getItem\('satk-lang'\);\n?\s*"
                          r"if \(saved === 'en'\) setLang\('en'\);\n?\s*\} catch\(e\)\{\}")
# Nur fuer FR/ES/IT/PT: hartkodierte Literale, die DE/EN (noch) behalten.
# "RTW" ist ein Fremdhersteller und darf in den neuen Sprachen nicht stehen.
LITERAL_NEW = {"RTW-Style": "Broadcast style"}
JSONLD_NAME_EN = {"Startseite": "Home", "Abo jährlich": "Annual subscription",
                  "Abo monatlich": "Monthly subscription"}


def meta_content(s, sel):
    m = re.search(r'<meta %s content="(.*?)">' % sel, s, re.S)
    return html.unescape(m.group(1)) if m else None


def set_meta(s, sel, val):
    return re.sub(r'<meta %s content=".*?">' % sel,
                  lambda m: '<meta %s content="%s">' % (sel, val), s, count=1, flags=re.S)


def build(g, lang, src, tr):
    """Eine Sprachfassung aus der (bereits gepatchten) deutschen Quelle erzeugen."""
    de_f, de_p, url = g["files"]["de"], g["urls"]["de"], g["urls"][lang]
    page = g["files"][lang]
    dtab, etab = parse_table(src, "de"), parse_table(src, "en")
    en_title, en_desc = EN.PAGES[de_f][3], EN.PAGES[de_f][4]

    if lang == "en":
        T = lambda de, en, kind, h=False: en
    else:
        T = lambda de, en, kind, h=False: tr(de, en, page, kind, h)

    def value_for(key, inner, is_html):
        de = dtab.get(key)
        if de is None:
            de = inner.strip() if is_html else html.unescape(inner.strip())
        en = etab.get(key, EN.HARDCODED_EN.get(key))
        if en is None:
            return None
        return T(de, en, "text", is_html)

    s = replace_i18n(src, value_for)
    s = rewrite_links(s, linkmap(lang), absolute=(lang in NEW))
    s = s.replace('<html lang="de">', '<html lang="%s">' % HREFLANG[lang], 1)

    # Titel, Description, Canonical, Social-Tags
    de_title = html.unescape(re.search(r"<title>(.*?)</title>", src, re.S).group(1))
    de_desc = meta_content(src, 'name="description"')
    if lang == "en":
        title, desc = en_title, en_desc
    else:
        title = attr(T(de_title, html.unescape(en_title), "title"))
        desc = attr(T(de_desc, html.unescape(en_desc), "description")) if de_desc else attr(html.unescape(en_desc))
    s = re.sub(r"<title>.*?</title>", lambda m: "<title>%s</title>" % title, s, count=1, flags=re.S)
    if re.search(r'<meta name="description" content=".*?">', s, re.S):
        s = set_meta(s, 'name="description"', desc)
    else:
        s = s.replace("</title>", "</title>\n<meta name=\"description\" content=\"%s\">" % desc, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">',
               '<link rel="canonical" href="%s%s">' % (BASE, url), s, count=1)
    for sel, val in (('property="og:title"', title), ('name="twitter:title"', title),
                     ('property="og:description"', desc), ('name="twitter:description"', desc),
                     ('property="og:url"', BASE + url), ('property="og:locale"', OG_LOCALE[lang])):
        s = set_meta(s, sel, val)
    s = re.sub(r'<meta property="og:locale:alternate" content="[^"]*">\n?', "", s)
    s = s.replace('<meta property="og:locale" content="%s">' % OG_LOCALE[lang],
                  "\n".join(['<meta property="og:locale" content="%s">' % OG_LOCALE[lang]] +
                            ['<meta property="og:locale:alternate" content="%s">' % OG_LOCALE[l]
                             for l in LANGS if l != lang]), 1)

    # JSON-LD
    s = s.replace('"url": "%s%s"' % (BASE, de_p), '"url": "%s%s"' % (BASE, url))
    s = re.sub(r'"inLanguage":\s*\[[^\]]*\]', '"inLanguage": "%s"' % HREFLANG[lang], s)
    s = re.sub(r'"inLanguage":\s*"de"', '"inLanguage": "%s"' % HREFLANG[lang], s)
    lm = linkmap(lang); lm["/"] = HOME[lang]
    s = re.sub(r'"item": "%s(/[a-z0-9-]*)?"' % re.escape(BASE),
               lambda m: '"item": "%s%s"' % (BASE, lm.get(m.group(1) or "/", m.group(1) or "/")), s)
    for de_txt, en_txt in JSONLD_NAME_EN.items():
        if '"name": "%s"' % de_txt in s:
            s = s.replace('"name": "%s"' % de_txt, '"name": "%s"' % jsonstr(T(de_txt, en_txt, "jsonld")))
    for de_txt, en_txt in EN.JSONLD_DESC_EN.items():
        if '"description": "%s"' % de_txt in s:
            s = s.replace('"description": "%s"' % de_txt,
                          '"description": "%s"' % jsonstr(T(de_txt, en_txt, "jsonld")))

    # Alt-Texte, Literale, Platzhalter
    for de_txt, en_txt in EN.ALT_EN.items():
        if 'alt="%s"' % de_txt in s:
            s = s.replace('alt="%s"' % de_txt, 'alt="%s"' % attr(T(de_txt, en_txt, "alt")))
    lits = dict(EN.LITERAL_EN, **(LITERAL_NEW if lang in NEW else {}))
    lit = {k: esc(T(k, v, "literal")) for k, v in lits.items() if k in s}
    s = apply_literals(s, lit)
    for de_txt, en_txt in EN.PLACEHOLDER_EN.items():
        if de_txt in s:
            t = attr(T(de_txt, en_txt, "placeholder"))
            s = re.sub(r'placeholder="([^"]*)"',
                       lambda m: 'placeholder="%s"' % m.group(1).replace(de_txt, t), s)

    # App-Store-Plakette: es gibt nur DE und EN, alle anderen nehmen EN
    s = re.sub(r'(<img )src="[^"]*"( data-src-de="[^"]*" data-src-en="([^"]*)")',
               lambda m: '%ssrc="%s"%s' % (m.group(1), m.group(3), m.group(2)), s)

    if lang in NEW:
        # JS liest Texte zur Laufzeit aus i18n[<html lang>] - Tabelle fuer diese Sprache anlegen
        # Die DE/EN-Tabellen fliegen raus: ungenutzt, und kein fremder Text im Quelltext.
        tab = {k: T(v, etab.get(k, v), "text") for k, v in dtab.items()}
        i = s.index("const i18n = {\n"); j = s.index("\n};", i) + 3
        s = s[:i] + ("const i18n = {'%s': %s};\ni18n.de = i18n.en = i18n['%s'];"
                     % (HREFLANG[lang], json.dumps(tab, ensure_ascii=False, indent=0), HREFLANG[lang])) + s[j:]
        s = s.replace("locale: document.documentElement.lang || 'de'",
                      "locale: '%s'" % PADDLE_LOCALE[lang])

    s = DEAD_AUTOSET.sub("", s)
    s = put_blocks(s, g, lang)
    s = s.replace("<!DOCTYPE html>", "<!DOCTYPE html>\n" + (GEN_NOTE % de_f).rstrip("\n"), 1)
    return s


# ---------------------------------------------------------------- Sitemap ---
def sitemap(cur):
    rows = []
    for g in GROUPS:
        if g["kind"] != "gen":
            continue
        try:
            lastmod = subprocess.check_output(["git", "log", "-1", "--format=%cs", "--", g["src"]],
                                              text=True).strip()
        except Exception:
            lastmod = ""
        for l in NEW:
            rows.append("  <url>\n    <loc>%s%s</loc>\n%s    <changefreq>monthly</changefreq>\n"
                        "    <priority>0.5</priority>\n  </url>"
                        % (BASE, g["urls"][l], "    <lastmod>%s</lastmod>\n" % lastmod if lastmod else ""))
    block = ("  <!-- I18N:START - erzeugt von tools/build-i18n.py -->\n%s\n  <!-- I18N:END -->"
             % "\n".join(rows))
    if "<!-- I18N:START" in cur:
        return re.sub(r"  <!-- I18N:START.*?<!-- I18N:END -->", lambda m: block, cur, count=1, flags=re.S)
    return cur.replace("</urlset>", block + "\n\n</urlset>", 1)


# ------------------------------------------------------------ Gegenlesen ---
REVIEW_HEAD = ["Nr", "Seiten", "Art", "Deutsch (Original)", "English (Referenz)",
               "Entwurf", "Hinweis zum Entwurf", "Korrektur", "Anmerkung"]


def write_review(lang, asked):
    """CSV fuer Muttersprachler. Korrektur/Anmerkung bleiben erhalten, wenn es die Datei schon gibt."""
    p = os.path.join(I18N_DIR, "gegenlesen-%s.csv" % lang)
    old = {}
    if os.path.exists(p):
        for r in csv.DictReader(io.open(p, encoding="utf-8-sig")):
            old[r["Deutsch (Original)"]] = r
    d = json.load(io.open(os.path.join(I18N_DIR, lang + ".json"), encoding="utf-8"))
    hp = os.path.join(I18N_DIR, lang + "-hinweise.json")
    hints = json.load(io.open(hp, encoding="utf-8")) if os.path.exists(hp) else {}
    with io.open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(REVIEW_HEAD)
        for n, a in enumerate(asked.values(), 1):
            o = old.get(a["de"], {})
            w.writerow([n, " ".join(sorted(a["pages"])), a["kind"] + (" (HTML)" if a["html"] else ""),
                        a["de"], a["en"], d.get(a["de"], ""), hints.get(a["de"], ""), o.get("Korrektur", ""), o.get("Anmerkung", "")])
    return p


def import_review(lang, path):
    jp = os.path.join(I18N_DIR, lang + ".json")
    d = json.load(io.open(jp, encoding="utf-8"))
    n = 0
    for r in csv.DictReader(io.open(path, encoding="utf-8-sig")):
        k, v = r["Deutsch (Original)"], (r.get("Korrektur") or "").strip()
        if v and d.get(k) != v:
            d[k] = v; n += 1
    io.open(jp, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  %d Korrekturen nach %s uebernommen" % (n, jp))


# ------------------------------------------------------------------ Lauf ---
def render_all():
    """Alle Ausgaben im Speicher: {datei: inhalt}, dazu die Uebersetzer (fuer Berichte)."""
    out, trs = {}, {l: Tr(l) for l in NEW}
    for g in GROUPS:
        de_f = g["files"]["de"]
        src = io.open(de_f, encoding="utf-8").read()
        if g["kind"] == "gen":
            src = put_blocks(src, g, "de")
            src = DEAD_AUTOSET.sub("", src)
            out[de_f] = src
            for l in ["en"] + NEW:
                out[g["files"][l]] = build(g, l, src, trs.get(l))
        elif g["kind"] == "pair":
            out[de_f] = put_blocks(src, g, "de")
            en_f = g["files"]["en"]
            out[en_f] = put_blocks(io.open(en_f, encoding="utf-8").read(), g, "en")
        else:
            out[de_f] = put_blocks(src, g, "de")
    out["sitemap.xml"] = sitemap(io.open("sitemap.xml", encoding="utf-8").read())
    return out, trs


def main():
    args = sys.argv[1:]
    if args[:1] == ["--import-review"]:
        import_review(args[1], args[2]); return
    out, trs = render_all()
    if "--export" in args:
        merged = {}
        for t in trs.values():
            for k, a in t.asked.items():
                merged.setdefault(k, a)
        p = os.path.join(I18N_DIR, "source.json")
        io.open(p, "w", encoding="utf-8").write(json.dumps(list(merged.values()), ensure_ascii=False, indent=1) + "\n")
        print("  %d Texte -> %s" % (len(merged), p)); return
    if "--review" in args:
        for l, t in trs.items():
            print("  " + write_review(l, t.asked))
        return
    check = "--check" in args
    drift = []
    for f, s in sorted(out.items()):
        old = io.open(f, encoding="utf-8").read() if os.path.exists(f) else None
        if old == s:
            continue
        drift.append(f)
        if not check:
            os.makedirs(os.path.dirname(f) or ".", exist_ok=True)
            io.open(f, "w", encoding="utf-8").write(s)
    for l, t in trs.items():
        n = sum(len(v) for v in t.missing.values())
        if n:
            print("  %-6s %3d Texte ohne Uebersetzung (englisch eingesetzt), z. B.: %s"
                  % (l, n, "; ".join(sorted(next(iter(t.missing.values())))[:2])))
    if check:
        print("  DRIFT: %s" % (", ".join(drift) if drift else "keiner, alles aktuell"))
        sys.exit(1 if drift else 0)
    print("  %d Dateien geschrieben" % len(drift))


if __name__ == "__main__":
    main()
