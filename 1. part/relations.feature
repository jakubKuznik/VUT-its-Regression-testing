Feature: Relationships creation and editation
    Entities have relationships with other entites, we can create and change these relationship.

    Background: 
      Given Administrator is logged in  
    
    # 16.
    Scenario: New relation between use case and Evaluation scenario 
      Given Use case is created
      Given a Evaluation scenario is created 
      And Evaluation scenario does not have any relations
      Given a web browser is on "Edit Use Case" page
      When Administrator add created "evaluation scenario" to "Evaluation Scenarios List" 
      And Administrator click on "Save" button
      Then Evaluation scenario is shown in Use case Evaluation Scenarios List
    
    # 17. 
    Scenario: Delete Evaluation scenario that has realation with use case  
      Given Evaluation scenario is created
      And Evaluation scenario has relation with use case
      Given a web browser is on that "evaluation scenario page"
      When Administrator click on "Actions Delete"
      Then evaluation scenario is not present in use case "Evaluation Scenarios List"
    
    # 18.
    Scenario: multiple use case relations with organizations
      Given use case is created
      And use case has no relations with any organization 
      Given two diferent organizations are created
      Given a Web browser is on "Edit Use Case" page
      And One organization is added to "Use Case Provider" list
      And Both organizations are added to "Partner" list
      When Administrator click on "Save" button
      Then use case page is presented
      And Organizations are shown in proper cathegories 

    # 19.
    Scenario: Change id of Test Case that has relation
      Given a method is created	
      And method has "Test Case or V&V" relation with "test case"
      Given a web browser is at "Edit test case" page 
      And "Test Case Id" is changed to diferent one 
      When administrator click on "Save" button
      Then method page has "Test Case or V&V" relation with "test case"  
    
    # 20.
    # check if there is cyclical dependence between V&V and Methods throught Context
    Scenario: Adding new context type
      Given method, test case are created
      And they have "Evaluation Type" "Experimental - Testing"
      Given method has relation with test case 
      Given a web browser is on test case "Edit page"
      And "Experimental - Monitoring" is added to "Evaluation Type"
      When administrator click on "Save" button
      Then method page does not have "Experimental - monitoring" in "Evaluation Type" list  
    
    # 21.
    Scenario: Deleting Evaluation from test case 
      Given test case is created
      And test case has "Evaluation Enviroment Type" set as "In-the-lab enviroment"
      Given a web browser is on "Edit test case" page
      And "In-the-lab enviroment" checbox is unmarked
      When administrator click on "Save" button
      Then test case page is presented with no Evaluation Type
    
    # 22.
    Scenario: Two requirements with same name 
      Given evaluation scenario is created
      And evaluation scenario has 2 requirements in "Evaluation Scenario Req. List"
      Given a web browser is one of these requirement "Edit page"
      And title is changed to same name as second requirement
      When administrator click on "Save" button
      Then both requirements are presented in "evaluation scenario page" in "Evaluation Scenario List" 
      And they have same name 
    
    # 23.
    Scenario: Unsuported evaluation scenario owner 
      Given method is created 
      Given a web browser is on Evaluation Scenario creation page
      And all required fields are filled 
      And "Evaluation Scenario Owner" is set to test case
      When administrator click on "Save" button
      Then Error occur OR "Evaluation Scenario Owner" is not presented



