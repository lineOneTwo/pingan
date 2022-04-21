import cv2 as cv
import pytesseract
from PIL import Image


def recognize_text(image):
    # 边缘保留滤波  去噪
    blur =cv.pyrMeanShiftFiltering(image, sp=8, sr=70)

    blur = cv.pyrMeanShiftFiltering(blur, sp=100, sr=70)

    blur = cv.pyrMeanShiftFiltering(blur, sp=100, sr=70)
    cv.imshow('dst', blur)


    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(f'二值化自适应阈值：{ret}')
    cv.imshow('binary', binary)


    # 形态学操作  获取结构元素  开操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 3))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow('bin1', bin1)



    kernel = cv.getStructuringElement(cv.MORPH_OPEN, (5, 3)) # 不能动
    bin2 = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow('bin2', bin2)




    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(bin2, bin2)
    cv.imshow('binary-image', bin2)
    # 识别
    test_message = Image.fromarray(bin2)
    text = pytesseract.image_to_string(test_message)
    print(f'识别结果：{text}')



# ran = Image.open("F://PT/1.png")
# box = (990, 436, 1115, 470)  # 截取二维码
# ran.crop(box).save("F://PT/2.png")  # 保存截图
src = cv.imread("F://PT/2.png")
cv.imshow('input image', src)


# 放大图像
fx = 4
fy = 3
enlarge = cv.resize(src, (0, 0), fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)
cv.imwrite("F://PT/3.png", enlarge, [cv.IMWRITE_PNG_COMPRESSION, 0])
src = cv.imread("F://PT/3.png")

recognize_text(src)
cv.waitKey(0)
cv.destroyAllWindows()

