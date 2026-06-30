``` javascript
// ==UserScript==
// @name         BLUDV Bypass
// @description  Pula os anúncios ao fazer download no site do BLUDV
// @version      2026-06-17
// @match        *://*.systemads.xyz/*
// @match        *://*.systemads.net/*
// @match        *://*.autotop.net/*
// @match        *://*.celomoda.com/*
// @match        *://*.solucoescreditos.com/*
// @match        *://*.redirecionandovoce.info/*
// @match        *://*moneyaide.com/*
// @match        *://*redirectad.net/*
// @match        *://*.videosad.net/*
// @match        *://*videosad.net/*
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    const hideCSS = document.createElement('style');
    hideCSS.id = 'bludv-bypass-hide';
    hideCSS.textContent = 'html { background-color: #ffffff !important; } body { display: none !important; opacity: 0 !important; visibility: hidden !important; }';
    document.documentElement.appendChild(hideCSS);

    let timeoutId;

    const performRedirect = (url) => {
        window.stop();
        window.location.replace(url);
    };

    const tryDecodeAndRedirect = (data) => {
        if (!data) return false;
        try {
            const m = atob(data);
            if (m.startsWith('magnet:')) {
                performRedirect(m);
                return true;
            }
        } catch (e) {}
        return false;
    };

    const check = () => {
        const htmlMatch = document.documentElement.innerHTML.match(/(magnet:\?xt=urn:btih:[^"'\\]+)/);
        if (htmlMatch) {
            performRedirect(htmlMatch[1]);
            return true;
        }

        const data = document.querySelector('[data-download]')?.dataset.download || document.body?.dataset.download;
        if (tryDecodeAndRedirect(data)) return true;

        const magnetLink = document.querySelector('a[href^="magnet:"]')?.href;
        if (magnetLink) {
            performRedirect(magnetLink);
            return true;
        }

        const elements = document.querySelectorAll('input, button, a, [data-url], [data-href], [data-link]');
        for (let el of elements) {
            const val = el.value || el.dataset.url || el.dataset.href || el.dataset.link;
            if (tryDecodeAndRedirect(val)) return true;
        }

        return false;
    };

    const obs = new MutationObserver(() => {
        if (check()) {
            obs.disconnect();
            clearTimeout(timeoutId);
        }
    });

    obs.observe(document.documentElement, {childList: true, subtree: true, attributes: true});

    window.addEventListener('DOMContentLoaded', () => {
        if (!check()) {
            const interval = setInterval(() => {
                if (check()) clearInterval(interval);
            }, 500);

            timeoutId = setTimeout(() => {
                clearInterval(interval);
                obs.disconnect();
                const styleTag = document.getElementById('bludv-bypass-hide');
                if (styleTag) styleTag.remove();
            }, 4000);
        }
    });
})();
```
