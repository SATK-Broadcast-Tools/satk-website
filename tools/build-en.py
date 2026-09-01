#!/usr/bin/env python3
"""Erzeugt die englischen Produktseiten aus den deutschen.

Einzige Quelle der Wahrheit ist die deutsche Seite samt ihrer bereits
vorhandenen `en:`-i18n-Tabelle. Dieses Skript backt die englischen Strings
statisch in eine eigene Datei, damit Google sie ueberhaupt sieht - vorher
existierte das Englische nur als JS-Strings und war fuer Crawler unsichtbar.

Aufruf aus dem Repo-Wurzelverzeichnis:  python3 tools/build-en.py [--check]

--check schreibt nichts, sondern meldet nur, ob die erzeugten Dateien noch
zum aktuellen Stand der deutschen Seiten passen (Exit 1 bei Drift).
"""
import io, os, re, sys

BASE = "https://pegelwerk.com"

# de-Datei -> (en-Datei, DE-Pfad, EN-Pfad, EN-Titel, EN-Description)
PAGES = {
 "index.html": ("en.html", "/", "/en",
   "pegelWERK - Pro Audio Software for Broadcast &amp; Post Production",
   "pegelWERK pro audio apps for macOS and iPad: voyzSESSION PRO, loudness METER PRO, loudness CORRECT, easy EDITOR and instant PLAYER."),
 "mac.html": ("mac-en.html", "/mac", "/mac-en",
   "pegelWERK Mac Apps - loudness METER PRO, voyzSESSION PRO, loudness CORRECT",
   "Native macOS apps for broadcast and post production: loudness METER PRO, voyzSESSION PRO and loudness CORRECT with EBU R128 metering and correction."),
 "ios.html": ("ios-en.html", "/ios", "/ios-en",
   "pegelWERK iOS Apps - iPhone and iPad on the App Store",
   "iOS apps for iPhone and iPad on the App Store: loudness METER PRO, voyzSESSION, loudness CORRECT, easy EDITOR and instant PLAYER."),
 "broadcast-meter-pro.html": ("broadcast-meter-pro-en.html", "/broadcast-meter-pro", "/broadcast-meter-pro-en",
   "pegelWERK loudness METER PRO - EBU R128 Metering for Broadcast",
   "EBU R128 / ITU-R BS.1770-4 / BS.1771 loudness metering: PPM, LUFS, True Peak, FFT, goniometer, speech clarity. macOS, iPad and iPhone."),
 "loudness-correct.html": ("loudness-correct-en.html", "/loudness-correct", "/loudness-correct-en",
   "pegelWERK loudness CORRECT - EBU R128 / ITU-R BS.1770-4 Loudness Correction",
   "Offline loudness correction to EBU R128, ATSC A/85, OTT, Spotify, YouTube. Two-pass with verify-and-refine to +/-0.1 LU. macOS standalone and iPad."),
 "voyzsession.html": ("voyzsession-en.html", "/voyzsession", "/voyzsession-en",
   "voyzSESSION PRO - the DAW for voice production on the Mac | pegelWERK",
   "voyzSESSION PRO: the DAW for voice production on the Mac. Record. Auto Mix. Deliver. Auto Mix to EBU R128, ATSC A/85 and ARIB."),
 "broadcast-meter-ios.html": ("broadcast-meter-ios-en.html", "/broadcast-meter-ios", "/broadcast-meter-ios-en",
   "pegelWERK loudness METER PRO &amp; loudness METER - EBU R128 on iPad and iPhone",
   "EBU R128 / ITU-R BS.1770-4 loudness metering on iOS: loudness METER PRO for iPad with Silero VAD, forecast and MIDI learn."),
 "loudness-correct-ios.html": ("loudness-correct-ios-en.html", "/loudness-correct-ios", "/loudness-correct-ios-en",
   "pegelWERK loudness CORRECT - EBU R128 loudness correction on iPad",
   "Offline EBU R128 loudness correction on the iPad. 16 delivery presets, two-pass with verify-and-refine, 4x polyphase true-peak limiter."),
 "voyzsession-ios.html": ("voyzsession-ios-en.html", "/voyzsession-ios", "/voyzsession-ios-en",
   "voyzSESSION for iPad - voice-over &amp; podcast, broadcast-ready | pegelWERK",
   "voyzSESSION for iPad: mix and master voice-over and podcast. AutoEdit, AutoMix to EBU R128, SmartDucker and R128 export."),
 "easy-editor.html": ("easy-editor-en.html", "/easy-editor", "/easy-editor-en",
   "pegelWERK easy EDITOR - trim audio and hit EBU R128 -23 LUFS",
   "Audio editor for iPhone and iPad: open a file, trim it, normalise to EBU R128 -23 LUFS with a true-peak limiter."),
 "instant-player-app.html": ("instant-player-app-en.html", "/instant-player-app", "/instant-player-app-en",
   "pegelWERK instant PLAYER - 64-pad soundboard for live, theatre and studio",
   "Free soundboard for iPhone and iPad: 64 pads in 4 banks, MULTI/SINGLE mode with cross-fade, AUTO-CUE and LOOP."),
 "support.html": ("support-en.html", "/support", "/support-en",
   "pegelWERK Support - contact &amp; help",
   "Support and contact for pegelWERK loudness METER PRO, voyzSESSION PRO and loudness CORRECT. Email support directly from the developer."),
}

