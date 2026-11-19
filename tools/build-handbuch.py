#!/usr/bin/env python3
"""Erzeugt das Online-Handbuch zu voyzSESSION PRO in allen Sprachen.

Quellen:   tools/handbuch/<sprache>.md   (ein Markdown je Sprache, gleiche Gliederung)
           tools/handbuch/template.html  (Seite mit Inhaltsverzeichnis, Suche, Blaettern)
Ergebnis:  voyzsession-handbuch/            (de)
           voyzsession-handbuch-en/         (en)
           fr|es|it|pt/voyzsession-handbuch/
           je index.html + content.json; die Bilder liegen einmal in voyzsession-handbuch/img/

Aufbau einer Quelle: "## <Nr> Titel" ist ein Kapitel, "### <Nr> Titel" ein Thema.
Das erste und das letzte Kapitel tragen keine Nummer (Vorwort, Anhang).
Bilder: [[IMG:datei.png|Bildunterschrift]]. Querverweise: [Text](#k12-5).

AUFRUF (im Wurzelverzeichnis des Repos):  python3 tools/build-handbuch.py
Braucht pandoc.
"""
import html, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "handbuch")
IMG = "/voyzsession-handbuch/img/"

LANGS = {
    "de": dict(dir="voyzsession-handbuch", base="/voyzsession-handbuch/", html="de", name="Deutsch",
               product="/voyzsession", support="/support"),
    "en": dict(dir="voyzsession-handbuch-en", base="/voyzsession-handbuch-en/", html="en", name="English",
               product="/voyzsession-en", support="/support-en"),
    "fr": dict(dir="fr/voyzsession-handbuch", base="/fr/voyzsession-handbuch/", html="fr", name="Français",
               product="/fr/voyzsession", support="/fr/support"),
    "es": dict(dir="es/voyzsession-handbuch", base="/es/voyzsession-handbuch/", html="es", name="Español",
               product="/es/voyzsession", support="/es/support"),
    "it": dict(dir="it/voyzsession-handbuch", base="/it/voyzsession-handbuch/", html="it", name="Italiano",
               product="/it/voyzsession", support="/it/support"),
    "pt": dict(dir="pt/voyzsession-handbuch", base="/pt/voyzsession-handbuch/", html="pt-PT", name="Português",
               product="/pt/voyzsession", support="/pt/support"),
}

