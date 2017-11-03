Feature: testing the main application

  Scenario: test player guess checking
     Given we have a guess and an answer, both without repeated numbers
      when we test it against the answer
      then we have the correct element count for both lists without repeated numbers

      Given we have a guess with repeated numbers and a game answer without repeated numbers
       when we test it against the answer
       then we have the correct element count for a guess with repeated numbers

  Scenario: removing guesses from the set
     Given I have a player guess which is not the code
      when I get the response for the number of correct and regular elements
      then I have a set with the elements that would not give this response removed
