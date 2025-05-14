import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from Utility import consolelogger


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        logger = consolelogger.get_logger()
        home_page=HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        logger.info("Entering product into search box")
        home_page.click_search_button()
        logger.info("Clicking search button")
        search_page=SearchPage(self.driver)
        search_page.display_status_valid_product()
        logger.info("Displaying status of valid product")