# Schluessel, die in KEINER der beiden Tabellen stehen (hartkodiert im Markup)
# und deshalb hier uebersetzt werden muessen. Wortlaut aus agb-en.html uebernommen.
HARDCODED_EN = {
 "f_security": "Security", "nav_videos": "Videos", "nav_info": "Support request",
 "pc_h_feature": "Feature", "pc_h_macos": "macOS app",
 "pc_price": "Price", "pc_price_iphone": "Free",
 "sup_err_p": "The form could not deliver your request right now. No problem, send it "
              "by email instead. Everything you entered will be pre-filled in the message.",
}

# Hartkodierte deutsche Literale OHNE data-i18n. Die hat auch der bisherige
# JS-Umschalter nie uebersetzt - sie blieben selbst im EN-Modus deutsch.
LITERAL_EN = {
 "Wellenform": "Waveform",
 "Mini-Preview mit Cue-Marker": "Mini preview with cue marker",
 ".satkip (ZIP mit 24-Bit-WAVs)": ".satkip (ZIP with 24-bit WAVs)",
 "SmartDucker mit BedSpeechDetector": "SmartDucker with BedSpeechDetector",
 "Allgemein / Sonstiges": "General / other",
 "Frage / Wie geht...": "Question / how do I...",
 "Feature-Wunsch": "Feature request",
 "Lizenz / Bestellung": "Licence / order",
 "Sonstiges": "Other",
 "Andere": "Other",
 "macOS App": "macOS app",
}

# Nur fuer placeholder-Attribute. value= bleibt bewusst deutsch: das sind die
# Werte, die das Support-Formular absendet - sonst kaemen zwei Varianten an.
PLACEHOLDER_EN = {"z. B.": "e.g."}

