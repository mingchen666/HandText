import { createApp } from 'vue'
import 'element-plus/theme-chalk/dark/css-vars.css'
import '@/assets/main.css'
import { createPinia } from 'pinia'
import persistedstate from 'pinia-plugin-persistedstate'
import i18n from '@/lang/index'
import App from './App.vue'
import router from './router'
// 导入饿了么plus样式
import 'element-plus/dist/index.css'
// 导入unocss
import 'virtual:uno.css'
// 导入自定义样式
import '@/styles/index.css'
// 导入自定义插件
// import createMessagePlugin from './plugins/messagePlugin'
// import { register } from '@/plugins/index'
// register()
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(createPinia().use(persistedstate))
app.use(router)
app.use(i18n)
app.mount('#app')
