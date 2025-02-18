Feature: User permissions

  Scenario Outline: User can see and preview public documents

    Given the following documents:
      | title                           | visibility  | case_id |
      | A study in bats                 | public      |       1 |
      | Igorville Park assessment       | private     |       2 |
      | Igorville Park restoration plan | private     |       3 |
    And I am logged in as <user type>
    And I am assigned to <case>
    When I search for "bats"
    Then I can see "bats" in search results
    Then I can preview "bats" in search previews

      Examples:
        | user type                     | case_ids |
        | guest user                    |          |
        | superuser                     |          |
        | staff                         | 1        |
        | staff                         |          |
        | Technical Support Group (TSG) |          |
        | FWS Regional Coordinator (RC) |          |


  Scenario: Guest user sees only public documents

    Given the following documents:
      | title                           | visibility  | case_id |
      | A study in bats                 | public      |       1 |
      | Igorville Park assessment       | private     |       2 |
      | Igorville Park restoration plan | private     |       3 |
    And I am a guest user
    When I search for "Igorville"
    Then I cannot see "Igorville" in search results
    And I cannot preview "Igorville" in search previews
    And I do not see private previews


  Scenario: Superuser sees all documents

    Given the following documents:
      | title                           | visibility  | case_id |
      | A study in bats                 | public      |       1 |
      | Igorville Park assessment       | private     |       2 |
      | Igorville Park restoration plan | private     |       3 |
    And I am logged in as a superuser
    When I search for "Igorville"
    Then I can see "Igorville" in search results
    And I can preview "Igorville" in search previews
    And I do not see private previews


  Scenario: Staff can see public documents and private documents on their cases

    Given the following documents:
      | title                           | visibility  | case_id |
      | A study in bats                 | public      |       1 |
      | Igorville Park assessment       | private     |       2 |
      | Igorville Park restoration plan | private     |       3 |
    And I am logged in as staff
    And I am assigned to case 2
    When I search for "Igorville"
    Then I can see "Igorville Park assessment" in search results
    And I see "A study in bats" in search results
    And I cannot see "Igorville Park restoration plan" in search results
    And I see one private preview


  Scenario: Technical support group can see all documents

    Given the following documents:
      | title                           | visibility  | case_id |
      | A study in bats                 | public      |       1 |
      | Igorville Park assessment       | private     |       2 |
      | Igorville Park restoration plan | private     |       3 |
    And I am logged in as Technical Support Group
    When I search for "Igorville"
    Then I can see "Igorville" in 2 search results
    And I see "A study in bats" in search results
    And I do not see private previews


  Scenario: FWS Regional Coordinator see all documents in region

    Given the following documents:
      | title                           | visibility  | case_id | case_region |
      | A study in bats                 | public      |       1 |           6 |
      | Igorville Park assessment       | private     |       2 |           7 |
      | Igorville Park restoration plan | private     |       3 |           8 |
    And I am logged in as Technical Support Group
    And I am assigned to Region 7
    When I search for "Igorville"
    Then I can see "Igorville Park assessment" in search results
    And I see "A study in bats" in search results
    And I cannot see "Igorville Park restoration plan" in search results
    And I see one private preview