# Bild-Alternativtexte. Auf einer englischen Seite darf kein deutscher alt-Text
# stehen - er zaehlt fuer Screenreader und die Bildersuche.
ALT_EN = {
 "pegelWERK loudness METER PRO auf iPad": "pegelWERK loudness METER PRO on iPad",
 "loudness METER auf iPhone, Meters-Page": "loudness METER on iPhone, meters page",
 "loudness METER auf iPhone, Spectrum-Page": "loudness METER on iPhone, spectrum page",
 "pegelWERK loudness METER PRO Interface": "pegelWERK loudness METER PRO interface",
 "loudness METER PRO, iPad App": "loudness METER PRO, iPad app",
 "loudness METER PRO Mini, Page Meters": "loudness METER PRO Mini, meters page",
 "loudness METER PRO Mini, Page Spectrum": "loudness METER PRO Mini, spectrum page",
 "pegelWERK easy EDITOR, Wellenform-Editor f\u00fcr iPhone und iPad": "pegelWERK easy EDITOR, waveform editor for iPhone and iPad",
 "Mac Apps, Standalone f\u00fcr macOS": "Mac apps, standalone for macOS",
 "iOS Apps, iPhone und iPad": "iOS apps, iPhone and iPad",
 "pegelWERK instant PLAYER, 64-Pad-Soundboard f\u00fcr iPhone und iPad": "pegelWERK instant PLAYER, 64-pad soundboard for iPhone and iPad",
 "pegelWERK loudness METER PRO, iPad und iPhone": "pegelWERK loudness METER PRO, iPad and iPhone",
 "pegelWERK easy EDITOR, Wellenform-Editor fuer iPhone und iPad, zur Detailseite": "pegelWERK easy EDITOR, waveform editor for iPhone and iPad, go to product page",
 "pegelWERK instant PLAYER, 64-Pad-Soundboard fuer iPhone und iPad, zur Detailseite": "pegelWERK instant PLAYER, 64-pad soundboard for iPhone and iPad, go to product page",
 "pegelWERK loudness CORRECT auf dem iPad: Original- und Vorgabe-Werte nebeneinander, EBU-R128-Preset": "pegelWERK loudness CORRECT on the iPad: original and target values side by side, EBU R128 preset",
 "pegelWERK loudness CORRECT: Original- und Vorgabe-Werte nebeneinander, EBU-R128-Preset, True Peak und Integrated auf Ziel": "pegelWERK loudness CORRECT: original and target values side by side, EBU R128 preset, true peak and integrated on target",
 "pegelWERK voyzSESSION PRO, zur Detailseite": "pegelWERK voyzSESSION PRO, go to product page",
 "pegelWERK loudness METER PRO, zur Detailseite": "pegelWERK loudness METER PRO, go to product page",
 "pegelWERK loudness CORRECT, zur Detailseite": "pegelWERK loudness CORRECT, go to product page",
 "pegelWERK voyzSESSION, iPad-Layout-Mockup (voyzSESSION PRO f\u00fcr Mac dargestellt)": "pegelWERK voyzSESSION, iPad layout mockup (voyzSESSION PRO for Mac shown)",
 "voyzSESSION PRO: Mischpult mit Voice-, Audio- und Gruppenkanaelen, Timeline mit Wellenformen": "voyzSESSION PRO: mixer with voice, audio and group channels, timeline with waveforms",
}

# JSON-LD-Descriptions. Google liest sie direkt aus den strukturierten Daten,
# deutscher Text dort widerspraeche der englischen Seite.
JSONLD_DESC_EN = {
 "EBU R128 / ITU-R BS.1770-4 Loudness-Meter f\u00fcr iPad. Silero-VAD-Sprachklarheit, Live-Forecast, RTW-PPM, Goniometer, Histograms, MIDI Learn + Bluetooth Pairing.":
   "EBU R128 / ITU-R BS.1770-4 loudness meter for iPad. Silero VAD speech clarity, live forecast, RTW PPM, goniometer, histograms, MIDI learn and Bluetooth pairing.",
 "Kompakter Loudness-Meter f\u00fcr iPhone. Zwei Swipe-Pages mit Meters und Spectrum. EBU R128 / ITU-R BS.1770-4. Background-Audio. Portrait und Landscape.":
   "Compact loudness meter for iPhone. Two swipe pages with meters and spectrum. EBU R128 / ITU-R BS.1770-4. Background audio. Portrait and landscape.",
 "EBU R128 / ITU-R BS.1770-4 / BS.1771 Loudness-Metering: PPM, LUFS, True Peak, FFT, Goniometer, Sprachklarheit. macOS-, iPad- und iPhone-App.":
   "EBU R128 / ITU-R BS.1770-4 / BS.1771 loudness metering: PPM, LUFS, true peak, FFT, goniometer, speech clarity. macOS, iPad and iPhone app.",
 "Audio-Editor f\u00fcr iPhone und iPad. Audio aus der Dateien-App \u00f6ffnen, trimmen, auf EBU R128 -23 LUFS mit True-Peak-Limiter normalisieren, als 24-Bit-WAV exportieren. Round-Trip mit pegelWERK instant PLAYER.":
   "Audio editor for iPhone and iPad. Open audio from the Files app, trim it, normalise to EBU R128 -23 LUFS with a true-peak limiter, export as 24-bit WAV. Round trip with pegelWERK instant PLAYER.",
 "Gratis-Soundboard f\u00fcr iPhone und iPad. 64 Pads in 4 Banks, MULTI/SINGLE-Mode mit Cross-Fade, AUTO-CUE, LOOP, .satkip-Show-Bundle. Round-Trip mit pegelWERK easy EDITOR.":
   "Free soundboard for iPhone and iPad. 64 pads in 4 banks, MULTI/SINGLE mode with cross-fade, AUTO-CUE, LOOP, .satkip show bundle. Round trip with pegelWERK easy EDITOR.",
 "Offline EBU-R128-Korrektur auf dem iPad. 16 Delivery-Presets, Two-Pass mit Verify-and-Refine, 4x Polyphase TP-Limiter, Mono bis 9.1.6 Surround.":
   "Offline EBU R128 correction on the iPad. 16 delivery presets, two-pass with verify-and-refine, 4x polyphase TP limiter, mono to 9.1.6 surround.",
 "Offline-Lautheitskorrektur nach EBU R128, ATSC A/85, OTT, Spotify, YouTube. Two-Pass mit Verify-and-Refine auf +/-0,1 LU. macOS Standalone und iPad.":
   "Offline loudness correction to EBU R128, ATSC A/85, OTT, Spotify, YouTube. Two-pass with verify-and-refine to +/-0.1 LU. macOS standalone and iPad.",
 "Voice-Over gegen Bewegtbild auf dem iPad. Prompter mit Auto-Scroll, AutoEdit, AutoMix nach EBU R128, SmartDucker.":
   "Voice-over to picture on the iPad. Prompter with auto-scroll, AutoEdit, AutoMix to EBU R128, SmartDucker.",
 "Die DAW f\u00fcr Sprachproduktion - Voice-over, Beitrag, Podcast, H\u00f6rspiel. Assist mischt automatisch normgerecht (EBU R128, ATSC A/85, ARIB TR-B32, OP-59), Manual bietet den vollen DAW-Umfang: AU/VST3-Inserts, Einzelspur-Stems, Hardware-Konsolen, MXF-Delivery. Prompter und Script-Editor an Bord. F\u00fcr macOS; die iPad-App hei\u00dft voyzSESSION.":
   "The DAW for voice production - voice-over, news pieces, podcast, radio drama. Assist mixes automatically to standard (EBU R128, ATSC A/85, ARIB TR-B32, OP-59), Manual offers the full DAW scope: AU/VST3 inserts, single-track stems, hardware consoles, MXF delivery. Prompter and script editor on board. For macOS; the iPad app is called voyzSESSION.",
}

