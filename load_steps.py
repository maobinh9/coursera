from behave import given
from myapp.models import Product

@given("the following products")
def step_impl(context):
    for row in context.table:
        Product.create(name=row["name"], category=row["category"], price=float(row["price"]), availability=row["availability"] == "True")
