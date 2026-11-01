# Sprachfassungen der Website

Stand 01.11.2026. Sechs Sprachen: Deutsch (Quelle), Englisch, Französisch,
Spanisch, Italienisch, Portugiesisch (eine Fassung für alle Portugiesisch-Sprecher, `hreflang="pt"`,
im Menü „Português“; formuliert europäisch (pt-PT), weil Europa der wichtigere
Markt ist. Wo pt-BR zwingend anders lautet, steht die brasilianische Form in
`pt-alternativen.json` und in der Gegenlese-Liste in der Spalte „Alternative pt-BR“).

## Adressschema

| Sprache | Startseite | Produktseite        | Datei                    |
|---------|------------|---------------------|--------------------------|
| DE      | `/`        | `/voyzsession`      | `voyzsession.html`       |
| EN      | `/en`      | `/voyzsession-en`   | `voyzsession-en.html`    |
| FR      | `/fr/`     | `/fr/voyzsession`   | `fr/voyzsession.html`    |
| ES      | `/es/`     | `/es/voyzsession`   | `es/voyzsession.html`    |
| IT      | `/it/`     | `/it/voyzsession`   | `it/voyzsession.html`    |
| PT      | `/pt/`     | `/pt/voyzsession`   | `pt/voyzsession.html`    |

Warum so:

* **Keine bestehende Adresse bricht.** DE und EN bleiben, wo sie sind. Auf sie
  zeigen Apps, App-Store-Einträge, Presse und Google. Nichts braucht eine
  Weiterleitung.
* **Neue Sprachen bekommen Unterordner.** Das ist das übliche Schema, Google
  ordnet es sicher zu, und der Slug bleibt der deutsche (`/fr/voyzsession`).
  Die Produktnamen sind ohnehin sprachneutral.
* Das Schema ist **gemischt** (EN mit Endung `-en`, der Rest mit Ordner). Wer EN
  später auch nach `/en/…` ziehen will, ändert eine Funktion im Generator und
  trägt zwölf 301-Zeilen in `_redirects` ein. Für 2.0 lohnt das nicht.

## Wer pflegt was

| Seiten | Quelle | Andere Sprachen |
|---|---|---|
| 12 Produkt- und Übersichtsseiten (index, mac, ios, voyzsession, …, support) | deutsche Seite + ihre `en:`-Tabelle | **erzeugt** von `tools/build-i18n.py` |
| AGB, Datenschutz, Impressum, Widerruf, Security, Open Source | `x.html` und `x-en.html` von Hand | keine (siehe Rechtsseiten) |
| Changelog, Presse, Videos, Lizenz verwalten | eine Datei, DE/EN per JS | keine: FR/ES/IT/PT lesen die englische Fassung |
| 404 | `404.html` | Menü führt auf die Startseiten |
| `activate.html` | Weiterleitung aus der Lizenz-Mail, ohne Kopfzeile | bekommt kein Menü |

Texte für FR/ES/IT/PT-BR stehen in `tools/i18n/<sprache>.json`. Der Schlüssel
ist der **deutsche Text**. Ändert sich ein deutscher Satz, findet der Generator
keine Übersetzung mehr. Er setzt dann die englische Fassung ein und meldet die
Stelle. Eine Sprachfassung kann so nie still eine alte Version oder einen alten
Preis zeigen.

## Arbeitsablauf

```bash
python3 tools/build-i18n.py            # alles erzeugen
python3 tools/build-i18n.py --check    # Drift? (Exit 1)
python3 tools/check-links.py           # 404, Menü, hreflang, Download-Links
```

**Release (Download-Links):** Links nur in den deutschen Seiten umstellen
(`index.html`, `mac.html`), dann `python3 tools/build-i18n.py`. Wer weiter per
`sed` auch `en.html`/`mac-en.html` anfasst, muss das Skript trotzdem laufen
lassen. `check-links.py` meldet, wenn eine Sprache eine andere DMG-Version zeigt.

**Spezifikationslisten** (`<li><b>Label</b> Wert</li>`, ohne `data-i18n`): deutsche Labels und Werte
kommen nach `SPEC_EN` in `tools/i18n_en.py`, die Übersetzung in `<sprache>.json`.

**Neuer Text auf einer Produktseite:** deutsch in die Seite und die `de:`-Tabelle,
englisch in die `en:`-Tabelle, dann `python3 tools/build-i18n.py --export`. In
`source.json` stehen danach alle Texte (Exportdatei, nicht eingecheckt). Die Übersetzungen kommen in
`<sprache>.json`.

## Gegenlesen durch Muttersprachler

`gegenlesen-<sprache>.csv` (UTF-8, Komma-getrennt, öffnet in Numbers, Google
Sheets und Excel). Spalten: Seiten, Art, Deutsch (Original), English (Referenz),
Entwurf, Hinweis zum Entwurf, **Korrektur**, Anmerkung, `pruefung` (Ergebnis der
Vorprüfung: ok / korrigiert / UNSICHER + Grund), `quelle` (Beleg aus lokalisierten DAWs).
Bericht zur Vorprüfung: `PRUEFBERICHT.md`.
Der Muttersprachler füllt nur **Korrektur**, und auch nur dort, wo der Entwurf
falsch oder holprig ist. Zurückholen:

```bash
python3 tools/build-i18n.py --import-review fr gegenlesen-fr.csv
python3 tools/build-i18n.py
```

`--review` schreibt die CSVs neu und behält schon eingetragene Korrekturen.

Art `text (HTML)`: Tags wie `<strong>` und `<br>` müssen stehen bleiben.
Produktnamen (voyzSESSION, loudness METER PRO, …) und Normen (EBU R128, LUFS)
werden nicht übersetzt. Namen fremder Hersteller und „Mute-O-Matic“ dürfen nicht
vorkommen.

## Rechtsseiten: Vorschlag (Entscheidung beim Nutzer)

Nicht übersetzt. Vorschlag, so wie gebaut:

1. **Deutsch ist verbindlich.** So steht es schon heute in jeder englischen
   Rechtsseite („The German version of this document is legally binding.“).
2. **Englisch bleibt Lesefassung** wie bisher.
3. **FR/ES/IT/PT verlinken im Fuß auf die englische Lesefassung.** Im Sprachmenü
   der Rechtsseiten steht hinter Français usw. „page en anglais“.

Alternativen: Fuß-Links auf die deutsche Fassung (verbindlich, aber für die
meisten Leser unlesbar), oder echte Übersetzungen durch einen Fachübersetzer
oder Anwalt (Kosten, dafür verständlich für Verbraucher im jeweiligen Land).
Der Widerruf für Verbraucher in FR/ES/IT läuft beim Direktkauf über Paddle als
Merchant of Record. Ob das reicht, ist eine Rechtsfrage und keine Website-Frage.
