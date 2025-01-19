<template>
  <el-dialog
    v-model="dialogVisible"
    title="用户上传图片协议"
    width="50%"
    :close-on-click-modal="false"
    :before-close="handleClose">
    <div class="agreement-content">
      <h4>欢迎您使用我们的服务！请仔细阅读以下简要协议内容：</h4>

      <h5>1. 接受条款</h5>
      <p>
        使用本服务即表示您同意遵守本协议的所有条款。
      </p>

      <h5>2. 上传规范</h5>
      <ul>
        <li><strong>合法合规：</strong> 不得上传任何违反法律法规的内容，包括但不限于涉及暴力、色情、低俗、恐怖主义、诽谤、侵权或其他违法不良信息。</li>
        <li><strong>尊重隐私：</strong> 禁止上传涉及他人隐私或敏感信息的照片，如身份证件、个人联系方式、医疗记录等。确保上传的图片不会侵犯他人的隐私权。</li>
        <li><strong>版权与原创性：</strong> 仅上传自己拥有版权或已获得授权使用的图片，避免上传伪造或误导性的图像。</li>
        <li><strong>文明分享：</strong> 上传的图片中不应含有侮辱性语言、仇恨言论或其他不当表述。</li>
        <li><strong>文件要求：</strong> 请上传清晰的手写图片，支持 .jpg, .png, .webp 等常见格式，文件大小不超过500KB。确保图片不含任何恶意软件或病毒。</li>
      </ul>

      <h5>3. 用户责任</h5>
      <p>
        您应对上传的内容负全部法律责任。如因上传违规图片导致的任何问题，您需自行承担全部责任。多次上传违规图片可能会导致账号被限制使用或永久封禁。
      </p>

      <h5>4. 特别提示</h5>
      <p>
        我们鼓励所有用户遵守上述规定，共同营造健康向上的网络空间。如果您有任何疑问或需要帮助，请随时联系我们：[联系邮箱]。
      </p>
      <p>
        <strong>重要提醒：</strong> 请勿上传包含个人隐私或敏感信息的照片，以保护您和他人的隐私安全。
      </p>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleClose">不同意</el-button>
        <el-button type="primary" @click="agreeToAgreement">我同意</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const dialogVisible = ref(false)
const emit = defineEmits(['close', 'agree'])

const handleClose = () => {
  dialogVisible.value = false
  emit('close')
}

const agreeToAgreement = () => {
  dialogVisible.value = false
  emit('agree')
}

defineExpose({
  open: () => {
    dialogVisible.value = true
  }
})
</script>

<style scoped>
.agreement-content {
  max-height: 300px;
  overflow-y: auto;
}
.agreement-content h4,
.agreement-content h5 {
  margin: 10px 0;
}
.agreement-content p,
.agreement-content ul {
  margin: 5px 0;
}
.agreement-content ul li {
  margin: 5px 0;
}
.dialog-footer {
  text-align: right;
}
</style>