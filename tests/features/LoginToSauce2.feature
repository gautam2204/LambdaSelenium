@account

Feature: Login page 0

  Scenario: Valid login 1
    Given Home page is opened
    When User enters credentials
    And User clicks Login button
    Then User lands on Account Home Page

  Scenario: Invalid login assert 2
    Given Home page is opened
    When User enters credentials
    And User clicks Login button
    Then User lands on Account Home Page incorrect validation

  Scenario: Valid login 2
    Given Home page is opened
    When User enters credentials
    And User clicks Login button
    Then User lands on Account Home Page

  Scenario: Valid login 3
    Given Home page is opened
    When User enters credentials
    And User clicks Login button
    Then User lands on Account Home Page