# _*_ coding: utf-8 _*_
from selenium import webdriver  # 导入需要的selenium
from os import path  # 导入文件处理的包
from selenium.webdriver.common.keys import Keys  # 导入键盘操作的包
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标操作的包


# 创建界面元素操作公共类
class Page_Object:
    # 写一个构造函数，有一个参数driver   初始化webdirver驱动
    def __init__(self, driver):
        self.driver = driver
        # 编写元素定位方法，多种元素定位进行统一处理

    def find_element(self, key, value):
        if key == 'id':
            return self.driver.find_element_by_id(value)
        elif key == 'class':
            return self.driver.find_element_by_class_name(value)
        elif key == 'name':
            return self.driver.find_element_by_name(value)
        elif key == 'tag':
            return self.driver.find_element_by_tag_name(value)
        elif key == 'linkText':
            return self.driver.find_element_by_link_text(value)
        elif key == 'cssSelector':
            return self.driver.find_element_by_css_selector(value)
        elif key == 'xpath':
            return self.driver.find_element_by_xpath(value)
        else:
            print('未找到需要定位的页面元素')

    # 打开需要进行测试的url地址
    def open_url(self, url):
        self.driver.get(url)
        print(url)

    # 控制浏览器页面最大化
    def max_window_page(self):
        self.driver.maximize_window()

    # 关闭浏览器页面
    def exit_page(self):
        self.driver.quit()

    # 控制浏览器前进
    def forward_page(self):
        self.driver.forward()

    # 控制浏览器后退
    def back_page(self):
        self.driver.back()

    # 清除定位的文本框内容
    def clear_textbox(self, key, value):
        self.find_element(key, value).clear()

    # 向定位到的文本框输入内容
    def write_textbox(self, key, value, keys):
        self.find_element(key, value).send_keys(keys)

    # 进行键盘回车操作
    def enter(self, key, value):
        self.find_element(key, value).send_keys(Keys.ENTER)

    # 进行键盘复制操作
    def enter_control_c(self, key, value):
        self.find_element(key, value).send_keys(Keys.CONTROL, 'c')

    # 进行键盘粘贴操作
    def enter_control_v(self, key, value):
        self.find_element(key, value).send_keys(Keys.CONTROL, 'v')

    # 进行键盘添加空格操作
    def enter_space(self, key, value):
        self.find_element(key, value).send_keys(Keys.SPACE)

    # 进行键盘删除字符操作
    def enter_back_space_textbox(self, key, value):
        self.find_element(key, value).send_keys(Keys.BACK_SPACE)

    # 进行鼠标点击操作
    def click(self, key, value):
        self.find_element(key, value).click()

    # 通过js代码设置滚动条
    def gundongtiao(self):
        self.driver.execute_script("window.scrollTo(400,800)")

    # 页面截图
    def get_image(self, ImagePath):
        self.driver.get_screenshot_as_file(ImagePath)

    # 获取元素标题
    def get_title(self):
        title = self.driver.title
        return title

    # 获取url地址
    def get_url(self):
        url = self.driver.current_url
        return url

    # 获取输入文本框大小
    def get_size(self):
        size = self.driver.size
        return size

    # 判断元素是否存在
    def get_dispaay(self, key, value):
        self.find_element(key, value).is_displayed()
