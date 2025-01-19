<script setup>
import { ref, onMounted } from 'vue'
import { useFontList } from '@/views/text2write/hooks/useGetfont'
import ImageUpload from '@/components/ImageUpload.vue'
import MarginSetting from './MarginSetting.vue'
import AdvancedSetting from './AdvancedSetting.vue'
import { useFormDataStore } from '@/stores/formdata'
import { useFileStore } from '@/stores/file'
import { generateText2WriteService } from '@/apis/text2write'
import { objectToFormData } from '@/utils/tools'
import { useStateStore } from '@/stores/state'
const stateStore = useStateStore()
const formDataStore = useFormDataStore()
const fileStore = useFileStore()
// !!! 请注意，这里的el-dialog组件挂载点是body，导致现在组件访问不到这个组件的ref
// 只能该组件的内部才能访问到
const elRef = ref(null)
const marginSettingRef = ref(null)
const advancedSettingRef = ref(null)
const imageUpload = ref(null)
onMounted(() => {
  console.log('组件已经挂载')
})
// 基础表单
const baseForm = ref({ ...formDataStore.baseForm })

// 字体
const { fontOptions } = useFontList()

// 控制边距设置对话框的显示与隐藏
const marginSettingDialogVisible = ref(false)
// 边距设置保存
const onSaveMarginForm = () => {
  marginSettingDialogVisible.value = false
  const newMarginForm = marginSettingRef.value.theMarginForm
  formDataStore.updateMarginForm(newMarginForm)
}
// 控制高级设置对话框的显示与隐藏
const advancedSettingDialogVisible = ref(false)
// 高级设置保存
const onSaveAdvancedSetting = () => {
  advancedSettingDialogVisible.value = false
  const newAdvancedForm = advancedSettingRef.value.theAdvancedForm
  formDataStore.updateAdvancedForm(newAdvancedForm)
}
// 保存所有表单设置 -- 这里无法调用上面的两个设置保存
const onSaveAll = () => {
  console.log('保存所有设置成功！')
  console.log('表单数据', baseForm.value)
  formDataStore.updateBaseForm(baseForm.value)
  // onSaveMarginForm()
  // onSaveAdvancedSetting()
}
// 显示预览效果
const onPreview = async () => {
  // 更新加载中状态
  stateStore.updatePreviewLoading(true)
  // 如果用户上传了背景图片
  if (imageUpload.value.fileState.binaryData) {
    baseForm.value.background_image = imageUpload.value.fileState.binaryData
    // 删除高度宽度属性
    delete baseForm.value.height
    delete baseForm.value.width
  }
  baseForm.value.pdf_save = false
  const dataForm = {
    preview: true,
    ...baseForm.value,
    ...formDataStore.marginForm,
    ...formDataStore.advancedForm
  }
  console.log('请求表单', dataForm)

  // 对象转换成表单对象
  const formData = objectToFormData(dataForm, imageUpload.value.fileState)
  // 发送请求
  const res = await generateText2WriteService(formData)
  // 将其转换成blob对象进行预览显示
  const blob = new Blob([res.data], { type: 'image/png' })
  const previewImageUrl = URL.createObjectURL(blob)
  // 更新pinia
  fileStore.setPreviewImageUrl(previewImageUrl)
  stateStore.updatePreviewLoading(false)
}
// 父接受子信息,文件删除,重置宽高,背景图片
const onDeleteFile = () => {
  // 重置宽高
  baseForm.value.width = 2479
  baseForm.value.height = 3508
  // 重置背景图片
  baseForm.value.background_image = null
}
// 保存为pdf
const onSaveAsPdf = async () => {
  // 如果用户上传了背景图片
  if (imageUpload.value.fileState.binaryData) {
    baseForm.value.background_image = imageUpload.value.fileState.binaryData
    // 删除高度宽度属性
    delete baseForm.value.height
    delete baseForm.value.width
  }
  // pdf_save设置为true
  baseForm.value.pdf_save = true
  const dataForm = {
    preview: true,
    ...baseForm.value,
    ...formDataStore.marginForm,
    ...formDataStore.advancedForm
  }
  // 对象转换成表单对象
  const formData = objectToFormData(dataForm, imageUpload.value.fileState)
  // 发送请求
  const res = await generateText2WriteService(formData)
  // 将响应转换为 Blob 对象
  const blob = new Blob([res.data], { type: 'application/pdf' })

  // 创建一个 URL 对象
  const url = window.URL.createObjectURL(blob)

  // 创建一个隐藏的 <a> 标签
  const a = document.createElement('a')
  a.href = url
  a.download = 'handwrite.pdf' // 设置下载的文件名
  // 将 <a> 标签添加到 DOM 中并触发点击事件
  document.body.appendChild(a)
  a.click()
  // 移除 <a> 标签并释放 URL 对象
  document.body.removeChild(a)
  window.URL.revokeObjectURL(url)
}
// 重置设置
const onResetSetting = () => {
  console.log('重置设置')
  formDataStore.resetAllForm()
  // 重新设置baseForm
  baseForm.value = formDataStore.baseForm
}
// 字体颜色改变触发
// const colorChange = (val) => {
//   // 去除'rgb'字符串
//   baseForm.fill = val.replace('rgb', '')
// }
</script>
<template>
  <!-- <div>66666</div> -->
  <div class="text-config-container">
