<template>
  <div>
    <!-- 文本/文件输入框 -->
    <div class="text-input">
      <TextInput></TextInput>
    </div>
    <!-- 基础表单 -->
    <el-form
      class="config-form"
      :model="form"
      label-width="auto"
      label-position="left"
      style="width: 90%; max-width: 800px">
      <el-form-item class="font-options" label="字体文件:">
        <el-select v-model="fontValue" placeholder="请选择字体" style="width: 40%">
          <el-option
            v-for="item in fontOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value" />
        </el-select>
        <!-- 字体文件上传选项 -->

        <div class="font-upload">
          <span>&emsp;{{ $t('or') }}&emsp;</span>
          <FileUpload :type="'file'" btn-text="上传字体文件" />
        </div>
      </el-form-item>
      <!-- 背景图片上传选项 -->
      <el-form-item class="font-options" label="背景图片:">
        <div class="img-upload">
          <FileUpload :type="'file'" btn-text="上传背景图片" />
        </div>
      </el-form-item>
      <el-form-item label="宽度:">
        <el-input v-model="form.width" />
      </el-form-item>

      <el-form-item label="高度:">
        <el-input v-model="form.height" />
      </el-form-item>
      <el-form-item label="字体大小:">
        <el-input-number v-model="form.fontSize" :min="1" :max="10" />
      </el-form-item>
      <el-form-item label="增加下划线:">
        <el-switch v-model="form.isUnderline" />
      </el-form-item>
      <!-- <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button>取消</el-button>
      </el-form-item> -->
    </el-form>
    <!-- 更多设置 -->
    <el-collapse accordion>
      <el-collapse-item title="更多设置" name="1">
        <div class="more-setting">
          <el-button type="primary" @click="extraSettingDialogVisible = true">额外设置⚙️</el-button>
          <el-button type="primary" @click="advancedSettingDialogVisible = true">
            高级设置🔧
          </el-button>
        </div>
      </el-collapse-item>
    </el-collapse>
    <!-- 1.额外设置 -->
    <el-dialog
      title="额外设置"
      v-model="extraSettingDialogVisible"
      width="50%"
      align-center
      :before-close="handleExtraSettingClose">
      <ExtraSetting />
      <!-- 底部保存按钮 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="extraSettingDialogVisible = false">{{ $t('cancel') }}</el-button>
          <el-button type="primary" @click="dialogVisible = false">
            {{ $t('save') }}
          </el-button>
        </div>
      </template>
    </el-dialog>

    <!-- 2.高级设置 -->
    <el-dialog
      title="高级设置"
      align-center
      v-model="advancedSettingDialogVisible"
      width="50%"
      :before-close="handleAdvancedSettingClose">
      <AdvancedSetting />
      <!-- 底部保存按钮 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="advancedSettingDialogVisible = false">{{ $t('cancel') }}</el-button>
          <el-button type="primary" @click="dialogVisible = false">
            {{ $t('save') }}
          </el-button>
        </div>
      </template>
    </el-dialog>
    <!-- 按钮组 -->
    <div class="btn-group w-full">
      <el-button plain type="primary" round>保存设置</el-button>
      <el-button plain round>载入设置</el-button>
      <el-button plain type="success" round>预览</el-button>
      <el-button plain type="info" round>生成完整手写图片</el-button>
      <el-button plain type="warning" round>生成pdf</el-button>
      <!-- <el-button plain type="danger" round>反馈</el-button> -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import FileUpload from '@/components/ImageUpload.vue'
import TextInput from '@/components/TextInput.vue'
import ExtraSetting from './ExtraSetting.vue'
import AdvancedSetting from './AdvancedSetting.vue'
// 表单
const form = ref({
  width: '',
  height: '',
  isUnderline: false,
  fontFile: '',
  fontSize: 5
})
const fontValue = ref('')
// 字体
const fontOptions = [
  {
    value: 'Option1',
    label: 'Option1'
  },
  {
    value: 'Option2',
    label: 'Option2'
  },
  {
    value: 'Option3',
    label: 'Option3'
  }
]
// 当前激活的折叠面板
const activeName = ref('text')
// 控制额外设置对话框的显示与隐藏
const extraSettingDialogVisible = ref(false)

// 控制高级设置对话框的显示与隐藏
const advancedSettingDialogVisible = ref(false)

const onSubmit = () => {
  console.log('submit!')
}
</script>
<style scoped>
.config-form {
  margin-top: 20px;
}
.setting-collapse {
  width: 100%;
}
/* 折叠面板 */
:deep(.el-collapse-item__header1) {
  width: 25%;
}
:deep(.el-collapse-item__header.is-active) {
  color: #4284e6;
}
/* 字体菜单选项 */
.font-options {
  display: flex;
  align-items: center;
  justify-content: space-between !important;
}
.font-upload {
  display: flex;
}
/* 更多设置 */
.more-setting {
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: space-between; */
}
/* 按钮组 */
.btn-group {
  margin-top: 5px;
}
</style>
