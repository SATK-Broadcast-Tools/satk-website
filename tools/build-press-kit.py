#!/usr/bin/env python3
"""Erzeugt Pressemitteilung, Faktenblatt und beide Press Kits fuer voyzSESSION.

WARUM ES DAS GIBT: bis 1.5.2 wurde das Material jedes Mal von Hand nachgebaut --
die Quell-HTML lag nie im Repo, nur die fertigen PDFs. Wer die naechste Version
ausliefern wollte, musste die Gestaltung aus einem PDF zurueckentwickeln
(Skia/PDF, Subset-Fonts, kein extrahierbarer Text). Beim 1.5.2-Durchgang sind
genau so zwei Abweichungen entstanden -- die gruene Linie unter dem Kopfband
fehlte, Band und Seitenrand waren zu schmal -- und eine dritte war schlimmer:
das Kit trug noch das limegruene Logo von VOR der Markenumstellung.

AUFRUF (im Wurzelverzeichnis des Website-Repos):

    python3 tools/build-press-kit.py

Schreibt press/*.pdf, press/*.zip und zieht press.html auf die neue Version
nach. Danach die vier PDFs ansehen -- der Generator prueft die Gestaltung nicht.

VORAUSSETZUNGEN: Google Chrome (druckt die PDFs) und die Schrift Inter im
System. Beides war schon da, als die 1.5.2-Fassung entstand.
"""
import os, re, shutil, subprocess, zipfile, pathlib, sys

ROOT  = pathlib.Path(__file__).resolve().parent.parent
PRESS = ROOT / "press"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

VERSION  = "1.6.0"
VTAG     = "160"                      # Cache-Buster in den Links: ?v=160
DATE_DE  = "21. September 2026"
DATE_EN  = "21 September 2026"
MONTH_DE = "September 2026"
MONTH_EN = "September 2026"

# ---------------------------------------------------------------- Inhalte ----
# Eine Quelle für PDF, Textfassung, Kit-Beilagen UND press.html. Wer hier
# etwas ändert, ändert es ueberall -- vorher liefen die Fassungen auseinander.

