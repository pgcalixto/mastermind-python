#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Mastermind game

This module is responsible for being a Mastermind game solver.
"""

def check_answer(code, guess):
    """Calculates good and regular elements from the player guess.

    For every element in the guess, checks if it has the same value as the
    element in the same index of the code. If it does, adds 1 to the good
    elements count. Otherwise, checks if that guess element is present in the
    code. If it is, adds 1 to the regular elements count.

    Args:
        code (str): The game code.
        guess (str): The player guess in that round.

    Returns:
        tuple: A tuple containing the number of good and the number of regular
        elements in the player guess.
    """
    good = 0
    regular = 0

    for i in range(4):
        # if guess[i] equals code[i], increments the good elements count
        if guess[i] == code[i]:
            good += 1
        # otherwise, increments the regular elements count if guess[i] is
        # present in the code
        else:
            for j in range(4):
                if guess[i] == code[j]:
                    regular += 1

    # finally, decrements the times the regular elements were incorrectly
    # counted in positions where the element was good
    regular -= good

    return (good, regular)

def delete_guesses(guesses, guess, good, regular):
    """Removes imposible guesses given the player's last guess answer.

    Added a function which has the good and regular elements answer from the
    player's current guess, and remove from the list of guesses any guess that
    would not give that answer, if the last player's guess were the code.

    Args:
        guesses (list): List of all current possible guesses.
        guess (list): Last player guess.
        good (int): Number of good elements from the player's last guess.
        regular (int): Number of regular elements from the player's last guess.

    Returns:
        list: An updated guesses list with all impossible guesses removed.
    """
    return [x for x in guesses if \
            check_answer(x, guess) != (good, regular)]
