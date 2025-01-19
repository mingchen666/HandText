import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useI18nStore = defineStore(
  'i18n',
  () => {
    const locale = ref('zh') 

    const setLocale = (newLocale) => {
      locale.value = newLocale
    }

    return {
      locale,
      setLocale
    }
  },
  {
    persist: true // 启用持久化
  }
)