# Interne Links, die auf die englische Entsprechung zeigen sollen.
LINKMAP = {"/": "/en"}
for de_f, (en_f, de_p, en_p, _t, _d) in PAGES.items():
    if de_p != "/":
        LINKMAP[de_p] = en_p
    LINKMAP["/" + de_f] = en_p
    LINKMAP[de_f] = en_p
for slug in ("agb", "datenschutz", "impressum", "widerruf", "security"):
    LINKMAP["/" + slug] = "/" + slug + "-en"

GEN_NOTE = ("<!-- GENERIERT von tools/build-en.py aus %s - NICHT von Hand aendern.\n"
            "     Aenderungen gehoeren in die deutsche Seite bzw. ihre en:-i18n-Tabelle,\n"
            "     danach `python3 tools/build-en.py` neu laufen lassen. -->\n")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def parse_en_table(src):
    """Liest die en:-Tabelle als dict. Werte sind einfach gequotete JS-Strings."""
    ei = src.index("\n en: {")
    m = re.search(r"\n\s*\}\s*;", src[ei:])
    block = src[ei:ei + m.start()]
    out = {}
    for k, v in re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*'((?:[^'\\]|\\.)*)'\s*,?\s*$",
                           block, re.M):
        out[k] = v.replace("\\'", "'").replace('\\"', '"').replace("\\\\", "\\")
    return out


def replace_i18n(src, table, missing):
    """Ersetzt den Inhalt jedes [data-i18n]/[data-i18n-html]-Elements durch das Englische."""
    out, pos = [], 0
    pat = re.compile(r'<([a-zA-Z][\w-]*)\b[^>]*?data-i18n(-html)?="([^"]+)"[^>]*>')
    while True:
        m = pat.search(src, pos)
        if not m:
            out.append(src[pos:]); break
        tag, is_html, key = m.group(1), bool(m.group(2)), m.group(3)
        # passendes schliessendes Tag suchen (Verschachtelung gleichen Namens beachten)
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
                    inner_end = nc.start(); close_end = nc.end()
        val = table.get(key, HARDCODED_EN.get(key))
        out.append(src[pos:m.end()])
        if val is None:
            missing.add(key)
            out.append(src[m.end():inner_end])          # deutschen Text stehen lassen
        else:
            out.append(val if is_html else esc(val))
        out.append(src[inner_end:close_end])
        pos = close_end
    return "".join(out)


