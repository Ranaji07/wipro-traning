from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(3)

# text input
text_input = driver.find_element(By.ID,value="my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#password input
password_input = driver.find_element(By.NAME, value="my-password")
password_input.clear()
password_input.send_keys("secret123")

# text area
textarea = driver.find_element(By.NAME, value="my-textarea")
textarea.clear()
textarea.send_keys("This is a sample message.")

# checkbox
checkbox = driver.find_element(By.ID, value="my-check-2")
checkbox.click()

# radio
radio = driver.find_element(By.ID, value="my-radio-2")
radio.click()

# dropdown
dropdown = driver.find_element(By.NAME, value="my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, value="select[name='my-select'] option[value='2']")
option.click()

# multi-select
multi_select = driver.find_element(By.NAME, value="my-datalist")
multi_select.send_keys('New York')

# file upload
file_upload = driver.find_element(By.NAME, value="my-file")
file_upload.send_keys("C:\\wipro traning\\selenium\\automation basics\\selenium_basics")

# range slider
range_slider = driver.find_element(By.NAME, value="my-range")
driver.execute_script(script="arguments[0].value = 10;", args= range_slider)

# date picker
date_input = driver.find_element(By.NAME, value="my-date")
date_input.send_keys("2025-12-25")

# colour picker
color_picker = driver.find_element(By.NAME, value="my-color")
color_picker.send_keys("#00ff00")

# submit button
submit_btn = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(20)
driver.quit()