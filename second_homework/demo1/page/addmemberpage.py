from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from second_homework.demo1.page.dase_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self, name, account, phonenum):
        # name = "aa_0"
        # account = "aa_0_hogwarts"
        # phonenum = "13911111111"
        # 输入用户名
        self.find(By.ID, "username").send_keys(name)
        # 输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入电话号码
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 保存，如果页面相同属性的元素有多个，那么通过 find_element 定位到的元素是第一个
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return True

    def get_member(self, value):
        # wait = WebDriverWait(self.driver,10)
        # 联系人中的复选框元素
        locator = (By.CSS_SELECTOR, ".ww_checkbox")
        # wait.until(ec.element_to_be_clickable(locator))
        # 使用显性等待方式定位复选框
        self.wait_for_click(locator)
        # 定义一个空列表，用来存放获取到的联系人姓名
        titles_totla = []

        while True:
            # 获取到当前页姓名的所有元素
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            # 将当前页姓名元素中的姓名文本提取出来，存放到title的列表中
            titles = [element.get_attribute("title") for element in elements]
            # 如果value(需要查找的姓名）在当前页且已经找到，则返回True
            if value in titles:
                return True
            # 将当前页获取到的姓名列表添加到总的姓名列表中去
            titles_totla.extend(titles)

            # 获取联系人页页码文本信息
            page: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            # 页码格式为当前页/总页码（1/10),需要分割，使用split方法，分割后为一个列表["1","10"]
            num, total = page.split("/", 1)
            # 判断当前页是否等于总页数，如果等于，说明已经是最后一页，还没有找到该姓名，则返回False
            if int(num) == int(total):
                return False
            # 如果当前页不等于总页数，则点击下一页，继续循环
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