DE = {
 "kicker": "PRESSEMITTEILUNG",
 "headline": f"voyzSESSION {VERSION}: Aufnahme auf die Platte, Medienablage und Kapitel für Podcasts",
 "lead": "Die DAW für Sprachproduktion nimmt jetzt direkt in den Projektordner auf, bekommt eine "
         "durchsuchbare Medienablage mit Vorhören und liefert Podcasts mit Kapitelmarken aus.",
 "body": [
  f"<b>Siegburg, {DATE_DE}</b> &ndash; pegelWERK veröffentlicht Version {VERSION} von voyzSESSION, der DAW "
  "für Sprachproduktion. Es ist das größte Update seit dem Erstrelease: die Aufnahme wandert von "
  "Arbeitsspeicher auf die Platte, eine Medienablage kommt dazu, Podcasts bekommen Kapitel, und die "
  "Zeitleiste lässt sich bedienen wie in den großen DAWs.",

  "Aufgenommen wird ab dieser Version direkt in den Projektordner, in 32 Bit Fließkomma und unter dem "
  "Namen der Spur. Damit ist der Stillstand bei langen Sitzungen weg: bisher hielt das Programm jede "
  "Aufnahme vollständig im Arbeitsspeicher, und bei zehn Spuren begann macOS auszulagern. Speichern "
  "verknüpft die Dateien jetzt, statt sie zu kopieren &ndash; ein Projekt mit 29 GB Audio ist in Sekunden "
  "gesichert statt in Minuten und belegt den Platz nur einmal.",

  "Die neue Medienablage sitzt rechts neben der Zeitleiste, dort, wo Pro Tools seine Clip List hat. Sie "
  "durchsucht das Material des offenen Projekts, ein Klick hört vor, Ziehen legt auf die Spur. "
  "Vorgehört wird auf dem Pegel, den die Datei auf der Spur haben wird &ndash; ein gekaufter Jingle liegt "
  "gern 14 Dezibel über einem sendefertigen Programm und klingt hier trotzdem so wie nachher. Dasselbe "
  "Vorhören gibt es im Importdialog des Systems.",

  "Für Podcasts gibt es ein eigenes Kapitel-Fenster mit Zeit, Titel, Bild und Link. Ausgeliefert wird "
  "als MP3 mit ID3v2.3-Kapitelmarken, Titelbild und Folgenangaben, dazu eine Kapiteldatei nach "
  "Podcasting-2.0-Norm. Verfehlt das Titelbild die Vorgaben von Apple Podcasts, sagt das Programm es "
  "beim Auswählen &ndash; sonst erfährt man es Tage später vom Hoster.",

  "Neu sind außerdem Sitzungsvorlagen, das Dehnen eines Takes auf eine Bildlücke ohne "
  "Tonhöhenänderung und die Referenzstimme: die Klangfarbe einer Spur wird angelernt, jede andere "
  "Stimmspur lässt sich darauf abgleichen. Das Profil gehört dem Sprecher und steht in jedem Projekt "
  "zur Verfügung, damit eine Folge klingt wie die vorige.",

  "Bei den Formaten kommen FLAC, Opus und die AES31-3-Schnittliste dazu. Damit deckt voyzSESSION alle "
  "gängigen Liefer-Formate ab, und alles, was das Programm verlässt, wird an einer Stelle angehakt.",

  "Im Manual-Modus ist der AutoMix jetzt wirklich die Basis: Kanalzug und Pegelverlauf werden einmal je "
  "Spur übernommen, wie sie geklungen haben, und liegen als editierbare Keyframes auf der Spur. Dazu "
  "kommt Software-Monitoring nach DAW-Vorbild mit einem &bdquo;I&ldquo; je Stimmspur.",

  "Behoben sind drei Fehler, die im Betrieb die Arbeit anhalten konnten: nach einem Wechsel des "
  "Audio-Interfaces konnte alles stumm bleiben, gelöschte Aufnahmen überlebten das Speichern nicht, "
  "und eine Aufnahme, die nicht geschrieben werden konnte, hinterließ stille Lücken, ohne es zu sagen.",
 ],
 "bullets_h": f"NEU IN {VERSION}",
 "bullets": [
  "Aufnahme direkt in den Projektordner statt in den Arbeitsspeicher, in 32 Bit Fließkomma und unter dem Namen der Spur",
  "Speichern verknüpft die Audiodateien statt sie zu kopieren &ndash; ein Projekt mit 29 GB ist in Sekunden gesichert",
  "Medienablage mit Suche, Vorhören auf Zielpegel und Ziehen auf die Spur, auch im Importdialog des Systems",
  "Kapitel für Podcasts mit Zeit, Titel, Bild und Link; MP3 mit ID3v2.3-Kapitelmarken und Kapiteldatei nach Podcasting-2.0-Norm",
  "Sitzungsvorlagen für Spuren, Namen, Farben, DSP, Inserts, Gruppen und Prompter-Text",
  "Take auf eine Bildlücke dehnen (&bdquo;fit to picture&ldquo;), die Tonhöhe bleibt",
  "Referenzstimme: Klangfarbe anlernen und jede andere Stimmspur darauf abgleichen",
  "FLAC- und Opus-Export sowie AES31-3-Schnittlisten",
  "Zeitleiste verschieben und auf die Auswahl zoomen, Spur per Klick auf den Kopf wählen, Auswahl auf eine andere Spur ziehen",
  "Der AutoMix ist im Manual-Modus die Basis: Kanalzug und Pegelverlauf als editierbare Keyframes",
  "Software-Monitoring mit einem &bdquo;I&ldquo; je Stimmspur (AUTO INPUT und INPUT ONLY)",
  "Transkript im Skript-Editor per Doppelklick korrigierbar, ohne den Ton anzufassen",
  "Behoben: stummes Audiogerät nach Interfacewechsel, gelöschte Aufnahmen beim Speichern, stille Lücken bei vollem Datenträger",
 ],
 "avail_h": "VERFÜGBARKEIT",
 "avail": f"voyzSESSION {VERSION} steht ab sofort auf pegelwerk.com zum Download bereit. Für Bestandskunden "
          "ist das Update kostenlos. Das Abo kostet 24,99 EUR im Monat oder 249 EUR im Jahr, jeweils "
          "inklusive Mehrwertsteuer und monatlich kündbar. Sieben Tage lässt sich die Vollversion "
          "kostenlos testen &ndash; ohne Konto und ohne E-Mail-Adresse. voyzSESSION läuft auf macOS.",
 "about_h": "ÜBER PEGELWERK",
 "about": "pegelWERK ist eine unabhängige Audio-Software-Schmiede aus Siegburg, Deutschland, gegründet "
          "von Sascha Hömske. Das Lineup umfasst native Apps für macOS, iPadOS und iPhone rund um "
          "Broadcast, Postproduktion und Voiceover. Alle Apps teilen sich dieselbe EBU-R128-DSP-Engine. "
          "Mehr unter pegelwerk.com.",
 "contact": "<b>Pressekontakt</b> Sascha Hömske, pegelWERK &middot; info@pegelwerk.com &middot; Siegburg, "
            "Deutschland &middot; pegelwerk.com",
 "cleared": "Alle Materialien sind zur redaktionellen Verwendung freigegeben.",
 "fs_kicker": "FACT SHEET",
 "fs_title": "voyzSESSION &ndash; Fact Sheet",
 "fs_sub": "Die DAW für Sprachproduktion: Voice-over, Beitrag, Podcast, Hörspiel.",
 "fs_rows": [
  ("Produkt", "voyzSESSION &ndash; DAW für Sprachproduktion mit R128-Automatik und Handmodus"),
  ("Kategorie", "Voice-over- und Podcast-Produktion, Audio-Postproduktion, Broadcast-Auslieferung"),
  ("Plattformen", "macOS 12+ (Apple Silicon und Intel, Universal Binary) &middot; iPadOS"),
  ("Arbeitsweisen", "Assist-Modus mit Auto Edit, Auto DSP und Auto Mix &middot; Manual-Modus mit Kanalzügen, "
                    "Gruppen und Automation in Read, Touch, Latch und Write"),
  ("Aufnahme", "Direkt in den Projektordner, 32 Bit Fließkomma &middot; Overdub gegen Video oder Skript &middot; "
               "V-PUNCH, der sprachgesteuerte Ein- und Ausstieg &middot; sprachsynchroner Prompter, auch für "
               "PDF-Skripte &middot; Mehrspur mit Sprecher-Ausgleich &middot; Kabinenfenster für den Monitor beim "
               "Sprecher &middot; Software- und Hardware-Monitoring"),
  ("Bearbeitung", "Medienablage mit Suche und Vorhören auf Zielpegel &middot; Take auf eine Bildlücke dehnen, "
                  "ohne die Tonhöhe zu ändern &middot; Sitzungsvorlagen &middot; Kapitel für Podcasts"),
  ("Klang", "Neuronale Entrauschung (DeepFilterNet 3) &middot; Echtzeit-Sprachkette mit EQ, Kompressor, "
            "De-Esser, SmartLeveler &middot; Referenzstimme je Sprecher &middot; Musik- und FX-Bett mit Auto-Ducking"),
  ("Plugins", "AU und VST3, fünf Insert-Plätze je Kanal, dazu Voice-, IT/FX- und Master-Gruppe (macOS)"),
  ("Transkription", "Offline und wortgenau, Sprachmodell im Programm &middot; Script-Editor mit korrigierbarem "
                    "Transkript &middot; Untertitel als SubRip (.srt) und WebVTT (.vtt)"),
  ("Format-Profile", "EBU R128, ATSC A/85, ARIB TR-B32, OP-59, CST-RT-040 &middot; Podcast (-16 LUFS), YouTube "
                     "(-14 LUFS), Hörbuch, Doku, Sport &middot; Studio 0 dB ohne Normalisierung"),
  ("Auslieferung", "MXF mit acht Sound-Tracks, M&amp;E der Quelle bleibt erhalten &middot; Profile für ARD/ZDF "
                   "HDF01a, ARIB RDD9 und CST AS-10 &middot; Video-Mux &middot; WAV, AIFF, FLAC, AAC, MP3, MP2 und "
                   "Opus &middot; MP3 mit Kapitelmarken und Kapiteldatei &middot; AES31-3-Schnittliste (ADL)"),
  ("Schnittstellen", "Virtuelle Kamera und virtuelles Audiogerät &middot; Mackie MCU &middot; Elgato Stream Deck "
                     "&middot; OSC &middot; Web-Konsole für MakePro X"),
  ("Datenschutz", "Alles läuft lokal auf dem eigenen Rechner: kein Cloud-Sync, kein Upload, kein Streaming"),
  ("Technik", "Nativ in C++ auf JUCE 8"),
  ("Preis", "Abo 24,99 EUR im Monat oder 249 EUR im Jahr, inkl. MwSt., monatlich kündbar &middot; sieben Tage "
            "kostenlos testen, ohne Konto und ohne E-Mail"),
  ("Version", f"{VERSION} ({MONTH_DE})"),
  ("Hersteller", "pegelWERK &ndash; Sascha Hömske, Siegburg, Deutschland"),
  ("Web", "pegelwerk.com &middot; info@pegelwerk.com"),
 ],
 "card_summary": f"Stand {MONTH_DE}, Version {VERSION}. Aufgenommen wird jetzt direkt in den Projektordner "
                 "statt in den Arbeitsspeicher, womit der Stillstand bei langen Sitzungen entfällt. Neu sind "
                 "eine durchsuchbare Medienablage mit Vorhören, Kapitel für Podcasts samt ID3-Marken und "
                 "Kapiteldatei, Sitzungsvorlagen, das Dehnen eines Takes aufs Bild und die Referenzstimme. "
                 "Dazu FLAC, Opus und AES31-3. Kostenloses Update für Bestandskunden.",
}

