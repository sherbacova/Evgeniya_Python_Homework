from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
images = driver.find_elements(By.TAG_NAME, "img")

print(len(images)) # Вывод количества найденных изображений

if len(images) >= 3:
    src_attribute = images[2].get_attribute("src")
    print(src_attribute)
else:
    print("На странице меньше трех изображений.")

driver.quit()

