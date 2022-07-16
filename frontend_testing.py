from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\ohada\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)
driver.get('http://127.0.0.1:5001/get_user_name/1')
print(driver.find_element(by=By.ID, value="1").text)
driver.quit()