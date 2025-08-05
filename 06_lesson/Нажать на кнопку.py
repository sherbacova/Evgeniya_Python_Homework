from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window() #для разворачивания окна
driver.get(" http://uitestingplayground.com/ajax")

input_field = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

wait = WebDriverWait(driver, 10)
green_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
# 3. Получаем текст из зеленой плашки
text = green_button.text


# 4. Выводим текст в консоль
print(text)

driver.quit()




