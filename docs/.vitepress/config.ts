import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Guia de Bolso",
  description: "Guia de Bolso",
  base: '/guia-de-bolso/', 
  
  themeConfig: {
    outline: {
      label: 'Nesta página'
    },

    nav: [
      { text: 'Início', link: '/' }
    ],
    sidebar: [
      {
        text: 'Guias',
        items: [
          { text: 'Ajustes Gerais', link: '/ajustes-gerais' },
          { text: 'Configurar Servidor de Mídia', link: '/criando-servidor-midia' },
        ]
      }
    ],
    docFooter: {
      prev: false,
      next: false,
    }
  }
})
