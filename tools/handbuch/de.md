## 1 Einführung

voyzSESSION PRO ist eine Aufnahme- und Mischsoftware (DAW) für Sprachproduktionen: Voice-over und Off-Kommentar zum Bild, Synchron, Radiobeiträge, Podcasts und Hörbücher.

Bei Produktionen zum Bild laden Sie ein Video, nehmen den Text synchron dazu auf und exportieren die fertige Mischung als Audiodatei oder direkt im Video bzw. im MXF. Reine Audioproduktionen wie Podcast, Hörbuch oder Radiobeitrag kommen ohne Video aus. Dafür gibt es die Seite **AUDIO** mit dem Script Editor, Lautheitsprofile für Radio, Podcast und Hörbuch sowie Exportformate wie MP2, MP3, FLAC und Opus.

### 1.1 Assist-Modus und Manual-Modus

|                   | Assist-Modus                                               | Manual-Modus                                        |
|-------------------|------------------------------------------------------------|-----------------------------------------------------|
| Gedacht für       | Sprecher, Redakteure und Cutter ohne Tontechnik-Kenntnisse | Tonmeister und Toningenieure                        |
| Wer mischt        | Die Automatik (AUTO MIX)                                   | Sie selbst, wie in Pro Tools oder Logic             |
| Typischer Einsatz | Aufnahme und schnelle Lieferung                            | Schnitt und Feinmischung                            |
| Ergebnis          | Mischung nach der gewählten Lautheitsnorm per Knopfdruck   | Volle Kontrolle über Regler, Plugins und Automation |

Was der AUTO MIX im Assist-Modus berechnet, übernimmt der Manual-Modus als Ausgangspunkt. Aufnehmen können Sie in beiden Modi.

### 1.2 Systemvoraussetzungen

|                 | Empfohlen                                        | Mindestens                                    |
|-----------------|--------------------------------------------------|-----------------------------------------------|
| Mac             | Apple-Prozessor (M1 oder neuer)                  | Intel-Mac (lauffähig, aber nicht empfohlen)   |
| Betriebssystem  | macOS 14 Sonoma oder neuer                       | macOS 14 Sonoma                               |
| Arbeitsspeicher | 32 GB bei Projekten über 30 Minuten mit 4K-Video | 16 GB                                         |
| Speicherplatz   | SSD                                              | 5 GB frei, dazu Platz für das Projektmaterial |
| Audio           | Audio-Interface mit Mikrofon und Kopfhörer       | Eingebautes Mikrofon oder USB-Mikrofon        |

Auf Intel-Macs und bei weniger als 16 GB Arbeitsspeicher zeigt die App beim ersten Start einmalig einen Hinweis zur Hardware. Der Audiotreiber für die Fernvertonung braucht macOS 13, die virtuelle Kamera macOS 12.3. Beides ist mit macOS 14 erfüllt.

### 1.3 Installation

1.  Laden Sie `voyzsession-2.0.dmg` von pegelwerk.com herunter.
2.  Öffnen Sie die DMG und ziehen Sie voyzSESSION PRO in den Ordner Programme. Die virtuelle Kamera funktioniert nur, wenn die App dort liegt.
3.  Starten Sie die App. macOS fragt nach dem Zugriff auf das Mikrofon. Erlauben Sie ihn, sonst ist keine Aufnahme möglich.
4.  Beim ersten Öffnen des Prompters fragt macOS nach der Spracherkennung. Erlauben Sie auch diese, damit der Text Ihrer Stimme folgen kann.

Neue Versionen meldet die App mit dem Schild UPDATE in der Kopfleiste.

### 1.4 Lizenz und Testphase

Beim ersten Start öffnet sich das Fenster „voyzSESSION PRO - Lizenz“. Sie können die App 7 Tage lang testen. Ein Schild in der Kopfleiste zeigt die verbleibenden Tage.

So aktivieren Sie die Lizenz:

1.  Fügen Sie den Lizenzschlüssel aus Ihrer E-Mail in das Feld ein oder ziehen Sie die Datei `license.lic` auf das Fenster. Sie können auch auf den Aktivierungslink in der E-Mail klicken.
2.  Klicken Sie auf **Aktivieren**.

**Lizenz kaufen** führt zum Shop. Bei einem Abo heißt der Knopf **Abo verwalten**. Über das Lizenzschild in der Kopfleiste öffnen Sie das Fenster jederzeit wieder.

Nach Ablauf der Testphase läuft die App eingeschränkt weiter und gibt jede Minute einen kurzen Erinnerungston aus. Ist ein Abo abgelaufen, ist der Export gesperrt.

## 2 Die Oberfläche

Das Hauptfenster besteht aus drei festen Bereichen: oben die Kopfleiste, in der Mitte die Arbeitsseite (**VIDEO**, **AUDIO** oder **EDIT**) und unten die Transportleiste mit den Knöpfen für Wiedergabe und Aufnahme. Zwischen Arbeitsseite und Transportleiste kann die Navigationszeile eingeblendet werden.

### 2.1 Kopfleiste

Die Elemente von links nach rechts:

