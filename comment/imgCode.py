# _*_ coding: utf-8 _*_
# 导入页面封装好的操作类
import time
import pytesseract
import cv2
# 导入time   sleep单位为秒  便于设置等待时间
from PIL import Image, ImageEnhance


# 该Login类继承页面类Page_Object
def getCode():
    # 获取截图
    ran = Image.open("F://PT/1.png")
    # 截取二维码
    box = (990, 436, 1115, 460)
    ran.crop(box).save("F://PT/2.png")

    img = cv2.imread("F://PT/2.png", -1)
    # 放大图像
    fx = 10
    fy = 10
    enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    # 保存
    cv2.imwrite("F://PT/2.png", enlarge, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    imageCode = Image.open("F://PT/2.png")
    imgry = imageCode.convert('L')  # 图像增强，二值化
    pixels = imgry.load()
    for x in range(imgry.width):
        for y in range(imgry.height):
            if pixels[x, y] > 150:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0

    sharp_img = ImageEnhance.Contrast(imgry).enhance(2.0)  # 对比度增强

    #  删除一些扰乱识别的像素点
    data = sharp_img.getdata()
    w, h = sharp_img.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    sharp_img.putpixel((x, y), 255)
                black_point = 0

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
