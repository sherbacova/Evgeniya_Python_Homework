from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Устанавливаем ChromeDriver с помощью webdriver_manager
service = ChromeService(ChromeDriverManager().install())

# Инициализируем драйвер Chrome с использованием установленного сервиса
driver = webdriver.Chrome(service=service)

# Открываем целевую страницу
driver.get("http://uitestingplayground.com/classattr/")

# Находим кнопку по CSS-селектору
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

# Кликаем на кнопку
button.click()

# Закрываем браузер
driver.quit()