<!-- 文本输入框 -->
    <div class="text-input">
      <el-input
        v-model="baseForm.text"
        style="width: 90%"
        :rows="6"
        maxlength="3000"
        show-word-limit
        type="textarea"
        :placeholder="$t('text2write.base_form.input_placeholder')" />
    </div>

    <!-- 基础表单 -->
    <div class="base-form">
      <el-form
        class="config-form"
        :model="baseForm"
        label-width="auto"
        label-position="left"
        style="width: 90%; max-width: 800px">
        <el-form-item
          class="font-options"
          :label="$t('text2write.base_form.select_font')">
          <el-select
            v-model="baseForm.font_option"
            :placeholder="$t('text2write.please_select')"
            style="width: 40%">
            <el-option
              v-for="item in fontOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value" />
          </el-select>
          <!-- 字体文件上传选项 -->
          <!-- <div class="font-upload"> -->
          <!-- <div>
            <span>&emsp;{{ $t('or') }}&emsp;</span>
          </div>
          <FileUpload :type="0" btn-text="上传字体文件" /> -->
          <!-- </div>  -->
        </el-form-item>
        <!-- 背景图片上传选项 -->
        <el-form-item class="font-options" :label="$t('text2write.base_form.background_image_optional')">
          <div class="img-upload">
            <ImageUpload
              ref="imageUpload"
              :btn-text="$t('text2write.base_form.upload_background_image')"
              @deleteFile="onDeleteFile" />
          </div>
        </el-form-item>
        <el-form-item :label="$t('text2write.base_form.width')">
          <el-input-number v-model="baseForm.width" />
        </el-form-item>

        <el-form-item :label="$t('text2write.base_form.height')">
          <el-input-number v-model="baseForm.height" />
        </el-form-item>
        <el-form-item :label="$t('text2write.base_form.font_color')">
          <el-color-picker v-model="baseForm.fill" color-format="rgb" />
        </el-form-item>
        <el-form-item :label="$t('text2write.base_form.font_size')">
          <el-input-number v-model="baseForm.font_size" :min="1" />
        </el-form-item>
        <el-form-item :label="$t('text2write.base_form.underline')">
          <el-switch v-model="baseForm.isUnderlined" />
        </el-form-item>
        <!-- <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button>取消</el-button>
      </el-form-item> -->
      </el-form>
    </div>

    <!-- 更多设置 -->
    <el-collapse accordion>
      <el-collapse-item :title="$t('text2write.more_settings.title')" name="1">
        <div class="more-setting">
          <el-button type="primary" @click="marginSettingDialogVisible = true">
            {{ $t('text2write.more_settings.margin_setting') }}
          </el-button>
          <el-button type="primary" @click="advancedSettingDialogVisible = true">
            {{ $t('text2write.more_settings.advanced_setting') }}
          </el-button>
        </div>
      </el-collapse-item>
    </el-collapse>

    <!-- 1.-边距设置 -弹窗-->
    <!-- !!! 请注意，这里的el-dialog组件挂载点是body，导致现在组件访问不到这个组件的ref -->
    <el-dialog
      :title="$t('text2write.more_settings.margin_setting')"
      ref="elRef"
      v-model="marginSettingDialogVisible"
      width="50%"
      align-center>
      <MarginSetting ref="marginSettingRef" />
      <!-- 底部保存按钮 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="marginSettingDialogVisible = false">
            {{ $t('text2write.buttons.cancel') }}
          </el-button>
          <el-button type="primary" @click="onSaveMarginForm">
            {{ $t('text2write.buttons.save') }}
          </el-button>
        </div>
      </template>
    </el-dialog>

    <!-- 2.高级设置 -弹框-->
    <el-dialog
      :title="$t('text2write.more_settings.advanced_setting')"
      align-center
      v-model="advancedSettingDialogVisible"
      width="50%">
      <AdvancedSetting ref="advancedSettingRef" />
      <!-- 底部保存按钮 -->
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="advancedSettingDialogVisible = false">
            {{ $t('text2write.buttons.cancel') }}
          </el-button>
          <el-button type="primary" @click="onSaveAdvancedSetting">
            {{ $t('text2write.buttons.save') }}
          </el-button>
        </div>
      </template>
    </el-dialog>

    <!-- 按钮组 -->
    <div class="btn-group w-full">
      <el-button plain type="primary" round @click="onSaveAll">
        {{ $t('text2write.buttons.save_all') }}
      </el-button>
      <el-button plain round @click="onResetSetting">{{ $t('text2write.buttons.reset') }}</el-button>
      <el-button plain type="success" round @click="onPreview">
        {{ $t('text2write.buttons.preview') }}
      </el-button>
      <el-button plain type="info" round>{{ $t('text2write.buttons.generate_image') }}</el-button>
      <el-button plain type="warning" round @click="onSaveAsPdf">
        {{ $t('text2write.buttons.generate_pdf') }}
      </el-button>
      <!-- <el-button plain type="danger" round>反馈</el-button> -->
    </div>
  </div>
</template>

<style scoped>
.text-config-container {
  width: 90%;
  display: flex;
  flex-direction: column;
}
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
/* .more-setting { */
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: space-between; */
/* } */
/* 按钮组 */
.btn-group {
  margin-top: 5px;
}
/* 选择器选中样式 */
.el-select-dropdown__item.is-selected {
  color: red;
}
</style>
