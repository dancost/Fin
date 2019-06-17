from product_page import ProductPage
from test_template import TestTemplate


class TestHomePage(TestTemplate):
    def test_leasing_available(self):
        main_page = ProductPage(self.driver)
        assert main_page.check_category_leasing()