from openai import OpenAI
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 读取环境变量
api_key = os.environ.get("api_key")
base_url = os.environ.get("base_url")
version_model = os.environ.get("version_model", "glm-4v-flash")

system_prompt = """你是一个专业的OCR文字识别工具。请严格按照以下规则:
1. 只输出图片中实际存在的文字内容,不要添加任何解释、评论或额外内容
2. 保持原文的格式、换行、缩进、标点符号等完全一致
3. 对于难以识别的文字,使用[...]标注,不要猜测或补充
4. 如果是表格,尽可能保持原有的表格结构
5. 如果是代码,保持原有的代码格式
6. 如果包含数学公式,使用LaTeX格式并用$$包裹
7. 如果内容包含多种语言,请准确识别并保持原有语言
8. 如果有标点符号,保持原有的标点使用
9. 如果有特殊符号或公式,确保准确转换为对应的格式
10.不要对文字内容进行任何修改、润色或重新组织
11.用户只能上传手写文字的图片，如果用户上传了其他非手写的图片，请直接输出:False
12.如果图片是违规敏感图片，请直接输出:False
"""

client = OpenAI(base_url=base_url, api_key=api_key)

# ai识图转文字
def image2text(img_base64):
    response = client.chat.completions.create(
        model=version_model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": img_base64
                        }
                    },
                    {
                        "type": "text",
                        "text": "首先判断这张图片是不是手写文字的图片，如果这个图片不是手写文字的图片或者是违规敏感的图片，直接输出:False。如果是请帮我识别这张图片中的文字内容,按照上述规则输出结果，确保输出结果的准确性且没有多余内容。"
                    }
                ]
            }
        ]
    )
    # print('结果',response.choices[0].message.content)
    return response.choices[0].message.content

