# import webdriver  
from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys  

  
# create webdriver object  
driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\geckodriver.exe')
    
# get geeksforgeeks.org  
driver.get("https://www.gmail.com")  
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("Krzyzanowski")
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys(Keys.ENTER)

    
# get element  after explicitly waiting for 10 seconds 
element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.xpath, "//input[@id='identifierId']")) 
    ) 
# click the element  
element.click()  