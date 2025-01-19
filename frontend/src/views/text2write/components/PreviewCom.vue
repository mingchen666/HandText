<script setup>
import { useFileStore } from '@/stores/file'
import { useStateStore } from '@/stores/state'
const stateStore = useStateStore()
const fileStore = useFileStore()
// fileStore.previewImage ||
// const previewImage = ref('https://ww1.sinaimg.cn/mw690/9516662fgy1hbgtkc74jsj20j60j6tbv.jpg')
// 下载图片
const downloadImage = () => {
  // 创建一个隐藏的 <a> 标签
  const link = document.createElement('a')
  // 设置下载的文件名
  link.download = 'preview.png'
  // 设置 href 属性为 预览图片的url---fileStore.previewImageUrl
  link.href = fileStore.previewImageUrl
  // 将 <a> 标签添加到 DOM 中
  document.body.appendChild(link)
  // 触发点击事件
  link.click()
  // 移除 <a> 标签
  document.body.removeChild(link)
  // 释放内存
  URL.revokeObjectURL(fileStore.previewImageUrl)
}
</script>
<template>
  <!-- 预览区 -->
  <div
    class="preview"
    v-loading="stateStore.isPreviewLoading"
    :element-loading-text="$t('text2write.preview_area.loading_text')">
    <div class="header flex">
      <h2>{{ $t('text2write.preview_area.title') }}</h2>
      <el-tooltip
        class="icon-container"
        effect="light"
        :content="$t('text2write.preview_area.tooltip_download')"
        placement="bottom">
        <el-icon class="download-icon" size="30" @click="downloadImage"><Download /></el-icon>
      </el-tooltip>

      <!-- <div class="icon-container">
      <el-icon size="30"><Download /></el-icon>
    </div> -->
    </div>
    <!-- <div v-viewer> -->
    <div class="preview-content">
      <img
        :src="fileStore.previewImageUrl"
        :alt="$t('text2write.preview_area.alt_text')"
        class="preview-image" />
    </div>
    <!-- </div> -->
  </div>
</template>
<style scoped>
.preview {
  width: 100%;
  height: 100%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  /* overflow: hidden; */
}
.preview img {
  max-width: 100%;
  /* max-height: 100%; */
  height: auto;
  /* object-fit: none; */
  object-position: center;
  /* position: sticky; */
  /* top: 0; */
}
.preview h2 {
  text-align: center;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.header h2 {
  flex-grow: 1;
  text-align: center;
}

.download-icon {
  cursor: pointer;
}
.preview-content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.preview-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* 保持图片的宽高比 */
}

</style>
