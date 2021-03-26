from django.test import TestCase

# Create your tests here.
from django.urls import reverse, resolve
from bag.views import view_bag


class TestBagUrls(TestCase):

    def test_bag_url_resolves(self):
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)
