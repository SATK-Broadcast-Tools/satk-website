# Prüfbericht: Website-Übersetzungen FR, ES, IT, PT

Stand 01.11.2026. Vorprüfung vor den Muttersprachlern, auf einem anderen Modell als die Übersetzung.
Branch `claude/website-gegenlesen-e9b153`, abgezweigt von `claude/website-sprachen-e5c579` (`fe836fa`). Nicht live.

## Was geprüft wurde und wie

* **Umfang:** alle 554 Texte je Sprache (`tools/i18n/<sprache>.json` = Quelle der 12 Seiten unter `fr/ es/ it/ pt/`),
  verglichen mit Deutsch (verbindlich) und Englisch, dazu der Seitentext außerhalb der Liste (Sprachmenü, Generator-Texte).
* **Korrigiert wurde in der Quelle**, nicht in den HTML-Dateien: Die Seiten erzeugt `tools/build-i18n.py`.
  Eine Hand-Korrektur im HTML wäre beim nächsten Generatorlauf weg. Danach `python3 tools/build-i18n.py`, die Seiten sind neu erzeugt.
* **CSV `gegenlesen-<sprache>.csv`:** Spalte `Entwurf` = Text, der jetzt auf der Seite steht. Neu sind die Spalten
  `pruefung` (ok / korrigiert (Art): Grund | vorher: … / UNSICHER: Grund) und `quelle` (Beleg aus lokalisierten DAWs).
  Der Generator behält beide Spalten bei `--review` (kleine Änderung in `write_review`).
  `Korrektur` und `Anmerkung` bleiben leer für die Muttersprachler.
* **Typografie mechanisch** (Skript, nur Text außerhalb von Tags, URLs und Entities):
  FR schmales geschütztes Leerzeichen U+202F vor `: ; ! ?` und innerhalb `« »` (vorher normales geschütztes Leerzeichen U+00A0);
  IT Apostroph `’` statt `'` (vorher 125 × ASCII, 1 × typografisch). Anführungszeichen im Fließtext in allen vier Sprachen `« »`.
  Das Sprachmenü (Text für Bildschirmleser „Langue : Français“) bekommt im Generator das U+202F ebenfalls.
* **Sicherheitsgrade:** Die Satz-für-Satz-Lektüre haben vier Prüf-Agenten gemacht (je Sprache einer). Von mir nachgeprüft (*gemessen*):
  die zehn wichtigsten Korrekturen je Sprache und je 5 Zufallsstichproben; alle mechanischen Prüfungen unten.
  Dabei habe ich FR Nr 489 nachgeschärft. Die italienischen Seiten habe ich bei „superficie di controllo“ selbst
  angeglichen; der Beleg ist das Ableton-Handbuch IT, das ich geöffnet habe. Die DAW-Belege in `quelle` stammen sonst von
  den Agenten (*gelesen*); geprüft habe ich davon die Aussage „Logic-Handbuch gibt es nicht auf Italienisch“. Sie stimmt:
  Unter it-it ist nur die Navigation italienisch, der Text englisch.

## Ergebnis auf einen Blick

| Sprache | korrigiert | davon nur Typografie | UNSICHER | ok | DAW-Begriffe belegt |
|---|---:|---:|---:|---:|---:|
| FR | 123 | 89 | 22 | 409 | 21 |
| ES | 50 | 8 | 12 | 492 | 29 |
| IT | 136 | 82 | 14 | 404 | 36 |
| PT | 71 | 3 | 13 | 470 | 25 |

Inhaltlich (ohne reine Typografie) also FR 34, ES 42, IT 54, PT 68 Korrekturen. Häufigste Art überall: **Formulierung**,
meist Lehnübersetzungen aus dem Deutschen (z. B. „4 étapes jusqu’à …“, „En 4 pasos hasta …“, „verdad DSP“,
„sul prossimo iPad“, „Frequenza di aggiornamento 200 ms“). Im Portugiesischen sind es zuerst **brasilianische Formen**
(sistema operacional, controle, detecta, contagem regressiva, barra de status, precisar + Infinitiv ohne „de“).
Echte Sinnfehler gab es wenige, aber schwere: FR/PT „Ce qui fait / O que faz“ (= „was es tut“ statt „was es ausmacht“),
FR 489 (iPad-App „heißt auf dem Mac“ voyzSESSION), IT „disdici ogni mese“ (= „kündige jeden Monat“),
IT „riduzione del rumore neurale“ (= Reduktion von neuronalem Rauschen), ES „Apps de Apple“ (= von Apple hergestellt).

## Anrede

Begründungen der Prüf-Agenten, *gelesen*, nicht einzeln mit Quellen belegt.

| Sprache | Form | Begründung |
|---|---|---|
| FR | vous | Französische Software- und App-Websites siezen durchgehend (Apple FR, Audio-Hersteller); „tu“ wirkt auf Broadcast-Kunden unprofessionell. |
| ES | tú | Software- und App-Websites in Spanien duzen heute (Apple ES, DAW-Hersteller); „usted“ wirkt im Produktmarketing steif. |
| IT | tu | Italienische Software-Websites und Apple IT duzen im Marketing; „Lei“ ist Behörden- und Vertragston. |
| PT | ohne „você“ | In pt-PT wirkt „você“ distanziert bis unhöflich, „tu“ zu vertraut; üblich sind Imperativ der 3. Person („Abra“, „Experimente“) und unpersönliche Sätze, so auch Apple PT. |

Alle vier stimmen mit den App-Festlegungen überein (`tools/lang/README.md` im App-Repo). Kein Wechsel der Anrede gefunden.

## Mechanische Prüfungen (gemessen)

* **HTML-Struktur:** Ein Skript vergleicht für alle 48 Seiten den Stand vor der Prüfung (`fe836fa`) mit dem neuen.
  Verglichen werden die Folge aller Tags, alle Attribute einschließlich Links und `hreflang`, Kommentare und Skripte, deren
  String-Inhalte maskiert sind. Ausgenommen sind nur Textknoten und übersetzte Text-Attribute (`alt`, `title`,
  `placeholder`, `aria-label`, `meta content` von description/title).
  Ergebnis: **48 Seiten, 0 Abweichungen**. Gegenprobe mit absichtlich geändertem `href` und `hreflang`: beide erkannt.
* `python3 tools/build-i18n.py --check`: kein Drift. `python3 tools/check-links.py`: 90 Seiten, 18 hreflang-Gruppen, keine Fehler.
* FR: kein Leerzeichen-Rest vor `: ; ! ?`, keine geraden Anführungszeichen. IT: kein ASCII-Apostroph mehr im Text.
  ES: jede Frage mit `¿`. ES/IT/PT: keine geraden Anführungszeichen im Fließtext.
* `text (HTML)`-Einträge: Tag-Folge jeder Korrektur identisch mit dem Entwurf (sonst wäre sie verworfen worden; verworfen: 0).
* DE- und EN-Seiten unverändert (nur `fr/ es/ it/ pt/` und `tools/` im Diff).

## Befunde für alle Sprachen (nicht in der Übersetzung lösbar)

1. **Deutsche Reste auf allen Sprachseiten, auch auf der englischen (live).** Die Spezifikationslisten
   `<li><b>…</b> …</li>` der Quelle haben kein `data-i18n` und keinen Literal-Eintrag. Deshalb stehen auf FR/ES/IT/PT und EN
   wörtlich: „Silero v5 (ONNX, lokal)“, „PPM-Skala“, „Modi“, „externe Interfaces (RME, UA, ...)“, „Dark, Sprache English“
   (broadcast-meter-ios), „folgt Audio-Hardware / DAW“, „Sprache“ (broadcast-meter-pro), „Aktionen“ (easy-editor),
   „Mono bis 9.1.6 (16)“ (loudness-correct-ios) und „folgt Audio-Hardware“ (voyzsession-ios). Abhilfe: in der DE-Quelle mit
   `data-i18n` auszeichnen oder als Literal in `tools/i18n_en.py` eintragen, dann übersetzen. Das ist eine Strukturänderung
   und war hier nicht erlaubt.
2. **Herstellernamen aus dem deutschen Original** stehen auf allen Sprachseiten: Mackie (MCU), Elgato Stream Deck und
   MakePro X (voyzsession, Nr 508 und 540), RME und UA (Spezifikationsliste, siehe 1), JUCE (Lizenzhinweis Open Source).
   Dazu kommt der Platzhalter im DAW-Feld des Supportformulars: „z. B. Pro Tools 2024.3“. Übersetzt wird nur „z. B.“, der Rest steht
   fest in `support.html`, deshalb lässt er sich nur in der Quelle ändern (Vorschlag: „z. B. Name und Version“).
   Die übrigen Namen sind Kompatibilitäts- und Lizenzangaben, kein Vergleich. Sie sind als UNSICHER markiert und nicht entfernt.
   **Entscheidung beim Nutzer**, und dann für DE und EN gleich. JUCE muss als Lizenzhinweis vermutlich bleiben.
   Den Hersteller RTW hatten die Übersetzer bereits überall entfernt („PPM“, „Style broadcast“).
