# Inherits BasePage
# Holds page specific locators and actions




from base_page import BasePage
import time

# TODO: Replate all time.sleep calls with wait for element visible


class LeasingPage(BasePage):

    KAUFPREIS = '//input[@type="text"]'
    OBJEKTTYP = 'select-assetCategory'
    OBJEKTTYP_CATEGORY = '//li[@data-value=5]'
    UNTERKATEGORIE = 'select-assetType'
    UNCAT_SELECTION = '//li[@data-value=63]'
    LAUFZEIT = 'select-term'
    LAUFZEIT_SELECTION = '//li[@data-value=60]'
    CONTINUE_BUTTON = '//button'
    COMPANY_NAME = 'companyName'
    COMPANY_SEARCH_SUBMIT = '//button'
    SELECT_COMPANY = '//div[@class]/h3[text()="{}"]'


    def check_kaufpreis(self):
        return self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).is_displayed()

    def set_kaufprice(self, ammount):
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).click()
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).send_keys(ammount)

    def check_objekttyp(self):
        return self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).is_displayed()

    def set_objekttyp(self):
        self._driver.find_element_by_id(LeasingPage.OBJEKTTYP).click()
        time.sleep(2)
        self._driver.find_element_by_xpath(LeasingPage.OBJEKTTYP_CATEGORY).click()

    def check_unterkategorie(self):
        return self._driver.find_element_by_id(LeasingPage.UNTERKATEGORIE).is_displayed()

    def set_unterkategorie(self):
        time.sleep(2)
        self._driver.find_element_by_id(LeasingPage.UNTERKATEGORIE).click()
        time.sleep(2)
        self._driver.find_element_by_xpath(LeasingPage.UNCAT_SELECTION).click()

    def check_laufzeit(self):
        return self._driver.find_element_by_id(LeasingPage.LAUFZEIT).is_displayed()

    def set_laufzeit(self):
        time.sleep(2)
        self._driver.find_element_by_id(LeasingPage.LAUFZEIT).click()
        time.sleep(2)
        self._driver.find_element_by_xpath(LeasingPage.LAUFZEIT_SELECTION).click()

    def check_continue(self):
        return self._driver.find_element_by_xpath(LeasingPage.CONTINUE_BUTTON)

    def click_continue(self):
        time.sleep(2)
        self._driver.find_element_by_xpath(LeasingPage.CONTINUE_BUTTON).click()

    def input_company_name(self, company):
        self._driver.find_element_by_id(LeasingPage.COMPANY_NAME).send_keys(company)
        self._driver.find_element_by_xpath(LeasingPage.COMPANY_SEARCH_SUBMIT).click()

    def select_company(self, company_name):
        LeasingPage.SELECT_COMPANY = LeasingPage.SELECT_COMPANY.format(company_name)
        time.sleep(2)
        self._driver.find_element_by_xpath(LeasingPage.SELECT_COMPANY).click()