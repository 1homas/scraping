#!/usr/bin/env python3
"""
Tests Selenium web scraper using Firefox on DuckDuckGo.com
"""
__author__ = "Thomas Howard"
__email__ = "t@thomas-howard.com"
__license__ = "MIT - https://mit-license.org/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://duckduckgo.com"
query = "python web scraping"

driver = webdriver.Firefox()
driver.set_window_size(1920, 1080)
driver.get(url)
assert "DuckDuckGo" in driver.title

elem = driver.find_element(By.ID, "searchbox_input")  # Find the search box
elem.send_keys(query + Keys.RETURN)

# browser.quit()
