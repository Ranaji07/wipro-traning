# from re import search
import driver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:

    SEARCH_INPUT = (By.Id, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")


    @pytest.mark.parametrize("searchproduct", [
        ("wireless mouse")
    ])


    def __init__(self, driver):
        self.driver = driver
    wait = WebDriverWait(driver, timeout=5)

    def type_search_input(self, searchproduct):
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys("wireless mouse")

    def click_search_button(self, searchproduct):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def is_amazone_page_loaded(self):
        return self.driver.current_url.__contains__('amazon') and self.driver.title.__contains__('Amazon')


