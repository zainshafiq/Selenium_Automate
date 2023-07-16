import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Admin credentials
username = "Admin"
password = "admin123"

# Set up logging
logging.basicConfig(filename='this_REPORT_filling_forms.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

browser = webdriver.Chrome()

# Maximize the window
browser.maximize_window()

# Use orangeHRM demo website
browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Waiting for 3 seconds (for pages to load up)
time.sleep(3)

# ---------------------------------------------------- FIRST TEST - SUCCESSFUL LOGIN ----------------------------------------------------------------------------- #

# Log the test step of inputting the correct credentials
logging.info('INITIATE FIRST TEST - SUCCESSFULL LOGIN')

# Input the correct credentials to see its pass - Find element by NAME
logging.info('INPUTTING USERNAME')
browser.find_element(By.NAME, "username").send_keys(username)
logging.info('INPUTTING PASSWORD')
browser.find_element(By.NAME, "password").send_keys(password)

# Click login - Find element by XPATH
logging.info('CLICKING THE LOGIN BUTTON')
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(5)

# Take a screenshot
browser.save_screenshot("success_Login.png")
print('FIRST TEST .... SUCCESS - SUCCESSFUL LOGIN')

# Log the test step and result
logging.info('FIRST TEST .... SUCCESS - SUCCESSFUL LOGIN')

time.sleep(3)

# ---------------------------------------------------- SECOND TEST - FILLING UP FIRST FORM ----------------------------------------------------------------------------- #

# Log the test step of inputting the correct credentials
logging.info('INITIATE SECOND TEST - SUCCESSFULL LOGIN')

# Click My Info - Find element by XPATH
logging.info('CLICKING THE MY INFO OPTION BUTTON')
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()

time.sleep(5)

# Close the WebDriver
browser.quit()