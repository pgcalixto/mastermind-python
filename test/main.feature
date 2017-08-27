Feature: testing the main application

  Scenario: test player guess checking
     Given we have a player guess and a game answer
      when we test it against the answer
      then we have the correct and regular count

     Given we have a player guess with an incorrect size
      when we test it against the answer
      then it throws a WrongSizeList exception
