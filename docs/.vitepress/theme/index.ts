// docs/.vitepress/theme/index.js
import DefaultTheme from 'vitepress/theme'
import './custom.css' // Importa o CSS do FMHY

export default {
  extends: DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    // Aqui pode adicionar componentes extra se necessário no futuro
  }
}
