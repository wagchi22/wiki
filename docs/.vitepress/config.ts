import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Minhas Anotações",
  description: "Meu servidor de mídia e guias",
  base: '/meus-arquivos/', 
  
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' }
    ],
    sidebar: [
      {
        text: 'Guias',
        items: [
          { text: 'Configurar Servidor de Mídia', link: '/criando-servidor-midia' }
        ]
      }
    ]
  }
})
