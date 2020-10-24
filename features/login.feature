Feature: Validate the login feature

  Background:
    Given Launch the browser
    When Open the https://opensource-demo.orangehrmlive.com/ website
    Then The login portal has been opened

  @valid_login
  Scenario: Login with valid credentials
    And Provide the username "Admin" and password "admin123"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Close the browser

  Scenario Outline: Login with invalid credentials
    And Provide the username "<username>" and password "<password> "
    And Click on the Login button
    Then Login is failed and invlid credential error is displayed
    Then Close the browser
    Examples:
      | username | password |
      | abcd     | 1234     |
      | 35473    | afsdf    |

  Scenario: Login with emmpty username
    And Provide the password "admin123"
    And Click on the Login button
    Then Login is failed and empty username error is displayed
    Then Close the browser

  Scenario: Login with empty password
    And Provide the username "Admin"
    And Click on the Login button
    Then Login is failed and empty password error is displayed
    Then Close the browser