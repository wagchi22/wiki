import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Minhas Anotações",
  description: "Minhas Anotações",
  base: '/meus-arquivos/', 
  
  themeConfig: {
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
    ]
  },
  docFooter: {
  prev: false,
  next: false,
  }
})
