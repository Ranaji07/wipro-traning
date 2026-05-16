
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    yield driver
    driver.quit()

def test_open_amozon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "amazon" in driver.title, 'Title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, timeout=5)
    search_box = wait.until(EC.presence_of_element_located(By.ID, "twoabsearchtextbox"))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, value="nav-search-button")
    search_button.click()
    assert driver.current_url.__contains__('wireless'), 'Search results page did not load.'
    assert driver.title.__contains__('wireless'), 'Search results page did not load.'
    print("\nSearch result page loaded successfully")

def test_find_elements_amazone(driver):
    wait = WebDriverWait(driver, timeout=15)

    first_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print("\nFirst Product:", first_product.text)
    product_title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print(f"\nFound {len(product_title)} product titles on page one.\n")
    for i, title in enumerate(product_title[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_title) > 0, "No products"