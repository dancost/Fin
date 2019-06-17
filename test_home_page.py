from home_page import HomePage
from test_template import TestTemplate


class TestHomePage(TestTemplate):
    def test_buttons_available(self):
        main_page = HomePage(self.driver)
        assert main_page.check_category_leasing()




        # assert main_page.check_create_account()
        # assert main_page.check_login()
        # assert main_page.check_search()

    def test_buttons_click(self):
        main_page = HomePage(self.driver)
        main_page.select_leasing()
        # main_page.login()
        # main_page.search()
