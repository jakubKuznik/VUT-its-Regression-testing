Feature: Content editation

## creation  - adding, change, deletion
## editation - adding, change, deletion 
Scenario: Changing Use case visibility
  Given a web browse is at use case sharing page
  Given a Administrator is logged in
  Given a use case 
  When administrator click "Can view" checkbox, after that "Save" button 
  Then User can see this new use case in the Use Cases cathegory
