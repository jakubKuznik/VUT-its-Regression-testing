Feature: Content sharing changes
  In default only Administrator can view or edit elements, but we can give this right to logged users.
  Visitor can only see published entites. 

  ## note:
  # administrator     - administrator account 
  # reg_user          - registred user 
  # user 	      - page visitor 

  ## basic visibility - switch off
  Scenario: switch off Use case visibility
    Given a web browser is at the use case "sharing page"
    Given a use case is created with only "Logged-in user can view" option
    Given a Administrator is logged in 
    When Administrator click "Can view" checkbox.
    And Administrator click "Save" button 
    Then reg_user can not see this "use case" in the "Use Cases cathegory"

  ## bacis visibility - switch on
  Scenario: switch on Use case visibility
    Given a web browser is at the use case "sharing page"
    Given a use case is created with no "sharing rights" 
    Given a Administrator is logged in 
    When Administrator click "Can view checkbox"
    And Administrator click on "Save" button
    Then reg_user can see this "use case" in the "Use Cases cathegory"

  ## basic edit
  Scenario: Editing relation 
    Given a Tool is created with "Logged-in user can view and edit" sharing right
    Given User reg_user is logged in
    Given a web browser is at "tool editing page"
    When reg_user "change name" of Tool to new one 
    And reg_user click on "save" button
    Then Page with new "tool" name is presented to reg_user

  ## basic edit with sharing change
  Scenario: Changing tool edit ability
    Given a web browser is at the method "sharing page"
    Given a test tool is create with "Logged-in user can view it" sharing right
    Given a Administrator is logged in 
    When Administrator click "Can edit" checkbox
    And Administrator click "Save" button 
    Then reg_user can edit tool name

  ## advanced edit with relations
  Scenario: Changing Method edit ability
    Given a web browser is at the method "sharing page"
    Given a test method is created with "Logged-in user can view it" sharing right
    Given a test tool is create with "Logged-in user can view it" sharing right
    Given a test "method" has "Tools relation" with "tool"
    Given a Administrator is logged in 
    When Administrator click "Can edit" checkbox
    And Administrator click on "Save" button
    Then reg_user cannot edit tool name
    
  ## Add access right
  Scenario: Adding use case  
    Given a web browser is at the Use Cases page 
    Given a Use Cases has "Logged-in user can add" access right
    Given a reg_user is logged in 
    When If there is "Add new.." button then clik on it
    Then to reg_user is shown:
	    | Add new..|
	    | Folder   |
            | Use Case |
	    | More...  |

  ## Add access right advanced
  Scenario: Adding use case 
    Given a web browser is at the Use Cases page 
    Given a Use Cases has "Logged-in user can add" access right
    Given a reg_user is logged in 
    When If there is "Add new.. Use Case" button then click on it
    And Fill all required fields 
    And click "save" button 
    Then to reg_user is shown his Use case page 

  ## Public state 
  Scenario: Public Use Case
    Given a web browser is at the existing use case page
    Given use case state is private 
    Given Administrator is logged in 
    When Administrator click on "Publish" option from "State" menu
    Then User see use case in Use Cases cathegory page 

  ## Private state  
  Scenario: Hide Use Case from public
    Given a web browser is at the existing use case page
    Given use case state is public  
    Given Administrator is logged in 
    When Administrator click on "Send back" option from "State" menu
    Then "Use case" is not shown to User in "Use Cases page"  












