import pytest
from selenium import webdriver
from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from selenium.webdriver.firefox.webdriver import WebDriver
import allure
from allure_commons.types import Severity



@pytest.fixture()
def driver():
    """
    Фикстура Pytest для создания и настройки веб-драйвера Firefox.
    """
    driver: WebDriver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
@allure.title("Сквозной тест Saucedemo")
@allure.description("Проходит полный флоу покупки на сайте Saucedemo: логин, добавление товаров в корзину,"
                      "оформление заказа и проверка итоговой стоимости.")
@allure.feature("Покупка товаров")
@allure.severity(Severity.CRITICAL)
def test_saucedemo_flow(driver):
    """
    Тест, проходящий полный флоу покупки на сайте Saucedemo.
    """
    with allure.step( "1. Логин" ):
        login_page = LoginPage( driver )
        login_page.open( "https://www.saucedemo.com/" )
        login_page.login( "standard_user", "secret_sauce" )

    with allure.step( "2. Добавление товаров в корзину" ):
        inventory_page = InventoryPage( driver )
        inventory_page.add_backpack_to_cart()
        inventory_page.add_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

    with allure.step( "3. Переход в корзину" ):
        inventory_page.go_to_cart()

    with allure.step( "4. Переход к оформлению заказа" ):
        cart_page = CartPage( driver )
        cart_page.click_checkout()

    with allure.step( "5. Заполнение формы оформления заказа" ):
        checkout_page = CheckoutPage( driver )
        checkout_page.fill_form( "Zhenya", "Ivanova", "197235" )

    with allure.step( "6. Получение итоговой стоимости" ):
        total_cost = checkout_page.get_total()

    with allure.step( "7. Проверка итоговой стоимости" ):
        assert total_cost == "Total: $58.29", f"Expected total to be $58.29, but got {total_cost}"
        checkout_page.click_finish()