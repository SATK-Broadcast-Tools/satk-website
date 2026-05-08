# Handover — CF Pages Migration aktiv

**Datum:** 2026-05-08
**Status:** mitten in der Migration, Web-Chat auf Mobil-Laptop wird auf
Hauptrechner-Chat übergeben weil Dashboard-Navigation einfacher ist
wenn Chat + Browser auf demselben Mac sind.

---

## Akuter Anlass (Vormittag 2026-05-08)

`satk.tech` ist seit heute morgen **sehr langsam (5+ Sek pro Anfrage)
und schwankend bis nicht erreichbar**. Heute morgen wurden HTML-Seiten
als Download statt gerendert ausgeliefert — typisches Symptom wenn
Cloudflare-Origin-Timeout eintritt und der Browser keinen Content-Type
mehr bekommt.

## Diagnose-Ergebnis

```
cf-cache-status: DYNAMIC      ← Cloudflare cached HTML NICHT
vary: Accept-Encoding,Cookie  ← IONOS-Apache setzt session-cookies pro Visitor
                                 → jede Anfrage = neuer Cache-Key
                                 → faktisch zero edge-cache-hits
                                 → jede Anfrage geht zu IONOS-Origin
                                 → dort hängt's bei 5+ Sek
```

Page Rule „Cache Everything" wurde aktiviert (4h Edge TTL), greift aber
nicht weil `Vary: Cookie` von IONOS jede Anfrage uniqe macht. Dieses
IONOS-Apache-Verhalten ist auf Shared-Webhosting nicht zuverlässig
abschaltbar.

## Entscheidung

**Migration zu Cloudflare Pages** — kostenlos, eliminiert IONOS
komplett aus dem Pfad, edge-cached automatisch global. Weitere
Begründung in Chat-Historie auf Mobil-Laptop.

---

## Was schon erledigt ist (auf GitHub committed)

**Commit `e4a34bb`** auf `main` Branch von `satk-website`:

- **`_redirects`** — Pretty-URL-Mapping (alle `.html` → ohne Extension via 301)
- **`_headers`** — komplette Security-Header-Suite und Cache-Control:
  - HSTS (preload), X-Frame-Options DENY, CSP mit Plausible+Worker
  - Referrer-Policy strict-origin-when-cross-origin
  - COOP same-origin-allow-popups
  - Cache-Control nach Asset-Typ (Bilder 30d, CSS/JS 7d, HTML 1h, Fonts 30d immutable)

Beide Dateien sind CF-Pages-spezifisch und werden von IONOS-Apache
ignoriert — laufen also parallel zur `.htaccess` bis zum DNS-Cutover.

## Was als Nächstes zu tun ist

### Schritt 1 — Pages-Projekt erstellen (auf Hauptrechner)

User stockte beim Finden von „Pages" im CF-Dashboard. **Direkt-Link:**
```
https://dash.cloudflare.com/?to=/:account/workers-and-pages
```

Auf Workers & Pages-Übersicht:
1. Tab **Pages**
2. Button **„Create application"** → Tab **„Connect to Git"**
3. **Connect GitHub** (einmalige OAuth-Autorisierung für `SATK-Broadcast-Tools`)
4. Repo auswählen: **`satk-website`** → **„Begin setup"**
5. Setup-Formular:
   - Project name: `satk-website`
   - Production branch: `main`
   - Framework preset: **None**
   - Build command: leer
   - Build output directory: leer
   - Root directory: leer
   - Environment variables: keine
6. **„Save and Deploy"** — CF baut 30-60 Sek
7. Preview-URL erscheint: `satk-website-XXX.pages.dev`

### Schritt 2 — Preview testen

Web-Chat (auf Hauptrechner) testet alle wichtigen URLs auf der
Preview-Domain durch:

- Hauptseite (sollte HTML korrekt rendern, nicht downloaden)
- Pretty-URLs: `/manage-license`, `/support`, `/broadcast-meter-pro`,
  `/loudness-correct`, `/changelog`
- HTML-Header korrekt (CSP, HSTS, COOP) via curl -I prüfen
- Plausible-Tag aktiv (Network-Tab im Browser zeigt
  `plausible.io/js/pa-...js`)
- Self-Service-Portal ruft Worker auf: Lookup mit Test-Lizenz
  `lic_d6dcbb56...` und Email `s.hoemske@icloud.com` muss 200 + Lizenz
  zurückgeben (verifiziert dass CSP `connect-src` durchlässt)
