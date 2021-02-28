from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from bag.views import (view_bag, add_wine_to_bag, add_subscription_to_bag,
                       adjust_wine_in_bag, adjust_subscription_in_bag,
                       remove_wine_from_bag, remove_subscription_from_bag)


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

    def test_adjust_wine_in_bag_url_resolves(self):
        url = reverse('adjust_wine_in_bag')
        self.assertEquals(resolve(url).func, adjust_wine_in_bag)

    def test_adjust_subscription_in_bag_url_resolves(self):
        url = reverse('adjust_subscription_in_bag')
        self.assertEquals(resolve(url).func, adjust_subscription_in_bag)

    def test_remove_wine_from_bag_url_resolves(self):
        url = reverse('remove_wine_from_bag')
        self.assertEquals(resolve(url).func, remove_wine_from_bag)

    def test_remove_subscription_from_bag_url_resolves(self):
        url = reverse('remove_subscription_from_bag')
        self.assertEquals(resolve(url).func, remove_subscription_from_bag)
