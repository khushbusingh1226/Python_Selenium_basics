"""
Dynamic wait
time to wait for seconds
Global wait
apply only for web elements like find element and find elements
not applicable for alerts, titles,URL
default time is 500 milliseconds
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://app.hubspot.com/')
print(driver.title)
driver.implicitly_wait(5)
# override from 10 to 5
driver.find_element(By.ID, 'username').send_keys('k@gmail.com')
driver.implicitly_wait(0)
# nulify implicitly wait is 0
driver.find_element(By.ID, 'password').send_keys('test123')
