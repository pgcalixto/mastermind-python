
from behave import given, when, then
from mastermind import main

@given('we have a player guess and a game answer')
def step_impl(context):
    context.guess = [5, 3, 2, 1]
    context.answer = [1, 2, 3, 4]

@when('we test it against the answer')
def step_impl(context):
    try:
        context.element_count = main.check_answer(context.guess, context.answer)
        context.exception = None
    except Exception as e:
        context.exception = e

@then('we have the correct and regular count')
def step_impl(context):
    assert context.element_count == (0, 3)

@given('we have a player guess with an incorrect size')
def step_impl(context):
    context.guess = [5, 3, 2]
    context.answer = [1, 2, 3, 4]

@then('it throws a WrongSizeList exception')
def step_impl(context):
    assert isinstance(context.exception, main.WrongSizeList)
