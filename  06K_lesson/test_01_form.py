import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():

    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)  # Неявные ожидания использовать нежелательно, лучше явные
    yield driver # Предоставляет driver тестовой функции
    driver.quit()

def test_form(driver):
    # Заполнение формы
    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")

    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")

    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")

    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    job_position.send_keys("QA")

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
    submit_button.click()

    # Проверки (используем явные ожидания) Сделано с использованием проверки класса из-за динамического изменения класса при валидации.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'zip-code')))
    zip_code_field = driver.find_element(By.ID, "zip-code") #Обновляем элемент

    assert "danger" in zip_code_field.get_attribute("class") # проверяем естьли нужный класс


    # Проверка, что остальные поля подсвечены зеленым
    valid_fields_selectors = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for selector in valid_fields_selectors:

        field = driver.find_element(By.ID, selector)

        assert "success" in field.get_attribute("class")