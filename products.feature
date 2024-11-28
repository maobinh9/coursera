Feature: Product Management

  Scenario: List all products
    When I visit "/products"
    Then I should see a list of products

  Scenario: Search by name
    When I search for "Laptop" by name
    Then I should see "Laptop" in the results

  Scenario: Update a product
    Given a product with name "Laptop"
    When I update its name to "Smartphone"
    Then I should see "Smartphone" in the results

  Scenario: Delete a product
    Given a product with name "Laptop"
    When I delete the product
    Then I should not see "Laptop" in the results
