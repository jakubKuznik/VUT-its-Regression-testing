Feature: Content creation and editation
    Administrator or registered user who have rights can create new entitiy or editing existing one. 

    Background: 
      Given Administrator is logged in  

    # 9.
    Scenario: Creating use case 
      Given a web browser is on "Use case creation" page 
      And all required fields are filled 	
      When Administrator click on "Save" button
      Then use case is visible in "Use Cases" page 
    
    # 10.
    Scenario: Creating Evaluation scenario 
      Given a web browser is on "Evaluation scenario creation" page 
      And all required fields are filled 	
      When Administrator click on "Save" button
      Then Evaluation scenario is visible in "Evaluation scenario page"

    # 11.
    Scenario: Delete Tool
      Given tool is created
      Given a web browser is on "Tools" page 
      And tool "checkbox" is selected 
      When Administrator click on "Delete" button (trash bin) 
      Then Tool is not visible in "Tools page"
    
    # 12. Method name editation 
    Scenario: Method editation
      Given Method is created
      Given a web browser is on "method editation" page
      And Name textbox is changet to new one 
      When Administrator click on "save" button 
      Then Method page with new name is presented 

    # 13. Test case id editation # in relations test we check if all the relations stay after id change 
    Scenario: Test case editation 
      Given test is created
      Given a web browser is on "test case editation" page
      And "Test Case id" is changed to new one  
      When Administrator click on "save" button 
      Then Method page with same name and new id is created  
   
    # 14.
    Scenario: Create Evaluation Performance Indicator
      Given use case is created 
      Given a web browser is on "Edit Use Case" page
      And a web browser is at section "VALU3S Framework" 
      Given in "Evaluation Performance Indicator" "V&V process criteria" is chosen
      When Administrator click on "Save" button
      Then use case page is presented
      And "V&V process criteria" is pre in "Evaluation Performance Indicator"


    # 15. ## probably fail, becouse there is no option for workflow creation 
    Scenario: Workflow creation
	    Given a web browser is on "home page"
	    When administrator click on "Add new... Workflow"
	    Then Workflow edit page is presented 


