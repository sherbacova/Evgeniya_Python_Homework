import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/  ")

    yield driver
    driver.quit()

def test_shop(driver):
    user_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")

    password= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")


    driver.find_element(By.CSS_SELECTOR, "[name='login-button']").click()


    #добавление в карзину
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    #переход в карзину
    driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()

    #нажать Checkout
    driver.find_element(By.ID,"checkout").click()

    #заполнение формы


    search_box = driver.find_element( By.ID,"first-name")
    search_box.send_keys("Zhenya")

    search_box = driver.find_element(By.ID, "last-name")
    search_box.send_keys("Ivanova")

    search_box = driver.find_element(By.ID, "postal-code")
    search_box.send_keys("197235")

    driver.find_element(By.ID, "continue").click()

    total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text



    # Проверка итоговой суммы
    assert total_cost == "Total: $58.29", f"Итоговая сумма должна быть 58.29,  получена {total_cost}"
    driver.find_element(By.ID, "finish").click()


