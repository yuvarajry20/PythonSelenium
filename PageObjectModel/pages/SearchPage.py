from selenium.webdriver.common.by import By
class SearchPage:
    def __init__(self,driver):
        self.driver=driver

    display_status_valid_product_link_text="HP LP3065"

    def display_status_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT,self.display_status_valid_product_link_text).is_displayed()