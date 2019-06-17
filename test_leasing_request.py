from product_page import ProductPage
from leasing_page import LeasingPage
from test_template import TestTemplate
import time

class TestLeasing(TestTemplate):

    # def test_leasing_category(self):
    #     main_page = ProductPage(self.driver)
    #     assert main_page.check_category_leasing()

    def test_leasing_request(self):
        main_page = ProductPage(self.driver)
        leasing_page = LeasingPage(self.driver)

        main_page.select_leasing()
        leasing_page.set_kaufprice(100)
        time.sleep(10)
        leasing_page.set_objekttyp('IT & Büro')
