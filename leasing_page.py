from base_page import BasePage


class LeasingPage(BasePage):

    KAUFPREIS = '//input[@type="text"]'
    OBJEKTTYP = 'select-assetCategory'
    OBJEKTTYP_CATEGORY = '//li[@data-value=5]'
    UNTERKATEGORIE = 'assetType'
    UNCAT_SELECTION = '//li[@data-value=63]'
    LAUFZEIT = 'select-term'
    LAUFZEIT_SELECTION = '//li[@data-value=60]'
    CONTINUE_BUTTON = '//button'

    def check_kaufpreis(self):
        return self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).is_displayed()

    def set_kaufprice(self, ammount):
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).click()
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).send_keys(ammount)

    def check_objekttyp(self):
        return self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).is_displayed()

    def set_objekttyp(self):
        self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).click()
        self._driver.find_element_by_xpath(LeasingPage.OBJEKTTYP_CATEGORY).click()

    def check_unterkategorie(self):
        return self._driver.find_element_by_id(LeasingPage.UNTERKATEGORIE).is_displayed()

    def set_unterkategorie(self):
        self._driver.find_element_by_id(LeasingPage.UNTERKATEGORIE).click()
        self._driver.find_element_by_xpath(LeasingPage.UNCAT_SELECTION).click()

    def check_laufzeit(self):
        return self._driver.find_element_by_id(LeasingPage.LAUFZEIT).is_displayed()

    def set_laufzeit(self):
        self._driver.find_element_by_id(LeasingPage.LAUFZEIT).click()
        self._driver.find_element_by_xpath(LeasingPage.LAUFZEIT_SELECTION).click()

    def check_continue(self):
        return self._driver.find_element_by_xpath(LeasingPage.CONTINUE_BUTTON)

    def click_continue(self):
        self._driver.find_element_by_xpath(LeasingPage.CONTINUE_BUTTON).click()

