<template>
  <el-input
    v-model="text"
    style="width: 90%"
    :rows="6"
    type="textarea"
    placeholder="请输入需要手写的文字" />
</template>

<script setup>
import { ref } from 'vue'

const text = ref('')
// 对外暴露数据
defineExpose({ text })

</script>

<style scoped>
.upload-com {
  width: 90%;
  height: 220px;
}
</style>
