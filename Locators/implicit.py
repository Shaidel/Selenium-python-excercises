# import webdriver  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  

  
# create webdriver object  
driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\geckodriver.exe') 
    
# set implicit wait time 
driver.implicitly_wait(10) # seconds 
  
# get gmail.com
driver.get("https://www.gmail.com")  

# get element after 10 seconds
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("Krzyzanowski")
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys(Keys.ENTER)

# click element 
driver.find_element_by_name("VfPpkd-RLmnJb").click()
    
