import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo_flow(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Add items to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # 3. Go to cart
    inventory_page.go_to_cart()

    # 4. Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 5. Fill checkout form
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Zhenya", "Ivanova", "197235")

    # 6. Get total cost
    total_cost = checkout_page.get_total()

    # 7. Assert total cost
    assert total_cost == "Total: $58.29", f"Expected total to be $58.29, but got {total_cost}"
    checkout_page.click_finish()