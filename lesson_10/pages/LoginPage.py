from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import allure
from allure_commons.types import Severity

@allure.feature("Страница логина")
class LoginPage:
    """
    Класс, представляющий страницу логина.
    """
    def __init__(self, driver: WebDriver):
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_button_locator = (By.CSS_SELECTOR, "[name='login-button']")

    @allure.step("Открытие страницы логина")
    def open(self, url: str):
        """
        Открывает страницу логина по указанному URL.

        :param url: str — URL страницы логина.
        :return: None
        """
        self.driver.get(url)

    @allure.step("Ввод имени пользователя '{username}'")
    def enter_username(self, username: str):
        """
        Вводит имя пользователя в поле "Username".

        :param username: str — имя пользователя.
        :return: None
        """
        username_field = self.driver.find_element(*self.username_locator)
        username_field.send_keys(username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        """
        Вводит пароль в поле "Password".

        :param password: str — пароль.
        :return: None
        """
        password_field = self.driver.find_element(*self.password_locator)
        password_field.send_keys(password)

    @allure.step("Нажатие кнопки 'Login'")
    def click_login(self):
        """
        Кликает на кнопку "Login".

        :return: None
        """
        self.driver.find_element(*self.login_button_locator).click()

    @allure.step("Выполнение логина с именем пользователя '{username}' и паролем")
    def login(self, username, password: str):
        """
        Выполняет процесс логина.

        :param username: str — имя пользователя.
        :param password: str — пароль.
        :return: None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()