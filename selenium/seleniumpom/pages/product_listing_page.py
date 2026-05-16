# import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")
    # BRAND_FILTER = (By.XPATH, "//span[text()='Logitech']/pareent::a/descendant::input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def find_product_titles(self):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\nFirst Products:", first_product.text)

    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        for i, title in enumerate(product_titles[:5], start=1):
            print(f"{i}, {title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(self, brandname):
        BRAND_FILTER = (By.XPATH, "//span[text()="' + brandname + '"]/pareent::a/descendant::")
        # print("Brand Filter:", BRAND_FILTER)
        return BRAND_FILTER

    def select_brand_filter(self):
        brand_filter = self.driver.find_element(*self.BRAND_FILTER)
        brand_filter.click()

    def check_product_title_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLES))

        for title in product_titles:
            print("Title:", title.text)
            # time.sleep(30)
            if title.text.__contains__(brandname):
                return False
        return True

    def mensize_locator(self, mensize):
        MENSIZE_FILTER = (By.XPATH, "(//span[@class='a-list-item']/descendant::button[@value='" + mensize + "'])[1]")
        return MENSIZE_FILTER
    def select_mensize_filter(self, mensize):
        mensize_filter = self.driver.find_element(*self.mensize_locator(mensize))
        mensize_filter.click()

    def check_size(self, mensize):
        return self.driver.titel.__contains__(mensize)
