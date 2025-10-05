from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from allure_commons.types import Severity

@allure.feature("Страница инвентаря")
class InventoryPage:
    """
    Класс, представляющий страницу инвентаря (каталог товаров).
    """
    def __init__(self, driver: WebDriver):
        """
        Конструктор класса InventoryPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.backpack_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.tshirt_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.cart_link_locator = (By.CSS_SELECTOR, "[class='shopping_cart_link']")

    @allure.step( "Добавление товара в корзину по локатору" )
    def add_to_cart(self, locator):
        """
        Добавляет товар в корзину по заданному локатору.

        :param locator: tuple — локатор элемента "Add to cart".
        :return: None
        """
        self.driver.find_element( *locator ).click()

    @allure.step( "Добавление рюкзака в корзину" )
    def add_backpack_to_cart(self):
        """
        Добавляет рюкзак в корзину.

        :return: None
        """
        self.add_to_cart( self.backpack_locator )

    @allure.step( "Добавление футболки в корзину" )
    def add_tshirt_to_cart(self):
        """
        Добавляет футболку в корзину.

        :return: None
        """
        self.add_to_cart( self.tshirt_locator )
        self.add_to_cart( self.tshirt_locator )

    @allure.step( "Добавление детского комбинезона в корзину" )
    def add_onesie_to_cart(self):
        """
        Добавляет детский комбинезон в корзину.

        :return: None
        """
        self.add_to_cart( self.onesie_locator )

    @allure.step( "Переход в корзину" )
    def go_to_cart(self):
        """
        Переходит в корзину.

        :return: None
        """
        self.driver.find_element( *self.cart_link_locator ).click()
