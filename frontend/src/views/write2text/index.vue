<template>
  <div class="container">
    <div class="left-container"><LeftUpload /></div>
    <div class="right-container"><RightPreview /></div>
  </div>
</template>

<script setup>
import LeftUpload from './components/LeftUpload.vue'
import RightPreview from './components/RightPreview.vue'
</script>
<style scoped>
.container {
  display: flex;
  height: 100vh;
  /* flex-direction: row; */
  gap: 10px;
  /* justify-content: space-between; */
}
.left-container,
.right-container {
  flex: 1;
  height: 100%;
}
</style>
