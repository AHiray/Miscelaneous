import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 


browser = webdriver.Chrome('/Users/arnavhiray/Selenium/chromedriver')  # Optional argument, if not specified will search path.



browser.get("https://www.tradingview.com/#signin")
browser.maximize_window()
browser.find_element_by_name("username").send_keys("*********")
browser.find_element_by_name("password").send_keys("*********")
browser.find_element_by_xpath("//button[@type='submit']").click()

browser.find_element_by_name('query').send_keys('AAPL')
browser.find_element_by_name("query").send_keys(Keys.ENTER)

browser.find_element_by_class_name('tv-goto-chart-button').click()
time.sleep(7)
action = ActionChains(browser) 
  
# move the cursor 
action.move_by_offset(200, 200) 
  
# perform the operation 
action.perform() 


