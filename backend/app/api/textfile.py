import os
from flask import request, jsonify
from flask_restful import Resource
# from werkzeug.utils import secure_filename

from ..api.response import ApiResponse
from ..utils.file import read_pdf, read_docx


class TextResource(Resource):
    def post(self):
        """
        处理文本文件的API接口。
        该接口接收一个文件，支持.docx、.pdf、.doc、.txt和.rtf格式文件的处理。
        根据文件类型的不同，调用不同的处理函数来读取文件内容，并返回文本数据。
        Returns:
            如果文件读取成功，返回包含文本内容的JSON响应。
            如果文件读取失败或文件类型不支持，返回相应的错误信息和状态码。
        """
        # 检查请求中是否包含文件
        if "file" not in request.files:
            return ApiResponse.error('未上传文件！')

        file = request.files["file"]
        # 检查文件名是否为空
        if file.filename == "":
            return ApiResponse.error('文件为空！')

        # 检查文件类型，并尝试读取文件内容
        if file and (
                file.filename.endswith(".docx")
                or file.filename.endswith(".pdf")
                or file.filename.endswith(".doc")
                or file.filename.endswith(".txt")
                # or file.filename.endswith(".rtf")
        ):
            # 保留原始文件名
            filename = file.filename
            filepath = os.path.join("./uploads/text2write/files", filename)
            # 检查并创建目录
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)  # 确保目录存在
            file.save(filepath)
            text = ""
            try:
                # 根据不同的文件类型，调用相应的处理函数
                if file.filename.endswith(".docx"):
                    text = read_docx(filepath)
                elif file.filename.endswith(".pdf"):
                    text = read_pdf(filepath)
                elif file.filename.endswith(".txt") :
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                elif file.filename.endswith(".doc"):
                    return ApiResponse.error('doc文件暂不支持')
            except Exception as e:
                return ApiResponse.error( f"发生错误: {str(e)}")

            # 注释掉删除临时文件的部分
            # if os.path.exists(filepath):
            #     os.remove(filepath)
            #     print(f"{filepath} has been deleted.")
            #     # logger.info(f"{filepath} has been deleted.")
            # else:
            #     print(f"{filepath} does not exist.")
            #     # logger.error(f"{filepath} does not exist.")
            return ApiResponse.success(data={"text": text})
            # return jsonify({"text": text})

        return ApiResponse.error("非法文件类型!")
