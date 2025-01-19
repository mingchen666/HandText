# 手写转文本
import base64
import os

from flask import request
from flask_restful import Resource

from .response import ApiResponse
from ..utils.llm import image2text


class Write2Text(Resource):
    def post(self):
        # 获取 form 数据
        data = request.form
        extra_content = data.get("extra_content", "")

        # 获取文件数据
        if 'image' not in request.files:
            return ApiResponse.error('未上传图片！')
        file = request.files['image']
        print('file:',file)
        if file.filename == "":
            return ApiResponse.error('图片为空！')

        # 保存到指定目录
        filepath = os.path.join("./uploads/write2text/images", file.filename)
        # 检查并创建目录
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 保存文件
        file.save(filepath)

        # 将文件转换为Base64编码
        with open(filepath, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        # 调用，解析识别结果
        result = image2text(encoded_string)
        if result == "False":
            return ApiResponse.invalid(message='图片不是手写文字！')
        return ApiResponse.success(result)