# Texte der Seite selbst (Kopf, Startseite, Suche, Blaettern)
S = {
 "de": dict(title="voyzSESSION PRO Benutzerhandbuch", manual="Benutzerhandbuch", toc="Inhalt", toc_long="Inhaltsverzeichnis",
   home_aria="Startseite des Handbuchs", search="Handbuch durchsuchen", search_short="Suchen", loading="Handbuch wird geladen...",
   load_error="Der Inhalt konnte nicht geladen werden. Bitte die Seite neu laden.", toggle="auf- oder zuklappen",
   paging="Blättern", prev="Zurück", next="Weiter", chapter="Kapitel", reference="Nachschlagen", topics="Themen",
   version="Version 2.0 für macOS", tagline="Aufnehmen, schneiden und mischen für Voice-over, Synchron, Podcast, Hörbuch und Radio.",
   first_steps="Erste Schritte", start=["Projekt anlegen und speichern", "Mikrofon einpegeln", "Erste Aufnahme", "AUTO MIX starten", "Exportieren"],
   product="Produktseite und Download", support="Supportanfrage", site_link="voyzSESSION PRO auf pegelwerk.com",
   in_chapter="In diesem Kapitel", overview="Kapitelübersicht", show_all="Alle %n Treffer anzeigen",
   no_hits="Keine Treffer für „%q“.", search_title="Suche: „%q“", hits="Treffer", lang="Sprache",
   desc="Online-Handbuch zu voyzSESSION PRO 2.0 für macOS: Aufnehmen, Schneiden, AUTO MIX, Manual-Modus, Klangmodule, Export und Fernvertonung. Mit Suche und Inhaltsverzeichnis."),
 "en": dict(title="voyzSESSION PRO User Guide", manual="User Guide", toc="Contents", toc_long="Table of contents",
   home_aria="Start page of the guide", search="Search the guide", search_short="Search", loading="Loading the guide...",
   load_error="The content could not be loaded. Please reload the page.", toggle="expand or collapse",
   paging="Page navigation", prev="Previous", next="Next", chapter="Chapter", reference="Reference", topics="topics",
   version="Version 2.0 for macOS", tagline="Record, edit and mix voice-over, dubbing, podcasts, audiobooks and radio.",
   first_steps="Getting started", start=["Create and save a project", "Set the microphone level", "First recording", "Start AUTO MIX", "Export"],
   product="Product page and download", support="Support request", site_link="voyzSESSION PRO on pegelwerk.com",
   in_chapter="In this chapter", overview="Chapter overview", show_all="Show all %n results",
   no_hits="No results for “%q”.", search_title="Search: “%q”", hits="results", lang="Language",
   desc="Online user guide for voyzSESSION PRO 2.0 for macOS: recording, editing, AUTO MIX, Manual mode, sound modules, export and remote recording. With search and table of contents."),
 "fr": dict(title="Manuel de voyzSESSION PRO", manual="Manuel", toc="Sommaire", toc_long="Table des matières",
   home_aria="Page d’accueil du manuel", search="Rechercher dans le manuel", search_short="Rechercher", loading="Chargement du manuel...",
   load_error="Le contenu n’a pas pu être chargé. Veuillez recharger la page.", toggle="déplier ou replier",
   paging="Navigation", prev="Précédent", next="Suivant", chapter="Chapitre", reference="Référence", topics="rubriques",
   version="Version 2.0 pour macOS", tagline="Enregistrer, monter et mixer voix off, doublage, podcasts, livres audio et radio.",
   first_steps="Premiers pas", start=["Créer et enregistrer un projet", "Régler le niveau du micro", "Premier enregistrement", "Lancer AUTO MIX", "Exporter"],
   product="Page produit et téléchargement", support="Demande d’assistance", site_link="voyzSESSION PRO sur pegelwerk.com",
   in_chapter="Dans ce chapitre", overview="Vue d’ensemble du chapitre", show_all="Afficher les %n résultats",
   no_hits="Aucun résultat pour « %q ».", search_title="Recherche : « %q »", hits="résultats", lang="Langue",
   desc="Manuel en ligne de voyzSESSION PRO 2.0 pour macOS : enregistrement, montage, AUTO MIX, mode Manual, modules sonores, export et enregistrement à distance. Avec recherche et sommaire."),
 "es": dict(title="Manual de voyzSESSION PRO", manual="Manual", toc="Contenido", toc_long="Índice",
   home_aria="Página de inicio del manual", search="Buscar en el manual", search_short="Buscar", loading="Cargando el manual...",
   load_error="No se ha podido cargar el contenido. Vuelve a cargar la página.", toggle="desplegar o plegar",
   paging="Navegación", prev="Anterior", next="Siguiente", chapter="Capítulo", reference="Consulta", topics="temas",
   version="Versión 2.0 para macOS", tagline="Grabar, editar y mezclar locución, doblaje, pódcast, audiolibros y radio.",
   first_steps="Primeros pasos", start=["Crear y guardar un proyecto", "Ajustar el nivel del micrófono", "Primera grabación", "Iniciar AUTO MIX", "Exportar"],
   product="Página del producto y descarga", support="Solicitud de soporte", site_link="voyzSESSION PRO en pegelwerk.com",
   in_chapter="En este capítulo", overview="Resumen del capítulo", show_all="Mostrar los %n resultados",
   no_hits="No hay resultados para «%q».", search_title="Búsqueda: «%q»", hits="resultados", lang="Idioma",
   desc="Manual en línea de voyzSESSION PRO 2.0 para macOS: grabación, edición, AUTO MIX, modo Manual, módulos de sonido, exportación y grabación a distancia. Con búsqueda e índice."),
 "it": dict(title="Manuale di voyzSESSION PRO", manual="Manuale", toc="Indice", toc_long="Indice dei contenuti",
   home_aria="Pagina iniziale del manuale", search="Cerca nel manuale", search_short="Cerca", loading="Caricamento del manuale...",
   load_error="Impossibile caricare il contenuto. Ricarica la pagina.", toggle="espandi o comprimi",
   paging="Navigazione", prev="Indietro", next="Avanti", chapter="Capitolo", reference="Consultazione", topics="argomenti",
   version="Versione 2.0 per macOS", tagline="Registrare, montare e mixare voice-over, doppiaggio, podcast, audiolibri e radio.",
   first_steps="Primi passi", start=["Creare e salvare un progetto", "Regolare il livello del microfono", "Prima registrazione", "Avviare AUTO MIX", "Esportare"],
   product="Pagina del prodotto e download", support="Richiesta di supporto", site_link="voyzSESSION PRO su pegelwerk.com",
   in_chapter="In questo capitolo", overview="Panoramica del capitolo", show_all="Mostra tutti i %n risultati",
   no_hits="Nessun risultato per «%q».", search_title="Ricerca: «%q»", hits="risultati", lang="Lingua",
   desc="Manuale online di voyzSESSION PRO 2.0 per macOS: registrazione, montaggio, AUTO MIX, modalità Manual, moduli audio, esportazione e registrazione a distanza. Con ricerca e indice."),
 "pt": dict(title="Manual do voyzSESSION PRO", manual="Manual", toc="Índice", toc_long="Índice",
   home_aria="Página inicial do manual", search="Pesquisar no manual", search_short="Pesquisar", loading="A carregar o manual...",
   load_error="Não foi possível carregar o conteúdo. Volte a carregar a página.", toggle="expandir ou recolher",
   paging="Navegação", prev="Anterior", next="Seguinte", chapter="Capítulo", reference="Consulta", topics="temas",
   version="Versão 2.0 para macOS", tagline="Gravar, editar e misturar locução, dobragem, podcasts, audiolivros e rádio.",
   first_steps="Primeiros passos", start=["Criar e guardar um projeto", "Ajustar o nível do microfone", "Primeira gravação", "Iniciar o AUTO MIX", "Exportar"],
   product="Página do produto e download", support="Pedido de suporte", site_link="voyzSESSION PRO em pegelwerk.com",
   in_chapter="Neste capítulo", overview="Visão geral do capítulo", show_all="Mostrar os %n resultados",
   no_hits="Sem resultados para «%q».", search_title="Pesquisa: «%q»", hits="resultados", lang="Idioma",
   desc="Manual online do voyzSESSION PRO 2.0 para macOS: gravação, edição, AUTO MIX, modo Manual, módulos de som, exportação e gravação à distância. Com pesquisa e índice."),
}
START_IDS = ["k3-1", "k3-3", "k3-5", "k7-2", "k12-1"]


