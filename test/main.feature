Feature: testing the main application

  Scenario: test player guess checking
     Given we have a player guess and a game answer
      when we test it against the answer
      then we have the correct and regular count
