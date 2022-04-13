Feature: Content creation and editation
  Administrator or registered user who have rights can create new entities or editing existing once. 
  Entities have relationships with each other, we can also change and create these relationship.

  Background: Administrator is logged in  

  Scenario: Creating Use case 
    Given a web browse is at "Add Use case" page 
    And all required fields are filled 	
    When administrator click on "Save" button
    Then Use case page is visible in "Use Cases" page 

  Scenario: New relation between Use case and Evaluation scenario 
    Given Use case is created
    Given a Evaluation scenario is created 
    When administrator click "Add new... Use Case" button.
    Then "Add Use Case" page is shown


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















