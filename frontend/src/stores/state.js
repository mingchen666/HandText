import { ref } from 'vue'
import { defineStore } from 'pinia'
export const useStateStore = defineStore('state-store', () => {
  // 图片预览加载状态
  const isPreviewLoading = ref(false)
  // 更新图片预览加载状态
  const updatePreviewLoading = (val) => {
    isPreviewLoading.value = val
  }
  // 手写转文字状态
  const isWrite2TextLoading = ref(false)
  const updateWrite2TextLoading = (val) => {
    isWrite2TextLoading.value = val
  }
  return { isPreviewLoading, updatePreviewLoading, isWrite2TextLoading, updateWrite2TextLoading }
})
