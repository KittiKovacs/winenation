from django.test import TestCase
from django.urls import reverse, resolve
from profiles.views import profile, order_history


class TestProfilesUrls(TestCase):

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_order_history_url_resolves(self):
        url = reverse('order_history', args=['1'])
        self.assertEquals(resolve(url).func, order_history)
