from selenium import webdriver

# Открываем браузер FireFox
driver = webdriver.Firefox()

driver.get("http://www.google.com")
print(driver.title)
driver.quit()
