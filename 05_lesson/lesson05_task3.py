from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Устанавливаем GeckoDriver (Firefox) с помощью webdriver_manager
service = FirefoxService(GeckoDriverManager().install())

# Инициализируем драйвер Firefox
driver = webdriver.Firefox(service=service)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода (предположим, что оно одно на странице)
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "Sky"
input_field.send_keys("Sky")

# Очищаем поле
input_field.clear()

# Вводим текст "Pro"
input_field.send_keys("Pro")

# Закрываем браузер
driver.quit()