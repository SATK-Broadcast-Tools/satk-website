# Entscheidungen zu den UNSICHER-Stellen (FR, ES, IT, PT)

Stand 01.11.2026, Branch `claude/website-unsicher-521aaf`, aufgesetzt auf `2a4da11` (Gegenlesen).
Dritter, unabhängiger Prüfer. Der Nutzer hat keine Muttersprachler, deshalb ist jede Stelle anhand von Quellen
entschieden, nicht weitergereicht.

## Ergebnis in Zahlen

* **61 von 61 UNSICHER-Stellen entschieden** (FR 22, ES 12, IT 14, PT 13). In den CSVs steht kein `UNSICHER` mehr.
  Spalte `pruefung` beginnt mit „entschieden:“, Spalte `quelle` enthält die Belege mit URL.
* Davon **geändert 22** (FR 10, ES 1, IT 7, PT 4), **beibehalten 39**. Beibehalten heißt: geprüft und begründet, nicht „offen gelassen“.
* **Mitgezogen** an 19 weiteren Stellen, damit ein Begriff auf allen Seiten gleich heißt (z. B. PT „aparar“ → „encurtar“ überall).
* **Ton** (Ganz-Lesen von `index`, `voyzsession`, `mac` je Sprache): 21 Schlüssel in 19 Sätzen vorsichtig geglättet.
* Bei jeder geänderten Zeile steht der neue Text auch in `Korrektur`. Ein späteres `--import-review` setzt also nicht
  den alten Stand zurück.

## Prüfung (gemessen)

* `python3 tools/build-i18n.py`: 18 Dateien geschrieben. `--check`: kein Drift. `--review`: CSV-Spalte `Entwurf` aktualisiert.
* `python3 tools/check-links.py`: 90 Seiten, 18 hreflang-Gruppen, keine Fehler.
* Strukturvergleich (Nachbau des Gegenleser-Skripts: Tag-Folge, alle Attribute außer `alt`/`title`/`placeholder`/
  `aria-label`/übersetzte `meta content`, Kommentare, Skripte mit maskierten Strings) gegen `2a4da11`:
  **48 Seiten, 0 Abweichungen**. Gegenprobe mit absichtlich geändertem `href` in `es/support.html`: erkannt.
* Geändert sind nur `tools/i18n/{fr,es,it,pt}.json`, die vier `gegenlesen-*.csv`, die erzeugten Seiten unter
  `/fr/ /es/ /it/ /pt/` und diese Datei. DE, EN und der Generator sind unberührt.

## Wie entschieden wurde

Rangfolge der Quellen: (a) Microsoft-Terminologie/Learn in der Sprache, (b) Apples lokalisierte Handbücher
(Logic, Final Cut, iMovie), (c) Gesetzestexte und IATE, (d) lokalisierte DAW-Handbücher, (e) Fachgebrauch.
Dazu die gemeinsamen App-Begriffe (`tools/lang/README.md` und die Sprachtabellen
`Source/Localization/Tables/LangTable_*.h` auf `origin/claude/sprachen-stufe1-2574ac` im App-Repo).

Sicherheitsgrade, wie im Projekt üblich:
* **gemessen**: Seite selbst abgerufen und die Stelle gelesen (alle URLs in `quelle`, außer den unten genannten).
* **gelesen**: nur aus dem Bericht des Gegenlesers übernommen. Steht dann im Text als „Angabe des Gegenlesers,
  hier nicht nachgeprüft“ (Logic FR „module“, Apple pt-PT „taxa de amostragem“).
* **gefolgert**: kein Beleg gefunden; dann ist die vorsichtigste, eindeutigste Form gewählt und das steht dabei.

Grundsatz bei Fachbegriffen: **Die Website benennt, was der Nutzer in der App sieht.** Wo Apple und die App
denselben Begriff haben, gewinnt dieser auch gegen eine DAW, die übersetzt (FR Release/Lookahead/pre-roll).
Microsoft-Terminologie ist allgemeine Software; wo sie für Audio unpassend wäre (ES „complemento“ für ein
VST3/AU-Plug-in), ist sie benannt und begründet verworfen.

Hinweis zu den Apple-FR-Belegen: Die abgerufenen französischen Apple-Handbuchseiten liegen unter `fr-afri`
(französische Ausgabe für Afrika). `fr-fr` habe ich nicht eigens abgerufen; Abweichungen sind dort nicht zu erwarten, aber nicht geprüft.

## Französisch

### Die 22 UNSICHER-Stellen

