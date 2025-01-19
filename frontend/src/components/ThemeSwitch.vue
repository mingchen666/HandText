<template>
  <div>
    <el-button v-if="!isDark" @click="toggleTheme" class="rounded-lg" color="#44bd87">
      <el-icon size="16"><Sunny /></el-icon> Light</el-button
    >
    <el-button v-else @click="toggleTheme" color="#44bd87" class="rounded-lg"
      ><el-icon size="16"><Moon /></el-icon> Dark</el-button
    >
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useDark, useToggle } from '@vueuse/core'
import { Sunny, Moon } from '@element-plus/icons-vue'
const isDark = ref(false)
const theDark = useDark()
const toggleDark = useToggle(theDark)
// 切换主题
const toggleTheme = () => {
  isDark.value = !isDark.value
  toggleDark()
}
</script>
<style scoped></style>
