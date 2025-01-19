# 文件相关功能函数
import glob
import os
import time

import PyPDF2
from docx import Document
import tempfile
import shutil
from PIL import Image
import fitz  # PyMuPDF

# 根据图片生成pdf

def generate_pdf(images, output_dir='/output/pdf'):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    try:
        pdf_document = fitz.open()  # 创建一个新的空白PDF文档
        # 设置A4纸的尺寸和分辨率
        a4_width_in_inches = 8.3
        a4_height_in_inches = 11.7
        dpi = 300  # dots per inch
        a4_width_in_pixels = int(a4_width_in_inches * dpi)
        a4_height_in_pixels = int(a4_height_in_inches * dpi)

        for i, img in enumerate(images):
            # 调整图像大小以适应A4纸
            img_resized = img.resize((a4_width_in_pixels, a4_height_in_pixels), Image.LANCZOS)
            # 保存每张图像到输出目录
            temp_img_format = 'JPEG' if img.format == 'JPEG' else 'PNG'
            temp_img_extension = '.jpg' if img.format == 'JPEG' else '.png'
            temp_img_path = os.path.join(output_dir, f'image{i}{temp_img_extension}')
            img_resized.save(temp_img_path, format=temp_img_format, quality=85)

            # 创建新页面
            pdf_page = pdf_document.new_page(width=a4_width_in_pixels, height=a4_height_in_pixels)
            # 定义插入图像的矩形区域
            rect = fitz.Rect(0, 0, a4_width_in_pixels, a4_height_in_pixels)
            # 插入图像到PDF页面
            pdf_page.insert_image(rect, filename=temp_img_path)

        # 生成基于时间戳的文件名
        timestamp = int(time.time() * 1000)  # 毫秒时间戳
        timestamp_filename = f"{timestamp}.pdf"
        pdf_file_path = os.path.join(output_dir, timestamp_filename)
        # pdf_file_path = os.path.join(output_dir, timestamp_filename).replace('\\', '/')
        # 保存PDF文档到指定文件
        pdf_document.save(pdf_file_path)
        # 关闭PDF文档
        pdf_document.close()
        print(pdf_file_path)
        return pdf_file_path  # 返回 pdf 路径

    except Exception as e:
        print(f"Error: {e}")
        return None  # 返回 None 表示生成失败
    finally:
        pass

# 示例调用
# images = [Image.open("F:\桌面文件\screenshot.png"), Image.open("F:\桌面文件\wordCard.png")]
# pdf_path = generate_pdf(images)
# print(pdf_path)

# 读取docx文件中的文本内容
def read_docx(file_path):
    document = Document(file_path)
    text = " ".join([paragraph.text for paragraph in document.paragraphs])
    return text


# 读取pdf文件中的文本内容
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            text += page_obj.extract_text()
    return text


# a=read_docx("F:\桌面文件\“泉涌情深：润兵甘泉的故事”.docx")
# print(a)
# 从字体文件获取字体


def get_fonts_list(directory):
    # print(f"Current working directory: {os.getcwd()}")
    font_file_names = [
        f
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.endswith(".ttf")
    ]
    print(font_file_names)
    return font_file_names

import os


def get_fonts_list1(directory = "../public/fonts"):

    ttf_files = glob.glob(os.path.join(directory, '*.ttf'))
    print(ttf_files)
    return ttf_files


# get_fonts_list()
def get_filenames_in_dir(directory):
    """
    获取目录中所有.ttf文件的文件名。
    遍历指定目录中的所有文件，判断它们是否为.ttf文件，
    如果是，则将文件名添加到返回列表中。
    返回:
    list: 包含所有.ttf文件名的列表。
    """
    return [
        f
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.endswith(".ttf")
    ]