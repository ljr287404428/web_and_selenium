import os
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class Test_WX:

    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    #验证使用复用已有的浏览器登录成功
    def test_login(self):
        #打开企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #获取退出按钮的元素列表
        ele_list = self.driver.find_elements(By.ID,"logout")
        #当获取到的元素信息不等于0时，说明登录成功
        assert len(ele_list) != 0

    #获取登录之后页面的cook信息，并且保存
    def test_cookie(self):
        cookies = self.driver.get_cookies()   #获取cook信息
        db =shelve.open("cookies")     #打开python知道的数据库shelve，文件名为cookies
        db['cookie'] = cookies         #将获取到的cookies数据存入到数据库中
        db.close()                     #关闭文件
        assert "cookies.bak" in (os.listdir('./'))   #判定当前目录是否存在被保存的cook文件




