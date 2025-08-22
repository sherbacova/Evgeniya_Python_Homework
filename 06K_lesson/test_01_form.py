
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(scope="module")
def driver():
    options = EdgeOptions()
    options.use_chromium = True  # Ensure Chromium-based Edge is used
    edge_driver_path = r"D:\Edge\драйвер Edge"\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    yield driver
    driver.quit()


