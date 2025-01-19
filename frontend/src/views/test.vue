<script setup>
import NumberCaptcha from '@/components/NumberCaptcha.vue'
import LanguageSwitch from '@/components/LanguageSwitch.vue'
import ThemeSwitch from '@/components/ThemeSwitch.vue'
import RcR from '@/components/RcR.vue'
import DialogBox from '@/components/DialogBox.vue'
import { ref } from 'vue'
import Popup from '@/components/Popup.vue'
import FileEditor from '@/components/FileEditor.vue'
const Num = ref(null)
const aa = () => {
  console.log(Num.value.canvasWidth)
}

// --------
const props = defineProps({
  buttonText: {
    type: String,
    default: '打开弹出框'
  },
  popupTitle: {
    type: String,
    default: '弹出框标题6'
  },
  popupContent: {
    type: String,
    default: '这里是弹出框的内容。'
  }
})

const popupRef = ref(null)

function togglePopup() {
  popupRef.value.open()
}

function closePopup() {
  popupRef.value.close()
}
const popupVisible = ref(false)

const dialogBox = ref(null)
const openPop = () => {
  // popupRef.value.open()
  dialogBox.value.open()
}
</script>
<template>
  <div>首页</div>
  <ThemeSwitch />
  <h1>{{ $t('hello') }}</h1>
  <h1>{{ $t('button.submit') }}</h1>
  <el-button type="success" @click="aa">Success</el-button>
  <br />
  <NumberCaptcha ref="Num" />
  <LanguageSwitch />
  <!-- <RcR /> -->
  <br />
  <div>分割线</div>
  <FileEditor ref="dialogBox" />
  <div>分割线</div>
  <!-- <button class="popup-trigger-btn" @click="togglePopup">{{ buttonText }}</button> -->
  <Popup ref="popupRef" v-model:visible="popupVisible" :title="popupTitle">
    <!-- <template #header>
      <h2>{{ popupTitle }}</h2>
    </template> -->
    <p>{{ popupContent }}</p>
    <!-- <template #footer>
      <button class="popup-btn" @click="closePopup">确认</button>
      <button class="popup-btn" @click="closePopup">取消</button>
    </template> -->
  </Popup>
  <button @click="openPop">打开弹出框</button>
</template>
