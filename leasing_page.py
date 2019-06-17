from base_page import BasePage


class LeasingPage(BasePage):

    KAUFPREIS = '//input[@type="text"]'
    OBJEKTTYP = '//*[@id="select-assetCategory"]'
    OBJEKTTYP_CATEGORY = '//li[text()="IT & Büro"]'
    UNTERKATEGORIE = '//*[@id="select-assetType"]'
    LAUFZEIT = '//*[@id="select-term"]'

    def check_kaufpreis(self):
        return self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).is_displayed()

    def set_kaufprice(self, ammount):
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).click()
        self._driver.find_element_by_xpath(LeasingPage.KAUFPREIS).send_keys(ammount)

    def check_objekttyp(self):
        return self._driver.find_element_by_xpath(LeasingPage.OBJEKTTYP).is_displayed()

    def set_objekttyp(self):
        self._driver.find_element_by_xpath(LeasingPage.OBJEKTTYP).click()
        self._driver.find_element_by_xpath(LeasingPage.OBJEKTTYP_CATEGORY).click()

    def check_unterkategorie(self):
        pass

    def set_unterkategorie(self, u_category):
        pass

    def check_laufzeit(self):
        pass

    def set_laufzeit(self, running_time):
        pass


    # HEADING = "firstHeading"
    # SEE_ALSO = "See_also"
    # DOMAIN_ARTICLES = "Domain-specific_articles"
    # READING = "Further_reading"
    # REF = "References"
    # EXTERNAL_LINKS = "External_links"
    #
    # def heading_text(self):
    #     return self._driver.find_element_by_id(SearchPage.HEADING).text
    #
    # def see_also_text(self):
    #     return self._driver.find_element_by_xpath(SearchPage.SEE_ALSO).text
    #
    # def domain_articles_text(self):
    #     return self._driver.find_element_by_xpath(SearchPage.DOMAIN_ARTICLES).text
    #
    # def reading_text(self):
    #     return self._driver.find_element_by_xpath(SearchPage.READING).text
    #
    # def ref_text(self):
    #     return self._driver.find_element_by_xpath(SearchPage.REF).text
    #
    # def external_links_text(self):
    #     return self._driver.find_element_by_xpath(SearchPage.EXTERNAL_LINKS).text
