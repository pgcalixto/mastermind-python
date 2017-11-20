Feature: answer checking

  Scenario: test player guess checking
     Given we have a guess and an answer, both without repeated numbers
      when we test it against the answer
      then we have the correct element count for both lists without repeated numbers

     Given we have a guess with repeated numbers and a game answer without repeated numbers
      when we test it against the answer
      then we have the correct element count for a guess with repeated numbers

     Given we have a guess and an answer, both with repeated numbers
      when we test it against the answer
      then we have the correct element count for bot list with repeated numbers
