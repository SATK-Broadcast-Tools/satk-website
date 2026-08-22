# Übergabe: Produktseite voyzSESSION neu gestalten

**Angelegt 2026-08-21.** Auftrag: `voyzsession.html` im **Look der IBC-Postkarte**
neu gestalten **und die Fakten auf den heutigen Code-Stand bringen**.

> **Erst lesen, dann schreiben.** Die Faktenlage unten ist am Quelltext von
> `satk-overdub-studio` belegt, nicht an der bestehenden Seite. Wo die Seite
> etwas anderes behauptet, hat die Seite unrecht — sie beschreibt 1.4.1 vom Juli.
> Zeilennummern wandern, also nach Symbol suchen.

---

## 0. Stand beim Übergeben

**Branch `voyzsession-relaunch` ist angelegt** (von `main` abgezweigt), noch ohne
Änderung an der Seite. Dort weiterarbeiten, nicht auf `main`.

Beim Sichten des Kopfbereichs ist ein weiterer Fehler aufgefallen, der in
Abschnitt 5 fehlt: **Das JSON-LD wiederholt die iPad-Falschaussage.** In
`"description"` steht „smart Prompter (macOS)", was den Prompter als
Mac-Funktion ausgibt — er ist Kernfunktion der iPad-App. Ebenso prüfen:
`"operatingSystem"`, `"offers"` (199 EUR) und die `og:`/`twitter:`-Beschreibungen,
die alle dieselbe veraltete Erzählung tragen. **Kopfbereich mitziehen, nicht nur
den sichtbaren Text.**

## 1. Was wo liegt

| | |
|---|---|
| Seite | `voyzsession.html` (528 Zeilen), Schwester `voyzsession-ios.html` |
| Repo | `satk-website`, Branch `main`, Cloudflare Pages |
| Sprachen | deutsch primär, englisch über `data-i18n` + JS-Wörterbuch am Seitenende |
| Farbtokens heute | `:root{--bg:#0a0a0b;--sf:#101114;--bd:#1a1a20;--ac:#12d0ff;--tx:#e8e8ec;--mu:#9a9aa8;--mu2:#d4d4dc}` |
| Schriften | Arimo (Überschriften), Inter (Fließtext), lokal in `fonts/` |
| Nicht anfassen | `_redirects` (301 von `/overdub-studio*`), `overdub-studio-latest.json` als Feed-Name, `sitemap.xml` nur ergänzen |

## 2. Der Postkarten-Look

Die Vorlagen und der Generator liegen in
`~/Downloads/voyzSESSION-IBC-Postkarte/` — `.work/gen_postcard.py` ist die
maßgebliche Quelle für Farben, Größenverhältnisse und Texte, `.work/make_hero.py`
für den Bildeffekt.

**Die vier Gestaltungsmittel, die den Look ausmachen:**

1. **Gekippte Oberfläche mit Schlagschatten.** Der App-Screenshot wird
   perspektivisch verzerrt (echte 4-Punkt-Projektion, linke Kante näher, rechte
   weicht zurück) und bekommt einen weichen Schatten. Fürs Web: entweder die
   fertigen PNGs aus `.work/hero-*.png` verwenden oder in CSS mit
   `transform: perspective() rotateY()` nachbauen.
2. **Farbfeld statt Schwarz.** Drei weiche Farbblasen hinter der Fläche —
   Cyan oben rechts, Tiefblau `#2b4bd8` links, pegelWERK-Grün `#b6e34a` unten
   rechts, alle als radiale Verläufe mit niedriger Deckkraft über `#0a0a0b`.
3. **Zwei-Spalten-Vergleich ASSIST / MANUAL** mit Kopfzeile, Unterzeile und
   quadratischen Aufzählungszeichen in der Spaltenfarbe (Assist cyan, Manual
   hell).
4. **Spec-Band als zweispaltige Tabelle** — Label links in gesperrtem Cyan-
   Versal, Angabe rechts in Grau, feste Spaltenkante.

**Typografie:** Versal-Eyebrows in Arimo Bold mit `letter-spacing: 0.22em` in
Cyan, große Claims in Arimo Bold, alles andere Inter.

