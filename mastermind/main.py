
def check_answer(guess, answer):

    """Calculates correct and answer elements from the player guess.

    For every element in the guess, checks if it has the same value as the
    element in the same index of the answer. If it does, adds 1 to the correct
    elements count. Otherwise, checks if that guess element is present in the
    answer. If it is, adds 1 to the regular elements count.

    Args:
        guess: The player guess in that round.
        answer: The final answer to the game.

    Returns:
        A tuple containing the number of correct and the number of regular
        elements in the player guess.

    Raises:
        WrongSizeList: An error occurred when the guess or answer list has a
        size different than 4.
    """
    correct = 0
    regular = 0

    if len(guess) != 4 or len(answer) != 4:
        raise WrongSizeList("Guess/answer has size different than 4.")

    for element in enumerate(guess):
        index = element[0]
        value = element[1]
        if value == answer[index]:
            correct += 1
        elif value in answer:
            regular += 1

    return (correct, regular)


class WrongSizeList(Exception):
    """Raised when the guess or answer list has a size different than 4"""
    pass
