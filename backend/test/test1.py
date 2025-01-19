import requests

# 定义 API 的 URL
url = "http://localhost:5000/api/generate_handwriting"


# 定义请求的表单数据
data = {
    "text": "这是一个示例文本。",
    "font_size": "24",
    "line_spacing": "30",
    "fill": "(0, 0, 0, 225)",  # 黑色
    "left_margin": "10",
    "top_margin": "10",
    "right_margin": "10",
    "bottom_margin": "10",
    "word_spacing": "5",
    "line_spacing_sigma": "0",
    "font_size_sigma": "0",
    "word_spacing_sigma": "0",
    "perturb_x_sigma": "0",
    "perturb_y_sigma": "0",
    "perturb_theta_sigma": "0",
    "preview": "true",
    "pdf_save": "false"
}

# 发送 POST 请求
response = requests.post(url, data=data)

# 检查响应状态码
if response.status_code == 200:
    # 确认响应内容类型是图片
    content_type = response.headers.get('content-type')
    if 'image' in content_type:
        # 保存图片
        with open("preview.png", "wb") as f:
            f.write(response.content)
        print("预览图像已保存为 preview.png")
    else:
        print(f"响应内容类型不是图片，内容类型: {content_type}")
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
