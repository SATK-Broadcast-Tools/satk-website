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
