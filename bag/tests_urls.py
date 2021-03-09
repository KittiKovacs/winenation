from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from bag.views import (view_bag, add_wine_to_bag, add_subscription_to_bag)


class TestBagUrls(TestCase):

    def test_bag_url_resolves(self):
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)

    def test_add_wine_to_bag_url_resolves(self):
        url = reverse('add_wine_to_bag')
        self.assertEquals(resolve(url).func, add_wine_to_bag)

    def test_add_subscription_to_bag_url_resolves(self):
        url = reverse('add_subscription_to_bag')
        self.assertEquals(resolve(url).func, add_subscription_to_bag)
