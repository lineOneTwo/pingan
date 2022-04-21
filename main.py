from comment.pages import pages
from comment.data import data
from comment.logger import Logger
log = Logger()

if __name__ == '__main__':
    login = pages()
    person = data()
    personlist = person.read_data()
    for i in range(len(personlist)):
        result = login.login(personlist[i],'bgfg1000lbfwlXP#')  # 获取社区账号并登录
        # result = login.login('13734206025','bgfg1000lbfwlXP#')  # 登录
        if result == 'https://www.pingan.gov.cn:9260/system':  # 判断是否登录成功
            log.write("登录成功")
            login.events()  # 执行办结
            login.loginout()  # 退出账号
        else:
            log.write("登录失败")

    login.quit()  # 关闭浏览器