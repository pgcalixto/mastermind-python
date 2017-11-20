from behave import given, when, then
from mastermind import main

@given('we have a guess and an answer, both without repeated numbers')
def step_impl(context):
    context.guess = '5321'
    context.answer = '1234'

@when('we test it against the answer')
def step_impl(context):
    context.element_count = main.check_answer(context.guess, context.answer)

@then('we have the correct element count for both lists without repeated numbers')
def step_impl(context):
    assert context.element_count == (0, 3)

@given('we have a guess with repeated numbers and a game answer without repeated numbers')
def step_impl(context):
    context.guess = '1321'
    context.answer = '1234'

@then('we have the correct element count for a guess with repeated numbers')
def step_impl(context):
    assert context.element_count == (1, 2)

@given('we have a guess and an answer, both with repeated numbers')
def step_impl(context):
    context.guess = '1121'
    context.answer = '1241'

@then('we have the correct element count for bot list with repeated numbers')
def step_impl(context):
    assert context.element_count == (2, 1)
