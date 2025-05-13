from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_bank():
 driver=webdriver.Chrome()
 wait=WebDriverWait(driver,10)
 driver.get("https://parabank.parasoft.com/parabank/index.htm")
 register=driver.find_element(By.XPATH,value="//a[text()='Register']")
 register.click()
 Firstname=driver.find_element(By.ID,value="customer.firstName")
 Firstname.send_keys("yuvaraj")
 Lastname=driver.find_element(locate_with(By.TAG_NAME,"input").below(Firstname))
 Lastname.send_keys("ramesh")
 Address=driver.find_element(locate_with(By.TAG_NAME,"input").below(Lastname))
 Address.send_keys("Salem")
 City=driver.find_element(locate_with(By.TAG_NAME,"input").below(Address))
 City.send_keys("Salem")
 State=driver.find_element(locate_with(By.TAG_NAME,"input").below(City))
 State.send_keys("tamilnadu")
 ZipCode=driver.find_element(locate_with(By.TAG_NAME,"input").below(State))
 ZipCode.send_keys("636305")
 Phone=driver.find_element(locate_with(By.TAG_NAME,"input").below(ZipCode))
 Phone.send_keys("6385761600")
 ssn=driver.find_element(locate_with(By.TAG_NAME,"input").below(Phone))
 ssn.send_keys("789456")
 Username=driver.find_element(By.ID,value="customer.username")
 Username.send_keys("yjrajj2220")
 Password=driver.find_element(locate_with(By.TAG_NAME,"input").below(Username))
 Password.send_keys("123456")
 Confirm=driver.find_element(locate_with(By.TAG_NAME,"input").below(Password))
 Confirm.send_keys("123456")
 register=driver.find_element(locate_with(By.TAG_NAME,"input").below(Confirm))
 register.click()
 verifyregister=driver.find_element(By.XPATH,value="//h1[@class='title']/following-sibling::p")
 print(verifyregister.text)
 expected="Your account was created successfully. You are now logged in."
 assert verifyregister.text.__eq__(expected)

 logout=driver.find_element(By.XPATH,value="//a[text()='Log Out']")
 logout.click()

 driver.implicitly_wait(10)
 # wait.until(EC.presence_of_element_located((By.XPATH,"(//p/following-sibling::div)[1]")))
 login=driver.find_element(By.XPATH,value="(//p/following-sibling::div/input)[1]")
 login.send_keys("yuvarajry200420")
 password1=driver.find_element(locate_with(By.TAG_NAME,"input").below(login))
 password1.send_keys("123456")
 loginbtn=driver.find_element(locate_with(By.TAG_NAME,"input").below(password1))
 loginbtn.click()
 verifylogin=driver.find_element(By.XPATH,value="//p[@class='smallText']/child::b")
 expected1=verifylogin.text
 actual="Welco"
 assert actual==expected1
 print(verifylogin.text)