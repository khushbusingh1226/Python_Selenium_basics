from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.reddit.com/")
driver.maximize_window()
print(driver.get_cookies())
driver.add_cookie({"name": "khushbu", "domain": "www.reddit.com", "value": "Python"})
cookies = driver.get_cookies()

for cook in cookies:
    print(cook)
time.sleep(5)
driver.quit()
