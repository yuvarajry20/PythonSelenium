import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
import requests
# driver=webdriver.Firefox()
driver=webdriver.Chrome()
action=ActionChains(driver)
driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# print(driver.title)
# print(len(driver.title))
# str="https://www.flipkart.com/"
# print(driver.current_url)
# if str==driver.current_url:
#     print("verfied")
# else:
#     print("not verfied")
# print(driver.page_source)
# print(len(driver.page_source))
# driver.quit()

# driver.get("https://www.google.com/")
# time.sleep(5)
# driver.get("https://www.flipkart.com/")
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()

# driver.get("https://www.toolsqa.com/selenium-training/")
# registerLink=driver.find_element(By.XPATH, "//a[text()='Go To Registration ']")
# print(registerLink.location)
# print(registerLink.size)
# print(registerLink.tag_name)
# driver.save_screenshot("screenshot.png")
# driver.back()
# driver.forward()
# # driver.To()
# driver.refresh()
# driver.quit()

# driver.get("https://www.google.co.in")
# driver.maximize_window()
# pageTitle=driver.title
# print(pageTitle)
# if pageTitle=="Google":
#     print("Page title is verified")
# else:
#     print("Page title is not verified")
# googleSearchBox=driver.find_element(By.NAME, "q")
# print(googleSearchBox.is_enabled())
# googleSearchBox.send_keys("Selenium")
# driver.implicitly_wait(5)
# googlesearchButton=driver.find_element(By.XPATH, value="//input[@aria-label='Google Search']")
# print(googlesearchButton.is_enabled())
# googlesearchButton.click()


# driver.get("https://selenium08.blogspot.com/2019/07/check-box-and-radio-buttons.html")
# driver.maximize_window()
# driver.implicitly_wait(5)
# RedCheckBox=driver.find_element(By.XPATH, value="//input[@value='red']")
# print(RedCheckBox.is_enabled())
# print(RedCheckBox.is_selected())
# Opera=driver.find_element(By.XPATH, value="//input[@value='Opera']")
# print(Opera.is_selected())


# driver.get("https://www.hyrtutorials.com/p/css-selectors-practice.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
# FirstName=driver.find_element(By.ID,value="firstName")
# FirstName.send_keys("yuvaraj")
# LastName=driver.find_element(locate_with(By.TAG_NAME,"input").below(FirstName))
# LastName.send_keys("Ramesh")
# Gender=driver.find_element(locate_with(By.TAG_NAME,"input").below(LastName))
# Gender.send_keys("Male")
# City=driver.find_element(locate_with(By.TAG_NAME,"input").below(Gender))
# City.send_keys("Salem")
# Country=driver.find_element(locate_with(By.TAG_NAME,"input").below(City))
# Country.send_keys("India")
# Enter_Your_Security_Question=driver.find_element(locate_with(By.TAG_NAME,"input").below(Country))
# Enter_Your_Security_Question.send_keys("What is My Name?")
# Enter_Your_Security_Answer=driver.find_element(locate_with(By.TAG_NAME,"input").below(Enter_Your_Security_Question))
# Enter_Your_Security_Answer.send_keys("Yuvaraj")
# Verfiy_Your_personal_details=driver.find_element(locate_with(By.TAG_NAME,"input").below(Enter_Your_Security_Answer))
# Verfiy_Your_personal_details.send_keys("Correct")
# Button3=driver.find_element(By.ID,value="button3")
# Button3.click()
# # # driver.back()
# # time.sleep(5)
# # Button2=driver.find_element(locate_with(By.TAG_NAME,"input").to_left_of(Button3))
# # Button2.click()
# # # driver.back()
# # time.sleep(5)
# # Button1=driver.find_element(locate_with(By.TAG_NAME,"input").to_left_of(Button2))
# # Button1.click()
# Button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "input")))
# Button2.click()
# Button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "input")))
# Button1.click()

# driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
# driver.maximize_window()
# # driver.implicitly_wait(10)
# btn1=driver.find_element(By.ID,value="btn1")
# btn1.click()
# # txt1=driver.find_element(By.ID,value="txt1")
# # txt1=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"txt1")))
# txt1=WebDriverWait(driver,timeout=30,poll_frequency=5,ignored_exceptions=[NoSuchElementException]).until(EC.presence_of_element_located((By.ID,"txt1")))
# txt1.send_keys("Yuvaraj")
# btn2=driver.find_element(By.ID,value="btn2")
# btn2.click()
# # txt2=driver.find_element(By.ID,value="txt2")
# # txt2=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"txt2")))
# txt2=WebDriverWait(driver,timeout=30,poll_frequency=5,ignored_exceptions=[NoSuchElementException]).until(EC.presence_of_element_located((By.ID,"txt2")))
# txt2.send_keys("Yuvaraj")

# driver.get("https://www.zoho.com/signup.html")
# driver.maximize_window()
# driver.implicitly_wait(10)
# # wait=WebDriverWait(driver,10)
# email=driver.find_element(By.ID,value="email")
# email.send_keys("yuvaraj5504@gmail.com")
# password=driver.find_element(By.ID,value="password")
# password.send_keys("ryuvi20@yuvi")
# number=driver.find_element(By.ID,value="rmobile")
# number.send_keys("9876321654")
# terms=driver.find_element(By.ID,value="signup-termservice")               
# terms.click()
# signup=driver.find_element(By.ID,value="signupbtn")
# signup.click()
# input("Press Enter after solving the CAPTCHA...")
# signup.click()

# driver.get("https://omayo.blogspot.com/")
# Blogs=driver.find_element(By.ID,value="blogsmenu")
# action.move_to_element(Blogs).perform()
# option2=driver.find_element(By.XPATH,value="//span[text()='SeleniumByArun']")
# action.click(option2).perform()

# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# driver.find_element(By.ID,value="input-email").send_keys("aarun.83@gmail.com")
# driver.find_element(By.ID,value="input-password").send_keys("Arun123")
# action.send_keys(Keys.ENTER).perform()

# def verify_url(url):
#     try:
#         response=requests.head(url,timeout=10)
#         # if response.status_code==200:
#         if (response.status_code==301 or response.status_code==302 or response.status_code==503):
#             print(f"{url} - {response.reason}")
#         else:
#             print(f"{url} - {response.reason} is a broken link.")
#     except Exception as e:
#         print(f"{url} - is broken link")

# driver.get("https://omayo.blogspot.com/")
# links=driver.find_elements(By.XPATH,value="//div[@id='LinkList1']//a")
# print(len(links))
# for link in links:
#     # print(link.get_attribute("href"))
#     url=link.get_attribute("href")
#     # url="https://www.google.com/"
#     if url:
#         verify_url(url)

# for link in links:
#     action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
# tabledata=driver.find_elements(By.XPATH,value="//table[@id='table1']//td[3]")
# for table in tabledata:
#     print(table.text)
# rows=driver.find_elements(By.XPATH,value="//table[@id='table1']//tr")
# print(len(rows))
# cols=driver.find_elements(By.XPATH,value="//table[@id='table1']//th")
# print(len(cols))
# for r in range(1,len(rows)+1):
#     for c in range(1,len(cols)+1):
#         if r==1:
#             data=driver.find_element(By.XPATH,value="//table[@id='table1']//tr["+str(r)+"]//th["+str(c)+"]").text
#             print(data,end=" ")
#         else:
#             data=driver.find_element(By.XPATH,value="//table[@id='table1']//tr["+str(r-1)+"]//td["+str(c)+"]").text
#             print(data,end=" ")
#     print()


# driver.get("https://thinking-tester-contact-list.herokuapp.com/")
# driver.find_element(By.ID,value="email").send_keys("aa.83@gmail.com")
# driver.find_element(By.ID,value="password").send_keys("Test143$")
# driver.find_element(By.ID,value="submit").click()
# time.sleep(5)

# excepted="Babu A"
# contact=driver.find_elements(By.XPATH,value="//table[@id='myTable']/tr/td[2]")
# contact_count=len(contact)
# print(contact)
# for name in contact:
#     print(name.text)
# i=1
# for name in contact:
#     if name.text.__eq__(excepted):
#         actual_rowdata=driver.find_elements(By.XPATH,value="//table[@id='myTable']/tr["+str(i)+"]")
#         for actname in actual_rowdata:
#             print(actname.text)
#     i=i+1