EN = {
 "kicker": "PRESS RELEASE",
 "headline": f"voyzSESSION {VERSION}: Recording to disk, a media pool and podcast chapters",
 "lead": "The DAW for voice production now records straight into the project folder, gains a searchable "
         "media pool with auditioning, and delivers podcasts with chapter marks.",
 "body": [
  f"<b>Siegburg, Germany, {DATE_EN}</b> &ndash; pegelWERK releases version {VERSION} of voyzSESSION, the DAW "
  "for voice production. It is the biggest update since launch: recording moves from memory to disk, a "
  "media pool arrives, podcasts get chapters, and the timeline can be handled the way the big DAWs do it.",

  "From this version on, recording goes straight into the project folder, in 32-bit float and under the "
  "track’s name. That removes the stalls during long sessions: until now the app held every recording "
  "fully in memory, and with ten tracks macOS began to swap. Saving links the files instead of copying "
  "them &ndash; a project with 29 GB of audio is saved in seconds instead of minutes, and takes the space "
  "only once.",

  "The new media pool sits to the right of the timeline, where Pro Tools keeps its Clip List. It searches "
  "the open project’s material, a click auditions, dragging places the file on a track. Auditioning plays "
  "at the level the file will have on the track &ndash; a bought jingle often sits 14 decibels above a "
  "broadcast-ready programme and still sounds here the way it will later. The same auditioning works "
  "inside the system’s import dialog.",

  "For podcasts there is a chapter window of its own, with time, title, image and link. Delivery is MP3 "
  "with ID3v2.3 chapter marks, cover art and episode details, plus a chapter file to the Podcasting 2.0 "
  "spec. If the cover art misses Apple Podcasts’ requirements, the app says so while you pick it &ndash; "
  "otherwise you hear about it days later from the host.",

  "Also new are session templates, fitting a take to a gap in the picture without changing its pitch, and "
  "the reference voice: the tonal character of one track is learned, and any other voice track can be "
  "matched to it. The profile belongs to the speaker and is available in every project, so one episode "
  "sounds like the last.",

  "On formats, FLAC, Opus and the AES31-3 edit list are added. voyzSESSION now covers every common "
  "delivery format, and everything that leaves the app is ticked in one place.",

  "In manual mode the AutoMix really is the basis now: channel strip and level ride are taken over once "
  "per track, exactly as they sounded, and appear as editable keyframes. Alongside comes software "
  "monitoring the way DAWs do it, with an &ldquo;I&rdquo; on each voice track.",

  "Three bugs that could halt work are fixed: after switching audio interfaces everything could go silent, "
  "deleted recordings did not survive saving, and a recording that could not be written left silent gaps "
  "without saying so.",
 ],
 "bullets_h": f"NEW IN {VERSION}",
 "bullets": [
  "Recording straight into the project folder instead of into memory, in 32-bit float and under the track’s name",
  "Saving links the audio files instead of copying them &ndash; a 29 GB project is saved in seconds",
  "Media pool with search, auditioning at target level and drag-to-track, inside the system import dialog as well",
  "Podcast chapters with time, title, image and link; MP3 with ID3v2.3 chapter marks and a Podcasting 2.0 chapter file",
  "Session templates for tracks, names, colours, DSP, inserts, groups and prompter text",
  "Fit a take to a gap in the picture (&ldquo;fit to picture&rdquo;), pitch preserved",
  "Reference voice: learn a tonal character and match any other voice track to it",
  "FLAC and Opus export, plus AES31-3 edit lists",
  "Scroll and zoom the timeline to the selection, select a track from its head, drag a selection to another track",
  "In manual mode the AutoMix is the basis: channel strip and level ride as editable keyframes",
  "Software monitoring with an &ldquo;I&rdquo; on each voice track (AUTO INPUT and INPUT ONLY)",
  "Correct the transcript in the script editor by double-click, without touching the audio",
  "Fixed: dead audio device after an interface switch, deleted recordings lost on save, silent gaps on a full disk",
 ],
 "avail_h": "AVAILABILITY",
 "avail": f"voyzSESSION {VERSION} is available for download at pegelwerk.com. The update is free for existing "
          "customers. The subscription costs EUR 24.99 per month or EUR 249 per year, each including VAT and "
          "cancellable monthly. A full seven-day trial is available &ndash; no account, no email address. "
          "voyzSESSION runs on macOS.",
 "about_h": "ABOUT PEGELWERK",
 "about": "pegelWERK is an independent audio software company based in Siegburg, Germany, founded by Sascha "
          "Hömske. The lineup covers native apps for macOS, iPadOS and iPhone around broadcast, post "
          "production and voiceover. All apps share the same EBU R128 DSP engine. More at pegelwerk.com.",
 "contact": "<b>Press contact</b> Sascha Hömske, pegelWERK &middot; info@pegelwerk.com &middot; Siegburg, "
            "Germany &middot; pegelwerk.com",
 "cleared": "All materials are cleared for editorial use.",
 "fs_kicker": "FACT SHEET",
 "fs_title": "voyzSESSION &ndash; Fact Sheet",
 "fs_sub": "The DAW for voice production: voice-over, reporting, podcast, radio drama.",
 "fs_rows": [
  ("Product", "voyzSESSION &ndash; DAW for voice production with R128 automation and a manual mode"),
  ("Category", "Voice-over and podcast production, audio post production, broadcast delivery"),
  ("Platforms", "macOS 12+ (Apple Silicon and Intel, universal binary) &middot; iPadOS"),
  ("Modes", "Assist mode with auto edit, auto DSP and auto mix &middot; manual mode with channel strips, groups "
            "and automation in read, touch, latch and write"),
  ("Recording", "Straight into the project folder, 32-bit float &middot; overdub against video or script &middot; "
                "V-PUNCH, the voice-driven punch in and out &middot; voice-synced prompter, PDF scripts included "
                "&middot; multitrack with speaker matching &middot; booth window for the monitor at the speaker "
                "&middot; software and hardware monitoring"),
  ("Editing", "Media pool with search and auditioning at target level &middot; fit a take to a gap in the "
              "picture without changing pitch &middot; session templates &middot; podcast chapters"),
  ("Sound", "Neural noise removal (DeepFilterNet 3) &middot; real-time voice chain with EQ, compressor, "
            "de-esser, SmartLeveler &middot; reference voice per speaker &middot; music and FX bed with auto ducking"),
  ("Plugins", "AU and VST3, five insert slots per channel, plus voice, IT/FX and master group (macOS)"),
  ("Transcription", "Offline and word-accurate, speech model inside the app &middot; script editor with a "
                    "correctable transcript &middot; subtitles as SubRip (.srt) and WebVTT (.vtt)"),
  ("Format profiles", "EBU R128, ATSC A/85, ARIB TR-B32, OP-59, CST-RT-040 &middot; podcast (-16 LUFS), YouTube "
                      "(-14 LUFS), audiobook, documentary, sport &middot; Studio 0 dB without normalisation"),
  ("Delivery", "MXF with eight sound tracks, the source M&amp;E is preserved &middot; profiles for ARD/ZDF HDF01a, "
               "ARIB RDD9 and CST AS-10 &middot; video mux &middot; WAV, AIFF, FLAC, AAC, MP3, MP2 and Opus &middot; "
               "MP3 with chapter marks and a chapter file &middot; AES31-3 edit list (ADL)"),
  ("Interfaces", "Virtual camera and virtual audio device &middot; Mackie MCU &middot; Elgato Stream Deck &middot; "
                 "OSC &middot; web console for MakePro X"),
  ("Privacy", "Everything runs locally on your own machine: no cloud sync, no upload, no streaming"),
  ("Technology", "Native C++ on JUCE 8"),
  ("Price", "Subscription EUR 24.99 per month or EUR 249 per year, VAT included, cancellable monthly &middot; "
            "seven-day free trial, no account and no email"),
  ("Version", f"{VERSION} ({MONTH_EN})"),
  ("Vendor", "pegelWERK &ndash; Sascha Hömske, Siegburg, Germany"),
  ("Web", "pegelwerk.com &middot; info@pegelwerk.com"),
 ],
 "card_summary": f"As of {MONTH_EN}, version {VERSION}. Recording now goes straight into the project folder "
                 "instead of into memory, which removes the stalls during long sessions. New are a searchable "
                 "media pool with auditioning, podcast chapters with ID3 marks and a chapter file, session "
                 "templates, fitting a take to picture, and the reference voice. Plus FLAC, Opus and AES31-3. "
                 "Free update for existing customers.",
}

