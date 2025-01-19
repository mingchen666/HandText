<template>
  <!-- 图片上传 -->
  <div class="img-upload">
    <el-upload
      v-model:file-list="file_List"
      ref="upload"
      class="upload"
      :before-upload="handleBeforeUploadImg"
      action="http://localhost:5000/upload"
      :limit="1"
      :on-success="handleSuccess"
      :on-change="handleChange"
      :on-error="handleError"
      :on-exceed="handleExceed"
      :on-remove="handleRemove"
      list-type="picture"
      accept=".jpg,.jpeg,.png,.webp"
      :auto-upload="true">
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
  console.log('文件移除', uploadFile, uploadFiles)
  // 清空 fileState 中的数据
  fileState.value.file = null
  fileState.value.binaryData = null
  // 子传父，告诉父组件文件删除，需要重新设置宽高
  emit('deleteFile')
}

// 图片上传之前
const handleBeforeUploadImg = async (file) => {
  // 弹出框确认是否自动识别四周边距以及是否上传
  return ElMessageBox.confirm('确认上传该背景图片吗?这将使用图片的宽高', 'Warning', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
    type: 'warning'
  })
    .then(() => {
      // 检查文件类型
      const fileType = file.type
      const allowedTypeArray =
        props.type === 1 //
          ? ['image/jpeg', 'image/png', 'image/jpg', 'image/webp']
          : [
              'application/pdf',
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

      ElMessage({
        type: 'success',
        message: '上传成功'
      })
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
  console.log('文件上传')
  upload.value.submit()
}

// 文件上传成功
const handleSuccess = (response, uploadFile) => {
  fileState.value.binaryData = response
}

const props = defineProps({
  type: {
    type: Number,
    default: 1
  },
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