# driver.get("https://omayo.blogspot.com/")
# parent_windowID=driver.current_window_handle
# driver.find_element(By.LINK_TEXT,value="Open a popup window").click()
# WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))
# windowsID=driver.window_handles
# for w in windowsID:
#     driver.switch_to.window(w)
#     if driver.title.__eq__("New Window"):
#        window_text=driver.find_element(By.XPATH,value="//div[@class='example']/h3").text
#        print(window_text)
#        driver.close()
#        break
# time.sleep(5)
# driver.switch_to.window(parent_windowID)
# driver.find_element(By.ID,value="ta1").send_keys("hello Welcome")
# time.sleep(5)
# driver.quit()

# driver.get("https://letcode.in/frame")
# driver.switch_to.frame("firstFr")
# driver.find_element(By.NAME,value="fname").send_keys("ArunKumar")
# driver.find_element(By.NAME,value="lname").send_keys("Arumugam")
# time.sleep(5)
# child_frame=driver.find_element(By.XPATH,value="//div[@class='container has-text-centered mb-4 mt-6']//iframe")
# driver.switch_to.frame(1)
# driver.find_element(By.NAME,value="email").send_keys("aarun.83@gmail.com")
# time.sleep(5)
# driver.switch_to.parent_frame()

# driver.get("https://omayo.blogspot.com/")
# time.sleep(5)
# frame=driver.find_element(By.ID,value="navbar-iframe")
# driver.switch_to.frame(frame)
# driver.find_element(By.NAME,value="q").send_keys("Page")
# driver.find_element(By.XPATH,value="//span[@class='m3Blcf opT0zc']").click()
# driver.switch_to.default_content() 
# str=driver.find_element(By.XPATH,value="//div[@class='status-msg-wrap']").text
# print(str)

# driver.get("https://omayo.blogspot.com/")
# select_element = driver.find_element(By.ID,"drop1")
# select = Select(select_element)
# dropdown = select.options
# print(len(dropdown))
# for options in dropdown:
#     print(options.text)
# select.select_by_visible_text("doc 2")
# select.select_by_index(4)
# select.select_by_value("mno")

# time.sleep(3)

# # select_element1=driver.find_element(By.ID,value="multisele")
# select_element.send_keys("doc 1")
# time.sleep(5)
# driver.execute_script("arguments[0].value='ghi';",select_element)
# time.sleep(5)
# opt1=driver.find_element(By.ID,value="ironman4")
# actions=ActionChains(driver)
# # actions.key_down(Keys.CONTROL).click(select_element).perform()
# actions.key_down(Keys.CONTROL).click(select_element).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()
# time.sleep(5)


# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Alert']").click()
# alert=driver.switch_to.alert
# time.sleep(5)
# print(alert.text)
# alert.accept()
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Confirm']").click()
# alert=driver.switch_to.alert
# time.sleep(5)
# print(alert.text)
# alert.accept()
# driver.find_element(By.XPATH,value="//button[text()='Click for JS Prompt']").click()
# alert=driver.switch_to.alert
# print(alert.text)
# alert.send_keys("Hi Yuvaraj")
# alert.accept()
# time.sleep(5)


# def click_element(driver,By,value,timeout=10):
#     try:
#         element=WebDriverWait(driver,timeout).until(EC.element_to_be_clickable((By,value)))
#         driver.execute_script("arguments[0].click();",element)
#     except Exception as e:
#         print(f"Click Failed: {e}")

# driver.get("https://omayo.blogspot.com/")
# click_element(driver,By.ID,"alert1")
# a=driver.switch_to.alert
# time.sleep(5)
# a.accept()
# time.sleep(3)

# def flash_element(element):
#     for i in range(1,30):
#         driver.execute_script("arguments[0].style.background='red';",element)
#         time.sleep(0.2)
#         default_color=element.value_of_css_property("color")
#         driver.execute_script("arguments[0].style.background='"+default_color+"';",element)

# driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
# driver.maximize_window()
# login_button=driver.find_element(By.XPATH,"//input[@type='submit']")
# flash_element(login_button)
# time.sleep(5)
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# driver.execute_script("history.go(0)")
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,500)")
# time.sleep(5)
# driver.execute_script("history.go(0)")
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,-500)")
# time.sleep(5)












