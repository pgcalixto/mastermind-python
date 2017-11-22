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
        int, int: A tuple containing the number of good and regular elements in
                  the player guess.
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

def get_best_guess(unused_guesses, possible_guesses):
    """Returns best guess using Knuth's minimax algorithm.

    Apply minimax technique to find a next guess as follows:

    Being S the list of the possible guesses, the best guess will be the guess
    that can match the most codes for one good and regular combination.

    For each guess G of S and all answer A of all possible answer, there is a C
    number of possible codes. The score of the guess G is the maximum C number
    of possible codes that G can have.

    The best guess will be the guess G with the minimum score.

    Args:
        possible_guesses (list): Current possible guesses.

    Returns:
        str: The best guess to play next.
    """

    n_guesses = len(possible_guesses)
    best_guesses = []
    best_score = 0

    for guess in unused_guesses:

        code_matches = {}
        for code in possible_guesses:

            answer = check_answer(code, guess)
            if answer not in code_matches:
                code_matches[answer] = 1
            else:
                code_matches[answer] += 1

        # the guess score is the maximum number of code matches it can have
        guess_score = min([n_guesses - x for x in code_matches.values()])

        # if the current guess score equals to the best score, includes the
        # current guess to the best guesses list
        if guess_score == best_score:
            best_guesses.append(guess)
        # otherwise, if the current guess score is greater than the best
        # score, updates the best score and the best guesses list
        elif guess_score > best_score:
            best_score = guess_score
            best_guesses = [guess]

    # uses as next guess an element of S, if possible. otherwise, select the
    # first element of the best guesses list
    best_guess = next((guess for guess in best_guesses if
                       guess in possible_guesses),
                      best_guesses[0])
    return best_guess
