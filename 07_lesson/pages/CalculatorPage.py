from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 46)

        # Локаторы для элементов калькулятора
        self.delay_input_locator = (By.ID, "delay")
        self.button_7_locator = (By.XPATH, "//span[text()='7']")  # Использую XPATH для текста
        self.button_plus_locator = (By.XPATH, "//span[text()='+']")
        self.button_8_locator = (By.XPATH, "//span[text()='8']")
        self.button_equals_locator = (By.XPATH, "//span[text()='=']")
        self.result_locator = (By.CLASS_NAME, "screen")  # Или другой подходящий локатор

    def open(self, url):
        self.driver.get(url)

    def enter_delay(self, delay):
        delay_input = self.driver.find_element(*self.delay_input_locator)
        delay_input.clear()  # Очищаем поле перед вводом
        delay_input.send_keys(delay)

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def get_result(self):
        # Ожидаем, пока результат появится на экране
        self.wait.until(EC.text_to_be_present_in_element(self.result_locator, "15"))
        result_element = self.driver.find_element(*self.result_locator)
        return result_element.text

