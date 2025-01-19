<template>
  <div class="header-nav">
    <div class="right-container">
      <div class="github">
        <a href="https://github.com/mingchen666/HandText" target="_blank">
          <!-- <el-icon size="24" > -->
          <Github />
          <!-- </el-icon> -->
        </a>
      </div>
      <LanguageSwitch></LanguageSwitch>
      <ThemeSwitcher></ThemeSwitcher>

      <el-avatar :src="avatarUrl" />
    </div>
  </div>
</template>

<script setup>
import avatarUrl from '@/assets/logo.jpg'
import ThemeSwitcher from '@/components/ThemeSwitch.vue'
import LanguageSwitch from '@/components/LanguageSwitch.vue'
import Github from '@/components/icons/Github.vue'
const handleSelect = (key, keyPath) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.header-nav {
  display: flex;
  justify-content: flex-end;
  /* 将内容推到右侧 */
  align-items: center;
  padding: 10px 20px;
  border-bottom: 1px solid #131212;
}

.right-container {
  display: flex;
  gap: 15px;
  /* 增加按钮之间的间距 */
  align-items: center;
}

.github {
  margin-right: 0;
  cursor: pointer;
  background: none;
}
</style>
