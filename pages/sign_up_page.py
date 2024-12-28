import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SIGN_UP_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    CUSTOMER_MENU = (By.CSS_SELECTOR,"div[class='panel header'] button[type='button']")
    SIGN_OUT = (By.CSS_SELECTOR,"div[aria-hidden='false'] li[data-label='or'] a")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_sign_up(self):
        self.driver.find_element(*self.SIGN_UP_BUTTON).click()

    def click_Customer_menu(self):
        time.sleep(5)
        self.driver.find_element(*self.CUSTOMER_MENU).click()

    def click_sign_out(self):
        time.sleep(2)
        self.driver.find_element(*self.SIGN_OUT).click()

    def create_account(self, first_name, last_name, email, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_sign_up()
        self.click_Customer_menu()
        self.click_sign_out()
