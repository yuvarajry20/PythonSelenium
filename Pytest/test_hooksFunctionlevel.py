import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")

def teardown_function(function):
    driver.quit()

@pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
def test_google_search(search_term):
    driver.find_element(By.NAME,value="q").send_keys(search_term)
    driver.find_element(By.CLASS_NAME,value="gNO89b").click()