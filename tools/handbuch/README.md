# Online-Handbuch voyzSESSION PRO

Angelegt 19.11.2026. Live unter `/voyzsession-handbuch/` (de), `/voyzsession-handbuch-en/` (en),
`/fr|es|it|pt/voyzsession-handbuch/`.

## Was wo liegt

| Datei | Zweck |
|---|---|
| `tools/handbuch/<sprache>.md` | **Die Quelle.** Ein Markdown je Sprache (de, en, fr, es, it, pt), gleiche Gliederung |
| `tools/handbuch/template.html` | Seite mit Inhaltsverzeichnis, Suche, Blaettern, Sprachwahl. Sprachneutral, Texte kommen aus dem Generator |
| `tools/build-handbuch.py` | Erzeugt aus Quelle + Vorlage je Sprache `index.html` und `content.json`. Oberflaechentexte der Seite (Suche, Zurueck/Weiter, Startseite) stehen dort in der Tabelle `S` |
| `voyzsession-handbuch/img/` | Bilder, einmal fuer alle Sprachen (absolut verlinkt) |
| `voyzsession-handbuch*/`, `<lang>/voyzsession-handbuch/` | **Erzeugt, nicht von Hand aendern** |

## Aendern

1. Text in `tools/handbuch/de.md` aendern, **dieselbe Stelle in den anderen fuenf Sprachen**.
2. `python3 tools/build-handbuch.py` (braucht pandoc). Bricht ab, wenn eine Sprache eine andere Gliederung hat.
3. `python3 tools/check-links.py`, dann committen. Push auf `main` = live (Cloudflare Pages).

## Regeln fuer die Quelle

- `## <Nr> Titel` = Kapitel, `### <Nr> Titel` = Thema. Erstes und letztes Kapitel ohne Nummer (Vorwort, Anhang).
  Die IDs (`k9-3`, `anhang-c`) entstehen aus den Nummern; Querverweise schreiben `[Text](#k12-5)`.
- Bilder: `[[IMG:datei.png|Bildunterschrift]]` auf eigener Zeile.
- **Bezeichnungen von Knoepfen und Menues so, wie die App sie in der jeweiligen Sprache zeigt.** Nachschlagen in
  `satk-overdub-studio/Source/Localization/Tables/LangTable_DE.h` (deutsch -> englischer Schluessel), dann denselben
  Schluessel in `LangTable_<XX>.h`. Fest verdrahtete Texte (MESSEN, Rescan plugins..., Rename...) stehen so, wie die App sie zeigt.
- Inhalt nur aus dem Code belegen, nicht aus Notizen (Regel aus `satk-overdub-studio/CLAUDE.md`).
- Keine Gedankenstriche, Mittelpunkte, Pfeile; "..." statt Auslassungszeichen; Minus als "-". Keine KI-typischen Wendungen.
- Produktname immer `voyzSESSION PRO`. Ausnahme: Geraetenamen, wie macOS sie zeigt (`voyzSESSION Send`, `voyzSESSION Return`, Kamera `voyzSESSION`).
- Anrede: de "Sie" (Website duzt, offen), en "you", fr "vous", es "tu", it "tu", pt dritte Person.
- Fett = Bedienelement; in Tabellen keine Fettschrift (setzt der Generator).

## Offen (Stand 19.11.2026)

- Sechs Bildschirmfotos fehlen (Hauptfenster VIDEO, Script Editor, Seite EDIT, Zeitleiste nach AUTO MIX, Mixer, Export-Fenster).
  Liste und Plaetze: `satk-overdub-studio/UEBERGABE-2026-11-19-HANDBUCH.md`.
- macOS-Systemeinstellungspfade in fr/it/pt nicht gegen ein echtes macOS geprueft.
- Modulbilder zeigen die deutsche Oberflaeche.
