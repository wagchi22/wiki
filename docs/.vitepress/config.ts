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
        text: "🏠 Início", 
        link: "/inicio" 
      }
    ],
    
    sidebar: [
      {
        text: "Guias",
        items: [
          { text: "⚙️ Meus Ajustes Gerais", link: "/guias/meus-ajustes-gerais" },
          { text: "🎬 Configurando um servidor de mídia", link: "/guias/configurando-um-servidor-de-midia" },
          { text: "📽️ Instalando HEVC no Windows 11", link: "/guias/instalando-hevc-no-windows-11" },
          { text: "🛜 Testando rede usando MTR no Windows 11", link: "/guias/testando-rede-usando-mtr-no-windows-11" },
          { text: "📺 Instalando TizenTube no Fire TV com Android", link: "/guias/instalando-tizentube-no-firetv-com-android" },
          { text: "📄 Lista de softwares úteis", link: "/guias/lista-de-softwares-uteis" },
          { text: "🖼️ Corrigindo miniaturas MP4 no Windows 11", link: "/guias/corrigindo-miniaturas-mp4-no-windows-11" },
          { text: "📦 Gerenciando pacotes com Winget", link: "/guias/gerenciando-pacotes-com-winget" },
          { text: "🔆 Escolhendo iluminação ideal para casa", link: "/guias/escolhendo-iluminacao-ideal-para-casa" }
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