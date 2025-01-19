<template>
  <div class="container flex justify-center h-full">
    <div class="left-container flex">
      <router-view></router-view>
      <!-- <ConfigCom /> -->
    </div>
    <div class="right-container flex">
      <PreviewCom />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import PreviewCom from './components/PreviewCom.vue'
</script>
<style scoped>
/* .container > div {
  flex: 1;
} */
.left-container {
  flex: 1;
}
.right-container {
  flex: 1;
  /* background-color: rgb(157, 242, 174); */
}
/* 适配移动端 */
@media (max-width: 768px) {
  .container {
    flex-direction: column; /* 在移动设备上保持按列排列 */
  }

  .left-container {
    order: 1; /* 将左侧容器放在底部 */
  }

  .right-container {
    order: 2; /* 将右侧容器放在顶部 */
  }
}
</style>
