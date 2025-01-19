// src/composables/getFontList.js

import { ref, onMounted } from 'vue'
import request from '@/utils/request'

export function useFontList() {
  const fonts = ref([])
  const fontOptions = ref([])

  const getFonts = async () => {
    try {
      const res = await request({
        url: '/api/fonts',
        method: 'get'
      })
    
      fonts.value = res.data.data
      fontOptions.value = fonts.value.map((item) => {
        return {
          label: item,
          value: item
        }
      })
    } catch (error) {
      console.error('Failed to fetch fonts:', error)
    }
  }

  onMounted(() => {
    getFonts()
  })

  return { fonts, fontOptions }
}