# ------------------------------------------------------------- Gestaltung ----
# Hausfarbe am 1.5.2-PDF abgemessen (#4FB99A), nicht geraten. Das Kopfband
# blutet über negative Raender aus dem Satzspiegel heraus; @page traegt die
# Raender, damit Folgeseiten denselben Rand bekommen.

CSS = """
/* Seitenrand 0 + Innenabstand im Satz: NUR so blutet das Kopfband bis an die
   Blattkante. Chrome druckt NICHTS ausserhalb des Seitenrand-Kastens, negative
   Raender werden abgeschnitten (am 21.09.2026 gemessen). Nebenwirkung, die das
   Original genauso hat: Folgeseiten beginnen buendig oben. */
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin:0; padding:0 16mm 18mm; font-family:'Inter', -apple-system, sans-serif;
       font-size:9.6pt; line-height:1.55; color:#23232a;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.band { background:#0a0a0b; color:#fff; margin:0 -16mm; padding:10mm 16mm 7mm;
        display:flex; align-items:center; justify-content:space-between;
        border-bottom:3px solid #4fb99a; }
.band img { width:52mm; }
.kicker { color:#4fb99a; font-size:7.6pt; font-weight:700; letter-spacing:.22em; }
h1 { font-size:20pt; line-height:1.2; margin:11mm 0 4mm; color:#0a0a0b; letter-spacing:-.01em; }
.lead { font-size:11.4pt; line-height:1.5; color:#7c7c88; margin:0 0 7mm; }
p { margin:0 0 3.6mm; }
h2 { color:#4fb99a; font-size:8pt; font-weight:700; letter-spacing:.22em;
     margin:8mm 0 3mm; text-transform:uppercase; }
ul { margin:0; padding:0; list-style:none; }
li { position:relative; padding-left:6mm; margin-bottom:2.6mm; }
li::before { content:''; position:absolute; left:0; top:1.55mm;
             width:1.9mm; height:1.9mm; background:#4fb99a; }
.box { background:#f4f6f5; border-left:3px solid #4fb99a; padding:4mm 5mm; margin:4mm 0 0; }
.box p { margin:0; }
.foot { margin-top:9mm; padding-top:3mm; border-top:1px solid #dcdce2;
        font-size:8pt; color:#7c7c88; }
.foot p { margin:0 0 1mm; }
table { width:100%; border-collapse:collapse; margin-top:7mm; }
td { vertical-align:top; padding:2.8mm 0; border-top:1px solid #e4e4ea; }
tr:first-child td { border-top:none; }
td.k { width:34mm; padding-right:5mm; color:#4fb99a; font-weight:700;
       font-size:8pt; letter-spacing:.06em; }
"""

