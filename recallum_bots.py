from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# current chromedriver vers : 114
browser = webdriver.Chrome()

browser.maximize_window()

browser.get('https://recallum.reka.re/')

# waiting for 3 seconds (for pages to load up)
time.sleep(5)

browser.find_element(By.XPATH, '//*[@id="START"]').click()

time.sleep(3)

# browser.find_element(By.XPATH, '//*[@id="Wordloader"]')

for x in range(9):
    browser.find_element(By.XPATH, '//*[@id="N"]').click()

browser.find_element(By.XPATH, '//*[@id="Y"]').click()

for x in range(9):
    browser.find_element(By.XPATH, '//*[@id="N"]').click()

browser.find_element(By.XPATH, '//*[@id="Y"]').click()

for x in range(9):
    browser.find_element(By.XPATH, '//*[@id="N"]').click()

browser.find_element(By.XPATH, '//*[@id="Y"]').click()

for x in range(9):
    browser.find_element(By.XPATH, '//*[@id="N"]').click()

browser.find_element(By.XPATH, '//*[@id="Y"]').click()

time.sleep(15)





