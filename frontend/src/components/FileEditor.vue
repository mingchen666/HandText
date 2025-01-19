<template>
  <div>
    <Popup ref="popupRef" v-model:visible="popupVisible" :title="'文件解析预览'">
      <TextEditor ref="textEditorRef" />
      <!-- <button @click="test">ahhhhhhh</button> -->
    </Popup>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import TextEditor from './texteditor/TextEditor.vue'
import Popup from './Popup.vue'
const popupRef = ref(null)
const textEditorRef = ref(null)
const popupVisible = ref(false)
// const test = () => {
//   popupVisible.value = true
//   console.log(textEditorRef.value.content)
// }
const open = () => {
  popupVisible.value = true
}
const close = () => {
  popupVisible.value = false
}
// onMounted(() => {
//   popupVisible.value = true
// })
defineExpose({
  open,
  close
})
</script>
<style scoped></style>
