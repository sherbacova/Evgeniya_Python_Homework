from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from allure_commons.types import Severity


@allure.feature("Страница корзины")
class CartPage:
    """
    Класс, представляющий страницу корзины.
    """
    def __init__(self, driver: WebDriver):
        """
        Конструктор класса  CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.checkout_button_locator = (By.ID, "checkout")

    @allure.step( "Нажатие на кнопку 'Checkout'" )
    def click_checkout(self):
        """
         Кликает на кнопку "Checkout".

         :return: None
        """
        self.driver.find_element(*self.checkout_button_locator).click()