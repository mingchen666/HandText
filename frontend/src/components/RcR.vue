<template>
  <div class="verify-container">
    <input type="text" placeholder="请输入验证码" v-model="inputResult" class="input-container" />
    <canvas
      id="random-canvas"
      :width="canvasWidth"
      :height="canvasHeight"
      @click="getCaptcha"
    ></canvas>
  </div>
  <el-button @click="verifyResult">验证</el-button>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const canvasWidth = 84
const canvasHeight = 40
const result = ref(0) // 实际计算结果
const inputResult = ref('') // 用户输入结果
// 固定背景颜色选项
const backgroundColors = ['#FFD700', '#ADD8E6', '#90EE90', '#FFA07A', '#FFB6C1']
const randomBackgroundColor = () =>
  backgroundColors[Math.floor(Math.random() * backgroundColors.length)]

// 随机颜色
const randomColor = (min, max) => {
  const r = Math.floor(Math.random() * (max - min + 1)) + min
  const g = Math.floor(Math.random() * (max - min + 1)) + min
  const b = Math.floor(Math.random() * (max - min + 1)) + min
  return `rgb(${r},${g},${b})`
}

// 计算公式生成文本
const generateFormula = () => {
  const num1 = Math.floor(Math.random() * 10) + 1
  const num2 = Math.floor(Math.random() * 10) + 1
  const num3 = Math.floor(Math.random() * 10) + 1
  const operators = ['+', '-', '*']
  const op1 = operators[Math.floor(Math.random() * operators.length)]
  const op2 = operators[Math.floor(Math.random() * operators.length)]
  return `${num1} ${op1} ${num2} ${op2} ${num3} =`
}

// 绘制文本
const drawText = (ctx, text) => {
  const fontSize = 16
  const x = canvasWidth / 2
  const y = canvasHeight / 2
  ctx.font = `${fontSize}px Arial`
  ctx.fillStyle = 'black' // 固定为黑色
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(text, x, y)
}

// 随机线
const drawLine = (ctx) => {
  for (let i = 0; i < 5; i++) {
    const x1 = Math.random() * canvasWidth
    const y1 = Math.random() * canvasHeight
    const x2 = Math.random() * canvasWidth
    const y2 = Math.random() * canvasHeight
    ctx.beginPath()
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.strokeStyle = randomColor(100, 200)
    ctx.lineWidth = Math.random() * 2 + 1
    ctx.stroke()
  }
}

// 随机点
const drawDot = (ctx) => {
  for (let i = 0; i < 100; i++) {
    const x = Math.random() * canvasWidth
    const y = Math.random() * canvasHeight
    ctx.beginPath()
    ctx.arc(x, y, Math.random() * 2 + 1, 0, Math.PI * 2, true)
    ctx.fillStyle = randomColor(150, 255)
    ctx.fill()
  }
}

// 绘图,并且返回一个计算结果
const drawPic = () => {
  const canvas = document.getElementById('random-canvas')
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, canvasWidth, canvasHeight)

  // 绘制背景
  ctx.fillStyle = randomBackgroundColor()
  ctx.fillRect(0, 0, canvasWidth, canvasHeight)

  drawLine(ctx)
  drawDot(ctx)

  // 绘制文字
  const formula = generateFormula()

  drawText(ctx, formula)
  // 返回实际计算结果
  console.log(eval(formula.replace('=', '')))
  return eval(formula.replace('=', ''))
}
// 检验验证码正确性
const verifyResult = () => {
  if (Number(inputResult.value) !== result.value) {
    ElMessage.error('验证码错误')
    return false
  }

  ElMessage.success(`验证码正确`)
  return Number(inputResult.value) === result.value
}
// 获取验证码图片结果
const getCaptcha = () => {
  result.value = drawPic()
}

onMounted(() => {
  getCaptcha()
})
const porps=defineProps({
  // 验证码
  captcha: {
    type: String,
    default: '1234'
  }
})
// 暴露方法
defineExpose({ drawPic, verifyResult })
</script>

<style scoped>
#random-canvas {
  /* width: 30%; */
  border: 2px solid #ccc;
  border-radius: 5px;
}
.verify-container {
  width: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: aqua; */
}
.input-container {
  width: 60%; /* 输入框宽度 */
  padding: 10px; /* 内边距 */
  margin: 0 10px 0 0;
  font-size: 16px; /* 字体大小 */
  border: 1px solid #ccc; /* 边框 */
  border-radius: 5px; /* 圆角 */
  background-color: #fff; /* 背景色 */
  color: #333; /* 文字颜色 */
  transition:
    border-color 0.3s,
    box-shadow 0.3s; /* 平滑过渡 */
}

/* 当输入框获得焦点时 */
.input-container:focus {
  border-color: #007bff; /* 改变边框颜色 */
  outline: none; /* 去掉默认的焦点轮廓 */
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* 添加阴影 */
}

/* 占位符颜色 */
::placeholder {
  color: #aaa; /* 占位符颜色 */
  opacity: 1; /* Firefox浏览器需要设置此属性 */
}
</style>
