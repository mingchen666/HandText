<!-- 自定义弹出框 -->
<template>
  <transition name="modal">
    <div v-if="visible" class="overlay" @click.self="close">
      <div class="popup" :style="{ width: width, height: height }">
        <!-- 头部 -->
        <header class="popup-header">
          <slot name="header">
            <h2>{{ title }}</h2>
          </slot>
          <button class="popup-close-btn" @click="close">&times;</button>
        </header>
        <!-- 主体部分 -->
        <section class="popup-body">
          <slot>主体内容</slot>
        </section>
        <!-- 底部 -->
        <footer class="popup-footer">
          <slot name="footer">
            <button class="popup-btn" @click="comfirm">确认</button>
            <!-- <button class="popup-btn" @click="close">取消</button> -->
          </slot>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script setup>

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
    default: false
  },
  width: {
    type: String,
    default: '1000px'
  },
  height: {
    type: String,
    default: '500px'
  },
  title: {
    type: String,
    default: '弹出框'
  }
})

const emit = defineEmits(['update:visible'])

function open() {
  emit('update:visible', true)
}
function comfirm() {
  emit('update:visible', false)
}

function close() {
  emit('update:visible', false)
}
// 对外暴露
defineExpose({
  open,
  close
})
</script>

<style scoped>
/* 背景遮罩层样式 */
.overlay {
  position: fixed; /* 固定定位，覆盖整个屏幕 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明黑色背景 */
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: center;
  align-items: center; 
  z-index: 1000; /* 确保遮罩层在最上层 */
}

/* 弹出框容器样式 */
.popup {
  background-color: #fff; /* 白色背景 */
  padding: 20px; /* 内边距 */
  border-radius: 8px; /* 圆角 */
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  width: 100%; /* 宽度占满父容器 */
  font-family: 'Arial', sans-serif; /* 字体设置 */
  overflow: hidden; /* 隐藏溢出内容 */
  display: flex; /* 使用 Flexbox 布局 */
  flex-direction: column; /* 垂直排列子元素 */
  justify-content: space-between; /* 子元素之间均匀分布 */
}

/* 弹出框头部样式 */
.popup-header {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: space-between; /* 子元素两端对齐 */
  align-items: center; /* 子元素垂直居中 */
  margin-bottom: 20px; /* 底部外边距 */
  font-size: 1rem; /* 字体大小 */
  font-weight: bold; /* 加粗字体 */
  color: #333; /* 字体颜色 */
}

/* 关闭按钮样式 */
.popup-close-btn {
  background: none; /* 无背景 */
  border: none; /* 无边框 */
  font-size: 2.5rem; /* 字体大小 */
  cursor: pointer; /* 鼠标悬停时显示为指针 */
  color: #999; /* 字体颜色 */
  transition: color 0.3s ease; /* 颜色变化过渡效果 */
}

/* 关闭按钮悬停效果 */
.popup-close-btn:hover {
  color: #e21c1c; /* 悬停时字体颜色变为红色 */
}

/* 弹出框主体内容样式 */
.popup-body {
  margin-bottom: 20px; /* 底部外边距 */
  font-size: 1rem; /* 字体大小 */
  color: #555; /* 字体颜色 */
  flex: 1; /* 占据剩余空间 */
}

/* 弹出框底部样式 */
.popup-footer {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: flex-end; /* 子元素靠右对齐 */
}

/* 弹出框按钮样式 */
.popup-btn {
  background-color: #007bff; /* 背景颜色 */
  color: white; /* 字体颜色 */
  border: none; /* 无边框 */
  padding: 10px 20px; /* 内边距 */
  border-radius: 10px; /* 圆角 */
  cursor: pointer; /* 鼠标悬停时显示为指针 */
  transition: background-color 0.3s ease; /* 背景颜色变化过渡效果 */
  margin-left: 8px; /* 左侧外边距 */
}

/* 弹出框按钮悬停效果 */
.popup-btn:hover {
  background-color: #0056b3; /* 悬停时背景颜色变为深蓝色 */
}

/* 弹出框进入动画 */
.modal-enter-active,
.modal-leave-active {
  transition:
    opacity 0.4s ease-out,
    /* 透明度变化过渡效果 */ transform 0.4s ease-out; /* 变换变化过渡效果 */
}

/* 弹出框进入前和离开后的状态 */
.modal-enter-from,
.modal-leave-to {
  opacity: 0; /* 完全透明 */
  transform: scale(0.9); /* 缩放到 0.9 倍 */
}
</style>
