<template>
  <transition name="message-fade">
    <div
      v-if="visible"
      :class="['message', `message--${type}`]"
      :style="styles"
    >
      <i :class="iconClass"></i>
      <span>{{ message }}</span>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';

const props = defineProps({
  message: String,
  type: {
    type: String,
    default: 'info',
  },
  duration: {
    type: Number,
    default: 3000,
  },
  color: {
    type: String,
    default: '',
  },
});

const visible = ref(false);
const styles = computed(() => ({
  backgroundColor: props.color || getDefaultBackgroundColor(props.type),
}));

function show() {
  visible.value = true;
}

function hide() {
  visible.value = false;
}

onMounted(() => {
  show();
  setTimeout(hide, props.duration);
});

onUnmounted(() => {
  hide();
});

function getDefaultBackgroundColor(type) {
  switch (type) {
    case 'success':
      return '#e1f3d8';
    case 'warning':
      return '#fce788';
    case 'error':
      return '#fde2e2';
    default:
      return '#f9f9f9';
  }
}

function getIconClass(type) {
  switch (type) {
    case 'success':
      return 'el-icon-success';
    case 'warning':
      return 'el-icon-warning';
    case 'error':
      return 'el-icon-error';
    default:
      return 'el-icon-info';
  }
}

const iconClass = computed(() => getIconClass(props.type));
</script>

<style scoped>
.message {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px;
  border-radius: 4px;
  background-color: #f9f9f9;
  box-shadow: rgba(0,0,0,0.1) -4px -4px -4px rgba(255,255,255,1), rgba(0,0,0,0.3) -4px -4px -4px inset;
}

.message--info .el-icon-info::before {
  content: '\e7a8';
}

.message--success .el-icon-success::before {
  content: '\e66b';
}

.message--warning .el-icon-warning::before {
  content: '\e66a';
}

.message--error .el-icon-error::before {
  content: '\e66c';
}

.message-fade-enter-active,
.message-fade-leave-active {
 transition: opacity .3s ease-in-out, transform .3s ease-in-out;
}

.message-fade-enter-from,
.message-fade-leave-to {
 opacity: .5;
}
</style>
