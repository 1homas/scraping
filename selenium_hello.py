#!/usr/bin/env python3

import random
from selenium import webdriver

urls = [
  'https://nytimes.com',
  'https://latimes.com',
  'https://cisco.com',
]
# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get(random.choice(urls))
driver.implicitly_wait(10) # applies to every element call for the entire session

# wait = WebDriverWait(driver, timeout=2) 
# wait.until(lambda d : revealed.is_displayed()) # poll for a specific condition to be true 

driver.quit()
