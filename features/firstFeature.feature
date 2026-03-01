Feature: validation on login page

  Background:
    Given opening browser

  @smoke
  Scenario: verifying login page with valid username and password
    When provide valid "varshith" and "123456789"
    Then verify titlle of the page

  @regression
  Scenario Outline:
    When provide valid "<username>" and "<password>"
    Then verify success message
    Examples:
      | username | password  |
      | varshi   | 123456    |
      | tony     | 456875666 |

  Scenario: Testing table formats
    When verify login using below
          | varshi   | 123456    |
          | tony     | 456875666 |
    Then verify title of the page