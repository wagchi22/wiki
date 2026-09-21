import DefaultTheme from 'vitepress/theme'
import './custom.css'
import Icons from '../components/icons.vue/index.js'

export default {
  extends: DefaultTheme,

  enhanceApp({ app }) {
    app.component('Icons', Icons)
  }
}