def page(kicker, inner):
    logo = (ROOT / "logo-lockup-2.svg").as_uri()
    return f"""<!doctype html><html lang="de"><meta charset="utf-8">
<style>{CSS}</style>
<div class="band"><img src="{logo}" alt="pegelWERK"><span class="kicker">{kicker}</span></div>
{inner}</html>"""

def release_html(t):
    body = "".join(f"<p>{p}</p>" for p in t["body"])
    bl   = "".join(f"<li>{b}</li>" for b in t["bullets"])
    return page(t["kicker"], f"""
<h1>{t['headline']}</h1>
<p class="lead">{t['lead']}</p>
{body}
<h2>{t['bullets_h']}</h2><ul>{bl}</ul>
<h2>{t['avail_h']}</h2><div class="box"><p>{t['avail']}</p></div>
<h2>{t['about_h']}</h2><p>{t['about']}</p>
<div class="foot"><p>{t['contact']}</p><p>{t['cleared']}</p></div>""")

def factsheet_html(t):
    rows = "".join(f'<tr><td class="k">{k}</td><td>{v}</td></tr>' for k, v in t["fs_rows"])
    return page(t["fs_kicker"], f"""
<h1>{t['fs_title']}</h1>
<p class="lead">{t['fs_sub']}</p>
<table>{rows}</table>
<div class="foot"><p>{t['contact']}</p><p>{t['cleared']}</p></div>""")

