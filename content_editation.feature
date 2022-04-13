Feature: Content creation and editation
    Administrator or registered user who have rights can create new entities or editing existing once. 
    Entities have relationships with each other, we can also change and create these relationship.

    Background: Administrator is logged in  

    Scenario: Creating use case 
      Given a web browser is at "Use case creation" page 
      And all required fields are filled 	
      When Administrator click on "Save" button
      Then use case is visible in "Use Cases" page 

    Scenario: New relation between use case and Evaluation scenario 
      Given Use case is created
      Given a Evaluation scenario is created 
      And Evaluation scenario does not have any relations
      Given web browser is at "Edit Use Case" page
      When Administrator add created evaluation scenario to Evaluation Scenarios List 
      And Administrator click on "Save" button
      Then Evaluation scenario is shown in Use case Evaluation Scenarios List 
   
    Scenario: Delete Evaluation scenario that has realation with use case  
      Given Evaluation scenario is created
      And Evaluation scenario has relation with use case
      Given Web browser is on That evaluation scenario page
      When Administrator click on "Actions Delete"
      Then evaluation scenario is not present in use case "Evaluation Scenarios List" 

    Scenario: Create Evaluation Performance Indicator  
      Given use case is created 
      Given Web browser is at "Edit Use Case" page
      And Web browser is at section "VALU3S Framework" 
      Given in "Evaluation Performance Indicator" "V&V process criteria" is chosen
      When Administrator click on "Save" button
      Then use case page is presented
      And "V&V process criteria" is pre in "Evaluation Performance Indicator"

    Scenario: Use case relations with organization
      Given use case is created
      And use case has no relations with any organization 
      Given two diferent organizations are created
      Given Web browser is at "Edit Use Case" page
      And One organization is added to "Use Case Provider"
      And Both organizations are added to "Partner"
      When Administrator click on "Save" button
      Then use case page is presented
      And Organizations are shown in proper cathegories 


#create new standart assign it to use case 


# create organization map it to use case 

# create organization ## map it to use case # delete organization

# u have use case that has relation with evaluation scenario, 
# change use case name 

# use case has standart 
# change standart number 

## use case has relation with one evaluation scenario add another 

## standart has use case add another there 















