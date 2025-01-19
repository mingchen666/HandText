import { createI18n } from 'vue-i18n'
import en from './en.json'
import zh from './zh.json'

const messages = {
  en,
  zh
}

const i18n = createI18n({
  locale: navigator.language, // 默认语言
  fallbackLocale: 'en', // 设置回退语言
  messages
})

export default i18n