# ------------------------------------------------------------- Textfassung ---
def plain(s):
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in [("&ndash;", "-"), ("&middot;", "-"), ("&bdquo;", '"'), ("&ldquo;", '"'),
                 ("&rdquo;", '"'), ("&amp;", "&")]:
        s = s.replace(a, b)
    return s

def release_txt(t):
    out = [t["kicker"], "", plain(t["headline"]), "", plain(t["lead"]), ""]
    out += [plain(p) for p in t["body"]]
    out += ["", t["bullets_h"], ""] + ["- " + plain(b) for b in t["bullets"]]
    out += ["", t["avail_h"], "", plain(t["avail"])]
    out += ["", t["about_h"], "", plain(t["about"])]
    out += ["", plain(t["contact"]), plain(t["cleared"])]
    return "\n".join(out) + "\n"

def factsheet_md(t):
    out = [f"# {plain(t['fs_title'])}", "", f"**{plain(t['fs_sub'])}**", ""]
    out += [f"- **{k}:** {plain(v)}" for k, v in t["fs_rows"]]
    return "\n".join(out) + "\n"

def readme(lang, t):
    rel = "Pressemitteilung zu Version" if lang == "de" else "press release for version"
    fs  = "Fact Sheet" if lang == "de" else "fact sheet"
    bp  = "Kurzprofil pegelWERK" if lang == "de" else "pegelWERK boilerplate"
    ic  = "App-Icon (1024x1024)" if lang == "de" else "app icon (1024x1024)"
    sc  = "Screenshot" if lang == "de" else "screenshot"
    lg  = "Hersteller-Logo" if lang == "de" else "vendor logo"
    hd  = "Inhalt:" if lang == "de" else "Contents:"
    ct  = "Pressekontakt" if lang == "de" else "Press contact"
    return (f"# pegelWERK voyzSESSION — Press Kit ({lang.upper()})\n\n{hd}\n"
            f"- press-release.pdf / .txt — {rel} {VERSION}\n"
            f"- fact-sheet.pdf / .md — {fs}\n"
            f"- boilerplate.txt — {bp}\n"
            f"- assets/voyzsession-icon.png — {ic}\n"
            f"- assets/voyzsession-hero.png — {sc}\n"
            f"- assets/pegelwerk-logo.png — {lg}\n\n"
            f"{plain(t['cleared'])}\n{ct}: Sascha Hömske · info@pegelwerk.com · pegelwerk.com\n")

