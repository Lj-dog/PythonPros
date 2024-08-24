from PIL import Image, ImageDraw, ImageFont

# 创建一个空白图像
image = Image.new('RGB', (200, 100), color='white')

# 创建一个ImageDraw对象
draw = ImageDraw.Draw(image)

# 选择一个字体和大小
font = ImageFont.truetype('arial.ttf', 15)

# 要绘制的文本
text = "Hello, World!"

# 计算文本的边界框
bbox = draw.textbbox((0, 0), text, font=font)

# 输出边界框坐标
print("Text bounding box:", bbox)
