import selenium
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.select import Select
print("sample test case started") 
print(" ") 
#driver = webdriver.Chrome(executable_path=r'C:\AT_WiN\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\geckodriver.exe')
#driver = webdriver.Opera(executable_path=r'C:\AT_WiN\operadriver.exe')
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  

#navigate to the url  
driver.get("https://demoqa.com") 

#click 
driver.find_element_by_xpath("//h5[contains(text(),'Forms')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Practice Form')]").click()

driver.find_element_by_xpath("//input[@id='firstName']").send_keys("Andrzej")
driver.find_element_by_xpath("//input[@id='firstName']")

driver.find_element_by_xpath("//input[@id='lastName']").send_keys("Krzyzanowski")
driver.find_element_by_xpath("//input[@id='lastName']")

driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("shaidel@wp.pl")
driver.find_element_by_xpath("//input[@id='userEmail']")

driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()

driver.find_element_by_xpath("//input[@id='userNumber']").send_keys("1234567890")
driver.find_element_by_xpath("//input[@id='userNumber']")

driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").click()
driver.find_element_by_xpath("//div[contains(text(),'30')]").click()

driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys(Keys.BACKSPACE)

driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").send_keys("1977")

#driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]").click()
#driver.find_element_by_class_name("subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3").send_keys("m")
#time.sleep(3)
#driver.find_element_by_xpath("//*[@id="subjectsContainer"]/div/div[1]/div[2]").send_keys("Maths") 

#time.sleep(3)
#driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]").send_keys("Computer Science")
#driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]").send_keys("Econimics")

driver.find_element_by_xpath("//label[contains(text(),'Reading')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Music')]").click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#driver.find_element_by_xpath("//div[contains(text(),'Select State')]").click()
#driver.find_element_by_xpath("//div[contains(text(),'Select State')]").select_by_visible_text("NCR")

#sel = Select(driver.find_element_by_xpath("//div[contains(text(),'Select State')]"))
#select by select_by_visible_text() method
#sel.select_by_visible_text("NCR")
#time.sleep(0.8)
#select by select_by_index() method
#sel.select_by_index(0)
#driver.close()

driver.find_element_by_xpath("//button[@id='submit']").click()



LabelStudentName = driver.find_element_by_xpath("//td[contains(text(),'Student Name')]")
ValuesStudentName = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]")
print(LabelStudentName.text + " " + ValuesStudentName.text)

LabelStudentEmail= driver.find_element_by_xpath("//td[contains(text(),'Student Email')]")
ValuesStudentEmail = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]")
print(LabelStudentEmail.text + " " + ValuesStudentEmail.text)

LabelStudentGender= driver.find_element_by_xpath("//td[contains(text(),'Gender')]")
ValuesStudentGender = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[2]")
print(LabelStudentGender.text + " " + ValuesStudentGender.text)

LabelStudentMobile= driver.find_element_by_xpath("//td[contains(text(),'Mobile')]")
ValuesStudentMobile = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[2]")
print(LabelStudentMobile.text + " " + ValuesStudentMobile.text)

LabelStudentDateofBirth= driver.find_element_by_xpath("//td[contains(text(),'Date of Birth')]")
ValuesStudentDateofBirth = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[2]")
print(LabelStudentDateofBirth.text + " " + ValuesStudentDateofBirth.text)



time.sleep(3)  

#close the browser  
#driver.close()  
print(" ") 
print("sample test case successfully completed")  