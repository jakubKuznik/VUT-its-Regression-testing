Feature: Content creation and editation
  Administrator or registered user who have rights can create new entities or editing existing once. 
  Entities have relationships with each other, we can also change and create these relationship.

  Background: Administrator is logged in  

  Scenario: Creating Use case 
    Given a web browser is at "Use case creation" page 
    And all required fields are filled 	
    When Administrator click on "Save" button
    Then Use case page is visible in "Use Cases" page 

  Scenario: New relation between Use case and Evaluation scenario 
    Given Use case is created
    Given a Evaluation scenario is created 
    And Evaluation scenario does not have any relations
    Given web browser is at "Edit Use Case" page
    When Administrator add created evaluation scenario to Evaluation Scenarios List 
    And Administrator click on "Save" button
    Then Evaluation scenario is shown in Use case Evaluation Scenarios List 
   
   Scenario: Delete Evaluation scenario that has realations Warning test  
     Given Evaluation scenario is created
     And Evaluation scenario has relation with use case
     Given Web browser is on That evaluation scenario page
     When Administrator click on "Actions Delete"
     Then Warning form is presented with "Potential link Breakage" message
	
  Scenario: Delete Evaluation scenario that has realations  
     Given Evaluation scenario is created
     And Evaluation scenario has relation with use case
     Given Web browser is on That evaluation scenario page
     When Administrator click on "Actions Delete"
     Then Warning form is presented with "Potential link Breakage" message

# u have use case that is maped to evaluation scenario 
#  change it to difrent one 

#create new standart assign it to use case 


# create organization map it to use case 

# create organization ## map it to use case # delete organization

# u have use case that has relation with evaluation scenario, 
# change use case name 

# use case has standart 
# change standart number 

## use case has relation with one evaluation scenario add another 

## standart has use case add another there 