# ------------------------------------------------------------------ Bauen ----
def to_pdf(html, out):
    tmp = pathlib.Path("/tmp") / (out.stem + ".html")
    tmp.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=4000", f"--print-to-pdf={out}", tmp.as_uri()],
                   check=True, capture_output=True)
    print(f"    {out.name}  {out.stat().st_size:,} Bytes")

def build():
    if not pathlib.Path(CHROME).exists():
        sys.exit("Google Chrome fehlt - es druckt die PDFs.")
    for lang, t in (("de", DE), ("en", EN)):
        print(f"==> {lang.upper()}")
        to_pdf(release_html(t),   PRESS / f"voyzsession-press-release-{lang}.pdf")
        to_pdf(factsheet_html(t), PRESS / f"voyzsession-fact-sheet-{lang}.pdf")

        stage = pathlib.Path("/tmp") / f"kit-{lang}" / lang
        shutil.rmtree(stage.parent, ignore_errors=True)
        (stage / "assets").mkdir(parents=True)
        (stage / "README.md").write_text(readme(lang, t), encoding="utf-8")
        (stage / "boilerplate.txt").write_text(plain(t["about"]) + "\n", encoding="utf-8")
        (stage / "fact-sheet.md").write_text(factsheet_md(t), encoding="utf-8")
        (stage / "press-release.txt").write_text(release_txt(t), encoding="utf-8")
        shutil.copy(PRESS / f"voyzsession-fact-sheet-{lang}.pdf",   stage / "fact-sheet.pdf")
        shutil.copy(PRESS / f"voyzsession-press-release-{lang}.pdf", stage / "press-release.pdf")
        # Bildmaterial IMMER aus press/assets/ - eine eigene Kopie im Kit ist
        # genau der Weg, auf dem Redaktionen bis 1.5.1 das alte Logo bekamen.
        for src, dst in (("pegelwerk-logo.png", "pegelwerk-logo.png"),
                         ("voyzsession-hero.png", "voyzsession-hero.png"),
                         ("voyzsession-icon.png", "voyzsession-icon.png")):
            shutil.copy(PRESS / "assets" / src, stage / "assets" / dst)

        zpath = PRESS / f"pegelwerk-voyzsession-press-kit-{lang}.zip"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(stage.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(stage.parent))
        print(f"    {zpath.name}  {zpath.stat().st_size:,} Bytes")

