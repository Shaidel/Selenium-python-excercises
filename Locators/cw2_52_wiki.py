import selenium
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
  
print("sample test case started")  

#driver = webdriver.Chrome(executable_path=r'C:\AT_WiN\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\AT_WiN\geckodriver.exe')
#driver = webdriver.Opera(executable_path=r'C:\AT_WiN\operadriver.exe')
  
#maximize the window size  
driver.maximize_window()
  
#navigate to the url  
driver.get("https://pl.wikipedia.org")  

time.sleep(3)  
 
#1
driver.find_element_by_id("searchInput").send_keys(Keys.ENTER)  
time.sleep(3)  
#2
driver.find_element_by_name("search").send_keys(Keys.ENTER) 
time.sleep(3)  
#3
driver.find_element_by_class_name("searchButton").send_keys(Keys.ENTER) 
time.sleep(3)  
#4
driver.find_element_by_xpath("//input[@id='searchInput']").send_keys(Keys.ENTER) 
time.sleep(3) 
#5
driver.find_element_by_css_selector("#searchInput").send_keys(Keys.ENTER) 
time.sleep(3) 
#6
driver.find_element_by_link_text('O Wikipedii').send_keys(Keys.ENTER) 
time.sleep(3) 
#7
driver.find_element_by_partial_link_text('Konta').send_keys(Keys.ENTER) 
#time.sleep(3) 
#8
driver.find_element_by_tag_name("input").send_keys(Keys.ENTER) 
time.sleep(3) 

#close the browser  
driver.close()  
print("sample test case successfully completed")  