def apply_literals(src):
    """Ersetzt hartkodierte deutsche Literale - NUR in Textknoten ausserhalb von
    <script>/<style>. Attribute bleiben unberuehrt, insbesondere value=, das
    das Support-Formular absendet. Laengste Schluessel zuerst, damit
    "Allgemein / Sonstiges" nicht von "Sonstiges" zerlegt wird."""
    keys = sorted(LITERAL_EN, key=len, reverse=True)
    parts = re.split(r"(<script\b.*?</script>|<style\b.*?</style>)", src, flags=re.S)
    for i in range(0, len(parts), 2):
        seg = re.split(r"(<[^>]*>)", parts[i])        # ungerade Indizes = Tags
        for j in range(0, len(seg), 2):               # gerade Indizes = Textknoten
            for k in keys:
                seg[j] = seg[j].replace(k, LITERAL_EN[k])
        parts[i] = "".join(seg)
    out = "".join(parts)
    for de_txt, en_txt in PLACEHOLDER_EN.items():
        out = re.sub(r'placeholder="([^"]*)"',
                     lambda m: 'placeholder="%s"' % m.group(1).replace(de_txt, en_txt), out)
    return out


def rewrite_links(src):
    def rep(m):
        q, href = m.group(1), m.group(2)
        return 'href=%s%s%s' % (q, LINKMAP.get(href, href), q)
    return re.sub(r'href=(["\'])([^"\']+)\1', rep, src)


STRIP_SWITCH = re.compile(r"<script>\s*\nfunction switchLang.*?</script>\n?", re.S)


def hreflang_block(de_p, en_p):
    return ('<link rel="alternate" hreflang="de" href="%s%s">\n'
            '<link rel="alternate" hreflang="en" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">\n'
            % (BASE, de_p, BASE, en_p, BASE, de_p))


def build_en(de_file):
    en_file, de_p, en_p, title, desc = PAGES[de_file]
    src = io.open(de_file, encoding="utf-8").read()
    table = parse_en_table(src)
    missing = set()

    s = replace_i18n(src, table, missing)
    s = rewrite_links(s)
    s = s.replace('<html lang="de">', '<html lang="en">', 1)

    # Kopf: Titel, Description, Canonical, hreflang
    s = re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, s, count=1, flags=re.S)
    if re.search(r'<meta name="description" content=".*?">', s, re.S):
        s = re.sub(r'<meta name="description" content=".*?">',
                   '<meta name="description" content="%s">' % desc, s, count=1, flags=re.S)
    else:
        s = s.replace("</title>", "</title>\n<meta name=\"description\" content=\"%s\">" % desc, 1)
    s = re.sub(r'<link rel="canonical" href="[^"]*">',
               '<link rel="canonical" href="%s%s">' % (BASE, en_p), s, count=1)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', "", s)
    s = s.replace('<link rel="canonical" href="%s%s">' % (BASE, en_p),
                  '<link rel="canonical" href="%s%s">\n%s' % (BASE, en_p, hreflang_block(de_p, en_p).rstrip("\n")), 1)

    # JSON-LD auf die englische Fassung drehen
    s = s.replace('"url": "%s%s"' % (BASE, de_p), '"url": "%s%s"' % (BASE, en_p))
    s = re.sub(r'"inLanguage":\s*\[[^\]]*\]', '"inLanguage": "en"', s)
    s = re.sub(r'"inLanguage":\s*"de"', '"inLanguage": "en"', s)

    # Alt-Texte und JSON-LD-Descriptions uebersetzen
    for de_txt, en_txt in ALT_EN.items():
        s = s.replace('alt="%s"' % de_txt, 'alt="%s"' % en_txt)
    for de_txt, en_txt in JSONLD_DESC_EN.items():
        s = s.replace('"description": "%s"' % de_txt, '"description": "%s"' % en_txt)

    s = apply_literals(s)

    # BreadcrumbList: item-URLs auf die englischen Entsprechungen, Namen uebersetzen
    def _crumb(m):
        path = m.group(1) or "/"
        return '"item": "%s%s"' % (BASE, LINKMAP.get(path, path))
    s = re.sub(r'"item": "%s(/[a-z0-9-]*)?"' % re.escape(BASE), _crumb, s)
    s = s.replace('"name": "Startseite"', '"name": "Home"')

    # Sprachumschalter: navigiert, statt Text zu tauschen. Merkt die Wahl,
    # damit der Auto-Redirect den Besucher nicht sofort zurueckwirft.
    s = s.replace('onclick="setLang(\'de\')"', 'onclick="switchLang(\'de\',\'%s\')"' % de_p)
    s = s.replace('onclick="setLang(\'en\')"', 'onclick="switchLang(\'en\',\'%s\')"' % en_p)
    s = s.replace('<span class="lang active" id="btnDE"', '<span class="lang" id="btnDE"')
    s = s.replace('<span class="lang" id="btnEN"', '<span class="lang active" id="btnEN"')
    s = STRIP_SWITCH.sub("", s)
    s = s.replace("</head>", SWITCH_JS % ('de', de_p) + "</head>", 1)

    # Auto-setLang beim Laden entfernen - die Seite IST schon englisch
    s = re.sub(r"\n?try \{\n?\s*const saved = localStorage\.getItem\('satk-lang'\);\n?\s*"
               r"if \(saved === 'en'\) setLang\('en'\);\n?\s*\} catch\(e\)\{\}", "", s)

    s = s.replace("<!DOCTYPE html>", "<!DOCTYPE html>\n" + (GEN_NOTE % de_file).rstrip("\n"), 1)
    return en_file, s, missing


