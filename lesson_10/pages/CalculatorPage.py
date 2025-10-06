from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import Severity

@allure.feature("Страница калькулятора")
class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.
    """
    def __init__(self, driver: WebDriver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 46)

        # Локаторы для элементов калькулятора
        self.delay_input_locator = (By.ID, "delay")
        self.button_7_locator = (By.XPATH, "//span[text()='7']")  # Использую XPATH для текста
        self.button_plus_locator = (By.XPATH, "//span[text()='+']")
        self.button_8_locator = (By.XPATH, "//span[text()='8']")
        self.button_equals_locator = (By.XPATH, "//span[text()='=']")
        self.result_locator = (By.CLASS_NAME, "screen")  # Или другой подходящий локатор

    @allure.step( "Открытие страницы калькулятора" )
    def open(self,url: str):
        """
        Открывает страницу калькулятора.
        :param  url: str — URL страницы калькулятора.
        :return: None
        """
        self.driver.get( "https://bonigarcia.dev/"
                         "selenium-webdriver-java/slow-calculator.html" )
        self.driver.get(url)

    @allure.step( "Установка задержки {delay} секунд" )
    def enter_delay(self, delay: str):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: str — время задержки в секундах.
        :return: None
        """
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()  # Очищаем поле перед вводом
        delay_input.send_keys(delay)

    @allure.step( "Нажатие кнопки '{locator}'" )
    def click_button(self, locator):
        """
        Нажимает на кнопку калькулятора.

        :param locator: str — текст на кнопке, которую нужно нажать.
        :return: None
        """
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step( "Получение результата с экрана калькулятора" )
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        # Ожидаем, пока результат появится на экране
        self.wait.until(EC.text_to_be_present_in_element(self.result_locator, "15"))
        result_element = self.driver.find_element(*self.result_locator)
        return result_element.text