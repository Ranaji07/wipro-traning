import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()


def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, value="/button[text()='Click for JS Alert']")
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", 'Alert text was wrong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, value="result").text
    assert "You successfully clicked an alert" in result, 'Result text was wrong'

def test_js_confirmdismiss(driver):
    driver.find_element(By.XPATH, value="//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am JS Confirm", 'Alert text was wrong'
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, value="result").text
    assert "You clicked: Cancel" in result, 'Result text was wrong'

def test_js_confirmok(driver):
    driver.find_element(By.XPATH, value="//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am JS Confirm", 'Alert text was wrong'
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, value="result").text
    assert "You clicked: Ok" in result, 'Result text was wrong'

def test_js_prompt(driver):
    driver.find_element(By.XPATH, value="//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    time.sleep(3)
    assert alert.text == "I am JS Prompt", 'Alert text was wrong'
    alert.send_keys("Python Selenium")
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, value="result").text
    assert "Python Selenium" in result, 'Result text was wrong'

def test_multiple_windows_handel(driver):
    wait = WebDriverWait(driver, timeout=10)
    parent_window =

