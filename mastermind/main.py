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
        elif guess[i] in code:
            regular += 1

    return (good, regular)

def get_possible_guesses(guesses, guess, answer):
    """Retrieves possible codes given a game guess and its answer.

    Given a game guess and its good and regular elements answer, retrieves all
    the codes that would match this answer for that guess.

    Args:
        guesses (list): List of all guesses to be chosen from.
        guess (str): Player guess.
        answer (int, int): Number of good and regular elements when the guess is
                           played against the code.

    Returns:
        list: A list with all possible guesses.
    """
    return [code for code in guesses if check_answer(code, guess) != answer]
