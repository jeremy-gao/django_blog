#encoding:utf-8

from random import randint
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import os 

def Code():
    array_list = [];
    for i in xrange(5):
        if i == randint(1,5):
            array_list.append(str(i));
        else:
            array_list.append(chr(randint(65,90)));
              
    code = ''.join(array_list);
    return code;

# 随机颜色1:
def rndColor():
    return (randint(64, 255), randint(64, 255), randint(64, 255));

# 随机颜色2:
def rndColor2():
    return (randint(32, 127), randint(32, 127), randint(32, 127));


def Img(code,width=100,height=45):
    code=code;
    width = width;
    height = height;
    image = Image.new('RGB', (width, height), (255, 255, 255));
    # 创建Font对象:
    font = ImageFont.truetype('Ubuntu-C.ttf', 30);
    # 创建Draw对象:
    draw = ImageDraw.Draw(image);
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    draw.text((10, 10), code, font=font, fill=rndColor2());
    # 模糊:
    image = image.filter(ImageFilter.SMOOTH_MORE)
    path_dir =os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/images/');
    image.save(path_dir + 'code.png', 'png');   

