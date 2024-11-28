import factory
from factory.fuzzy import FuzzyChoice
from faker import Faker
from myapp.models import Product

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.unique.word())
    category = FuzzyChoice(["Electronics", "Clothing", "Food", "Books"])
    price = factory.LazyAttribute(lambda _: round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2))
    availability = FuzzyChoice([True, False])
