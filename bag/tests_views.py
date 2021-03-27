from django.test import TestCase
from products.models import Product, Category


class TestBagViews(TestCase):

    def test_view_bag(self):
        categories = Category(name="Category Name")
        categories.save()
        product_details = Product(name="Test product", price=30.00,
                                  description="Test description",
                                  image="test.jpg")
        product_details.save()
        response = self.client.get("/bag/")
        self.assertEqual(response.status_code, 200)