def to_html(md):
    out = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
                         input=md, capture_output=True, text=True, check=True).stdout
    out = out.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    # einheitlicher Satz: in Tabellen keine Fettschrift, Stichwort am Anfang eines Listenpunkts fett
    out = re.sub(r"(<table>.*?</table>)", lambda m: re.sub(r"</?strong>", "", m.group(1)), out, flags=re.S)
    out = re.sub(r"<li>(?!<strong>)([A-ZÀ-Ý][^<:]{1,38}):\s", r"<li><strong>\1:</strong> ", out)
    return out.strip()


def figure(m):
    f, cap = m.group(1).strip(), html.escape(m.group(2).strip())
    return (f'<figure class="fig module"><img src="{IMG}{f}" alt="{cap}" loading="lazy">'
            f'<figcaption>{cap}</figcaption></figure>')


def plain(h):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def parse(md):
    md = re.sub(r"(?m)^\[\[IMG:([^|\]]+)\|([^\]]*)\]\]\s*$", lambda m: "\n" + figure(m) + "\n", md)
    blocks = re.split(r"(?m)^## ", md)[1:]
    chapters = []
    for n, block in enumerate(blocks):
        head, _, rest = block.partition("\n")
        m = re.match(r"(\d+) (.*)", head.strip())
        num, title = (m.group(1), m.group(2)) if m else ("", head.strip())
        cid = "k" + num if num else ("k0" if n == 0 else "anhang")
        parts = re.split(r"(?m)^### ", rest)
        ch = {"id": cid, "num": num, "title": title, "intro": to_html(parts[0]), "topics": []}
        for i, p in enumerate(parts[1:], 1):
            th, _, tb = p.partition("\n")
            tm = re.match(r"(\d+\.\d+|[A-Z]) (.*)", th.strip())
            tnum, ttitle = (tm.group(1), tm.group(2)) if tm else ("", th.strip())
            if "." in tnum:
                tid = "%s-%s" % (cid, tnum.split(".")[1])
            elif tnum:
                tid = "%s-%s" % (cid, tnum.lower())
            else:
                tid = "%s-%d" % (cid, i)
            ch["topics"].append({"id": tid, "num": tnum, "title": ttitle, "html": to_html(tb)})
        ch["text"] = plain(ch["intro"])
        for t in ch["topics"]:
            t["text"] = plain(t["html"])
        chapters.append(ch)
    return chapters