3. **Fehler in der deutschen Quelle:**
   * Nr 161 (easy-editor) und Nr 372 (loudness-correct): Zwischen den Arbeitsschritten fehlen die Pfeile,
     schon in `easy-editor.html` und `loudness-correct.html` (gemessen, auch EN). FR/ES/PT haben die Sätze
     jetzt mit Satzzeichen lesbar gemacht, IT mit „→“. Die DE-Quelle sollte repariert werden; danach bitte die Sprachen angleichen.
   * Zahl der Delivery-Presets: 13 (Nr 370), 14 (Nr 209/227/360/363) und 16 (Nr 293/302/305/325). Die Übersetzungen folgen dem
     Deutschen treu. Welche Zahl stimmt, ist eine Sachfrage an die App.
**Erledigt am 01.11.2026 (Branch `claude/website-sprachen-e5c579`):**
* Zu 1: Die Spezifikationslisten übersetzt jetzt `SPEC_EN` in `tools/i18n_en.py` (nur ganze Labels/Werte, Art `spec`
  in der Gegenlese-Liste), insgesamt 38 deutsche Labels und Werte, nicht nur die zehn genannten.
* Zu 2: Platzhalter jetzt „z. B. Name und Version“. JUCE ist von den Produktseiten und aus der Bestandteil-Tabelle
  von `open-source(-en).html` entfernt: Der JUCE-8-EULA verlangt keinen Hinweis, Klausel 2.9 verbietet nur, Hinweise
  im Framework zu entfernen. RME/UA/Mackie/Elgato/MakePro X bleiben (Nutzer). Der Platzhalter „z. B. RME UCX II“ im Feld
  Audio-Interface ist geblieben.
* Zu 3: Pfeile NICHT wieder eingesetzt: Commit `79c912c` hat sie bewusst entfernt (keine KI-typischen Unicode-Zeichen).
  Stattdessen Kommas in DE, EN und allen vier Sprachen, IT ohne „→“. Preset-Zahl gegen `satk-loudness-correct`
  `Source/Presets/LoudnessPresets.h:78` (14 Einträge = 13 Targets + Custom, Netflix/Leq seit iPad 1.1.0 entfernt):
  iOS-Seite von 16 auf 14 Presets und 13 Targets, Netflix → OTT -27 LUFS, Leq-Kacheln raus; Mac-Titel
  „14 Targets ab Werk“ → „13 Targets ab Werk“. Der Changelog (1.0.0 mit 16 Presets) bleibt als Geschichte stehen.

4. **IT-Gedankenstrich:** Die Seiten setzen „ - “ (Bindestrich) als Gedankenstrich, wie das DE-Original. Typografisch richtig wäre
   „ – “. Nicht geändert, weil das DE-Original es genauso macht. Wenn gewünscht, lässt es sich in allen vier Sprachen
   mechanisch ersetzen.

## Änderung auch für die App

Kein DAW-Abgleich hat einen Begriff ergeben, der einer Festlegung in `tools/lang/README.md` widerspricht
(`anders_als_app` überall false). Beim Abgleich mit den App-Texten (`tools/lang/review/help_*.txt`, `pt.csv`
auf `claude/sprachen-stufe1-2574ac`, nur gelesen) fielen aber drei Punkte auf:

| Begriff | Website jetzt | App heute | Vorschlag |
|---|---|---|---|
| Control Surface (FR/ES/IT) | surface de contrôle / superficie de control / superficie di controllo (Website vorher: console matérielle / consola de hardware / console hardware) | Hilfe-Texte sagen schon surface de contrôle / superficie de control / superficie di controllo | In die README-Festlegungen aufnehmen. In den UI-Texten prüfen, ob noch „console/consola“ steht. |
| Control Surface (PT) | consola de hardware (beibehalten, UNSICHER) | README: „consola“; Hilfe help_pt: „superfície de controlo“ | **Gemeinsam entscheiden.** Für Einheitlichkeit mit FR/ES/IT spricht „superfície de controlo“; eine pt-PT-DAW-Quelle gibt es nicht. |
| Abtastrate (PT) | frequência de amostragem (wie README) | README: frequência; in `tools/lang/review` steht 7 × „taxa de amostragem“, 3 × „frequência de amostragem“ | Apple pt-PT schreibt „taxa de amostragem“ (Beleg in der PT-CSV, Nr 173). Erst die App in sich einheitlich machen, dann die Website angleichen. |
| Plug-in (ES/IT/PT) | plug-in(s) (auf allen Seiten einheitlich) | Hilfe-Texte: plugins / plugin | Die Schreibweise in einer der beiden Fassungen angleichen. Für „plug-in“ sprechen Ableton ES und Apple pt-PT; Logic sagt „módulos“ (ES) bzw. „module“ (FR), das ist UNSICHER. |

Zu den Quellen: Logic Pro ist für FR und ES lokalisiert. Für IT und PT steht unter it-it/pt-pt nur die Navigation in der
Landessprache, der Handbuchtext ist englisch. Dort dienen GarageBand und iMovie (Apple) sowie Ableton als Beleg. Steinberg
(Cubase/Nuendo) blockiert den Abruf (HTTP 403), dafür gibt es nur Belege aus Suchtreffern. Für Pro Tools und Reaper wurden
keine offiziellen Handbücher in den vier Sprachen gefunden, Sender-Glossare (RTVE, RAI, RTP, France Télévisions) ebenfalls
nicht. Die Herstellernamen aus dem DAW-Abgleich stehen nur in CSV und Bericht, nicht auf den Seiten
(per grep geprüft; einzige Ausnahme ist der Platzhalter „Pro Tools“ aus der Quelle, siehe Befund 2).

## Französisch (`fr/`)

**Anrede:** vous – französische Software- und App-Websites (auch Apple FR, Audio-Hersteller) siezen durchgängig; „tu“ wirkt auf B2B/Broadcast-Kunden unprofessionell. Der Entwurf ist durchgehend in vous-Form, keine tu-Reste.

**Ergebnis:** 123 von 554 Einträgen korrigiert (davon 89 nur Typografie), 22 UNSICHER, 409 ok.

| Art | Einträge |
|---|---:|
| grammatik | 5 |
| rechtschreibung | 2 |
| typografie | 102 |
| formulierung | 21 |
| einheitlichkeit | 17 |
| treue | 3 |

(Ein Eintrag kann mehrere Arten haben.)

### Die zehn wichtigsten Korrekturen

| Nr | Art | vorher | nachher | Grund |
|---|---|---|---|---|
| 489 | treue, formulierung, typografie | `…V, en MXF ou directement avec la vidéo. Pour Mac, l’app iPad s’appelle voyzSESSION.` | `…V, en MXF ou directement avec la vidéo. Version Mac. L’app pour iPad s’appelle voyzSESSION.` | Sinnfehler: „Pour Mac, l’app iPad s’appelle…“ sagt, die iPad-App heiße auf dem Mac so. Schlusssatz nachgeschärft: „Version Mac.“ statt Fragment „Pour Mac.“ |
| 478 | grammatik, einheitlichkeit, typografie | `…es outils d’atelier de la version Mac : <b>plug-ins AU/VST3</b>, l’<b>éditeur de script</b> avec transcription, les <b>profils de livraison MXF</b>, les <b>consoles matérielles</b> et la <b>caméra virtuelle</b>. Si v…` | `…es outils d’atelier de la version Mac : les <b>plug-ins AU/VST3</b>, l’<b>éditeur de script</b> avec transcription, les <b>profils de livraison MXF</b>, les <b>surfaces de contrôle</b> et la <b>caméra virtuelle</b>. Si v…` | Artikel vor erstem Listenglied ergänzt; „Hardware-Konsolen“ (MCU, Stream Deck) heißen in Logic FR „surfaces de contrôle“. |
| 120 | treue, typografie | `Ouvrez l’app autonome, l’audio est routé automatiquement : aucune installation, aucune configuration nécessaire.` | `Ouvrez l’app autonome, l’audio est routé automatiquement : rien à préparer, aucune configuration nécessaire.` | „Setup“ meint Vorbereitung, nicht Installation; die App muss ja installiert werden. |
| 509 | formulierung | `Ce qui fait voyzSESSION PRO` | `Ce qui distingue voyzSESSION PRO` | „Ce qui fait voyzSESSION PRO“ ist unvollständig (Calque von „ausmacht“). |
| 237 | formulierung | `…ête. Superposez les sons en mode MULTI, enchaînez-les en fondu enchaîné en mode SINGLE. Enreg…` | `…ête. Superposez les sons en mode MULTI, passez de l’un à l’autre en fondu enchaîné en mode SINGLE. Enreg…` | Doppelung „enchaînez … enchaîné“; „ablösen“ = vom einen zum anderen wechseln. |
| 272 | formulierung | `…tre les cues. ESC arrête tout, Fade-All fait disparaître proprement tous les pads en cours de lecture.` | `…tre les cues. ESC arrête tout, Fade-All arrête proprement en fondu tous les pads en cours de lecture.` | Pads „verschwinden“ nicht; gemeint ist sauberes Ausblenden. |
| 149 | einheitlichkeit, formulierung, typografie | `easy EDITOR est un éditeur audio ciblé pour la radio, le podcast et la postproduction. Pas de multipiste, pas de plug-ins, pas de MIDI : uniquement découper, couper, normaliser selon R128 et exp…` | `easy EDITOR est un éditeur audio spécialisé pour la radio, le podcast et la postproduction. Pas de multipiste, pas de plug-ins, pas de MIDI : uniquement rogner, couper, normaliser selon R128 et exp…` | „découper, couper“ doppelt; Trim = „rogner“ wie Nr 150. „ciblé“ als Calque von „fokussiert“. |
| 503 | einheitlichkeit | `Brancher une console matérielle` | `Brancher une surface de contrôle` | Gemeint sind Bedienoberflächen (MCU, OSC); Logic FR: „surfaces de contrôle“, nicht Mischpult. |
| 350 | grammatik, formulierung, typografie | `…ne : atteignez votre cible à +/-0,1 LU, proprement limitée, sans tour de passe-passe de re-rendu.` | `…ne : atteignez votre cible à +/-0,1 LU, avec une limitation propre, sans tour de passe-passe de re-rendu.` | „limitée“ bezieht sich grammatisch auf „cible“; gemeint ist das Signal. |
| 251 | grammatik | `…actif vers pegelWERK easy EDITOR. Coupez ou normalisez-le selon R128, puis SEND BACK le renvoie automatiquement dans le même pad. Sans easy EDITOR, un lien vers l’App Store s’affiche à la place.` | `…actif vers pegelWERK easy EDITOR. Coupez-le ou normalisez-le selon R128, puis SEND BACK le renvoie automatiquement dans le même pad. Sans easy EDITOR, un message renvoyant vers l’App Store s’affiche à la place.` | Pronomen muss bei beiden Imperativen stehen; DE „Hinweis“ ist kein Link. |

