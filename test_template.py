# BaseClass for all test cases
# HOlds common code for all test cases - e.g. Setup and Teardown

import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://app.fincompare.de/wizard/products")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