## 3. Texte, die schon abgenommen sind

Aus der Postkarte übernehmen — sie sind mehrfach überarbeitet und am Code geprüft:

- Eyebrow: **A DAW MADE FOR VOICE PRODUCTIONS**
- Claim: **Record. Auto Mix. Deliver.**
- Subline: **No overkill. Just workflow.** (steht schon als `od_features_title`
  auf der Seite)
- Vergleichsüberschrift: **ONE SESSION, TWO WAYS TO WORK**

**ASSIST** — *sound shaping, compliant out*
Auto Mix: R128 · A/85 · TR-B32 · OP-59 · Automatic DSP: EQ, compressor, de-ess ·
SmartLeveler, multiband ducker, DNN NR · V-PUNCH: speech-triggered punch-in ·
AutoCut strips the dead air per take · Script editor: all tracks, one text

**MANUAL** — *only what voice production really needs*
All DAW standards on board · MXF: embed on any track you need · Dry per-track
stems, pre-bus · Mic Mix: gain-sharing automix per track · Connect a hardware
control surface · Easy remote recording, no aggregate device

**Band:** INTERNATIONAL DELIVERY — MXF 8-track M&E · ARD/ZDF HDF01a · ARIB RDD9 ·
CST AS-10 · WAV · SRT/VTT | VIRTUAL VIDEO I/O — own camera, no extra software |
CONTROLLER — MakePro X (MPX), MCU, OSC

## 4. Fakten, die auf der Seite fehlen

Alles am Code belegt (Repo `satk-overdub-studio`):

| Thema | Beleg |
|---|---|
| **AU/VST3-Plugin-Hosting**, 5 Insert-Slots je Kanal, dazu Voice-, IT/FX- und Master-Gruppe | `CMakeLists.txt` (JUCE_PLUGINHOST_*, Desktop-only), `Track.h` `kNumInserts = 5`, `Project.h` masterInserts/itGroupInserts/voiceGroupInserts |
| **Assist- und Manual-Modus** als Produktkonzept | `Project.h` `manualMix`, `Track.h` `levelerFor()`, `AutoModeButton.h` |
| **DNN-Entrauschung** (ONNX) neben SmartDenoiser | `Source/DSP/NeuralDenoiser/`, `CMakeLists.txt` `SATK_WITH_ONNX` default ON |
| **V-PUNCH** — sprachgesteuerter Einstiegspunkt | `TransportBar.h` Button `"V-PUNCH"`, Texte in `MainComponent.cpp` |
| **Script-Editor** — wortgenaues Transkript aller Spuren, Whisper offline, Wort anklicken springt zum Playhead | `Source/Transcribe/WhisperTranscriber.h`, `Source/GUI/ScriptEditorView.h` |
| **Untertitel-Export SRT/VTT** | `ScriptEditorView.cpp` Menü „SubRip (.srt)" / „WebVTT (.vtt)" |
| **AutoCut** und **Mic Mix** (gain-sharing) als Spurfunktionen | `TimelineView.h` `runAutoCutTake`, `Track.h` `micMix` |
| **Delivery-Profile** EBU R128 · US ATSC · Stereo · **ARD/ZDF HDF01a · ARIB RDD9 · CST AS-10** | `Source/Model/DeliveryProfiles.h` |
| **Controller**: Mackie MCU, OSC, Web-Konsole für MakePro X | `Source/Control/` |
| **Eigene virtuelle Kamera** im App-Bundle, installiert sich selbst | `CameraExtension/`, `Source/Camera/SystemExtensionInstaller.mm` |
| **Remote**: Cue- und Talkback-Bus auf eigenem Ausgangspaar | `AudioEngine.h` setTalkbackInput/OutputChannel, `AudioSettingsPanel.h` |
| **Exportformate**: WAV, AIFF, AAC (.m4a), MP3, MXF, Video-Mux; 44,1–96 kHz; 16/24/32-Bit-Float | `Source/GUI/ExportDialog.cpp`, `Source/Export/AudioEncoder.cpp` |

