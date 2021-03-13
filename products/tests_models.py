from django.test import TestCase
from .models import Product


class TestProductModels(TestCase):

    def test_product(self):
        product = Product.objects.create(sku=25,
                                   name="Test wine",
                                   price=65,
                                   image="vineyard.jpg",
                                   winery="Ikon",
                                   vintage=2015,
                                   alc_vol=15,
                                   pairing="beef")
