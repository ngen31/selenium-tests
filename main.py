#import selenium
import time
from os.path import exists

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Open browser
opts = Options();
opts.add_argument("--headless=new");
opts.add_argument("--no-sandbox");
opts.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=opts)
#time.sleep(2)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
#time.sleep(4)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
#time.sleep(1)

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
#time.sleep(1)

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
log_out_button_locator_xpath = driver.find_element(By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']")
log_out_button_locator_link_text = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator_link_text.is_displayed()
assert log_out_button_locator_xpath.is_displayed()
