import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
# def test_google_search(search_term):
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.com/")
#     driver.find_element(By.NAME,value="q").send_keys(search_term)
#     time.sleep(5)
#     driver.find_element(By.CLASS_NAME,value="gNO89b").click()
#     time.sleep(5)
#     driver.quit()

@pytest.mark.parametrize('browser',[('chrome'),('firefox')])
@pytest.mark.parametrize('url',[('https://www.flipkart.com/'),('https://www.amazon.com/')])
def test_browser(browser,url):
    if browser=="chrome":
        driver=webdriver.Chrome()
    if browser=="firefox":
        driver=webdriver.Firefox()
    driver.maximize_window()
    print(driver.get(url))
