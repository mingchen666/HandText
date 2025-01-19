<template>
  <el-form :inline="true" :model="theMarginForm" class="w-full extra-form">
    <el-form-item label="行间距">
      <el-input-number v-model="theMarginForm.line_spacing" :min="1" />
    </el-form-item>
    <el-form-item label="字间距">
      <el-input-number v-model="theMarginForm.word_spacing" :min="1" />
    </el-form-item>
    <el-form-item label="上边距">
      <el-input-number v-model="theMarginForm.top_margin" :min="1" />
    </el-form-item>
    <el-form-item label="下边距">
      <el-input-number v-model="theMarginForm.bottom_margin" :min="1" />
    </el-form-item>
    <el-form-item label="左边距">
      <el-input-number v-model="theMarginForm.left_margin" :min="1" />
    </el-form-item>
    <el-form-item label="右边距">
      <el-input-number v-model="theMarginForm.right_margin" :min="1" />
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue'
import { useFormDataStore } from '@/stores/formdata'
const formDataStore = useFormDataStore()
const initialMarginForm = formDataStore.marginForm
const theMarginForm = initialMarginForm

defineExpose({
  theMarginForm
})
</script>

<style></style>
