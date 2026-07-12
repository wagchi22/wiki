// TS sometimes can't locate vitepress types in local setups; ignore the error here
// @ts-ignore
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Wiki",
  description: "Coleção pessoal de coisas úteis.",
  base: '/wiki/', 
  
  cleanUrls: true,
  
  lastUpdated: true,

  themeConfig: {
    lastUpdatedText: "Última atualização em",
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

    // Ícone do GitHub no menu superior
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/wagchi22/wiki",
      },
    ],
    
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
          { text: 'Configurar Servidor de Mídia', link: '/configurar-servidor-midia' },
        ]
      }
    ],

    editLink: {
      pattern: 'https://github.com/wagchi22/wiki/edit/main/docs/:path',
      text: 'Edite essa página no GitHub'
    },
    
    docFooter: {
      prev: false,
      next: false,
    },

    // Configurações Mobile (Corrigidas para dentro de themeConfig)
    returnToTopLabel: "Voltar ao topo",
    sidebarMenuLabel: "Menu"
  },

  markdown: {
    attrs: false,
    lineNumbers: true,
  }
})
