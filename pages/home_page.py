from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ACCOUNT_ICON = (By.CSS_SELECTOR, "div[class='panel header'] li[data-label='or'] a")
    SIGN_IN_EMAIL = (By.ID, "email")
    SIGN_IN_PASSWORD = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")

    def click_account_icon(self):
        self.driver.find_element(*self.ACCOUNT_ICON).click()

    def enter_sign_in_email(self, email):
        self.driver.find_element(*self.SIGN_IN_EMAIL).send_keys(email)

    def enter_sign_in_password(self, password):
        self.driver.find_element(*self.SIGN_IN_PASSWORD).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def sign_in(self, email, password):
        self.click_account_icon()
        self.enter_sign_in_email(email)
        self.enter_sign_in_password(password)
        self.click_sign_in_button()
