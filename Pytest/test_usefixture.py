import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_HP(self):
        driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("HP")
        driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
        exp="Search - HP"
        assert driver.find_element(By.XPATH,value="//div[@class='col-sm-12']//h1").text.__eq__(exp)
    def test_Honda(self):
       driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("Honda")
       driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
       exp="There is no product that matches the search criteria."
       assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)

    def test_empty(self):
       driver.find_element(By.XPATH,value="//input[@class='form-control input-lg']").send_keys("")
       driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']").click()
       exp="There is no product that matches the search criteria."
       assert driver.find_element(By.XPATH,value="//input[@class='btn btn-primary']//following-sibling::p").text.__eq__(exp)