import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Guia de Bolso",
  description: "Guia de Bolso",
  base: '/guia-de-bolso/', 
  
  cleanUrls: true,

  themeConfig: {
    // Busca nativa configurada em Português
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Pesquisar',
            buttonAriaLabel: 'Pesquisar documentos'
          },
          modal: {
            noResultsText: 'Nenhum resultado encontrado para',
            resetButtonTitle: 'Limpar pesquisa',
            footer: {
              selectText: 'para selecionar',
              navigateText: 'para navegar',
              closeText: 'para fechar'
            }
          }
        }
      }
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
        collapsed: false,
        items: [
          { text: 'Ajustes Gerais', link: '/ajustes-gerais' },
          { text: 'Configurar Servidor de Mídia', link: '/criando-servidor-midia' },
        ]
      }
    ],

    editLink: {
      pattern: 'https://github.com/wagchi22/meus-arquivos/edit/main/docs/:path',
      text: 'Edite essa página no GitHub'
    },
    
    docFooter: {
      prev: false,
      next: false,
    }
  },

  markdown: {
    lineNumbers: true,
  }
})
