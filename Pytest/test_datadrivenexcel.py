import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from Utility import excelReader

@pytest.mark.parametrize("username,password", excelReader.get_data("ExcelFiles/logindata.xlsx", "Sheet1"))
class TestLogin1:
    def test_validation1(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID,value="login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID,value="loginusername").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,value="loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        time.sleep(5)
        # assert self.driver.find_element(By.ID,"logout2").is_displayed()
        if(username=="admin"):
          expec="Welcome admin"
          assert self.driver.find_element(By.ID,value="nameofuser").text.__eq__(expec)
        else:
           expec="Wrong password."
           assert self.driver.switch_to.alert.text.__eq__(expec)
        self.driver.quit()
