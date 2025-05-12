import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_HP(test_setup_and_teardown):
    driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("HP")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    exp="Search - HP"
    assert driver.find_element(By.XPATH,value="//div[@class='col-sm-12']//h1").text.__eq__(exp)

def test_Honda(test_setup_and_teardown):
    driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("Honda")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    exp="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)

def test_empty(test_setup_and_teardown):
    driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("")
    driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
    exp="There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)