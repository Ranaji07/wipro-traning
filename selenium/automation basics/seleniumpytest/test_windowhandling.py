import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    yield driver
    driver.quit()

def test_multiple_windows_handle(driver):
    wait = WebDriverWait(driver, timeout=10)
    parent_window = dr