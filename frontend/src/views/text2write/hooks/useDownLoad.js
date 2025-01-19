// src/hooks/useDownload.js
import { ref } from 'vue'

export function useDownload() {
  const downloadFile = (url, filename) => {
    // 创建一个隐藏的 <a> 标签
    const link = document.createElement('a')
    // 设置下载的文件名
    link.download = filename
    // 设置 href 属性为文件的URL
    link.href = url

    // 将 <a> 标签添加到 DOM 中
    document.body.appendChild(link)

    // 触发点击事件
    link.click()

    // 移除 <a> 标签
    document.body.removeChild(link)

    // 释放内存
    URL.revokeObjectURL(url)
  }

  return {
    downloadFile
  }
}