### DAW-Abgleich der Fachbegriffe (21 Begriffe)

| Begriff auf der Website | EN | in den DAWs | Entscheidung | Quelle |
|---|---|---|---|---|
| piste | track | piste | übernommen | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb19bfd0d/mac; Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb1998a98/mac |
| take | take | prise (Logic, Ableton) | beibehalten weil App-Festlegung „take“ verbindlich | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb1998a98/mac; Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/ |
| fondu enchaîné | crossfade | fondu enchaîné | übernommen | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/ |
| forme d’onde | waveform | forme d’onde | übernommen | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb1998a98/mac |
| tête de lecture | playhead | tête de lecture | übernommen | Apple Logic Pro – https://support.apple.com/guide/logicpro/set-the-playhead-position-lgcp0f34ca7a/mac; Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb19bfd0d/mac |
| tranche de console | channel strip | tranche de console | übernommen | Apple Logic Pro – https://support.apple.com/guide/logicpro/work-with-channel-strip-settings-lgcp35966da6/mac; Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcef1bec0a5/mac |
| table de mixage | mixer | table de mixage | übernommen (Entwurf „console de mixage“ korrigiert) | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpce71eefd/10.7/mac/11.0 |
| surface de contrôle | control surface / hardware console | surfaces de contrôle | übernommen (Entwurf „consoles matérielles“ korrigiert) | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro-css/welcome/mac |
| marqueur de cue | cue marker | marqueur | übernommen (Entwurf „repère de cue“ korrigiert); Nr 455 „repère à l’écran“ ist anderer Sinn, bleibt | Apple Logic Pro – https://support.apple.com/guide/logicpro/markers-overview-lgcp0ec9fc09/mac |
| périphérique agrégé | aggregate device | périphérique agrégé | beibehalten weil Entwurf mit Apple FR übereinstimmt (meine Erstkorrektur „appareil agrégé“ widerlegt) | Apple Configuration audio et MIDI – https://support.apple.com/fr-fr/guide/audio-midi-setup/welcome/mac |
| plug-in | plug-in | plug-in (Ableton) / module (Logic) | UNSICHER weil DAWs uneinig; beibehalten, da „module“ mit „modules DSP“ kollidieren würde | Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/; Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcef1bec0a5/mac |
| insert | insert | effets d’insert | übernommen (Insert englisch wie App) | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcef1bec0a5/mac |
| Punch | punch in/out | Punch In / Punch Out | übernommen (englisch wie App) | Apple Logic Pro – https://support.apple.com/fr-fr/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/ |
| décompte | count-in | décompte | übernommen | Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/ |
| pré-roll | pre-roll | pré-défilement (Ableton) / Pre-roll (Logic) | UNSICHER weil DAWs uneinig; beibehalten | Ableton Live – https://www.ableton.com/fr/manual/recording-new-clips/ |
| relâchement | release | rétablissement (Ableton) / Release (Logic, engl.) | UNSICHER weil DAWs uneinig; frz. Fachprosa üblich, beibehalten | Ableton Live – https://www.ableton.com/fr/manual/live-audio-effect-reference/; Apple Final Cut Pro (Logic-Effekte) – https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac |
| anticipation | lookahead | anticipation (Ableton) / Lookahead (Logic, engl.) | UNSICHER weil Logic englisch lässt; Ableton stützt Entwurf, beibehalten | Ableton Live – https://www.ableton.com/fr/manual/live-audio-effect-reference/; Apple Final Cut Pro (Logic-Effekte) – https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac |
| genou doux | soft knee | Knee (Ableton, Logic – englisch) | UNSICHER weil beide DAWs englisch; im Fließtext beibehalten | Ableton Live – https://www.ableton.com/fr/manual/live-audio-effect-reference/; Apple Final Cut Pro (Logic-Effekte) – https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac |
| compresseur / limiteur | compressor / limiter | compresseur (Ableton); Limiter/Compressor als Modulnamen | übernommen | Ableton Live – https://www.ableton.com/fr/manual/live-audio-effect-reference/; Apple Final Cut Pro (Logic-Effekte) – https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac |
| fréquence d’échantillonnage | sample rate | fréquence d’échantillonnage | übernommen | Apple Logic Pro – https://support.apple.com/guide/logicpro/set-the-project-sample-rate-lgcpce0958b8/mac |
| 32 bits à virgule flottante | 32-bit float | 32 bits à virgule flottante | übernommen (Entwurf „32 bits flottant“ korrigiert); Ableton: „Résolution en bits“ | Apple Logic Pro – https://support.apple.com/kb/PH13235?locale=en_CA&viewlocale=fr_FR |

### Für die Muttersprachler (FR, alle UNSICHER-Stellen)

