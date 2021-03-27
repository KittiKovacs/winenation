from django.test import TestCase
from .models import Product


class TestProductModels(TestCase):

    def test_product_is_a_wine(self):
        wine = Product.objects.create(name="Test wine",
                                      sku="10001",
                                      winery="Test winery",
                                      country="Testland",
                                      alc_vol="12.5",
                                      description="Test description",
                                      price=9.99,
                                      is_a_subscription=False)
        self.assertFalse(wine.is_a_subscription)

    def test_product_is_a_subscription(self):
        subscription = Product.objects.create(name="Test subscription",
                                              sku="10002",
                                              description="Test description",
                                              price=9.99,
                                              is_a_subscription=True)
        self.assertTrue(subscription.is_a_subscription)
