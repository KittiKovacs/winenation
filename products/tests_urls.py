from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (all_wines, wine_details, all_events,
                            all_subscriptions)


class TestServiceUrls(SimpleTestCase):

    def test_all_wines_url_resolves(self):
        url = reverse('wines')
        self.assertEquals(resolve(url).func, all_wines)

    def test_wine_details_url_resolves(self):
        url = reverse('wine_details', args=('1'))
        self.assertEquals(resolve(url).func, wine_details)

    def test_all_events_url_resolves(self):
        url = reverse('events')
        self.assertEquals(resolve(url).func, all_events)

    def test_all_subscriptions_url_resolves(self):
        url = reverse('subscriptions')
        self.assertEquals(resolve(url).func, all_subscriptions)
