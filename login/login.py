import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Admin credentials
email = "Admin"
password = "admin123"

# Fail Admin credential
email1 = "admin1"
password1 = "password1"

# Set up logging
logging.basicConfig(filename='this_REPORT.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

browser = webdriver.Chrome()

# Maximize the window
browser.maximize_window()

browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Waiting for 3 seconds (for pages to load up)
time.sleep(3)

# Input wrong credentials to see its fail - Find element by NAME
browser.find_element(By.NAME, "username").send_keys(email1)
browser.find_element(By.NAME, "password").send_keys(password1)

# Click login - Find element by LINK TEXT
browser.find_element(By.LINK_TEXT, "login").click()

time.sleep(2)