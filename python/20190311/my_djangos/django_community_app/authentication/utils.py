#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create_lines(draw, lines=4):
    """绘制干扰线"""
    for i in range(lines):
        begin = (random.randint(0, 320), random.randint(0, 30))
        end = (random.randint(0, 320), random.randint(0, 30))
        draw.line([begin, end], fill=(0, 0, 0))


def create_verify_code():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('seguiemj.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    create_lines(draw)
    # 输出文字:
    codes = ''
    for t in range(4):
        random_char = rndChar()
        draw.text((60 * t + 10, 10), random_char, font=font, fill=rndColor2())
        codes += random_char
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    # image.save('code.jpg', 'jpeg')
    return image, codes