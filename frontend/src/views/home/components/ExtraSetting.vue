<template>
  <el-form :inline="true" :model="marginForm" class="w-full extra-form">
    <el-form-item label="行间距">
      <el-input-number v-model="marginForm.line_space" :min="1" />
    </el-form-item>
    <el-form-item label="字间距">
      <el-input-number v-model="marginForm.line_space" :min="1" />
    </el-form-item>
    <el-form-item label="上边距">
      <el-input-number v-model="marginForm.top_margin" :min="1" />
    </el-form-item>
    <el-form-item label="下边距">
      <el-input-number v-model="marginForm.bottom_margin" :min="1" />
    </el-form-item>
    <el-form-item label="左边距">
      <el-input-number v-model="marginForm.lfet_margin" :min="1" />
    </el-form-item>
    <el-form-item label="右边距">
      <el-input-number v-model="marginForm.right_margin" :min="1" />
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
// defineProps({
//   marginForm: {
//     type: Object,
//     default: () => ({})
//   }
// })
// const emit = defineEmits(['updateVisible'])
const marginForm = ref({
  line_space: 200,
  line_space1: 200,
  top_margin: 50,
  bottom_margin: 50,
  lfet_margin: 50,
  right_margin: 50
})

// 保存额外设置
const onSaveExtraForm = () => {
  // emit('updateVisible', false)
}
defineExpose({
  marginForm
})
</script>

<style>
.demo-form-inline .el-input {
  --el-input-width: 220px;
}

.demo-form-inline .el-select {
  --el-select-width: 220px;
}
</style>
