# ✍️ HandText

[📄 English](./README.md)

## 📖 项目简介

🎉使用 **Vue3**和 **Flask**框架,
基于[📄 handwriting-web](https://github.com/14790897/handwriting-web)进行重构，优化代码结构、增强部分功能

---

## 🚀 主要功能

- **手写文字识别**：支持上传图片并提取其中的手写文字。🖼️➡️📝
- **手写字体生成**：将输入的文本转换为手写风格的图片或保存为PDF文件。📄➡️🖋️
- **文本编辑**：支持文件上传编辑功能。✂️📋💾
- **多语言支持**：支持中英文切换。🌐
- **主题切换**：支持亮色和暗色主题切换。🌞🌙

---

## 🛠️ 技术栈

### 前端
- **框架**：Vue3
- **状态管理**：Pinia
- **UI 组件库**：Element Plus
- **路由管理**：Vue-Router
- **国际化**：vue-i18n
- **HTTP库**：axios

### 后端
- **框架**：Flask
- **文件处理**：支持图片上传、文本生成和文件存储。
- **API 接口**：提供手写文字识别、文本生成等功能。

---

## 🚀 快速开始

### 前端部署


```bash

1. 克隆项目
git clone https://github.com/mingchen666/HandText.git
cd frontend
 
1. 安装依赖
npm install

3. 启动开发服务器
npm run dev
 
4. 打包
npm run build
```
 
### 后端部署
```bash

1. 进入后端目录
cd backend

2. 安装依赖
pip install -r requirements.txt

3. 在env文件中填写环境变量

3. 启动开发服务器
python app.py

```
 
## 📜 许可证

本项目采用 MIT 许可证
