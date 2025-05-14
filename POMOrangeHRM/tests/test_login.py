import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from Utility import excelReader
from selenium.webdriver.common.by import By

test_data = excelReader.get_data("C:\\Users\\yuvar\\PythonSelenium\\POMOrangeHRM\\ExcelFiles\\loginData.xlsx", "Sheet2")

@pytest.mark.usefixtures("setup_and_teardown")
class TestOrangeHRMLogin:
    @pytest.mark.parametrize("username, password", [test_data[0]])
    def test_valid_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.get_dashboard_heading() == "Dashboard"
    @pytest.mark.parametrize("username, password", [test_data[1]])
    def test_invalid_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        error_msg = self.driver.find_element(By.XPATH, "//p[contains(@class,'oxd-alert')]").text
        assert "Invalid credentials" in error_msg