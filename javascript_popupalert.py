from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME, 'proceed').click()
time.sleep(5)

alertpopup = driver.switch_to.alert
print(alertpopup.text)
alertpopup.accept()
#
# alertpopup.send_keys('test')
driver.switch_to.default_content()
driver.quit()
