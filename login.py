import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up logging
logging.basicConfig(filename='TEST_REPORT.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

browser = webdriver.Chrome()

# Maximize the window
browser.maximize_window()

browser.get('https://www.veltra.com/en')

# Waiting for 3 seconds (for pages to load up)
time.sleep(3)