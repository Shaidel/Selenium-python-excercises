import selenium
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  

print("sample test case started")  

driver = webdriver.Chrome(executable_path=r'C:\AT_WiN\chromedriver.exe')
#driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\geckodriver.exe')
#driver = webdriver.Opera(executable_path=r'C:\AT_WiN\operadriver.exe')
  
#maximize the window size  
driver.maximize_window()  

#navigate to the url  
driver.get("https://www.google.com/")  

#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("Hello webdriver |!|")  
time.sleep(3)  

#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  

#close the browser  
driver.close()  

print("sample test case successfully completed")  