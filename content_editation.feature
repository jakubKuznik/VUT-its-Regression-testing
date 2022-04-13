Feature: Content creation and editation
    Administrator or registered user who have rights can create new entitiy or editing existing one. 
    Entities have relationships with each other, we can also change and create these relationship.

    Background: 
      Given Administrator is logged in  

    # 9.
    Scenario: Creating use case 
      Given a web browser is on "Use case creation" page 
      And all required fields are filled 	
      When Administrator click on "Save" button
      Then use case is visible in "Use Cases" page 
    
    # 10.
    Scenario: New relation between use case and Evaluation scenario 
      Given Use case is created
      Given a Evaluation scenario is created 
      And Evaluation scenario does not have any relations
      Given web browser is on "Edit Use Case" page
      When Administrator add created "evaluation scenario" to "Evaluation Scenarios List" 
      And Administrator click on "Save" button
      Then Evaluation scenario is shown in Use case Evaluation Scenarios List

    # 11. 
    Scenario: Delete Evaluation scenario that has realation with use case  
      Given Evaluation scenario is created
      And Evaluation scenario has relation with use case
      Given Web browser is on that "evaluation scenario page"
      When Administrator click on "Actions Delete"
      Then evaluation scenario is not present in use case "Evaluation Scenarios List"

    # 12.
    Scenario: multiple use case relations with organizations
      Given use case is created
      And use case has no relations with any organization 
      Given two diferent organizations are created
      Given Web browser is on "Edit Use Case" page
      And One organization is added to "Use Case Provider" list
      And Both organizations are added to "Partner" list
      When Administrator click on "Save" button
      Then use case page is presented
      And Organizations are shown in proper cathegories 

    # 13.
    Scenario: Create Evaluation Performance Indicator
      Given use case is created 
      Given web browser is on "Edit Use Case" page
      And web browser is at section "VALU3S Framework" 
      Given in "Evaluation Performance Indicator" "V&V process criteria" is chosen
      When Administrator click on "Save" button
      Then use case page is presented
      And "V&V process criteria" is pre in "Evaluation Performance Indicator"

    # 14.
    Scenario: Change id of Test Case that has relation
      Given a method is created	
      And  method has "Test Case or V&V" relation with "test case"
      Given web browser is at "Edit test case" page 
      And "Test Case Id" is changed to diferent one 
      When administrator click on "Save" button
      Then method page has "Test Case or V&V" relation with "test case"  

    # 15.
    # check if there is cyclical dependence between V&V and Methods throught Context
    Scenario: Adding new context type
      Given method, test case are created
      And they have "Evaluation Type" "Experimental - Testing"
      Given method has relation with test case 
      Given web browser is on test case "Edit page"
      And "Experimental - Monitoring" is added to "Evaluation Type"
      When administrator click on "Save" button
      Then method page does not have "Experimental - monitoring" in "Evaluation Type" list  

    # 16.
    Scenario: Deleting Evaluation from test case 
      Given test case is created
      And test case has "Evaluation Enviroment Type" set as "In-the-lab enviroment"
      Given web browser is on "Edit test case" page
      And "In-the-lab enviroment" checbox is unmarked
      When administrator click on "Save" button
      Then test case page is presented with no Evaluation Type













