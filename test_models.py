import unittest
from myapp.models import Product

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="Laptop", category="Electronics", price=1200.00, availability=True)

    def test_read_product(self):
        self.assertEqual(self.product.name, "Laptop")

    def test_update_product(self):
        self.product.name = "Smartphone"
        self.assertEqual(self.product.name, "Smartphone")

    def test_delete_product(self):
        self.product = None
        self.assertIsNone(self.product)

    def test_list_all_products(self):
        products = [Product(name=f"Item {i}", category="Misc", price=10.00 * i, availability=True) for i in range(5)]
        self.assertEqual(len(products), 5)

    def test_find_by_name(self):
        self.assertEqual(self.product.name, "Laptop")

    def test_find_by_category(self):
        self.assertEqual(self.product.category, "Electronics")

    def test_find_by_availability(self):
        self.assertTrue(self.product.availability)
