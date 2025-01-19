import { defineStore } from 'pinia'
import { ref } from 'vue'
import avatarUrl from '@/assets/image.jpg'
export const useFileStore = defineStore(
  'file-store',
  () => {
    // 预览图片scr
    const previewImageUrl = ref(avatarUrl)
    // const previewImageUrl = ref('https://ww2.sinaimg.cn/mw690/c4877746ly1hshcm5po9vj20qo0qo79e.jpg')
    const setPreviewImageUrl = (url) => {
      previewImageUrl.value = url
    }
    // 文件文本解析内容
    const fileContent = ref(`hello,小罗！`)
    const updateFileContent = (content) => {
      fileContent.value = content
    }
    // 手写转文字识别内容
    const write2TextContent = ref(`hello,小罗！`)
    const updateWrite2TextContent = (content) => {
      write2TextContent.value = content
    }
    return {
      write2TextContent,
      previewImageUrl,
      fileContent,
      updateWrite2TextContent,
      setPreviewImageUrl,
      updateFileContent
    }
  },
  {
    // 使用会话存储
    persist: {
      storage: sessionStorage
    }
  }
)
