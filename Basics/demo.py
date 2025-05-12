import time
from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
url="https://www.speedtest.net/"
# driver.get("https://www.google.co.in")
driver.get(url)
# time.sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()