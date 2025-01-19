<!-- :on-success="handleSuccess" -->

<template>
  <div class="file-upload">
    <el-upload
      ref="fileUploadRef"
      class="upload"
      :action="actionUrl"
      :limit="1"
      drag
      :before-upload="handleBeforeUploadFile"
      :on-change="handleChange"
      :on-error="handleError"
      :on-exceed="handleExceed"
      :on-remove="handleRemove"
      :http-request="customUploadRequest"
      accept=".txt,.word,.pdf,.doc,.docx,.md,.markdown"
      :auto-upload="false"
      :file-list="fileList">
      <!-- 禁用自动上传 -->
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        {{ $t('file_upload.drag_or_click') }}
        <em>{{ $t('file_upload.click_to_upload') }}</em>
      </div>
      <template #tip>
        <div class="el-upload-tip">
          {{ $t('file_upload.supported_file_types') }}
        </div>
      </template>
    </el-upload>
    <div class="btns flex justify-start">
      <el-button type="primary" @click="handleFileUpload">上传文件</el-button>
      <el-button v-if="isPreviewFile" type="primary" @click="onPreviewFile">预览文件内容</el-button>
    </div>
    <!-- 进度条 -->
    <el-progress
      :indeterminate="isIndeterminate"
      :percentage="uploadPercentage"
      :status="uploadStatus"
      :duration="3">
      <span>{{ uploadStatusText }}</span>
    </el-progress>
  </div>
  <!-- 文件编辑预览弹出框 -->
  <FileEditor ref="fileEditorRef" />
</template>
<script setup>
import { ref } from 'vue'
import JSZip from 'jszip'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import FileEditor from './FileEditor.vue'
import { useFileStore } from '@/stores/file'
import { useAuthStore } from '@/stores/auth'
const authStore = useAuthStore()
const fileStore = useFileStore()
const fileUploadRef = ref(null)
const fileEditorRef = ref(null)

const actionUrl = `${import.meta.env.VITE_APP_BASE_URL}/api/upload`
const fileState = ref({
  file: null,
  binaryData: null
})
// 是否显示预览文件按钮
const isPreviewFile = ref(true)
const emit = defineEmits(['deleteFile'])
const fileList = ref([]) // 用于存储文件列表

// 上传状态管理
const uploadStatus = ref('') // '' (默认), 'success', 'exception', 'warning'
const uploadPercentage = ref(0)
const uploadStatusText = ref('待上传')
const isIndeterminate = ref(false)

// 处理文件变化事件
const handleChange = (file, fileList) => {
  // 清空之前的文件
  fileList.value = [file]
  fileState.value.file = file.raw
  // 如果已经有文件存在，则先清除旧的二进制数据
  if (fileState.value.binaryData) {
    fileState.value.binaryData = null
  }
  // 转换文件为二进制数据
  const reader = new FileReader()
  reader.onload = (event) => {
    // event.target.result 包含文件的二进制数据 (ArrayBuffer)
    fileState.value.binaryData = event.target.result
    console.log('Binary Data:', fileState.value.binaryData)
  }
  reader.onerror = () => {
    console.error('File reading failed')
  }

  // 读取文件为 ArrayBuffer
  reader.readAsArrayBuffer(file.raw)
  // 更新上传状态
  uploadStatus.value = ''
  uploadPercentage.value = 0
  uploadStatusText.value = '待上传'
}

// 当超出限制时，执行的钩子函数
const handleExceed = (files) => {
  ElMessage.error('每次只能上传一个文件,请删除文件再上传!')
}

// 文件删除
const handleRemove = (uploadFile, uploadFiles) => {
  console.log('文件移除', uploadFile, uploadFiles)
  // 清空 fileState 中的数据
  fileState.value.file = null
  fileState.value.binaryData = null
  fileList.value = [] // 清空文件列表
  // 子传父，告诉父组件文件删除，需要重新设置宽高
  emit('deleteFile')

  // 更新上传状态
  uploadStatus.value = ''
  uploadPercentage.value = 0
  uploadStatusText.value = '待上传'
}

// 文件上传之前
const handleBeforeUploadFile = async (file) => {
  // 弹出框确认是否上传
  return ElMessageBox.confirm('确认上传该文件吗?', 'Warning', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
    type: 'warning'
  })
    .then(() => {
      // 检查文件类型
      const fileType = file.type
      console.log('文件类型', fileType)

      const allowedTypeArray = [
        // 'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain',
        'text/markdown'
      ]
      if (!allowedTypeArray.includes(fileType)) {
        ElMessage.error(`文件类型不支持，仅支持 ${allowedTypeArray.join(', ')} 格式`)
        return false
      }

      // 检查文件大小
      const fileSize = file.size
      const maxSize = 5 * 1024 * 1024 // 5MB
      if (fileSize > maxSize) {
        ElMessage.error(`文件大小不能超过 ${maxSize / (1024 * 1024)} MB`)
        return false
      }
      // ElMessage({
      //   type: 'success',
      //   message: '文件已选择'
      // })
      return true
    })
    .catch(() => {
      ElMessage({
        type: 'warning',
        message: '用户已取消上传'
      })
      return false // 阻止上传
    })
}

