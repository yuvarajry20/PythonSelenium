import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class Testss:
   @pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
   def test_google_search(self,search_term):
      self.driver.find_element(By.NAME,value="q").send_keys(search_term)
      self.driver.find_element(By.CLASS_NAME,value="gNO89b").click()

# @pytest.mark.parametrize('browser',[('chrome'),('firefox')])
# @pytest.mark.parametrize('url',[('https://www.flipkart.com/'),('https://www.amazon.com/')])
# def test_browser(browser,url):
#     if browser=="chrome":
#         driver=webdriver.Chrome()
#     if browser=="firefox":
#         driver=webdriver.Firefox()
#     driver.maximize_window()
#     print(driver.get(url))
