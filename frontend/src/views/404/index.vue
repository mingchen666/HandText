<template>
  <div class="not-found">
    <el-result icon="warning" title="404" sub-title="糟糕，您访问的页面不存在！">
      <template #extra>
        <el-button type="primary" @click="goHome">返回首页</el-button>
      </template>
    </el-result>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NotFound',
  methods: {
    goHome() {
      this.$router.push('/')
    }
  }
})
</script>

<style scoped>
.not-found {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}
</style>
