
from behave import given, when, then
from mastermind import main
from itertools import permutations

@given('we have a player guess and a game answer')
def step_impl(context):
    context.guess = [5, 3, 2, 1]
    context.answer = [1, 2, 3, 4]

@when('we test it against the answer')
def step_impl(context):
    context.element_count = main.check_answer(context.guess, context.answer)

@then('we have the correct and regular count')
def step_impl(context):
    assert context.element_count == (0, 3)

@given('I have a player guess which is not the code')
def step_impl(context):
    context.all_guesses = [list(p) for p in permutations(range(1, 7), 4)]
    context.guess = [5, 3, 2, 1]
    context.answer = [1, 2, 3, 4]

@when('I get the response for the number of correct and regular elements')
def step_impl(context):
    context.correct, context.regular = main.check_answer(context.guess, context.answer)

@then('I have a set with the elements that would not give this response removed')
def step_impl(context):

    new_guesses = [[1, 2, 3, 5], [1, 2, 4, 6], [1, 2, 5, 3], [1, 2, 6, 4],
                   [1, 3, 2, 4], [1, 3, 2, 5], [1, 3, 2, 6], [1, 3, 4, 2],
                   [1, 3, 4, 5], [1, 3, 4, 6], [1, 3, 5, 2], [1, 3, 5, 4],
                   [1, 3, 5, 6], [1, 3, 6, 2], [1, 3, 6, 4], [1, 3, 6, 5],
                   [1, 4, 2, 3], [1, 4, 2, 5], [1, 4, 2, 6], [1, 4, 3, 6],
                   [1, 4, 5, 6], [1, 4, 6, 2], [1, 4, 6, 3], [1, 4, 6, 5],
                   [1, 5, 2, 3], [1, 5, 2, 4], [1, 5, 2, 6], [1, 5, 3, 2],
                   [1, 5, 4, 6], [1, 5, 6, 4], [1, 6, 2, 3], [1, 6, 2, 4],
                   [1, 6, 2, 5], [1, 6, 3, 4], [1, 6, 4, 2], [1, 6, 4, 3],
                   [1, 6, 4, 5], [1, 6, 5, 4], [2, 1, 3, 5], [2, 1, 4, 6],
                   [2, 1, 5, 3], [2, 1, 6, 4], [2, 3, 1, 4], [2, 3, 1, 5],
                   [2, 3, 1, 6], [2, 3, 4, 1], [2, 3, 4, 5], [2, 3, 4, 6],
                   [2, 3, 5, 1], [2, 3, 5, 4], [2, 3, 5, 6], [2, 3, 6, 1],
                   [2, 3, 6, 4], [2, 3, 6, 5], [2, 4, 1, 6], [2, 4, 3, 1],
                   [2, 4, 3, 6], [2, 4, 5, 1], [2, 4, 5, 6], [2, 4, 6, 1],
                   [2, 4, 6, 3], [2, 4, 6, 5], [2, 5, 1, 3], [2, 5, 3, 1],
                   [2, 5, 4, 1], [2, 5, 4, 6], [2, 5, 6, 1], [2, 5, 6, 4],
                   [2, 6, 1, 4], [2, 6, 3, 1], [2, 6, 3, 4], [2, 6, 4, 1],
                   [2, 6, 4, 3], [2, 6, 4, 5], [2, 6, 5, 1], [2, 6, 5, 4],
                   [3, 1, 2, 4], [3, 1, 2, 5], [3, 1, 2, 6], [3, 1, 4, 6],
                   [3, 1, 5, 2], [3, 1, 6, 4], [3, 2, 1, 5], [3, 2, 4, 1],
                   [3, 2, 4, 6], [3, 2, 5, 1], [3, 2, 6, 1], [3, 2, 6, 4],
                   [3, 4, 1, 6], [3, 4, 2, 1], [3, 4, 2, 5], [3, 4, 2, 6],
                   [3, 4, 5, 1], [3, 4, 5, 6], [3, 4, 6, 1], [3, 4, 6, 2],
                   [3, 4, 6, 5], [3, 5, 1, 2], [3, 5, 2, 1], [3, 5, 2, 4],
                   [3, 5, 2, 6], [3, 5, 4, 1], [3, 5, 4, 6], [3, 5, 6, 1],
                   [3, 5, 6, 4], [3, 6, 1, 4], [3, 6, 2, 1], [3, 6, 2, 4],
                   [3, 6, 2, 5], [3, 6, 4, 1], [3, 6, 4, 2], [3, 6, 4, 5],
                   [3, 6, 5, 1], [3, 6, 5, 4], [4, 1, 2, 3], [4, 1, 2, 5],
                   [4, 1, 2, 6], [4, 1, 3, 6], [4, 1, 5, 6], [4, 1, 6, 2],
                   [4, 1, 6, 3], [4, 1, 6, 5], [4, 2, 1, 6], [4, 2, 3, 1],
                   [4, 2, 3, 6], [4, 2, 5, 1], [4, 2, 5, 6], [4, 2, 6, 1],
                   [4, 2, 6, 3], [4, 2, 6, 5], [4, 3, 1, 2], [4, 3, 1, 5],
                   [4, 3, 1, 6], [4, 3, 2, 1], [4, 3, 2, 5], [4, 3, 2, 6],
                   [4, 3, 5, 1], [4, 3, 5, 2], [4, 3, 5, 6], [4, 3, 6, 1],
                   [4, 3, 6, 2], [4, 3, 6, 5], [4, 5, 1, 6], [4, 5, 2, 1],
                   [4, 5, 2, 3], [4, 5, 2, 6], [4, 5, 3, 1], [4, 5, 3, 6],
                   [4, 5, 6, 1], [4, 5, 6, 2], [4, 5, 6, 3], [4, 6, 1, 2],
                   [4, 6, 1, 3], [4, 6, 1, 5], [4, 6, 2, 1], [4, 6, 2, 3],
                   [4, 6, 2, 5], [4, 6, 3, 1], [4, 6, 3, 2], [4, 6, 3, 5],
                   [4, 6, 5, 1], [4, 6, 5, 2], [4, 6, 5, 3], [5, 1, 2, 3],
                   [5, 1, 2, 4], [5, 1, 2, 6], [5, 1, 3, 2], [5, 1, 3, 4],
                   [5, 1, 3, 6], [5, 1, 4, 2], [5, 1, 4, 3], [5, 1, 4, 6],
                   [5, 1, 6, 2], [5, 1, 6, 3], [5, 1, 6, 4], [5, 2, 1, 3],
                   [5, 2, 1, 4], [5, 2, 1, 6], [5, 2, 3, 1], [5, 2, 3, 4],
                   [5, 2, 3, 6], [5, 2, 4, 1], [5, 2, 4, 3], [5, 2, 4, 6],
                   [5, 2, 6, 1], [5, 2, 6, 3], [5, 2, 6, 4], [5, 3, 1, 2],
                   [5, 3, 1, 4], [5, 3, 1, 6], [5, 3, 2, 1], [5, 3, 2, 4],
                   [5, 3, 2, 6], [5, 3, 4, 1], [5, 3, 4, 2], [5, 3, 4, 6],
                   [5, 3, 6, 1], [5, 3, 6, 2], [5, 3, 6, 4], [5, 4, 1, 2],
                   [5, 4, 1, 3], [5, 4, 1, 6], [5, 4, 2, 1], [5, 4, 2, 3],
                   [5, 4, 2, 6], [5, 4, 3, 1], [5, 4, 3, 2], [5, 4, 3, 6],
                   [5, 4, 6, 1], [5, 4, 6, 2], [5, 4, 6, 3], [5, 6, 1, 2],
                   [5, 6, 1, 3], [5, 6, 1, 4], [5, 6, 2, 1], [5, 6, 2, 3],
                   [5, 6, 2, 4], [5, 6, 3, 1], [5, 6, 3, 2], [5, 6, 3, 4],
                   [5, 6, 4, 1], [5, 6, 4, 2], [5, 6, 4, 3], [6, 1, 2, 3],
                   [6, 1, 2, 4], [6, 1, 2, 5], [6, 1, 3, 4], [6, 1, 4, 2],
                   [6, 1, 4, 3], [6, 1, 4, 5], [6, 1, 5, 4], [6, 2, 1, 4],
                   [6, 2, 3, 1], [6, 2, 3, 4], [6, 2, 4, 1], [6, 2, 4, 3],
                   [6, 2, 4, 5], [6, 2, 5, 1], [6, 2, 5, 4], [6, 3, 1, 2],
                   [6, 3, 1, 4], [6, 3, 1, 5], [6, 3, 2, 1], [6, 3, 2, 4],
                   [6, 3, 2, 5], [6, 3, 4, 1], [6, 3, 4, 2], [6, 3, 4, 5],
                   [6, 3, 5, 1], [6, 3, 5, 2], [6, 3, 5, 4], [6, 4, 1, 2],
                   [6, 4, 1, 3], [6, 4, 1, 5], [6, 4, 2, 1], [6, 4, 2, 3],
                   [6, 4, 2, 5], [6, 4, 3, 1], [6, 4, 3, 2], [6, 4, 3, 5],
                   [6, 4, 5, 1], [6, 4, 5, 2], [6, 4, 5, 3], [6, 5, 1, 4],
                   [6, 5, 2, 1], [6, 5, 2, 3], [6, 5, 2, 4], [6, 5, 3, 1],
                   [6, 5, 3, 4], [6, 5, 4, 1], [6, 5, 4, 2], [6, 5, 4, 3]]
    assert new_guesses == main.delete_guesses(context.all_guesses,
                                              context.guess, context.correct,
                                              context.regular)
