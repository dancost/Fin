import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def tearDown(self):
        self.driver.quit()