// 文件上传
const handleFileUpload = () => {
  if (!fileState.value.file) {
    ElMessage.error('请选择文件上传')
    return
  }

  // 更新上传状态
  // uploadStatus.value = ''
  // uploadStatus.value = 'success'
  uploadPercentage.value = 100
  uploadStatusText.value = '上传中'
  isIndeterminate.value = true
  fileUploadRef.value.submit() // 手动触发上传
  isPreviewFile.value = true
  // console.log('文件上传', fileState.value)
}

// 预览文件内容
const onPreviewFile = () => {
  console.log('预览文件')
  fileEditorRef.value.open()
}

// 文件上传成功
const handleSuccess = async (response, file, fileList) => {
  try {
    // Unzip the response
    // const zip = new JSZip()
    // const unzipped = await zip.loadAsync(response)
    // const content = await unzipped.file('content.txt').async('string')

    // 更新store 的文本内容
    // fileStore.updateFileContent(content)
    // console.log('解压content:', content)
    // ElMessage.success('文件上传并处理成功!')

    // 更新上传状态
    uploadStatus.value = 'success'
    uploadPercentage.value = 100
    uploadStatusText.value = '已上传'
    isIndeterminate.value = false
  } catch (error) {
    console.error('Error processing uploaded file:', error)
    ElMessage.error('文件上传处理失败.')

    // 更新上传状态
    uploadStatus.value = 'exception'
    uploadPercentage.value = 0
    uploadStatusText.value = '上传失败'
    isIndeterminate.value = false
  }
}

// 自定义上传文件请求
const customUploadRequest = (options) => {
  // 更新上传状态为“上传中”
  uploadStatus.value = ''
  uploadStatusText.value = '上传中'
  isIndeterminate.value = true

  const formData = new FormData()
  formData.append('file', options.file)

  axios
    .post(options.action, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${authStore.token}`
      },
      responseType: 'arraybuffer',
      onUploadProgress: (progressEvent) => {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total)
        uploadPercentage.value = percentCompleted
      }
    })
    .then(async (response) => {
      // 解压响应数据并更新store内容
      const zip = new JSZip()
      const unzipped = await zip.loadAsync(response.data)
      const content = await unzipped.file('content.txt').async('string')
      fileStore.updateFileContent(content)

      // 更新上传状态为“成功”
      uploadStatus.value = 'success'
      uploadPercentage.value = 100
      uploadStatusText.value = '已上传'
      isIndeterminate.value = false
      ElMessage.success('文件上传并处理成功!')
    })
    .catch((error) => {
      console.error('Error processing uploaded file:', error)
      ElMessage.error('文件上传处理失败.')

      // 更新上传状态为“失败”
      uploadStatus.value = 'exception'
      uploadPercentage.value = 0
      uploadStatusText.value = '上传失败'
      isIndeterminate.value = false
    })
}
const customUploadRequest1111 = async (options) => {
  const formData = new FormData()
  formData.append('file', options.file)

  try {
    const response = await axios.post(options.action, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: 'arraybuffer', // Important to handle binary data
      onUploadProgress: (progressEvent) => {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total)
        uploadPercentage.value = percentCompleted
      }
    })

    // Unzip the response
    const zip = new JSZip()
    const unzipped = await zip.loadAsync(response.data)
    const content = await unzipped.file('content.txt').async('string')
    // 更新store 的文本内容
    fileStore.updateFileContent(content)
    console.log('解压content:', content)
    ElMessage.success('文件上传并处理成功!')

    // 更新上传状态
    uploadStatus.value = 'success'
    uploadPercentage.value = 100
    uploadStatusText.value = '已上传'
    isIndeterminate.value = false
  } catch (error) {
    console.error('Error processing uploaded file:', error)
    ElMessage.error('文件上传处理失败.')

    // 更新上传状态
    uploadStatus.value = 'exception'
    uploadPercentage.value = 0
    uploadStatusText.value = '上传失败'
    isIndeterminate.value = false
  }
}

const props = defineProps({
  btnText: {
    type: String,
    default: '上传文件'
  }
})

// 对外暴露
defineExpose({
  fileState
})

// 上传失败
const handleError = (err, file, fileList) => {
  console.log('文件上传失败', err, file, fileList)
  ElMessage.error('文件上传失败')

  // 更新上传状态
  uploadStatus.value = 'exception'
  uploadPercentage.value = 0
  uploadStatusText.value = '上传失败'
  isIndeterminate.value = false
}
</script>
<style scoped>
.upload {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  /* align-items: center; */
}
:deep(.el-upload-tip) {
  display: flex;
  font-size: 14px;
  justify-content: flex-start;
  margin: 5px 0;
}
</style>