def main():
    tpl = open(os.path.join(SRC, "template.html"), encoding="utf-8").read()
    ref_ids = None
    hreflang = "\n".join('<link rel="alternate" hreflang="%s" href="https://pegelwerk.com%s">' % (l if l != "pt" else "pt", c["base"])
                         for l, c in LANGS.items())
    hreflang += '\n<link rel="alternate" hreflang="x-default" href="https://pegelwerk.com%s">' % LANGS["en"]["base"]
    for lang, cfg in LANGS.items():
        path = os.path.join(SRC, lang + ".md")
        if not os.path.exists(path):
            print("  %s: keine Quelle, uebersprungen" % lang)
            continue
        chapters = parse(open(path, encoding="utf-8").read())
        ids = [c["id"] for c in chapters] + [t["id"] for c in chapters for t in c["topics"]]
        if ref_ids is None:
            ref_ids = ids
        elif ids != ref_ids:
            sys.exit("%s: Gliederung weicht von der ersten Sprache ab (%d statt %d Eintraege)" % (lang, len(ids), len(ref_ids)))
        s = S[lang]
        L = dict(s)
        L["start_links"] = list(zip(START_IDS, s["start"]))
        L["product_url"], L["support_url"] = cfg["product"], cfg["support"]
        del L["start"]
        langs = " ".join('<a href="%s" hreflang="%s"%s>%s</a>' % (c["base"], l, ' class="cur" aria-current="true"' if l == lang else "", c["name"])
                         for l, c in LANGS.items())
        page = tpl
        for k, v in s.items():
            if isinstance(v, str):
                page = page.replace("{{S:%s}}" % k, html.escape(v, quote=True))
        page = (page.replace("{{HTML_LANG}}", cfg["html"]).replace("{{BASE}}", cfg["base"])
                    .replace("{{TITLE}}", html.escape(s["title"])).replace("{{DESC}}", html.escape(s["desc"], quote=True))
                    .replace("{{HREFLANG}}", hreflang).replace("{{PRODUCT}}", cfg["product"]).replace("{{SUPPORT}}", cfg["support"])
                    .replace("{{LANGS}}", langs)
                    .replace("{{L_JSON}}", json.dumps(L, ensure_ascii=False).replace("</", "<\\/")))
        left = re.findall(r"\{\{[^}]+\}\}", page)
        if left:
            sys.exit("%s: Platzhalter offen: %s" % (lang, left))
        out = os.path.join(ROOT, cfg["dir"])
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
        json.dump({"chapters": chapters}, open(os.path.join(out, "content.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"))
        print("  %s: %d Kapitel, %d Themen -> %s/" % (lang, len(chapters), sum(len(c["topics"]) for c in chapters), cfg["dir"]))


if __name__ == "__main__":
    main()
