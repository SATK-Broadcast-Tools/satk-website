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

VERSION  = "2.0"
VTAG     = "200"                      # Cache-Buster in den Links: ?v=200
DATE_DE  = "18. November 2026"
DATE_EN  = "18 November 2026"
MONTH_DE = "November 2026"
MONTH_EN = "November 2026"

# ---------------------------------------------------------------- Inhalte ----
# Eine Quelle für PDF, Textfassung, Kit-Beilagen UND press.html. Wer hier
# etwas ändert, ändert es ueberall -- vorher liefen die Fassungen auseinander.
# 2.0 (16./17.11.2026): keine fremden Produktnamen im Text (Nutzerregel 13.10.);
# Schnittstellen-Namen (Stream Deck, MCU) bleiben, sie beschreiben Kompatibilitaet.

DE = {
 "kicker": "PRESSEMITTEILUNG",
 "headline": f"voyzSESSION PRO {VERSION}: Die komplette Sprachproduktion in einer Anwendung, vom Prompter bis zum <span style=\"white-space:nowrap\">Sende-MXF</span>",
 "lead": "voyzSESSION PRO 2.0 bündelt, was in der Sprachproduktion sonst auf mehrere Programme und "
         "Plugin-Pakete verteilt ist. Die Anwendung reicht von der Aufnahme gegen Bild und Skript über die "
         "Klangbearbeitung und eine automatische Mischung, die jede Stimme vorher vermisst, bis zur "
         "sendefertigen Datei.",
 "body": [
  f"<b>Siegburg, {DATE_DE}</b> &ndash; pegelWERK veröffentlicht Version {VERSION} von voyzSESSION PRO, der "
  "DAW für Sprachproduktion. Für einen vertonten Beitrag, einen Podcast oder ein Hörspiel braucht man bisher "
  "in der Regel mehrere Werkzeuge: eine DAW, Plugin-Pakete für den Klang, einen Teleprompter, einen "
  "Transkriptionsdienst und ein Programm für die Auslieferung. voyzSESSION PRO 2.0 vereint diese Aufgaben in "
  "einer Anwendung. Alle dafür nötigen Klangbausteine sind enthalten, Software von Drittanbietern wird nicht "
  "gebraucht. Wer eigene Plugins einsetzen möchte, kann das trotzdem tun.",

  "Bei der Aufnahme läuft der Prompter per Spracherkennung mit dem Sprecher mit. Ein Kabinenfenster zeigt ihm "
  "Text, Bild und Timecode. Verspricht er sich, findet die Funktion V-PUNCH anhand des Gesprochenen die "
  "Stelle, an der er neu einsetzt. Aufgenommen wird gegen das Video und direkt in den Projektordner.",

  "Für den Klang hat jede Spur einen Kanalzug mit neun eigenen Modulen, von der Restauration über "
  "Entrauschen, EQ, De-Esser und Kompressor bis zum Hall. Die Module zeigen die Werte, mit denen sie "
  "tatsächlich arbeiten, denn Kurven und Anzeigen werden aus denselben Daten berechnet wie der Klang. Die "
  "Reihenfolge der Module lässt sich ändern, und es gibt Werks- und eigene Presets.",

  "Im Mittelpunkt steht der AUTO MIX. Er misst vor dem Mischen jede Stimme einzeln aus, also ihre "
  "Klangfarbe, ihr Pegelverhalten und wie scharf ihre S-Laute sind. Danach stellt er EQ, Kompressor und "
  "De-Esser passend zu dieser Stimme ein, beim Sprecher ebenso wie beim O-Ton. Beim Sprecher behandelt er "
  "außerdem Atmer und Klicks an den Stellen, an denen sie vorkommen. Der AUTO MIX arbeitet auch mit "
  "ungepegeltem Rohmaterial. Jede Spurart hat ein eigenes Pegelziel, Sprecher und O-Ton stehen im "
  "Vordergrund, Musik und Atmo werden darunter gemischt, und eine eigene Einstellung für Stadionatmo hält "
  "diese gleichmäßig. Das Ergebnis ist eine sendefertige Mischung nach dem gewählten Lautheitsprofil.",

  "voyzSESSION PRO hat zwei Arbeitsweisen. Im Assist-Modus erreichen auch Anwender ohne Erfahrung im Ton ein "
  "professionelles Ergebnis. Der Manual-Modus richtet sich an Tonprofis und arbeitet wie eine "
  "professionelle DAW, mit Master-Fader, Automation und einem Trim-Modus für gezielte Korrekturen an "
  "einzelnen Stellen. Was der AUTO MIX ermittelt hat, ist dort als Einstellung im jeweiligen Modul "
  "sichtbar und kann weiterbearbeitet werden. Auch die Pegelkurve der Stimme und das Absenken der Musik "
  "unter der Sprache liegen sichtbar auf den Spuren.",

  "Für die Auslieferung schreibt voyzSESSION PRO MXF-Dateien mit acht Tonspuren, unter anderem nach den "
  "Lieferprofilen von ARD und ZDF. Das Bild wird dabei unverändert übernommen, und Tonspuren der Quelle, "
  "die nicht ersetzt werden, bleiben bitgleich erhalten. Daneben stehen die gängigen Audioformate zur "
  "Verfügung, MP3 mit Kapitelmarken für Podcasts, Untertitel aus der Transkription und Schnittlisten im "
  "AES31-Format. Alle Berechnungen laufen auf dem eigenen Rechner, es werden keine Daten in eine Cloud "
  "geladen.",

  "Neu in Version 2.0 sind außerdem sechs Sprachen für die Bedienoberfläche (Deutsch, Englisch, "
  "Französisch, Spanisch, Italienisch und Portugiesisch), Spuren, die sich umsortieren lassen, eine "
  "Navigationszeile und Projekteinstellungen für Abtastrate, Bildrate und Startzeitcode. voyzSESSION PRO "
  "2.0 läuft ab macOS 14 Sonoma. Empfohlen wird ein Mac mit Apple-Prozessor (M1 oder neuer) und "
  "mindestens 16 GB Arbeitsspeicher, weil AUTO MIX, Entrauschen und Transkription dort deutlich schneller "
  "laufen.",
 ],
 "bullets_h": f"NEU IN {VERSION}",
 "bullets": [
  "Alles in einer Anwendung: Prompter, Aufnahme gegen Bild, Klangbearbeitung, AUTO MIX, Transkription und Sende-Auslieferung, ohne Drittanbieter-Software",
  "Kanalzug mit neun Modulen: Restauration, Entrauschen, EQ, Resonanz, De-Esser, Kompressor, De-Breath, Saturate, Hall",
  "Modulfenster mit echten Parametern, Werks- und eigenen Presets; Anzeigen aus denselben Werten wie der Klang",
  "Signalfolge im Kanalzug änderbar; eigene Kanalzüge für Gruppen und Master",
  "AUTO MIX für ungepegeltes Rohmaterial: Pegelziel je Rolle, Sprecher und O-Ton führen, neue Rolle Stadion",
  "Pegelarbeit sichtbar: Ritt der Stimme als Linie am Take, Ducks als Automation auf der Spur",
  "Analyse vor dem Mischen: EQ, Kompressor und De-Esser je Stimme aus Klangfarbe, Dynamik und S-Schärfe eingestellt, für Sprecher und O-Ton",
  "Manual-Modus nach DAW-Standard: rohe Abhöre, Export als reiner Bounce, Normalisieren nur auf Wunsch",
  "Master-Fader mit Automation; Automation für Pan, Mute und Plugin-Parameter; Trim-Modus",
  "Aufnahme-Mithören nach dem Auto-Input-Prinzip; das Mikrofon läuft durch die Kette seiner Spur",
  "Spuren umsortieren, Navigationszeile, Projekteinstellungen mit Abtastrate, Bildrate und Startzeitcode",
  "Sechs Sprachen: Deutsch, Englisch, Französisch, Spanisch, Italienisch, Portugiesisch",
  "Rückfrage beim Beenden mit ungespeicherten Änderungen",
  "Ab macOS 14 Sonoma; empfohlen: Mac mit Apple-Prozessor und 16 GB",
 ],
 "avail_h": "VERFÜGBARKEIT",
 "avail": f"voyzSESSION PRO {VERSION} steht ab sofort auf pegelwerk.com zum Download bereit. Für Bestandskunden "
          "ist das Update kostenlos. Das Abo kostet 24,99 EUR im Monat oder 249 EUR im Jahr, jeweils "
          "inklusive Mehrwertsteuer und monatlich kündbar. Sieben Tage lässt sich die Vollversion "
          "kostenlos testen &ndash; ohne Konto und ohne E-Mail-Adresse. voyzSESSION PRO läuft ab macOS 14 Sonoma; "
          "empfohlen ist ein Mac mit Apple-Prozessor.",
 "about_h": "ÜBER PEGELWERK",
 "about": "pegelWERK ist eine unabhängige Audio-Software-Schmiede aus Siegburg, Deutschland, gegründet "
          "von Sascha Hömske. Das Lineup umfasst native Apps für macOS, iPadOS und iPhone rund um "
          "Broadcast, Postproduktion und Voiceover. Alle Apps teilen sich dieselbe EBU-R128-DSP-Engine. "
          "Mehr unter pegelwerk.com.",
 "contact": "<b>Pressekontakt</b> Sascha Hömske, pegelWERK &middot; info@pegelwerk.com &middot; Siegburg, "
            "Deutschland &middot; pegelwerk.com",
 "cleared": "Alle Materialien sind zur redaktionellen Verwendung freigegeben.",
 "fs_kicker": "FACT SHEET",
 "fs_title": "voyzSESSION PRO &ndash; Fact Sheet",
 "fs_sub": "Die DAW für Sprachproduktion: Voice-over, Beitrag, Podcast, Hörspiel.",
 "fs_rows": [
  ("Produkt", "voyzSESSION PRO &ndash; DAW für Sprachproduktion mit AUTO MIX und Manual-Modus nach DAW-Standard"),
  ("Kategorie", "Voice-over- und Podcast-Produktion, Audio-Postproduktion, Broadcast-Auslieferung"),
  ("Systeme", "macOS 14 Sonoma oder neuer &middot; empfohlen: Mac mit Apple-Prozessor (M1 oder neuer) und "
              "16 GB Arbeitsspeicher, 32 GB für lange Projekte mit 4K-Video &middot; Intel-Macs laufen weiterhin "
              "&middot; iPadOS als eigene App"),
  ("Arbeitsweisen", "Assist-Modus mit Auto Edit, Auto DSP und AUTO MIX &middot; Manual-Modus mit Kanalzügen, "
                    "Gruppen, Master-Fader und Automation in Read, Touch, Latch, Write und Trim"),
  ("Kanalzug", "Neun Module: Restauration (De-Click, De-Plosive), Entrauschen, EQ mit dynamischen Bändern, "
               "Resonanz, De-Esser, Kompressor, De-Breath, Saturate, Hall &middot; Werks- und eigene Presets "
               "&middot; Signalfolge änderbar &middot; Referenzstimme je Sprecher"),
  ("AUTO MIX", "Analysiert jede Stimme vor dem Mischen (Klangfarbe, Dynamik, S-Schärfe, Atmer, Klicks) und "
               "stellt EQ, Kompressor und De-Esser je Sprecher und O-Ton ein, beim Sprecher zusätzlich De-Breath und "
               "De-Click &middot; für "
               "ungepegeltes Rohmaterial &middot; Pegelziel je Rolle (Sprecher, O-Ton, Musik, Atmo, Stadion u. a.) "
               "&middot; Ritt der Stimme als Linie am Take, Ducks als Automation"),
  ("Aufnahme", "Direkt in den Projektordner, 32 Bit Fließkomma &middot; Overdub gegen Video oder Skript &middot; "
               "V-PUNCH, der sprachgesteuerte Ein- und Ausstieg &middot; sprachsynchroner Prompter, auch für "
               "PDF-Skripte &middot; Mehrspur &middot; Kabinenfenster für den Monitor beim Sprecher &middot; "
               "Auto Input, Software- und Hardware-Monitoring"),
  ("Bearbeitung", "Medienablage mit Suche und Vorhören auf Zielpegel &middot; Spuren umsortieren &middot; "
                  "Navigationszeile &middot; Take auf eine Bildlücke dehnen &middot; Sitzungsvorlagen &middot; "
                  "Kapitel für Podcasts"),
  ("Plugins", "AU und VST3, fünf Insert-Plätze je Kanal, dazu Voice-, IT- und Master-Gruppe"),
  ("Transkription", "Offline und wortgenau, Sprachmodell im Programm &middot; Script-Editor mit korrigierbarem "
                    "Transkript &middot; Untertitel als SubRip (.srt) und WebVTT (.vtt)"),
  ("Format-Profile", "EBU R128, ATSC A/85, ARIB TR-B32, OP-59, CST-RT-040 &middot; Podcast (-16 LUFS), YouTube "
                     "(-14 LUFS), Hörbuch, Doku, Sport &middot; Studio 0 dB ohne Normalisierung"),
  ("Auslieferung", "MXF mit acht Sound-Tracks, Bild unverändert durchgereicht, nicht ersetzte Tonspuren der "
                   "Quelle bitgleich &middot; Profile für ARD/ZDF HDF01a, ARIB RDD9 und CST AS-10 &middot; "
                   "Video-Mux &middot; WAV, AIFF, FLAC, AAC, MP3, MP2 und Opus &middot; MP3 mit Kapitelmarken "
                   "&middot; AES31-3-Schnittliste (ADL)"),
  ("Schnittstellen", "Virtuelle Kamera und virtuelles Audiogerät &middot; Mackie MCU &middot; Elgato Stream Deck "
                     "&middot; OSC"),
  ("Sprachen", "Deutsch, Englisch, Französisch, Spanisch, Italienisch, Portugiesisch"),
  ("Datenschutz", "Alles läuft lokal auf dem eigenen Rechner: kein Cloud-Sync, kein Upload, kein Streaming"),
  ("Technik", "Nativ in C++"),
  ("Preis", "Abo 24,99 EUR im Monat oder 249 EUR im Jahr, inkl. MwSt., monatlich kündbar &middot; sieben Tage "
            "kostenlos testen, ohne Konto und ohne E-Mail"),
  ("Version", f"{VERSION} ({MONTH_DE})"),
  ("Hersteller", "pegelWERK &ndash; Sascha Hömske, Siegburg, Deutschland"),
  ("Web", "pegelwerk.com &middot; info@pegelwerk.com"),
 ],
 "card_summary": f"Stand {MONTH_DE}, Version {VERSION}. Die komplette Sprachproduktion in einer Anwendung: ein Kanalzug mit "
                 "neun Modulen, ein Manual-Modus nach DAW-Standard mit Master-Fader und Trim, und ein AUTO MIX "
                 "für ungepegeltes Rohmaterial mit sichtbarer Pegelarbeit. Sechs Sprachen, ab macOS 14, "
                 "empfohlen auf Macs mit Apple-Prozessor. Kostenloses Update für Bestandskunden.",
}

