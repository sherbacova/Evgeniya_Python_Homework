from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #для разворачивания окна
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
updated_button_text = button.text
print(updated_button_text)

driver.quit()

