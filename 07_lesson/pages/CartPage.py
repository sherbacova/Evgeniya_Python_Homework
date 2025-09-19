from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.checkout_button_locator = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button_locator).click()