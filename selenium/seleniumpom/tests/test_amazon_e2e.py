import time
import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage

@pytest.mark.parametrize(("searchproduct", "brandname)"
[
    ("shoes", "Nike", "9")
]))
def test_brand_filter(driver, searchproduct, brandname, mansize, mensize=None):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazone_page_loaded(), 'Search results page did not load'
    print(f"Search results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter()

    assert productlistingpage.check_product_titel_for_brand_filter('Logitech'), 'Brand filter did not apply'
    productlistingpage.select_brand_filter(mensize)
    assert productlistingpage.check_size_in_title(mensize), 'mensize filter did not apply'
