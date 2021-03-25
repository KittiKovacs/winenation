from django.test import TestCase
from .models import Product


class TestProductModels(TestCase):

    def test_product(self):
        wine = Product(name="Test Wine")
        self.assertEqual(str(wine), wine.name)
