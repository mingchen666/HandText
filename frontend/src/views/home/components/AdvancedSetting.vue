<template>
  <el-collapse v-model="activeName" accordion class="setting-collapse">
    <!-- 1.偏移设置 -->
    <el-collapse-item name="1">
      <template #title>
        >>>1.偏移设置
        <el-icon class="header-icon">
          <info-filled />
        </el-icon>
      </template>
      <el-form :inline="true" :model="advancedForm" class="w-full extra-form">
        <el-form-item label="笔画横向偏移">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="笔画纵向偏移">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="笔画旋转偏移">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
    <!-- 2.扰动设置 -->
    <el-collapse-item name="2">
      <template #title>
        >>>2.扰动设置
        <el-icon class="header-icon">
          <info-filled />
        </el-icon>
      </template>
      <el-form :inline="true" :model="advancedForm" class="w-full extra-form">
        <el-form-item label="行间距扰动">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="字体大小扰动">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="字间距扰动">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
    <!-- 3.标准差 -->
    <el-collapse-item name="3">
      <template #title>
        >>>3.标准差设置
        <el-icon class="header-icon">
          <info-filled />
        </el-icon>
      </template>
      <el-form :inline="true" :model="advancedForm" class="w-full extra-form">
        <el-form-item label="涂改线长度标准差">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="涂改线宽度标准差">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="涂改线角度标准差">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
    <!-- 4.其他 -->
    <el-collapse-item name="4">
      <template #title>
        >>>4.其他设置
        <el-icon class="header-icon">
          <info-filled />
        </el-icon>
      </template>
      <el-form :inline="true" :model="advancedForm" class="w-full extra-form">
        <el-form-item label="涂改出现的几率">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="涂改线宽度">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
        <el-form-item label="墨汁深度标准差">
          <el-input-number v-model="advancedForm.user" :min="1" :max="10" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { ref } from 'vue'
const activeName = ref('')
const advancedForm = ref({
  user: '',
  region: '',
  date: ''
})

const onSubmit = () => {
  console.log('submit!')
}
</script>

<style>
.demo-form-inline .el-input {
  --el-input-width: 220px;
}

.demo-form-inline .el-select {
  --el-select-width: 220px;
}
</style>
