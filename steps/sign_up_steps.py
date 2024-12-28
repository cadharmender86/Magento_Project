from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.sign_up_page import SignUpPage
from pages.home_page import HomePage
import time

@given('I navigate to the Magento sign-up page')
def step_given_navigate_to_signup_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://magento.softwaretestingboard.com/")
    context.driver.find_element(By.LINK_TEXT, "Create an Account").click()
    context.signup_page = SignUpPage(context.driver)

@when('I create a new account with valid details')
def step_when_create_new_account(context):
    context.signup_page.create_account("Donald", "Trump", "dduunald.trump@example.com", "Test@1234")

@then('I should be able to sign in with the created account')
def step_then_sign_in(context):
    time.sleep(10)  # Wait for account creation to complete
    context.home_page = HomePage(context.driver)
    context.home_page.sign_in("dduunald.trump@example.com", "Test@1234")
    time.sleep(2)  # Wait for sign-in to complete
    assert "Welcome, Donald Trump!" in context.driver.page_source  # Change this text based on actual confirmation text
    context.driver.quit()
