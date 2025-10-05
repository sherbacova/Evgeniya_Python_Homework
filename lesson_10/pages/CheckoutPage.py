from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import allure
from allure_commons.types import Severity

@allure.feature("Страница оформления заказа")
class CheckoutPage:
    """
    Класс, представляющий страницу оформления заказа.
    """
    def __init__(self, driver: WebDriver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Add wait

        self.firstname_locator = (By.ID, "first-name")
        self.lastname_locator = (By.ID, "last-name")
        self.postalcode_locator = (By.ID, "postal-code")
        self.continue_button_locator = (By.ID, "continue")
        self.total_locator = (By.CLASS_NAME, "summary_total_label")
        self.finish_button_locator = (By.ID, "finish")

    @allure.step( "Ввод имени '{firstname}'" )
    def enter_firstname(self, firstname: str):
        """
        Вводит имя в поле "First Name".

        :param firstname: str — имя для ввода.
        :return: None
        """
        firstname_field = self.driver.find_element(*self.firstname_locator)
        firstname_field.send_keys(firstname)

    @allure.step( "Ввод фамилии '{lastname}'" )
    def enter_lastname(self, lastname: str):
        """
        Вводит фамилию в поле "Last Name".

        :param lastname: str — фамилия для ввода.
        :return: None
        """
        lastname_field = self.driver.find_element(*self.lastname_locator)
        lastname_field.send_keys(lastname)

    @allure.step( "Ввод почтового кода '{postalcode}'" )
    def enter_postalcode(self,  postalcode: str):
        """
        Вводит почтовый код в поле "Postal Code".

        :param postalcode: str — почтовый код для ввода.
        :return: None
        """

        postalcode_field = self.driver.find_element(*self.postalcode_locator)
        postalcode_field.send_keys(postalcode)

    @allure.step( "Нажатие кнопки 'Continue'" )
    def click_continue(self):
        """
        Кликает на кнопку "Continue".

        :return: None
        """
        self.driver.find_element(*self.continue_button_locator).click()

    @allure.step( "Получение итоговой суммы" )
    def get_total(self):
        """
        Получает итоговую сумму заказа.

        :return: str — текст, содержащий итоговую сумму.
        """

        total_element = self.driver.find_element(*self.total_locator)
        return total_element.text

    @allure.step("Заполнение формы оформления заказа: имя='{firstname}', фамилия='{lastname}', почтовый код='{postalcode}'" )
    def fill_form(self, firstname, lastname, postalcode):
        """
        Заполняет форму оформления заказа.

        :param firstname: str — имя.
        :param lastname: str — фамилия.
        :param postalcode: str — почтовый код.
        :return: None
        """
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_postalcode(postalcode)
        self.click_continue()

    @allure.step( "Нажатие кнопки 'Finish'" )
    def click_finish(self):
        """
        Кликает на кнопку "Finish".

        :return: None
        """
        self.driver.find_element(*self.finish_button_locator).click()