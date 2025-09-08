from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_button_locator = (By.CSS_SELECTOR, "[name='login-button']")

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_locator)
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_locator)
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()