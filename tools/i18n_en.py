#!/usr/bin/env python3
"""Englische Daten fuer tools/build-i18n.py (frueher tools/build-en.py).

Die englischen Texte der Produktseiten stehen weiterhin in der en:-Tabelle der
jeweiligen deutschen Seite. Hier liegt nur, was dort NICHT steht: Seitenliste,
Titel und Descriptions, hartkodierte Literale, Alt-Texte, JSON-LD.
Aufruf und Ablauf: siehe tools/build-i18n.py.
"""

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
   "Offline EBU R128 loudness correction on the iPad. 14 delivery presets, two-pass with verify-and-refine, 4x polyphase true-peak limiter."),
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
 "Native (unverändert)": "Native (unchanged)",
 "Wraparound zum Cue-Punkt": "Wraparound to the cue point",
}

# Spezifikationslisten <li><b>Label</b> Wert</li> ohne data-i18n. Gilt nur fuer
# GANZE Labels bzw. Werte (build-i18n.py, spec()). Schluessel ohne HTML-Entities.
SPEC_EN = {
 "Aktionen": "Actions",
 "Histogramme": "Histograms",
 "LFE-Gewicht": "LFE weight",
 "Modi": "Modes",
 "PPM-Skala": "PPM scale",
 "Profil": "Profile",
 "Sprache": "Language",
 "Tastatur": "Keyboard",
 "Stille-Skip am Anfang": "Skips leading silence",
 "externe Interfaces (RME, UA, ...)": "external interfaces (RME, UA, ...)",
 "Audio-Mode aktiv": "audio mode active",
 "Mono bis 9.1.6 (16)": "Mono to 9.1.6 (16)",
 "Linkwitz-Riley 4. Ordnung": "4th-order Linkwitz-Riley",
 "3-Band Linkwitz-Riley 4. Ordnung": "3-band 4th-order Linkwitz-Riley",
 "0 (BS.1770-konform)": "0 (BS.1770-compliant)",
 "iPad (iPhone via HW-Tasten)": "iPad (iPhone via hardware buttons)",
 "Name · Farbe · Vol": "Name · colour · vol",
 "kein Server, keine Analytics": "no server, no analytics",
 "50 ms exponentiell": "50 ms exponential",
 "Hintergrund-Thread": "background thread",
 "folgt Audio-Hardware / DAW": "follows audio hardware / DAW",
 "folgt Audio-Hardware": "follows audio hardware",
 "English UI": "English UI",
 "Dateien · iCloud · AirDrop": "Files · iCloud · AirDrop",
 "Dark, Sprache English": "Dark, English",
 "Auto-Refine bei > 0,1 LU": "Auto-refine at > 0.1 LU",
 "64 (1 pro Slot)": "64 (1 per slot)",
 "Fit · Detail · zu In · zu Out": "Fit · Detail · to In · to Out",
 "alle 4 Orientierungen": "all 4 orientations",
 "Hoch + Quer": "Portrait + landscape",
 "iOS 16+ (Mini · separate App)": "iOS 16+ (Mini · separate app)",
 "Silero v5 (ONNX, lokal)": "Silero v5 (ONNX, local)",
 "1,41 (Power-Domain)": "1.41 (power domain)",
 "In/Out-Drag-Handles": "In/Out drag handles",
 "WAV-Stems · Video-Mux": "WAV stems · video mux",
 "1.5 s Smoothing": "1.5 s smoothing",
 "Play · Play In · Play Out (1,5 s)": "Play · Play In · Play Out (1.5 s)",
 "OFF · 0,5 · 1,5 · 4 s": "OFF · 0.5 · 1.5 · 4 s",
}

# Nur fuer placeholder-Attribute. value= bleibt bewusst deutsch: das sind die
# Werte, die das Support-Formular absendet - sonst kaemen zwei Varianten an.
PLACEHOLDER_EN = {"z. B.": "e.g.", "Name und Version": "name and version"}

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
 "Offline EBU-R128-Korrektur auf dem iPad. 14 Delivery-Presets, Two-Pass mit Verify-and-Refine, 4x Polyphase TP-Limiter, Mono bis 9.1.6 Surround.":
   "Offline EBU R128 correction on the iPad. 14 delivery presets, two-pass with verify-and-refine, 4x polyphase TP limiter, mono to 9.1.6 surround.",
 "Offline-Lautheitskorrektur nach EBU R128, ATSC A/85, OTT, Spotify, YouTube. Two-Pass mit Verify-and-Refine auf +/-0,1 LU. macOS Standalone und iPad.":
   "Offline loudness correction to EBU R128, ATSC A/85, OTT, Spotify, YouTube. Two-pass with verify-and-refine to +/-0.1 LU. macOS standalone and iPad.",
 "Voice-Over gegen Bewegtbild auf dem iPad. Prompter mit Auto-Scroll, AutoEdit, AutoMix nach EBU R128, SmartDucker.":
   "Voice-over to picture on the iPad. Prompter with auto-scroll, AutoEdit, AutoMix to EBU R128, SmartDucker.",
 "Die DAW f\u00fcr Sprachproduktion - Voice-over, Beitrag, Podcast, H\u00f6rspiel. Assist mischt automatisch normgerecht (EBU R128, ATSC A/85, ARIB TR-B32, OP-59), Manual bietet den vollen DAW-Umfang: AU/VST3-Inserts, Einzelspur-Stems, Hardware-Konsolen, MXF-Delivery. Prompter und Script-Editor an Bord. F\u00fcr macOS; die iPad-App hei\u00dft voyzSESSION.":
   "The DAW for voice production - voice-over, news pieces, podcast, radio drama. Assist mixes automatically to standard (EBU R128, ATSC A/85, ARIB TR-B32, OP-59), Manual offers the full DAW scope: AU/VST3 inserts, single-track stems, hardware consoles, MXF delivery. Prompter and script editor on board. For macOS; the iPad app is called voyzSESSION.",
}
