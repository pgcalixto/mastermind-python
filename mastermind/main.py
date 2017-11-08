#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Mastermind game

This module is responsible for being a Mastermind game solver.
"""

def check_answer(guess, answer):
    """Calculates correct and answer elements from the player guess.

    For every element in the guess, checks if it has the same value as the
    element in the same index of the answer. If it does, adds 1 to the correct
    elements count. Otherwise, checks if that guess element is present in the
    answer. If it is, adds 1 to the regular elements count.

    Args:
        guess (str): The player guess in that round.
        answer (str): The game answer / game code.

    Returns:
        tuple: A tuple containing the number of good and the number of regular
        elements in the player guess.
    """
    good = 0
    regular = 0

    for i in range(4):
        # if guess[i] equals answer[i], increments the good elements count
        if guess[i] == answer[i]:
            good += 1
        # otherwise, increments the regular counts by the number of times
        # guess[i] is present in the answer
        else:
            for j in range(4):
                if guess[i] == answer[j]:
                    regular += 1

    # finally, decrements the times the regular elements were incorrectly
    # counted in positions where the element was good
    regular -= good

    return (good, regular)

def delete_guesses(guesses, guess, correct, regular):
    """Removes imposible guesses given the player's last guess response.

    Added a function which has the correct and regular elements response from
    the player's current guess, and remove from the list of guesses any guess
    that would not give that response, if the last player's guess were the
    answer.

    Args:
        guesses (list): List of all current possible guesses.
        guess (list): Last player guess.
        correct (int): Number of correct elements from the player's last guess.
        regular (int): Number of regular elements from the player's last guess.

    Returns:
        list: An updated guesses list with all impossible guesses removed.
    """
    return [x for x in guesses if \
            check_answer(x, guess) != (correct, regular)]
