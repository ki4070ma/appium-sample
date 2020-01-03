from behave import given, when, then, step


@given('User starts GnuCash for the first time.')
def step_impl(context):
    pass


@when('On the {screen} screen: User clicks {button}')
def step_impl(context):
    pass


@when('On the {screen} screen: User clicks {item} and clicks {button}')
def step_impl(context):
    pass


@when('On the {screen} screen: User scrolls to {item} and clicks {item} and clicks {button}')
def step_impl(context):
    pass


@when('On the {screen} screen: User scrolls to {item} and clicks {item} and clicks {button}')
def step_impl(context):
    pass


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number


@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
