from second_homework.demo1.page.index_page import IndexPage


class TestContact:

    def setup(self):
        self.index = IndexPage()

    def teardown(self):
        self.index.driver.quit()

    def test_addcontact(self):
        name = "aa_0"
        account = "aa_0_hogwarts"
        phonenum = "13911111111"
        addmenberpage = self.index.click_add_member()
        addmenberpage.add_member(name, account, phonenum)
        result = addmenberpage.get_member(name)
        assert result
