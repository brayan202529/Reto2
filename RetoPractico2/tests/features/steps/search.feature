Feature: Amazon Cart
Scenario: Add a product to the cart
Given I am on the Amazon homepage
When I search for "mouse"
And I select the first product
And I add the product to the cart
Then I see the product in the cart