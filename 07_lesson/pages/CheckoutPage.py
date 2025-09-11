from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Add wait

        self.firstname_locator = (By.ID, "first-name")
        self.lastname_locator = (By.ID, "last-name")
        self.postalcode_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")
        self.total_locator = (By.CLASS_NAME, "summary_total_label")
        self.finish_button_locator = (By.ID, "finish")


    def enter_firstname(self, firstname):
        firstname_field = self.driver.find_element(*self.firstname_locator)
        firstname_field.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = self.driver.find_element(*self.lastname_locator)
        lastname_field.send_keys(lastname)

    def enter_postalcode(self, postalcode):
        postalcode_field = self.driver.find_element(*self.postalcode_locator)
        postalcode_field.send_keys(postalcode)

    def click_continue(self):
        self.driver.find_element(*self.continue_button_locator).click()

    def get_total(self):

        total_element = self.driver.find_element(*self.total_locator)
        return total_element.text

    def fill_form(self, firstname, lastname, postalcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_postalcode(postalcode)
        self.click_continue()
    def click_finish(self):

       self.driver.find_element(*self.finish_button_locator).click()