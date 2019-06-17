from base_page import BasePage


class LeasingPage(BasePage):

    KAUFPREIS = '//input[@type="text"]'
    OBJEKTTYP = 'select-assetCategory'
    OBJEKTTYP_CATEGORY = '//li[@data-value=5]'
    UNTERKATEGORIE = '//*[@id="select-assetType"]'
    LAUFZEIT = '//*[@id="select-term"]'



    def check_kaufpreis(self):
        return self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).is_displayed()

    def set_kaufprice(self, ammount):
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).click()
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).send_keys(ammount)

    def check_objekttyp(self):
        return self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).is_displayed()

    def set_objekttyp(self):
        self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).click()
        self._driver.find_element_by_id(LeasingPage.OBJEKTTYP_CATEGORY).click()

    def check_unterkategorie(self):
        pass

    def set_unterkategorie(self, u_category):
        pass

    def check_laufzeit(self):
        pass

    def set_laufzeit(self, running_time):
        pass

