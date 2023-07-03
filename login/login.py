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
time.sleep(5)

# ---------------------------------------------------- FIRST TEST - FAILED LOGIN ----------------------------------------------------------------------------- #

# Log the test step of inputting the wrong credentials
logging.info('INPUTTING THE WRONG CREDENTIALS')

# Input wrong credentials to see its fail - Find element by NAME
browser.find_element(By.NAME, "username").send_keys(email1)
browser.find_element(By.NAME, "password").send_keys(password1)

time.sleep(2)

# Click login - Find element by XPATH
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(2)

browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]').screenshot('fail_Alert.png')

# Take a screenshot
browser.save_screenshot("fail_Login.png")
print('FIRST TEST .... SUCCESS - FAILED LOGIN')

# Log the test step and result
logging.info('FIRST TEST .... SUCCESS - FAILED LOGIN')

# ---------------------------------------------------- SECOND TEST - SUCCESSFUL LOGIN ----------------------------------------------------------------------------- #

# Refresh the page
browser.refresh()

# Waiting for 5 seconds (for pages to refresh)
time.sleep(5)

# Log the test step of inputting the correct credentials
logging.info('INPUTTING THE CORRECT CREDENTIALS')

# Input the correct credentials to see its pass - Find element by NAME
browser.find_element(By.NAME, "username").send_keys(email)
browser.find_element(By.NAME, "password").send_keys(password)

# Click login - Find element by XPATH
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(5)

# Take a screenshot
browser.save_screenshot("success_Login.png")
print('SECOND TEST .... SUCCESS - SUCCESSFUL LOGIN')

# Log the test step and result
logging.info('SECOND TEST .... SUCCESS - SUCCESSFUL LOGIN')

time.sleep(5)

# Close the WebDriver
# browser.quit()

# ---------------------------------------------------- THIRD TEST - LOGOUT AND FORGOT ----------------------------------------------------------------------------- #

# Click profile, dropdown menu
browser.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()

# Logout and back to login page
browser.find_element(By.ROLE, "menuitem").click()
