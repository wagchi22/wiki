// ==UserScript==
// @name         MEMORIADATV Bypass
// @description  Pula os anúncios do MEMORIADATV
// @version      2026-07-07
// @author       wagchi22
// @match        *://*.memoriadatv.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function removerElemento() {
        const elemento = document.getElementById('arlinablock');
        if (elemento) {
            elemento.remove();
        }
    }

    // Tenta remover imediatamente
    removerElemento();

    // Monitora mutações no DOM caso o elemento seja carregado dinamicamente
    const observer = new MutationObserver(removerElemento);
    observer.observe(document.body, { childList: true, subtree: true });
})();
