from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    def test_create_valid_profile_form(self):
        form = UserProfileForm({
            'default_phone_number': '3698751223',
            'default_postcode': '69875',
            'default_town_or_city': 'Town',
            'default_street_address1': '1 Street ',
            'default_street_address2': '2 Street ',
            'default_county': 'County'})
        self.assertTrue(form.is_valid())