SWITCH_JS = """<script>
function switchLang(l,u){try{localStorage.setItem('satk-lang',l);}catch(e){}location.href=u;}
// Auto-redirect zur anderen Sprachfassung nur bei EXPLIZIT gesetzter Vorliebe
// (null/unset = hierbleiben, der Besucher hat diese URL bewusst aufgerufen)
try { if (localStorage.getItem('satk-lang') === '%s') { location.replace('%s'); } } catch(e){}
</script>
"""


def patch_de(de_file):
    """Die deutsche Seite bekommt hreflang, den navigierenden Umschalter und den Redirect."""
    en_file, de_p, en_p, _t, _d = PAGES[de_file]
    s = io.open(de_file, encoding="utf-8").read()
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', "", s)
    s = re.sub(r'(<link rel="canonical" href="[^"]*">\n)',
               r"\1" + hreflang_block(de_p, en_p), s, count=1)
    s = s.replace('onclick="setLang(\'de\')"', 'onclick="switchLang(\'de\',\'%s\')"' % de_p)
    s = s.replace('onclick="setLang(\'en\')"', 'onclick="switchLang(\'en\',\'%s\')"' % en_p)
    s = STRIP_SWITCH.sub("", s)
    s = s.replace("</head>", SWITCH_JS % ('en', en_p) + "</head>", 1)
    s = re.sub(r"\n?try \{\n?\s*const saved = localStorage\.getItem\('satk-lang'\);\n?\s*"
               r"if \(saved === 'en'\) setLang\('en'\);\n?\s*\} catch\(e\)\{\}", "", s)
    return s


if __name__ == "__main__":
    check = "--check" in sys.argv
    drift, allmiss = [], {}
    for de_file in sorted(PAGES):
        en_file, en_src, missing = build_en(de_file)
        de_src = patch_de(de_file)
        if missing:
            allmiss[de_file] = sorted(missing)
        if check:
            old = io.open(en_file, encoding="utf-8").read() if os.path.exists(en_file) else None
            if old != en_src:
                drift.append(en_file)
        else:
            io.open(en_file, "w", encoding="utf-8").write(en_src)
            io.open(de_file, "w", encoding="utf-8").write(de_src)
            print("  %-28s -> %s" % (de_file, en_file))
    if allmiss:
        print("\n  Ohne EN-Uebersetzung (deutscher Text bleibt stehen):")
        for f, ks in allmiss.items():
            print("    %-28s %s" % (f, ", ".join(ks)))
    if check:
        print("\n  DRIFT: %s" % (", ".join(drift) if drift else "keiner, alles aktuell"))
        sys.exit(1 if drift else 0)
