<template>
  <div class="image-upload-container">
<!-- 图片上传区域 -->
<div class="upload-section">
  <h3 class="section-title">{{ $t('write2text.upload_section.title') }}</h3>
  <ImageUpload ref="imageUploadRef" :btnText="$t('write2text.upload_section.btn_text')" />
</div>

<!-- 阅读协议勾选框 -->
<div class="agreement-section">
  <el-checkbox v-model="agreedToTerms" @change="handleCheckboxChange">
    {{ $t('write2text.agreement.read_and_agree') }}
    <span @click="openAgreementDialog">{{ $t('write2text.agreement.terms_link') }}</span>
  </el-checkbox>
</div>

<div class="btn">
  <el-button
    class="btn-submit"
    type="primary"
    :disabled="!agreedToTerms"
    @click="convertToText">
    {{ $t('write2text.submit_button') }}
  </el-button>
</div>
    <!-- 提示框 -->
    <TipsAlert></TipsAlert>
    <!-- 协议弹窗 -->
    <AgreementDialog
      ref="agreementDialogRef"
      @close="onAgreementDialogClose"
      @agree="onAgreementDialogAgree" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TipsAlert from './TipsAlert.vue'
import ImageUpload from './ImageUpload.vue'
import { useAuthStore } from '@/stores/auth'
import { ElMessage } from 'element-plus'
import { generateWrite2TextService } from '@/apis/write2text'
import { useFileStore } from '@/stores/file'
import { useStateStore } from '@/stores/state'
import AgreementDialog from './TermsDialog.vue'

const stateStore = useStateStore()
const authStore = useAuthStore()
const fileStore = useFileStore()
const imageUploadRef = ref(null)
const agreementDialogRef = ref(null) // 引用协议弹窗组件

// 文件列表
const fileList = ref([])

// 阅读协议是否同意
const agreedToTerms = ref(false)

// 打开协议弹窗
const openAgreementDialog = () => {
  agreementDialogRef.value.open()
}

// 协议弹窗关闭事件
const onAgreementDialogClose = () => {
  agreedToTerms.value = false
  authStore.updateAgreeImageTerms(false)
}

// 协议弹窗同意事件
const onAgreementDialogAgree = () => {
  authStore.updateAgreeImageTerms(true)
}

// 处理勾选框变化
const handleCheckboxChange = (value) => {
  if (!authStore.isAgreeImageTerms) {
    openAgreementDialog()
  }
}

// 请求---手写转文字
const convertToText = async () => {
  if (agreedToTerms.value && imageUploadRef.value.fileState.file) {
    // 更新状态加载中
    stateStore.updateWrite2TextLoading(true)
    // 对象转换成表单对象
    const formData = new FormData()
    formData.append('extra_content', 666)
    // 文件上传
    // imageUploadRef.value.handleFileUpload()
    // 添加文件对象到表单对象
    formData.append('image', imageUploadRef.value.fileState.file)
    console.log('图片对象', imageUploadRef.value.fileState.file)
    console.log('表单对象formData', formData)
    for (var value of formData.values()) {
      console.log(value)
    }

    try {
      const res = await generateWrite2TextService(formData)
      // 更新store 的文本内容
      fileStore.updateWrite2TextContent(res.data.data)

      ElMessage.success('转换成功!')
    } catch (error) {
      if (error.status === 400) {
        ElMessage.error('该图片非手写文字图片，请重新上传!')
        return
      }
      // console.error('转换为文字失败', error.status)
      ElMessage.error('转换为文字失败，请重试')
    } finally {
      // 确保无论是否发生错误，都关闭加载状态
      stateStore.updateWrite2TextLoading(false)
    }
  } else {
    ElMessage.error('请先上传图片并同意协议')
  }
}
</script>

<style scoped>
.image-upload-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 10px 20px;
  /* background-color: var(--el-bg-color-page); */
}
.section-title {
  margin-bottom: 20px;
}
.upload-section {
  width: 100%;
  margin-top: 20px;
}

.btn {
  margin: 15px auto;
}
.btn > .btn-submit {
  font-size: large;
  padding: 20px 30px;
}

/* 图片列表样式穿透 */
:deep(.el-upload-list.el-upload-list--picture) {
  width: 100%;
}
/* 同意图片上传条款 */
:deep(.el-checkbox__input.is-checked + .el-checkbox__label) {
  color: var(--el-text-color-regular);
}
.agreement-section span {
  cursor: pointer;
  color: #409eff;
}
/* 阅读协议样式 */
.agreement-section {
  margin: 20px 0;
}
</style>
