<template>
  <div class="dialog-box" :style="{ width: componentWidth, height: componentHeight }">
    <!-- 工具栏 -->
    <div class="tool-tab">
      <button @click="undoContent">撤销</button>
      <button @click="copyContent">复制</button>
      <button @click="deleteContent">删除</button>
      <button @click="saveContent">保存</button>
      <button @click="saveContent">优化</button>
      <button @click="summarizeContent">一键总结</button>
    </div>
    <!-- 文本编辑区域 -->
    <div class="text-editor" @click="focusEditor">
      <div
        ref="editor"
        contenteditable="true"
        @input="onInput"
        @blur="onBlur"
        class="editor-content"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { ElMessage } from 'element-plus'
import { useFileStore } from '@/stores/file'
const fileStore = useFileStore()
// 定义props以接收父组件传递的宽度和高度
const props = defineProps({
  width: {
    type: String,
    default: '100%'
  },
  height: {
    type: String,
    default: '400px'
  }
})

const componentWidth = ref(props.width)
const componentHeight = ref(props.height)

// 定义编辑器的内容
const editor = ref(null)
const content = ref('你呢你你你你你你你你你那那那')
onMounted(async () => {
  content.value = fileStore.fileContent
  await nextTick() // 确保 DOM 更新后再进行赋值
  if (editor.value) {
    editor.value.textContent = content.value
  }
})

const historyStack = ref([]) // 历史记录栈

// 挂载时从本地存储加载内容（已删除）
// onMounted(() => {
//   const savedContent = localStorage.getItem('editorContent')
//   if (savedContent) {
//     content.value = savedContent.trim() // 清理多余空格和换行符
//     editor.value.textContent = content.value // 使用 textContent
//   }
// })

// 监听输入事件
const onInput = () => {
  content.value = editor.value.textContent.trim() // 清理多余空格和换行符
  historyStack.value.push(content.value) // 将当前内容推入历史记录栈
}

// 监听失去焦点事件（可选）
const onBlur = () => {
  // 可以在这里执行一些操作，例如验证内容或保存内容
}

// 复制内容
const copyContent = () => {
  if (!navigator.clipboard) {
    ElMessage.error('当前浏览器不支持复制')
    return
  }
  if (content.value == '') {
    ElMessage.error('内容为空!')
    return
  }
  let textToCopy = ''
  if (window.getSelection) {
    const selection = window.getSelection()
    if (selection.toString()) {
      textToCopy = selection.toString()
    } else {
      textToCopy = content.value
    }
  } else if (document.selection && document.selection.type !== 'Control') {
    textToCopy = document.selection.createRange().text
  }
  navigator.clipboard
    .writeText(textToCopy)
    .then(() => {
      ElMessage.success('复制成功!')
    })
    .catch((err) => {
      ElMessage.error('复制失败~')
    })
}

// 删除内容
const deleteContent = () => {
  // 检查浏览器是否支持 window.getSelection
  if (window.getSelection) {
    const selection = window.getSelection()
    // 检查是否存在选中的范围
    if (selection.rangeCount > 0) {
      const range = selection.getRangeAt(0)
      range.deleteContents() // 删除选中的内容
      content.value = editor.value.textContent.trim() // 更新 content.value 以反映删除后的文本
      fileStore.setFileContent(content.value) // 同步 Pinia store
      editor.value.textContent = content.value
      historyStack.value.push(content.value) // 将更新后的文本添加到历史堆栈中
    } else {
      // 没有选中任何内容，直接返回
      return
    }
  } else if (document.selection && document.selection.type !== 'Control') {
    // 对于旧版本的IE浏览器，使用 document.selection
    const range = document.selection.createRange()
    range.text = '' // 删除选中的内容
    content.value = editor.value.textContent.trim() // 更新 content.value 以反映删除后的文本
    fileStore.setFileContent(content.value) // 更新 Pinia store
    editor.value.textContent = content.value // 确保编辑器内容与 content.value 同步
    historyStack.value.push(content.value) // 将更新后的文本添加到历史堆栈中
  } else {
    // 如果浏览器不支持 window.getSelection 或 document.selection，直接返回
    return
  }
}
// 保存内容
const saveContent = () => {
  fileStore.setFileContent(content.value)
  ElMessage.success('保存成功~')
}
// 插入内容
// const insertContent = () => {
//   content.value += '这是插入的文本。\n'
//   editor.value.textContent = content.value
// }

// 一键总结（这里假设简单地截取前100个字符作为总结）
const summarizeContent = () => {
  console.log('总结', fileStore.fileContent)
  console.log(editor.value)
  content.value = fileStore.fileContent
  // content.value = content.value.slice(0, 100)
  // editor.value.textContent = content.value
}

// 撤销功能
const undoContent = () => {
  if (historyStack.value.length > 1) {
    historyStack.value.pop() // 弹出当前内容
    content.value = historyStack.value[historyStack.value.length - 1] // 恢复上一次内容
    editor.value.textContent = content.value
    ElMessage.success('撤销成功')
  }
}

// 点击编辑器区域自动聚焦
const focusEditor = () => {
  editor.value.focus()
}
defineExpose({
  content
})
</script>

<style scoped>
.dialog-box {
  /* border: 1px solid #ccc; */
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}

.tool-tab {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  margin-bottom: 10px;
  flex-wrap: nowrap; /* 防止换行 */
  overflow-x: auto; /* 水平滚动条 */
}

.tool-tab button {
  padding: 5px 10px;
  background-color: #5da8f9;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  flex-shrink: 0; /* 防止缩小 */
}

.tool-tab button:hover {
  background-color: #bcf1a5;
  color: #000;
}

.text-editor {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  /* position: relative; */
  /* min-height: 200px; */
  height: calc(100% - 40px);
  overflow-y: auto;
}

.editor-content {
  max-height: 100%;
  outline: none;
  border: none;
  resize: vertical;
  /* display: inline-flex; */
  /* justify-content: flex-end; */
  white-space: pre-wrap; /* 保留空白符序列，但是正常地进行换行 */
}

@media (max-width: 600px) {
  .tool-tab {
    flex-wrap: wrap; /* 适配移动端 */
  }

  .tool-tab button {
    flex: 1 1 calc(50% - 10px); /* 适配移动端 */
    margin-bottom: 5px;
  }
}
</style>
