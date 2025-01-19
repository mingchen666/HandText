<template>
  <!-- 底部信息 -->
  <el-footer class="footer">
    <p class="footer-text">© 2025 Handtext</p>
    <p class="footer-text">
      联系我:
      <a href="https://github.com/mingchen666">mingchen666</a>
    </p>
  </el-footer>
</template>

<script setup></script>

<style scoped>
.footer {
  text-align: center;
  padding: 20px;
  background-color: var(--el-bg-color);
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
}

.footer-text {
  font-size: 0.9rem;
  color: var(--el-text-color-secondary);
  margin: 5px 0;
}

.footer-text a {
  color: var(--el-color-primary);
  text-decoration: none;
}

.footer-text a:hover {
  text-decoration: underline;
}
</style>
