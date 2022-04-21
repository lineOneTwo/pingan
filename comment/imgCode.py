# _*_ coding: utf-8 _*_
# 导入页面封装好的操作类
import time
import pytesseract
import cv2
import matplotlib.pyplot as plt
# 导入time   sleep单位为秒  便于设置等待时间
from PIL import Image, ImageEnhance


# 该Login类继承页面类Page_Object
def getCode():
    # 获取截图
    ran = Image.open("F://PT/1.png")
    # 截取二维码
    box = (990, 436, 1115, 460)
    ran.crop(box).save("F://PT/2.png")

    sharp_img = cv2.imread("F://PT/2.png", -1)

    # 放大图像
    fx = 5
    fy = 5
    enlarge = cv2.resize(sharp_img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("F://PT/3.png", enlarge, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    # 图像增强，二值化
    imageCode = Image.open("F://PT/3.png")
    imgry = imageCode.convert('L')
    pixels = imgry.load()
    for x in range(imgry.width):
        for y in range(imgry.height):
            if pixels[x, y] > 150:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    sharp_img = ImageEnhance.Contrast(imgry).enhance(2.0)  # 对比度增强

    # 保存最终图片
    sharp_img.save("F://PT/4.png")
    time.sleep(2)
    # 图片转字符串
    code = pytesseract.image_to_string(Image.open("F://PT/4.png")).strip()
    print(code)
    if code == '':
        print('no code')
    else:
        return code

if __name__ == '__main__':
    getCode()
