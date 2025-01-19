<template>
  <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
    <el-tab-pane label="文本输入" name="text">
      <el-input
        v-model="textarea"
        style="width: 90%"
        :rows="5"
        type="textarea"
        placeholder="请输入需要手写的文字" />
    </el-tab-pane>
    <el-tab-pane label="文档文件上传" name="file">
      <el-upload
        class="upload-com"
        drag
        :limit="1"
        action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15">
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">
          将需要手写的文档拖放到此处或
          <em>点击上传</em>
        </div>
        <template #tip>
          <div class="el-upload__tip">小于500kb的jpg/png文件</div>
        </template>
      </el-upload>
    </el-tab-pane>
  </el-tabs>
</template>

<script setup>
import { ref } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'
const textarea = ref('')
const activeName = ref('text')

const handleClick = (tab, event) => {
  console.log(tab, event)
}
</script>

<style scoped>
.upload-com {
  width: 90%;
  height: 220px;
}
</style>
