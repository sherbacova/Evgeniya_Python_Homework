import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from CalculatorPage import CalculatorPage

@pytest.fixture()
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page.enter_delay("45")
    calculator_page.click_button(calculator_page.button_7_locator)
    calculator_page.click_button(calculator_page.button_plus_locator)
    calculator_page.click_button(calculator_page.button_8_locator)
    calculator_page.click_button(calculator_page.button_equals_locator)


    result = calculator_page.get_result()
    assert result == "15", f"Expected result to be 15, but got {result}"