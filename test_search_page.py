from home_page import HomePage
from search_page import SearchPage
from test_template import TestTemplate


class TestSearchPage(TestTemplate):
    def test_result_found(self):
        home_page = HomePage(self.driver)
        home_page.set_search_query("Design patterns")
        home_page.search()
        result = SearchPage(self.driver)
        assert result.heading_text() == "Design pattern"