| Nr | vorher | nachher | Entscheidung | Beleg |
|---|---|---|---|---|
| 8 | Développé par un ingénieur broadcast en activité, pour les ingénieurs broadcast. Le même m… | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 84 | …z le master d’une fiction radio ou meniez une émission en direct, loudnes… | …z le master d’une fiction radio ou assuriez une émission en direct, loudnes… | „assuriez une émission en direct“: „mener“ heißt moderieren/leiten; für den Techniker sagt man „assurer un direct“. | [INA-Ausbildung Tontechnik: „assurer un direct“](https://campus.ina.fr/print/pdf/taxonomy_term/1640200?year=2025) |
| 180 | Pas de multipiste, pas de plug-ins, pas de MIDI : si vous en avez besoin, prenez une DAW. … | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 188 | pegelWERK : apps et plug-ins pour la production média professionnelle. | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 218 | Plug-in · VST3 · AU | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 301 | Apps et plug-ins pour la production média professionnelle. | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 317 | …êtes inter-échantillons avec 5 ms d’anticipation et un relâchement exponentiel de 50 ms. Enveloppe à … | …êtes inter-échantillons avec 5 ms de lookahead et un release exponentiel de 50 ms. Enveloppe à … | Release und Lookahead englisch: Apple FR (Compressor in Logic/Final Cut) lässt beide englisch, die App FR auch („mémoire de release“, „sans lookahead“). Ableton übersetzt nur in Klammern. Genus: „un release“ (Fachjargon). | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>[Ableton FR: „Release (rétablissement](https://www.ableton.com/fr/manual/live-audio-effect-reference/)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 321 | …<= 150 Hz et >= 3 kHz. Compression à genou doux par bande avec constantes de temps… | …<= 150 Hz et >= 3 kHz. Compression soft knee par bande avec constantes de temps… | „soft knee“ englisch: Apple FR schreibt „(soft knee)“, Ableton FR lässt „Knee“ englisch; „genou doux“ fand sich in keiner der Quellen. | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>[Ableton FR: „Release (rétablissement](https://www.ableton.com/fr/manual/live-audio-effect-reference/) |
| 355 | … qu’il mesure, il le limite. 5 ms d’anticipation, enveloppe à double constante de temps, relâchement exponentiel de 50 ms. Des courbes … | … qu’il mesure, il le limite. 5 ms de lookahead, enveloppe à double constante de temps, release exponentiel de 50 ms. Des courbes … | wie Nr 317: „5 ms de lookahead“, „release exponentiel“. | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>[Ableton FR: „Release (rétablissement](https://www.ableton.com/fr/manual/live-audio-effect-reference/)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 357 | …00 Hz, aigu > 3000 Hz. Compresseur à genou doux par bande avec enveloppe RMS. Cons… | …00 Hz, aigu > 3000 Hz. Compresseur soft knee par bande avec enveloppe RMS. Cons… | wie Nr 321: „Compresseur soft knee par bande“. | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>[Ableton FR: „Release (rétablissement](https://www.ableton.com/fr/manual/live-audio-effect-reference/) |
| 405 | Allemand et anglais. | (unverändert) | beibehalten: Der Satz nennt die tatsächlichen Supportsprachen. Ein Zusatz („gern auf Englisch“) wäre Inhalt, keine Übersetzung – gehört in die DE-Quelle (Betreiber). | – |
| 421 | (facultatif, uniquement pour un plug-in) | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 431 | Les clés de licence vous sont envoyées par e-mail par Paddle juste après l’achat (pour les… | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 433 | Les licences plug-in et autonomes sont valables pour 2 ordinateurs. Les apps de l’App Stor… | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 463 | … sur l’iPad (USB-C / Lightning), pré-roll, affichage de niveau clair. T… | … sur l’iPad (USB-C / Lightning), pre-roll, affichage de niveau clair. T… | „pre-roll“ ohne Akzent: Apple FR „Durée de pre-roll“, App FR „Pre-roll marche/arrêt“. | [Apple FR: „Durée de pre-roll“, ohne Akzent](https://support.apple.com/fr-afri/guide/final-cut-pro/verb8e60ab7/10.5.3/mac)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 469 | Lancez le pré-roll, enregistrez le take, continu… | Lancez le pre-roll, enregistrez le take, continu… | wie Nr 463. | [Apple FR: „Durée de pre-roll“, ohne Akzent](https://support.apple.com/fr-afri/guide/final-cut-pro/verb8e60ab7/10.5.3/mac)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 480 | voyzSESSION n’est pas un fragment de DAW pour iPad. C’est un outil ciblé po… | voyzSESSION n’est pas une DAW amputée pour iPad. C’est un outil ciblé po… | „une DAW amputée pour iPad“ statt „fragment de DAW“: gemeint ist eine gekürzte DAW. Kein autoritativer Beleg; „version amputée“ ist die verbreitete Wendung der frz. Softwarepresse. plug-in wie Nr 8. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic) |
| 508 | MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC | (unverändert) | beibehalten wie DE-Quelle: Kompatibilitätsangabe mit Produktnamen; Neutralisieren wäre eine Inhaltsänderung der DE-Quelle (Betreiber), keine Sprachfrage. | – |
| 512 | …veler et un ducker multibande avec anticipation. | …veler et un ducker multibande avec lookahead. | Lookahead englisch wie Nr 317 (Apple FR, App FR). | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 521 | Vos plug-ins, votre son | (unverändert) | „plug-in“ beibehalten: Microsoft FR schreibt „plug-in(s)“, die App FR ebenso; Logic FR „module“ (Angabe des Gegenlesers, hier nicht nachgeprüft) verworfen, weil „module“ auf der Seite neben VST3/AU als Teil einer App gelesen würde. | [Microsoft FR: „plug-ins“](https://learn.microsoft.com/fr-fr/power-apps/developer/data-platform/best-practices/business-logic)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 536 | SmartDucker multibande, avec anticipation | SmartDucker multibande, avec lookahead | wie Nr 512. | [Apple FR, Compressor: „Release“, „Lookahead“, „(soft knee](https://support.apple.com/fr-afri/guide/final-cut-pro-logic-effects/lgex931a1d54/mac)<br>App FR: „plug-in“, „pre-roll“, „release“, „lookahead“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_FR.h) |
| 540 | Mackie MCU · Elgato Stream Deck · OSC · console web pour MakePro X (macOS) | (unverändert) | wie Nr 508. | – |

### Mitgezogen (dieselbe Entscheidung an weiteren Stellen)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 161 | … pad dans pegelWERK instant PLAYER transmettre à easy EDITOR couper, normaliser SEND BACK : le résultat revient da… | … pad dans pegelWERK instant PLAYER → transmettre à easy EDITOR → couper, normaliser → SEND BACK : le résultat revient da… | Pfeile der Kette ergänzt (fehlen in DE-Quelle, IT hat sie schon) |
| 372 | …nouveau fichier avec gain statique correction LRA multibande optionnelle limiteur TP. | …nouveau fichier avec gain statique → correction LRA multibande optionnelle → limiteur TP. | Pfeile der Kette ergänzt (wie IT) |

### Ton (Ganz-Lesen index, voyzsession, mac)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 194 | …pour 2 ordinateurs. Paiement unique. Paiement sécurisé via Paddle. | …pour 2 ordinateurs. Paiement unique et sécurisé via Paddle. | Doppelung „Paiement … Paiement“ zusammengezogen |
| 195 | …ites. Mises à jour majeures à prix de mise à niveau réduit. | …ites. Mises à jour majeures à prix réduit. | „à prix de mise à niveau réduit“ schwerfällig, Wort-für-Wort |
| 196 | Assistance par e-mail directement par le développeur. Pas de file d’attente… | Assistance par e-mail, directement auprès du développeur. Pas de file d’attente… | „par … par“ doppelt; „auprès de“ ist die übliche Wendung |
| 400 | Assistance par e-mail directement par le développeur. Pas de file d’attente… | Assistance par e-mail, directement auprès du développeur. Pas de file d’attente… | „par … par“ doppelt; „auprès de“ ist die übliche Wendung |
| 439 | …ness CORRECT. Assistance par e-mail directement par le développeur. | …ness CORRECT. Assistance par e-mail, directement auprès du développeur. | „par … par“ doppelt; „auprès de“ ist die übliche Wendung |
| 489 | …t au niveau de diffusion, l’export part en WAV, en MXF ou directement ave… | …t au niveau de diffusion, l’export se fait en WAV, en MXF ou directement ave… | „l’export part en“ wörtlich aus „geht raus“ |
| 512 | …ruitage neuronal (DeepFilterNet 3) tire une qualité studio même d’un environnement bruyant, dosable en continu au fader. S’y ajoute l… | …ruitage neuronal (DeepFilterNet 3) offre une qualité studio même dans un lieu bruyant, et se dose en continu au fader. S’y ajoute l… | „tirer une qualité d’un environnement“ und nachgestelltes „dosable“ klangen übersetzt |
| 522 | …e dans toute DAW. Ce qui tourne en direct sonne de façon identique à l’export. macOS. | …e dans toute DAW. Ce qui tourne en temps réel sonne à l’identique à l’export. macOS. | „en direct“ = Sendung; gemeint ist Echtzeit (wie PT) |
| 548 | …n vocale rapide et professionnelle au quotidien en rédaction, et pour le jour où il f… | …n vocale rapide et professionnelle dans le quotidien d’une rédaction, et pour le jour où il f… | idiomatische Fügung |

## Spanisch

### Die 12 UNSICHER-Stellen

| Nr | vorher | nachher | Entscheidung | Beleg |
|---|---|---|---|---|
| 8 | Desarrollado por un ingeniero de broadcast en activo para ingenieros de broadcast. El mism… | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 188 | pegelWERK - apps y plug-ins para producciones audiovisuales profesionales. | (unverändert) | „producciones audiovisuales“ beibehalten (statt Calque „de medios“): „audiovisual“ schließt im span. Recht den Hörfunk ein. plug-in wie Nr 8. | [Ley 13/2022 General de Comunicación Audiovisual, Art. 2.7 sc](https://www.boe.es/buscar/act.php?id=BOE-A-2022-11311)<br>[Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf) |
| 218 | Plug-in · VST3 · AU | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 301 | Apps y plug-ins para producciones audiovisuales profesionales. | (unverändert) | wie Nr 188. | [Ley 13/2022 General de Comunicación Audiovisual, Art. 2.7 sc](https://www.boe.es/buscar/act.php?id=BOE-A-2022-11311)<br>[Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf) |
| 421 | (opcional, solo para plug-ins) | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 431 | Las claves de licencia llegan por correo electrónico de Paddle justo después de la compra … | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 433 | Las licencias de plug-in y standalone son válidas para 2 ordenadores. Las apps del App Sto… | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 478 | …Pad no incluye las herramientas de taller de la versión para Mac: <b>plug-in… | …Pad no incluye las herramientas de estudio de la versión para Mac: <b>plug-in… | „herramientas de estudio“ statt „de taller“ (gleich IT „strumenti da studio“); „superficies de control“ und „plug-ins“ wie Nr 8. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf) |
| 508 | MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC | (unverändert) | beibehalten wie DE-Quelle (siehe FR Nr 508). | – |
| 518 | Whisper transcribe sin conexión y con precisión de palabra, todas las pistas en un solo te… | (unverändert) | „cursor de reproducción“ beibehalten: Logic ES (selbst nachgeprüft). App ES verkürzt auf „cursor“. | [Logic ES: „cursor de reproducción“](https://support.apple.com/es-es/guide/logicpro/lgcp0ec9fc09/mac)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 521 | Tus plug-ins, tu sonido | (unverändert) | „plug-in(s)“ beibehalten: Microsoft ES sagt allgemein „complemento“, im Audiobereich schreibt Cubase ES „plug-ins“; „complemento“ wäre neben VST3/AU unüblich. App ES schreibt „plugin“ – siehe „Auch für die App“. | [Cubase ES: „Instalar y gestionar plug-ins VST“](https://archive.steinberg.help/cubase_ai/v11/es/Cubase_AI_11_Manual_de_operaciones_es.pdf)<br>[Microsoft ES: „complementos“, allgemeine Software](https://learn.microsoft.com/es-es/training/modules/introduction-dataverse-developers/extensibility)<br>App ES: „plugin“ ohne Bindestrich (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_ES.h) |
| 540 | Mackie MCU · Elgato Stream Deck · OSC · consola web para MakePro X (macOS) | (unverändert) | wie Nr 508. | – |

### Ton (Ganz-Lesen index, voyzsession, mac)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 194 | …lida para 2 ordenadores. Pago único. Pago seguro a través de Paddle. | …lida para 2 ordenadores. Pago único y seguro a través de Paddle. | Doppelung „Pago … Pago“ zusammengezogen |
| 489 | …nivel de emisión y la exportación sale como WAV, MXF o directamente con el víd… | …nivel de emisión y la exportación se hace en WAV, MXF o directamente con el víd… | „sale como“ wörtlich aus „geht raus als“ |
| 522 | …T3, como en cualquier DAW. Lo que suena en directo suena idéntico en la exportación. … | …T3, como en cualquier DAW. Lo que se procesa en tiempo real suena idéntico en la exportación. … | „suena … suena“ doppelt; „en directo“ = Sendung, gemeint ist Echtzeit |

## Italienisch

### Die 14 UNSICHER-Stellen

| Nr | vorher | nachher | Entscheidung | Beleg |
|---|---|---|---|---|
| 64 | Condizioni generali | (unverändert) | „Condizioni generali“ beibehalten: Rechtsbegriff „condizioni generali di contratto“ (Art. 1341 c.c.), gleichlaufend mit FR „CGV“ und ES „Condiciones generales“; als Fußzeilen-Link kurz genug. | [Codice civile Art. 1341 „Condizioni generali di contratto“](https://www.brocardi.it/codice-civile/libro-quarto/titolo-ii/capo-ii/sezione-i/art1341.html) |
| 161 | Scegli un pad in pegelWERK instant PLAYER → passalo a easy EDITOR → rifila, normalizza → c… | (unverändert) | Pfeile beibehalten (Kette sonst unlesbar); jetzt auch in FR und PT ergänzt. Die DE-Quelle repariert die Übersetzungs-Sitzung. | – |
| 175 | App iOS nativa basata su JUCE. Motore R128 condiviso con pegelWERK loudness CORRECT. | (unverändert) | „basata su JUCE“ beibehalten: Faktangabe der DE-Quelle, kein Calque mehr; „App iOS nativa su JUCE 8“ an anderer Stelle angeglichen. | – |
| 241 | …AUTO-CUE. Mini forma d’onda con marcatore di cue direttamente su ogni pad. | …AUTO-CUE. Mini forma d’onda con marker di cue direttamente su ogni pad. | „marker di cue“ statt „marcatore“: Logic IT lässt „Marker“ englisch, die App IT sagt „marker“ („Vai al marker successivo“). | [Logic IT: „Marker“ bleibt englisch](https://support.apple.com/it-it/guide/logicpro/lgcp0ec9fc09/mac)<br>App IT: „marker“, „plugin“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_IT.h) |
| 268 | …nteprima della forma d’onda con marcatore di cue. | …nteprima della forma d’onda con marker di cue. | „marker di cue“ statt „marcatore“: Logic IT lässt „Marker“ englisch, die App IT sagt „marker“ („Vai al marker successivo“). | [Logic IT: „Marker“ bleibt englisch](https://support.apple.com/it-it/guide/logicpro/lgcp0ec9fc09/mac)<br>App IT: „marker“, „plugin“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_IT.h) |
| 276 | App iOS nativa basata su JUCE. Audio in background attivo, così i cue continuano anche a s… | (unverändert) | wie Nr 175. | – |
| 285 | Mini anteprima con marcatore di cue | Mini anteprima con marker di cue | „marker di cue“ statt „marcatore“: Logic IT lässt „Marker“ englisch, die App IT sagt „marker“ („Vai al marker successivo“). | [Logic IT: „Marker“ bleibt englisch](https://support.apple.com/it-it/guide/logicpro/lgcp0ec9fc09/mac)<br>App IT: „marker“, „plugin“ (App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_IT.h) |
| 372 | Il primo passaggio misura LUFS-I/S/M, LRA, TP. Il secondo scrive un nuovo file con gain st… | (unverändert) | wie Nr 161. | – |
| 452 | Flusso di mix, non un kit di montaggio | Flusso di lavoro per il mix, non un editor da assemblare | „Flusso di lavoro per il mix, non un editor da assemblare“: vermeidet den Doppelsinn montaggio (= Videoschnitt) auf einer Schnitt-/Mischseite. Kein autoritativer Beleg; „kit da assemblare“ ist die eindeutige Alltagsform. | – |
| 479 | Non è un kit di montaggio. | Non è un kit da assemblare. | „kit da assemblare“ statt „kit di montaggio“ (Doppelsinn Schnitt), einheitlich mit Nr 452. | – |
| 508 | MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC | (unverändert) | beibehalten wie DE-Quelle (siehe FR Nr 508). | – |
| 540 | Mackie MCU · Elgato Stream Deck · OSC · console web per MakePro X (macOS) | (unverändert) | wie Nr 508. | – |
| 547 | Non è un kit di montaggio.<br>È uno strumento. | Non è un kit da assemblare.<br>È uno strumento. | „kit da assemblare“ statt „kit di montaggio“ (Doppelsinn Schnitt), einheitlich mit Nr 452. | – |
| 548 | voyzSESSION PRO non è un kit di montaggio, ma uno strumento. Per una produzi… | voyzSESSION PRO non è un kit da assemblare, ma uno strumento. Per una produzi… | „kit da assemblare“ statt „kit di montaggio“ (Doppelsinn Schnitt), einheitlich mit Nr 452. | – |

### Mitgezogen (dieselbe Entscheidung an weiteren Stellen)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 475 | App iOS nativa su JUCE 8. Motore R128 condiviso co… | App iOS nativa basata su JUCE 8. Motore R128 condiviso co… | einheitlich mit „basata su JUCE“ |

### Ton (Ganz-Lesen index, voyzsession, mac)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 194 | …ale per 2 computer. Pagamento unico. Pagamento sicuro tramite Paddle. | …ale per 2 computer. Pagamento unico e sicuro tramite Paddle. | Doppelung „Pagamento … Pagamento“ zusammengezogen |
| 464 | In 4 passi al servizio finito | Il servizio pronto in 4 passi | Telegrammstil aus dem Deutschen („In 4 Schritten zum …“) |
| 489 | …livello di messa in onda, l’export esce come WAV, MXF o direttamente insieme al… | …livello di messa in onda, l’export avviene in WAV, MXF o direttamente insieme al… | „esce come“ wörtlich aus „geht raus als“ |
| 522 | … e VST3, come in ogni DAW. Ciò che suona dal vivo, suona identico nell’esportazione. … | … e VST3, come in ogni DAW. Ciò che gira in tempo reale suona identico nell’esportazione. … | „suona … suona“ doppelt; „dal vivo“ = Auftritt, gemeint ist Echtzeit |

## Portugiesisch (pt-PT)

### Die 13 UNSICHER-Stellen

| Nr | vorher | nachher | Entscheidung | Beleg |
|---|---|---|---|---|
| 64 | Termos e Condições | (unverändert) | „Termos e Condições“ beibehalten: im port. Onlinehandel die übliche Linkbezeichnung; der Gesetzesbegriff (Cláusulas Contratuais Gerais, DL 446/85) gehört in den Seitentext, nicht in die Fußzeile. | – |
| 65 | Direito de livre resolução | (unverändert) | „Direito de livre resolução“ beibehalten: gesetzliche Bezeichnung im DL 24/2014 (Art. 10 ff.), so auch DECO. | [DL 24/2014, Art. 10 ff.](https://www.fd.ulisboa.pt/wp-content/uploads/2023/03/Decreto-Lei-24-2014-contratos-celebrados-a-distancia-e-fora-do-estabelecimento-comercial.pdf); [DECO: „formulário de livre resolução“](https://www.deco.proteste.pt/info/institucional/formulario-de-livre-resolucao) |
| 81 | …ional para emissão, pós-produção e broadcast ao vivo, em conformidade com EBU R128 / I… | …ional para emissão, pós-produção e transmissões em direto, em conformidade com EBU R128 / I… | „transmissões em direto“: pt-PT-Rundfunk sagt „em direto“ (RTP), „ao vivo“ ist der Live-Auftritt. Zugleich „previsão ao vivo“ → „previsão em tempo real“ (4×) und „medidor/corre ao vivo“ → „em tempo real“. | [RTP: „Emissões em Direto“, „TV em direto“](https://www.rtp.pt/play/direto) |
| 150 | Aparar, cortar, desfazer | Encurtar, cortar, desfazer | „Encurtar“ statt „Aparar“: Apple pt-PT (iMovie) „Encurtar clips“. Auf allen PT-Seiten angeglichen (aparar/apare → encurtar/encurte). | [Apple pt-PT: „Encurtar clips“, „cronograma“](https://support.apple.com/pt-pt/guide/imovie/welcome/mac) |
| 173 | EXPORT WAV guarda um WAV de 24 bits (frequência de amostragem nativa, opcionalmente normal… | (unverändert) | „frequência de amostragem“ beibehalten: IATE-Form (über Infopedia) und App-Festlegung; Apple pt-PT sagt laut Gegenleser „taxa“ (hier nicht nachgeprüft) – siehe Restrisiko. | [Infopedia nach IATE: sampling rate = „frequência de amostrag](https://www.infopedia.pt/dicionarios/ingles-portugues/sampling)<br>App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h) |
| 260 | Jingles · Stings · Camas | Jingles · Stings · Camas musicais | „Camas musicais“: „camas“ allein ist mehrdeutig. Kein autoritativer Beleg gefunden; ausgeschriebene Form ist die vorsichtigere. | – |
| 478 | … Fora da versão para iPad ficam as partes de oficina da versão para Mac: <b>plug-ins AU… | … Fora da versão para iPad ficam as ferramentas de estúdio da versão para Mac: <b>plug-ins AU… | „ferramentas de estúdio“ statt „partes de oficina“ (gleich IT); „plug-ins“ und „consolas de hardware“ wie Nr 503. | App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h) |
| 503 | Ligue uma consola de hardware | (unverändert) | „consola de hardware“ beibehalten: App-Festlegung (README tools/lang) und wörtlich DE „Hardware-Konsole“. Die App-Hilfe help_pt sagt „superfície de controlo“ – Uneinheitlichkeit liegt in der App. | App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h) |
| 508 | MakePro X (MPX), Mackie MCU, Elgato Stream Deck, OSC | (unverändert) | beibehalten wie DE-Quelle (siehe FR Nr 508). | – |
| 514 | Guião à esquerda, vídeo à direita, timeline em baixo - uma só página. O texto desloca-se c… | (unverändert) | „timeline“ beibehalten: so heißt das Bedienelement in der App PT („Timeline: mais ou menos tempo no ecrã“). Apple iMovie pt-PT sagt „cronograma“ – siehe Restrisiko. „linha do tempo“ im PDF-Bericht des Broadcast-Meters bleibt, das ist ein Zeitdiagramm, nicht die Schnitt-Timeline. | App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h)<br>[Apple pt-PT: „Encurtar clips“, „cronograma“](https://support.apple.com/pt-pt/guide/imovie/welcome/mac) |
| 540 | Mackie MCU · Elgato Stream Deck · OSC · consola web para MakePro X (macOS) | (unverändert) | wie Nr 508. | – |
| 553 | A DAW para produção de voz - locução, peça, podcast, audiodrama. O Assist faz a mistura au… | (unverändert) | wie Nr 503. | App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h) |
| 554 | voyzSESSION PRO: mesa de mistura com canais de voz, áudio e grupo, timeline com formas de … | (unverändert) | wie Nr 514. | App PT: „Timeline“, „frequência de amostragem“, „consola“ (README tools/lang + App-Tabelle satk-overdub-studio origin/claude/sprachen-stufe1-2574ac:Source/Localization/Tables/LangTable_PT.h)<br>[Apple pt-PT: „Encurtar clips“, „cronograma“](https://support.apple.com/pt-pt/guide/imovie/welcome/mac) |

### Mitgezogen (dieselbe Entscheidung an weiteren Stellen)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 15 | …ormato tátil. Silero VAD, previsão ao vivo, PPM, goniómetro, radar, FFT, hist… | …ormato tátil. Silero VAD, previsão em tempo real, PPM, goniómetro, radar, FFT, hist… | „ao vivo“ = Live-Auftritt; Prognose läuft in Echtzeit |
| 22 | Previsão ao vivo até ao fim da emissão | Previsão em tempo real até ao fim da emissão | wie 1 |
| 53 | …iPhone), MIDI Learn, GPI, previsão ao vivo, histogramas, Loudness Radar. Quem… | …iPhone), MIDI Learn, GPI, previsão em tempo real, histogramas, Loudness Radar. Quem… | „ao vivo“ = Live-Auftritt; Prognose läuft in Echtzeit |
| 71 | …a da fala com Silero VAD, previsão ao vivo, PPM, goniómetro, histogramas, MID… | …a da fala com Silero VAD, previsão em tempo real, PPM, goniómetro, histogramas, MID… | „ao vivo“ = Live-Auftritt; Prognose läuft in Echtzeit |
| 147 | …icheiro de áudio na app Ficheiros, apare o áudio até ao trecho desejado, n… | …icheiro de áudio na app Ficheiros, encurte o áudio até ao trecho desejado, n… | trim = „encurtar“ wie Apple pt-PT |
| 149 | …ta, sem plug-ins, sem MIDI: apenas aparar, cortar, normalizar para R128 e … | …ta, sem plug-ins, sem MIDI: apenas encurtar, cortar, normalizar para R128 e … | trim = „encurtar“ wie Apple pt-PT |
| 161 | …um pad no pegelWERK instant PLAYER envie para o easy EDITOR apare, normalize SEND BACK coloca o resultado no me… | …um pad no pegelWERK instant PLAYER → envie para o easy EDITOR → encurte, normalize → SEND BACK coloca o resultado no me… | trim = „encurtar“ wie Apple pt-PT; Pfeile der Kette ergänzt (wie IT) |
| 180 | … EDITOR é para quando quer cortar, aparar e normalizar rapidamente para o … | … EDITOR é para quando quer cortar, encurtar e normalizar rapidamente para o … | trim = „encurtar“ wie Apple pt-PT |
| 181 | pegelWERK easy EDITOR - aparar áudio e levá-lo a EBU R128 -23 L… | pegelWERK easy EDITOR - encurtar áudio e levá-lo a EBU R128 -23 L… | trim = „encurtar“ wie Apple pt-PT |
| 182 | …ra iPhone e iPad: abra o ficheiro, apare, normalize para EBU R128 -23 LUFS… | …ra iPhone e iPad: abra o ficheiro, encurte, normalize para EBU R128 -23 LUFS… | trim = „encurtar“ wie Apple pt-PT |
| 183 | …iPad. Abra áudio na app Ficheiros, apare, normalize para EBU R128 -23 LUFS… | …iPad. Abra áudio na app Ficheiros, encurte, normalize para EBU R128 -23 LUFS… | trim = „encurtar“ wie Apple pt-PT |
| 251 | …a o pegelWERK easy EDITOR. Aí pode aparar ou normalizar para R128, e com S… | …a o pegelWERK easy EDITOR. Aí pode encurtar ou normalizar para R128, e com S… | trim = „encurtar“ wie Apple pt-PT |
| 270 | …ser, envie para o easy EDITOR para aparar. | …ser, envie para o easy EDITOR para encurtar. | trim = „encurtar“ wie Apple pt-PT |
| 343 | …e correção offline, não um medidor ao vivo. Mede o ficheiro inteiro, planeia … | …e correção offline, não um medidor em tempo real. Mede o ficheiro inteiro, planeia … | Messung in Echtzeit, nicht Auftritt |
| 372 | …m novo ficheiro com ganho estático correção multibanda de LRA opcional limitador TP. | …m novo ficheiro com ganho estático → correção multibanda de LRA opcional → limitador TP. | Pfeile der Kette ergänzt (wie IT) |
| 522 | … como em qualquer DAW. O que corre ao vivo soa idêntico na exportação. macOS. | … como em qualquer DAW. O que corre em tempo real soa idêntico na exportação. macOS. | Verarbeitung in Echtzeit, nicht Auftritt |

### Ton (Ganz-Lesen index, voyzsession, mac)

| Nr | vorher | nachher | Grund |
|---|---|---|---|
| 194 | …ara 2 computadores. Pagamento único. Pagamento seguro via Paddle. | …ara 2 computadores. Pagamento único e seguro via Paddle. | Doppelung „Pagamento … Pagamento“ zusammengezogen |
| 489 | …oudness de emissão, e a exportação sai como WAV, MXF ou diretamente com o víde… | …oudness de emissão, e a exportação é feita em WAV, MXF ou diretamente com o víde… | „sai como“ wörtlich aus „geht raus als“ |
| 511 | …, ATSC A/85, ARIB TR-B32 ou OP-59. Além de perfis para podcast, YouTube e aud… | …, ATSC A/85, ARIB TR-B32 ou OP-59. Há ainda perfis para podcast, YouTube e aud… | Satzfragment „Além de …“ (aus „Dazu …“) |
| 512 | …el de forma contínua com o fader. Além do acabamento automático: EQ, compre… | …el de forma contínua com o fader. A isto junta-se o acabamento automático: EQ, compre… | Satzfragment „Além do …“ (aus „Dazu …“) |
| 524 | …e gravado e contagem decrescente - e sabe onde entrar. O retorno de cue e o talkb… | …e gravado e contagem decrescente - para que saiba quando entrar. O retorno de cue e o talkb… | Zweck fehlte („damit er weiß, wann“) |

## Auch für die App

Begriffe, bei denen Website und App jetzt voneinander abweichen oder die App selbst uneinheitlich ist.
Nichts davon ist im App-Repo geändert.

| Sprache | Website | App heute | Vorschlag |
|---|---|---|---|
| ES | „plug-in(s)“ (mit Bindestrich, wie Cubase ES) | „plugin(s)“ („Añadir plugin“) | Eine Schreibung für beide festlegen. Beides ist im span. Audiobereich verbreitet; die Website folgt Cubase ES. Kippt die App nicht, wäre die Website mit einem Suchen/Ersetzen anzugleichen. |
| IT | „plug-in“ (wie Microsoft IT) | „plugin“ („Aggiungi plugin“) | wie ES |
| PT | „plug-in(s)“ (wie Microsoft pt) | „plugin(s)“ | wie ES |
| PT | „encurtar“ für Trim (Apple pt-PT „Encurtar clips“) | kein Trim-Begriff in der App gefunden | Falls die App „aparar“ einführt: „encurtar“ nehmen. |
| PT | „consola de hardware“ (App-README) | Tabelle: „consola“; App-Hilfe `help_pt`: „superfície de controlo“ (laut Gegenleser) | Uneinheitlichkeit liegt in der App, nicht auf der Website. |
| PT | „timeline“ (wie die App-Oberfläche) | „Timeline“ | Apple iMovie pt-PT sagt „cronograma“. Nur ändern, wenn die App wechselt. |
| FR | „release“, „lookahead“, „soft knee“, „pre-roll“ (ohne Akzent) | „release“, „lookahead“, „Pre-roll“ | jetzt gleich; keine Aktion. Vorher stand auf der Website „relâchement“, „anticipation“, „genou doux“, „pré-roll“. |
| IT | „marker“ | „marker“ | jetzt gleich (vorher Website „marcatore“). |

## Restrisiko (was ohne Muttersprachler offen bleibt)

Fehler im Sinn von falschem Begriff, falscher Grammatik oder falscher Rechtsbezeichnung sind an den 61 Stellen
nach bestem verfügbarem Beleg ausgeräumt. Offen bleibt der **Ton**, und das lässt sich ohne Muttersprachler nicht
messen, nur abschätzen:

* **Werbesprache wirkt übersetzt, wo der deutsche Satzbau durchscheint.** Typisch sind die kurzen Reihungen der
  Vorlage („Video laden, sprechen, fertig“, „Ein Klick, sendefertig“) und Überschriften im Telegrammstil
  („In 4 Schritten zum …“). Korrigiert habe ich nur, wo eine Wendung erkennbar wörtlich war („l’export part en“,
  „la exportación sale como“, „Pagamento único. Pagamento seguro“). Der Rhythmus der Vorlage ist sonst
  beibehalten; ein Muttersprachler würde vermutlich mehr umstellen.
* **Anglizismen-Dichte** ist eine Geschmacksfrage der Zielgruppe. Ich habe mich für die Form entschieden, die in
  Apple-Handbüchern und in der App steht (z. B. FR „release“, „lookahead“). Ein französischer Toningenieur liest
  das selbstverständlich; ein Lektor aus dem Verlagswesen würde es übersetzen wollen.
* **Gefolgert, ohne Beleg** (bewusst vorsichtig gewählt): FR „une DAW amputée“ (Nr 480), IT „kit da assemblare“ /
  „editor da assemblare“ (Nr 452/479/547/548), PT „Camas musicais“ (Nr 260), alle Ton-Korrekturen.
* **Nur einmal geprüft:** Apple-FR-Seiten in der `fr-afri`-Ausgabe; die italienische Logic-Seite zeigte englische
  Überschriften („Markers overview“) – ob das echte Lokalisierung oder ein englischer Rückfall ist, lässt sich
  von außen nicht unterscheiden. Die App IT sagt aber ebenfalls „marker“, die Entscheidung hängt nicht daran allein.
* **pt-PT gegen pt-BR:** Die Seiten sind europäisch formuliert. Brasilianische Leser verstehen sie, empfinden aber
  „ecrã“, „ficheiro“, „guardar“ als fremd. Das ist die gewollte Folge der Entscheidung „eine Fassung, pt-PT“.
* **Rechtsbezeichnungen:** selbst nachgeschlagen sind PT „Direito de livre resolução“ (DL 24/2014) und IT
  „Condizioni generali“ (Art. 1341 c.c.). FR „Rétractation“, ES „Desistimiento“, IT „Diritto di recesso“ waren nicht
  UNSICHER und entsprechen den Gesetzesbegriffen, die der Auftrag nennt; eigens nachgeschlagen habe ich sie nicht.
  Ob der übersetzte Rechtstext inhaltlich trägt, ist eine Rechtsfrage, keine Sprachfrage, und hier nicht geprüft.

## Außerhalb dieser Runde (gehört in die DE-Quelle, Betreiber entscheidet)

* Herstellernamen in der Kompatibilitätsliste (Mackie MCU, Elgato Stream Deck, MakePro X; Nr 508/540): in allen
  Sprachen beibehalten wie im Deutschen. Neutralisieren wäre eine Inhaltsänderung der Quelle.
* Support nur auf Deutsch und Englisch (FR Nr 405): korrekt übersetzt; ein Zusatz „Anfragen gern auf Englisch“
  wäre neuer Inhalt.
* Fehlende Pfeile in der DE-Quelle (Nr 161/372): IT hatte sie schon, FR und PT jetzt auch; ES formuliert die Kette
  mit Kommas und braucht sie nicht. Die DE-Quelle repariert die Übersetzungs-Sitzung.
* Englische Überschriften auf `/fr/voyzsession.html` u. a. („Updates“, „Support“, „Plugins“, „Script-Editor“,
  „One session, two ways to work“): kommen ohne `data-i18n` aus der DE-Quelle und sind deshalb in keiner Sprache
  übersetzbar. Schon im Prüfbericht des Gegenlesers genannt; eine Strukturänderung, also nicht in dieser Runde.
