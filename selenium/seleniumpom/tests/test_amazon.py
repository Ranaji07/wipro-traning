import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


# def test_open_amazon(driver):
#     assert "amazon" in  driver.current_url, 'URL for amazon in not correct'
#     print("\nOpened Amazon Homepage. Title & URL verified.")
#     @pytest.mark.parametrize("searchproduct",[
#         ("wireless mouse"), ("shoes")
#     ])
# def test_search_product(driver):
#     homepage = HomePage(driver)
#
#     homepage.type_search_input(searchproduct)
#     print(f"Searching product - {searchproduct}")
#     homepage.click_search_button()
#
#     assert  homepage.is_amazone_page_loaded(), 'Search results page did not load'
#     print(f"Search results page loaded successfully") - {searchproduct}
#     productlistingpage = ProductListingPage(driver)
#     productlistingpage.find_product_titles()
#     val = productlistingpage.all_products()
#
# def test_find_elements_amazon(driver):
#     productlistingpage = ProductListingPage(driver)
#
#     productlistingpage.find_product_titles(driver)
#     productlistingpage.all_products()
#
#     assert val, "No products found on Amazon search results!"
@pytest.mark.parametrize(("searchproduct", "brandname)" [
         ("wireless mouse"), ("Logitech")
         ("shoes", "Nike")
]))
def test_brand_filter(driver, searchproduct, brandname, mensize=None):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazone_page_loaded(), 'Search results page did not load'
    print(f"Search results page loaded successfully")
    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter()

    assert productlistingpage.check_product_titel_for_brand_filter('Logitech'), 'Brand filter did not apply'
    # productlistingpage.select_brand_filter(mensize)
    # assert productlistingpage.check_size_in_title(mensize), 'mensize filter did not apply'