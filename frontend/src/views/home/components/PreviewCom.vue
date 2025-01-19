<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
const previewImage = ref('https://ww1.sinaimg.cn/mw690/9516662fgy1hbgtkc74jsj20j60j6tbv.jpg')
</script>
<template>
  <!-- 预览区 -->
  <div class="preview">
    <h2>图片预览区域</h2>

    <!-- <div v-viewer> -->
    <img :src="previewImage" :alt="$t('message.previewImage')" style="width: 600px" />
    <!-- </div> -->
  </div>
</template>
<style scoped>
.preview {
  width: 100%;
  height: 100%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.preview img {
  /* max-width: 100%; */
  height: auto;
  object-fit: cover;
  /* position: sticky; */

  /* top: 0; */
}
.preview h2 {
  text-align: center;
}
</style>
