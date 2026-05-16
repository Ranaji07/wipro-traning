import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.relative_locator import locate_with

from selenium_basics.google_homepage_test import driver

#
# driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

# driver.get("https://www.google.com")

#id
# search_input = driver.find_element(By.Id, value="APjFqb.gLFyf")
# search_input.send_keys("selenium")
# time.sleep(3)
# search_input.clear()
# time.sleep(3)

#name
# search_input = driver.find_element(By.NAME, value='q')
# search_input.send_keys("location")
# time.sleep(10)
#
# # name
# googlesearch_button = driver.find_element(By.NAME, value='btnK')
# googlesearch_button.click()
# time.sleep(30)

# classname
# imfl_button = driver.find_element(By.CLASS_NAME."RNmpXc")
# imfl_button.click()
# time.sleep(10)

# tagname
# href_elements = driver.find_element(By.TAG_NAME, value='a')
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute('href')}')

# linktest
# images_link = driver.find_element(By.LINK_TEXT, value="Images")
# images_link.click()
# time.sleep(10)

# partial
# images_link = driver.find_element(By.PARTIAL_LINK_TEXT, value="ma")
# images_link.click()
# time.sleep(10)

# CSSsel
# search_input = driver.find_element(By.CSS_SELECTOR, value='div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)

# xpath
# settings_text = driver.find_element(By.XPATH,
#                                     value='/html/body/div[2]/div[7]/div/div[2]/div[2]/span/g-popup/div[1]/div')
# print(settings_text.text)
# time.sleep(5)

# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(5)

# AND & OR
# and_example = driver.find_element(By.XPATH, value="//td[text()='tim' and @class='first-name']")
# print(f"AND Example-> Found with both conditions: {and_example.text}")
#
# or_example = driver.find_element(By.XPATH, value="//td[text()='tim' or text()='Frank']")
# print(f"OR Example -> Found with OR condition: {for_example.text}")
#
#
# # child- select all
# rows = driver.find_elements(By.XPATH, value="//table[@id='table1']/tbody/tr/td")
# print(f"Child Example -> Found {len(rows)} columns in the first table.")
#
# # parent- get the parent row of particular cell
# email_cell = driver.find_element(By.XPATH, value="//table[@id='table1']//td[text()='jdoe@hotmail.com']")
# parent_row = driver.find_element(By.XPATH, value="//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
# print(f"Parent Example -> Email '{email_cell.text}'belongs to row with first name:"
#       f"{parent_row.find_element(By.XPATH, value='./td[2]').text}")

# ancestor
# ancestor_table = driver.find_element(By.XPATH, value="//td[text()='jsmith@gmail.com']/ancestor::table")
# print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")
#
# # descendants
# descendants = driver.find_elements(By.XPATH, value="//table[@id='table1']/descendant::td")
# print(f"Descendant Example -> Found {len(descendants)} descendant cells.")

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# elements used for reference
username_field = driver.find_element(By.ID, value="user-name")
password_field = driver.find_element(By.ID, value="password")
login_button = driver.find_element(By.ID, value="login-button")

# above -> elements located above other
elmt_above_password = driver.find_element(
    locate_with(By.TAG_NAME, using="input").above(password_field)
)
print(f"Above Example -> Text above password: {elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(5)

# below
field_below_username = driver.find_element(
    locate_with(By.TAG_NAME, using="input").below(username_field)
)
print(f"Below Example -> Placeholder below username: {field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys('standard_user')
time.sleep(5)
login_button.click(5)
time.sleep(5)

# to rightof
twitter_icon = driver.find_element(By.LINK_TEXT, value="Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME, using="a").to_right_of(twitter_icon))
print(f"toRightOf Example -> Element to the right of Twitter icon hs href: {facebook_icon.get_attribute('href')}")

# to lefof->
left_icon =driver.find_element(lo)