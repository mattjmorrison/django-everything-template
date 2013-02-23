Feature: Index

        Scenario: Template Tag
                Given I am on the url '/demo/'
		When I get look at the 'number' field
		Then I should see '8'