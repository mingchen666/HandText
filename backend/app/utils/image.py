# 图片相关功能函数
# 创建一个新的白色图片，并添加间隔的线条作为背景
from PIL import Image, ImageDraw


def create_notebook_image(
        width,
        height,
        line_spacing,
        top_margin,
        bottom_margin,
        left_margin,
        right_margin,
        font_size,
        isUnderlined,
):
    """
    创建一个模拟笔记本纸张的图像。

    参数:
    - width: 图像的宽度。
    - height: 图像的高度。
    - line_spacing: 行间距。
    - top_margin: 顶部边距。
    - bottom_margin: 底部边距。
    - left_margin: 左侧边距。
    - right_margin: 右侧边距。
    - font_size: 字体大小。
    - isUnderlined: 是否有下划线。

    返回值:
    - Image对象，表示创建的图像。
    """
    image = Image.new("RGB", (width, height), "white")

    if isUnderlined == "true":
        draw = ImageDraw.Draw(image)
        # todo  这个距离的原理不清楚7.15
        y = top_margin + line_spacing  # 开始的y坐标设为顶部边距加字体大小
        # bottom_margin -= line_spacing
        while y < height - bottom_margin:  # 当y坐标小于（图片高度-底部边距）时，继续画线
            draw.line((left_margin, y, width - right_margin, y), fill="black")
            y += line_spacing  # 每次循环，y坐标增加行间距
        # draw.line((left_margin, y, width - right_margin, y), fill="black")
    return image


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # 创建图像
    image = create_notebook_image(800, 600, 30, 50, 50, 50, 50, 20, "true")

    # 使用 matplotlib 显示图像
    plt.imshow(image)
    plt.axis('off')  # 关闭坐标轴
    plt.show()