EN = {
 "kicker": "PRESS RELEASE",
 "headline": f"voyzSESSION PRO {VERSION}: The complete voice production in one application, from prompter to broadcast MXF",
 "lead": "voyzSESSION PRO 2.0 brings together what voice production otherwise spreads across several "
         "programs and plugin bundles. The application covers recording against picture and script, sound "
         "processing, an automatic mix that measures every voice first, and the finished broadcast file.",
 "body": [
  f"<b>Siegburg, {DATE_EN}</b> &ndash; pegelWERK releases version {VERSION} of voyzSESSION PRO, the DAW for "
  "voice production. A voiced report, a podcast or a radio drama has so far usually required several tools: "
  "a DAW, plugin bundles for the sound, a teleprompter, a transcription service and a program for delivery. "
  "voyzSESSION PRO 2.0 handles these tasks in one application. All the sound processors the work needs are "
  "included, and no third-party software is required. Users who want to add their own plugins can still do "
  "so.",

  "During recording the prompter follows the narrator via speech recognition. A booth window shows the "
  "narrator text, picture and timecode. After a slip of the tongue, the V-PUNCH function uses what was said "
  "to find the point where the narrator picks up again. Recording runs against the video and goes straight "
  "into the project folder.",

  "For the sound, every track has a channel strip with nine in-house modules, from restoration through noise "
  "reduction, EQ, de-esser and compressor to reverb. The modules show the values they actually work with, "
  "because curves and displays are computed from the same data as the sound. The order of the modules can "
  "be changed, and there are factory and user presets.",

  "At the centre is AUTO MIX. Before mixing, it measures every voice on its own, meaning its timbre, its "
  "level behaviour and how sharp its sibilants are. It then sets EQ, compressor and de-esser to suit this "
  "voice, for the narrator as well as for original sound. On the narrator it also treats breaths and clicks "
  "where they occur. AUTO MIX also works with unlevelled raw material. Every kind of track has its own level "
  "target, narrator and original sound stay in front, music and ambience are mixed below them, and a "
  "dedicated setting for stadium atmosphere keeps it steady. The result is a broadcast-ready mix to the "
  "chosen loudness profile.",

  "voyzSESSION PRO offers two ways of working. In Assist mode, users without audio experience still reach a "
  "professional result. Manual mode is aimed at audio professionals and works like a professional DAW, with "
  "a master fader, automation and a trim mode for targeted corrections at individual spots. Whatever AUTO "
  "MIX has determined is visible there as a setting in the relevant module and can be edited further. The "
  "level curve of the voice and the lowering of the music under speech are also shown on the tracks.",

  "For delivery, voyzSESSION PRO writes MXF files with eight audio tracks, including to the delivery "
  "profiles of German public broadcasters ARD and ZDF. The picture is carried over unchanged, and source "
  "audio tracks that are not replaced stay bit-identical. The common audio formats are also available, plus "
  "MP3 with chapter marks for podcasts, subtitles from the transcription and AES31 edit lists. All "
  "processing runs on the user's own machine, and no data is uploaded to a cloud.",

  "Also new in version 2.0 are six interface languages (German, English, French, Spanish, Italian and "
  "Portuguese), reorderable tracks, a navigation bar and project settings for sample rate, frame rate and "
  "start timecode. voyzSESSION PRO 2.0 runs on macOS 14 Sonoma or later. A Mac with Apple silicon (M1 or "
  "newer) and at least 16 GB of memory is recommended, because AUTO MIX, noise reduction and transcription "
  "run much faster there.",
 ],
 "bullets_h": f"NEW IN {VERSION}",
 "bullets": [
  "Everything in one application: prompter, recording to picture, sound processing, AUTO MIX, transcription and broadcast delivery, no third-party software needed",
  "Channel strip with nine modules: restoration, noise reduction, EQ, resonance, de-esser, compressor, de-breath, saturate, reverb",
  "Module windows with real parameters, factory and user presets; displays computed from the same values as the sound",
  "Signal order in the channel strip can be changed; own channel strips for groups and master",
  "AUTO MIX for unlevelled raw material: level target per role, narrator and original sound lead, new Stadium role",
  "Level work made visible: voice ride as a line on the take, ducks as automation on the track",
  "Analysis before mixing: EQ, compressor and de-esser set per voice from timbre, dynamics and sibilance, for narrator and original sound",
  "Manual mode to DAW standard: raw monitoring, export as a plain bounce, normalisation only on request",
  "Master fader with automation; automation for pan, mute and plugin parameters; trim mode",
  "Input monitoring on the auto-input principle; the microphone runs through the chain of its track",
  "Reorder tracks, navigation bar, project settings with sample rate, frame rate and start timecode",
  "Six languages: German, English, French, Spanish, Italian, Portuguese",
  "Prompt to save unsaved changes when quitting",
  "macOS 14 Sonoma or later; recommended: Mac with Apple silicon and 16 GB",
 ],
 "avail_h": "AVAILABILITY",
 "avail": f"voyzSESSION PRO {VERSION} is available for download at pegelwerk.com. The update is free for existing "
          "customers. The subscription costs EUR 24.99 per month or EUR 249 per year, VAT included, cancellable "
          "monthly. The full version can be tried free for seven days &ndash; no account and no email address "
          "needed. voyzSESSION PRO runs on macOS 14 Sonoma or later; a Mac with Apple silicon is recommended.",
 "about_h": "ABOUT PEGELWERK",
 "about": "pegelWERK is an independent audio software company based in Siegburg, Germany, founded by Sascha "
          "Hömske. The lineup covers native apps for macOS, iPadOS and iPhone around broadcast, post production "
          "and voice-over. All apps share the same EBU R128 DSP engine. More at pegelwerk.com.",
 "contact": "<b>Press contact</b> Sascha Hömske, pegelWERK &middot; info@pegelwerk.com &middot; Siegburg, "
            "Germany &middot; pegelwerk.com",
 "cleared": "All materials are cleared for editorial use.",
 "fs_kicker": "FACT SHEET",
 "fs_title": "voyzSESSION PRO &ndash; Fact Sheet",
 "fs_sub": "The DAW for voice production: voice-over, reporting, podcast, radio drama.",
 "fs_rows": [
  ("Product", "voyzSESSION PRO &ndash; DAW for voice production with AUTO MIX and a manual mode built to DAW standard"),
  ("Category", "Voice-over and podcast production, audio post production, broadcast delivery"),
  ("Systems", "macOS 14 Sonoma or later &middot; recommended: Mac with Apple silicon (M1 or newer) and 16 GB of "
              "memory, 32 GB for long projects with 4K video &middot; Intel Macs still run &middot; iPadOS as a "
              "separate app"),
  ("Modes", "Assist mode with auto edit, auto DSP and AUTO MIX &middot; manual mode with channel strips, groups, "
            "master fader and automation in read, touch, latch, write and trim"),
  ("Channel strip", "Nine modules: restoration (de-click, de-plosive), noise reduction, EQ with dynamic bands, "
                    "resonance, de-esser, compressor, de-breath, saturate, reverb &middot; factory and user presets "
                    "&middot; signal order can be changed &middot; reference voice per narrator"),
  ("AUTO MIX", "Analyses every voice before mixing (timbre, dynamics, sibilance, breaths, clicks) and sets EQ, "
               "compressor and de-esser per narrator and original sound, plus de-breath and de-click on the narrator "
               "&middot; for "
               "unlevelled raw material &middot; level target per role (narrator, original sound, music, ambience, "
               "stadium and more) &middot; voice ride as a line on the take, ducks as automation"),
  ("Recording", "Straight into the project folder, 32-bit float &middot; overdub against video or script &middot; "
                "V-PUNCH, the voice-driven punch in and out &middot; speech-synced prompter, PDF scripts included "
                "&middot; multitrack &middot; booth window for the narrator's monitor &middot; auto input, "
                "software and hardware monitoring"),
  ("Editing", "Media pool with search and auditioning at target level &middot; reorder tracks &middot; navigation "
              "bar &middot; fit a take to a picture gap &middot; session templates &middot; podcast chapters"),
  ("Plugins", "AU and VST3, five insert slots per channel, plus voice, IT and master group"),
  ("Transcription", "Offline and word-accurate, speech model built in &middot; script editor with correctable "
                    "transcript &middot; subtitles as SubRip (.srt) and WebVTT (.vtt)"),
  ("Loudness profiles", "EBU R128, ATSC A/85, ARIB TR-B32, OP-59, CST-RT-040 &middot; podcast (-16 LUFS), YouTube "
                        "(-14 LUFS), audiobook, documentary, sport &middot; studio 0 dB without normalisation"),
  ("Delivery", "MXF with eight sound tracks, picture passed through unchanged, source tracks not replaced stay "
               "bit-identical &middot; profiles for ARD/ZDF HDF01a, ARIB RDD9 and CST AS-10 &middot; video mux "
               "&middot; WAV, AIFF, FLAC, AAC, MP3, MP2 and Opus &middot; MP3 with chapter marks &middot; "
               "AES31-3 edit list (ADL)"),
  ("Interfaces", "Virtual camera and virtual audio device &middot; Mackie MCU &middot; Elgato Stream Deck "
                 "&middot; OSC"),
  ("Languages", "German, English, French, Spanish, Italian, Portuguese"),
  ("Privacy", "Everything runs locally on your own machine: no cloud sync, no upload, no streaming"),
  ("Technology", "Native C++"),
  ("Price", "Subscription EUR 24.99 per month or EUR 249 per year, VAT included, cancellable monthly &middot; "
            "seven-day free trial, no account and no email"),
  ("Version", f"{VERSION} ({MONTH_EN})"),
  ("Vendor", "pegelWERK &ndash; Sascha Hömske, Siegburg, Germany"),
  ("Web", "pegelwerk.com &middot; info@pegelwerk.com"),
 ],
 "card_summary": f"As of {MONTH_EN}, version {VERSION}. The complete voice production in one application: a channel "
                 "strip with nine modules, a manual mode built to DAW standard with master fader and trim, and "
                 "an AUTO MIX for unlevelled raw material with visible level work. Six languages, macOS 14 or "
                 "later, recommended on Macs with Apple silicon. Free update for existing customers.",
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
    return (f"# pegelWERK voyzSESSION PRO — Press Kit ({lang.upper()})\n\n{hd}\n"
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
    s = re.sub(r'(<div class="card-meta">pegelWERK voyzSESSION)(?: PRO)? [\d.]+(</div>)',
               rf"\g<1> PRO {VERSION}\g<2>", s)
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
