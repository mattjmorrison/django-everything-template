Feature: Restful Webservice for Person

        Scenario: Create a Person
                Given the following data
                        | name | language   |
                        | Kyle | JavaScript |
                When I 'POST' to the '/demo/person/' resource url
                Then I should get a '201' status code
                And I should get a valid json document in the response body
                And I should get a 'name' of 'Kyle' in the json document
                And I should get a 'language' of 'JavaScript' in the json document
                And I should see an 'id' field in the json document

        Scenario: Get a Person
                Given the following data
                        | name | language |
                        | Carl | Ruby     |
                When I 'POST' to the '/demo/person/' resource url
                And I 'GET' to the '/demo/person/' resource url with the 'id' from the previous response
                Then I should get a '200' status code
                And I should get a valid json document in the response body
                And I should get a 'name' of 'Carl' in the json document
                And I should get a 'language' of 'Ruby' in the json document
                And I should see an 'id' field in the json document

        Scenario: Update a Person
                Given the following data
                        | name | language |
                        | Carl | Ruby     |
                When I 'POST' to the '/demo/person/' resource url
                And I 'PUT' to the '/demo/person/' resource url with the 'id' from the previous response with the following data
                        | name | language |
                        | Carl | Python   |                
                Then I should get a '200' status code
                And I should get a valid json document in the response body
                And I should get a 'name' of 'Carl' in the json document
                And I should get a 'language' of 'Python' in the json document
                And I should see an 'id' field in the json document

        Scenario: Delete a Person
                Given the following data
                        | name | language |
                        | Carl | Ruby     |
                When I 'POST' to the '/demo/person/' resource url
                And I 'DELETE' to the '/demo/person/' resource url with the 'id' from the previous response
                Then I should get a '204' status code
                And I 'GET' to the '/demo/person/' resource url with the 'id' from the previous response
                Then I should get a '404' status code
