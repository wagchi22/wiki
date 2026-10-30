import { defineConfig } from "vitepress"

export default defineConfig({
  title: "Wiki",
  description: "Uma base de conhecimento técnico com guias e configurações documentadas para consulta.",
  base: "/wiki/",

  cleanUrls: true,

  lastUpdated: true,

  head: [
    [
      "link",
      {
        rel: "shortcut icon",
        type: "image/x-icon",
        href: "/wiki/favicon.ico",
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
      },
    ],

    sidebar: [
      {
        text: "Guias",
        items: [
          { text: "Ajustes de dispositivos", link: "/guias/ajustes-de-dispositivos" },
          { text: "Como configurar um Servarr", link: "/guias/como-configurar-um-servarr" },
          { text: "Como instalar o Docker", link: "/guias/como-instalar-o-docker" },
          { text: "Como instalar e usar o WinMTR", link: "/guias/como-instalar-e-usar-o-winmtr" },
          { text: "Como usar o Winget", link: "/guias/como-usar-o-winget" }
        ]
      },
      {
        text: "Recursos",
        items: [
          { text: "Template", link: "/templates/guia-template" }
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