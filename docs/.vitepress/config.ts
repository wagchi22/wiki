import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Guia de Bolso",
  description: "Guia de Bolso",
  base: '/guia-de-bolso/', 
  
  // URLs limpas
  cleanUrls: true,

  themeConfig: {
    // ATIVA A BUSCA NATIVA DO VITEPRESS
    search: {
      provider: 'local'
    },

    outline: {
      label: 'Nesta página'
    },

    nav: [
      { text: 'Início', link: '/' }
    ],
    
    sidebar: [
      {
        text: 'Guias',
        collapsed: false, // Menu retrátil
        items: [
          { text: 'Ajustes Gerais', link: '/ajustes-gerais' },
          { text: 'Configurar Servidor de Mídia', link: '/criando-servidor-midia' },
        ]
      }
    ],

    // Link para editar no GitHub
    editLink: {
      pattern: 'https://github.com/wagchi22/meus-arquivos/edit/main/docs/:path',
      text: 'Edite essa página no GitHub'
    },
    
    docFooter: {
      prev: false,
      next: false,
    }
  },

  // Numeração de linhas no código
  markdown: {
    lineNumbers: true,
  }
})
