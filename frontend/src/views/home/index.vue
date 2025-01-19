<template>
  <div class="home-page">
    <!-- 首页 Banner -->
    <div class="banner">
      <div class="banner-content">
        <h1 class="banner-title">Handtext</h1>
        <p class="banner-subtitle">手写文字/文本</p>
        <el-button class="btn-start" type="primary" size="large" @click="startNow">
          {{ $t('Start now') }}
        </el-button>
      </div>
      <div class="banner-wave"></div>
    </div>

    <!-- 功能介绍 -->
    <div class="features-section">
      <h2 class="section-title">{{ $t('core features') }}</h2>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card class="feature-card" shadow="hover">
            <el-icon :size="50" class="feature-icon"><Document /></el-icon>
            <h3 class="feature-title">{{ $t('handwriting text recognition') }}</h3>
            <p class="feature-description">
              {{
                $t(
                  'Upload handwritten images and quickly recognize them as text, supporting various image formats.'
                )
              }}
            </p>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="feature-card" shadow="hover">
            <el-icon :size="50" class="feature-icon"><Upload /></el-icon>
            <h3 class="feature-title">{{ $t('text to handwriting') }}</h3>
            <p class="feature-description">
              {{
                $t(
                  'Support uploading Word, TXT and other files, and convert them into handwritten style.'
                )
              }}
            </p>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card class="feature-card" shadow="hover">
            <el-icon :size="50" class="feature-icon"><Setting /></el-icon>
            <h3 class="feature-title">{{ $t('efficient and accurate') }}</h3>
            <p class="feature-description">
              {{
                $t('Based on advanced LLMs, it offers fast recognition speed and high accuracy.')
              }}
            </p>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 使用步骤 -->
    <div class="steps-section">
      <h2 class="section-title">{{ $t('How to use') }}</h2>
      <el-steps :active="3" align-center>
        <el-step
          :title="$t('Upload file')"
          :description="$t('Select handwritten image or upload file')" />
        <el-step
          :title="$t('System processing')"
          :description="$t('Autonomous recognition or conversion of content')" />
        <el-step
          :title="$t('Get results')"
          :description="$t('Download or copy the recognized text')" />
      </el-steps>
    </div>

    <!-- 开源介绍 -->
    <div class="open-source-section">
      <h2 class="section-title">{{ $t('Open source project') }}</h2>
      <p class="open-source-description">
        {{
          $t(
            'This project is completely open source, with publicly available code, and contributions and feedback are welcome. You can find our code repository on GitHub: GitHub Repository.'
          )
        }}
        <a href="https://github.com/mingchen666/HandText" target="_blank">
          {{ $t('GitHub Repository') }}
        </a>
      </p>
    </div>

    <!-- 用户评价 -->
    <div v-if="false" class="testimonials-section">
      <h2 class="section-title">{{ $t('User reviews') }}</h2>
      <el-row :gutter="20">
        <!-- 显示前五个评价 -->
        <el-col v-for="(testimonial, index) in testimonials.slice(0, 5)" :key="index" :span="8">
          <el-card class="testimonial-card" shadow="hover">
            <div class="testimonial-header">
              <el-avatar :size="50" :src="testimonial.avatar" class="testimonial-avatar" />
              <div class="testimonial-info">
                <h3 class="testimonial-name">{{ testimonial.name }}</h3>
                <el-rate v-model="testimonial.rating" disabled />
              </div>
            </div>
            <p class="testimonial-text">{{ testimonial.text }}</p>
          </el-card>
        </el-col>
        <!-- 显示“查看更多评价”卡片 -->
        <el-col :span="8">
          <el-card class="testimonial-card more-card" shadow="hover">
            <div class="testimonial-more">
              <el-icon :size="50" class="more-icon"><More /></el-icon>
              <p class="more-text">{{ $t('View more reviews') }}</p>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Document, Upload, Setting, More } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'
const router = useRouter()

