from selenium import webdriver
from comment.imgCode import getCode
from comment.PageObject import Page_Object
import time

class pages:
    driver = webdriver.Chrome()
    def login(self,username, password ):

        # 跳转到登录页面
        self.driver.get('https://www.pingan.gov.cn:9260/system/login')
        # driver.find_element_by_css_selector('.login_btn').click()

        # 获取登录页截图
        PO = Page_Object(self.driver)
        PO.max_window_page()
        self.driver.save_screenshot("F://PT/1.png")

        # 输入账号密码验证码登录
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('createValidCodeImg').send_keys(getCode())
        self.driver.find_element_by_class_name('btn btn-lg btn-login btn-block').click()
        print(time.ctime())
        # driver.quit()

    # 进入事件处置模块
    def events(self):
        self.driver.find_element_by_id('treeDemo_88_span').click()
        self.driver.find_element_by_id('treeDemo_90_span').click()

        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/table/tbody/tr[1]/td[2]/button').click()
