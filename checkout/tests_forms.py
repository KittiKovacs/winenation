from django.test import TestCase
from .forms import OrderForm

# Create your tests here.


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):
        form = OrderForm({
            'full_name': 'Jane Test',
            'email': 'JaneTest@gmail.com',
            'phone_number': '00445698754',
            'street_address1': '1 Street test',
            'street_address2': 'District 9',
            'town_or_city': 'Testville',
            'country': 'US',
            'county': 'Madison'})
        self.assertTrue(form.is_valid())
