from selenium import webdriver
import pytest
from Drivers.Drivers import executables


@pytest.fixture
def setUp():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executables.CHROME_EXECUTABLE_PATH, options = chrome_options)
    return driver