# satk-website — Claude Context

Statische Marketing-Site für pegelWERK. Reine HTML/CSS/JS,
kein Build, kein Framework.

> **Brand-Rebrand SATK zu pegelWERK (seit 2026-05-29):** Alle sichtbaren
> Texte, Logos, Favicons und Marken-URLs (canonical/og/Links/E-Mail) sind
> auf pegelWERK bzw. pegelwerk.com umgestellt. **Noch NICHT umgestellt
> (bewusst, bis DNS-Cutover):** Live-Domain ist weiterhin `satk.tech`,
> der Download-Host `download.satk.tech`, der Worker-Endpoint
> `satk-license-worker.weathered-lake-eea9.workers.dev`, das CF-Pages-
> Projekt `satk-website`, sowie alle nicht-sichtbaren Bezeichner: Apple-
> Bundle-IDs `com.satk.*`, CSS-Klassen/JS-Vars `satk-*`/`_satkAC`,
> Datei-Formate `.satkip`/`.satkproj`, App-URL-Schemes `easyeditor://`/
> `instantplayer://`, Paddle-Price-IDs. Diese NICHT anfassen, sonst
> bricht Shop/Lizenz/Deploy.

> **Komplementärer Web-/Backend-Chat-Hub:** Das Repo `satk-license-worker`
> (`SATK-Broadcast-Tools/satk-license-worker`) hat den vollen Operator-
> Kontext (Architektur, Lizenz-API, Recovery-Pfade). Bei allem was über
> reines Frontend-Editing hinausgeht: dort lesen.

---

## Hosting & Deploy

- **Plattform:** Cloudflare Pages (Projekt-Name `satk-website`,
  verbunden mit diesem GitHub-Repo)
- **Auto-Deploy:** jeder Push auf `main` triggert Build + Live-Deploy
  auf https://satk.tech (~30–60 Sek)
- **Preview-Deploys:** jeder Branch außer `main` bekommt automatisch
  eine `<branch>.satk-website.pages.dev`-URL — perfekt für Reviews
  bevor `main` aktualisiert wird
- **Build:** keine Build-Schritte nötig (statische Files), CF Pages
  serviert die Repo-Root direkt
- **Rollback:** im CF Pages Dashboard → Deployments → Klick auf
  früheres Deployment → „Rollback to this deployment" (1-Klick)

**Was es nicht mehr gibt** (alte IONOS-Pipeline, abgeschaltet 2026-05-08):
- Kein `deploy.sh`-ZIP-Upload
- Kein FTP zu IONOS
- Keine `.htaccess` (durch `_headers` + `_redirects` ersetzt)

## Architektur

- **HTML-Struktur:** alle Seiten direkt im Repo-Root (`index.html`,
  `<produkt>.html`)
- **Browser-Tools** (`audio-editor.html`, `podcast-recorder.html`,
  `r128-normalizer.html`, …) werden von `tools.html` als
  **same-origin iframes** eingebettet — daher `frame-src 'self'`,
  `frame-ancestors 'self'`, `X-Frame-Options: SAMEORIGIN`
- **AudioWorklet im Podcast-Recorder** lädt aus blob:-URL → daher
  `worker-src 'self' blob:`. Audio-Playback aus blob → `media-src
  'self' blob:`
- **Lizenz-Backend:** separates Repo `satk-license-worker` (CF Worker
  unter `satk-license-worker.weathered-lake-eea9.workers.dev`)
- **Checkout:** Paddle (Inline-Popup, lädt erst beim Klick)
- **Self-Service-Portal:** `manage-license.html` ruft den Worker via
  `connect-src` (CSP-Whitelist drin)
- **Analytics:** Plausible (privacy-friendly, lokales JS-Snippet aus
  satk.tech, Datenfluss zu plausible.io)

## Wichtige Files

| File | Zweck |
|---|---|
| `_headers` | Security-Header (HSTS, CSP, X-Frame, COOP, …) + Cache-Control nach Asset-Typ — **nur CF Pages liest das** |
| `_redirects` | Pretty-URL-Mapping (`.html` → ohne Extension via 301) — **nur CF Pages liest das** |
| `index.html` | Homepage (Hero, Highlights, Trust-Block, Newsletter) |
| `tools.html` | Browser-Tools-Hub (iframet die Tool-Pages) |
| `manage-license.html` | Self-Service-Portal (Lookup/Resend/Deactivate) |
| `changelog.html` | Release-Notes (LC-Slot vorbereitet als HTML-Kommentar) |
| `<produkt>.html` | Marketing-Seiten pro Produkt (BM, OD, LC, …) |
| `<produkt>-pro.html` | Pro-Versionen mit Pricing/Paddle-Checkout |
| `agb.html`, `datenschutz.html`, `impressum.html`, `widerruf.html` | Rechtliches (DE) |
| `agb-en.html`, `widerruf-en.html` | Englische Pendants |
| `fonts.css` + `fonts/` | Lokale Font-Files (kein Google-Fonts-CDN, DSGVO) |

## Konventionen

- **Keine Frameworks, keine Build-Pipeline.** Reines HTML/CSS/JS,
  damit der Stack langfristig wartbar bleibt
- **i18n via `data-i18n`-Attribute** + JS-Switch im `<head>` jeder Seite
- **Kein Inline-Style** wenn vermeidbar (CSP `style-src 'self'
  'unsafe-inline'` ist locker, aber Konvention ist class-based)
- **Bilder als WebP** (98% kleinere Files als PNG, alle Browser
  unterstützen es seit Jahren)
- **Pretty-URLs:** intern verlinken auf `/<seite>` (ohne `.html`),
  `_redirects` macht 301 für `.html`-Variante

## Bei Änderungen am API-Vertrag (Worker-Endpoints / Token-Format)

→ Master-Spec in `satk-license-worker/LICENSING.md` zuerst ändern,
dann Spiegel in `satk-broadcastmeter/LICENSING.md`,
`satk-overdub-studio/LICENSING.md`, etc.
Frontend hier **darf nicht** vorpreschen.

## Pfade pro Mac

| Mac | Pfad |
|---|---|
| Mobil-Laptop | `~/Documents/SATK/satk-website` |
| Hauptrechner | `/Volumes/Recording/satk-website` |
