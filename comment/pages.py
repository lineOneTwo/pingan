from selenium import webdriver
from comment.code1 import recognize_text
from comment.PageObject import Page_Object
import time
from comment.logger import Logger

log = Logger()

class pages:
    driver = webdriver.Chrome()
    driver.get('https://www.pingan.gov.cn:9260/system/login')

    def login(self,username, password ):

        # 获取登录页截图
        PO = Page_Object(self.driver)
        PO.max_window_page()

        # 登录失败则循环登录
        # for i in range(2):
        #     # 输入账号密码验证码登录
        #     self.driver.save_screenshot("F://PT/1.png")
        #     self.driver.find_element_by_name('username').send_keys(username)
        #     log.write('登录账号是{}'.format(username))
        #     self.driver.find_element_by_name('password').send_keys(password)
        #     self.driver.find_element_by_name('validCode').send_keys(recognize_text())
        #     self.driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
        #     if self.driver.current_url == 'https://www.pingan.gov.cn:9260/system/login?error=1003':
        #         time.sleep(1)
        #         self.driver.find_element_by_class_name('noty_close_button').click() # 关闭弹窗提示
        #         time.sleep(1)
        #         continue
        #     else:
        #         break

        # 输入账号密码验证码登录
        self.driver.save_screenshot("F://PT/1.png") # 屏幕截屏
        self.driver.find_element_by_name('username').send_keys(username)
        log.write('登录账号是{}'.format(username))
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('validCode').send_keys(recognize_text())
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
        if self.driver.current_url == 'https://www.pingan.gov.cn:9260/system/login?error=1003':
            time.sleep(1)
            self.driver.find_element_by_class_name('noty_close_button').click()  # 关闭弹窗提示
            time.sleep(1)


        log.write(time.strftime("%Y-%m-%d %X", time.localtime())) # 输出当前时间
        log.write('当前浏览器地址是{}'.format(self.driver.current_url)) # 输出浏览器地址
        return  self.driver.current_url


    # 进入事件处置模块
    def events(self):
        pageNum = self.driver.find_element_by_id('btnJump').text # 总条数
        count = int(''.join(filter(str.isdigit,pageNum))) # 获取条数

        if count > 0 :  # 判断待办事件条数
            for i in range(1, count):  # 循环执行次数为总条数
                self.driver.find_element_by_id('txtToPager').click()  # 点击设置页码输入流
                self.driver.find_element_by_id('txtToPager').send_keys(i)  # 设置页码
                self.driver.find_element_by_class_name('glyphicon glyphicon-share-alt').click()  # 点击跳转页面按钮

                self.driver.find_element_by_id('treeDemo_88_span').click()  # 事件处置
                self.driver.find_element_by_id('treeDemo_90_span').click()  # 待办事件

                self.driver.find_element_by_class_name('btn btn-info btn-xs').click()  # 详情信息按钮
                self.driver.find_element_by_class_name('btn btn-outline btn-default btnCaoZ btnbanj').click()  # 办结按钮

                self.driver.find_element_by_name('yiJ').click()  # 点击输入框
                self.driver.find_element_by_name('yiJ').send_keys('请继续发挥网格张职责，及时上报有效信息，切实做好疫情防控，确保一方平安。')  # 输入办结信息

                self.driver.find_element_by_class_name('ui-dialog-autofocus')  # 保存按钮
                time.sleep(1)  # 等待跳转回列表
        else:
            log.write("当前账号无待办事件")



    # 退出登录
    def loginout(self):
        self.driver.find_element_by_css_selector('.fa-sign-out').click() # 退出按钮


    def quit(self):
        self.driver.quit()
