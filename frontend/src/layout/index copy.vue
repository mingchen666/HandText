<script setup>
import { ref } from 'vue'
import ThemeSwitcher from '@/components/ThemeSwitch.vue'
import { Message, Setting, Delete } from '@element-plus/icons-vue'
import Aside from './components/Aside.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
const isCollapse = ref(false)
const toggleCollapse = () => {
  isCollapse.value = !isCollapse.value
}
</script>

<template>
  <el-container class="layout-container flex h-full">
    <!-- 侧边栏 -->
    <el-aside :class="{ collapsed: isCollapse }" class="h-full nav-aside">
      <Aside :isCollapse="isCollapse"></Aside>
      <!-- 侧边栏折叠按钮 -->
      <el-affix
        target=".nav-aside"
        class="toggle-com"
        @click="toggleCollapse"
        position="bottom"
        :offset="0">
        <!-- <div class="toggle-com" @click="toggleCollapse"> -->
        <span v-if="!isCollapse">
          <el-icon size="24"><ArrowLeftBold /></el-icon>
        </span>
        <span v-else>
          <el-icon size="24"><ArrowRightBold /></el-icon>
        </span>
        <!-- </div> -->
      </el-affix>
    </el-aside>

    <el-container class="h-full main-container">
      <!-- 头部 -->
      <el-header style="text-align: right">
        <Header></Header>
      </el-header>
      <!-- 主体 -->
      <el-main>
        <RouterView></RouterView>
      </el-main>
      <!-- 底部 -->
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </el-container>
</template>

<style scoped>
/* .layout-container > * {
  height: 100%;
} */
.layout-container .el-aside1 {
  height: 100%;
}
.layout-container .nav-aside {
  color: var(--el-text-color-primary);
  transition: width 0.3s;
  position: relative;
  width: 200px; /* 展开时的宽度 */
  overflow-x: hidden;
}

.layout-container .el-aside.collapsed {
  width: 64px; /* 折叠时的宽度 */
}

.layout-container .el-container {
  display: flex;
  flex-direction: column;
}

.layout-container .el-main {
  flex: 1;
}

.toggle-com {
  /* border: 2px solid red; */
  position: absolute;
  bottom: 0px;
  right: 5px;
  transform: translate(50%, -50%);
  cursor: pointer;
  z-index: 9999 !important;
  opacity: 1;
  transition: opacity 0.3s;
}

.nav-aside:hover .toggle-com {
  opacity: 1; /* 鼠标经过时显示 */
}
.main-container {
  border-left: 1px solid #b3c5ef;
}
</style>
