from product_page import ProductPage
from leasing_page import LeasingPage
from test_template import TestTemplate
import time

# A test case (scenario)_

# TODO: Add validation step after actions


class TestLeasing(TestTemplate):

    # def test_leasing_category(self):
    #     main_page = ProductPage(self.driver)
    #     assert main_page.check_category_leasing()

    def test_leasing_request(self):
        main_page = ProductPage(self.driver)
        leasing_page = LeasingPage(self.driver)

        main_page.select_leasing()
        leasing_page.set_kaufprice(100)
        leasing_page.set_objekttyp()
        leasing_page.set_unterkategorie()
        leasing_page.check_laufzeit()
        leasing_page.set_laufzeit()
        leasing_page.click_continue()
        leasing_page.input_company_name("FinCompare")
        leasing_page.select_company("FinCompare GmbH")
        # show page before quit()
        time.sleep(10)



