<template>
<div class="h-full aside" :class="{ collapsed: isCollapse }">
    <el-menu default-active="/" class="el-menu h-full" :collapse="isCollapse" router>
      <el-menu-item index="/">
        <el-icon><Home /></el-icon>
        <template #title>{{$t('menu.home')}}</template>
      </el-menu-item>
      <el-sub-menu index="2">
        <template #title>
          <el-icon><TextWrite /></el-icon>
          <span>{{$t('menu.text_to_handwriting')}}</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/write/text">{{$t('menu.text_to_handwriting_items.text_to_handwriting_text')}}</el-menu-item>
          <el-menu-item index="/write/file">{{$t('menu.text_to_handwriting_items.text_to_handwriting_file')}}</el-menu-item>
        </el-menu-item-group>
      </el-sub-menu>
      <el-menu-item index="/write2text">
        <el-icon size="26"><WriteText /></el-icon>
        <template #title>{{$t('menu.handwriting_to_text')}}</template>
      </el-menu-item>
      <!-- <el-sub-menu index="3">
        <template #title>
          <el-icon><location /></el-icon>
          <span>等待添加</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1">等待添加~</el-menu-item>
          <el-menu-item index="3-2">等待添加~</el-menu-item>
        </el-menu-item-group>
      </el-sub-menu> -->

  
    </el-menu>
  </div>
</template>

<script setup>
import TextWrite from '@/components/icons/TextWrite.vue'
import Home from '@/components/icons/Home.vue'
import WriteText from '@/components/icons/WriteText.vue'
import Suggest from '@/components/icons/Suggest.vue'
import Person from '@/components/icons/Person.vue'
import Question from '@/components/icons/Question.vue'
const props = defineProps({
  isCollapse: {
    type: Boolean,
    default: true
  }
})

// const handleOpen = (key, keyPath) => {
//   console.log(key, keyPath)
// }

// const handleClose = (key, keyPath) => {
//   console.log(key, keyPath)
// }
</script>

<style scoped>
.el-menu {
  border: none;
}
.nav-aside.collapsed {
  width: 100%; /* 折叠时的宽度 */
}
.aside {
  min-height: 100vh;
  height: 100%;
  /* border-right: 1px solid #b3c5ef; */

  /* background-color: aqua; */
}
</style>
