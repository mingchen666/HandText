import ast
import io
import os
import shutil
import tempfile
import time

from PIL import Image, ImageFont
from flask import request, jsonify, send_file, make_response
from flask_restful import Resource
from handright import Template, handwrite

from .response import ApiResponse
from ..extensions import limiter
from ..utils.image import create_notebook_image
from ..utils.file import get_fonts_list, generate_pdf


def custom_rate_limit(limit):
    response = make_response(
        jsonify(
            code=429,
            status='fail',
            error="Too Many Requests",
            message=f"Rate limit {limit.limit} exceeded"
        ),
        429
    )
    return response


class WriteResource(Resource):
    @limiter.limit(limit_value="10 per minute", on_breach=custom_rate_limit)  # 每分钟最多10次请求
    def post(self):
        """
        生成手写字体图像或PDF。
        根据用户提供的文本和样式信息，生成手写字体图像或PDF文件。如果用户选择生成图像，
        可以选择保存为ZIP文件或单张图像。如果用户选择生成PDF，则将所有图像合并为一个PDF文件。
        """
        # logger.info("已经进入generate_handwriting")
        # if enable_user_auth.lower() == "true":
        #     if "username" not in session:
        #         return jsonify({"status": "error", "message": "You haven't login."}), 500
        # try:
        # 先获取 form 数据
        data = request.form
        print('表单字段', data)
        required_form_fields = [
            "text",
            "font_size",
            "line_spacing",
            "fill",
            "left_margin",
            "top_margin",
            "right_margin",
            "bottom_margin",
            "word_spacing",
            "line_spacing_sigma",
            "font_size_sigma",
            "word_spacing_sigma",
            "perturb_x_sigma",
            "perturb_y_sigma",
            "perturb_theta_sigma",
            "preview",
        ]
        # "height","width",

        for field in required_form_fields:
            if field not in data:
                return ApiResponse.error(f"缺少{field}请求参数字段")
            # else:
            #     print('存在')
            # logger.info(f"{field}: {data[field]}")  # 打印具体的 form 字段值
            # 如果存在height和width，就创建一个新的背景图     todo
            # height=int(data["height"]),
            # width=int(data["width"]),

        # 如果用户提供了宽度和高度，创建一个新的笔记本背景图像
        if "width" in data and "height" in data:
            line_spacing = int(data.get("line_spacing", 30))
            top_margin = int(data.get("top_margin", 0))
            bottom_margin = int(data.get("bottom_margin", 0))
            left_margin = int(data.get("left_margin", 0))
            right_margin = int(data.get("right_margin", 0))
            width = int(data["width"])
            height = int(data["height"])
            font_size = int(data.get("font_size", 0))
            isUnderlined = data.get("isUnderlined", False)
            background_image = create_notebook_image(
                width,
                height,
                line_spacing,
                top_margin,
                bottom_margin,
                left_margin,
                right_margin,
                font_size,
                isUnderlined,
            )
        # 否则使用用户上传的背景图像
        else:

            background_image = request.files.get("background_image")
            if background_image is None:
                return ApiResponse.error(f"缺少 background_image 请求参数字段")
            image_data = io.BytesIO(background_image.read())

            # 使用 PIL 打开图像
            try:
                background_image = Image.open(image_data)

                # 如果图像包含 Alpha 通道（模式为 'RGBA' 或 'LA'），则去除 Alpha 通道
                if background_image.mode in ("RGBA", "LA"):
                    # 将图像转换为 'RGB' 模式
                    background_image = background_image.convert("RGB")

            except IOError:
                return ApiResponse.error(f"打开图像出错,非法图片格式！")
        text_to_generate = data["text"]

        # if data["preview"] == "true":
        #     # 截短字符，只生成一面
        #     preview_length = 300  # 可以调整为所需的预览长度
        #     text_to_generate = text_to_generate[:preview_length]

        # 从表单中获取字体文件并处理 7.4
        if "font_file" in request.files:
            font = request.files["font_file"].read()
            font = ImageFont.truetype(io.BytesIO(font), size=int(data["font_size"]))
        else:
            font_option = data["font_option"]
            font_file_names = get_fonts_list('app/public/fonts')
            # logger.info(f"font_option: {font_option}")
            # logger.info(f"font_file_names: {font_file_names}")
            if font_option in font_file_names:
                # 确定字体文件的完整路径
                font_path = os.path.join("app/public/fonts", font_option)
                # logger.info(f"font_path: {font_path}")
                # 打开字体文件并读取其内容为字节
                with open(font_path, "rb") as f:
                    font_content = f.read()
                # 通过 io.BytesIO 创建一个 BytesIO 对象，然后使用 ImageFont.truetype 从字节中加载字体
                font = ImageFont.truetype(
                    io.BytesIO(font_content), size=int(data["font_size"])
                )
            else:
                return ApiResponse.error(f"缺少字体文件!")
        # 创建模板
        template = Template(
            # fill=tuple(data["fill"]),# 默认黑色
            background=background_image,
            font=font,
            line_spacing=int(data["line_spacing"]),  # + int(data["font_size"])
            fill=ast.literal_eval(data["fill"][4:-1]),  # Ignore the alpha value
            # fill=(0),#如果feel是只有一个颜色的话那么在改变墨水的时候会导致R变化而GB不变化,颜色会变红 9.17
            left_margin=int(data["left_margin"]),
            top_margin=int(data["top_margin"]),
            right_margin=int(data["right_margin"]) - int(data["word_spacing"]) * 2,
            bottom_margin=int(data["bottom_margin"]),
            word_spacing=int(data["word_spacing"]),
            line_spacing_sigma=int(data["line_spacing_sigma"]),  # 行间距随机扰动
            font_size_sigma=int(data["font_size_sigma"]),  # 字体大小随机扰动
            word_spacing_sigma=int(data["word_spacing_sigma"]),  # 字间距随机扰动
            end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
            perturb_x_sigma=int(data["perturb_x_sigma"]),  # 笔画横向偏移随机扰动
            perturb_y_sigma=int(data["perturb_y_sigma"]),  # 笔画纵向偏移随机扰动
            perturb_theta_sigma=float(data["perturb_theta_sigma"]),  # 笔画旋转偏移随机扰动
            strikethrough_probability=float(data["strikethrough_probability"]),  # 删除线概率
            strikethrough_length_sigma=float(
                data["strikethrough_length_sigma"]
            ),  # 删除线长度随机扰动
            strikethrough_width_sigma=float(data["strikethrough_width_sigma"]),  # 删除线宽度随机扰动
            strikethrough_angle_sigma=float(data["strikethrough_angle_sigma"]),  # 删除线角度随机扰动
            strikethrough_width=float(data["strikethrough_width"]),  # 删除线宽度
            ink_depth_sigma=float(data["ink_depth_sigma"]),  # 墨水深度随机扰动
        )

        # 创建一个BytesIO对象，用于保存.zip文件的内容
        # logger.info(f"data[pdf_save]: {data['pdf_save']}")
        # 保存为pdf
        if not data["pdf_save"] == "true":
            images = handwrite(text_to_generate, template)
            # logger.info("handwrite initial images generated successfully")
            # 创建临时目录
            temp_dir = tempfile.mkdtemp()
            unique_filename = "images_" + str(time.time())
            zip_path = f"./temp/{unique_filename}.zip"
            # zip_path = os.path.join(temp_dir, unique_filename + ".zip")
            try:
                for i, im in enumerate(images):
                    # 保存每张图像到临时目录
                    image_path = os.path.join(temp_dir, f"{i}.png")
                    im.save(image_path)
                    # logger.info(f"Image {i} saved successfully")
                    del im  # 释放内存

                    if data["preview"] == "true":
                        # 如果需要预览图像，直接发送文件
                        return send_file(image_path, mimetype="image/png")

                if not data["preview"] == "true":
                    # 创建ZIP文件

                    shutil.make_archive(zip_path[:-4], "zip", temp_dir)

                    # 发送文件，并在之后删除ZIP文件
                    response = send_file(
                        f"./temp/{unique_filename}.zip",
                        download_name="images.zip",
                        mimetype="application/zip",
                        as_attachment=True,
                    )
                    return response  # todo 这里缩进了4个
            finally:
                pass
                # try:
                #     # 确保删除临时目录
                #     if os.path.exists(temp_dir):
                #         shutil.rmtree(temp_dir)
                # except Exception as e:
                #     print(f"删除临时目录失败: {temp_dir}: {e}")
                #     # logger.error(f"Failed to delete temp directory {temp_dir}: {e}")
                # # 如果存在zip，删除zip文件
                # try:
                #     if os.path.exists(zip_path):
                #         os.remove(zip_path)
                # except Exception as e:
                #     print(f"删除zip文件: {zip_path}: {e}")
                    # logger.error(f"Failed to delete zip file {zip_path}: {e}")
        else:
            # logger.info("PDF generate")
            temp_pdf_file_path = None  # 初始化变量
            images = handwrite(text_to_generate, template)
            try:
                temp_pdf_file_path = generate_pdf(images=images)
                if temp_pdf_file_path is None:
                    return ApiResponse.error("Failed to generate PDF", 400)
                # 将文件路径存储在请求上下文中，以便稍后可以访问它
                request.temp_file_path = temp_pdf_file_path
                return send_file(
                    temp_pdf_file_path,
                    download_name="images.pdf",
                    mimetype="application/pdf",
                    as_attachment=True,
                    conditional=True,
                )
            finally:
                pass
            #     if temp_pdf_file_path is not None:  # 检查变量是否已赋值
            #         for _ in range(5):  # 尝试5次
            #             try:
            #                 os.remove(temp_pdf_file_path)  # 尝试删除文件
            #                 break  # 如果成功删除，跳出循环
            #             except Exception as e:  # 捕获并处理删除文件时可能出现的异常
            #                 logger.error(f"Failed to remove temporary PDF file: {e}")
            #                 time.sleep(1)
            # unique_filename = "images_" + str(time.time()) + ".zip"

            # # 如果用户选择了保存为PDF，将所有图片合并为一个PDF文件
            # pdf_bytes = handwrite(text_to_generate, template, export_pdf=True, file_path=unique_filename)
            # logger.info("pdf generated successfully")
            # # 返回PDF文件
            # # mysql_operation(pdf_io)
            # return send_file(
            #     pdf_bytes,
            #     # attachment_filename="images.pdf",
            #     download_name="images.pdf",
            #     mimetype="application/pdf",
            #     as_attachment=True,
            # )
