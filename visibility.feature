Feature: Content visibility

  Background:
    Given a Administrator is logged in 

  ## bacis visibility
  Scenario: switch on Use case visibility
    Given a use case is created with no "sharing rights" 
    Given a web browse is at the use case "sharing page"
    When administrator click "Can view" checkbox", after that "Save" button
    Then administrator should see table: 
      | Logged-in users | Can add | Can edit | Can review | Can view |
      |   	        |   ✓     |          |            |          | 

  Scenario Outline: switch off Use case visibility
    Given a use case is created with only "Logged-in user"
    Given a web browse is at the use case "sharing page"
    When administrator click "Can view" checkbox, after that "Save" button 
    Then User "itsreviewer" cannot see this new "use case" in the "Use Cases cathegory"

  ## bacis visibility
  Scenario: switch on Use case visibility
    Given a use case is created with no "sharing rights" 
    Given a web browse is at the use case "sharing page"
    When administrator click "Can view" checkbox", after that "Save" button
    Then administrator should see table: 
    Then User "itsreviewer" can see this new use case in the Use Cases cathegory



  ## basic edit
  # I think there is an error 
  Scenario: Changing tool edit ability
    Given a web browse is at the method "sharing page"
    Given a test tool is create "everyone" can view it
    When administrator click "Can edit" checkbox, after that "Save" button
    Then User "itsreviewer" can edit tool name


  ## advanced edit with relations 
  Scenario: Changing Method edit ability
    Given a web browse is at the method "sharing page"
    Given a test method is created "everyone" can view it
    Given a test tool is create "everyone" can view it
    Given a test method has "Tools relation" with tool
    When administrator click "Can edit" checkbox, after that "Save" button
    Then User "itsreviewer" cannot edit tool name

  Scenario: 
    Given: 

















