Feature: testing the main application

  Scenario: test player guess checking
     Given we have a player guess and a game answer
      when we test it against the answer
      then we have the correct element count

  Scenario: removing guesses from the set
     Given I have a player guess which is not the code
      when I get the response for the number of correct and regular elements
      then I have a set with the elements that would not give this response removed
