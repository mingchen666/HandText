<template>
  <div class="dropdown" @mouseenter="showDropdown" @mouseleave="hideDropdown">
    <button class="dropdown-toggle" @click="toggleDropdown">
      <Translate />
    </button>
    <div v-if="dropdownVisible" class="dropdown-content">
      <a href="#" @click="selectLanguage('zh')">简体中文</a>
      <a href="#" @click="selectLanguage('en')">English</a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Translate from './icons/Translate.vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const dropdownVisible = ref(false)

const showDropdown = () => {
  dropdownVisible.value = true
}

const hideDropdown = () => {
  dropdownVisible.value = false
}

const toggleDropdown = () => {
  dropdownVisible.value = !dropdownVisible.value
}

const selectLanguage = (language) => {
  locale.value = language
  hideDropdown()
}
</script>

<style scoped>
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0 5px;
  font-size: 16px;
}

.dropdown-toggle:hover {
  background-color: transparent; /* 保持透明背景 */
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border-radius: 5px;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: center;
}

.dropdown-content a:hover {
  color: rgb(16, 99, 242);
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>