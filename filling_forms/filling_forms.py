import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up logging
logging.basicConfig(filename='this_REPORT_filling_forms.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

browser = webdriver.Chrome()

# Maximize the window
browser.maximize_window()

# Use orangeHRM demo website
browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Waiting for 3 seconds (for pages to load up)
time.sleep(5)

# Close the WebDriver
browser.quit()