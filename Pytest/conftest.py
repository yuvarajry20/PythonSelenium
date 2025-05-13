import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class",params=["chrome","firefox","edge"])
def setup_and_teardown(request):
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if request.param=="chrome":
      driver=webdriver.Chrome(options=options)
    elif request.param=="firefox":
      driver=webdriver.Firefox()
    elif request.param=="edge":
       driver=webdriver.Edge()
    driver.get("https://www.google.com/")
    request.cls.driver=driver
    # yield driver
    # driver.quit()
    # Teardown explicitly registered
    def quit_driver():
        try:
            driver.quit()
        except Exception as e:
            print(f"Error while quitting driver: {e}")

    request.addfinalizer(quit_driver)