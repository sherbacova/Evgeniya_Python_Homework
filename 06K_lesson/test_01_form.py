import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Initialize and return the Edge webdriver."""

    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_form_validation(driver):


    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Define locators
    first_name_locator = (By.NAME, "firstName")
    last_name_locator = (By.NAME, "lastName")
    address_locator = (By.NAME, "address")
    email_locator = (By.NAME, "eMail")
    phone_locator = (By.NAME, "phone")
    zip_code_locator = (By.NAME, "zipCode")
    city_locator = (By.NAME, "city")
    country_locator = (By.NAME, "country")
    job_locator = (By.NAME, "jobTitle")
    company_locator = (By.NAME, "company")
    submit_button_locator = (By.CSS_SELECTOR, "button.btn")

    # Find elements
    first_name = driver.find_element(*first_name_locator)
    last_name = driver.find_element(*last_name_locator)
    address = driver.find_element(*address_locator)
    email = driver.find_element(*email_locator)
    phone = driver.find_element(*phone_locator)
    zip_code = driver.find_element(*zip_code_locator)
    city = driver.find_element(*city_locator)
    country = driver.find_element(*country_locator)
    job = driver.find_element(*job_locator)
    company = driver.find_element(*company_locator)
    submit_button = driver.find_element(*submit_button_locator)

    # Fill the form
    first_name.send_keys("Иван")
    last_name.send_keys("Петров")
    address.send_keys("Ленина, 55-3")
    email.send_keys("test@skypro.com")
    phone.send_keys("+7985899998787")
    city.send_keys("Москва")
    country.send_keys("Россия")
    job.send_keys("QA")
    company.send_keys("SkyPro")

    # Click Submit
    submit_button.click()


    # Wait for the validation styles to be applied (adjust timeout as needed)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".is-invalid")))  # Or another criteria

    # Assertions
    assert "is-invalid" in zip_code.get_attribute("class"), "Zip code field is not highlighted in red."

    assert "is-valid" in first_name.get_attribute("class"), "First name field is not highlighted in green."
    assert "is-valid" in last_name.get_attribute("class"), "Last name field is not highlighted in green."
    assert "is-valid" in address.get_attribute("class"), "Address field is not highlighted in green."
    assert "is-valid" in email.get_attribute("class"), "Email field is not highlighted in green."
    assert "is-valid" in phone.get_attribute("class"), "Phone field is not highlighted in green."
    assert "is-valid" in city.get_attribute("class"), "City field is not highlighted in green."
    assert "is-valid" in country.get_attribute("class"), "Country field is not highlighted in green."
    assert "is-valid" in job.get_attribute("class"), "Job field is not highlighted in green."
    assert "is-valid" in company.get_attribute("class"), "Company field is not highlighted in green."