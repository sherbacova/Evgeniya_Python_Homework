from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.backpack_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.tshirt_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_locator = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        self.cart_link_locator = (By.CSS_SELECTOR, "[class='shopping_cart_link']")

    def add_to_cart(self, locator):
        self.driver.find_element(*locator).click()

    def add_backpack_to_cart(self):
        self.add_to_cart(self.backpack_locator)

    def add_tshirt_to_cart(self):
        self.add_to_cart(self.tshirt_locator)

    def add_onesie_to_cart(self):
        self.add_to_cart(self.onesie_locator)

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link_locator).click()
        