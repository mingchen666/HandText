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
      <el-form :inline="true" :model="theAdvancedForm" class="w-full extra-form">
        <el-form-item label="笔画横向偏移">
          <el-input-number
            v-model="theAdvancedForm.perturb_x_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="笔画纵向偏移">
          <el-input-number
            v-model="theAdvancedForm.perturb_y_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="笔画旋转偏移">
          <el-input-number
            v-model="theAdvancedForm.perturb_theta_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
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
      <el-form :inline="true" :model="theAdvancedForm" class="w-full extra-form">
        <el-form-item label="每行间距扰动值">
          <el-input-number
            v-model="theAdvancedForm.line_spacing_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="字体大小扰动值">
          <el-input-number
            v-model="theAdvancedForm.font_size_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="字体间距扰动值">
          <el-input-number
            v-model="theAdvancedForm.word_spacing_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="涂改线长度扰动">
          <el-input-number
            v-model="theAdvancedForm.strikethrough_length_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="涂改线宽度扰动">
          <el-input-number
            v-model="theAdvancedForm.strikethrough_width_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="涂改线角度扰动">
          <el-input-number
            v-model="theAdvancedForm.strikethrough_angle_sigma"
            :min="0"
            :precision="1"
            :step="0.1" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
    <!-- 3.其他 -->
    <el-collapse-item name="4">
      <template #title>
        >>>3.其他设置
        <el-icon class="header-icon">
          <info-filled />
        </el-icon>
      </template>
      <el-form :inline="true" :model="theAdvancedForm" class="w-full extra-form">
        <el-form-item label="涂改出现的几率">
          <el-input-number
            v-model="theAdvancedForm.strikethrough_probability"
            :min="0"
            :precision="2"
            :step="0.05" />
        </el-form-item>
        <el-form-item label="涂改线宽度">
          <el-input-number
            v-model="theAdvancedForm.strikethrough_width_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
        <el-form-item label="墨汁深度扰动值">
          <el-input-number
            v-model="theAdvancedForm.ink_depth_sigma"
            :min="0"
            :precision="2"
            :step="0.1" />
        </el-form-item>
      </el-form>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { ref } from 'vue'
import { useFormDataStore } from '@/stores/formdata'
const formDataStore = useFormDataStore()
const initialAdvancedForm = formDataStore.advancedForm
const theAdvancedForm = initialAdvancedForm
const activeName = ref('')
// const advancedForm = ref({
//   line_spacing_sigma: 1.0, // 行间距的随机扰动值
//   font_size_sigma: 2.0, // 字体大小的随机扰动值
//   word_spacing_sigma: 2.0, // 单词间距的随机扰动值
//   perturb_x_sigma: 3.0, // 笔画横向偏移的随机扰动值
//   perturb_y_sigma: 3.0, // 笔画纵向偏移的随机扰动值
//   perturb_theta_sigma: 0.05, // 笔画旋转偏移的随机扰动值
//   strikethrough_probability: 2.0, // 删除线的概率
//   strikethrough_length_sigma: 2.0, // 删除线长度的随机扰动值
//   strikethrough_width_sigma: 2.0, // 删除线宽度的随机扰动值
//   strikethrough_angle_sigma: 2.0, // 删除线角度的随机扰动值
//   strikethrough_width: 8.0, // 删除线的宽度
//   ink_depth_sigma: 30.0 // 墨水深度的随机扰动值
// })

defineExpose({ theAdvancedForm })
</script>

<style>
.demo-form-inline .el-input {
  --el-input-width: 220px;
}

.demo-form-inline .el-select {
  --el-select-width: 220px;
}
</style>
