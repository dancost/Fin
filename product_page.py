# Inherits BasePage
# Holds page specific locators and actions

from base_page import BasePage


class ProductPage(BasePage):
    LEASING_AND_MIETKAUF = '//*[@class="funnel__products__title" and text()="Leasing & Mietkauf"]'

    def check_category_leasing(self):
        return self._driver.find_element_by_xpath(ProductPage.LEASING_AND_MIETKAUF).is_displayed()

    def select_leasing(self):
        self._driver.find_element_by_xpath(ProductPage.LEASING_AND_MIETKAUF).click()
