from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Устанавливаем GeckoDriver (Firefox) с помощью webdriver_manager
service = FirefoxService(GeckoDriverManager().install())

# Инициализируем драйвер Firefox
driver = webdriver.Firefox(service=service)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода (предположим, что оно одно на странице)
username_field = driver.find_element(By.ID, "username")

# Вводим текст "Sky"
username_field.send_keys("tomsmith")


# Вводим текст "Pro"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

success_message = driver.find_element(By.ID, "flash")
print(success_message.text)


driver.quit()
