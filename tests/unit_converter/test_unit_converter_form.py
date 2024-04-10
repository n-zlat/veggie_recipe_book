from django.test import TestCase
from django.urls import reverse
from veggie_recipe_book.unit_converter.models import MeasurementUnit


class UnitConverterFormTest(TestCase):
    def setUp(self):
        # Create measurement units for testing
        MeasurementUnit.objects.create(name='gram')
        MeasurementUnit.objects.create(name='milligram')
        MeasurementUnit.objects.create(name='liter')
        MeasurementUnit.objects.create(name='ounce')

    def test_missing_amount_returns_form_again(self):
        form_data = {'from_unit': 'liter', 'to_unit': 'ounce'}
        response = self.client.post(reverse('unit_converter'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_missing_from_unit_returns_form_again(self):
        form_data = {'amount': '100', 'to_unit': 'ounce'}
        response = self.client.post(reverse('unit_converter'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_amount_returns_form_again(self):
        form_data = {'amount': 'little', 'from_unit': 'gram', 'to_unit': 'ounce'}
        response = self.client.post(reverse('unit_converter'), form_data)
        self.assertEqual(response.status_code, 200)
