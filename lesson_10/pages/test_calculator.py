import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from CalculatorPage import CalculatorPage
import allure
from allure_commons.types import Severity



@pytest.fixture()
def driver():
    """
    Фикстура Pytest для создания и настройки веб-драйвера Chrome.
    """
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тест сложения на калькуляторе")
@allure.description("Проверяет сложение чисел 7 и 8 на странице калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(Severity.NORMAL)
def test_calculator(driver):
    """
    Тест сложения чисел на калькуляторе.
    """
    with allure.step( "Инициализация страницы калькулятора" ):
        calculator_page = CalculatorPage( driver )
    with allure.step( "Открытие страницы калькулятора" ):
        calculator_page.open( "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html" )

    with allure.step( "Ввод задержки" ):
        calculator_page.enter_delay( "46" )
    with allure.step( "Нажатие кнопки '7'" ):
        calculator_page.click_button( calculator_page.button_7_locator )
    with allure.step( "Нажатие кнопки '+'" ):
        calculator_page.click_button( calculator_page.button_plus_locator )
    with allure.step( "Нажатие кнопки '8'" ):
        calculator_page.click_button( calculator_page.button_8_locator )
    with allure.step( "Нажатие кнопки '='" ):
        calculator_page.click_button( calculator_page.button_equals_locator )

    with allure.step( "Получение результата" ):
        result = calculator_page.get_result()
    with allure.step( "Проверка результата" ):
        assert result == "15", f"Expected result to be 15, but got {result}"