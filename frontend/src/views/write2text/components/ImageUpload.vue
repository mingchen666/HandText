<template>
  <!-- 图片上传 -->
  <div class="img-upload">
    <el-upload
      v-model:file-list="file_List"
      ref="upload"
      class="upload"
      :before-upload="handleBeforeUploadImg"
      action="http://localhost:5000/"
      :limit="1"
      :on-success="handleSuccess"
      :on-change="handleChange"
      :on-error="handleError"
      :on-exceed="handleExceed"
      :on-remove="handleRemove"
      list-type="picture"
      accept=".jpg,.jpeg,.png,.webp"
      :auto-upload="false">
      <template #trigger>
        <el-button type="primary">{{ props.btnText }}</el-button>
      </template>
      <!-- <template #tip>
        <div class="el-upload__tip text-red">limit 1 file, new file will cover the old file</div>
      </template> -->
    </el-upload>
  </div>
  <!-- 文件上传 -->
</template>

<script setup>
import { ref } from 'vue'
import { genFileId } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'

const upload = ref(null)
const fileState = ref({
  file: null,
  binaryData: null
})
const emit = defineEmits(['deleteFile'])
const file_List = ref([])

// 处理文件变化事件
const handleChange = (file, fileList) => {
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
  // // 手动触发上传确认对话框
  // if (props.type === 1 && !file_List.value.length) {
  //   handleBeforeUploadImg(file.raw).then((shouldUpload) => {
  //     if (shouldUpload) {
  //       upload.value.submit()
  //     }
  //   })
  // }
}

// 当超出限制时，执行的钩子函数
const handleExceed = (files) => {
  upload.value.clearFiles()
  const file = files[0]
  file.uid = genFileId()
  upload.value.handleStart(file)
}

// 文件删除
const handleRemove = (uploadFile, uploadFiles) => {
  // console.log('文件移除', uploadFile, uploadFiles)
  // 清空 fileState 中的数据
  fileState.value.file = null
  fileState.value.binaryData = null
}

// 图片上传之前
const handleBeforeUploadImg = async (file) => {
  // console.log('文件上传', file)
  // 检查文件类型
  const fileType = file.type
  const allowedTypeArray = ['image/jpeg', 'image/png', 'image/jpg', 'image/webp']
  if (!allowedTypeArray.includes(fileType)) {
    ElMessage.error(`文件类型不支持，仅支持 png/jpg/webp等图片格式`)
    return false
  }
  // 检查文件大小
  const fileSize = file.size
  const maxSize = 2 * 1024 * 1024 // 5MB
  if (fileSize > maxSize) {
    ElMessage.error(`文件大小不能超过 ${maxSize / (1024 * 1024)} MB`)
    return false
  }

  /*  ElMessage({
    type: 'success',
    message: '上传成功'
  })
    */
  return true
}

// 文件上传
const handleFileUpload = () => {
  if (file_List.length === 0) {
    ElMessage.error('请选择文件上传')
    return
  }
  // console.log('文件上传', file)
  upload.value.submit()
}

// 文件上传成功
const handleSuccess = (response, uploadFile) => {
  fileState.value.binaryData = response
}

const props = defineProps({
  btnText: {
    type: String,
    default: '上传图片'
  }
})

// 对外暴露
defineExpose({
  fileState,
  handleFileUpload
})

// 上传失败
const handleError = (err, file, fileList) => {
  console.log('文件上传失败', err, file, fileList)
  ElMessage.error('上传失败')
  // 清空 fileState 中的数据
  fileState.value.file = null
  fileState.value.binaryData = null
}
</script>

<style>
.file-upload {
  text-align: center;
  vertical-align: middle;
}

.file-upload * {
  padding: 0;
  margin: 0;
}

.img-upload.upload {
  width: 100%;
}

.el-upload-list.el-upload-list--picture {
  width: 80%;
}

.upload .el-button {
  padding: 10px 5px;
}
</style>
