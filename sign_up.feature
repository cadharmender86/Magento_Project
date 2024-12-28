Feature: Sign up and sign in on the Magento website

  Scenario: Create an account and sign in successfully
    Given I navigate to the Magento sign-up page
    When I create a new account with valid details
    Then I should be able to sign in with the created account
