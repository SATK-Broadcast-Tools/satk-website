/* Sprachmenue: Knopf + Liste von Links (WAI-ARIA "Disclosure"-Muster, kein role=menu).
   Markup schreibt tools/build-i18n.py. Ein Klick merkt die Wahl in localStorage
   'satk-lang'; das kleine Skript im <head> jeder Seite springt beim naechsten Besuch
   auf die passende Fassung. Seiten mit data-inpage (Changelog, Presse, Videos,
   Lizenz) gibt es nur als EINE Datei mit DE/EN - dort schaltet setLang() der Seite um.
   Nach einer Aenderung ASSET_V in tools/build-i18n.py hochzaehlen. */
(function () {
  'use strict';
  function remember(l) { try { localStorage.setItem('satk-lang', l); } catch (e) {} }

  function init(root) {
    var btn = root.querySelector('.lm-btn');
    var list = root.querySelector('.lm-list');
    var links = Array.prototype.slice.call(list.querySelectorAll('a'));
    var inpage = root.hasAttribute('data-inpage') && typeof window.setLang === 'function';

    function currentIndex() {
      for (var i = 0; i < links.length; i++) if (links[i].getAttribute('aria-current') === 'true') return i;
      return 0;
    }
    function focusAt(i) { links[(i + links.length) % links.length].focus(); }
    function open(i) {
      list.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      if (i !== undefined) focusAt(i);
    }
    function close(returnFocus) {
      if (list.hidden) return;
      list.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
      if (returnFocus) btn.focus();
    }

    // Auf DE/EN-Seiten mit Umschalter im Dokument: Knopf und Markierung folgen <html lang>
    function sync() {
      var l = (document.documentElement.lang || 'de').toLowerCase() === 'en' ? 'en' : 'de';
      var labels = {};
      try { labels = JSON.parse(root.getAttribute('data-labels') || '{}'); } catch (e) {}
      links.forEach(function (a) {
        if (a.getAttribute('data-lang') === l) a.setAttribute('aria-current', 'true');
        else a.removeAttribute('aria-current');
      });
      var code = btn.querySelector('.lm-code'), sr = btn.querySelector('.lm-sr');
      var name = links[currentIndex()].firstChild.nodeValue;
      if (code) code.textContent = l.toUpperCase();
      if (sr) sr.textContent = ' – ' + (labels[l] || 'Language') + ': ' + name;
    }
    if (inpage) {
      sync();
      new MutationObserver(sync).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
    }

    btn.addEventListener('click', function () { list.hidden ? open() : close(false); });
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); open(currentIndex()); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); open(links.length - 1); }
      else if (e.key === 'Escape') { close(true); }
    });
    list.addEventListener('keydown', function (e) {
      var i = links.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); focusAt(i + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); focusAt(i - 1); }
      else if (e.key === 'Home') { e.preventDefault(); focusAt(0); }
      else if (e.key === 'End') { e.preventDefault(); focusAt(links.length - 1); }
      else if (e.key === 'Escape') { e.preventDefault(); close(true); }
    });
    root.addEventListener('focusout', function (e) {
      if (e.relatedTarget && !root.contains(e.relatedTarget)) close(false);
    });
    document.addEventListener('click', function (e) { if (!root.contains(e.target)) close(false); });

    links.forEach(function (a) {
      a.addEventListener('click', function (e) {
        var l = a.getAttribute('data-lang');
        if (inpage) {
          e.preventDefault();
          window.setLang(l === 'de' ? 'de' : 'en');
          remember(l);                  // setLang() der Seite schreibt 'en' - die echte Wahl gewinnt
          close(true);
          return;
        }
        remember(l);
      });
    });
  }

  function start() {
    Array.prototype.forEach.call(document.querySelectorAll('.lm'), init);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