def patch_html():
    p = ROOT / "press.html"
    s = p.read_text(encoding="utf-8")
    before = s
    # NUR die Presse-Dateien. Ein blankes \?v=\d+ erwischt auch die
    # Favicon- und og:image-Marker -- die sind seitenweit und haben mit
    # der Programmversion nichts zu tun (am 21.09.2026 einmal passiert).
    # NUR die sechs voyzSESSION-Dateien. Ein blankes \?v=\d+ erwischt die
    # seitenweiten Favicon-Marker, und /press/ allein auch die Anhaenge der
    # ANDEREN Produkte -- beides am 21.09.2026 einmal passiert.
    s = re.sub(r"(/press/(?:pegelwerk-)?voyzsession-[A-Za-z0-9._-]+)\?v=\d+",
               rf"\g<1>?v={VTAG}", s)
    s = re.sub(r'(<div class="card-meta">pegelWERK voyzSESSION )[\d.]+(</div>)',
               rf"\g<1>{VERSION}\g<2>", s)
    # Die beiden Prosa-Felder stehen dreimal (sichtbarer Text + zwei Tabellen).
    s = re.sub(r'(data-i18n="latest_h">)[^<]*(</div>)',
               lambda m: m.group(1) + plain(DE["headline"]) + m.group(2), s)
    s = re.sub(r'(data-i18n="latest_p">)[^<]*(</p>)',
               lambda m: m.group(1) + plain(DE["card_summary"]) + m.group(2), s)
    for tbl, t in (("de", DE), ("en", EN)):
        start = s.index(f"\n {tbl}: {{")
        end   = s.index("\n }", start)
        chunk = s[start:end]
        chunk = re.sub(r"(latest_h: ')[^']*(')", lambda m, t=t: m.group(1) + plain(t["headline"]) + m.group(2), chunk)
        chunk = re.sub(r"(latest_p: ')[^']*(')", lambda m, t=t: m.group(1) + plain(t["card_summary"]) + m.group(2), chunk)
        s = s[:start] + chunk + s[end:]
    p.write_text(s, encoding="utf-8")
    print("==> press.html", "geändert" if s != before else "unveraendert")

if __name__ == "__main__":
    build()
    patch_html()
    print(f"\nFertig. Jetzt die vier PDFs ANSEHEN - der Generator prueft keine Gestaltung.")