| Element                   | Funktion                                                                                                                           |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| DATEI                     | Neues Projekt, Öffnen, Zuletzt verwendet, Speichern, Speichern unter, Vorlagen ([Kapitel 15](#k15))                                |
| PROJEKT...                | Projekteinstellungen: Abtastrate, Bildrate, Startzeitcode, Profil                                                                  |
| VIDEO, AUDIO, EDIT, MIXER | Wechsel der Arbeitsseite ([Abschnitt 2.2](#k2-2))                                                                                  |
| MEDIA                     | Medienablage ein- und ausblenden                                                                                                   |
| VIDEO LADEN               | Video öffnen. Ist ein Video geladen, erscheint daneben ein x zum Entfernen. Das Entfernen lässt sich rückgängig machen.            |
| BILD                      | Videofenster ein oder aus (Cmd+9). Per Rechtsklick legen Sie das Bild auf einen externen Bildschirm oder blenden den Timecode ein. |
| LEVEL                     | Pegel-Check für das Mikrofon                                                                                                       |
| A/V...                    | Audio- und Videoeinstellungen (Interface, Ein- und Ausgang)                                                                        |
| HILFE                     | Eingebaute Hilfe ein- und ausblenden, schließen mit Esc                                                                            |

Während der Testphase zeigt ein Schild mit der Aufschrift TRIAL die verbleibenden Tage. Gibt es eine neue Version, erscheint ein Schild UPDATE, das zur Downloadseite führt.

### 2.2 Arbeitsseiten

| Seite | Zweck                                      | Inhalt                                                                                          |
|-------|--------------------------------------------|-------------------------------------------------------------------------------------------------|
| VIDEO | Aufnahme zum Bild                          | Video und Prompter mit dem Sprechtext                                                           |
| AUDIO | Reine Audioprojekte, zum Beispiel Podcasts | Script Editor mit dem Transkript der Aufnahmen                                                  |
| EDIT  | Schnitt und Arrangement                    | Mehrspur-Zeitleiste                                                                             |
| MIXER | Mischen                                    | Das Mischpult wird über die aktuelle Seite gelegt. Ein Klick auf eine andere Seite schließt es. |

### 2.3 Transportleiste

- **Links:** Rückgängig und Wiederholen, ein Wippschalter für den Zoom der Zeitachse und einer für die Spurhöhe.
- **Mitte:** \|\<\< (zum Anfang), Zurückspulen, **PLAY/STOP**, **REC**, **LOOP**, Vorspulen, \>\>\| (zum Ende). Ein kurzer Druck auf eine Spultaste springt 1 Sekunde, gedrückt halten spult mit zunehmender Geschwindigkeit bis zum 32-fachen Tempo.
- **Positionszähler:** zeigt die aktuelle Position, rot bei Aufnahme, grün bei Wiedergabe. Nach einem Klick können Sie eine Zeit eingeben. Per Rechtsklick wählen Sie die Anzeige in Timecode, Minuten:Sekunden oder Samples.
- **Aufnahmegruppe:** **V-PUNCH** (Punch per Spracherkennung), **PRE** (Vorlauf vor der Aufnahme, 0 bis 10 Sekunden) und **POST** (Nachlauf nach dem Punch-Out).
- **Rechts:** der Umschalter **ASSIST \| MANUAL**, der Knopf **AUTO MIX** (nur im Assist-Modus) und **EXPORT**.

Unter den Knöpfen liegt eine Hinweiszeile, in der die App den aktuellen Vorgang meldet, etwa „Mix wird erzeugt...“. Erfolgsmeldungen erscheinen in Grün. Leuchtet **AUTO MIX** blau, passt die gespeicherte Mischung nicht mehr zum Projekt und sollte neu berechnet werden.

### 2.4 Navigationszeile

Die Navigationszeile blenden Sie über Fenster \> Navigationszeile ein und aus. Sie zeigt das ganze Projekt als Wellenform. Ein Klick springt an die gewählte Stelle. Auf der Seite **EDIT** markiert ein Rahmen den sichtbaren Ausschnitt, den Sie mit der Maus verschieben können.

Links geben Sie **START**, **ENDE** und **LÄNGE** des Bereichs ein. Rechts liegen die Knöpfe für Marken: **MK +** setzt eine Marke, die Knöpfe **MK** mit Pfeil springen zur vorigen oder nächsten Marke, **MARKER** zeigt eine Liste aller Marken. Ein Projekt kann bis zu 999 Marken enthalten.

### 2.5 Menüleiste

| Menü            | Eintrag                                                                                            | Tastenkombination |
|-----------------|----------------------------------------------------------------------------------------------------|-------------------|
| voyzSESSION PRO | Über voyzSESSION PRO..., Stream Deck: Plugin installieren..., Stream Deck: Belegung laden, Beenden | Cmd+Q             |
| Einstellungen   | Allgemein...                                                                                       | Cmd+,             |
| Einstellungen   | Audio/Video...                                                                                     |                   |
| Einstellungen   | Crossfade bei Überlappung (ein/aus)                                                                |                   |
| Fenster         | Kabinenfenster                                                                                     | Cmd+Shift+B       |
| Fenster         | Kapitel                                                                                            | Cmd+Shift+K       |
| Fenster         | Videofenster                                                                                       | Cmd+9             |
| Fenster         | Navigationszeile (ein/aus)                                                                         |                   |

Ein Menü „Datei“ gibt es in der Menüleiste nicht. Die zugehörigen Befehle liegen im Knopf **DATEI** in der Kopfleiste.

## 3 Erste Schritte

Dieses Kapitel führt vom leeren Projekt bis zur ersten Aufnahme.

### 3.1 Projekt anlegen und speichern

1.  Wählen Sie **DATEI** \> **Neues leeres Projekt**. Ein neues Projekt enthält bereits eine Sprecherspur.
2.  Speichern Sie das Projekt sofort mit **DATEI** \> **Speichern...** (Cmd+S), am besten auf einer SSD mit ausreichend Platz.

Die App schreibt Aufnahmen direkt in den Projektordner. Bei einem noch nicht gespeicherten Projekt erscheint beim ersten Druck auf **REC** die Meldung „Aufnahme braucht einen Projektordner“.

Wenn Sie häufig mit derselben Spuraufteilung arbeiten, legen Sie neue Projekte über **DATEI** \> **Neu aus Vorlage** an ([Kapitel 15](#k15)).

### 3.2 Audiogerät einrichten

1.  Klicken Sie in der Kopfleiste auf **A/V...**.
2.  Wählen Sie unter **OUTPUT** Ihren Kopfhörerausgang bzw. Ihr Interface und unter **INPUT** Ihr Mikrofon.
3.  Wenn Sie sich direkt über das Interface abhören (Direct Monitor am Gerät), lassen Sie **Direct hardware monitoring** eingeschaltet. Ohne diese Möglichkeit schalten Sie die Option aus. Dann hören Sie sich über die Software.

Nehmen Sie immer mit Kopfhörer auf. Bei Wiedergabe über Lautsprecher gelangt der Ton des Videos in das Mikrofon.

### 3.3 Mikrofon einpegeln (Pegel-Check)

Kurz nach dem Start erscheint der Pegel-Check. Sie können ihn jederzeit über **LEVEL** in der Kopfleiste öffnen.

1.  Wählen Sie oben das Mikrofon.
2.  Sprechen Sie einige Sätze in der Lautstärke, in der Sie später aufnehmen.
3.  Stellen Sie die Vorverstärkung (Gain) am Interface so ein, dass die Anzeige „Optimaler Pegel“ meldet.

| Anzeige         | Spitzenpegel    | Maßnahme                                          |
|-----------------|-----------------|---------------------------------------------------|
| Kein Signal     | unter -50 dBFS  | Kabel, Mikrofonauswahl und Phantomspeisung prüfen |
| Zu leise        | unter -18 dBFS  | Gain am Interface erhöhen                         |
| Optimaler Pegel | -18 bis -3 dBFS | Einstellung beibehalten                           |
| Zu laut         | über -3 dBFS    | Gain verringern, sonst verzerrt die Aufnahme      |

Im selben Fenster wählen Sie das Format-Profil, also die Norm, für die Sie liefern, zum Beispiel EBU/ARD-ZDF oder Podcast. Mit „Beim nächsten Start nicht mehr zeigen“ schalten Sie den automatischen Pegel-Check ab.

### 3.4 Video laden

1.  Klicken Sie auf **VIDEO LADEN** oder ziehen Sie die Datei in das Fenster.
2.  Unterstützt werden MP4, MOV, M4V und MXF. WebM wird nicht unterstützt.
3.  Bei MXF erstellt die App zunächst eine Abspielkopie (Proxy). Ein Fortschrittsbalken zeigt den Vorgang an. Beim nächsten Öffnen wird die Kopie wiederverwendet.

Hat das Video mehr als zwei Tonspuren, was bei MXF häufig vorkommt, erscheint das Fenster „Welche Tonspuren sollen ins Projekt?“:

- Setzen Sie bei jeder benötigten Spur einen Haken. In der Grundeinstellung ist keine Spur ausgewählt.
- Mit der Klammer neben einem Paar (1+2, 3+4 usw.) legen Sie zwei Monospuren als eine Stereospur an.
- **Wählen Sie für jede Zeile die Rolle:** Auto, IT-Vormischung, Sprecher, O-Ton, Musik, Atmo, Stadion oder Effekte. Die Rolle steuert später den AUTO MIX ([Kapitel 7](#k7)).
- **Importieren** übernimmt die Auswahl. Wenn Sie das Fenster stattdessen schließen, wird der gesamte Import abgebrochen.

Videos mit einer oder zwei Tonspuren werden ohne Rückfrage mit der Rolle Auto übernommen.

### 3.5 Erste Aufnahme

1.  Klicken Sie im Spurkopf der Sprecherspur auf **R**, um die Spur scharf zu schalten. Die Taste leuchtet rot.
2.  Drücken Sie **REC** oder die Taste R. Nach dem Vorlauf (**PRE**, Grundeinstellung 4 Sekunden) beginnt die Aufnahme.
3.  Beenden Sie die Aufnahme mit **STOP REC** oder erneut mit der Taste R.
4.  Mit der Leertaste spielen Sie die Aufnahme ab.

[Kapitel 4](#k4) beschreibt die Aufnahme ausführlich, [Kapitel 7](#k7) die automatische Mischung und [Kapitel 12](#k12) den Export.

## 4 Aufnehmen

Aufgenommen wird auf jede Spur, die scharf geschaltet ist. Es können mehrere Spuren gleichzeitig scharf geschaltet sein, und jede davon ist hörbar, wie in anderen DAWs auch.

### 4.1 Spurkopf

| Taste   | Name                         | Funktion                                                                                                                                  |
|---------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| R       | Scharf schalten              | REC nimmt auf dieser Spur auf. Alt+Klick wirkt auf alle Spuren.                                                                           |
| I       | Eingang abhören (INPUT ONLY) | Ein: Der Eingang ist auch bei der Wiedergabe hörbar. Aus (Auto Input): Der Eingang ist nur im Stillstand und während der Aufnahme hörbar. |
| M       | Stumm                        | Spur stummschalten                                                                                                                        |
| S       | Solo                         | Nur diese Spur hören                                                                                                                      |
| AC      | AutoCut                      | Schneidet die nächste Aufnahme automatisch an den Pausen                                                                                  |
| IMPORT  | Import                       | Audiodatei auf diese Spur holen                                                                                                           |
| Eingang | Eingangswahl                 | Eingang des Interfaces, der auf die Spur geht                                                                                             |

Die Taste I erscheint nur auf Sprecherspuren und nur dann, wenn das Hardware-Monitoring ausgeschaltet ist.

Mit **+ Voice** legen Sie eine neue Sprecherspur (mono) an, mit **+ Audio** eine Zuspielspur (stereo) für Musik, Atmo und Ähnliches.

Per Rechtsklick auf den Spurkopf oder über das Zahnrad erreichen Sie weitere Befehle: Umbenennen, Nach oben/unten verschieben, Referenzstimme, Stereo zusammenlegen oder trennen, Ansicht und Spur löschen. Spuren lassen sich auch durch Ziehen am Spurkopf verschieben. Mit Cmd- oder Shift-Klick wählen Sie mehrere Spuren aus. Die letzte Sprecherspur kann nicht gelöscht werden. Die Farbe einer Spur ändern Sie im Mixer per Doppelklick auf den Spurnamen.

### 4.2 Vorlauf und Nachlauf

- **PRE** (Pre-Roll) bestimmt, wie lange das Video vor dem Aufnahmepunkt anläuft. Einstellbar sind 0 bis 10 Sekunden, die Grundeinstellung ist 4 Sekunden. Per Doppelklick auf die Zahl geben Sie einen Wert ein.
- **POST** (Post-Roll) bestimmt, wie lange die Wiedergabe nach dem Ende einer Bereichsaufnahme weiterläuft.
- Während des Vorlaufs zählt der Knopf herunter (zum Beispiel „**PRE** 3.2s“), danach zeigt er **STOP REC**. Ein erneuter Druck bricht die Aufnahme ab.
- Wird über einen vorhandenen Take aufgenommen, ersetzt die neue Aufnahme den überlappten Teil. Was davor und dahinter liegt, bleibt erhalten.

### 4.3 Bereich, Loop und Punch

Oben im Lineal liegt eine Leiste für einen Bereich. Dieser Bereich gilt sowohl für den Loop als auch für die Aufnahme im Bereich.

- **Bereich anlegen:** In der leeren Leiste ziehen. Ziehen an einer Kante ändert die Länge, Ziehen in der Mitte verschiebt den Bereich, ein Doppelklick löscht ihn. Start, Ende und Länge lassen sich auch in der Navigationszeile eingeben.
- **LOOP** oder die Taste L wiederholt den Bereich. Ist kein Bereich gesetzt, verwendet die App den sichtbaren Ausschnitt.
- **Aufnahme nur im Bereich (Punch):** Ein Rechtsklick auf **REC** schaltet zwischen „Aufnahme bis STOP“ und „Aufnahme im Bereich“ um. Im zweiten Fall wird der Bereich orange dargestellt, und die Aufnahme beginnt und endet genau an seinen Kanten.

### 4.4 Voice Punch

Mit **V-PUNCH** setzen Sie nach einem Versprecher den Einstiegspunkt per Sprache:

1.  Drücken Sie **V-PUNCH**.
2.  Sprechen Sie die letzten fehlerfreien Worte vor dem Versprecher.
3.  Die App sucht diese Stelle, setzt den Einstieg in die Pause danach, spielt den Vorlauf ab und startet die Aufnahme. Ab dort sprechen Sie neu.

Mit Shift+Klick auf **V-PUNCH** sprechen Sie zusätzlich die ersten Worte nach dem Fehler. Dann wird nur der fehlerhafte Teil ersetzt, und das Original läuft danach weiter.

Voraussetzungen: Das Projekt ist gespeichert, die Seite **VIDEO** ist geöffnet, der Transport steht, eine Sprecherspur ist scharf geschaltet, die Spracherkennung von macOS ist erlaubt und der Take ist bereits transkribiert.

### 4.5 Marken

| Bedienung                    | Funktion                                     |
|------------------------------|----------------------------------------------|
| Alt+M oder MK +              | Marke an der Abspielposition setzen          |
| 1 bis 9                      | Marke auf Platz 1 bis 9 setzen               |
| Shift+1 bis 9                | Zu Marke 1 bis 9 springen                    |
| Alt+Komma, Alt+Punkt         | Zur vorigen bzw. nächsten Marke              |
| Fähnchen ziehen              | Marke verschieben                            |
| Klick auf die Beschriftung   | Marke benennen                               |
| Doppelklick auf das Fähnchen | Marke löschen (lässt sich rückgängig machen) |

## 5 Prompter, Script Editor und Kabinenfenster

Der Prompter zeigt während der Aufnahme den Sprechtext an und folgt der Stimme. Der Script Editor zeigt das Gesprochene als Text an. Dort können Sie Audio schneiden, indem Sie Wörter markieren und löschen.

### 5.1 Prompter (Seite VIDEO)

Mit **SKRIPT LADEN** öffnen Sie eine Textdatei im Format .txt, .rtf oder .pdf (PDF nur mit Textebene). Sie können die Datei auch in das Fenster ziehen oder den Text mit Cmd+V einfügen.

Während Sie sprechen, hört die Spracherkennung von macOS mit und führt die aktuelle Zeile nach. Wenn Sie mit dem Mausrad scrollen, setzt das Mitlaufen für 8 Sekunden aus. Kann der Prompter der Stimme nicht folgen, etwa weil die Diktierfunktion fehlt, zeigt er einen Hinweis an.

| Bedienung                             | Funktion                                                                                                |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|
| LANG                                  | Sprache der Spracherkennung, unabhängig von der Sprache der App                                         |
| EDIT / DONE                           | Text direkt bearbeiten. Die Spracherkennung pausiert so lange.                                          |
| A- / A+, Cmd+Minus / Cmd+Plus / Cmd+0 | Schriftgröße                                                                                            |
| Pfeiltasten                           | Ein Wort vor oder zurück                                                                                |
| Bild auf, Bild ab                     | 20 Wörter vor oder zurück                                                                               |
| Pos1                                  | Zum Textanfang                                                                                          |
| Klick auf ein Wort                    | Das Wort wird zur aktuellen Zeile. Ist der Text an eine Aufnahme gebunden, springt auch die Zeitleiste. |
| FROM TAKE                             | Erzeugt aus dem Transkript einer Aufnahme einen Prompter-Text                                           |

### 5.2 Script Editor (Seite AUDIO)

Der Script Editor zeigt das Transkript aller Sprecherspuren, jede Spur in ihrer Farbe. Die Transkription läuft auf dem Mac selbst und startet automatisch nach einer Aufnahme, einem Import oder dem Laden eines Projekts. Zuspielspuren werden nicht transkribiert.

- **Transkribieren** erscheint, solange noch kein Text vorhanden ist. Fehlt der Text nur bei einzelnen Takes, heißt der Knopf **Fehlende transkribieren**.
- Ein Klick auf ein Wort setzt den Abspielkopf in die Pause davor.
- **Audio schneiden:** Wörter durch Ziehen markieren und Entf drücken. Die App schneidet das Audio heraus, legt die Schnitte in die nächsten Pausen und schließt die Lücke. Der Vorgang lässt sich in einem Schritt rückgängig machen.
- **Wort korrigieren:** Doppelklick auf das Wort, Text ändern, Return drücken. Dabei ändert sich nur der Text, nicht das Audio.
- **Füller entfernen** sucht Füllwörter wie „äh“, **Textsuche** findet Stellen im Transkript.
- **TEXT EXPORT** speichert das Transkript oder Untertitel (SRT, VTT, TXT, JSON).

Die Wortzeiten eignen sich zur Orientierung. Für sehr genaue Schnitte sollten Sie das Ergebnis abhören.

### 5.3 Kabinenfenster

Das Kabinenfenster (Fenster \> Kabinenfenster, Cmd+Shift+B) ist für einen Monitor in der Sprecherkabine gedacht, der per HDMI angeschlossen ist. Es zeigt links den Prompter und rechts das Bild mit Timecode. Während der Aufnahme erscheint ein roter Rahmen, im Vorlauf wird der Timecode rot. Der Prompter im Kabinenfenster läuft synchron zum Prompter im Hauptfenster. Ist ein zweiter Bildschirm angeschlossen, öffnet sich das Fenster dort im Vollbild.

## 6 Bearbeiten in der Zeitleiste

Die Seite **EDIT** zeigt alle Spuren in einer Zeitleiste. Hier schneiden, verschieben und blenden Sie die Takes.

### 6.1 Takes bearbeiten

Die obere und die untere Hälfte eines Takes reagieren unterschiedlich:

| Bereich                  | Ziehen bewirkt                          |
|--------------------------|-----------------------------------------|
| Untere Hälfte            | Take verschieben                        |
| Obere Hälfte             | Gelben Auswahlbereich im Take markieren |
| Linke oder rechte Kante  | Take kürzen oder verlängern (Trimmen)   |
| Blendengriff an der Ecke | Ein- oder Ausblendung einstellen        |

- Cmd+Klick fügt Takes zur Auswahl hinzu, Cmd+A wählt alle Takes.
- Mit gedrückter Control- oder Shift-Taste wechselt ein gezogener Take nur die Spur, die Zeitposition bleibt unverändert. Im Lineal erscheint dabei „ZEIT GESPERRT“.
- Mit gedrückter Alt-Taste wird beim Ziehen nicht eingerastet.
- Cmd+Pfeil nach oben oder unten verschiebt den Take auf die Nachbarspur, mit Shift entsteht eine Kopie.
- Pfeil links oder rechts verschiebt die Auswahl um ein Bild, mit Shift um eine Sekunde.

### 6.2 Schneiden, Löschen, Kopieren

| Befehl                                                    | Tastenkombination   |
|-----------------------------------------------------------|---------------------|
| Am Abspielkopf teilen oder Auswahlbereich herausschneiden | Cmd+E               |
| Löschen                                                   | Entf oder Rücktaste |
| Kopieren, am Abspielkopf einfügen                         | Cmd+C, Cmd+V        |
| Duplizieren                                               | Cmd+D               |
| Take stummschalten                                        | M                   |
| AutoCut (Stille herausschneiden)                          | S                   |
| Rückgängig, Wiederholen                                   | Cmd+Z, Cmd+Shift+Z  |

Geteilte Stücke erhalten fortlaufende Namen, zum Beispiel „Take 3-01“ und „Take 3-02“. Der Rechtsklick auf einen Take bietet unter anderem: Rename..., Replace audio..., Auswahl entfernen, Nur Auswahl behalten, Dehnen scharfschalten (danach an der Kante ziehen, um den Take zeitlich zu dehnen), Fade/Crossfade und Clip-Gain-Korrektur zurücksetzen. Ein Rechtsklick auf eine leere Stelle bietet „Audio hier einfügen...“.

### 6.3 Blenden und Crossfades

- **Taste F:** Markieren Sie am Anfang oder Ende eines Takes einen Bereich und drücken Sie F. Es entsteht eine Blende. Liegt die Markierung über der Grenze zweier Takes, entsteht ein Crossfade.
- **Überlappen:** Wird ein Take über einen anderen gezogen, entsteht über der Überlappung automatisch ein Crossfade. Liegt er vollständig innerhalb eines anderen Takes, erhalten beide Kanten einen Crossfade von 50 ms. Diese Funktion schalten Sie unter Einstellungen \> Crossfade bei Überlappung ab. Der gezogene Take überschreibt dann den darunterliegenden.
- Die Länge eines Crossfades ändern Sie durch Ziehen an den Kanten des Crossfade-Kästchens.

### 6.4 Clip-Gain

Unten links in jedem Take sitzt ein kleiner Regler. Ziehen nach oben oder unten macht den ganzen Take lauter oder leiser, mit Shift in feinen Schritten. Ein Doppelklick setzt die Korrektur zurück.

Auf der Clip-Gain-Linie im Take setzen Sie per Klick Punkte, ziehen sie auf den gewünschten Pegel und löschen sie per Doppelklick. So lassen sich einzelne Wörter lauter oder leiser machen. Die Linie des AUTO MIX und Ihre eigene Korrektur liegen als zwei Ebenen übereinander.

### 6.5 Zoom und Ansicht

| Funktion                | Bedienung                                                                   |
|-------------------------|-----------------------------------------------------------------------------|
| Zeitachse zoomen        | Wippschalter links in der Transportleiste, Cmd+= und Cmd+Minus, Cmd+Mausrad |
| Ganzes Projekt anzeigen | Taste 0                                                                     |
| Auf die Auswahl zoomen  | Taste Z                                                                     |
| Spurhöhe                | Zweiter Wippschalter, Control+Alt+Pfeil nach oben/unten, Alt+Mausrad        |
| Wellenform vergrößern   | Cmd+Alt+Pfeil nach oben/unten, Shift+Alt+Mausrad                            |
| Zum Anfang, zum Ende    | Return, Ende                                                                |
| Spulen                  | Komma, Punkt (je 1 Sekunde)                                                 |

### 6.6 Medienablage

**MEDIA** in der Kopfleiste öffnet die Medienablage (Clipliste). Sie enthält das gesamte Material des Projekts in den Gruppen IMPORTIERT, VIDEOTON, AUFNAHMEN und NICHT VERWENDET.

- **IMPORT** holt Dateien in die Ablage, aber noch nicht auf eine Spur. Mögliche Formate sind WAV, BWF, AIFF, FLAC, OGG, MP3, M4A, AAC und CAF. Importierte Dateien behalten ihren Originalnamen.
- **Vorhören:** Mauszeiger kurz auf einer Zeile ruhen lassen oder die Pfeiltasten benutzen. Die Leertaste startet und stoppt, Esc beendet.
- **Platzieren:** Ein Doppelklick legt die Datei an der Abspielposition auf die ausgewählte Spur. Alternativ ziehen Sie die Datei in die Zeitleiste.
- Regionen stehen eingerückt unter ihrer Datei. Ein Klick zeigt die Region in der Zeitleiste, beim Ziehen wird nur diese Region abgelegt.
- **Per Rechtsklick:** Auf die ausgewählte Spur importieren, Im Finder zeigen, Aus der Clipliste entfernen, Ungenutzte entfernen.

Ohne die Ablage geht es auch so: Spur auswählen und die Taste I drücken. Die gewählte Datei wird an der Abspielposition eingefügt.

## 7 Assist-Modus und AUTO MIX

Im Assist-Modus übernimmt die App die Mischung. **AUTO MIX** (oder Cmd+M) bearbeitet die Stimme, senkt Musik und Atmo unter der Sprache ab und bringt die Mischung auf die Lautheit des gewählten Profils. Nach dem Start ist der Assist-Modus aktiv.

### 7.1 Vorbereitung: Profil und Rollen

Unter **PROJEKT...** \> Format-Profil legen Sie fest, für welche Norm Sie liefern. Das Profil bestimmt die Ziel-Lautheit und die höchste zulässige Spitze (True Peak).

| Gruppe    | Profil                  | Lautheit           | True Peak         |
|-----------|-------------------------|--------------------|-------------------|
| TV/Radio  | EBU/ARD-ZDF             | -23 LUFS           | -1 dBTP           |
| TV/Radio  | ATSC A/85 (USA)         | -24 LUFS           | -2 dBTP           |
| TV/Radio  | ARIB TR-B32 (Japan)     | -24 LUFS           | -1 dBTP           |
| TV/Radio  | OP-59 (Australien)      | -24 LUFS           | -2 dBTP           |
| TV/Radio  | CST-RT-040 (Frankreich) | -23 LUFS           | -3 dBTP           |
| Streaming | Podcast                 | -16 LUFS           | -1 dBTP           |
| Streaming | YouTube                 | -14 LUFS           | -1 dBTP           |
| Weitere   | Doku                    | -23 LUFS           | -1 dBTP           |
| Weitere   | Sport                   | -23 LUFS           | -1 dBTP           |
| Weitere   | Hörbuch                 | -18 LUFS           | -3 dBTP           |
| Weitere   | Studio 0 dB             | kein Lautheitsziel | Spitze auf 0 dBTP |

Jede Spur braucht außerdem eine Rolle. Sie teilt der Automatik mit, was auf der Spur liegt. Die Rolle wählen Sie über die Rollentaste im Spurkopf oder im Mixer.

| Rolle                    | Kürzel | Pegel im Verhältnis zum Sprecher | Bearbeitung durch die Automatik                                                    |
|--------------------------|--------|----------------------------------|------------------------------------------------------------------------------------|
| Sprecher                 | SPKR   | Bezugspegel                      | Stimme wird bearbeitet und im Pegel ausgeglichen                                   |
| O-Ton                    | OT     | gleich laut (0 LU)               | Wird gegen den Sprecher ausgeglichen, eigene Stimmkette                            |
| Musik                    | MUS    | 4 LU leiser                      | Wird unter Sprecher und O-Ton abgesenkt                                            |
| Effekt                   | FX     | 4 LU leiser                      | Wird abgesenkt                                                                     |
| Atmo                     | ATMO   | 16 LU leiser                     | Wird abgesenkt                                                                     |
| Stadion                  | STAD   | 5 LU leiser                      | Pegelsprünge werden ausgeglichen, die Spur wird aber nie abgesenkt                 |
| IT-Vormischung           | PRE    | unverändert                      | Für eine fertige Vormischung aus dem Schnitt, verhält sich wie „Nicht eingeordnet“ |
| Nicht eingeordnet (Auto) | AUTO   | unverändert                      | Keine Bearbeitung                                                                  |

Neue Spuren haben die Rolle Sprecher. Eine Mono-Zuspielspur wird über den Menüpunkt „Sprecher - Spur wird Stimmspur“ zur Sprecherspur.

### 7.2 AUTO MIX starten

1.  Es muss mindestens eine Aufnahme vorhanden sein, und Solo darf nicht aktiv sein.
2.  Drücken Sie **AUTO MIX** rechts in der Transportleiste oder Cmd+M.
3.  Ein Fortschrittsfenster zeigt die einzelnen Schritte: vorbereiten, Stimme aufbereiten, Kompression und Pegel, Klang, Bett und Ducking, Lautheit. Mit **Abbrechen** beenden Sie den Vorgang jederzeit.
4.  Danach spielen Sie mit **PLAY** die fertige Mischung ab.

Vor der Berechnung stellt die App im Assist-Modus alle Fader des Mischpults auf 0 dB. Das lässt sich rückgängig machen. Wurden auf Zuspielspuren bereits eigene Automationspunkte gesetzt, fragt die App: **Neu berechnen**, **Eigene behalten** oder **Abbrechen**.

**AUTO MIX** startet nicht während einer Aufnahme („Nicht während der Aufnahme.“), bei aktivem Solo („**SOLO** ausschalten, bevor der AUTO MIX läuft.“) und im Manual-Modus. Im Manual-Modus normalisiert stattdessen der Export.

### 7.3 Ergebnis des AUTO MIX

Alle Entscheidungen der Automatik lassen sich ansehen und ändern:

- **Clip-Gain-Linie der Stimme:** Die Lautstärke der Sprache wird über eine Linie am Take ausgeglichen, im Bereich von bis zu 9 dB nach oben oder unten. Ihre eigene Korrektur liegt als zweite Ebene darüber.
- **Ducking als Volume-Automation:** Das Absenken von Musik und Atmo unter der Sprache steht als Kurve in der Lautstärke-Automation der jeweiligen Spur.
- **Werte im Kanalzug:** EQ, Kompressor, De-Esser und die anderen Module sind mit den berechneten Werten belegt. Rechtsklick auf eine Taste \> **Ansehen...** zeigt das Modul gesperrt mit diesen Werten.

Leuchtet **AUTO MIX** blau, passt die gespeicherte Mischung nicht mehr zum Projekt, etwa nach einer neuen Aufnahme oder einem Schnitt. Drücken Sie den Knopf dann erneut.

Projekte aus Version 1.6 brauchen einen neuen **AUTO MIX**, weil sich die Signalkette in Version 2.0 geändert hat.

### 7.4 Einstellmöglichkeiten im Assist-Modus

- Die Fader der Spuren lassen sich bewegen. Die Fader der Voice-Gruppe und des Masters sind im Assist-Modus fest eingestellt (Anzeige **FIXED**).
- Die Tasten im Kanalzug schalten Module nur ein und aus. Die Einstellung der Module übernimmt die Automatik.
- Insert-Slots für Plugins sind sichtbar, aber erst im Manual-Modus aktiv.

Wer selbst mischen möchte, wechselt mit **MANUAL** in den Manual-Modus. Die Mischung des AUTO MIX wird dabei vollständig als Ausgangspunkt übernommen ([Kapitel 8](#k8)).

## 8 Manual-Modus: Mixer, Kanalzug, Gruppen, Master

Im Manual-Modus mischen Sie selbst, wie in Pro Tools, Logic oder Nuendo. Die App verändert keine Fader, die Abhöre spielt ohne zusätzliche Bearbeitung, und der Export schreibt genau das in die Datei, was Sie hören.

### 8.1 In den Manual-Modus wechseln

Klicken Sie in der Transportleiste auf **MANUAL**. Der Wechsel funktioniert auch während der Wiedergabe und wird ohne Knacken überblendet.

Üblicher Ablauf: Im Assist-Modus aufnehmen und **AUTO MIX** ausführen, danach in den Manual-Modus wechseln. Kanalzug, Module, Pegellinien und Ducking werden so übernommen, wie sie zuletzt geklungen haben. Anschließend korrigieren Sie die Stellen, die Sie anders haben möchten.

| Funktion                      | Assist                     | Manual                                          |
|-------------------------------|----------------------------|-------------------------------------------------|
| Knopf AUTO MIX                | sichtbar                   | ausgeblendet                                    |
| Tasten im Kanalzug            | nur ein/aus                | ein/aus, öffnet das Modul zur Bearbeitung       |
| Insert-Slots (Plugins)        | sichtbar, inaktiv          | aktiv                                           |
| Automation                    | aus (Anzeige AUTO in Grau) | Read, Touch, Latch, Write, Trim                 |
| Fader Voice-Gruppe und Master | fest (Anzeige FIXED)       | frei                                            |
| Saturate und Hall             | nicht hörbar               | hörbar                                          |
| Normalisierung                | immer, durch den AUTO MIX  | nur mit Haken „Normalisieren“ im Export-Fenster |

Übersteuert die Mischung im Manual-Modus, schützt ein Begrenzer am Ausgang das Gehör. Die App meldet dann, dass der Export clippen würde. Ziehen Sie in diesem Fall den Master-Fader herunter oder setzen Sie beim Export den Haken „Normalisieren“.

### 8.2 Mixer

Den Mixer öffnen Sie mit **MIXER** in der Kopfleiste. Jede Spur hat einen Kanalzug mit folgenden Bereichen, von oben nach unten:

1.  **DSP-Tasten:** die neun eingebauten Klangmodule ([Kapitel 9](#k9))
2.  Eingang
3.  **Inserts:** fünf Plätze für Plugins ([Kapitel 10](#k10))
4.  **Sends:** fünf Plätze, in Version 2.0 noch ohne Funktion
5.  **Ausgang:** nur Anzeige
6.  Automationsmodus ([Kapitel 11](#k11))
7.  **Pan:** Position im Stereobild
8.  Fader mit Pegelanzeige, Bereich minus unendlich bis +12 dB
9.  **S, M und Aufnahmetaste:** Solo, Stummschaltung, Aufnahmebereitschaft
10. Rolle und Name

Über das Kontextmenü des Kanalzugs blenden Sie einzelne Bereiche ein oder aus, zum Beispiel Inserts oder Sends. Dort legen Sie auch zwei Monospuren zu einer Stereospur zusammen oder trennen sie wieder.

Neben dem Fader zeigt ein cyanfarbener Balken die Pegelreduktion (Gain Reduction) des Kompressors, mit Markierungen bei 6 und 12 dB.

### 8.3 DSP-Tasten

Jeder Kanalzug hat ein Raster aus neun Tasten. In Leserichtung entspricht es der Reihenfolge im Signalweg:

|                |                |                |
|----------------|----------------|----------------|
| REPR Reparatur | NR Entrauschen | EQ Equalizer   |
| TAME Resonanz  | DES De-Esser   | CMP Kompressor |
| BRTH De-Breath | SAT Saturate   | REV Hall       |

- Einschalten öffnet das Modul, Ausschalten schließt es. Ist ein Modul bereits eingeschaltet, öffnet der erste Klick nur das Fenster.
- **Reihenfolge ändern:** EQ, TAME, DES, CMP, BRTH und SAT lassen sich wie Inserts an einen anderen Platz ziehen. Ein blaues Sternchen zeigt an, dass die Reihenfolge geändert wurde. Rechtsklick \> Standardreihenfolge stellt sie wieder her. REPR und NR stehen fest am Anfang, REV fest am Ende. Diese Tasten tragen einen kleinen Punkt.
- Eine graue Taste mit dem Hinweis „Nur im Manual“ wirkt nur im Manual-Modus.

Zuspielspuren (Musik, Atmo, O-Ton usw.) haben dasselbe Raster, mit zwei Einschränkungen. Bei der Rolle „Nicht eingeordnet“ sind die meisten Tasten gesperrt, bis eine Rolle gewählt ist. NR und BRTH gibt es auf Zuspielspuren noch nicht, der De-Esser wirkt nur bei O-Ton und Sprecher.

### 8.4 Gruppen: Voice und IT

Neben den Spuren stehen zwei Gruppen-Kanalzüge. Die Voice-Gruppe fasst alle Sprecherspuren zusammen, die IT-Gruppe alle Zuspielspuren (die internationale Tonmischung ohne Sprecher). Beide Gruppen haben Fader, Automation, Inserts und ein Raster mit EQ, TAME, CMP und REV, das nur im Manual-Modus aktiv ist. Bei der Wiedergabe zeigt der Fader der IT-Gruppe, wie das Ducking arbeitet.

### 8.5 Master

Der Master ist die Summe, die exportiert wird.

- Master-Fader mit Automation.
- **PRE-GAIN** (bis 24 dB nach oben oder unten) vor dem Fader. Hier legt der AUTO MIX seinen Pegelausgleich ab, damit der Fader nach dem Wechsel in den Manual-Modus auf 0 dB steht. Ziehen ändert den Wert, Shift erlaubt feine Schritte, Doppelklick setzt ihn auf 0.
- **EQ** und **CMP** (Bus-Kompressor), nur im Manual-Modus.
- **Pegelanzeigen:** Spitzenpegel links und rechts sowie Lautheit in LUFS als Momentan-, Kurzzeit- und integrierter Wert. Der große Wert LUFS I erscheint grün, wenn er höchstens 1 LU vom Ziel abweicht, orange bis 3 LU und rot darüber.
- **LRA**: der Lautheitsbereich, also wie stark die Lautheit über das Programm schwankt.
- **CLIP**-Anzeige: leuchtet nach einer Übersteuerung. Ein Klick auf den Kanalzug setzt sie zurück.

Der eigene Kanalzug **CUE** speist den Kopfhörerweg (**KOPFHÖRER**) und hat einen Insert-Platz.

## 9 Die Klangmodule

Jedes der neun Klangmodule hat ein eigenes Fenster mit Reglern. Die Anzeige im Modul beruht auf denselben Werten, mit denen auch Abhöre und Export rechnen.

Für alle Module gilt:

- Die Statuszeile zeigt „Werte aus dem AUTO MIX“, „Bearbeitet (weicht vom **AUTO MIX** ab)“ oder „Noch kein AUTO MIX - zeigt die Abhöre“.
- **Auf AUTO MIX zurücksetzen** stellt die Werte der Automatik wieder her.
- Im Assist-Modus öffnet Rechtsklick \> **Ansehen...** das Modul gesperrt mit dem Hinweis „Vom **AUTO MIX** eingestellt“. Der Knopf **Im Manual bearbeiten** wechselt in den Manual-Modus und gibt das Modul frei.
- **Presets:** Werks-Presets nach Kategorien, außerdem „Eigene“, „Preset sichern...“ und „Preset-Ordner zeigen“. Eigene Presets liegen unter `~/Library/SATK/Presets/`. Presets lassen sich nur im Manual-Modus laden.
- Cmd+Z, Cmd+S und die Leertaste funktionieren auch, wenn ein Modulfenster im Vordergrund ist.

### 9.1 REPR: Reparatur (De-Click und De-Plosive)

De-Click entfernt Klicks und Schmatzgeräusche im Mund, De-Plosive dämpft Popplaute bei P und B unterhalb von 240 Hz.

[[IMG:repr.png|Das Modul REPAIR mit De-Click und De-Plosive]]

| Regler               | Bereich     | Grundeinstellung | Funktion                                             |
|----------------------|-------------|------------------|------------------------------------------------------|
| EMPFINDLICHKEIT      | 0 bis 10    | 4                | Empfindlichkeit der Klickerkennung                   |
| FREQUENZ-SCHWERPUNKT | -10 bis +10 | 0                | Verschiebt die Erkennung zu tiefen oder hohen Klicks |
| KLICK-VERBREITERUNG  | 0 bis 10 ms | 4 ms             | Breite des reparierten Bereichs um einen Klick       |

**NUR KLICKS** spielt nur das Entfernte ab. So lässt sich prüfen, ob zu viel entfernt wird. De-Click arbeitet ohne Verzögerung. Klicks in Sprechpausen werden über das volle Frequenzband entfernt. De-Plosive arbeitet mit festen Einstellungen. Im Assist-Modus ist REPR ausgeschaltet, im Manual-Modus kann es zugeschaltet werden.

### 9.2 NR: Entrauschen

NR entfernt gleichmäßige Hintergrundgeräusche wie Lüfter, Brummen oder Raumrauschen. Ein neuronales Netz trennt dabei Stimme und Geräusch.

[[IMG:nr.png|Das Modul NR mit dem Regler Stärke]]

Das Modul hat einen einzigen Regler, **STÄRKE** (0 bis 100). Ein Segment am Ring schaltet NR ein und aus, ein Doppelklick setzt den Wert auf 100. Im Kreis wird das gemessene Spektrum angezeigt. NR ist in der Grundeinstellung ausgeschaltet, und auch der AUTO MIX schaltet es nicht ein. In Version 2.0 steht NR auf Sprecherspuren zur Verfügung.

Höhere Werte entfernen mehr Geräusch, können aber S-Laute verändern. Achten Sie beim Einstellen auf die S-Laute.

### 9.3 EQ: Equalizer

Der EQ verändert den Klang einer Spur, zum Beispiel um eine Stimme heller oder wärmer zu machen oder um dröhnende Frequenzen abzusenken.

[[IMG:eq.png|Das EQ-Modul mit Analyzer, Bändern und Dynamik-Reglern]]

Der EQ hat neun Bänder: Tiefensperre (Hochpass, 20 Hz bis 1 kHz), Glocke 1 bis 5, Höhenregal, Höhensperre (1 bis 20 kHz, in der Grundeinstellung aus) und Luft (8 kHz).

| Regler         | Bereich                                                   |
|----------------|-----------------------------------------------------------|
| FREQ           | Frequenz in Hz                                            |
| GAIN           | -18 bis +18 dB                                            |
| Q (Bandbreite) | Glocken 0,15 bis 14, Regale 0,1 bis 10, Sperren 0,3 bis 4 |

Glocken und Regale lassen sich dynamisch schalten (**DYN**). Das Band reagiert dann auf den Pegel und senkt eine Frequenz zum Beispiel nur ab, wenn sie zu laut wird. Regler: **RANGE** (-24 bis +24 dB), **THRESHOLD** (-80 bis 0 dB), **ATTACK** (0,1 bis 500 ms), **RELEASE** (5 ms bis 5 s oder AUTO).

**SOLO** am Band (oder Alt+Klick auf einen Bandpunkt) spielt nur den Frequenzbereich dieses Bandes ab. Das funktioniert auch im Assist-Modus und wirkt sich nie auf den Export aus. Der Analyzer zeigt das Spektrum vor und nach dem EQ. Im Menü **ANALYZER** stellen Sie **POST**, **PRE**+**POST** oder AUS ein, außerdem Auflösung, Geschwindigkeit, Bereich, Neigung und Einfrieren.

### 9.4 TAME: Resonanz

TAME erkennt störende, schneidende oder dröhnende Einzeltöne und senkt sie nur in dem Moment ab, in dem sie auftreten.

[[IMG:tame.png|Das Modul TAME (Resonanz)]]

| Regler          | Bereich        | Funktion                               |
|-----------------|----------------|----------------------------------------|
| SOFT / HARD     |                | Sanfte oder kräftige Arbeitsweise      |
| DEPTH           | 0 bis 10       | Stärke der Absenkung                   |
| DETAIL          | 0 bis 10       | Wie fein einzelne Töne getrennt werden |
| ATTACK, RELEASE | 0 bis 10       | Ansprech- und Rücklaufzeit             |
| MIX             | 0 bis 100 %    | Anteil des bearbeiteten Signals        |
| MAX CUT         | aus bis 24 dB  | Größte Absenkung                       |
| OUT, WET TRIM   | -18 bis +18 dB | Ausgangspegel                          |

Mit bis zu acht Empfindlichkeitsbändern (Glocke, Regal, Sperre, Tilt und weitere) bestimmen Sie, in welchen Frequenzbereichen TAME genauer arbeitet. **DELTA** spielt nur das Entfernte ab. Es gibt 16 Werks-Presets in den Gruppen Allgemein, Sprache, Mischung und Musik.

### 9.5 DES: De-Esser

Der De-Esser macht scharfe S-, Sch- und Z-Laute weicher, ohne die Stimme dumpf klingen zu lassen.

[[IMG:deesser.png|Das Modul DE-ESS]]

| Regler                  | Bereich                  | Funktion                                                       |
|-------------------------|--------------------------|----------------------------------------------------------------|
| SINGLE VOCAL / ALLROUND |                          | Einzelne Stimme oder gemischtes Material                       |
| WIDE / SPLIT            |                          | Gesamtes Signal absenken oder nur den scharfen Frequenzbereich |
| THRESHOLD               | minus unendlich bis 0 dB | Einsatzschwelle                                                |
| RANGE                   | 0 bis 24 dB              | Größte Absenkung                                               |
| LOOKAHEAD               | 0 bis 15 ms, ein/aus     | Greift bereits kurz vor dem S-Laut                             |
| HIGH-PASS, LOW-PASS     | 2 bis 20 kHz             | Frequenzbereich, auf den der De-Esser reagiert                 |

**TRIGGER** spielt das Signal ab, auf das der De-Esser reagiert, **ENTFERNT** das Entfernte. Der AUTO MIX misst die Schärfe jeder Stimme und stellt den De-Esser entsprechend ein. Es gibt acht Werks-Presets, zum Beispiel für Männer- und Frauenstimmen.

### 9.6 CMP: Kompressor

Der Kompressor gleicht laute und leise Stellen an, damit die Stimme gleichmäßig und präsent klingt. Das Modul zeigt Kennlinie, Pegelverlauf und Pegelreduktion (in Cyan).

[[IMG:comp.png|Das Kompressor-Modul mit Kennlinie und Pegelverlauf]]

Es gibt drei Arbeitsweisen: **CLEAN** (spitzenorientiert, für Sprache), **SMOOTH** (weich, am Mittelwert orientiert) und **BUS** (für Gruppen und Master).

| Regler           | Bereich                                   | Funktion                                                                                                   |
|------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------|
| THRESHOLD        | -60 bis 0 dB                              | Pegel, ab dem komprimiert wird                                                                             |
| RATIO            | 1:1 bis 100:1                             | Stärke der Kompression                                                                                     |
| KNEE             | 0 bis 24 dB                               | Weicher oder harter Einsatz                                                                                |
| ATTACK           | 0,1 bis 250 ms                            | Ansprechzeit                                                                                               |
| RELEASE          | 5 ms bis 2,5 s oder AUTO                  | Rücklaufzeit. Bei AUTO passt sie sich an die Sprechpausen an, der eingestellte Wert ist dann ohne Wirkung. |
| MAKEUP           | -12 bis +24 dB (AUTO nur bei CLEAN)       | Gleicht die Pegelreduktion aus                                                                             |
| MIX              | 0 bis 100 %                               | Parallelkompression                                                                                        |
| HOLD, RANGE, DRY | 0 bis 500 ms, 0 bis 60 dB, aus bis +36 dB | Feineinstellung, bei SMOOTH ohne Wirkung                                                                   |

Werks-Presets: Sprache - Broadcast, Sprache - sanft, Musik - Bus-Glue, Musik - dichtes Bett, Atmo - Fläche, Effekt - Spitzen fassen. Für Gruppen und Master gibt es eigene Presets. Ein Preset setzt Arbeitsweise, Ratio, Knee, Zeiten und Mix, aber nicht Threshold und Makeup.

### 9.7 BRTH: De-Breath

De-Breath senkt Atemgeräusche zwischen den Sätzen ab, ohne die Sprache zu verändern. Die Atmer werden am Klang erkannt, nicht allein an der Lautstärke.

[[IMG:debreath.png|Das Modul DE-BREATH mit Übersicht und Lupe]]

| Regler            | Bereich                       | Grundeinstellung |
|-------------------|-------------------------------|------------------|
| RANGE (Absenkung) | 0 bis 24 dB                   | 12 dB            |
| Empfindlichkeit   | VORSICHTIG, NORMAL, GRÜNDLICH | NORMAL           |

Oben zeigt das Modul die gesamte Spur, darunter eine Lupe um den Abspielkopf mit der Wellenform vor und nach der Bearbeitung. Ein Klick auf einen Atmer entfernt ihn aus der Bearbeitung oder nimmt ihn wieder auf. Mit Alt+Ziehen markieren Sie einen Atmer von Hand. **BREATHS ONLY** spielt nur die Atmer ab. Die Statuszeile nennt die Zahl der gefundenen, von Hand gesetzten und unsicheren Atmer. Im Assist-Modus ist De-Breath in der Grundeinstellung eingeschaltet. Es wirkt bei Wiedergabe und Export, aber nicht während der Aufnahme.

### 9.8 SAT: Saturate

Saturate fügt eine analog klingende Sättigung hinzu, ähnlich einer Röhre oder einem Tonband. Das Modul wirkt nur im Manual-Modus und ist in der Grundeinstellung ausgeschaltet.

[[IMG:sat.png|Das Modul SATURATE mit Kennlinie und Spektrum]]

Als Art wählen Sie **TUBE** oder **TAPE**, jeweils kombinierbar mit **WARM**. Daraus ergeben sich Tube, Tape, Warm Tube und Warm Tape. Regler: **DRIVE** (0 bis 100), **MIX** (0 bis 100), **OUTPUT** (-24 bis +24 dB). Es gibt Werks-Presets wie Clean sowie mehrere Tube- und Tape-Varianten.

### 9.9 REV: Hall

Der Hall setzt eine Stimme in einen Raum, von der kleinen Sprecherkabine bis zur großen Halle. Er wirkt nur im Manual-Modus und ist das letzte Glied der Kette. Eine Sprecherspur wird ab dem Hall stereo, und der Nachhall ist im Export enthalten.

[[IMG:rev.png|Das Hall-Modul (REVERB)]]

| Regler       | Bereich      | Grundeinstellung | Funktion                            |
|--------------|--------------|------------------|-------------------------------------|
| SPACE        | 0,2 bis 10 s | 2,5 s            | Nachhallzeit, Größe des Raums       |
| DECAY RATE   | 0,5 bis 2    | 1                | Geschwindigkeit des Ausklingens     |
| DISTANCE     | 0 bis 1      | 0,5              | Wahrgenommene Entfernung der Stimme |
| BRIGHTNESS   | 0 bis 1      | 0,5              | Hell oder dunkel                    |
| CHARACTER    | 0 bis 1      | 0,3              | Klangfarbe des Raums                |
| STEREO WIDTH | 0 bis 1,2    | 0,7              | Stereobreite                        |
| MIX          | 0 bis 1      | 0,3              | Anteil des Halls                    |
| PREDELAY     | 0 bis 500 ms | 0                | Abstand zwischen Stimme und Hall    |

Dazu kommen Ein- und Ausgangspegel, Pan und zwei EQ-Reiter (DECAY EQ und **POST** EQ). Es gibt rund 30 Werks-Presets in den Gruppen Ambience, Small, Medium, Large, Very Large und Voice, zum Beispiel Vocal Booth, Narrator Polish und Radio Studio.

## 10 Plugins und Insert-Slots

In die Insert-Slots laden Sie Plugins anderer Hersteller in den Formaten Audio Unit (AU, auch AUv3) und VST3. Instrumente werden nicht angeboten. Plugins sind nur im Manual-Modus aktiv. Im Assist-Modus sind die Slots zwar sichtbar, aber ohne Wirkung.

Jede Spur, die Voice-Gruppe, die IT-Gruppe und der Master haben je fünf Slots, der CUE-Kanalzug hat einen. Die Plugins arbeiten in der Reihenfolge von oben nach unten und folgen auf die eingebauten Module.

### 10.1 Plugin einsetzen

1.  Klicken Sie auf einen leeren Slot. Die Auswahl öffnet sich, sortiert nach Herstellern.
2.  Wählen Sie das Plugin. Das Plugin-Fenster öffnet sich sofort.

### 10.2 Bedienung am Slot

| Bedienung                      | Funktion                                                          |
|--------------------------------|-------------------------------------------------------------------|
| Klick auf den Namen            | Plugin-Fenster öffnen                                             |
| Ein/Aus-Symbol oder Cmd+Klick  | Bypass (Plugin umgehen)                                           |
| x beim Überfahren mit der Maus | Plugin entfernen (Cmd+Z stellt es wieder her)                     |
| Rechtsklick                    | Menü mit Open editor, Bypass, Remove und Rescan plugins... |

Ist ein Plugin-Fenster im Vordergrund, gibt die App die Leertaste (Play/Stop), die Taste R (Aufnahme) und Pos1 weiterhin an den Transport weiter.

### 10.3 Plugin-Liste und neuer Scan

Beim Start prüft die App die installierten Plugins. Jedes Plugin wird dabei in einem eigenen Hilfsprozess getestet. Stürzt ein Plugin ab, kommt es auf eine Sperrliste und gefährdet die App nicht. Nach der Installation neuer Plugins oder einem Plugin-Update wählen Sie im Slot-Menü **Rescan plugins...**. Dabei wird auch die Sperrliste geleert, und nicht mehr vorhandene Plugins verschwinden aus der Liste.

Die Verzögerung (Latenz) von Plugins wird automatisch ausgeglichen, auch auf Gruppen und Master.

## 11 Automation

Automation zeichnet Reglerbewegungen auf und spielt sie bei jeder Wiedergabe ab. So wird zum Beispiel eine Stelle automatisch leiser und eine andere lauter. Automation steht im Manual-Modus zur Verfügung. Im Assist-Modus zeigt die Taste AUTO in Grau.

### 11.1 Automatisierbare Parameter

- Lautstärke (Fader) auf Spuren, Voice-Gruppe, IT-Gruppe und Master
- Pan
- Mute
- **Plugin-Parameter:** jeder Regler eines Plugins, den Sie während der Aufzeichnung bewegen

Der CUE-Kanalzug hat keine Automation.

### 11.2 Automationsmodi

Den Modus wählen Sie über die Automationstaste im Kanalzug. Bezeichnungen und Verhalten entsprechen den gängigen DAWs:

| Modus         | Farbe      | Verhalten                                                                                                                            |
|---------------|------------|--------------------------------------------------------------------------------------------------------------------------------------|
| READ          | grau       | Spielt die Kurve ab. Der Fader lässt sich trotzdem bewegen, eine Marke zeigt den Wert der Automation.                                |
| TOUCH         | hellblau   | Schreibt nur, solange der Regler berührt wird. Nach dem Loslassen kehrt er innerhalb von 0,25 Sekunden zur vorhandenen Kurve zurück. |
| LATCH         | dunkelblau | Schreibt ab der ersten Berührung und hält den letzten Wert bis STOP.                                                                 |
| WRITE         | rot        | Schreibt ab PLAY durchgehend, auch ohne Berührung. Nach einem Durchgang schaltet die Spur automatisch auf TOUCH.                     |
| TRIM (Zusatz) | gelb       | Schreibt keine absoluten Werte, sondern eine Korrektur der vorhandenen Kurve, zum Beispiel ein gesamtes Ducking 2 dB tiefer.         |

Mute-Automation: In **TOUCH** wirkt die Mute-Taste wie ein Taster und schaltet stumm, solange sie gedrückt ist. In **WRITE** wird ab dem Start geschrieben, in **LATCH** bis STOP.

### 11.3 Automation in der Zeitleiste

Im Spurkopf schalten Sie die Ansicht zwischen Wellenform und Volume um. Alt+Klick schaltet alle Spuren um. In der Ansicht Volume sehen Sie die Kurve und können Punkte setzen, verschieben und löschen (auswählen und Entf drücken). Auch das Ducking des AUTO MIX ist hier als Kurve zu sehen.

Die Automationsmodi werden mit dem Projekt gespeichert.

## 12 Export

Mit **EXPORT** in der Transportleiste erzeugen Sie die Lieferdateien: die fertige Mischung, auf Wunsch die Stimme als eigene Datei, das Video mit neuem Ton oder ein MXF für den Sendebetrieb. Alle Dateien landen in einem eigenen Lieferordner, vorhandene Dateien werden nicht überschrieben.

### 12.1 Ablauf

1.  Im Assist-Modus **AUTO MIX** ausführen ([Kapitel 7](#k7)), im Manual-Modus die Mischung fertigstellen.
2.  **EXPORT** drücken. Das Export-Fenster öffnet sich.
3.  Im Feld **Name** einen Namen für die Lieferung eintragen. Bleibt es leer, wird der Projektname verwendet.
4.  Auswählen, welche Dateien entstehen sollen ([Abschnitte 12.2](#k12-2) bis 12.4).
5.  **EXPORT** klicken oder Return drücken und den Zielordner wählen.

Im Zielordner entsteht ein Unterordner mit dem Liefernamen. Die Dateien heißen zum Beispiel `Beitrag_2026-11-19_v1_mix.wav` und `Beitrag_2026-11-19_v1_voice.wav`. Bei jedem weiteren Export steigt die Versionsnummer (v2, v3 usw.).

### 12.2 Audio

| Zeile                                      | Inhalt                                                                                                 | Grundeinstellung |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------|
| Audio-Mix                                  | Fertige Mischung (stereo)                                                                              | ein, WAV 24 Bit  |
| Voice-Stem                                 | Nur die Stimme bzw. Stimmen, zum Beispiel für eine spätere Neumischung                                 | aus              |
| Voice-Spuren einzeln                       | Eine Datei je Sprecherspur ohne Effekte, erst ab zwei Sprecherspuren verfügbar                         | aus              |
| Schnittliste für andere DAWs (AES31, .adl) | Zum Öffnen des Projekts in Pro Tools, Nuendo und anderen DAWs. Das Projekt muss dazu gespeichert sein. | aus              |

Verfügbare Formate: WAV, AIFF, AAC (.m4a), MP3, MP2 (.mp2), MP2 (.wav), FLAC und Opus.

| Einstellung                   | Auswahl                                 | Einschränkung                                   |
|-------------------------------|-----------------------------------------|-------------------------------------------------|
| Abtastrate                    | Projekt, 44,1, 48, 88,2 oder 96 kHz     | MP2 und MP3 höchstens 48 kHz, Opus immer 48 kHz |
| Bittiefe (WAV, AIFF, FLAC)    | 16 Bit mit Dither, 24 Bit, 32 Bit Float | FLAC höchstens 24 Bit                           |
| Bitrate (MP3, AAC, MP2, Opus) | 128, 192, 256 oder 320 kbit/s           | 384 kbit/s nur bei MP2                          |

WAV-Dateien erhalten einen Zeitstempel nach dem BWF-Standard, ausgehend vom Startzeitcode des Projekts.

### 12.3 Normalisieren

Der Haken „Auf -23 LUFS (...) normalisieren“ bringt die Datei auf die Ziel-Lautheit des Profils und begrenzt die Spitzen mit einem True-Peak-Limiter. Der Wert in der Beschriftung richtet sich nach dem Profil. Beim Profil Studio 0 dB wird stattdessen auf einen Spitzenpegel von 0 dBTP normalisiert.

- Im Assist-Modus normalisiert bereits der AUTO MIX. Der Export gibt die fertige Mischung aus.
- Im Manual-Modus wird nur normalisiert, wenn der Haken gesetzt ist. Eine Zeile im Fenster nennt, wie weit die Datei dann von Ihrer Abhöre abweicht.
- Der Haken gilt jeweils nur für den aktuellen Export.
- Zusätzlich können Sie „Lautheitsumfang begrenzen (LRA auf 6 LU, Mehrband)“ wählen. Diese Option verringert große Lautstärkeschwankungen.

### 12.4 Video und MXF

Unter **AUSGABEN** wählen Sie **Video (MOV/MP4)** oder **MXF (Broadcast)**. Aktiv ist jeweils die Option, die zum geladenen Video passt. Das Bild wird unverändert übernommen und der neue Ton eingesetzt.

Beim MXF gibt es zusätzliche Einstellungen:

- **Delivery-Profil:** EBU R128, US ATSC - IT 8, Stereo, DE ARD/ZDF - HDF01a, JP ARIB - RDD9, FR CST - AS-10. Passt das Format-Profil des Projekts nicht zum Delivery-Profil, erscheint eine rote Warnung.
- Voreinstellung für die Tonspuren, zum Beispiel „Mix 1+2, Voice 7+8“.
- **Tonspur-Belegung:** Für jede der acht Spuren T1 bis T8 legen Sie fest, was darauf liegt (Mischung L oder R, Voice, stumm oder ein Kanal der Quelle). Die Bezeichnung einer Spur ist nur ein Name und ändert ihren Inhalt nicht.

Neben dem MXF entsteht automatisch ein Belegungsblatt (`<Name>_tracks.txt`), das die tatsächliche Spurbelegung beschreibt.

### 12.5 Podcast: Kapitel und Folgen-Angaben

Für Podcasts öffnen Sie das Fenster Kapitel (Fenster \> Kapitel, Cmd+Shift+K):

1.  Abspielkopf an den Anfang des Kapitels setzen und **Am Abspielkopf anlegen** klicken.
2.  Titel eintragen, optional ein Bild und einen Link. Kapitel ohne Titel werden nicht exportiert.
3.  Unter **PROJEKT...** \> FOLGE Titel, Autor, Sendung, Kommentar und Titelbild eintragen. Das Titelbild muss quadratisch sein und 1400 bis 3000 Pixel groß, Kapitelbilder mindestens 600 Pixel.

Beim Export erhält der Mix ID3-Angaben und Kapitel. Zusätzlich entsteht eine Kapiteldatei `<Name>-chapters.json` nach dem Standard Podcasting 2.0 samt Kapitelbildern.

### 12.6 Untertitel und Transkript

Untertitel exportieren Sie im Script Editor auf der Seite **AUDIO** mit **TEXT EXPORT**. Zur Auswahl stehen SubRip (.srt), WebVTT (.vtt), Klartext (.txt) und JSON (Podcast 2.0).

## 13 Fernvertonung, virtuelle Kamera und Cue

Bei der Fernvertonung sitzt der Sprecher an einem anderen Ort und ist über einen Browser- oder Konferenzdienst verbunden. Dafür bringt voyzSESSION PRO ein eigenes virtuelles Audiogerät und eine virtuelle Kamera mit. Der Sprecher sieht Ihr Bild, hört Video und Regie und spricht direkt in Ihre Aufnahmespur.

### 13.1 Einmalige Einrichtung

1.  **Audiotreiber installieren:** Einstellungen \> Audio/Video..., dort unter „Virtual audio device“ auf **Install** klicken. Danach die App neu starten. Es entstehen zwei Geräte: voyzSESSION Send (Ausgang aus der App) und voyzSESSION Return (Eingang in die App).
2.  **Kamera installieren:** Im App-Menü **Virtuelle Kamera installieren...** wählen. Die App muss dazu im Ordner Programme liegen. macOS verlangt eine Freigabe unter Systemeinstellungen \> Allgemein \> Anmeldeobjekte & Erweiterungen \> Kamera-Erweiterungen. Unter Umständen ist ein Neustart nötig. **Virtuelle Kamera: Zustand...** zeigt an, ob die Kamera aktiv ist.
3.  In den A/V-Einstellungen **Virtual camera (video to browsers)** einschalten.

Das Fenster A/V-Einstellungen ist in Version 2.0 noch englisch beschriftet, auch wenn die App auf Deutsch eingestellt ist.

### 13.2 Eine Sitzung durchführen

1.  Im Konferenz- oder Browserdienst (zum Beispiel SessionLink PRO, Zoom oder Teams) einstellen: Mikrofon = voyzSESSION Send, Lautsprecher = voyzSESSION Return, Kamera = voyzSESSION.
2.  In voyzSESSION PRO die Sprecherspur auf den Eingang voyzSESSION Return L (oder R) legen.
3.  Im Mixer am Kanalzug **CUE** mit **MESSEN** die Laufzeit messen. Die App schickt einen leisen Testton zum Sprecher und sucht ihn im Rückweg. Das Ergebnis wird in Millisekunden angezeigt.
4.  Wie gewohnt aufnehmen ([Kapitel 4](#k4)).
5.  **Nach der Aufnahme:** Rechtsklick auf den Take \> **Um Laufzeit ausrichten**. Der Take wird um die gemessene Verzögerung nach vorn verschoben und liegt danach wieder synchron zum Bild.

### 13.3 Cue: Was der Sprecher hört

Der Cue-Weg zum Sprecher enthält den Ton von Video und Zuspielspuren, die bisherigen Takes und die Rückansage (Talkback). Die eigene Live-Stimme wird nicht zurückgeschickt, damit der Sprecher sich nicht verzögert hört.

- **TALK** im Kanalzug **CUE** schaltet das Talkback-Mikrofon zu, nur im Stillstand. Talkback ist nie auf den eigenen Lautsprechern zu hören.
- Der Cue-Fader regelt die Lautstärke zum Sprecher (-48 bis +6 dB). Gesendet wird mit -23 LUFS.
- Bei normaler Wiedergabe ist der Rückweg nur zu hören, wenn auf der Spur die Taste I (Eingang abhören) aktiv ist. Während der Aufnahme ist er immer hörbar.

### 13.4 Kabinenfenster und Videofenster

Für einen Sprecher in der eigenen Kabine gibt es das Kabinenfenster (Fenster \> Kabinenfenster, Cmd+Shift+B). Es wird über einen per HDMI angeschlossenen Monitor angezeigt und ist damit verzögerungsfrei. Links steht der Prompter, rechts das Bild mit Timecode, während der Aufnahme erscheint ein roter Rahmen. Das Videofenster (Cmd+9 oder **BILD**) zeigt nur das Bild ohne Rahmen, auf Wunsch auf einem externen Bildschirm.

## 14 Externe Steuerung: Stream Deck, Bedienpulte, OSC

voyzSESSION PRO lässt sich mit einem Elgato Stream Deck, einem Mackie-Control-Pult oder per OSC steuern. Das ist zum Beispiel nützlich, wenn ein Sprecher allein in der Kabine arbeitet.

### 14.1 Stream Deck

1.  Im App-Menü **Stream Deck: Plugin installieren...** wählen. Die Elgato-Software übernimmt das Plugin.
2.  Unter **Stream Deck: Belegung laden** die passende Vorlage wählen: Stream Deck (15 Tasten), Stream Deck MK.2 (15 Tasten), Stream Deck Mini (6 Tasten), Stream Deck XL (32 Tasten) oder Stream Deck + (Regler).
3.  In den A/V-Einstellungen **OSC remote control** einschalten. Das Plugin kommuniziert über OSC mit der App.

Die Tasten zeigen den Zustand der App an, etwa ein/aus oder aktuelle Werte. Die Kanalzug-Tasten stehen in derselben Reihenfolge wie im Mischpult und schalten auch Zuspielspuren.

### 14.2 Mackie-Control-Pult (MCU)

Wählen Sie in den A/V-Einstellungen unter **MCU FADER CONTROLLER (MIDI)** den MIDI-Anschluss Ihres Pults. Der Zusatz **RECEIVING** zeigt an, dass Daten vom Pult ankommen.

| Bedienelement am Pult           | Funktion                                                |
|---------------------------------|---------------------------------------------------------|
| 8 Fader (berührungsempfindlich) | Lautstärke der Spuren, wie der Fader auf dem Bildschirm |
| V-Pot, V-Pot drücken            | Pan, Pan auf Mitte                                      |
| REC, SOLO, MUTE, SELECT         | Je Kanal (REC nur auf Sprecherspuren)                   |
| PLAY, STOP, RECORD              | Transport (STOP im Stillstand springt zum Anfang)       |
| CYCLE                           | Loop                                                    |
| Rückspulen, Vorspulen           | Spulen                                                  |
| BANK, CHANNEL                   | Fader-Bank um 8 bzw. 1 Spur verschieben                 |

Der Master-Fader des Pults steuert den Master, die Timecode-Anzeige des Pults läuft mit.

### 14.3 OSC und Anzeigen im Browser

- **OSC:** Die App empfängt auf Port 8000 und meldet Zustände zurück, in der Grundeinstellung an 127.0.0.1:9000 (änderbar unter **OSC REPLY TO**). Über OSC sind Transport, Spurfunktionen (Arm, Solo, Mute, Automationsmodus), Schnitt, Marken, Ansichten, **AUTO MIX**, Speichern, Export und Talkback erreichbar.
- **Konsolen-Anzeigen im Browser:** **Console displays (web)** einschalten, mit **COPY URLS** die Adressen kopieren und auf einem Tablet oder zweiten Rechner im selben Netzwerk öffnen (Port 8422, mit Zugangsschlüssel in der Adresse).

## 15 Einstellungen, Projekte, Speichern und Wiederherstellen

### 15.1 Einstellungen > Allgemein (Cmd+,)

| Zeile                | Funktion                                                                                                                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Sprache              | Automatisch (Systemsprache), Deutsch, English, Français, Español, Italiano, Português. Die Änderung wirkt beim nächsten Start. |
| Lesesprache Prompter | Sprache, in der die Spracherkennung dem Text folgt                                                                             |
| Pegel-Check          | „Pegel-Check beim Start zeigen“ ein oder aus                                                                                   |
| Hinweise             | „Hinweise wieder anzeigen“ blendet einmalige Hinweise erneut ein                                                               |

Direkt im Menü Einstellungen liegt der Schalter **Crossfade bei Überlappung** (in der Grundeinstellung eingeschaltet, siehe [Kapitel 6](#k6)).

### 15.2 Einstellungen > Audio/Video (Knopf A/V...)

- **OUTPUT und INPUT:** Ausgabe- und Eingabegerät, unabhängig voneinander wählbar, zum Beispiel ein USB-Mikrofon zusammen mit einem Interface.
- **SAMPLE RATE und BUFFER SIZE:** Puffergröße von 32 bis 1024 Samples. Ein kleiner Puffer verkürzt die Verzögerung im Kopfhörer, erhöht aber die Rechenlast. Darunter steht die gemessene Gesamtverzögerung (Round trip).
- **Direct hardware monitoring:** eingeschaltet lassen, wenn Sie sich über das Interface abhören (Grundeinstellung). Die Software-Abhöre ist dann stumm, damit Sie sich nicht doppelt hören.
- **RECORDING DELAY:** verschiebt neue Takes um einige Samples, falls das Interface sie versetzt aufzeichnet.
- **Low latency monitoring:** umgeht auf abgehörten Spuren Plugins mit zu hoher Verzögerung. Diese Plugins werden orange markiert. Der Export ist davon nicht betroffen.
- **Außerdem:** MCU-Pult, virtuelles Audiogerät, Anzeigen im Browser, OSC und virtuelle Kamera ([Kapitel 13](#k13) und 14).

### 15.3 Projekteinstellungen (Knopf PROJEKT...)

Änderungen wirken sofort.

- **AUDIO, Abtastrate:** Die Abtastrate wird vom Projekt bestimmt, nicht vom Interface. Bei einem leeren Projekt stellen Sie sie direkt ein. Enthält das Projekt bereits Material, wählen Sie **Kopie mit anderer Abtastrate speichern**. Die App rechnet dann eine Kopie um, das Original bleibt unverändert.
- **ZEIT UND BILD:** Bildrate (23,976 bis 60 fps, auch Drop-Frame), Startzeitcode (Schnellwahl 00:00:00:00 oder 10:00:00:00) und **Vom Video übernehmen**. Weicht die Bildrate des Videos ab, wird sie rot angezeigt.
- **LAUTHEIT:** Format-Profil (Tabelle in [Kapitel 7](#k7)).
- **FOLGE:** Angaben für Podcasts ([Abschnitt 12.5](#k12-5)).

### 15.4 Speichern, Vorlagen, Wiederherstellen

- Speichern mit Cmd+S, Speichern unter mit Cmd+Shift+S oder über den Knopf **DATEI**. Ein Projekt ist ein Ordner mit der Endung `.satkproj`. Aufnahmen werden direkt im Unterordner `audio` des gespeicherten Projekts abgelegt. Ein neues Projekt sollte deshalb vor der ersten Aufnahme gespeichert werden.
- Cmd+S während eines **AUTO MIX** wird vorgemerkt und danach ausgeführt.
- **Vorlagen:** **DATEI** \> **Aktuelles als Vorlage sichern...** speichert Spuren, Einstellungen, Inserts, Profil und Prompter-Text, aber keine Aufnahmen, kein Video, keine Kapitel und keine Marken. Neue Projekte legen Sie dann mit **DATEI** \> **Neu aus Vorlage** an.
- **Automatische Sicherung:** Die App speichert bei Änderungen alle 30 Sekunden einen Wiederherstellungsstand. Nach einem Absturz fragt sie beim nächsten Start, ob dieser Stand wiederhergestellt oder verworfen werden soll.
- **Beenden:** Bei ungespeicherten Änderungen fragt die App, ob gespeichert, verworfen oder abgebrochen werden soll. Dieselbe Frage erscheint bei Neu und Öffnen.

## Anhang

### A Tastenkombinationen

Tasten ohne Cmd, Alt oder Control wirken nicht, solange ein Textfeld aktiv ist.

| Bereich    | Taste                             | Funktion                                              |
|------------|-----------------------------------|-------------------------------------------------------|
| Transport  | Leertaste                         | Wiedergabe, Stopp                                     |
| Transport  | R                                 | Aufnahme starten oder beenden                         |
| Transport  | L                                 | Loop ein oder aus                                     |
| Transport  | Return, Ende, Pos1                | Zum Anfang, zum Ende, auf Position 0                  |
| Transport  | Komma, Punkt                      | 1 Sekunde zurück oder vor                             |
| Marken     | Alt+M                             | Marke setzen                                          |
| Marken     | 1 bis 9, Shift+1 bis 9            | Marke setzen, Marke anspringen                        |
| Marken     | Alt+Komma, Alt+Punkt              | Vorige oder nächste Marke                             |
| Bearbeiten | Cmd+Z, Cmd+Shift+Z                | Rückgängig, Wiederholen                               |
| Bearbeiten | Cmd+E                             | Teilen                                                |
| Bearbeiten | Cmd+C, Cmd+V, Cmd+D               | Kopieren, Einfügen, Duplizieren                       |
| Bearbeiten | Cmd+A                             | Alle Takes auswählen                                  |
| Bearbeiten | Entf                              | Auswahl löschen                                       |
| Bearbeiten | M                                 | Take stummschalten                                    |
| Bearbeiten | S                                 | AutoCut                                               |
| Bearbeiten | F                                 | Blende oder Crossfade                                 |
| Bearbeiten | I                                 | Audio an der Abspielposition importieren              |
| Bearbeiten | Cmd+Pfeil nach oben/unten         | Take auf Nachbarspur verschieben, mit Shift kopieren  |
| Bearbeiten | Pfeil links/rechts                | Auswahl um 1 Bild verschieben, mit Shift um 1 Sekunde |
| Ansicht    | Cmd+=, Cmd+Minus                  | Zoom                                                  |
| Ansicht    | 0, Z                              | Ganzes Projekt, Auswahl                               |
| Ansicht    | Control+Alt+Pfeil nach oben/unten | Spurhöhe                                              |
| Ansicht    | Cmd+Alt+Pfeil nach oben/unten     | Höhe der Wellenform                                   |
| Mischen    | Cmd+M                             | AUTO MIX                                              |
| Projekt    | Cmd+S, Cmd+Shift+S                | Speichern, Speichern unter                            |
| Fenster    | Cmd+,                             | Einstellungen \> Allgemein                            |
| Fenster    | Cmd+9                             | Videofenster                                          |
| Fenster    | Cmd+Shift+B                       | Kabinenfenster                                        |
| Fenster    | Cmd+Shift+K                       | Kapitel                                               |
| Prompter   | Cmd+Plus, Cmd+Minus, Cmd+0        | Schriftgröße                                          |
| Hilfe      | Esc                               | Hilfe schließen                                       |

### B Glossar

| Begriff                         | Bedeutung                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------|
| AUTO MIX                        | Automatische Mischung im Assist-Modus                                                |
| Bounce                          | Die Mischung so in eine Datei schreiben, wie sie zu hören ist                        |
| Clip-Gain                       | Lautstärke direkt am Take, vor dem Kanalzug                                          |
| Crossfade                       | Überblendung zwischen zwei Takes                                                     |
| Ducking                         | Automatisches Absenken von Musik oder Atmo, während gesprochen wird                  |
| Fader                           | Schieberegler für die Lautstärke                                                     |
| Insert                          | Platz für ein Plugin im Kanalzug                                                     |
| IT (Internationale Tonmischung) | Alle Bestandteile außer dem Sprecher: O-Ton, Musik, Atmo, Effekte                    |
| LUFS, LU                        | Maßeinheiten für die wahrgenommene Lautheit. -23 LUFS ist die Fernsehnorm in Europa. |
| LRA                             | Lautheitsbereich, also wie stark die Lautheit über das Programm schwankt             |
| O-Ton                           | Originalton aus dem Video, zum Beispiel ein Interview                                |
| Pre-Roll, Post-Roll             | Vorlauf und Nachlauf einer Aufnahme                                                  |
| Punch                           | Aufnahme nur in einem festgelegten Bereich, um eine Stelle zu ersetzen               |
| Rolle                           | Art des Inhalts einer Spur (Sprecher, Musik usw.), steuert die Automatik             |
| Scharf schalten                 | Eine Spur für die Aufnahme vorbereiten                                               |
| Stem                            | Einzelner Bestandteil der Mischung als eigene Datei, zum Beispiel nur die Stimme     |
| Take, Region                    | Aufgenommenes oder importiertes Stück Audio auf einer Spur                           |
| True Peak (dBTP)                | Tatsächlicher höchster Spitzenwert des Signals                                       |

### C Fehlerbehebung

| Problem                                               | Lösung                                                                                                                                                                         |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pegel-Check zeigt „Kein Signal“                       | Mikrofon im Pegel-Check und unter A/V... \> INPUT prüfen. Außerdem prüfen, ob macOS den Mikrofonzugriff erlaubt (Systemeinstellungen \> Datenschutz & Sicherheit \> Mikrofon). |
| REC startet keine Aufnahme                            | Eine Spur muss scharf geschaltet sein (R). Ohne scharfe Spur meldet die App „Keine Spur scharf“. Ein neues Projekt muss zuerst gespeichert werden.                             |
| Die eigene Stimme ist doppelt oder hallig zu hören    | Die Stimme kommt über Interface und Software gleichzeitig. Unter A/V... Direct hardware monitoring einschalten oder am Interface den Direct Monitor ausschalten.               |
| AUTO MIX startet nicht                                | Solo ausschalten, laufende Aufnahme beenden, in den Assist-Modus wechseln. Mindestens ein Take muss vorhanden sein.                                                            |
| AUTO MIX leuchtet blau                                | Die gespeicherte Mischung passt nicht mehr zum Projekt. AUTO MIX erneut ausführen.                                                                                             |
| Meldung, dass der Export clippen würde (Manual-Modus) | Master-Fader herunterziehen oder beim Export „Normalisieren“ aktivieren.                                                                                                       |
| Ein Plugin fehlt in der Liste                         | Im Slot-Menü Rescan plugins... wählen. Instrumente werden grundsätzlich nicht angeboten.                                                                                            |
| Ein Plugin bringt die App zum Absturz                 | Das Plugin kommt beim nächsten Start auf die Sperrliste. Nach einem Update des Plugins neu scannen.                                                                            |
| Der Prompter folgt der Stimme nicht                   | Spracherkennung in macOS erlauben und die Diktierfunktion einschalten. Mit LANG die Sprache des Textes einstellen.                                                             |
| Der Script Editor bleibt leer                         | Transkribieren drücken. Zuspielspuren werden nicht transkribiert.                                                                                                              |
| Die virtuelle Kamera erscheint nicht                  | Die App muss im Ordner Programme liegen. Erweiterung in den Systemeinstellungen freigeben, gegebenenfalls den Mac neu starten und die Kamera unter A/V... einschalten.         |
| voyzSESSION Send oder Return fehlt                    | Treiber unter A/V... installieren und die App neu starten.                                                                                                                     |
| Die Bildrate wird rot angezeigt                       | Video und Projekt haben unterschiedliche Bildraten. Unter PROJEKT... „Vom Video übernehmen“ wählen.                                                                            |
| Die App ist abgestürzt                                | Beim nächsten Start die Wiederherstellung wählen. Die App sichert bei Änderungen alle 30 Sekunden.                                                                             |
| Falsche Sprache der Oberfläche                        | Einstellungen \> Allgemein \> Sprache wählen und die App neu starten.                                                                                                          |
| Das Fenster A/V-Einstellungen ist englisch            | Dieses Fenster ist in Version 2.0 noch nicht übersetzt. Die übrige App folgt der gewählten Sprache.                                                                            |
