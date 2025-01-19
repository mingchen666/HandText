import { defineStore } from 'pinia'
import { ref } from 'vue'
export const useAuthStore = defineStore(
  'auth',
  () => {
    const isLogin = ref(false)
    // 同意图片上传条款
    const isAgreeImageTerms = ref(false)
    const updateAgreeImageTerms = (val) => {
      isAgreeImageTerms.value = val
    }
    const login = () => {
      isLogin.value = true
    }
    const logout = () => {
      isLogin.value = false
    }
    return { isAgreeImageTerms, isLogin, login, logout, updateAgreeImageTerms }
  },
  {
    persist: true
    // persist: {
    //   paths: ['isLogin']
    // }
  }
)
