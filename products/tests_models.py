from django.test import TestCase
from .models import Wine


class TestProductModels(TestCase):

    def test_wine_default_to_false(self):
        wine = Wine.objects.create(sku=25,
                                   name="Test wine",
                                   price=65,
                                   image="vineyard.jpg",
                                   winery="Ikon",
                                   vintage=2015,
                                   alc_vol=15,
                                   pairing="beef")
        self.assertFalse(wine.vintage == 6000)
