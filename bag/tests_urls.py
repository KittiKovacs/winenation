from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from bag.views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagUrls(TestCase):

    def test_bag_url_resolves(self):
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)

    def test_add_url_resolves(self):
        url = reverse('add_to_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, add_to_bag)

    def test_adjust_url_resolves(self):
        url = reverse('adjust_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, adjust_bag)

    def test_remove_url_resolves(self):
        url = reverse('remove_from_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, remove_from_bag)
