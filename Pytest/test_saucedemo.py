import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from Utility import excelReader

@pytest.mark.parametrize("username,password", excelReader.get_data("C:\\Users\\yuvar\\PythonSelenium\\Pytest\\ExcelFiles\\loginData.xlsx", "Sheet2"))
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin2:
    def test_validation1(self,username,password):
        self.driver.find_element(By.ID,value="user-name").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,value="password").send_keys(password)
        self.driver.find_element(By.ID,value="login-button").click()
        time.sleep(5)
        if(username=="standard_user" or username=="problem_user" or username=="performance_glitch_user"):
          expec="Products"
          assert self.driver.find_element(By.XPATH,value="//div[@class='product_label']").text.__eq__(expec)
        else:
           expec="Sorry, this user has been locked out."
           assert expec in self.driver.find_element(By.XPATH,value="//h3[@data-test='error']").text
        self.driver.quit()
