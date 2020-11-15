import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Cookies_Login:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 验证被保存cook文件的可用性
    def test_use_cookies(self):
        # 打开企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        db = shelve.open("cookies")  # 打开cook文件
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)  # 添加cook信息
        self.driver.refresh()  # 刷新
        # 获取退出按钮的元素列表
        ele_list = self.driver.find_elements(By.ID, "logout")
        # 当获取到的元素信息不等于0时，说明登录成功
        assert len(ele_list) != 0

    def test_add_contacts(self):
        # 打开企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        db = shelve.open("cookies")  # 打开cook文件
        cookies = db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)  # 添加cook信息
        self.driver.refresh()  # 刷新
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()  #点击添加成员
        self.driver.find_element(By.ID,"username").send_keys("zhangsan11")   #输入姓名“zhangsan”
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("admin11")  #输入账号：admin
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13245678910") #输入电话
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()  #点击保存
        ele_text = self.driver.find_element(By.ID,"js_tips").text
        assert "保存成功" == ele_text