// 用户评论
const testimonials = ref([
  {
    name: '张三',
    avatar: 'https://via.placeholder.com/50',
    rating: 5,
    text: '这个工具太棒了！识别速度快，准确率高，完全满足我的需求。'
  },
  {
    name: '李四',
    avatar: 'https://via.placeholder.com/50',
    rating: 4,
    text: '文件上传转手写的功能非常实用，帮我节省了大量时间。'
  },
  {
    name: '王五',
    avatar: 'https://via.placeholder.com/50',
    rating: 5,
    text: '界面简洁美观，操作简单，强烈推荐！'
  },
  {
    name: '赵六',
    avatar: 'https://via.placeholder.com/50',
    rating: 4,
    text: '识别效果非常好，尤其是手写文字的识别准确率很高。'
  },
  {
    name: '孙七',
    avatar: 'https://via.placeholder.com/50',
    rating: 5,
    text: '非常方便的工具，支持多种文件格式，强烈推荐！'
  }
])

const startNow = () => {
  router.push('/write/text')
}
</script>

<style scoped>
.btn-start {
  padding: 15px 30px;
  font-size: 16px;
}

.home-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: var(--el-bg-color-page);
}

.banner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  background: linear-gradient(135deg, var(--el-color-primary), var(--el-color-primary-light-3));
  color: var(--el-color-white);
  text-align: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

.banner-content {
  max-width: 800px;
  z-index: 1;
}

.banner-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 20px;
  animation: fadeInDown 1s ease;
}

.banner-subtitle {
  font-size: 1.5rem;
  margin-bottom: 30px;
  animation: fadeInUp 1s ease;
}

.banner-wave {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 200%;
  height: 100px;
  background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23ffffff" fill-opacity="1" d="M0,160L48,149.3C96,139,192,117,288,128C384,139,480,181,576,181.3C672,181,768,139,864,128C960,117,1056,139,1152,149.3C1248,160,1344,160,1392,160L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>')
    repeat-x;
  animation: wave 10s linear infinite;
}

.features-section {
  padding: 60px 20px;
  background-color: var(--el-bg-color);
}

.section-title {
  font-size: 2rem;
  font-weight: bold;
  color: var(--el-text-color-primary);
  text-align: center;
  margin-bottom: 40px;
  animation: fadeIn 1s ease;
}

.feature-card {
  text-align: center;
  padding: 30px;
  border: none;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  background-color: var(--el-bg-color);
}

.feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  margin-bottom: 20px;
  color: var(--el-color-primary);
  animation: bounce 2s infinite;
}

.feature-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--el-text-color-primary);
  margin-bottom: 15px;
}

.feature-description {
  font-size: 1rem;
  color: var(--el-text-color-regular);
  line-height: 1.6;
}

.steps-section {
  padding: 60px 20px;
  background-color: var(--el-bg-color-page);
}

.open-source-section {
  padding: 60px 20px;
  background-color: var(--el-bg-color);
  text-align: center;
}

.open-source-description {
  font-size: 1.2rem;
  color: var(--el-text-color-regular);
  line-height: 1.6;
}

.open-source-description a {
  color: var(--el-color-primary);
  text-decoration: none;
}

.open-source-description a:hover {
  text-decoration: underline;
}

.testimonials-section {
  padding: 60px 20px;
  background-color: var(--el-bg-color);
}

.el-row {
  margin-bottom: 0; /* 移除行的底部间距 */
}

.el-col {
  margin-bottom: 0; /* 移除列的底部间距 */
}

.testimonial-card {
  padding: 20px;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
  margin-bottom: 20px; /* 添加卡片之间的间距 */
  display: flex; /* 使用Flexbox布局 */
  flex-direction: column; /* 内容垂直排列 */
  justify-content: space-between; /* 内容在垂直方向上均匀分布 */
  height: 100%; /* 确保卡片高度一致 */
}

.testimonial-card:last-child {
  margin-bottom: 0; /* 移除最后一个卡片的底部间距 */
}

.more-card {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.testimonial-more {
  text-align: center;
}

.more-icon {
  color: var(--el-color-primary);
}

.more-text {
  font-size: 1rem;
  color: var(--el-text-color-regular);
}

/* 动画效果 */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

@keyframes wave {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style>
