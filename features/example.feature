Feature: Target app

  Scenario: Initial setup
    Given User starts GnuCash for the first time.
     When On the "Welcome to GnuCash" screen: User clicks "Next"
      And On the "Default Currency" screen: User clicks "Other" and clicks "Next"
      And On the "Select Currency" screen: User scrolls to "JPY - Yen" and clicks "JPY - Yen" and clicks "Next"
      And On the "Account Setup" screen: User clicks "Create default accounts" and clicks "Next"
      And On the "Feedback Options" screen: User clicks "Disable crash reports" and clicks "Next"
     Then On the "Review" screen: User should be able to see "Default Currency" as "Other..." and "Select Currency" as "JPY" and the User clicks "Done"
     When On the "What's New" dialog: User clicks "Dismiss"
     Then User should be able to see the "Accounts" screen labeled with "Accounts".
      And User should be able to see the following accounts and labels:
        | name        |
        | Assets      |
        | Equity      |
        | Expenses    |
        | Income      |
        | Liabilities |
      And User should be able to see a create account button on the bottom right of the screen
      And User should be able to see a three line hamburger menu on the top left of the screen

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!