- **Nr 8** – „Développé par un ingénieur broadcast en activité, pour les ingénieurs broadcast. Le même m…“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 84** – „Que vous mixiez un journal, validiez le master d’une fiction radio ou meniez une émission …“: „meniez une émission“ = moderieren; für Technik evtl. „assuriez/pilotiez une émission en direct“.
- **Nr 180** – „Pas de multipiste, pas de plug-ins, pas de MIDI : si vous en avez besoin, prenez une DAW. …“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 188** – „pegelWERK : apps et plug-ins pour la production média professionnelle.“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 218** – „Plug-in · VST3 · AU“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden.
- **Nr 301** – „Apps et plug-ins pour la production média professionnelle.“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden.
- **Nr 317** – „Protection contre les crêtes inter-échantillons avec 5 ms d’anticipation et un relâchement…“: „relâchement“: Ableton „rétablissement“, Logic/FCP lässt „Release“ englisch – frz. Fachprosa üblich, beibehalten. \| DAW: „anticipation“ = Ableton FR; Logic/FCP lässt „Lookahead“ englisch – beibehalten. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 321** – „Activable en option si le LRA est trop élevé. Filtre Linkwitz-Riley du 4e ordre avec sépar…“: „genou doux“: Ableton und Logic/FCP lassen „Knee“ englisch – im Fließtext frz. Lehrbuchbegriff, beibehalten.
- **Nr 355** – „Coefficients polyphase identiques à ceux du détecteur TP : ce qu’il mesure, il le limite. …“: „relâchement“: Ableton „rétablissement“, Logic/FCP lässt „Release“ englisch – frz. Fachprosa üblich, beibehalten. \| DAW: „anticipation“ = Ableton FR; Logic/FCP lässt „Lookahead“ englisch – beibehalten. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 357** – „Linkwitz-Riley du 4e ordre avec reconstruction parfaite. Grave <= 150 Hz, médium 150-3000 …“: „genou doux“: Ableton und Logic/FCP lassen „Knee“ englisch – im Fließtext frz. Lehrbuchbegriff, beibehalten.
- **Nr 405** – „Allemand et anglais.“: Support nur DE/EN; ein Hinweis „Anfragen gern auf Englisch“ wäre Zusatz – Betreiber entscheidet.
- **Nr 421** – „(facultatif, uniquement pour un plug-in)“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden.
- **Nr 431** – „Les clés de licence vous sont envoyées par e-mail par Paddle juste après l’achat (pour les…“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 433** – „Les licences plug-in et autonomes sont valables pour 2 ordinateurs. Les apps de l’App Stor…“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden.
- **Nr 463** – „Interface audio externe directement sur l’iPad (USB-C / Lightning), pré-roll, affichage de…“: „pré-roll“: Ableton FR „pré-défilement“, Logic-Oberfläche „Pre-roll“ – beibehalten.
- **Nr 469** – „Lancez le pré-roll, enregistrez le take, continuez ou reprenez. AutoCut élimine les pauses…“: „pré-roll“: Ableton FR „pré-défilement“, Logic-Oberfläche „Pre-roll“ – beibehalten.
- **Nr 480** – „voyzSESSION n’est pas un fragment de DAW pour iPad. C’est un outil ciblé pour la voix off …“: „fragment de DAW“ für „Schnipsel“ verständlich; Ton prüfen (Alternative „un bout de DAW“). \| DAW: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 508** – „MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC“: Fremdhersteller Mackie, Elgato (Stream Deck) wie im DE; Kompatibilitätsangabe – Betreiber entscheidet, ob neutralisieren.
- **Nr 512** – „Le débruitage neuronal (DeepFilterNet 3) tire une qualité studio même d’un environnement b…“: „anticipation“ = Ableton FR; Logic/FCP lässt „Lookahead“ englisch – beibehalten. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 521** – „Vos plug-ins, votre son“: „plug-in“: Ableton FR „plug-in“, Logic FR „module“ – beibehalten, Muttersprachler entscheiden.
- **Nr 536** – „SmartDucker multibande, avec anticipation“: „anticipation“ = Ableton FR; Logic/FCP lässt „Lookahead“ englisch – beibehalten.
- **Nr 540** – „Mackie MCU · Elgato Stream Deck · OSC · console web pour MakePro X (macOS)“: Wie Nr 508: Mackie MCU, Elgato Stream Deck stehen auch im DE.

## Spanisch (`es/`)

**Anrede:** tú – spanische Software- und App-Websites (Apple España, gängige Audio-/Kreativ-Software) sprechen Endkunden durchgehend mit „tú“ an; deckt sich mit der App voyzSESSION. Im Dump keine einzige usted-Form gefunden.

**Ergebnis:** 50 von 554 Einträgen korrigiert (davon 8 nur Typografie), 12 UNSICHER, 492 ok.

| Art | Einträge |
|---|---:|
| grammatik | 9 |
| typografie | 10 |
| formulierung | 33 |
| einheitlichkeit | 8 |
| treue | 3 |

(Ein Eintrag kann mehrere Arten haben.)

### Die zehn wichtigsten Korrekturen

| Nr | Art | vorher | nachher | Grund |
|---|---|---|---|---|
| 220 | treue | `Apps de Apple` | `Apps para Apple` | „Apps de Apple“ heißt „von Apple hergestellt“; gemeint sind Apps für Apple-Geräte. |
| 161 | typografie, formulierung | `Elige un pad en pegelWERK instant PLAYER pásalo a easy EDITOR recorta, normaliza SEND BACK y el resultado vuelve al mismo pad. En mo…` | `Elige un pad en pegelWERK instant PLAYER, pásalo a easy EDITOR, recórtalo y normalízalo, y con SEND BACK el resultado vuelve al mismo pad. En mo…` | Trenner (Pfeile) fehlen schon im DE; Satz war unlesbar, jetzt als Abfolge interpunktiert. |
| 372 | typografie | `La pasada 1 mide LUFS-I/S/M, LRA y TP. La pasada 2 escribe un archivo nuevo con ganancia estática corrección multibanda de LRA opcional limitador TP.` | `La pasada 1 mide LUFS-I/S/M, LRA y TP. La pasada 2 escribe un archivo nuevo con ganancia estática, corrección multibanda de LRA opcional y limitador TP.` | Trenner fehlen (schon im DE); Aufzählung interpunktiert. |
| 406 | formulierung | `✓ Muchas gracias, hemos recibido tu solicitud. En breve recibirás un correo de confir…` | `✓ Muchas gracias, tu solicitud ha llegado correctamente. En breve recibirás un correo de confir…` | Personenwechsel „hemos“ → „Te respondo“ (ich); DE neutral formuliert. |
| 411 | grammatik | `…pos de la forma más completa posible: la versión de la app y del sistema operativo son d…` | `…pos de la forma más completa posible: las versiones de la app y del sistema operativo son d…` | Kongruenz: Singular-Subjekt mit Pluralverb. |
| 447 | formulierung, einheitlichkeit | `Locución contra imagen en el iPad. Prompter con desplazamiento automático, AutoEdit, AutoMix según EBU R128, SmartDucker y exportación R128. Ya en el App Store.` | `Locución sobre imagen en el iPad. Prompter con desplazamiento automático, AutoEdit, AutoMix según EBU R128, SmartDucker y exportación R128. Ya en el App Store.` | „contra imagen“ ist Calque von „gegen Bewegtbild“. |
| 10 | grammatik, formulierung | `Sin compras dentro de la app, sin publicidad. En familia de Apple para hasta 5 personas más. Actualizaciones a través de tu cuenta de Apple.` | `Sin compras dentro de la app, sin publicidad. Compatible con En familia de Apple para hasta 5 personas más. Actualizaciones a través de tu cuenta de Apple.` | Satzfragment „En familia de Apple para…“ ohne Bezug; „Compatible con“ ergänzt. |
| 500 | treue | `MXF: incrústalo en la pista que quieras` | `MXF: incrustación en la pista que quieras` | „lo“ bezog sich auf MXF; eingebettet wird das Audio in die MXF-Spur. |
| 53 | grammatik | `Omitido a propósito para que la app siga siendo…` | `Omitidos a propósito para que la app siga siendo…` | Kongruenz: bezieht sich auf die folgende Liste (Plural). |
| 5 | formulierung | `…igo. Dos apps independientes, una misma verdad DSP.` | `…igo. Dos apps independientes, una misma base DSP.` | „verdad DSP“ ist Calque von „DSP-Wahrheit“, auf Spanisch unidiomatisch. |

### DAW-Abgleich der Fachbegriffe (29 Begriffe)

| Begriff auf der Website | EN | in den DAWs | Entscheidung | Quelle |
|---|---|---|---|---|
| pista | track | pista (Logic, Ableton) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/ |
| toma | take | toma (Logic „tomas“, Ableton „toma“) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/recording-new-clips/ |
| fundido cruzado | crossfade | fundido cruzado (Logic, Ableton, Cubase) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/; Steinberg Cubase LE 13 (es, PDF; nur Inhaltsverzeichnis in Suchtreffer gesehen) – https://archive.steinberg.help/cubase_le/v13/es/Cubase_LE_13_Manual_de_operaciones_es.pdf |
| forma de onda | waveform | forma de onda (Ableton); Logic „ondas“ (Anzeigemodus) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/; Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| cursor de reproducción | playhead | Logic „cursor de reproducción“; Ableton „marcador de inserción“; Cubase „cursor del proyecto“ | UNSICHER weil DAWs uneins; Logic-Wort (Mac-Nutzer) beibehalten | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/; Steinberg Cubase LE 13 (es, PDF; nur Inhaltsverzeichnis in Suchtreffer gesehen) – https://archive.steinberg.help/cubase_le/v13/es/Cubase_LE_13_Manual_de_operaciones_es.pdf |
| línea de tiempo | timeline | línea de tiempo (Ableton); Logic ohne eigenen Begriff („regla“, „área Pistas“) | beibehalten weil einziges belegtes DAW-Wort | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/; Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| mezclador | mixer | mezclador (Logic, Ableton) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/mixing/ |
| plug-in | plug-in | Ableton „plug-ins“; Logic „módulos“ | UNSICHER weil DAWs uneins; Schreibung auf „plug-in(s)“ vereinheitlicht (Mehrheit im Markt, DE-Form „Plug-ins“), „módulos“ wäre die Logic-Variante | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/working-with-instruments-and-effects/; Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| Insert / inserts | insert | Logic „efectos de inserción“ | beibehalten weil App-Festlegung „Insert“ englisch | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| fader | fader | faders (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/midi-and-key-remote-control/ |
| bus | bus | bus (Ableton „bus de salida“) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/mixing/ |
| channel strip | channel strip | Logic „canal“ (Kanalzug); Ableton „controles de pista“ | beibehalten weil DE den englischen Begriff als Feature-Namen führt und „canal“ in Aufzählungen mehrdeutig wäre | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/mixing/ |
| superficie de control | control surface | superficies de control (Logic, Ableton) | übernommen – „consola de hardware“ in Nr 478, 503, 553 ersetzt | Apple Logic Pro, Control Surfaces (span. Titel) – https://support.apple.com/guide/logicpro-css/control-surfaces-overview-ctls036b3e21/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/midi-and-key-remote-control/ |
| frecuencia de muestreo | sample rate | frecuencia de muestreo (Logic, Ableton) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/live-concepts/ |
| bits | bit depth | Profundidad de bits (Ableton) | übernommen (Website nennt nur „24 bits“ usw., kein Konflikt) | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/recording-new-clips/ |
| marcador | marker | marcadores (Logic) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| pre-roll | pre-roll | pre-roll (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/recording-new-clips/ |
| Punch / V-PUNCH | punch-in | Logic „pinchazo“; Ableton „Punch-In“ | beibehalten weil App-Festlegung „Punch“ englisch; V-PUNCH ist Funktionsname | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/recording-new-clips/ |
| medidor | meter | medidor (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/mixing/ |
| enrutamiento | routing | enrutamiento (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/mixing/ |
| envolvente | envelope | envolvente (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/ |
| limitador | limiter | Limitador (Ableton) | übernommen | Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/working-with-instruments-and-effects/ |
| EQ / ecualizador | EQ | Logic „ecualizador de canal“; Ableton „EQ de canal“ | übernommen („EQ“ in beiden belegt) | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/working-with-instruments-and-effects/ |
| stem | stem | stems (Logic „divisor de stems“) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| dispositivo agregado | aggregate device | dispositivo agregado (Apple) | übernommen | Apple Configuración de Audio MIDI (es) – https://support.apple.com/es-lamr/102171 |
| sonoridad | loudness | sonoridad (UIT-R BS.1770 span. Fassung); Logic behält Plug-in-Namen „Loudness Meter“ | übernommen | UIT-R BS.1770-5 (es, PDF) – https://itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-S.pdf; Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| True Peak | true peak | UIT span.: „nivel verdadero de cresta“; DAWs behalten engl. Namen | beibehalten weil Branchenbegriff mit Einheit dBTP und in DE/EN identisch; „picos entre muestras“ steht erklärend daneben | UIT-R BS.1770-5 (es, PDF) – https://itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-S.pdf |
| deshacer | undo | Deshacer (Logic) | übernommen | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac |
| sesión | session | Logic/Ableton „proyecto“ (Ableton „Session“ = Ansicht) | beibehalten weil „Session“ der Produktbegriff von voyzSESSION ist (DE „Session“) | Apple Logic Pro (es-es) – https://support.apple.com/es-es/guide/logicpro/lgcpb19bfd0d/mac; Ableton Live 12 (es) – https://www.ableton.com/es/live-manual/12/arrangement-view/ |

### Für die Muttersprachler (ES, alle UNSICHER-Stellen)

- **Nr 8** – „Desarrollado por un ingeniero de broadcast en activo para ingenieros de broadcast. El mism…“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 188** – „pegelWERK - apps y plug-ins para producciones audiovisuales profesionales.“: „de medios profesionales“ mehrdeutig (Bezug auf „medios“); Calque. \| Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 218** – „Plug-in · VST3 · AU“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 301** – „Apps y plug-ins para producciones audiovisuales profesionales.“: Wie Nr 188. \| Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 421** – „(opcional, solo para plug-ins)“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 431** – „Las claves de licencia llegan por correo electrónico de Paddle justo después de la compra …“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 433** – „Las licencias de plug-in y standalone son válidas para 2 ordenadores. Las apps del App Sto…“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 478** – „El <b>prompter viene incluido</b>, con desplazamiento automático que sigue a la voz y reco…“: „piezas de taller“ klingt nach Ersatzteilen; gemeint sind Profi-Werkzeuge. \| Control Surface heißt in Logic und Ableton „superficie de control“; „consola“ klingt nach Mischpult. \| Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 508** – „MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC“: Fremdmarken (Mackie, Elgato, MakePro X) entgegen Regel 5, aber Kompatibilitätsangabe; DE gleich entscheiden.
- **Nr 518** – „Whisper transcribe sin conexión y con precisión de palabra, todas las pistas en un solo te…“: „cursor de reproducción“ = Logic; Ableton „marcador de inserción“, Cubase „cursor del proyecto“. Logic-Wort beibehalten.
- **Nr 521** – „Tus plug-ins, tu sonido“: Schreibung vereinheitlicht auf „plug-in(s)“ (Ableton; schon Nr 149/180/480). Logic sagt „módulos“ – DAWs uneins. *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 540** – „Mackie MCU · Elgato Stream Deck · OSC · consola web para MakePro X (macOS)“: Wie Nr 508: Mackie MCU / Elgato Stream Deck / MakePro X.

## Italienisch (`it/`)

**Anrede:** tu – italienische Software- und App-Websites (Apple Italia, Audio-/Musik-Hersteller, SaaS) sprechen im Marketing fast durchweg mit „tu“ an; „Lei“ wirkt dort bürokratisch. Der Entwurf hält „tu“ überall durch, kein Wechsel zu Lei/voi gefunden.

**Ergebnis:** 136 von 554 Einträgen korrigiert (davon 82 nur Typografie), 14 UNSICHER, 404 ok.

| Art | Einträge |
|---|---:|
| grammatik | 7 |
| typografie | 100 |
| formulierung | 38 |
| einheitlichkeit | 17 |
| treue | 6 |

(Ein Eintrag kann mehrere Arten haben.)

### Die zehn wichtigsten Korrekturen

| Nr | Art | vorher | nachher | Grund |
|---|---|---|---|---|
| 388 | treue, formulierung | `IVA inclusa · disdici ogni mese` | `IVA inclusa · disdetta mensile` | ‚disdici ogni mese‘ = ‚kündige jeden Monat‘; Sinn verfehlt |
| 384 | grammatik, formulierung | `Sincronizzazione video · riduzione del rumore neurale · AutoMix R128 · smart PROMPTER (50+ lingue) · MXF` | `Sincronizzazione video · riduzione neurale del rumore · AutoMix R128 · smart PROMPTER (50+ lingue) · MXF` | ‚rumore neurale‘ = neuronales Rauschen; gemeint neuronale Entrauschung |
| 512 | einheitlichkeit, formulierung, grammatik | `La riduzione del rumore neurale (DeepFilterNet 3) tira fuori qualità da studio anche da ambienti rumorosi - regolabile in continuo con un fader. In più la rifinitura automatica: EQ, compressore, de-esser, SmartLeveler e un ducker multibanda con look-ahead.` | `La riduzione neurale del rumore (DeepFilterNet 3) tira fuori qualità da studio anche da ambienti rumorosi - regolabile in continuo con un fader. In più, la rifinitura automatica: EQ, compressore, de-esser, SmartLeveler e un ducker multibanda con lookahead.` | ‚rumore neurale‘ falscher Bezug (wie Nr 384); Komma nach ‚In più‘; ‚lookahead‘ zusammen wie Nr 317/355 und DAW-Parametername |
| 482 | einheitlichkeit, formulierung | `voyzSESSION per iPad: mixa e masterizza voice-over e podcast. AutoEdit, AutoMix secondo EBU R128, SmartDucker, export R128. Il flusso di mix sempre con te. O…` | `voyzSESSION per iPad: mix e mastering di voice-over e podcast. AutoEdit, AutoMix secondo EBU R128, SmartDucker, esportazione R128. Il flusso di mix sempre con te. O…` | ‚masterizzare‘ heißt im Ital. meist CD brennen; Branche sagt ‚mastering‘; Substantiv ‚export‘ → ‚esportazione‘ wie in den DAWs |
| 51 | formulierung, treue | `In verticale per un rapido controllo dei livelli sul binario, in orizzontale per una lettura dettagliata al tavolo. Il layout si adatta automaticamente.` | `In verticale per un rapido controllo dei livelli al binario, in orizzontale per una lettura dettagliata al tavolo. Il layout si adatta automaticamente.` | ‚sul binario‘ = auf den Gleisen; Bahnsteig = ‚al binario‘ |
| 511 | typografie, grammatik | `…, ATSC A/85, ARIB TR-B32 o OP-59. In più profili per podcast, YouTube e audiolib…` | `…, ATSC A/85, ARIB TR-B32 o OP-59. In più, profili per podcast, YouTube e audiolib…` | ohne Komma liest sich ‚In più profili‘ als ‚in mehreren Profilen‘ |
| 10 | formulierung | `Nessun acquisto in-app, nessuna pubblicità. In famiglia di Apple per un massimo di 5 altre persone. Aggiornamenti tramite il tuo account Apple.` | `Nessun acquisto in-app, nessuna pubblicità. Condivisibile con In famiglia di Apple fino ad altre 5 persone. Aggiornamenti tramite il tuo account Apple.` | ‚In famiglia di Apple per…‘ ohne Verb unverständlich; ‚5 altre‘ → ‚altre 5‘ |
| 19 | formulierung, treue | `…. Compatibile con tutti i limiter R128. Frequenza di aggiornamento 200 ms, fluida e senza sfarfallii.` | `…. Compatibile con tutti i limiter R128. Aggiornamento ogni 200 ms, fluido e senza sfarfallii.` | Eine Frequenz misst man nicht in ms; ‚Aggiornamento ogni 200 ms‘ |
| 239 | formulierung, typografie | `…OP, cross-fade opzionale. L'intero show portatile in un unico bundle .satkip, via AirDrop sul prossimo iPad e subito pronto all'uso.` | `…OP, cross-fade opzionale. L’intero show in un unico bundle .satkip portatile: via AirDrop su un altro iPad, subito pronto all’uso.` | ‚sul prossimo iPad‘ Calque von ‚aufs nächste‘ (= zukünftiges iPad) |
| 495 | einheitlichkeit | `V-PUNCH: entrata in registrazione a comando vocale` | `V-PUNCH: punch-in a comando vocale` | App-Festlegung: Punch bleibt englisch; ‚punch-in‘ ist Branchenbegriff |

### DAW-Abgleich der Fachbegriffe (36 Begriffe)

| Begriff auf der Website | EN | in den DAWs | Entscheidung | Quelle |
|---|---|---|---|---|
| traccia | track | traccia | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/arrangement-view/; Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd22a07333/10.4.14/mac/15.6 |
| take | take | take (Ableton); versione (GarageBand) | beibehalten weil App-Festlegung und Ableton ‚take‘; GarageBand ‚versione‘ nur Einsteiger-App | Ableton – https://www.ableton.com/it/manual/recording-new-clips/; Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbndf80e7097/10.4.14/mac/15.6 |
| mix / mixaggio / mixare | mix / mixing | Mixaggio (Kapitel), mixer | beibehalten: ‚mix‘ für das Ergebnis, ‚mixaggio‘ für den Vorgang, deckt sich mit den DAWs | Ableton – https://www.ableton.com/it/manual/mixing/; Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbndf50dc69a/10.4.14/mac/15.6 |
| mixer | mixer | mixer | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/mixing/ |
| fader | fader | Volume (Ableton-Regler); kein ital. Fader-Begriff gefunden | beibehalten weil App-Festlegung (Fader englisch) | Ableton – https://www.ableton.com/it/manual/mixing/ |
| bus | bus | Traccia di Ritorno (Ableton, Return) | beibehalten weil App-Festlegung (Bus englisch); Ableton-Begriff meint Return, nicht Summen-Bus | Ableton – https://www.ableton.com/it/manual/mixing/ |
| insert (slot insert) | insert | insert effects (Logic, nur EN); dispositivo (Ableton) | beibehalten weil App-Festlegung (Insert englisch) | Apple Logic Pro (it-it-Guide nur englisch) – https://support.apple.com/it-it/guide/logicpro/lgcpbc2192ea/12.3/mac/15.6; Ableton – https://www.ableton.com/it/manual/mixing/ |
| punch-in | punch in | Punch-In (Ableton); Punch-in e punch-out (Cubase) | übernommen: Nr 495 von ‚entrata in registrazione‘ auf ‚punch-in‘ | Ableton – https://www.ableton.com/it/manual/recording-new-clips/; Steinberg Cubase AI 13 (ital. Handbuch, Suchergebnis-Auszug) – https://steinberg.help/cubase_ai/v13/it/Cubase_AI_13_Manuale_operativo_it.pdf |
| cross-fade | crossfade | dissolvenza incrociata (Ableton, Cubase) | UNSICHER weil DAWs einheitlich ‚dissolvenza incrociata‘ sagen; beibehalten, da in instant PLAYER Funktionsbegriff neben dem FADE-Knopf und in Radio-/Soundboard-Jargon üblich, Taglines sonst zu lang. Muttersprachler entscheiden | Ableton – https://www.ableton.com/it/manual/arrangement-view/; Steinberg Cubase Elements 12 (ital. Handbuch, Suchergebnis-Auszug) – https://archive.steinberg.help/cubase_elements/v12/it/Cubase_Elements_12_Manuale_operativo_it.pdf |
| forma d'onda | waveform | forma d’onda (Ableton); forme d'onda (Cubase) | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/arrangement-view/; Steinberg Cubase Elements 12 (ital. Handbuch, Suchergebnis-Auszug) – https://archive.steinberg.help/cubase_elements/v12/it/Cubase_Elements_12_Manuale_operativo_it.pdf |
| frequenza di campionamento | sample rate | frequenza di campionamento | übernommen (deckungsgleich) | Steinberg Helpcenter (ital., Suchergebnis) – https://helpcenter.steinberg.de/hc/it/articles/17081395391378-Cubase-Nuendo-il-file-audio-viene-riprodotto-con-un-volume-troppo-alto-troppo-basso-troppo-veloce-o-troppo-lento |
| a 24 bit / 32 bit float | bit depth | Profondità di Bit (Ableton) | beibehalten: Website nennt nur Werte (‚WAV a 24 bit‘), kein Konflikt | Ableton – https://www.ableton.com/it/manual/recording-new-clips/ |
| marker / marcatore | marker | marcatore (GarageBand, Ableton); marker (Cubase) | UNSICHER weil DAWs uneinig; Apple-/Mehrheitsform ‚marcatore di cue‘ eingesetzt | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd8431c634/10.4.14/mac/15.6; Ableton – https://www.ableton.com/it/manual/arrangement-view/; Steinberg Cubase Artist 12 (ital., Suchergebnis-Auszug) – https://archive.steinberg.help/cubase_artist/v12/it/cubase_nuendo/topics/playback/playback_time_formats_r.html |
| esportazione / esporta | export | Esportazione / Esporta (Ableton, GarageBand); Esporta mixdown audio (Cubase) | übernommen: Substantiv ‚export‘ → ‚esportazione‘; ‚Export o Send Back‘ (Nr 172) und EXPORT WAV bleiben, weil Button-Namen | Ableton – https://www.ableton.com/it/manual/arrangement-view/; Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd7cbf5ed9/10.4.14/mac/15.6; Steinberg Cubase AI 13 (ital. Handbuch, Suchergebnis-Auszug) – https://steinberg.help/cubase_ai/v13/it/Cubase_AI_13_Manuale_operativo_it.pdf |
| plug-in | plug-in | plugin (GarageBand) | beibehalten weil ‚plug-in‘ verbreitete ital. Schreibung und auf allen Seiten einheitlich; UNSICHER nur in der Schreibweise | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbndac55f7f8/10.4.14/mac/15.6 |
| riduzione del rumore | noise reduction | kein DAW-Beleg gefunden | beibehalten (gemeinsprachlicher Fachbegriff); Wortstellung in 384/512 korrigiert (‚riduzione neurale del rumore‘) | keine – in den geöffneten Ableton-/GarageBand-Seiten nicht vorhanden |
| compressore | compressor | compressore (Fließtext), Compressor (Gerätename) | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/ |
| limiter | limiter | Limiter | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/ |
| EQ / equalizzatore | EQ | equalizzatori (Ableton); EQ (GarageBand) | übernommen (Website nutzt ‚EQ‘) | Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/; Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd56ab9fca/10.4.14/mac/15.6 |
| release / lookahead / soft-knee | release / lookahead / soft knee | Release (Parameter) bzw. rilascio im Fließtext; Lookahead; Soft Knee | beibehalten als Parameternamen; ‚look-ahead‘ in 512/536 auf ‚lookahead‘ vereinheitlicht | Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/ |
| ducking / ducker / multibanda | ducking / multiband | Ducking; multibanda | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/ |
| inviluppo | envelope | inviluppo | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/arrangement-view/; Ableton – https://www.ableton.com/it/manual/live-audio-effect-reference/ |
| testina | playhead | testina di riproduzione (GarageBand); marcatore d’inserimento (Ableton, anderes Konzept) | beibehalten (Kurzform von ‚testina di riproduzione‘) | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd912c61f4/10.4.14/mac/15.6; Ableton – https://www.ableton.com/it/manual/arrangement-view/ |
| annulla | undo | Annullare (GarageBand); Annullamenti (Ableton) | übernommen (deckungsgleich) | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd674b44b9/10.4.14/mac/15.6; Ableton – https://www.ableton.com/it/manual/arrangement-view/ |
| rifilare / rifila | trim | ridimensionare (GarageBand, Regionen); ritaglio (Ableton); Logic nur EN ‚Trim‘ | UNSICHER weil DAWs uneinig und keine ‚rifilare‘ sagt; beibehalten, weil ‚ridimensionare‘ die Bedeutung (Datei auf Bereich kürzen) verfehlt und die App-Buttons ohnehin TRIM heißen. Muttersprachler entscheiden | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbnd29c6925e/10.4.14/mac/15.6; Ableton – https://www.ableton.com/it/manual/arrangement-view/ |
| selezione | selection | selezione di tempo | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/arrangement-view/ |
| sessione | session | progetto (GarageBand, Ableton, Cubase) | beibehalten weil bei voyzSESSION der Produkt-/App-Begriff ‚Session‘ ist und Nr 29 die iOS-Audio-Session meint | Apple GarageBand – https://support.apple.com/it-it/guide/garageband/gbndd0893c9b/10.4.14/mac/15.6; Ableton – https://www.ableton.com/it/manual/arrangement-view/ |
| stem | stem | Stem (Logic, nur EN) | beibehalten weil App-Festlegung | Apple Logic Pro (it-it-Guide nur englisch) – https://support.apple.com/it-it/guide/logicpro/lgcp61bae908/12.3/mac/15.6 |
| channel strip | channel strip | channel strip (Logic, nur EN); Controlli delle Tracce (Ableton) | beibehalten (Logic-Begriff, im ital. Studio-Jargon üblich) | Apple Logic Pro (it-it-Guide nur englisch) – https://support.apple.com/it-it/guide/logicpro/lgcpbc2192ea/12.3/mac/15.6; Ableton – https://www.ableton.com/it/manual/mixing/ |
| mandata / monitoraggio / ingresso / uscita | send / monitoring / input / output | Mandata; monitoraggio; ingresso; uscita | übernommen (deckungsgleich) | Ableton – https://www.ableton.com/it/manual/mixing/ |
| conto alla rovescia | countdown / count-in | pre-conteggio (Ableton, für Metronom-Einzähler) | beibehalten weil ‚Vorlaufzähler‘ ein eingeblendeter Bild-Countdown für den Gast ist, kein Metronom-Einzähler | Ableton – https://www.ableton.com/it/manual/recording-new-clips/ |
| pre-roll | pre-roll | kein ital. Beleg gefunden | beibehalten (Anglizismus im Broadcast üblich) | keine |
| dispositivo aggregato | aggregate device | Aggregate Device (Apple EN), dispositivo agregado (Apple ES); ital. Apple-Seite nicht gefunden | UNSICHER weil ital. Apple-Bezeichnung nicht belegt; beibehalten | Apple (EN) – https://support.apple.com/en-ae/102171; Apple (ES) – https://support.apple.com/es-lamr/guide/audio-midi-setup/ams1010/mac |
| voice-over | voice-over | kein DAW-Beleg | beibehalten (Branchenbegriff; ‚voce fuori campo‘ wäre die gemeinsprachliche Alternative) | keine |
| loudness / true peak / gating | loudness / true peak / gating | Normbegriffe (EBU), in DAW-Handbüchern nicht belegt | beibehalten (Normbegriffe, nicht übersetzen) | EBU – https://tech.ebu.ch/publications/r128 |
| superficie di controllo | control surface | superficie di controllo (Ableton it) | übernommen (wie App-Hilfe help_it) | Ableton Live 12 (it) – https://www.ableton.com/it/live-manual/12/midi-and-key-remote-control/ |

### Für die Muttersprachler (IT, alle UNSICHER-Stellen)

- **Nr 64** – „Condizioni generali“: ‚Condizioni generali‘ korrekt; im ital. Onlinehandel üblicher ‚Termini e condizioni‘ oder ‚Condizioni generali di vendita‘
- **Nr 161** – „Scegli un pad in pegelWERK instant PLAYER → passalo a easy EDITOR → rifila, normalizza → c…“: Pfeile fehlen schon in DE-Quelle, Satz unlesbar; Pfeile auch in DE ergänzen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 175** – „App iOS nativa basata su JUCE. Motore R128 condiviso con pegelWERK loudness CORRECT.“: ‚su audio JUCE‘ Calque; JUCE ist Fremdprodukt – ggf. ganz streichen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 241** – „64 slot per i cue, organizzati in quattro banchi (A / B / C / D) da 16 pad ciascuno. Per o…“: DAWs uneinig: GarageBand/Ableton ‚marcatore‘, Cubase ‚marker‘; Apple-Mehrheit genommen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 268** – „Tocca un pad vuoto e si apre il selettore di file. Scegli l’audio dall’app File, da iCloud…“: DAWs uneinig: GarageBand/Ableton ‚marcatore‘, Cubase ‚marker‘; Apple-Mehrheit genommen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 276** – „App iOS nativa basata su JUCE. Audio in background attivo, così i cue continuano anche a s…“: ‚su audio JUCE‘ Calque; JUCE Fremdprodukt – ggf. streichen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 285** – „Mini anteprima con marcatore di cue“: DAWs uneinig: GarageBand/Ableton ‚marcatore‘, Cubase ‚marker‘; Apple-Mehrheit genommen *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 372** – „Il primo passaggio misura LUFS-I/S/M, LRA, TP. Il secondo scrive un nuovo file con gain st…“: Pfeile fehlen schon in DE-Quelle; Kette sonst unlesbar *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 452** – „Flusso di mix, non un kit di montaggio“: ‚kit di montaggio‘ für Baukasten: hier passend, aber Doppelsinn montaggio = Schnitt; mit 479/547/548 einheitlich entscheiden
- **Nr 479** – „Non è un kit di montaggio.“: ‚kit di montaggio‘ kann als ‚Schnitt-Kit‘ missverstanden werden; Alternative ‚scatola di montaggio‘/‚sistema modulare‘
- **Nr 508** – „MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC“: Fremdhersteller (MakePro X, Mackie, Elgato) aus DE übernommen; Kompatibilitätsangabe – Regel entscheiden
- **Nr 540** – „Mackie MCU · Elgato Stream Deck · OSC · console web per MakePro X (macOS)“: Mackie MCU, Elgato Stream Deck, MakePro X aus DE übernommen; wie Nr 508 entscheiden
- **Nr 547** – „Non è un kit di montaggio.<br>È uno strumento.“: ‚kit di montaggio‘ (Doppelsinn Schnitt) – einheitlich mit 452/479/548 entscheiden; Tags unverändert lassen
- **Nr 548** – „voyzSESSION PRO non è un kit di montaggio, ma uno strumento. Per una produzione vocale rap…“: ‚kit di montaggio‘ wie Nr 547; bei Änderung dort mitziehen

## Portugiesisch (pt-PT) (`pt/`)

**Anrede:** Höfliche 3. Person ohne Pronomen bzw. Imperativ der 3. Person („Abra“, „Experimente“, „Se quer …“, „o seu“) – so schreiben Apple Portugal und portugiesische Software-/Händlerseiten; „você“ wirkt in Portugal distanziert-brasilianisch, „tu“ zu salopp. Der Entwurf hält das durchgehend ein, kein „você“/„tu“ gefunden.

**Ergebnis:** 71 von 554 Einträgen korrigiert (davon 3 nur Typografie), 13 UNSICHER, 470 ok.

| Art | Einträge |
|---|---:|
| grammatik | 13 |
| rechtschreibung | 1 |
| typografie | 5 |
| formulierung | 26 |
| einheitlichkeit | 19 |
| pt-br | 25 |
| treue | 2 |

(Ein Eintrag kann mehrere Arten haben.)

### Die zehn wichtigsten Korrekturen

| Nr | Art | vorher | nachher | Grund |
|---|---|---|---|---|
| 419 | pt-br | `Sistema operacional` | `Sistema operativo` | BR „sistema operacional“ → pt-PT „sistema operativo“ |
| 436 | pt-br, grammatik | `Meus dados de áudio são enviados para a nuvem?` | `Os meus dados de áudio são enviados para a nuvem?` | pt-PT verlangt Artikel vor Possessiv („Os meus“); BR-Form ohne Artikel |
| 202 | pt-br, einheitlichkeit | `Loudness EBU R128 · True Peak · Clareza da fala · Batch · Controle MIDI` | `Loudness EBU R128 · True Peak · Clareza da fala · Batch · Controlo MIDI` | BR „controle“ → pt-PT „controlo“ (Glossar) |
| 455 | rechtschreibung, pt-br | `O AutoCut detecta pausas e erros de leitura e corta de forma limpa entre eles. A voz continua alinhada ao cue no ecrã.` | `O AutoCut deteta pausas e erros de leitura e corta de forma limpa entre eles. A voz continua alinhada ao cue no ecrã.` | „detecta“ ist BR/vor-AO90; pt-PT AO90 „deteta“ |
| 509 | treue | `O que faz o voyzSESSION PRO` | `O que distingue o voyzSESSION PRO` | „O que faz“ = „was es tut“; DE „ausmacht“ = was es auszeichnet |
| 254 | formulierung | `Aplicações` | `Casos de utilização` | „Aplicações“ heißt in pt-PT auch „Apps“ – missverständlich für „Einsatzgebiete“ |
| 498 | grammatik | `só o que a produção de voz realmente precisa` | `só aquilo de que a produção de voz realmente precisa` | „precisar de“ verlangt Relativ „de que“ |
| 507 | pt-br | `A sessão aparece como uma câmara própria - em qualquer app que use câmara. Com timecode gravado na imagem e contagem regressiva, sem software adicional (macOS)` | `A sessão aparece como uma câmara própria - em qualquer app que use câmara. Com timecode gravado na imagem e contagem decrescente, sem software adicional (macOS)` | BR „contagem regressiva“ → pt-PT „contagem decrescente“ |
| 451 | pt-br | `Layout repensado para o iPad: ecrã inteiro, escuro, barra de status oculta. Nada de interface desktop espremida, e sim uma operação feita para o polegar.` | `Layout repensado para o iPad: ecrã inteiro, escuro, barra de estado oculta. Nada de interface desktop espremida, mas sim uma operação feita para o polegar.` | BR „barra de status“ → „barra de estado“ (iOS pt-PT); BR „e sim“ → „mas sim“ |
| 379 | pt-br, grammatik | `Limitadores em tempo real precisam estimar; o loudness CORRECT mede o ficheiro primeiro, planeia a correção, grava de forma limpa, mede de novo e refina se houver desvio. É assim que se acerta o alvo exatamente, e não mais ou menos. Documentado por r…` | `Limitadores em tempo real precisam de estimar; o loudness CORRECT mede o ficheiro primeiro, planeia a correção, grava de forma limpa, mede de novo e refina se houver desvio. É assim que se acerta no alvo com exatidão, e não mais ou menos. Documentado por r…` | BR „precisam estimar“ → pt-PT „precisam de estimar“; „acertar no alvo“ |

### DAW-Abgleich der Fachbegriffe (25 Begriffe)

| Begriff auf der Website | EN | in den DAWs | Entscheidung | Quelle |
|---|---|---|---|---|
| faixa | track | faixa | übernommen (deckt sich mit App) | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| take | take | excerto (pasta de excertos) | beibehalten weil App-Festlegung „take“ und Broadcast-Jargon; Logic (Profi-DAW) zeigt in PT ohnehin englisch „take“ | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndf80e7097/10.4.14/mac/15.6; Apple Logic Pro (Mac) – https://support.apple.com/pt-pt/guide/logicpro/welcome/mac (Guide unter pt-pt/pt-br nur Englisch) |
| mistura / misturar | mix | mistura / misturar | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndf50dc69a/10.4.14/mac/15.6 |
| mesa de mistura | mixer / mixing console | – (GarageBand ohne Mixer-Fenster, Logic nicht lokalisiert) | beibehalten weil pt-PT-Standardbegriff und Glossar; kein DAW-Beleg vorhanden | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndf50dc69a/10.4.14/mac/15.6; Apple Logic Pro (Mac) – https://support.apple.com/pt-pt/guide/logicpro/welcome/mac (Guide unter pt-pt/pt-br nur Englisch) |
| fader (englisch) | fader | nivelador (für Regler/Slider) | beibehalten weil App-Festlegung „Fader“ englisch; nur der Lautstärke-Slider in 270 → „nivelador“ | Apple GarageBand (iPad, pt-PT) – https://support.apple.com/pt-pt/guide/garageband-ipad/chs175dc411/2.3.20/ipados/27 |
| Insert, Bus, Stem, Punch (englisch) | insert, bus, stem, punch | englisch (Logic Pro nur englisch verfügbar) | beibehalten weil App-Festlegung; Logic-Nutzer in PT sehen dieselben englischen Begriffe | Apple Logic Pro (Mac) – https://support.apple.com/pt-pt/guide/logicpro/welcome/mac (Guide unter pt-pt/pt-br nur Englisch) |
| cross-fade / FADE | crossfade / fade | iMovie: „fade“ (englisch, „efeito fade in“); GarageBand: „desvanecimento“ (Fade-out) | beibehalten weil FADE ein Bedienelement-Label ist und Apple pt-PT „fade“ selbst englisch führt; Apple ist uneinheitlich | Apple iMovie (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/imovie/move7a2dcdc6/10.4.4/mac/13.5; Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbnd5e8076d0/10.4/mac |
| forma de onda | waveform | forma de onda | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndca7725e3/10.4.14/mac/15.6 |
| puxadores (vorher: alças) | handles | puxador | übernommen, „alças“ korrigiert | Apple iMovie (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/imovie/move7a2dcdc6/10.4.4/mac/13.5 |
| frequência de amostragem | sample rate | taxa de amostragem | UNSICHER weil Apple pt-PT „taxa de amostragem“ sagt, die App aber „frequência de amostragem“ festlegt; beibehalten bis App und Website gemeinsam entscheiden | Apple Support (pt-PT) – https://support.apple.com/pt-pt/HT212854 |
| marcador | marker | marcador | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| exportar / exportação | export | exportar | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbnd7cbf5ed9/10.4.14/mac/15.6 |
| plug-in | plug-in | plug-in(s) | übernommen; „plugin“ vereinheitlicht | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| compressor | compressor | compressor / compressão | übernommen | Apple GarageBand (iPad, pt-PT) – https://support.apple.com/pt-pt/guide/garageband-ipad/chs175dc411/2.3.20/ipados/27 |
| EQ / equalizador | EQ | EQ / equalizador / equalização | übernommen (Website nutzt „EQ“) | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| cursor de reprodução | playhead | cursor de reprodução | übernommen (deckt sich mit App) | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| timeline | timeline | cronograma (iMovie); Logic nur englisch | UNSICHER weil Apple-Videoschnitt „cronograma“ sagt, DAW-Jargon „timeline“; außerdem 124 „linha do tempo“ uneinheitlich | Apple iMovie (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/imovie/move7a2dcdc6/10.4.4/mac/13.5; Apple Logic Pro (Mac) – https://support.apple.com/pt-pt/guide/logicpro/welcome/mac (Guide unter pt-pt/pt-br nur Englisch) |
| aparar | trim | encurtar (Regionen/Clips) | UNSICHER weil Apple pt-PT „encurtar“ nutzt; „aparar“ ist verständlich und im easy EDITOR durchgängig, Massenänderung nur nach Muttersprachler-Entscheid | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndca7725e3/10.4.14/mac/15.6; Apple iMovie (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/imovie/toc |
| desfazer | undo | desfazer / refazer | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/gbndca7725e3/10.4.14/mac/15.6 |
| gravar / gravação | record / recording | gravar / gravação | übernommen | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| locução | voice-over | locução („Gravar uma locução“) | übernommen | Apple iMovie (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/imovie/toc |
| definições | settings | definições | übernommen (deckt sich mit App) | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| guardar | save | guardar („Criar, guardar e apagar projetos“) | übernommen (deckt sich mit App) | Apple GarageBand (Mac, pt-PT) – https://support.apple.com/pt-pt/guide/garageband/toc |
| cue (englisch) | cue | – (kein DAW-Beleg) | beibehalten weil App-Festlegung; Theater-/Radio-Jargon | Apple Logic Pro (Mac) – https://support.apple.com/pt-pt/guide/logicpro/welcome/mac (Guide unter pt-pt/pt-br nur Englisch) |
| consola de hardware | control surface | – (keine pt-PT-DAW-Quelle); FR/ES/IT-DAWs: surface/superficie | UNSICHER: App-README legt „consola“ fest, App-Hilfe help_pt sagt „superfície de controlo“ | keine pt-PT-DAW-Quelle; Vergleich: Ableton Live 12 (it/es/fr) – https://www.ableton.com/it/live-manual/12/midi-and-key-remote-control/ |

### Für die Muttersprachler (PT, alle UNSICHER-Stellen)

- **Nr 64** – „Termos e Condições“: „Termos e Condições“ üblich und korrekt; juristisch prüfen, ob „Condições Gerais de Venda“ gemeint ist
- **Nr 65** – „Direito de livre resolução“: „Direito de livre resolução“ ist der DL-24/2014-Begriff; juristische Bestätigung gewünscht, sprachlich korrekt
- **Nr 81** – „O medidor de loudness profissional para emissão, pós-produção e broadcast ao vivo, em conf…“: „broadcast ao vivo“: im pt-PT-Rundfunk üblicher „em direto“; gilt auch für „previsão ao vivo“ (22 u. a.). Muttersprachler entscheiden
- **Nr 150** – „Aparar, cortar, desfazer“: „aparar“ für Trim; Apple pt-PT nutzt „encurtar“ (Regionen/Clips). Betrifft auch 149, 161, 180–183, 251, 270, 294
- **Nr 173** – „EXPORT WAV guarda um WAV de 24 bits (frequência de amostragem nativa, opcionalmente normal…“: Apple pt-PT sagt „taxa de amostragem“; App-Festlegung „frequência de amostragem“ beibehalten – App und Website gemeinsam entscheiden
- **Nr 260** – „Jingles · Stings · Camas“: „camas“ im PT-Radio verständlich, aber „camas musicais“ oder „fundos musicais“ wäre eindeutiger; Muttersprachler entscheiden
- **Nr 478** – „O <b>prompter está a bordo</b> - com deslocamento automático que acompanha a voz e reconhe…“: „plugin“ → „plug-in“ wie Apple pt-PT und 149/180/480 \| „consola de hardware“ beibehalten (App-README legt „consola“ fest); DAWs in FR/ES/IT und die App-Hilfe help_pt sagen „superfície de controlo“ – gemeinsam mit der App entscheiden *(Vorschlag übernommen, bitte bestätigen)*
- **Nr 503** – „Ligue uma consola de hardware“: „consola de hardware“ beibehalten (App-README legt „consola“ fest); DAWs in FR/ES/IT und die App-Hilfe help_pt sagen „superfície de controlo“ – gemeinsam mit der App entscheiden
- **Nr 508** – „MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC“: Fremdhersteller (Mackie, Elgato, MakePro X) wie im DE; als unterstützte Hardware wohl nötig, Freigabe durch Auftraggeber
- **Nr 514** – „Guião à esquerda, vídeo à direita, timeline em baixo - uma só página. O texto desloca-se c…“: „timeline“ englisch; Apple iMovie pt-PT sagt „cronograma“, Logic ist nicht lokalisiert; 124 hat „linha do tempo“ – vereinheitlichen?
- **Nr 540** – „Mackie MCU · Elgato Stream Deck · OSC · consola web para MakePro X (macOS)“: wie 508: Mackie/Elgato/MakePro X aus dem Original; Freigabe durch Auftraggeber
- **Nr 553** – „A DAW para produção de voz - locução, peça, podcast, audiodrama. O Assist faz a mistura au…“: „consola de hardware“ beibehalten (App-README legt „consola“ fest); DAWs in FR/ES/IT und die App-Hilfe help_pt sagen „superfície de controlo“ – gemeinsam mit der App entscheiden
- **Nr 554** – „voyzSESSION PRO: mesa de mistura com canais de voz, áudio e grupo, timeline com formas de …“: „timeline“ englisch; Apple iMovie pt-PT sagt „cronograma“, Logic ist nicht lokalisiert; 124 hat „linha do tempo“ – vereinheitlichen?
