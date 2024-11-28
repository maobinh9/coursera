from behave import when, then

@when("I visit {endpoint}")
def step_impl(context, endpoint):
    context.response = context.client.get(endpoint)

@then("I should see a list of products")
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.json()) > 0
