#!/usr/bin/env python3
"""Prueft die Website im Arbeitsverzeichnis, ohne Server und ohne Netz.

  * jeder interne Link / jedes Bild loest auf eine Datei auf (wie Cloudflare
    Pages: /x -> x.html, /x/ -> x/index.html, _redirects werden befolgt)
  * jede Seite traegt GENAU ein Sprachmenue mit allen sechs Sprachen
  * hreflang: jede Sprachfassung nennt alle anderen, gegenseitig, x-default = EN,
    canonical zeigt auf sich selbst, <html lang> passt
  * Download-Links (download.pegelwerk.com) sind in allen Sprachen einer Seite gleich
  * verbotene Namen ("Mute-O-Matic", Fremdhersteller) stehen in keiner neuen Sprachfassung

Aufruf im Repo-Wurzelverzeichnis:  python3 tools/check-links.py     (Exit 1 bei Fehlern)
"""
import glob, io, os, re, sys

BASE = "https://pegelwerk.com"
LANGS = ["de", "en", "fr", "es", "it", "pt-br"]
HREFLANG = {"de": "de", "en": "en", "fr": "fr", "es": "es", "it": "it", "pt-br": "pt-BR"}
NEW_DIRS = ("fr", "es", "it", "pt-br")
FORBIDDEN = re.compile(r"mute-o-matic|\bRTW\b", re.I)
NO_MENU = {"activate.html"}           # Weiterleitung aus der Lizenz-Mail, ohne Kopfzeile

errors = []


def err(f, msg):
    errors.append("%-34s %s" % (f, msg))


def load_redirects():
    r = {}
    for line in io.open("_redirects", encoding="utf-8"):
        line = line.split("#", 1)[0].split()
        if len(line) >= 2 and "*" not in line[0] and ":" not in line[0]:
            r[line[0]] = line[1]
    return r


REDIR = load_redirects()


def resolve(path):
    """URL-Pfad -> Datei oder None. Folgt _redirects (max. 5 Spruenge)."""
    for _ in range(5):
        if path in REDIR:
            path = REDIR[path]
            if path.startswith("http"):
                return "<extern>"
            continue
        p = path.lstrip("/")
        cands = [os.path.join(p, "index.html")] if (p == "" or p.endswith("/")) else [p, p + ".html", os.path.join(p, "index.html")]
        for c in cands:
            if os.path.isfile(c or "index.html"):
                return c or "index.html"
        return None
    return None


def url_of(f):
    """Datei -> kanonischer URL-Pfad (Pages-Clean-URL)."""
    if f == "index.html":
        return "/"
    if f.endswith("/index.html"):
        return "/" + f[:-10]
    return "/" + f[:-5]


files = sorted(f for f in glob.glob("*.html") + glob.glob("*/*.html")
               if not f.startswith(("tools/", "press/")))
pages = {f: io.open(f, encoding="utf-8").read() for f in files}

# 1. Links und Bilder
REF = re.compile(r'\b(href|src|srcset|poster|data-src-[a-z]+)=(["\'])([^"\']*)\2')
for f, s in pages.items():
    body = re.sub(r"<script\b(?![^>]*ld\+json).*?</script>", "", s, flags=re.S)   # JS-Strings nicht pruefen
    here = os.path.dirname(url_of(f))             # /fr/ -> /fr, /mac -> /
    for a, _q, v in REF.findall(body):
        vals = [p.split()[0] for p in v.split(",") if p.strip()] if a == "srcset" else [v]
        for u in vals:
            if u.startswith(BASE):
                u = u[len(BASE):] or "/"
            if not u or re.match(r"^(#|mailto:|tel:|data:|javascript:|[a-z]+://)", u) or u.startswith("//"):
                continue
            path = re.split(r"[?#]", u)[0]
            if not path:
                continue
            if not path.startswith("/"):
                path = os.path.normpath(os.path.join(here, path)).replace("\\", "/")
                if not path.startswith("/"):
                    path = "/" + path
            if path.startswith("/tools/"):
                err(f, "verlinkt Build-Werkzeug %s" % u)
            elif resolve(path) is None:
                err(f, "404: %s=%s" % (a, u))

# 2. Sprachmenue
for f, s in pages.items():
    if f in NO_MENU:
        continue
    n = s.count("<!--LANG-MENU-->")
    if n != 1:
        err(f, "Sprachmenue %dx statt 1x" % n); continue
    menu = re.search(r"<!--LANG-MENU-->(.*?)<!--/LANG-MENU-->", s, re.S).group(1)
    langs = re.findall(r'data-lang="([^"]+)"', menu)
    if langs != LANGS:
        err(f, "Menue-Sprachen %s" % langs)
    if menu.count('aria-current="true"') != 1:
        err(f, "Menue: aktuelle Sprache %dx markiert" % menu.count('aria-current="true"'))
    if 'href="/lang-menu.js' not in s and 'src="/lang-menu.js' not in s:
        err(f, "lang-menu.js fehlt")

# 3. hreflang, canonical, <html lang>
groups = {}
for f, s in pages.items():
    alts = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', s))
    m = re.search(r'<link rel="canonical" href="([^"]+)">', s)
    lang = re.search(r'<html lang="([^"]+)"', s).group(1)
    folder = f.split("/")[0] if "/" in f else None
    if folder and lang != HREFLANG[folder]:
        err(f, "<html lang=%s> passt nicht zum Ordner" % lang)
    if not alts:
        continue
    canon = m.group(1) if m else None
    if canon != BASE + url_of(f):
        err(f, "canonical %s != %s" % (canon, BASE + url_of(f)))
    if alts.get(lang) != canon:
        err(f, "hreflang fuer die eigene Sprache %s zeigt nicht auf canonical" % lang)
    if "x-default" in alts and alts["x-default"] != alts.get("en"):
        err(f, "x-default ist nicht die englische Fassung")
    key = tuple(sorted(alts.items()))
    groups.setdefault(key, []).append(f)
    for hl, u in alts.items():
        if resolve(u[len(BASE):] or "/") is None:
            err(f, "hreflang %s -> 404 %s" % (hl, u))
for key, fs in groups.items():
    want = len([k for k, _ in key if k != "x-default"])
    if len(fs) != want:
        err(fs[0], "hreflang nicht gegenseitig: %d Dateien teilen den Satz, erwartet %d (%s)" % (len(fs), want, ", ".join(fs)))
    full = {k for k, _ in key} >= set(HREFLANG.values())
    if any("/" in x for x in fs) and not full:
        err(fs[0], "Sprachfassung ohne alle sechs Sprachpartner")

# 4. Download-Links in allen Sprachen gleich
for key, fs in groups.items():
    sets = {f: sorted(set(re.findall(r'https://download\.pegelwerk\.com/[^"\'\s<]+', pages[f]))) for f in fs}
    if len({tuple(v) for v in sets.values()}) > 1:
        ref = sets[fs[0]]
        for f, v in sets.items():
            if v != ref:
                err(f, "Download-Links weichen ab: %s" % ", ".join(sorted(set(v) ^ set(ref))))

# 5. Verbotene Namen in den neuen Sprachfassungen
for f, s in pages.items():
    if f.split("/")[0] in NEW_DIRS:
        txt = re.sub(r"<[^>]+>", " ", s)
        for m in set(FORBIDDEN.findall(txt)):
            err(f, "verbotener Name: %s" % m)

print("  %d Seiten geprueft, %d hreflang-Gruppen" % (len(pages), len(groups)))
if errors:
    print("\n".join("  " + e for e in errors))
    print("  %d FEHLER" % len(errors))
    sys.exit(1)
print("  keine Fehler")
