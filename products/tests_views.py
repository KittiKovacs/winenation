from django.test import TestCase
from .models import Wine


class TestProductViews(TestCase):
    def test_all_wines_page(self):
        response = self.client.get('/products/wines')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/wines.html')

    def test_wine_details_page(self):
        wine_details = Wine(name="Test wine", price=999.00,
                            sku=1,
                            winery="test", description="Test wine description")
        wine_details.save()

        response = self.client.get("/products/wines")
        self.assertEqual(response.status_code, 200)

    def test_all_subscriptions_page(self):
        response = self.client.get('/products/subscriptions')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/subscriptions.html')
