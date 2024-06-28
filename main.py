from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

EMAIL = "email"
PASSWORD = "linkedin password"
PHONE = "phone number"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/")

email_signin = driver.find_element(By.NAME, value="session_key")
email_signin.click()
email_signin.send_keys(EMAIL)
password = driver.find_element(By.ID, value= "session_password")
password.send_keys(PASSWORD)
signin_button = driver.find_element(By.ID, value="sign-in-form__submit-btn")
signin_button.click()

time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()


