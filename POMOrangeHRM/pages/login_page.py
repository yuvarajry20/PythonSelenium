from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.send_keys(self.username_input, username)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
