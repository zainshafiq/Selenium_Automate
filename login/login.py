import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up logging
logging.basicConfig(filename='TEST_REPORT.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

browser = webdriver.Chrome()

# Maximize the window
browser.maximize_window()

browser.get('https://the-internet.herokuapp.com/')

# Waiting for 3 seconds (for pages to load up)
time.sleep(3)

# Find element by "link text"
browser.find_element(By.LINK_TEXT, "Digest Authentication").click()

# Find element by "partial link text"
# browser.find_element(By.PARTIAL_LINK_TEXT, "Auth").click()

time.sleep(2)