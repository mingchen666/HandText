<template>
  <div
    class="preview-card"
    v-loading="stateStore.isWrite2TextLoading"
    element-loading-text="{{ $t('write2text.loading识别提示') }}">
    <div class="custom-card">
      <div class="card-header">
        <span class="card-title">{{ $t('write2text.preview_card.title') }}</span>
        <el-tooltip :content="$t('write2text.preview_card.tooltip_copy')" placement="bottom">
          <el-icon @click="copyText" class="copy-icon">
            <Copy />
          </el-icon>
        </el-tooltip>
      </div>
      <div class="card-content">{{ fileStore.write2TextContent }}</div>
    </div>
  </div>
</template>

<script setup>
import { ElMessage, ElTooltip } from 'element-plus'
import Copy from '@/components/icons/Copy.vue'
import { useFileStore } from '@/stores/file'
import { useStateStore } from '@/stores/state'
const stateStore = useStateStore()
const fileStore = useFileStore()

// 复制文本到剪贴板
function copyText() {
  navigator.clipboard
    .writeText(fileStore.write2TextContent)
    .then(() => {
      ElMessage.success('复制成功！')
    })
    .catch((err) => {
      console.error('复制失败：', err)
      ElMessage.error('复制失败！')
    })
}
</script>

<style scoped>
.preview-card {
  height: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid var(--el-border-color-light);
  background-color: var(--el-bg-color-overlay);
}

.custom-card {
  width: 100%;
  height: 100%;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid var(--el-border-color-light);
  display: flex;
  flex-direction: column;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  border-bottom: 1px dashed var(--el-border-color-light);
  padding-bottom: 10px;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
  color: var(--el-text-color-primary);
}

.card-content {
  flex: 1;
  font-size: 16px;
  white-space: pre-wrap; /* 保留文本中的换行符 */
  color: var(--el-text-color-regular);
  line-height: 1.6;
  padding: 10px;
  background-color: var(--el-bg-color-light);
  border-radius: 6px;
  border: 1px solid var(--el-border-color-lighter);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.copy-icon {
  cursor: pointer;
  transition:
    transform 0.3s ease,
    color 0.3s ease;
  color: var(--el-color-primary);
}

.copy-icon:hover {
  transform: scale(1.1);
  color: var(--el-color-primary-light-3);
}

/* 夜间主题样式 */
.night-theme .card-title,
.night-theme .card-content {
  color: var(--el-text-color-primary-inverse);
}

.night-theme .card-content {
  background-color: var(--el-bg-color-dark);
  border-color: var(--el-border-color-dark);
}
</style>
