import { defineConfig } from "vitepress"

export default defineConfig({
  title: "Wiki",
  description: "Documentação pessoal.",
  base: "/wiki/", 
  
  cleanUrls: true,
  
  lastUpdated: true,

  head: [
    [
      "link",
      {
        rel: "shortcut icon",
        type: "image/x-icon",
        href: "/favicon.ico",
      },
    ],
    ["style", {}, `
      :root {
        --vp-home-hero-name-color: transparent;
        --vp-home-hero-name-background: -webkit-linear-gradient(120deg, #bd34fe, #41d1ff);
      }
    `]
  ],

  themeConfig: {
    logo: "/logo.svg",
    lastUpdatedText: "Última atualização em",
    search: {
      provider: "local",
      options: {
        translations: {
          button: {
            buttonText: "Pesquisar",
            buttonAriaLabel: "Pesquisar documentos"
          },
          modal: {
            noResultsText: "Nenhum resultado encontrado para",
            resetButtonTitle: "Limpar pesquisa",
            footer: {
              selectText: "para selecionar",
              navigateText: "para navegar",
              closeText: "para fechar"
            }
          }
        }
      }
    },

    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/wagchi22/wiki",
      },
    ],
    
    outline: {
      label: "Nesta página"
    },

    nav: [
      { 
        text: "Início", 
        link: "/inicio" 
      }
    ],
    
    sidebar: [
      {
        text: "Guias",
        items: [
          { text: "Meus Ajustes Gerais", link: "/guias/meus-ajustes-gerais" },
          { text: "Configurar Mediaserver", link: "/guias/configurar-mediaserver" },
          { text: "Instalar Codec HEVC", link: "/guias/instalar-codec-hevc" },
          { text: "Instalar MTR Cygwin", link: "/guias/instalar-mtr-cygwin" },
        ]
      }
    ],

    editLink: {
      pattern: "https://github.com/wagchi22/wiki/edit/main/docs/:path",
      text: "Edite essa página no GitHub"
    },
    
    docFooter: {
      prev: "Anterior",
      next: "Próximo",
    },

    returnToTopLabel: "Voltar ao topo",
    sidebarMenuLabel: "Menu"
  },

  markdown: {
    attrs: {
      disable: true,
    },
    lineNumbers: true,
  }
})