- Trust-Block auf BM-Page korrekt formatiert
- Changelog-Slot LC ist noch im HTML-Kommentar (vorbereitet, nicht aktiv)

### Schritt 3 — Custom Domain hinzufügen

Nach erfolgreichem Test:

1. CF Pages-Projekt → **Custom domains** → **„Set up a custom domain"**
2. Domain: `satk.tech`
3. CF zeigt nötige DNS-Änderung (CNAME-Eintrag)
4. Da DNS schon bei CF liegt, wird der CNAME automatisch eingetragen
   (User klickt nur „Begin DNS transition")
5. Innerhalb 1-2 Min ist `satk.tech` von Pages bedient

Plus: Preview-URL bleibt parallel als Backup.

### Schritt 4 — Verifikation Live

Nach DNS-Switch curl gegen `satk.tech`:

```bash
curl -sI "https://satk.tech/" | grep -E "cf-cache-status|server|content-type"
```

Erwartet jetzt:
- `cf-cache-status: HIT` (oder MISS beim ersten Aufruf, dann HIT)
- `server: cloudflare`
- `content-type: text/html`
- Total-Time: <0.5s statt 5+ Sek

### Schritt 5 — Aufräumen (optional, nach 1-2 Wochen Monitoring)

- IONOS-Webhosting downgraden auf „nur Email"
  (Email-Hosting bleibt unverändert weiter bei IONOS — MX-Records
  unbeeinflusst)
- `.htaccess` und `deploy.sh` aus Repo löschen (nicht mehr benötigt)
- README.md, CLAUDE.md, OPERATOR-RUNBOOK auf neuen Deploy-Flow
  aktualisieren (kein ZIP-Upload mehr, statt dessen `git push` →
  Auto-Deploy)

---

## Wichtige Pfade auf Hauptrechner (für Chat)

Laut Memory + earlier Mobil-Laptop Sessions:

| Was | Pfad auf Hauptrechner |
|---|---|
| satk-website Repo | `/Volumes/Recording/satk-website` |
| satk-license-worker Repo | `/Volumes/Recording/satk-license-worker` |
| ADMIN_SECRET env | `~/.satk-release.env` |

Memory-Files auf Hauptrechner sind eigenständig und enthalten lokale
Pfade plus Lessons.

## Kontext für Hauptrechner-Chat

Falls Memory-Files nicht alles haben — die geteilten Repo-Files (auf
GitHub aktuell) haben den vollen Stand:

- **`satk-license-worker/CLAUDE.md`** — Web-Chat-Hub, Memory-Konventionen,
  Pfade pro Mac
- **`satk-license-worker/OPERATOR-RUNBOOK.md`** — Symptome→Recovery
- **`satk-license-worker/README.md`** — Setup + Deploy
- **`satk-license-worker/LICENSING.md`** — API-Vertrag, Method-Swizzle-Pflicht
- **`satk-loudness-correct/WEBCHAT-BRIEFING-1.0.0.md`** — LC-Release-Vorbereitung,
  wartet auf App-Chat-Ausfüllung

## Was NOCH offen ist (parallel laufende Threads)

1. **LC 1.0.0 Release** — Notarisierung läuft, Briefing-Template steht im
   LC-Repo. Wenn App-Chat das ausfüllt, kann der Web-Chat
   Live-Schaltung in einem Rutsch machen.

2. **OD Live-Aufschaltung** — irgendwann nach LC, gleicher Pattern.

3. **AVV-Sammlung** — Paddle-Vendor-Agreement-Mail vom 2026-05-06 wartet
   auf Antwort.

4. **Paddle API Key Rotation** — Reminder ~2026-08-03.

---

## Sofortige Aktion auf Hauptrechner

1. Diesen Branch pullen (sollte schon current sein):
   ```bash
   cd /Volumes/Recording/satk-website
   git pull origin main
   ```
2. Verifizieren dass `_headers` und `_redirects` da sind:
   ```bash
   ls -la _headers _redirects
   ```
3. CF-Dashboard öffnen via Direkt-Link oben → Pages-Projekt erstellen
4. Preview-URL kommt → an den Hauptrechner-Chat geben
5. Hauptrechner-Chat testet die Preview, dann DNS-Switch

Web-Chat auf Mobil-Laptop kann diesen Branch hier verlassen — Migration
wird vom Hauptrechner-Chat übernommen.