## 5. Fehler, die auf der Seite stehen

1. **„iPad iPadOS 16+ (ohne Prompter)"** — **falsch.** Der Prompter ist
   ausdrücklich Kernfunktion der iPad-App; `CLAUDE.md` im Produkt-Repo verbietet
   sogar, ihn dort zu entfernen. Muss weg.
2. **„Prompter SFSpeechRecognizer DE/EN"** — untertreibt. Prüfen, welche Sprachen
   tatsächlich unterstützt sind, statt DE/EN zu behaupten.
3. **„Denoiser SmartDenoiser (FFT)"** — unvollständig, die DNN-Stufe fehlt.
4. **„Export WAV · Stems · Video-Mux"** — unvollständig, siehe Tabelle oben.
5. **„MXF Round-Trip Sum + M+E + OT"** — inzwischen genauer beschreibbar:
   8 Sound-Tracks, Kanalziel wählbar, M&E bleibt erhalten.

## 6. Auflagen

- **Erst veröffentlichen, wenn das Release draußen ist.** Die Seite beschreibt
  heute bewusst 1.4.1; die neuen Funktionen sind noch nicht ausgeliefert.
  Auf einem Branch vorbereiten, nicht auf `main` live schalten.
- **Nicht behaupten, was nicht trägt.** Zwei Fallen aus der Kartenarbeit:
  **AS-11** ist nicht ausgeliefert (Commit `1dfe3bf`: „one mechanism missing"),
  und der **Script-Editor schneidet noch nicht** (`ScriptEditorView.h`:
  „Das Schneiden über Text-Selektion kommt als eigener Schritt") — also
  „Transkript und Navigation", nicht „Schneiden im Text".
- **„Dugan" gehört nicht in nutzersichtbaren Text.** Das Verfahren ist frei
  (Patente 1991/1993 abgelaufen), die **Marke ist es nicht** — Yamaha und Waves
  lizenzieren den Namen. Korrekt ist `gain-sharing automix`.
- **Kein Verlust an SEO.** Bestehende `id`-Anker, `sitemap.xml`, JSON-LD und die
  301-Weiterleitungen von `/overdub-studio*` müssen weiterleben.
- **Beide Sprachen pflegen.** Jede neue Zeile braucht ihren `data-i18n`-Eintrag
  in beiden Wörterbüchern.

---

## 7. Stand nach der Umsetzung (2026-08-22)

Umgesetzt auf `voyzsession-relaunch`. `voyzsession.html` ist neu gebaut, alle
Fakten sind am Quelltext von `satk-overdub-studio` nachgeprueft — nicht aus
Abschnitt 4 uebernommen, sondern jede Zeile selbst geoeffnet.

**Gestaltung.** Die vier Mittel der Postkarte sind uebernommen: Farbfeld aus drei
radialen Blasen (Cyan/Tiefblau/Gruen) statt Schwarz, die beiden gekippten
Flaechen aus `.work/hero-*.png` als WebP (`img-voyz-hero-mixer.webp`,
`img-voyz-hero-timeline.webp`, je ~160 kB, 2200 px), der Zwei-Spalten-Vergleich
ASSIST/MANUAL mit quadratischen Aufzaehlungszeichen, und das Spec-Band als
zweispaltige Liste mit gesperrtem Cyan-Versal links.

Statt des gedruckten Deck-Verlaufs wird die Flaeche per `mask-image` selbst
ausgeblendet — ein Verlaufsdeckel haette an der Bildunterkante eine sichtbare
Kante gegen das Farbfeld gesetzt (im Browser nachgesehen). Die Bildhoehe haengt
an `aspect-ratio`, nicht an `vh`: sonst schneidet `object-fit: cover` auf hohen
schmalen Schirmen seitlich ins Pult.

**Am Code geprueft (Datei:Zeile in dieser Sitzung geoeffnet):**

| Aussage | Beleg |
|---|---|
| Auto Mix R128 · A/85 · TR-B32 · OP-59 | `FormatProfiles.h:86-96` — OP-59 ist ein **Loudness**-Profil, kein Delivery-Profil; in `DeliveryProfiles.h` steht es NICHT |
| 5 Insert-Plaetze, AU/VST3, Desktop-only | `Track.h:243`, `Project.h:180/185/192`, `CMakeLists.txt:222-229` |
| DNN-NR = DeepFilterNet 3 ueber ONNX | `NeuralDenoiser.h:5`, `CMakeLists.txt:302` (`SATK_WITH_ONNX` default ON) |
| V-PUNCH inkl. Stitch (Shift) | `TransportBar.h:33/143`, `MainComponent.cpp:1696` |
| Script-Editor: Anzeigen + Navigieren | `ScriptEditorView.h:14` — **kein Schneiden**, so auch auf der Seite formuliert |
| SRT/VTT | `ScriptEditorView.cpp:91-92` |
| MXF 8 Sound-Tracks, M&E erhalten | `DeliveryProfiles.h:63-64, 92-130` |
| Audio-Export + Raten/Tiefen | `ExportDialog.cpp:39-84`, `AudioEncoder.h:16-41` |
| Video-Import | `VideoView.cpp:711` — `*.mp4;*.mov;*.m4v;*.mxf` |
| Cue/Talkback auf eigenen Ausgaengen | `AudioEngine.h:124-139`, `AudioSettingsPanel.h:47-66` |
| Prompter auf beiden Plattformen | `MainComponent.h` — kein `JUCE_IOS`-Guard; Prompter liegt jetzt LINKS auf der VIDEO-Seite (`MainComponent.h:195`), der eigene PROMPTER-Tab ist aufgeloest |

**Korrigierte Falschaussagen** (Abschnitt 5 abgearbeitet): „iPad ohne Prompter"
weg (auch aus JSON-LD, `og:`/`twitter:`), Prompter-Sprachen nicht mehr auf DE/EN
verengt (`SpeechRecognizer.mm:382` fragt `[SFSpeechRecognizer supportedLocales]`
zur Laufzeit), Denoiser um die DNN-Stufe ergaenzt, Export vollstaendig, MXF
genauer, **WebM entfernt** (steht nicht im Dateifilter), **macOS 13+ → 12+**
(`CMakeLists.txt:71`, `HARDWARE.md`: 13+ ist die *Empfehlung*).

**Preis im JSON-LD war falsch:** 199 EUR Einmalkauf. `mac.html:269-423` verkauft
seit dem Abo-Umbau **24,99 EUR/Monat oder 249 EUR/Jahr** — im `offers`-Array
korrigiert. Auf der Seite selbst steht bewusst kein Preis (er wuerde hier
veralten), die CTA fuehrt auf `/mac`.

**Nicht behauptet:** AS-11 (nicht ausgeliefert), Schneiden im Script-Editor,
„Dugan" (Marke; auf der Seite steht `Gain-Sharing-Automix`).

### Zwei offene Punkte fuer den, der veroeffentlicht

1. **Virtuelle Kamera steht NICHT auf der Seite.** Der Code traegt sie
   (`CameraExtension/VoyzCameraSource.mm:5` — „STUFE 3: die Kamera hat jetzt
   einen SINK-Strom", plus Commits `a0b341d`, `af70832`), aber
   `SATK_CAMERA_EXTENSION` ist **OFF by default** (`CMakeLists.txt:829`) und im
   Release nur bei `SATK_CAMERA=1` dabei (`dist/build-release-macos.sh:256`).
   Erst wenn ein Release sie wirklich mitbringt, gehoert die Zeile aus dem
   Postkarten-Band („VIRTUAL VIDEO I/O") auf die Seite.
   **Nebenbefund:** der Kommentar in `CMakeLists.txt:810` sagt noch „Stand:
   Stufe 1 … der Sink-Strom kommt danach" — das ist ueberholt und gehoert im
   Produkt-Repo korrigiert.
2. **Auflage 6 gilt weiter:** nicht auf `main` mergen, bevor das Release
   draussen ist. Der `post-commit`-Hook dieses Repos pusht nur den Branch und
   zieht `main` NICHT nach — nachgesehen in `.git/hooks/post-commit`.
